# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-28 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4.jsonl`
- **Structured JSON:** [`5e1099ce5ccb9e1d5789.json`](../../sessions/5e/5e1099ce5ccb9e1d5789.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T12:39:03.656Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T12:39:03.656Z",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-28 (UTC).**\n\nYour job: independently verify this idea's claims via web_search, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: AAAI 2026\nTrack: AI Alignment / Main Technical Track — Robustness Evaluation\n\nDirection: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated \"genuine capability\" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.\n\nSeed Papers:\n- Zawalski et al. \"CoDeC\" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation\n- Li et al. \"ATLAS\" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity\n- Hou et al. \"MaSTer\" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination\n- Zheng et al. \"ReasoningMath-Plus\" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component\n- Chen et al. \"Reasoning Models Don't Always Say What They Think\" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination\n- Xu et al. \"DCR\" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis\n- Kocetkov et al. \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches\n\nKnown Gaps:\n- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)\n- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only\n- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing\n- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives\n\nTheoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)\n- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)\n- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth\n\nQuality Self-Checks:\n- [x] Core insight: \"Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level.\"\n- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.\n- [x] Baseline fear test: A simple baseline of \"run on variants and average\" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.\n- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.\n\nAvoid:\n- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)\n- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark\n- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)\n- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead**\nEvaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献\n\n6. **评分诚实**：\n   - 4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} 2026 site:scholar.google.com`\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} 2026` — 按活跃作者追踪\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey 2026` — 找综述论文\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n\n### 搜索维度\n\n1. **正向搜索**：直接搜索主题相关论文\n2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？\n3. **相邻领域搜索**：其他领域是否已解决类似问题\n4. **反面搜索**：找到反对你 idea 的证据\n5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work\n\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n2. **知名团队追踪**：搜索相关团队最近的论文\n3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`\n4. **arXiv 近 3 个月密集搜索**\n\n## Review checklist\n1. **SOTA freshness**: Are baselines actually current SOTA?\n2. **Reference verification**: Do cited papers actually exist?\n3. **Gap validity**: Does the claimed gap still exist?\n4. **Venue validity**: Are target venue deadlines after 2026-05-28?\n5. **Feasibility**: Is the resource estimate realistic?\n6. **Novelty**: Is this sufficiently different from existing work?\n7. **Cost realism**: Are the three mode estimates internally consistent?\n\n## Idea under review (round 3/10)\n{\n  \"title\": \"CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items\",\n  \"core_problem\": \"No existing framework can determine whether a model fails adversarial benchmark variants because it memorized original answers (contamination) or because it lacks genuine reasoning ability (capability deficit) — all current work observes this entanglement but none models it within a measurement-theoretic framework, preventing trustworthy LLM capability assessment.\",\n  \"opportunity\": \"Three previously siloed research streams — IRT-based LLM evaluation (PSN-IRT AAAI 2026 Oral, ATLAS, LEGO-IRT), contamination detection/correction (DCR EMNLP 2025, ConStat NeurIPS 2024, JECS arXiv May 2026), and adversarial robustness testing (MaSTer, RIDE, MATH-Perturb ICML 2025) — have each matured independently to the point where their integration is both technically feasible and urgently needed. The critical catalyst is Wang et al.'s ICLR 2026 proof that all likelihood-based contamination detection fails on reasoning models (AUROC ≈ 50%), creating demand for response-pattern-based alternatives that bypass token-probability signals entirely. A key theoretical precedent exists but has never been applied to LLMs: the Deterministic Gated IRT model (DGM; Shu, Henson & Luecht, Psychometrika 2013) decomposes test performance into genuine ability and cheating/preknowledge components conditioned on item exposure status — precisely the structure needed for LLM contamination. PSN-IRT showed IRT works for LLMs (12 models, 41,871 items, 4PL) but left contamination-adjusted scoring as an explicit open question, flagging anomalous guessing-rate parameters as contamination indicators without providing corrected ability estimates. RankLLM (ICLR 2026) demonstrated that non-parametric difficulty-aware ranking achieves 90% human alignment with only a damping hyperparameter — but provides no contamination decomposition, producing rankings without interpretable ability vs. memorization parameters. The AAAI 2027 deadline (abstracts July 21, papers July 28, 2026) is 8 weeks out. Nobody sits at the three-way intersection of IRT estimation, contamination correction, and adversarial pairing because these communities publish at different venues (ACL/EMNLP for contamination, ICLR/NeurIPS for robustness, AAAI for psychometric evaluation, Psychometrika/JEBS for test security).\",\n  \"landscape\": \"The current best contamination-to-correction pipeline is DCR (EMNLP 2025), which produces a DCR Factor via fuzzy inference across four contamination levels, achieving ~4% average error on three benchmarks — but its ad-hoc multiplicative correction Acc_adj = Acc × (1 − DCR Factor) has no measurement-theoretic justification and empirically weakens on hard tasks (r=0.66). PSN-IRT (AAAI 2026 Oral) demonstrates IRT's power for LLM evaluation using a 4PL model across 12 LLMs on 11 benchmarks (41,871 items), flagging contamination indirectly via anomalous guessing-rate parameters, but produces no contamination-adjusted ability scores; critically, PSN-IRT succeeds with only 12 models by using neural network estimation (pseudo-Siamese architecture) rather than classical MLE, establishing that neural IRT estimation is viable at small model counts. RankLLM (ICLR 2026) provides a strong non-parametric baseline: bidirectional score propagation between models and questions achieves 90% human alignment on 30 models × 35,550 questions, with remarkable stability under model removal (ρ = 0.94 even with 50% pool removed) and 0.006s convergence — but it produces difficulty-weighted rankings without any contamination modeling. RIDE (arXiv 2025) combines IRT with adversarial perturbation for math evaluation — but uses IRT only as a difficulty reward signal for RL-based question rewriting via RIDE-8B, not for joint ability-contamination estimation. JECS (arXiv May 2026) achieves formal conformal guarantees for multi-model decontamination via joint envelope conformal selection, but wastes information by binarizing items into keep/discard rather than producing continuous corrected scores. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples using a statistical comparison against reference models, but does not model it as a latent variable within a psychometric framework. In psychometrics, the DGM (Shu et al., Psychometrika 2013) uses a gated IRT formulation estimated via hierarchical MCMC to decompose examinee performance into genuine ability and item-preknowledge components — but assumes item exposure status is known a priori, which is unavailable for LLM training data. Two paired-item approaches exist but use no IRT: PaCoST (arXiv 2024) performs paired confidence significance testing for binary contamination detection, and ConStat compares primary vs. reference benchmark performance — both confirm the paired-item signal is informative but neither models it as a latent variable. For adversarial variant generation, MaSTer (arXiv 2026) provides a validated multi-round rewrite-verify pipeline (5 parallel streams × 3 iterations) achieving 45-94% target failure rates on GSM8K and MATH-500 using Qwen2.5-32B-Instruct and SymPy verification; code is claimed at github.com/sustech-nlp/MaSTer but was unavailable as of May 2026 — backup pipelines exist via MathCheck (ICLR 2025, open code) and MATH-Perturb (ICML 2025, 279 expert-crafted perturbations with open code). MathArena (NeurIPS 2025 D&B Track) has expanded to ~900 problems across 2025-2026 competitions (AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, Apex) with 50+ models, providing rich uncontaminated ground-truth rankings. Recent IRT estimation advances for small samples include Fox (2025, JEBS) demonstrating IRT-BCSM for N=50-100 by analytically integrating out person parameters, and Bayesian hierarchical priors achieving stable 2PL estimation at small sample sizes. Concurrent work search (arXiv, OpenReview, May 2026): no paper attempts joint IRT-based contamination-ability decomposition with paired adversarial items — the three-way intersection remains unoccupied.\",\n  \"inspired_by\": \"Field guide gaps: 'Contamination-aware IRT' (gap 3), 'Joint contamination-robustness decomposition' (gap 1); Innovation patterns: 'Self-Referential Measurement' (model as own control via original-vs-variant), 'Formal Guarantees on Evaluation Methodology' (identifiability proof for Gated-2PL), 'Detection-to-Correction Bridge' (from detection signals to calibrated ability scores); Key theoretical bridge: DGM (Shu et al. 2013) provides the gated IRT structure for item preknowledge estimated via hierarchical MCMC, which we extend to the LLM contamination setting where item exposure status is unknown but inferred from paired adversarial items; Untried combinations: 'DGM-style gated IRT with adversarial variant generation for LLM evaluation' (primary), 'Conformal p-values as contamination priors for gated IRT' (secondary), 'RankLLM non-parametric ranking as sanity-check baseline for IRT-corrected rankings' (tertiary)\",\n  \"approach\": \"We extend the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from the test-security domain to LLM contamination assessment, introducing the Gated-2PL (G-2PL) model as the primary framework where correct-response probability decomposes into ability-driven and contamination-driven components via a gating mechanism. The key innovation over DGM is that item exposure status is not assumed known but is identified from paired adversarial items.\\n\\n**Model specification (primary: Gated-2PL):**\\n- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i)), a standard 2PL with difficulty shift δ_i\\n- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i))\\n- θ_j = model j's genuine reasoning ability (person parameter)\\n- ξ_j ∈ [0,1] = model j's contamination exposure (person parameter)\\n- η_i ∈ [0,1] = item i's contamination susceptibility (item parameter)\\n- a_i, b_i = discrimination and difficulty (shared across original-variant pairs)\\n- δ_i = variant difficulty shift (estimated from variant calibration)\\n\\n**Rationale for G-2PL over G-3PL:** The guessing parameter c_i in 3PL requires 200+ examinees for stable estimation under classical methods, while we have only 15-20 models. Dropping c_i to use 2PL eliminates the most problematic parameter for small samples while retaining the core contamination decomposition. PSN-IRT succeeded with 12 models using neural estimation, but their 4PL worked because they had 41,871 items providing massive per-item information; our gated model adds M+K contamination parameters, making parsimony critical. For math benchmarks with open-ended answers (MATH-500, GSM8K), guessing probability is effectively zero, making 2PL substantively appropriate.\\n\\n**Ablation to Gated-3PL (G-3PL):**\\n- P(Y_{j,i*}=1 | θ_j) = c_i + (1−c_i)·σ(a_i(θ_j − b_i − δ_i))\\n- P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·[c_i + (1−c_i)·σ(a_i(θ_j − b_i))]\\n- c_i fixed to domain-specific constants: c_i = 0 for open-ended math (MATH-500, GSM8K), enabling estimation only for any future MCQ extensions.\\n\\n**Estimation strategy (fully specified):**\\nPrimary: Bayesian MCMC via NumPyro/Stan with hierarchical priors, following DGM's original estimation framework:\\n- θ_j ~ N(0, σ²_θ), σ_θ ~ Half-Cauchy(0, 2.5)\\n- ξ_j ~ Beta(α_ξ, β_ξ), with α_ξ, β_ξ ~ Gamma(2, 1) (hierarchical; allows posterior to concentrate near 0 for clean models or near 1 for heavily contaminated ones)\\n- η_i ~ Beta(α_η, β_η), with α_η, β_η ~ Gamma(2, 1) (hierarchical)\\n- a_i ~ LogNormal(0, 0.5) (positive discrimination, weakly informative)\\n- b_i ~ N(0, 1) (centered difficulty)\\n- δ_i ~ N(0, 0.5) (variant shifts expected small)\\n- MCMC: 4 chains × 2,000 warmup + 2,000 samples, NUTS sampler, R̂ < 1.05 convergence criterion\\nComparison: Neural estimation extending PSN-IRT's pseudo-Siamese architecture with an additional gating head that outputs (ξ_j, η_i) — trained via binary cross-entropy on the joint original+variant response matrix. This provides a non-Bayesian point estimate comparison.\\nAblation: Variational inference via Pyro SVI as a faster alternative to MCMC, using amortized inference for scalability testing.\\n\\n**Formal identifiability (central theoretical contribution):**\\nWe prove identifiability via a two-step argument: (1) Variant items serve as contamination-free anchors, identifying θ_j and item parameters {a_i, b_i} via standard 2PL identifiability conditions (≥2 items with heterogeneous discriminations; cf. Maris & Bechger 2009). The difficulty shift δ_i is estimated from the variant calibration. (2) Given identified θ_j and item parameters, the original-variant performance gap identifies the bilinear product ξ_j·η_i. Under the rank-1 bilinear decomposition ξ_j·η_i with M models and K items, we have M·K observed gaps constraining M+K−1 free parameters (one fixed for scale), identifiable when M·K > M+K−1, i.e., (M−1)(K−1) > 0. This holds for any M,K ≥ 2. The 2PL formulation avoids the flat-likelihood surfaces that plague 3PL/4PL estimation with few examinees, as the Fisher information matrix for the 2PL is well-conditioned even at M=15.\\n\\n**Bilinear rank-1 model adequacy plan:**\\nThe rank-1 assumption (ξ_j·η_i) treats contamination as model-global and item-global, which is a first-order approximation — in reality, contamination may be topic-dependent (e.g., a model contaminated on geometry but not algebra). We address this as follows:\\n(a) Compute standardized residuals r_{j,i} = (Y_{j,i} − P̂_{j,i}) / √(P̂_{j,i}(1−P̂_{j,i})) from the rank-1 fit and report the residual matrix.\\n(b) Compute Yen's Q3 statistic for local dependence among original items after conditioning on θ_j — systematic topic-structured residuals would indicate rank-1 insufficiency.\\n(c) Apply person-fit statistics (standardized log-likelihood lz*) to detect models whose original-item response patterns deviate from the G-2PL predictions, flagging potential topic-specific contamination.\\n(d) If structured residuals emerge, explore rank-2 extension (ξ_j·η_i → ξ_j^(1)·η_i^(1) + ξ_j^(2)·η_i^(2)) or topic-stratified estimation as explicit future work.\\n(e) Justification for rank-1 as starting point: LLM contamination is primarily driven by overall training data overlap (entire benchmark suites appearing in Common Crawl/web scrapes) rather than topic-selective memorization; the rank-1 model captures this dominant effect.\\n\\n**Data collection (within 200 H100-hr budget):**\\nFor ~1,000 items from MATH-500 and a GSM8K subset, we generate symbolically-verified adversarial variants. Primary pipeline: MaSTer-style multi-round rewrite-verify using Qwen3.6-27B as rewriter with SymPy answer verification (~25 H100-hrs). Backup (if MaSTer code unavailable by week 1): (a) single-round rewrite-verify pipeline with Qwen3.6-27B + SymPy checking, implementable in 2-3 days; (b) MathCheck (ICLR 2025, open code at github.com/PremiLab-Math/MathCheck) for GSM8K variants; (c) seed with MATH-Perturb's 279 expert-crafted perturbations (ICML 2025, open code at github.com/Kaffaljidhmah2/MATH-Perturb) and extend via LLM rewriting for remaining items. We collect response matrices from 15-20 models: 10 open-weight (DeepSeek-R2 32B, DeepSeek-V4-Flash 284B, Qwen3.6-27B, Qwen3.5-397B-A17B, GLM-5.1 754B-A40B, OLMo-2-13B, Llama-4-Maverick-17B-A400B, Mistral-Large-3, plus 2 smaller reference models) and 5-8 closed-API models (GPT-4o, GPT-5.2, Claude Sonnet 4.6, Gemini 2.5 Flash, Gemini 3.1 Pro). For originals, we reuse Open LLM Leaderboard per-item response data (available via HuggingFace API at huggingface.co/datasets/open-llm-leaderboard/results) where available, requiring new inference only for variant items and models not on the leaderboard (~80 H100-hrs for open-weight variant inference, ~60 H100-hrs for missing original runs). IRT fitting is negligible (<1 hr CPU for MCMC).\\n\\n**Validation (three-pronged, addressing domain mismatch concern):**\\n\\n(1) External ranking correlation: Kendall-τ of CRADE-corrected ability rankings vs. MathArena 2026 uncontaminated competition rankings (~900 problems, 50+ models), targeting τ ≥ 0.85 (revised from 0.90 given domain mismatch between textbook-style MATH-500/GSM8K and competition-style MathArena). Report bootstrap 95% confidence interval. Compare against: (a) raw accuracy rankings, (b) RankLLM difficulty-weighted rankings, (c) DCR-corrected rankings (r=0.66 on hard tasks), (d) JECS-filtered rankings.\\n\\n(2) Synthetic contamination injection (causal validation): Deliberately fine-tune OLMo-2-13B on MATH-500 training items (1 epoch, mild contamination following established protocols from contamination survey literature) and re-evaluate. If G-2PL correctly recovers elevated ξ for the fine-tuned model while θ remains stable (matching pre-contamination ability), this provides causal evidence that the decomposition works. Compare fine-tuned ξ against clean OLMo-2-13B ξ via posterior credible interval separation. This is the strongest validation because it provides ground-truth contamination status.\\n\\n(3) Convergent validity with existing detectors: Correlate G-2PL's per-model ξ_j estimates with: (a) ConStat contamination flags (performance gap on rephrased vs. original), (b) PaCoST binary contamination verdicts (paired confidence significance test), (c) PSN-IRT's anomalous guessing-rate parameters. High concordance validates that ξ captures the same construct; low concordance would require investigation of what ξ uniquely captures beyond existing methods.\\n\\n(4) Ablation showing differential correction benefit: Demonstrate that CRADE correction improves ranking accuracy (vs. MathArena) more for models with high estimated ξ (provably or detectably contaminated) than for models with low ξ. This confirms the correction is targeted rather than uniformly applied.\\n\\n**Anchor assumption validation (variant contamination-free):**\\n(a) Fit standard 2PL to variant-only response matrix and compute item-fit statistics (S-X² or Orlando-Thissen) and person-fit statistics (lz*). Good fit supports the anchor assumption — variants behave like clean IRT items measuring genuine ability.\\n(b) Check that variant difficulty b_i + δ_i is predictable from original difficulty b_i plus a systematic shift; high-residual outlier items may indicate re-contaminated variants and should be flagged for manual review.\\n(c) Cross-validation: Hold out 20% of variant items, fit 2PL on remaining 80%, predict held-out responses. Prediction accuracy comparable to full-data fit supports generalizability.\\n(d) Ablation: Compare CRADE results using MATH-Perturb's expert-crafted perturbations (strongest anchor assumption) vs. MaSTer/LLM-generated variants to assess sensitivity to variant quality.\\n\\nAblations: (a) G-2PL vs. G-3PL (with fixed c_i = 0 for math), (b) Bayesian MCMC vs. neural estimation vs. variational inference, (c) number of variant items (100/500/1000), (d) number of models (10/15/20), (e) sensitivity to variant difficulty shift δ_i, (f) rank-1 vs. rank-2 bilinear decomposition if residuals warrant it, (g) RankLLM vs. G-2PL ranking quality.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180 H100-hrs (variant generation: 25 hrs with Qwen3.6-27B; open-weight inference on variants: 80 hrs across 10 models; gap-filling original inference: 60 hrs; synthetic contamination fine-tuning of OLMo-2-13B: 5 hrs; buffer: 10 hrs)\",\n      \"timeline\": \"8 weeks (1 researcher: wk1 pipeline+MaSTer check+backup plan, wk2 variant generation, wk3 inference+data collection, wk4 G-2PL implementation in NumPyro/Stan, wk5 fitting+synthetic contamination experiment, wk6 validation+ablations+RankLLM comparison, wk7-8 writing+proofs+residual analysis)\",\n      \"estimated_gpu_cost\": \"$2,200 ($540 GPU compute at $3/hr + $1,560 closed-model API for 8 models × 1K items × ~$0.002/item avg + $100 OLMo fine-tuning)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~155 H100-hrs (aggressive leaderboard data reuse, focused variant generation on MATH-500 only for initial submission, GSM8K as ablation, skip OLMo fine-tuning for camera-ready)\",\n      \"timeline\": \"6 weeks\",\n      \"claude_api_cost\": \"$280 (G-2PL model implementation in NumPyro, identifiability proof verification, residual analysis scripts, RankLLM baseline implementation, paper drafting)\",\n      \"estimated_gpu_cost\": \"$1,850 ($465 GPU + $1,385 closed-model APIs)\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~210 H100-hrs (full 20-model coverage, automated hyperparameter sweeps over G-2PL/G-3PL variants, extended GSM8K coverage, synthetic contamination experiment with 3 fine-tuning recipes)\",\n      \"timeline\": \"4 weeks (parallel inference, automated ablation grid)\",\n      \"claude_api_cost\": \"$900 (variant generation QA, pipeline orchestration, automated ablation analysis including rank-1 vs rank-2, draft writing, RankLLM reimplementation)\",\n      \"estimated_gpu_cost\": \"$2,500 ($630 GPU + $1,870 closed-model APIs)\",\n      \"speed_bottleneck\": \"Sequential GPU inference for MoE models (DeepSeek-V4-Flash on 2×H100, Qwen3.5-397B on 4×H100, GLM-5.1 on 4×H100); MCMC fitting with 4 chains is parallelizable but takes ~30 min on CPU\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract deadline Jul 21 2026, paper deadline Jul 28 2026 — primary target, same venue as PSN-IRT, natural psychometric-evaluation audience)\",\n    \"EACL 2027 (ARR submission deadline Aug 3 2026, commitment deadline Oct 11 2026 — ACL-community backup, contamination detection audience)\",\n    \"ICLR 2027 (submission expected ~Sep–Oct 2026, not yet announced — stretch target, highest-prestige ML venue)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Lost in Benchmarks? Rethinking LLM Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral) — 4PL IRT for 12 LLMs on 41,871 items via pseudo-Siamese neural estimation; flags contamination via guessing-rate anomalies but leaves corrected scoring as open question; demonstrates neural IRT estimation works with very few examinees\",\n    \"RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty (ICLR 2026) — non-parametric bidirectional score propagation achieving 90% human alignment on 30 models × 35,550 questions; robust to 50% model removal (ρ=0.94); no contamination modeling; our primary non-parametric baseline\",\n    \"DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025) — ad-hoc multiplicative contamination correction achieving r=0.66 on hard tasks; our measurement-theoretic G-2PL subsumes this\",\n    \"On The Fragility of Benchmark Contamination Detection in Reasoning Models [Wang, Li, Ko, Zhang] (ICLR 2026) — proves likelihood-based detection fails on reasoning models (AUROC ≈ 50%); motivates response-pattern-based approach\",\n    \"Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise [DGM; Shu, Henson, Luecht] (Psychometrika 2013) — key theoretical precedent: gated IRT with hierarchical MCMC estimation decomposes performance into ability + preknowledge; we extend to unknown item exposure via paired items\",\n    \"ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024) — detects contamination via performance gaps on rephrased samples against reference models; confirms paired-item signal but no latent-variable model; used as convergent validity comparison\",\n    \"Provable Joint Decontamination for Benchmarking Multiple Large Language Models [JECS] (arXiv May 2026) — conformal p-values via joint envelope selection for multi-model decontamination; binarizes items (keep/discard) while we produce continuous corrected scores\",\n    \"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025) — uses IRT as difficulty reward for RL-based rewriting; we use IRT for joint ability-contamination estimation\",\n    \"Toward Automated Robustness Evaluation of Mathematical Reasoning [MaSTer] (arXiv 2026) — validated multi-round adversarial variant pipeline (5 streams × 3 iterations) on 4×4090 GPUs using Qwen2.5-32B-Instruct with SymPy verification; 45-94% failure rates on GSM8K/MATH-500; code claimed at github.com/sustech-nlp/MaSTer but unavailable as of May 2026\",\n    \"Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist [MathCheck] (ICLR 2025) — open-source variant generation pipeline for GSM8K and GeoQA; backup pipeline for variant generation\",\n    \"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations (ICML 2025) — 279 expert-crafted MATH Level-5 perturbations with SymPy verification; demonstrates 10-25% drops on frontier models; open code provides seed perturbations and strongest anchor-assumption validation\",\n    \"MathArena: Evaluating LLMs on Uncontaminated Math Competitions (NeurIPS 2025 D&B Track) — expanded to ~900 problems across 2025-2026 competitions including AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, and Apex; our primary ground-truth validation source\",\n    \"PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs (arXiv 2024) — paired original-perturbed items for binary contamination detection via three-step statistical analysis; confirms paired signal without latent-variable modeling; used as convergent validity comparison\",\n    \"Redefining Item Response Models for Small Samples [Fox] (Journal of Educational and Behavioral Statistics 2025) — IRT-BCSM integrates out person parameters for stable estimation at N=50-100; establishes that Bayesian IRT estimation is viable with small person samples\",\n    \"On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory [San Martin et al.] (Psychometrika 2024) — establishes identifiability conditions for 3PL/4PL; our G-2PL proof builds on these results with simpler conditions\",\n    \"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration (arXiv April 2026) — anchor-item IRT calibration for extensible LLM evaluation; demonstrates fixed parameter calibration with <2% error using 100 anchor items per sub-domain; relevant to our variant-as-anchor approach\",\n    \"Investigating a weakly informative prior for item scale hyperparameters in hierarchical 3PNO IRT models (Frontiers in Psychology 2017) — half-t priors for hierarchical IRT; informs our prior specification for the G-2PL contamination parameters\",\n    \"py-irt: A Scalable Item Response Theory Library for Python (IJOC 2023) — GPU-accelerated Bayesian IRT fitting via variational inference; comparison estimation method\",\n    \"The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models (arXiv April 2026) — reasoning modes (genuine/scaffolding/decorative); provides qualitative taxonomy for interpreting contamination-ability decomposition\",\n    \"Unmasking Reasoning Processes: A Process-aware Benchmark for Evaluating Structural Mathematical Reasoning in LLMs [Zheng et al.] (arXiv 2602.00564) — process-level math evaluation; relevant to understanding what adversarial variants test\"\n  ],\n  \"description\": \"CRADE introduces a measurement-theoretic framework for decomposing LLM benchmark performance into genuine reasoning ability (θ), contamination exposure (ξ), and item properties, by extending the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from test-security psychometrics to LLM evaluation. The primary model is the Gated-2PL (G-2PL), chosen over G-3PL because the guessing parameter requires 200+ examinees for stable estimation while we have 15-20 models, and math benchmarks with open-ended answers have effectively zero guessing probability — making 2PL substantively appropriate and statistically tractable. The key innovation is a paired-item design where each benchmark question is coupled with a symbolically-verified adversarial variant, enabling identification of contamination parameters without requiring knowledge of which items appeared in training data — resolving DGM's assumption of known item exposure. Variant items serve as contamination-free anchors to identify genuine ability θ_j via standard 2PL, then per-model contamination ξ_j and per-item susceptibility η_i are identified from original-variant performance gaps under a bilinear decomposition with provable identifiability ((M−1)(K−1) > 0). Estimation uses Bayesian MCMC via NumPyro/Stan with hierarchical Beta priors on contamination parameters, following DGM's original estimation framework, with neural estimation (extending PSN-IRT's architecture) as comparison. This circumvents the critical failure of likelihood-based contamination detection on reasoning models (AUROC ≈ 50%, Wang et al. ICLR 2026) by operating entirely on response patterns. Three-pronged validation: (1) Kendall-τ ≥ 0.85 against MathArena's ~900-problem uncontaminated competition rankings, compared against RankLLM (ICLR 2026) non-parametric baseline, DCR correction, and JECS-filtered rankings; (2) synthetic contamination injection via deliberate fine-tuning of OLMo-2-13B on benchmark items to causally verify that G-2PL recovers elevated ξ while θ remains stable; (3) convergent validity correlation with existing detectors (ConStat, PaCoST, PSN-IRT anomalous parameters). Model adequacy assessed via standardized residuals, Q3 local dependence statistics, and person-fit lz* statistics from the rank-1 bilinear model, with rank-2 topic-specific extensions as explicit future work if structured residuals emerge. Focused on ~1,000 items from MATH-500 and GSM8K with 15-20 models (including DeepSeek-R2 32B, DeepSeek-V4-Flash, Qwen3.6-27B, GLM-5.1, and 5-8 closed-API models), the study fits within 210 H100-hrs. Backup variant generation pipelines (single-round rewrite-verify, MathCheck, MATH-Perturb seed data) mitigate the risk that MaSTer code remains unavailable.\",\n  \"project_name\": \"crade_gated_irt\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"issues_addressed\": {\n      \"MODERATE_estimation_algorithm\": \"Fully specified three-tier estimation strategy: (1) Primary: Bayesian MCMC via NumPyro/Stan with hierarchical Beta priors on ξ_j and η_i, LogNormal priors on a_i, normal priors on b_i and δ_i — 4 chains × 2000 warmup + 2000 samples, NUTS sampler, R̂ < 1.05. This follows DGM's original hierarchical MCMC framework. (2) Comparison: Neural estimation extending PSN-IRT's pseudo-Siamese architecture with gating head. (3) Ablation: Variational inference via Pyro SVI. Key decision: G-2PL as primary model (not G-3PL), because the guessing parameter c_i requires 200+ examinees for stable classical estimation while we have 15-20 models, and open-ended math problems have c ≈ 0 making 2PL substantively appropriate. G-3PL with fixed c_i = 0 becomes an ablation showing equivalence. This simplification strengthens the theoretical contribution (cleaner identifiability, better Fisher information conditioning) while maintaining the core contamination decomposition.\",\n      \"MODERATE_bilinear_rank1\": \"Added comprehensive model adequacy plan: (a) standardized residual matrix r_{j,i} from rank-1 fit, (b) Yen's Q3 statistic for topic-structured local dependence, (c) person-fit lz* statistics for aberrant response patterns, (d) rank-2 extension as explicit future work if residuals show structure. Justified rank-1 as first-order approximation: LLM contamination is primarily driven by bulk training data overlap (whole benchmark suites in web scrapes) rather than topic-selective memorization — rank-1 captures this dominant effect.\",\n      \"MODERATE_validation_target\": \"Revised τ target from >0.90 to ≥0.85 with bootstrap 95% CI, acknowledging domain mismatch between textbook-style MATH-500/GSM8K and competition-style MathArena. Added three additional validation strategies: (1) synthetic contamination injection (fine-tune OLMo-2-13B on benchmark items, verify G-2PL recovers elevated ξ with stable θ), (2) convergent validity with ConStat/PaCoST/PSN-IRT contamination flags, (3) differential correction benefit ablation (correction improves more for high-ξ models). This provides causal, correlational, and ablative evidence.\",\n      \"MODERATE_MaSTer_code\": \"Confirmed MaSTer code at github.com/sustech-nlp/MaSTer was unavailable as of May 2026 (repo not found on organization page). Added three concrete backup plans: (a) single-round rewrite-verify pipeline with Qwen3.6-27B + SymPy (implementable in 2-3 days), (b) MathCheck (ICLR 2025, open code at github.com/PremiLab-Math/MathCheck), (c) MATH-Perturb's 279 expert-crafted perturbations as seed data (ICML 2025, open code at github.com/Kaffaljidhmah2/MATH-Perturb). Week 1 decision point: check MaSTer availability → proceed with backup if unavailable.\",\n      \"MINOR_RankLLM_baseline\": \"Added RankLLM (ICLR 2026) as primary non-parametric baseline. RankLLM uses bidirectional score propagation with single damping hyperparameter α, achieving 90% human alignment on 30 models × 35,550 questions and robust to 50% model removal (ρ=0.94). Key comparison: RankLLM produces difficulty-weighted rankings but provides no contamination decomposition — cannot distinguish memorization from ability. CRADE produces interpretable per-model ξ_j and per-item η_i parameters that RankLLM cannot. Comparison: Raw accuracy vs. RankLLM vs. G-2PL uncorrected vs. G-2PL corrected vs. MathArena ground truth.\",\n      \"MINOR_MathArena_count\": \"Updated to ~900 problems (verified: 897 as of May 2026). Breakdown: ArXivLean (41), BrokenArxiv (148), ArXivMath (143), Visual Math/Kangaroo (168), Final-Answer Competitions (336 including AIME 2026, HMMT Feb 2026, Apex, Apex Shortlist), Proof-Based (50 including USAMO 2026, IMO 2025, Putnam 2025, Miklós Schweitzer 2025), Project Euler (50).\",\n      \"MINOR_anchor_assumption\": \"Added four-part empirical validation strategy: (a) fit standard 2PL to variant-only data and assess item-fit (S-X²) and person-fit (lz*) — good fit supports anchor assumption, (b) check variant difficulty predictability from original difficulty + systematic shift, flagging high-residual items, (c) 20% held-out cross-validation on variant responses, (d) ablation comparing MATH-Perturb expert-crafted perturbations (strongest anchor guarantee) vs. LLM-generated variants to assess sensitivity to variant quality.\"\n    },\n    \"deeper_changes\": {\n      \"model_simplification_to_G2PL\": \"The most significant change is adopting G-2PL as the primary model instead of G-3PL. This is not a compromise but a strengthening: (1) For open-ended math (MATH-500, GSM8K), guessing probability is genuinely near zero, making 2PL the correct substantive model. (2) Dropping c_i eliminates the parameter most problematic for small-sample estimation (requires 200+ examinees classically). (3) The 2PL Fisher information matrix is well-conditioned at M=15, unlike 3PL where c_i creates flat likelihood surfaces. (4) The identifiability proof simplifies: 2PL identifiability conditions are weaker than 3PL (Maris & Bechger 2009). (5) G-3PL with fixed c_i = 0 for math is mathematically equivalent to G-2PL, confirming no information loss for our target domain.\",\n      \"estimation_fully_grounded\": \"Estimation is now fully specified and grounded in the DGM literature. The original DGM (Shu et al. 2013) used hierarchical MCMC — we adopt the same framework with modern tools (NumPyro for GPU-accelerated HMC). The hierarchical Beta priors on ξ_j and η_i allow the posterior to be data-driven: clean models concentrate near ξ=0, contaminated models near ξ=1, without imposing a fixed prior mean. This is more principled than fixing priors to arbitrary constants.\",\n      \"validation_tripled\": \"Validation expanded from single MathArena τ to four complementary strategies covering causal evidence (synthetic injection), correlational evidence (existing detector concordance), discriminant evidence (differential correction), and external validity (MathArena ranking). The synthetic contamination experiment with OLMo-2-13B is the strongest addition — it provides ground-truth contamination status, which no observational comparison can.\",\n      \"RankLLM_as_foil\": \"RankLLM serves as a productive foil: it demonstrates that difficulty-aware non-parametric ranking works well for LLM evaluation (90% human alignment), raising the bar for CRADE's parametric approach. CRADE must justify its additional complexity by providing something RankLLM cannot: interpretable contamination decomposition and corrected ability scores. This sharpens the paper's contribution.\",\n      \"model_updates\": \"Updated Qwen3.5-27B → Qwen3.6-27B (released April 2026, Apache 2.0, supersedes 3.5 with flagship-level coding at 27B dense). Confirmed GLM-5.1 specifications (754B total / 40B active, MIT license, trained on Huawei Ascend 910B). Confirmed DeepSeek-R2 32B (MIT, single GPU, 92.7% AIME 2025).\"\n    }\n  }\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: Compute budget (800 H100-hrs minimum) exceeds user constraint (≤200 H100-hrs) by 4x — requires fundamental scope reduction\", \"CRITICAL: DeepSeek-R2 is 32B dense, NOT 800B-MoE — this model doesn't exist and compute estimates for it are wrong\", \"MAJOR: SymPy-backed symbolic verification is infeasible for MMLU-Pro (text-based multiple choice) — must drop MMLU-Pro or use different verification\", \"MAJOR: STIM-style token-level memorization scores require log-probability access, unavailable for most closed-API models (GPT-4o, Gemini) — limits SPA metric to open-weight models only\", \"MAJOR: 3PL/4PL IRT models have well-documented identifiability issues (flat likelihood surfaces, guessing-ability trade-offs); adding contamination parameter ξ_j exacerbates this — need formal identifiability proof for CA-4PL with paired items, not just intuitive argument\", \"MODERATE: ReasoningMath-Plus by Zheng et al. could not be verified as a real paper — closest match is 'Unmasking Reasoning Processes' (2602.00564) under different authors\", \"MODERATE: 8-week timeline assumes no infrastructure setup time, no failed experiments, no revision cycles — unrealistic for a 1-researcher project of this scope\", \"MINOR: Seed papers misattribute Fragility paper to 'Kocetkov et al.' when it's by Wang, Li, Ko, Zhang (ICLR 2026)\"]\nFeedback: The core idea is genuinely novel and well-motivated — the three-way gap is real and verified. To make this feasible: (1) SCOPE DOWN drastically: drop MMLU-Pro entirely, focus on MATH + GSM8K only (~2,000 items), reduce to 15-20 models, reuse Open LLM Leaderboard response data for original items to avoid re-running originals — this could bring compute to ~150-200 H100-hrs; (2) FIX model references: DeepSeek-R2 is 32B dense, use DeepSeek-V4 (1.6T MoE) or Qwen3.5-397B as the large MoE targets; (3) ADDRESS IRT identifiability formally: prove that the paired-item structure provides identifiability for ξ given θ and d — this is your central theoretical contribution and needs mathematical rigor, not just the intuitive argument that 'contamination only inflates originals'; (4) LIMIT SPA metric to open-weight models where log-probabilities are available, and use answer-pattern-only analysis for closed models; (5) VERIFY ReasoningMath-Plus reference or replace with confirmed papers (the 'Unmasking Reasoning Processes' paper at 2602.00564 may serve the same purpose); (6) Consider splitting into two papers: (a) CA-4PL theory + MATH validation, (b) step-level SPA analysis — the current scope is a full workshop + main conference paper combined.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MODERATE: IRT 3PL parameter estimation with only 15-20 models (examinees) lacks a concrete mitigation plan. Standard 3PL requires 200+ examinees for stable guessing-parameter estimation. PSN-IRT's 12-model success used neural networks, not standard 3PL. The proposal must specify: will you use Bayesian priors, reduce to 2PL, adopt PSN-IRT's neural approach, or use marginal maximum likelihood with strong regularization? This choice affects the entire theoretical contribution.\", \"MODERATE: Bilinear rank-1 contamination assumption (ξ_j·η_i) assumes model contamination and item susceptibility are independent. In reality, contamination is likely topic-dependent (e.g., a model contaminated on geometry but not algebra). No residual analysis or model adequacy test is planned. If rank-1 doesn't hold, the decomposition loses interpretability.\", \"MODERATE: τ > 0.90 validation target against MathArena is ambitious given domain mismatch — CRADE operates on MATH-500/GSM8K (textbook-style problems) while MathArena uses competition problems (AIME, USAMO, etc.) at different difficulty levels. High Kendall-τ isn't guaranteed even with perfect contamination correction. Need additional validation strategies.\", \"MODERATE: MaSTer's GitHub repository (github.com/sustech-nlp/MaSTer) returned 404 — code may not be publicly released yet. If unavailable, variant generation pipeline must be implemented from scratch, adding 1-2 weeks to the timeline.\", \"MINOR: RankLLM (ICLR 2026) is a missing baseline — a non-parametric difficulty-aware ranking method that avoids IRT's per-item logistic fits and handles small model samples gracefully. Should be compared as a simpler alternative.\", \"MINOR: MathArena problem count claimed as ~795 but verified at ~750+ (as of May 2026). Minor discrepancy but should be accurate.\", \"MINOR: The variant 'contamination-free anchor' assumption needs an empirical validation strategy. If variants share structural similarity with training data, θ_j estimates will be biased. Consider testing whether variant performance shows anomalous patterns inconsistent with the IRT model.\"]\nFeedback: The revision substantially improved the proposal — all critical round 1 issues were addressed, every reference verified, the DGM-grounded G-3PL formulation is significantly stronger than the original ad-hoc CA-4PL. The idea is close to passing. To get there: (1) **Specify the estimation algorithm**: State explicitly whether you'll use Bayesian MCMC (as in the original DGM), variational inference via Pyro/py-irt, or EM with regularization. For 15-20 models, Bayesian estimation with informative priors on guessing parameters is likely necessary — consider fixing c_i to benchmark-specific constants or using a hierarchical prior. Also consider a '2PL + contamination gate' as a simpler starting point with an ablation to 3PL. (2) **Add RankLLM (ICLR 2026) as baseline**: It's a non-parametric alternative that jointly estimates difficulty and competency, published at the same caliber venue, and explicitly handles small model counts. (3) **Diversify validation**: Beyond τ against MathArena, add: (a) synthetic contamination injection experiments (deliberately fine-tune a model on benchmark items and check if G-3PL recovers the contamination), (b) correlation with existing detectors (ConStat, PaCoST flags), (c) ablation showing that correction helps more on provably contaminated models. (4) **Plan for bilinear model adequacy**: State that you'll compute and report residuals from the rank-1 model, and if structured, explore rank-2 or topic-specific extensions as future work. (5) **Have a backup for MaSTer code**: If repo isn't public by week 1, implement a simpler single-round rewrite-verify pipeline with SymPy checking — this loses MaSTer's multi-round refinement but is implementable in days.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"...\"}\n  },\n  \"issues\": [\"specific issue 1\", ...],\n  \"feedback\": \"Actionable feedback (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold\n- \"fail\": fundamental flaw (gap doesn't exist, approach provably wrong)\n- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T12:39:03.661Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T12:39:03.661Z",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-28T12:39:03.679Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-28 (UTC).**

Your job: independently verify this idea's claims via web_search, then issue a verdict.

## User requirements
The user asked for: **Target: AAAI 2026
Track: AI Alignment / Main Technical Track — Robustness Evaluation

Direction: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated "genuine capability" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.

Seed Papers:
- Zawalski et al. "CoDeC" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation
- Li et al. "ATLAS" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity
- Hou et al. "MaSTer" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination
- Zheng et al. "ReasoningMath-Plus" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component
- Chen et al. "Reasoning Models Don't Always Say What They Think" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination
- Xu et al. "DCR" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis
- Kocetkov et al. "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches

Known Gaps:
- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)
- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only
- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing
- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives

Theoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.

Constraints:
- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)
- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)
- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth

Quality Self-Checks:
- [x] Core insight: "Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level."
- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.
- [x] Baseline fear test: A simple baseline of "run on variants and average" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.
- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.

Avoid:
- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)
- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark
- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)
- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead**
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
4. **Venue validity**: Are target venue deadlines after 2026-05-28?
5. **Feasibility**: Is the resource estimate realistic?
6. **Novelty**: Is this sufficiently different from existing work?
7. **Cost realism**: Are the three mode estimates internally consistent?

## Idea under review (round 3/10)
{
  "title": "CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items",
  "core_problem": "No existing framework can determine whether a model fails adversarial benchmark variants because it memorized original answers (contamination) or because it lacks genuine reasoning ability (capability deficit) — all current work observes this entanglement but none models it within a measurement-theoretic framework, preventing trustworthy LLM capability assessment.",
  "opportunity": "Three previously siloed research streams — IRT-based LLM evaluation (PSN-IRT AAAI 2026 Oral, ATLAS, LEGO-IRT), contamination detection/correction (DCR EMNLP 2025, ConStat NeurIPS 2024, JECS arXiv May 2026), and adversarial robustness testing (MaSTer, RIDE, MATH-Perturb ICML 2025) — have each matured independently to the point where their integration is both technically feasible and urgently needed. The critical catalyst is Wang et al.'s ICLR 2026 proof that all likelihood-based contamination detection fails on reasoning models (AUROC ≈ 50%), creating demand for response-pattern-based alternatives that bypass token-probability signals entirely. A key theoretical precedent exists but has never been applied to LLMs: the Deterministic Gated IRT model (DGM; Shu, Henson & Luecht, Psychometrika 2013) decomposes test performance into genuine ability and cheating/preknowledge components conditioned on item exposure status — precisely the structure needed for LLM contamination. PSN-IRT showed IRT works for LLMs (12 models, 41,871 items, 4PL) but left contamination-adjusted scoring as an explicit open question, flagging anomalous guessing-rate parameters as contamination indicators without providing corrected ability estimates. RankLLM (ICLR 2026) demonstrated that non-parametric difficulty-aware ranking achieves 90% human alignment with only a damping hyperparameter — but provides no contamination decomposition, producing rankings without interpretable ability vs. memorization parameters. The AAAI 2027 deadline (abstracts July 21, papers July 28, 2026) is 8 weeks out. Nobody sits at the three-way intersection of IRT estimation, contamination correction, and adversarial pairing because these communities publish at different venues (ACL/EMNLP for contamination, ICLR/NeurIPS for robustness, AAAI for psychometric evaluation, Psychometrika/JEBS for test security).",
  "landscape": "The current best contamination-to-correction pipeline is DCR (EMNLP 2025), which produces a DCR Factor via fuzzy inference across four contamination levels, achieving ~4% average error on three benchmarks — but its ad-hoc multiplicative correction Acc_adj = Acc × (1 − DCR Factor) has no measurement-theoretic justification and empirically weakens on hard tasks (r=0.66). PSN-IRT (AAAI 2026 Oral) demonstrates IRT's power for LLM evaluation using a 4PL model across 12 LLMs on 11 benchmarks (41,871 items), flagging contamination indirectly via anomalous guessing-rate parameters, but produces no contamination-adjusted ability scores; critically, PSN-IRT succeeds with only 12 models by using neural network estimation (pseudo-Siamese architecture) rather than classical MLE, establishing that neural IRT estimation is viable at small model counts. RankLLM (ICLR 2026) provides a strong non-parametric baseline: bidirectional score propagation between models and questions achieves 90% human alignment on 30 models × 35,550 questions, with remarkable stability under model removal (ρ = 0.94 even with 50% pool removed) and 0.006s convergence — but it produces difficulty-weighted rankings without any contamination modeling. RIDE (arXiv 2025) combines IRT with adversarial perturbation for math evaluation — but uses IRT only as a difficulty reward signal for RL-based question rewriting via RIDE-8B, not for joint ability-contamination estimation. JECS (arXiv May 2026) achieves formal conformal guarantees for multi-model decontamination via joint envelope conformal selection, but wastes information by binarizing items into keep/discard rather than producing continuous corrected scores. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples using a statistical comparison against reference models, but does not model it as a latent variable within a psychometric framework. In psychometrics, the DGM (Shu et al., Psychometrika 2013) uses a gated IRT formulation estimated via hierarchical MCMC to decompose examinee performance into genuine ability and item-preknowledge components — but assumes item exposure status is known a priori, which is unavailable for LLM training data. Two paired-item approaches exist but use no IRT: PaCoST (arXiv 2024) performs paired confidence significance testing for binary contamination detection, and ConStat compares primary vs. reference benchmark performance — both confirm the paired-item signal is informative but neither models it as a latent variable. For adversarial variant generation, MaSTer (arXiv 2026) provides a validated multi-round rewrite-verify pipeline (5 parallel streams × 3 iterations) achieving 45-94% target failure rates on GSM8K and MATH-500 using Qwen2.5-32B-Instruct and SymPy verification; code is claimed at github.com/sustech-nlp/MaSTer but was unavailable as of May 2026 — backup pipelines exist via MathCheck (ICLR 2025, open code) and MATH-Perturb (ICML 2025, 279 expert-crafted perturbations with open code). MathArena (NeurIPS 2025 D&B Track) has expanded to ~900 problems across 2025-2026 competitions (AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, Apex) with 50+ models, providing rich uncontaminated ground-truth rankings. Recent IRT estimation advances for small samples include Fox (2025, JEBS) demonstrating IRT-BCSM for N=50-100 by analytically integrating out person parameters, and Bayesian hierarchical priors achieving stable 2PL estimation at small sample sizes. Concurrent work search (arXiv, OpenReview, May 2026): no paper attempts joint IRT-based contamination-ability decomposition with paired adversarial items — the three-way intersection remains unoccupied.",
  "inspired_by": "Field guide gaps: 'Contamination-aware IRT' (gap 3), 'Joint contamination-robustness decomposition' (gap 1); Innovation patterns: 'Self-Referential Measurement' (model as own control via original-vs-variant), 'Formal Guarantees on Evaluation Methodology' (identifiability proof for Gated-2PL), 'Detection-to-Correction Bridge' (from detection signals to calibrated ability scores); Key theoretical bridge: DGM (Shu et al. 2013) provides the gated IRT structure for item preknowledge estimated via hierarchical MCMC, which we extend to the LLM contamination setting where item exposure status is unknown but inferred from paired adversarial items; Untried combinations: 'DGM-style gated IRT with adversarial variant generation for LLM evaluation' (primary), 'Conformal p-values as contamination priors for gated IRT' (secondary), 'RankLLM non-parametric ranking as sanity-check baseline for IRT-corrected rankings' (tertiary)",
  "approach": "We extend the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from the test-security domain to LLM contamination assessment, introducing the Gated-2PL (G-2PL) model as the primary framework where correct-response probability decomposes into ability-driven and contamination-driven components via a gating mechanism. The key innovation over DGM is that item exposure status is not assumed known but is identified from paired adversarial items.\n\n**Model specification (primary: Gated-2PL):**\n- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i)), a standard 2PL with difficulty shift δ_i\n- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i))\n- θ_j = model j's genuine reasoning ability (person parameter)\n- ξ_j ∈ [0,1] = model j's contamination exposure (person parameter)\n- η_i ∈ [0,1] = item i's contamination susceptibility (item parameter)\n- a_i, b_i = discrimination and difficulty (shared across original-variant pairs)\n- δ_i = variant difficulty shift (estimated from variant calibration)\n\n**Rationale for G-2PL over G-3PL:** The guessing parameter c_i in 3PL requires 200+ examinees for stable estimation under classical methods, while we have only 15-20 models. Dropping c_i to use 2PL eliminates the most problematic parameter for small samples while retaining the core contamination decomposition. PSN-IRT succeeded with 12 models using neural estimation, but their 4PL worked because they had 41,871 items providing massive per-item information; our gated model adds M+K contamination parameters, making parsimony critical. For math benchmarks with open-ended answers (MATH-500, GSM8K), guessing probability is effectively zero, making 2PL substantively appropriate.\n\n**Ablation to Gated-3PL (G-3PL):**\n- P(Y_{j,i*}=1 | θ_j) = c_i + (1−c_i)·σ(a_i(θ_j − b_i − δ_i))\n- P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·[c_i + (1−c_i)·σ(a_i(θ_j − b_i))]\n- c_i fixed to domain-specific constants: c_i = 0 for open-ended math (MATH-500, GSM8K), enabling estimation only for any future MCQ extensions.\n\n**Estimation strategy (fully specified):**\nPrimary: Bayesian MCMC via NumPyro/Stan with hierarchical priors, following DGM's original estimation framework:\n- θ_j ~ N(0, σ²_θ), σ_θ ~ Half-Cauchy(0, 2.5)\n- ξ_j ~ Beta(α_ξ, β_ξ), with α_ξ, β_ξ ~ Gamma(2, 1) (hierarchical; allows posterior to concentrate near 0 for clean models or near 1 for heavily contaminated ones)\n- η_i ~ Beta(α_η, β_η), with α_η, β_η ~ Gamma(2, 1) (hierarchical)\n- a_i ~ LogNormal(0, 0.5) (positive discrimination, weakly informative)\n- b_i ~ N(0, 1) (centered difficulty)\n- δ_i ~ N(0, 0.5) (variant shifts expected small)\n- MCMC: 4 chains × 2,000 warmup + 2,000 samples, NUTS sampler, R̂ < 1.05 convergence criterion\nComparison: Neural estimation extending PSN-IRT's pseudo-Siamese architecture with an additional gating head that outputs (ξ_j, η_i) — trained via binary cross-entropy on the joint original+variant response matrix. This provides a non-Bayesian point estimate comparison.\nAblation: Variational inference via Pyro SVI as a faster alternative to MCMC, using amortized inference for scalability testing.\n\n**Formal identifiability (central theoretical contribution):**\nWe prove identifiability via a two-step argument: (1) Variant items serve as contamination-free anchors, identifying θ_j and item parameters {a_i, b_i} via standard 2PL identifiability conditions (≥2 items with heterogeneous discriminations; cf. Maris & Bechger 2009). The difficulty shift δ_i is estimated from the variant calibration. (2) Given identified θ_j and item parameters, the original-variant performance gap identifies the bilinear product ξ_j·η_i. Under the rank-1 bilinear decomposition ξ_j·η_i with M models and K items, we have M·K observed gaps constraining M+K−1 free parameters (one fixed for scale), identifiable when M·K > M+K−1, i.e., (M−1)(K−1) > 0. This holds for any M,K ≥ 2. The 2PL formulation avoids the flat-likelihood surfaces that plague 3PL/4PL estimation with few examinees, as the Fisher information matrix for the 2PL is well-conditioned even at M=15.\n\n**Bilinear rank-1 model adequacy plan:**\nThe rank-1 assumption (ξ_j·η_i) treats contamination as model-global and item-global, which is a first-order approximation — in reality, contamination may be topic-dependent (e.g., a model contaminated on geometry but not algebra). We address this as follows:\n(a) Compute standardized residuals r_{j,i} = (Y_{j,i} − P̂_{j,i}) / √(P̂_{j,i}(1−P̂_{j,i})) from the rank-1 fit and report the residual matrix.\n(b) Compute Yen's Q3 statistic for local dependence among original items after conditioning on θ_j — systematic topic-structured residuals would indicate rank-1 insufficiency.\n(c) Apply person-fit statistics (standardized log-likelihood lz*) to detect models whose original-item response patterns deviate from the G-2PL predictions, flagging potential topic-specific contamination.\n(d) If structured residuals emerge, explore rank-2 extension (ξ_j·η_i → ξ_j^(1)·η_i^(1) + ξ_j^(2)·η_i^(2)) or topic-stratified estimation as explicit future work.\n(e) Justification for rank-1 as starting point: LLM contamination is primarily driven by overall training data overlap (entire benchmark suites appearing in Common Crawl/web scrapes) rather than topic-selective memorization; the rank-1 model captures this dominant effect.\n\n**Data collection (within 200 H100-hr budget):**\nFor ~1,000 items from MATH-500 and a GSM8K subset, we generate symbolically-verified adversarial variants. Primary pipeline: MaSTer-style multi-round rewrite-verify using Qwen3.6-27B as rewriter with SymPy answer verification (~25 H100-hrs). Backup (if MaSTer code unavailable by week 1): (a) single-round rewrite-verify pipeline with Qwen3.6-27B + SymPy checking, implementable in 2-3 days; (b) MathCheck (ICLR 2025, open code at github.com/PremiLab-Math/MathCheck) for GSM8K variants; (c) seed with MATH-Perturb's 279 expert-crafted perturbations (ICML 2025, open code at github.com/Kaffaljidhmah2/MATH-Perturb) and extend via LLM rewriting for remaining items. We collect response matrices from 15-20 models: 10 open-weight (DeepSeek-R2 32B, DeepSeek-V4-Flash 284B, Qwen3.6-27B, Qwen3.5-397B-A17B, GLM-5.1 754B-A40B, OLMo-2-13B, Llama-4-Maverick-17B-A400B, Mistral-Large-3, plus 2 smaller reference models) and 5-8 closed-API models (GPT-4o, GPT-5.2, Claude Sonnet 4.6, Gemini 2.5 Flash, Gemini 3.1 Pro). For originals, we reuse Open LLM Leaderboard per-item response data (available via HuggingFace API at huggingface.co/datasets/open-llm-leaderboard/results) where available, requiring new inference only for variant items and models not on the leaderboard (~80 H100-hrs for open-weight variant inference, ~60 H100-hrs for missing original runs). IRT fitting is negligible (<1 hr CPU for MCMC).\n\n**Validation (three-pronged, addressing domain mismatch concern):**\n\n(1) External ranking correlation: Kendall-τ of CRADE-corrected ability rankings vs. MathArena 2026 uncontaminated competition rankings (~900 problems, 50+ models), targeting τ ≥ 0.85 (revised from 0.90 given domain mismatch between textbook-style MATH-500/GSM8K and competition-style MathArena). Report bootstrap 95% confidence interval. Compare against: (a) raw accuracy rankings, (b) RankLLM difficulty-weighted rankings, (c) DCR-corrected rankings (r=0.66 on hard tasks), (d) JECS-filtered rankings.\n\n(2) Synthetic contamination injection (causal validation): Deliberately fine-tune OLMo-2-13B on MATH-500 training items (1 epoch, mild contamination following established protocols from contamination survey literature) and re-evaluate. If G-2PL correctly recovers elevated ξ for the fine-tuned model while θ remains stable (matching pre-contamination ability), this provides causal evidence that the decomposition works. Compare fine-tuned ξ against clean OLMo-2-13B ξ via posterior credible interval separation. This is the strongest validation because it provides ground-truth contamination status.\n\n(3) Convergent validity with existing detectors: Correlate G-2PL's per-model ξ_j estimates with: (a) ConStat contamination flags (performance gap on rephrased vs. original), (b) PaCoST binary contamination verdicts (paired confidence significance test), (c) PSN-IRT's anomalous guessing-rate parameters. High concordance validates that ξ captures the same construct; low concordance would require investigation of what ξ uniquely captures beyond existing methods.\n\n(4) Ablation showing differential correction benefit: Demonstrate that CRADE correction improves ranking accuracy (vs. MathArena) more for models with high estimated ξ (provably or detectably contaminated) than for models with low ξ. This confirms the correction is targeted rather than uniformly applied.\n\n**Anchor assumption validation (variant contamination-free):**\n(a) Fit standard 2PL to variant-only response matrix and compute item-fit statistics (S-X² or Orlando-Thissen) and person-fit statistics (lz*). Good fit supports the anchor assumption — variants behave like clean IRT items measuring genuine ability.\n(b) Check that variant difficulty b_i + δ_i is predictable from original difficulty b_i plus a systematic shift; high-residual outlier items may indicate re-contaminated variants and should be flagged for manual review.\n(c) Cross-validation: Hold out 20% of variant items, fit 2PL on remaining 80%, predict held-out responses. Prediction accuracy comparable to full-data fit supports generalizability.\n(d) Ablation: Compare CRADE results using MATH-Perturb's expert-crafted perturbations (strongest anchor assumption) vs. MaSTer/LLM-generated variants to assess sensitivity to variant quality.\n\nAblations: (a) G-2PL vs. G-3PL (with fixed c_i = 0 for math), (b) Bayesian MCMC vs. neural estimation vs. variational inference, (c) number of variant items (100/500/1000), (d) number of models (10/15/20), (e) sensitivity to variant difficulty shift δ_i, (f) rank-1 vs. rank-2 bilinear decomposition if residuals warrant it, (g) RankLLM vs. G-2PL ranking quality.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180 H100-hrs (variant generation: 25 hrs with Qwen3.6-27B; open-weight inference on variants: 80 hrs across 10 models; gap-filling original inference: 60 hrs; synthetic contamination fine-tuning of OLMo-2-13B: 5 hrs; buffer: 10 hrs)",
      "timeline": "8 weeks (1 researcher: wk1 pipeline+MaSTer check+backup plan, wk2 variant generation, wk3 inference+data collection, wk4 G-2PL implementation in NumPyro/Stan, wk5 fitting+synthetic contamination experiment, wk6 validation+ablations+RankLLM comparison, wk7-8 writing+proofs+residual analysis)",
      "estimated_gpu_cost": "$2,200 ($540 GPU compute at $3/hr + $1,560 closed-model API for 8 models × 1K items × ~$0.002/item avg + $100 OLMo fine-tuning)"
    },
    "human_in_loop": {
      "gpu_hours": "~155 H100-hrs (aggressive leaderboard data reuse, focused variant generation on MATH-500 only for initial submission, GSM8K as ablation, skip OLMo fine-tuning for camera-ready)",
      "timeline": "6 weeks",
      "claude_api_cost": "$280 (G-2PL model implementation in NumPyro, identifiability proof verification, residual analysis scripts, RankLLM baseline implementation, paper drafting)",
      "estimated_gpu_cost": "$1,850 ($465 GPU + $1,385 closed-model APIs)"
    },
    "auto_research": {
      "gpu_hours": "~210 H100-hrs (full 20-model coverage, automated hyperparameter sweeps over G-2PL/G-3PL variants, extended GSM8K coverage, synthetic contamination experiment with 3 fine-tuning recipes)",
      "timeline": "4 weeks (parallel inference, automated ablation grid)",
      "claude_api_cost": "$900 (variant generation QA, pipeline orchestration, automated ablation analysis including rank-1 vs rank-2, draft writing, RankLLM reimplementation)",
      "estimated_gpu_cost": "$2,500 ($630 GPU + $1,870 closed-model APIs)",
      "speed_bottleneck": "Sequential GPU inference for MoE models (DeepSeek-V4-Flash on 2×H100, Qwen3.5-397B on 4×H100, GLM-5.1 on 4×H100); MCMC fitting with 4 chains is parallelizable but takes ~30 min on CPU"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract deadline Jul 21 2026, paper deadline Jul 28 2026 — primary target, same venue as PSN-IRT, natural psychometric-evaluation audience)",
    "EACL 2027 (ARR submission deadline Aug 3 2026, commitment deadline Oct 11 2026 — ACL-community backup, contamination detection audience)",
    "ICLR 2027 (submission expected ~Sep–Oct 2026, not yet announced — stretch target, highest-prestige ML venue)"
  ],
  "level": "top-tier",
  "key_references": [
    "Lost in Benchmarks? Rethinking LLM Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral) — 4PL IRT for 12 LLMs on 41,871 items via pseudo-Siamese neural estimation; flags contamination via guessing-rate anomalies but leaves corrected scoring as open question; demonstrates neural IRT estimation works with very few examinees",
    "RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty (ICLR 2026) — non-parametric bidirectional score propagation achieving 90% human alignment on 30 models × 35,550 questions; robust to 50% model removal (ρ=0.94); no contamination modeling; our primary non-parametric baseline",
    "DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025) — ad-hoc multiplicative contamination correction achieving r=0.66 on hard tasks; our measurement-theoretic G-2PL subsumes this",
    "On The Fragility of Benchmark Contamination Detection in Reasoning Models [Wang, Li, Ko, Zhang] (ICLR 2026) — proves likelihood-based detection fails on reasoning models (AUROC ≈ 50%); motivates response-pattern-based approach",
    "Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise [DGM; Shu, Henson, Luecht] (Psychometrika 2013) — key theoretical precedent: gated IRT with hierarchical MCMC estimation decomposes performance into ability + preknowledge; we extend to unknown item exposure via paired items",
    "ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024) — detects contamination via performance gaps on rephrased samples against reference models; confirms paired-item signal but no latent-variable model; used as convergent validity comparison",
    "Provable Joint Decontamination for Benchmarking Multiple Large Language Models [JECS] (arXiv May 2026) — conformal p-values via joint envelope selection for multi-model decontamination; binarizes items (keep/discard) while we produce continuous corrected scores",
    "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025) — uses IRT as difficulty reward for RL-based rewriting; we use IRT for joint ability-contamination estimation",
    "Toward Automated Robustness Evaluation of Mathematical Reasoning [MaSTer] (arXiv 2026) — validated multi-round adversarial variant pipeline (5 streams × 3 iterations) on 4×4090 GPUs using Qwen2.5-32B-Instruct with SymPy verification; 45-94% failure rates on GSM8K/MATH-500; code claimed at github.com/sustech-nlp/MaSTer but unavailable as of May 2026",
    "Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist [MathCheck] (ICLR 2025) — open-source variant generation pipeline for GSM8K and GeoQA; backup pipeline for variant generation",
    "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations (ICML 2025) — 279 expert-crafted MATH Level-5 perturbations with SymPy verification; demonstrates 10-25% drops on frontier models; open code provides seed perturbations and strongest anchor-assumption validation",
    "MathArena: Evaluating LLMs on Uncontaminated Math Competitions (NeurIPS 2025 D&B Track) — expanded to ~900 problems across 2025-2026 competitions including AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, and Apex; our primary ground-truth validation source",
    "PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs (arXiv 2024) — paired original-perturbed items for binary contamination detection via three-step statistical analysis; confirms paired signal without latent-variable modeling; used as convergent validity comparison",
    "Redefining Item Response Models for Small Samples [Fox] (Journal of Educational and Behavioral Statistics 2025) — IRT-BCSM integrates out person parameters for stable estimation at N=50-100; establishes that Bayesian IRT estimation is viable with small person samples",
    "On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory [San Martin et al.] (Psychometrika 2024) — establishes identifiability conditions for 3PL/4PL; our G-2PL proof builds on these results with simpler conditions",
    "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration (arXiv April 2026) — anchor-item IRT calibration for extensible LLM evaluation; demonstrates fixed parameter calibration with <2% error using 100 anchor items per sub-domain; relevant to our variant-as-anchor approach",
    "Investigating a weakly informative prior for item scale hyperparameters in hierarchical 3PNO IRT models (Frontiers in Psychology 2017) — half-t priors for hierarchical IRT; informs our prior specification for the G-2PL contamination parameters",
    "py-irt: A Scalable Item Response Theory Library for Python (IJOC 2023) — GPU-accelerated Bayesian IRT fitting via variational inference; comparison estimation method",
    "The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models (arXiv April 2026) — reasoning modes (genuine/scaffolding/decorative); provides qualitative taxonomy for interpreting contamination-ability decomposition",
    "Unmasking Reasoning Processes: A Process-aware Benchmark for Evaluating Structural Mathematical Reasoning in LLMs [Zheng et al.] (arXiv 2602.00564) — process-level math evaluation; relevant to understanding what adversarial variants test"
  ],
  "description": "CRADE introduces a measurement-theoretic framework for decomposing LLM benchmark performance into genuine reasoning ability (θ), contamination exposure (ξ), and item properties, by extending the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from test-security psychometrics to LLM evaluation. The primary model is the Gated-2PL (G-2PL), chosen over G-3PL because the guessing parameter requires 200+ examinees for stable estimation while we have 15-20 models, and math benchmarks with open-ended answers have effectively zero guessing probability — making 2PL substantively appropriate and statistically tractable. The key innovation is a paired-item design where each benchmark question is coupled with a symbolically-verified adversarial variant, enabling identification of contamination parameters without requiring knowledge of which items appeared in training data — resolving DGM's assumption of known item exposure. Variant items serve as contamination-free anchors to identify genuine ability θ_j via standard 2PL, then per-model contamination ξ_j and per-item susceptibility η_i are identified from original-variant performance gaps under a bilinear decomposition with provable identifiability ((M−1)(K−1) > 0). Estimation uses Bayesian MCMC via NumPyro/Stan with hierarchical Beta priors on contamination parameters, following DGM's original estimation framework, with neural estimation (extending PSN-IRT's architecture) as comparison. This circumvents the critical failure of likelihood-based contamination detection on reasoning models (AUROC ≈ 50%, Wang et al. ICLR 2026) by operating entirely on response patterns. Three-pronged validation: (1) Kendall-τ ≥ 0.85 against MathArena's ~900-problem uncontaminated competition rankings, compared against RankLLM (ICLR 2026) non-parametric baseline, DCR correction, and JECS-filtered rankings; (2) synthetic contamination injection via deliberate fine-tuning of OLMo-2-13B on benchmark items to causally verify that G-2PL recovers elevated ξ while θ remains stable; (3) convergent validity correlation with existing detectors (ConStat, PaCoST, PSN-IRT anomalous parameters). Model adequacy assessed via standardized residuals, Q3 local dependence statistics, and person-fit lz* statistics from the rank-1 bilinear model, with rank-2 topic-specific extensions as explicit future work if structured residuals emerge. Focused on ~1,000 items from MATH-500 and GSM8K with 15-20 models (including DeepSeek-R2 32B, DeepSeek-V4-Flash, Qwen3.6-27B, GLM-5.1, and 5-8 closed-API models), the study fits within 210 H100-hrs. Backup variant generation pipelines (single-round rewrite-verify, MathCheck, MATH-Perturb seed data) mitigate the risk that MaSTer code remains unavailable.",
  "project_name": "crade_gated_irt",
  "source": "web_research",
  "revision_notes": {
    "issues_addressed": {
      "MODERATE_estimation_algorithm": "Fully specified three-tier estimation strategy: (1) Primary: Bayesian MCMC via NumPyro/Stan with hierarchical Beta priors on ξ_j and η_i, LogNormal priors on a_i, normal priors on b_i and δ_i — 4 chains × 2000 warmup + 2000 samples, NUTS sampler, R̂ < 1.05. This follows DGM's original hierarchical MCMC framework. (2) Comparison: Neural estimation extending PSN-IRT's pseudo-Siamese architecture with gating head. (3) Ablation: Variational inference via Pyro SVI. Key decision: G-2PL as primary model (not G-3PL), because the guessing parameter c_i requires 200+ examinees for stable classical estimation while we have 15-20 models, and open-ended math problems have c ≈ 0 making 2PL substantively appropriate. G-3PL with fixed c_i = 0 becomes an ablation showing equivalence. This simplification strengthens the theoretical contribution (cleaner identifiability, better Fisher information conditioning) while maintaining the core contamination decomposition.",
      "MODERATE_bilinear_rank1": "Added comprehensive model adequacy plan: (a) standardized residual matrix r_{j,i} from rank-1 fit, (b) Yen's Q3 statistic for topic-structured local dependence, (c) person-fit lz* statistics for aberrant response patterns, (d) rank-2 extension as explicit future work if residuals show structure. Justified rank-1 as first-order approximation: LLM contamination is primarily driven by bulk training data overlap (whole benchmark suites in web scrapes) rather than topic-selective memorization — rank-1 captures this dominant effect.",
      "MODERATE_validation_target": "Revised τ target from >0.90 to ≥0.85 with bootstrap 95% CI, acknowledging domain mismatch between textbook-style MATH-500/GSM8K and competition-style MathArena. Added three additional validation strategies: (1) synthetic contamination injection (fine-tune OLMo-2-13B on benchmark items, verify G-2PL recovers elevated ξ with stable θ), (2) convergent validity with ConStat/PaCoST/PSN-IRT contamination flags, (3) differential correction benefit ablation (correction improves more for high-ξ models). This provides causal, correlational, and ablative evidence.",
      "MODERATE_MaSTer_code": "Confirmed MaSTer code at github.com/sustech-nlp/MaSTer was unavailable as of May 2026 (repo not found on organization page). Added three concrete backup plans: (a) single-round rewrite-verify pipeline with Qwen3.6-27B + SymPy (implementable in 2-3 days), (b) MathCheck (ICLR 2025, open code at github.com/PremiLab-Math/MathCheck), (c) MATH-Perturb's 279 expert-crafted perturbations as seed data (ICML 2025, open code at github.com/Kaffaljidhmah2/MATH-Perturb). Week 1 decision point: check MaSTer availability → proceed with backup if unavailable.",
      "MINOR_RankLLM_baseline": "Added RankLLM (ICLR 2026) as primary non-parametric baseline. RankLLM uses bidirectional score propagation with single damping hyperparameter α, achieving 90% human alignment on 30 models × 35,550 questions and robust to 50% model removal (ρ=0.94). Key comparison: RankLLM produces difficulty-weighted rankings but provides no contamination decomposition — cannot distinguish memorization from ability. CRADE produces interpretable per-model ξ_j and per-item η_i parameters that RankLLM cannot. Comparison: Raw accuracy vs. RankLLM vs. G-2PL uncorrected vs. G-2PL corrected vs. MathArena ground truth.",
      "MINOR_MathArena_count": "Updated to ~900 problems (verified: 897 as of May 2026). Breakdown: ArXivLean (41), BrokenArxiv (148), ArXivMath (143), Visual Math/Kangaroo (168), Final-Answer Competitions (336 including AIME 2026, HMMT Feb 2026, Apex, Apex Shortlist), Proof-Based (50 including USAMO 2026, IMO 2025, Putnam 2025, Miklós Schweitzer 2025), Project Euler (50).",
      "MINOR_anchor_assumption": "Added four-part empirical validation strategy: (a) fit standard 2PL to variant-only data and assess item-fit (S-X²) and person-fit (lz*) — good fit supports anchor assumption, (b) check variant difficulty predictability from original difficulty + systematic shift, flagging high-residual items, (c) 20% held-out cross-validation on variant responses, (d) ablation comparing MATH-Perturb expert-crafted perturbations (strongest anchor guarantee) vs. LLM-generated variants to assess sensitivity to variant quality."
    },
    "deeper_changes": {
      "model_simplification_to_G2PL": "The most significant change is adopting G-2PL as the primary model instead of G-3PL. This is not a compromise but a strengthening: (1) For open-ended math (MATH-500, GSM8K), guessing probability is genuinely near zero, making 2PL the correct substantive model. (2) Dropping c_i eliminates the parameter most problematic for small-sample estimation (requires 200+ examinees classically). (3) The 2PL Fisher information matrix is well-conditioned at M=15, unlike 3PL where c_i creates flat likelihood surfaces. (4) The identifiability proof simplifies: 2PL identifiability conditions are weaker than 3PL (Maris & Bechger 2009). (5) G-3PL with fixed c_i = 0 for math is mathematically equivalent to G-2PL, confirming no information loss for our target domain.",
      "estimation_fully_grounded": "Estimation is now fully specified and grounded in the DGM literature. The original DGM (Shu et al. 2013) used hierarchical MCMC — we adopt the same framework with modern tools (NumPyro for GPU-accelerated HMC). The hierarchical Beta priors on ξ_j and η_i allow the posterior to be data-driven: clean models concentrate near ξ=0, contaminated models near ξ=1, without imposing a fixed prior mean. This is more principled than fixing priors to arbitrary constants.",
      "validation_tripled": "Validation expanded from single MathArena τ to four complementary strategies covering causal evidence (synthetic injection), correlational evidence (existing detector concordance), discriminant evidence (differential correction), and external validity (MathArena ranking). The synthetic contamination experiment with OLMo-2-13B is the strongest addition — it provides ground-truth contamination status, which no observational comparison can.",
      "RankLLM_as_foil": "RankLLM serves as a productive foil: it demonstrates that difficulty-aware non-parametric ranking works well for LLM evaluation (90% human alignment), raising the bar for CRADE's parametric approach. CRADE must justify its additional complexity by providing something RankLLM cannot: interpretable contamination decomposition and corrected ability scores. This sharpens the paper's contribution.",
      "model_updates": "Updated Qwen3.5-27B → Qwen3.6-27B (released April 2026, Apache 2.0, supersedes 3.5 with flagship-level coding at 27B dense). Confirmed GLM-5.1 specifications (754B total / 40B active, MIT license, trained on Huawei Ascend 910B). Confirmed DeepSeek-R2 32B (MIT, single GPU, 92.7% AIME 2025)."
    }
  }
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: Compute budget (800 H100-hrs minimum) exceeds user constraint (≤200 H100-hrs) by 4x — requires fundamental scope reduction", "CRITICAL: DeepSeek-R2 is 32B dense, NOT 800B-MoE — this model doesn't exist and compute estimates for it are wrong", "MAJOR: SymPy-backed symbolic verification is infeasible for MMLU-Pro (text-based multiple choice) — must drop MMLU-Pro or use different verification", "MAJOR: STIM-style token-level memorization scores require log-probability access, unavailable for most closed-API models (GPT-4o, Gemini) — limits SPA metric to open-weight models only", "MAJOR: 3PL/4PL IRT models have well-documented identifiability issues (flat likelihood surfaces, guessing-ability trade-offs); adding contamination parameter ξ_j exacerbates this — need formal identifiability proof for CA-4PL with paired items, not just intuitive argument", "MODERATE: ReasoningMath-Plus by Zheng et al. could not be verified as a real paper — closest match is 'Unmasking Reasoning Processes' (2602.00564) under different authors", "MODERATE: 8-week timeline assumes no infrastructure setup time, no failed experiments, no revision cycles — unrealistic for a 1-researcher project of this scope", "MINOR: Seed papers misattribute Fragility paper to 'Kocetkov et al.' when it's by Wang, Li, Ko, Zhang (ICLR 2026)"]
Feedback: The core idea is genuinely novel and well-motivated — the three-way gap is real and verified. To make this feasible: (1) SCOPE DOWN drastically: drop MMLU-Pro entirely, focus on MATH + GSM8K only (~2,000 items), reduce to 15-20 models, reuse Open LLM Leaderboard response data for original items to avoid re-running originals — this could bring compute to ~150-200 H100-hrs; (2) FIX model references: DeepSeek-R2 is 32B dense, use DeepSeek-V4 (1.6T MoE) or Qwen3.5-397B as the large MoE targets; (3) ADDRESS IRT identifiability formally: prove that the paired-item structure provides identifiability for ξ given θ and d — this is your central theoretical contribution and needs mathematical rigor, not just the intuitive argument that 'contamination only inflates originals'; (4) LIMIT SPA metric to open-weight models where log-probabilities are available, and use answer-pattern-only analysis for closed models; (5) VERIFY ReasoningMath-Plus reference or replace with confirmed papers (the 'Unmasking Reasoning Processes' paper at 2602.00564 may serve the same purpose); (6) Consider splitting into two papers: (a) CA-4PL theory + MATH validation, (b) step-level SPA analysis — the current scope is a full workshop + main conference paper combined.

### Round 2 review
Verdict: revise
Issues: ["MODERATE: IRT 3PL parameter estimation with only 15-20 models (examinees) lacks a concrete mitigation plan. Standard 3PL requires 200+ examinees for stable guessing-parameter estimation. PSN-IRT's 12-model success used neural networks, not standard 3PL. The proposal must specify: will you use Bayesian priors, reduce to 2PL, adopt PSN-IRT's neural approach, or use marginal maximum likelihood with strong regularization? This choice affects the entire theoretical contribution.", "MODERATE: Bilinear rank-1 contamination assumption (ξ_j·η_i) assumes model contamination and item susceptibility are independent. In reality, contamination is likely topic-dependent (e.g., a model contaminated on geometry but not algebra). No residual analysis or model adequacy test is planned. If rank-1 doesn't hold, the decomposition loses interpretability.", "MODERATE: τ > 0.90 validation target against MathArena is ambitious given domain mismatch — CRADE operates on MATH-500/GSM8K (textbook-style problems) while MathArena uses competition problems (AIME, USAMO, etc.) at different difficulty levels. High Kendall-τ isn't guaranteed even with perfect contamination correction. Need additional validation strategies.", "MODERATE: MaSTer's GitHub repository (github.com/sustech-nlp/MaSTer) returned 404 — code may not be publicly released yet. If unavailable, variant generation pipeline must be implemented from scratch, adding 1-2 weeks to the timeline.", "MINOR: RankLLM (ICLR 2026) is a missing baseline — a non-parametric difficulty-aware ranking method that avoids IRT's per-item logistic fits and handles small model samples gracefully. Should be compared as a simpler alternative.", "MINOR: MathArena problem count claimed as ~795 but verified at ~750+ (as of May 2026). Minor discrepancy but should be accurate.", "MINOR: The variant 'contamination-free anchor' assumption needs an empirical validation strategy. If variants share structural similarity with training data, θ_j estimates will be biased. Consider testing whether variant performance shows anomalous patterns inconsistent with the IRT model."]
Feedback: The revision substantially improved the proposal — all critical round 1 issues were addressed, every reference verified, the DGM-grounded G-3PL formulation is significantly stronger than the original ad-hoc CA-4PL. The idea is close to passing. To get there: (1) **Specify the estimation algorithm**: State explicitly whether you'll use Bayesian MCMC (as in the original DGM), variational inference via Pyro/py-irt, or EM with regularization. For 15-20 models, Bayesian estimation with informative priors on guessing parameters is likely necessary — consider fixing c_i to benchmark-specific constants or using a hierarchical prior. Also consider a '2PL + contamination gate' as a simpler starting point with an ablation to 3PL. (2) **Add RankLLM (ICLR 2026) as baseline**: It's a non-parametric alternative that jointly estimates difficulty and competency, published at the same caliber venue, and explicitly handles small model counts. (3) **Diversify validation**: Beyond τ against MathArena, add: (a) synthetic contamination injection experiments (deliberately fine-tune a model on benchmark items and check if G-3PL recovers the contamination), (b) correlation with existing detectors (ConStat, PaCoST flags), (c) ablation showing that correction helps more on provably contaminated models. (4) **Plan for bilinear model adequacy**: State that you'll compute and report residuals from the rank-1 model, and if structured, explore rank-2 or topic-specific extensions as future work. (5) **Have a backup for MaSTer code**: If repo isn't public by week 1, implement a simpler single-round rewrite-verify pipeline with SymPy checking — this loses MaSTer's multi-round refinement but is implementable in days.


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
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "type": "user",
  "uuid": "42370e64-99c7-4073-8d30-55bbafab0dfd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T12:39:03.677Z_

```json
{
  "parentUuid": "42370e64-99c7-4073-8d30-55bbafab0dfd",
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
  "uuid": "e441ad8d-fa55-4745-a84d-637d2d729756",
  "timestamp": "2026-05-28T12:39:03.677Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T12:39:03.677Z_

```json
{
  "parentUuid": "e441ad8d-fa55-4745-a84d-637d2d729756",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1e5d7dfd-6c15-4a84-8280-9925ee4b5a05",
  "timestamp": "2026-05-28T12:39:03.677Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "1e5d7dfd-6c15-4a84-8280-9925ee4b5a05",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CRADE contamination-ability decomposition via gated IRT",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Assistant

_source line 8 · 2026-05-28T12:39:10.583Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed ML research proposal review task. I need to independently verify the claims made in the CRADE proposal, check the SOTA, verify references, assess feasibility, and provide a thorough review. Let me systematically work through this.

Let me launch multiple search agents to verify different aspects of this proposal in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e5d7dfd-6c15-4a84-8280-9925ee4b5a05",
  "isSidechain": false,
  "requestId": "req_011CbUyqyxUd7Yv3bLBWxHTT",
  "type": "assistant",
  "uuid": "5062d97b-facb-4196-999d-781784f1a91c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6oP8QUCMGLHThYRxbtWqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16576,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2851,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2851,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16576
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

_source line 9 · 2026-05-28T12:39:10.756Z_

I'll conduct a thorough independent verification of this proposal's claims. Let me launch multiple parallel searches to verify references, check for competing work, and assess feasibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5062d97b-facb-4196-999d-781784f1a91c",
  "isSidechain": false,
  "requestId": "req_011CbUyqyxUd7Yv3bLBWxHTT",
  "type": "assistant",
  "uuid": "caf8bb87-938b-4d2c-8481-b2525d0a1069",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6oP8QUCMGLHThYRxbtWqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16576,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2851,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2851,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16576
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

_source line 10 · 2026-05-28T12:39:26.716Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YQUqHjX2v7kH8WhxNEijaV`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify PSN-IRT and DGM references",
  "prompt": "I'm reviewing a research proposal that cites several key papers. I need you to verify these specific papers exist and that the claims about them are accurate. Use WebSearch and WebFetch to verify each one.\n\n1. **PSN-IRT (AAAI 2026 Oral)**: \"Lost in Benchmarks? Rethinking LLM Benchmarking with Item Response Theory\" — Claims: 4PL IRT for 12 LLMs on 41,871 items via pseudo-Siamese neural estimation; flags contamination via guessing-rate anomalies but leaves corrected scoring as open question. Verify: Does this paper exist? Is it really AAAI 2026 Oral? Does it really use 12 models and 41,871 items? Does it really leave contamination-corrected scoring as open?\n\n2. **DGM (Shu, Henson, Luecht, Psychometrika 2013)**: \"Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise\" — Claims: gated IRT with hierarchical MCMC that decomposes performance into ability + preknowledge. Verify: Does this paper exist? Does it use gated IRT? Is it in Psychometrika 2013?\n\n3. **RankLLM (ICLR 2026)**: \"Weighted Ranking of LLMs by Quantifying Question Difficulty\" — Claims: non-parametric bidirectional score propagation achieving 90% human alignment on 30 models × 35,550 questions; robust to 50% model removal (ρ=0.94). Verify existence and claims.\n\n4. **Wang et al. (ICLR 2026)**: \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" — Claims: proves likelihood-based detection fails on reasoning models (AUROC ≈ 50%). Verify existence and claims.\n\n5. **JECS (arXiv May 2026)**: \"Provable Joint Decontamination for Benchmarking Multiple Large Language Models\" — Verify existence.\n\nSearch for each paper by title and by author names. Report what you find with specific evidence."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caf8bb87-938b-4d2c-8481-b2525d0a1069",
  "isSidechain": false,
  "requestId": "req_011CbUyqyxUd7Yv3bLBWxHTT",
  "type": "assistant",
  "uuid": "11f3a3d8-177d-4eeb-b72a-d0774ff270e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6oP8QUCMGLHThYRxbtWqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16576,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2851,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2851,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16576
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

_source line 11 · 2026-05-28T12:39:35.799Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FdgRhANzbhX2LDb9xVfXXP`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing concurrent work",
  "prompt": "I'm reviewing a research proposal called \"CRADE\" that combines IRT (Item Response Theory) with contamination detection and adversarial robustness for LLM evaluation. The proposal claims no existing work sits at this three-way intersection. I need you to do an adversarial search for competing or concurrent work that the authors may have missed.\n\nSearch for ALL of these queries using WebSearch:\n\n1. \"contamination-aware IRT\" OR \"contamination item response theory\" LLM 2025 2026\n2. \"benchmark contamination correction\" \"item response theory\" 2026\n3. \"decontamination\" \"IRT\" \"large language model\" 2026\n4. \"gated IRT\" language model\n5. site:arxiv.org \"contamination\" \"adversarial\" \"IRT\" LLM evaluation 2026\n6. site:openreview.net contamination IRT LLM evaluation 2026\n7. \"joint contamination ability\" OR \"contamination-adjusted scoring\" LLM 2026\n8. \"benchmark integrity\" \"measurement theory\" LLM 2025 2026\n9. \"paired item\" contamination LLM evaluation\n10. site:arxiv.org \"psychometric\" \"contamination\" \"language model\" 2026\n\nFor each search, report: what you found, whether any paper addresses the same three-way intersection (IRT + contamination + adversarial variants), and any paper that could be a direct competitor. Be thorough — the goal is to find work the proposal authors missed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11f3a3d8-177d-4eeb-b72a-d0774ff270e7",
  "isSidechain": false,
  "requestId": "req_011CbUyqyxUd7Yv3bLBWxHTT",
  "type": "assistant",
  "uuid": "998be71a-c8bd-445d-9112-6be1b38dc5fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6oP8QUCMGLHThYRxbtWqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16576,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2851,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2851,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16576
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

_source line 12 · 2026-05-28T12:39:48.415Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01WreL4deabGJ5rprQZbzUhz`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify venue deadlines and models",
  "prompt": "I need to verify several factual claims in a research proposal. Use WebSearch to check each:\n\n1. **AAAI 2027 deadline**: The proposal claims \"abstracts July 21, papers July 28, 2026\". Search for \"AAAI 2027 deadline\" or \"AAAI 2027 call for papers\" to verify. Note: today is May 28, 2026.\n\n2. **DeepSeek-R2 32B**: Verify this model exists, is 32B dense, MIT license, single GPU, 92.7% AIME 2025.\n\n3. **Qwen3.6-27B**: Verify this model exists, was released April 2026, Apache 2.0 license.\n\n4. **GLM-5.1**: Verify 754B total / 40B active parameters, MIT license, trained on Huawei Ascend 910B.\n\n5. **DeepSeek-V4-Flash 284B**: Verify this model exists with these specs.\n\n6. **MathArena**: Verify it has ~900 problems (claimed 897), includes AIME 2026, HMMT Feb 2026, USAMO 2026 etc. Search \"MathArena NeurIPS 2025\" and check the website.\n\n7. **MATH-Perturb (ICML 2025)**: Verify open code at github.com/Kaffaljidhmah2/MATH-Perturb, 279 expert-crafted perturbations.\n\n8. **MathCheck (ICLR 2025)**: Verify open code at github.com/PremiLab-Math/MathCheck.\n\n9. **Fox (2025, JEBS)**: \"Redefining Item Response Models for Small Samples\" — IRT-BCSM for N=50-100. Verify existence.\n\nReport what you find for each item with specific evidence."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "998be71a-c8bd-445d-9112-6be1b38dc5fb",
  "isSidechain": false,
  "requestId": "req_011CbUyqyxUd7Yv3bLBWxHTT",
  "type": "assistant",
  "uuid": "aff85b37-00e8-486f-becf-802f1d2e612b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6oP8QUCMGLHThYRxbtWqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16576,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2851,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2851,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16576
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

_source line 13 · 2026-05-28T12:40:00.786Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XtRSQ4i1tV2D2sGwHEnYrw`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify DCR, ConStat, RIDE, and remaining refs",
  "prompt": "I need to verify several papers cited in a research proposal. Use WebSearch and WebFetch to check each:\n\n1. **DCR (EMNLP 2025)**: \"Quantifying Data Contamination in LLMs Evaluation\" — Claims: fuzzy inference across four contamination levels, ad-hoc multiplicative correction Acc_adj = Acc × (1 − DCR Factor), r=0.66 on hard tasks. Verify it exists at EMNLP 2025 and check the claims.\n\n2. **ConStat (NeurIPS 2024)**: \"Performance-Based Contamination Detection in Large Language Models\" — Claims: detects contamination via performance gaps on rephrased samples against reference models. Verify.\n\n3. **RIDE (arXiv 2025)**: \"Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning\" — Claims: uses IRT as difficulty reward for RL-based question rewriting via RIDE-8B. Verify.\n\n4. **PaCoST (arXiv 2024)**: \"Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs\" — Verify existence and claims about paired original-perturbed items.\n\n5. **\"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\" (arXiv April 2026)** — Verify existence.\n\n6. **\"The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models\" (arXiv April 2026)** — Verify existence.\n\n7. **San Martin et al. (Psychometrika 2024)**: \"On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory\" — Verify.\n\n8. **py-irt (IJOC 2023)**: \"A Scalable Item Response Theory Library for Python\" — Verify existence.\n\nFor each, report: does it exist? Is the venue correct? Are the claims about its content accurate?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aff85b37-00e8-486f-becf-802f1d2e612b",
  "isSidechain": false,
  "requestId": "req_011CbUyqyxUd7Yv3bLBWxHTT",
  "type": "assistant",
  "uuid": "f9d8379a-1aea-4b81-aab7-47f796bb6c4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6oP8QUCMGLHThYRxbtWqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16576,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2851,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2851,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16576
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

_source line 14 · 2026-05-28T12:40:13.756Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01W1wvBDyuuQx4N3Lr4RtVsB`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Assess IRT feasibility for small samples",
  "prompt": "I'm reviewing a proposal that wants to fit a \"Gated 2PL IRT model\" with only 15-20 LLMs as examinees (but ~1000 items). The model is:\n- For variant items: P(Y=1) = σ(a_i(θ_j − b_i − δ_i)) — standard 2PL with difficulty shift\n- For original items: P(Y=1) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i)) — gated model\n- Parameters: θ_j (ability per model), ξ_j (contamination per model), η_i (item susceptibility), a_i (discrimination), b_i (difficulty), δ_i (variant shift)\n- Total free parameters: ~20 person parameters (θ, ξ) + ~4000 item parameters (a, b, δ, η for 1000 items)\n- Estimation: Bayesian MCMC via NumPyro, 4 chains × 2000+2000 samples\n\nSearch for information about:\n\n1. \"IRT small sample\" OR \"IRT few examinees\" Bayesian estimation — what's the minimum viable number of examinees for 2PL?\n2. \"Bayesian IRT\" \"small sample\" convergence — does Bayesian MCMC help with very small N?\n3. The identifiability claim: with M=15 models and K=1000 items, the bilinear product ξ_j·η_i has M+K-1 = 1014 free parameters constrained by M×K = 15,000 observations. Is this actually well-identified in practice?\n4. \"hierarchical IRT\" \"small sample size\" — does hierarchical prior structure help?\n5. Any practical issues with fitting IRT to 15-20 examinees — even with 1000+ items, are there known estimation problems?\n\nGive me a technically honest assessment: is this estimation feasible with 15-20 models? What are the realistic risks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9d8379a-1aea-4b81-aab7-47f796bb6c4d",
  "isSidechain": false,
  "requestId": "req_011CbUyqyxUd7Yv3bLBWxHTT",
  "type": "assistant",
  "uuid": "166d1c79-cf26-46d5-89a7-f2a42dd2435e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6oP8QUCMGLHThYRxbtWqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16576,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2851,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2851,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16576
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

_source line 15 · 2026-05-28T12:41:49.095Z_

<details><summary>↩ Tool result · `toolu_01WreL4deabGJ5rprQZbzUhz`</summary>

```text
Now I have enough information to provide a comprehensive report. Here is my analysis of all nine claims:

---

## Verification Results

### 1. AAAI 2027 Deadline
**VERIFIED.** The AAAI-27 Main Technical Track confirms: abstract submission deadline is **July 21, 2026** and full paper deadline is **July 28, 2026** (both at 11:59 PM UTC-12). The conference will be held February 16-23, 2027, in Montreal, Canada. The proposal's dates are correct.

Sources:
- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [AAAI-27 Conference Page](https://aaai.org/conference/aaai/aaai-27/)

---

### 2. DeepSeek-R2 32B
**VERIFIED.** DeepSeek-R2 is confirmed as a 32B dense transformer (not MoE), released under the MIT license, fits on a single 24 GB consumer GPU (RTX 4090 or A6000), and achieves 92.7% on AIME 2025. It was released in April 2026. All claims check out.

Sources:
- [DeepSeek R2 Explained: 92.7% AIME, 32B Open-Weight](https://decodethefuture.org/en/deepseek-r2-explained/)
- [DeepSeek Wikipedia](https://en.wikipedia.org/wiki/DeepSeek)

---

### 3. Qwen3.6-27B
**VERIFIED.** Alibaba's Qwen team released Qwen3.6-27B on **April 22, 2026** under the **Apache 2.0 license**. It is a 27.8B dense model. All claims are accurate.

Sources:
- [MarkTechPost: Alibaba Qwen Team Releases Qwen3.6-27B](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)
- [Qwen3.6-27B License on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/LICENSE)
- [LLM Stats: Qwen3.6-27B](https://llm-stats.com/models/qwen3.6-27b)

---

### 4. GLM-5.1
**VERIFIED.** GLM-5.1 is confirmed as a MoE model with **754B total parameters / ~40B active** per inference, released under the **MIT license**, and **trained entirely on Huawei Ascend 910B chips** using MindSpore (no Nvidia/AMD GPUs). Released April 7, 2026 by Z.ai (formerly Zhipu AI). All claims check out.

Sources:
- [GLM-5.1 Open-Source Review (BuildFastWithAI)](https://www.buildfastwithai.com/blogs/glm-5-1-open-source-review-2026)
- [DEV Community: GLM-5.1 754B MoE under MIT](https://dev.to/purpledoubled/glm-51-just-dropped-754b-open-weight-moe-model-under-mit-license-heres-how-to-run-it-27b1)
- [Effloow: GLM-5.1 744B MoE](https://effloow.com/articles/glm-5-1-744b-moe-open-source-swebench-guide-2026)

---

### 5. DeepSeek-V4-Flash 284B
**VERIFIED.** DeepSeek-V4-Flash is confirmed as a MoE model with **284B total parameters** and 13B activated parameters, with a 1M-token context window. The model exists on Hugging Face, Ollama, NVIDIA, and multiple inference providers.

Sources:
- [OpenRouter: DeepSeek V4 Flash](https://openrouter.ai/deepseek/deepseek-v4-flash)
- [Modular: DeepSeek V4 Flash 284B MoE](https://www.modular.com/models/deepseek-v4-flash)
- [Hugging Face: deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)

---

### 6. MathArena
**PARTIALLY VERIFIED / LIKELY INCORRECT on problem count.** Key findings:

- **NeurIPS 2025**: Confirmed -- MathArena was presented at NeurIPS Datasets & Benchmarks 2025.
- **AIME 2026**: Confirmed -- AIME 2026 is included in MathArena.
- **HMMT Feb 2026**: Confirmed -- HMMT Feb 2026 appears in the competition list.
- **USAMO 2026**: Confirmed -- USAMO 2026 is included, with datasets on Hugging Face.
- **~897 problems**: **NOT VERIFIED and likely incorrect.** The original NeurIPS 2025 paper states 162 problems across 7 competitions. The expanded 2026 version (arxiv 2605.00674, "Beyond Benchmarks") adds more competitions (AIME, HMMT, BRUMO, SMT, CMIMC, USAMO, IMO, IMC, Putnam, Miklos Schweitzer, Apex, plus arXiv-level problems), but I could not find any source citing ~897 total problems. The claim of 897 problems could not be corroborated and appears inflated relative to what is documented.

Sources:
- [MathArena NeurIPS Paper (OpenReview)](https://openreview.net/forum?id=y0zL9IZxZ7)
- [MathArena Competitions Page](https://matharena.ai/competitions)
- [MathArena AIME 2026](https://matharena.ai/?comp=aime--aime_2026)
- [Beyond Benchmarks (arXiv 2605.00674)](https://arxiv.org/abs/2605.00674)
- [MathArena USAMO 2026 on HuggingFace](https://huggingface.co/datasets/MathArena/usamo_2026)

---

### 7. MATH-Perturb (ICML 2025)
**VERIFIED.** All claims check out:
- Published at **ICML 2025**.
- Open code at **github.com/Kaffaljidhmah2/MATH-Perturb** -- confirmed.
- **279 expert-crafted perturbations** -- confirmed. Each of the two subsets (MATH-P-Simple and MATH-P-Hard) contains 279 perturbed problems derived from level-5 MATH problems, crafted by 12 graduate-level experts.

Sources:
- [GitHub: Kaffaljidhmah2/MATH-Perturb](https://github.com/Kaffaljidhmah2/MATH-Perturb)
- [ICML 2025 Poster](https://icml.cc/virtual/2025/poster/45435)
- [arXiv: 2502.06453](https://arxiv.org/abs/2502.06453)
- [MATH-Perturb Project Page](https://math-perturb.github.io/)

---

### 8. MathCheck (ICLR 2025)
**VERIFIED.** MathCheck is an ICLR 2025 paper titled "Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist." Open code is confirmed at **github.com/PremiLab-Math/MathCheck**. Datasets are also on Hugging Face.

Sources:
- [GitHub: PremiLab-Math/MathCheck](https://github.com/PremiLab-Math/MathCheck)
- [Hugging Face: PremiLab-Math/MathCheck](https://huggingface.co/datasets/PremiLab-Math/MathCheck)
- [arXiv: 2407.08733](https://arxiv.org/pdf/2407.08733)

---

### 9. Fox (2025, JEBS) -- IRT-BCSM
**VERIFIED with a minor date nuance.** The paper "Redefining Item Response Models for Small Samples" by Jean-Paul Fox exists in the **Journal of Educational and Behavioral Statistics** (JEBS). It introduces the **IRT-BCSM** (IRT Bayesian Covariance Structure Model) for small samples of **N=50-100** persons. The DOI (10.3102/10769986241269886) indicates it was published online in 2024 but appears in JEBS Volume 50, Issue 2, 2025 (pp. 272-295). Citing it as "Fox (2025)" is consistent with the journal volume year. All substantive claims are accurate.

Sources:
- [SAGE Journals: Redefining Item Response Models for Small Samples](https://journals.sagepub.com/doi/10.3102/10769986241269886)
- [Fox PDF](https://www.jean-paulfox.com/Fox/documents/Papers/2024/fox-2024-redefining-item-response-models-for-small-samples.pdf)
- [University of Twente Publication](https://research.utwente.nl/en/publications/redefining-item-response-models-for-small-samples)

---

## Summary

| # | Claim | Verdict |
|---|-------|---------|
| 1 | AAAI 2027 deadlines (Jul 21 / Jul 28) | VERIFIED |
| 2 | DeepSeek-R2 32B dense, MIT, single GPU, 92.7% AIME | VERIFIED |
| 3 | Qwen3.6-27B, April 2026, Apache 2.0 | VERIFIED |
| 4 | GLM-5.1 754B/40B active, MIT, Ascend 910B | VERIFIED |
| 5 | DeepSeek-V4-Flash 284B | VERIFIED |
| 6 | MathArena ~897 problems, includes AIME/HMMT/USAMO 2026 | **PARTIALLY -- competitions verified, but 897 problem count could not be corroborated** (paper says 162 in original; expanded version adds more but no source confirms ~897) |
| 7 | MATH-Perturb ICML 2025, GitHub, 279 perturbations | VERIFIED |
| 8 | MathCheck ICLR 2025, GitHub | VERIFIED |
| 9 | Fox (2025, JEBS), IRT-BCSM, N=50-100 | VERIFIED |

The only claim that could not be fully verified is the MathArena problem count of ~897. All other claims are accurate based on available evidence.

agentId: ab5d7354f8760c60c (use SendMessage with to: 'ab5d7354f8760c60c' to continue this agent)
&lt;usage>total_tokens: 27312
tool_uses: 19
duration_ms: 120674&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aff85b37-00e8-486f-becf-802f1d2e612b",
  "isSidechain": false,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "type": "user",
  "uuid": "3bdc3cd5-15c4-4efd-9240-720beaf0d8d0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several factual claims in a research proposal. Use WebSearch to check each:\n\n1. **AAAI 2027 deadline**: The proposal claims \"abstracts July 21, papers July 28, 2026\". Search for \"AAAI 2027 deadline\" or \"AAAI 2027 call for papers\" to verify. Note: today is May 28, 2026.\n\n2. **DeepSeek-R2 32B**: Verify this model exists, is 32B dense, MIT license, single GPU, 92.7% AIME 2025.\n\n3. **Qwen3.6-27B**: Verify this model exists, was released April 2026, Apache 2.0 license.\n\n4. **GLM-5.1**: Verify 754B total / 40B active parameters, MIT license, trained on Huawei Ascend 910B.\n\n5. **DeepSeek-V4-Flash 284B**: Verify this model exists with these specs.\n\n6. **MathArena**: Verify it has ~900 problems (claimed 897), includes AIME 2026, HMMT Feb 2026, USAMO 2026 etc. Search \"MathArena NeurIPS 2025\" and check the website.\n\n7. **MATH-Perturb (ICML 2025)**: Verify open code at github.com/Kaffaljidhmah2/MATH-Perturb, 279 expert-crafted perturbations.\n\n8. **MathCheck (ICLR 2025)**: Verify open code at github.com/PremiLab-Math/MathCheck.\n\n9. **Fox (2025, JEBS)**: \"Redefining Item Response Models for Small Samples\" — IRT-BCSM for N=50-100. Verify existence.\n\nReport what you find for each item with specific evidence.",
    "agentId": "ab5d7354f8760c60c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to provide a comprehensive report. Here is my analysis of all nine claims:\n\n---\n\n## Verification Results\n\n### 1. AAAI 2027 Deadline\n**VERIFIED.** The AAAI-27 Main Technical Track confirms: abstract submission deadline is **July 21, 2026** and full paper deadline is **July 28, 2026** (both at 11:59 PM UTC-12). The conference will be held February 16-23, 2027, in Montreal, Canada. The proposal's dates are correct.\n\nSources:\n- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)\n- [AAAI-27 Conference Page](https://aaai.org/conference/aaai/aaai-27/)\n\n---\n\n### 2. DeepSeek-R2 32B\n**VERIFIED.** DeepSeek-R2 is confirmed as a 32B dense transformer (not MoE), released under the MIT license, fits on a single 24 GB consumer GPU (RTX 4090 or A6000), and achieves 92.7% on AIME 2025. It was released in April 2026. All claims check out.\n\nSources:\n- [DeepSeek R2 Explained: 92.7% AIME, 32B Open-Weight](https://decodethefuture.org/en/deepseek-r2-explained/)\n- [DeepSeek Wikipedia](https://en.wikipedia.org/wiki/DeepSeek)\n\n---\n\n### 3. Qwen3.6-27B\n**VERIFIED.** Alibaba's Qwen team released Qwen3.6-27B on **April 22, 2026** under the **Apache 2.0 license**. It is a 27.8B dense model. All claims are accurate.\n\nSources:\n- [MarkTechPost: Alibaba Qwen Team Releases Qwen3.6-27B](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)\n- [Qwen3.6-27B License on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/LICENSE)\n- [LLM Stats: Qwen3.6-27B](https://llm-stats.com/models/qwen3.6-27b)\n\n---\n\n### 4. GLM-5.1\n**VERIFIED.** GLM-5.1 is confirmed as a MoE model with **754B total parameters / ~40B active** per inference, released under the **MIT license**, and **trained entirely on Huawei Ascend 910B chips** using MindSpore (no Nvidia/AMD GPUs). Released April 7, 2026 by Z.ai (formerly Zhipu AI). All claims check out.\n\nSources:\n- [GLM-5.1 Open-Source Review (BuildFastWithAI)](https://www.buildfastwithai.com/blogs/glm-5-1-open-source-review-2026)\n- [DEV Community: GLM-5.1 754B MoE under MIT](https://dev.to/purpledoubled/glm-51-just-dropped-754b-open-weight-moe-model-under-mit-license-heres-how-to-run-it-27b1)\n- [Effloow: GLM-5.1 744B MoE](https://effloow.com/articles/glm-5-1-744b-moe-open-source-swebench-guide-2026)\n\n---\n\n### 5. DeepSeek-V4-Flash 284B\n**VERIFIED.** DeepSeek-V4-Flash is confirmed as a MoE model with **284B total parameters** and 13B activated parameters, with a 1M-token context window. The model exists on Hugging Face, Ollama, NVIDIA, and multiple inference providers.\n\nSources:\n- [OpenRouter: DeepSeek V4 Flash](https://openrouter.ai/deepseek/deepseek-v4-flash)\n- [Modular: DeepSeek V4 Flash 284B MoE](https://www.modular.com/models/deepseek-v4-flash)\n- [Hugging Face: deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)\n\n---\n\n### 6. MathArena\n**PARTIALLY VERIFIED / LIKELY INCORRECT on problem count.** Key findings:\n\n- **NeurIPS 2025**: Confirmed -- MathArena was presented at NeurIPS Datasets & Benchmarks 2025.\n- **AIME 2026**: Confirmed -- AIME 2026 is included in MathArena.\n- **HMMT Feb 2026**: Confirmed -- HMMT Feb 2026 appears in the competition list.\n- **USAMO 2026**: Confirmed -- USAMO 2026 is included, with datasets on Hugging Face.\n- **~897 problems**: **NOT VERIFIED and likely incorrect.** The original NeurIPS 2025 paper states 162 problems across 7 competitions. The expanded 2026 version (arxiv 2605.00674, \"Beyond Benchmarks\") adds more competitions (AIME, HMMT, BRUMO, SMT, CMIMC, USAMO, IMO, IMC, Putnam, Miklos Schweitzer, Apex, plus arXiv-level problems), but I could not find any source citing ~897 total problems. The claim of 897 problems could not be corroborated and appears inflated relative to what is documented.\n\nSources:\n- [MathArena NeurIPS Paper (OpenReview)](https://openreview.net/forum?id=y0zL9IZxZ7)\n- [MathArena Competitions Page](https://matharena.ai/competitions)\n- [MathArena AIME 2026](https://matharena.ai/?comp=aime--aime_2026)\n- [Beyond Benchmarks (arXiv 2605.00674)](https://arxiv.org/abs/2605.00674)\n- [MathArena USAMO 2026 on HuggingFace](https://huggingface.co/datasets/MathArena/usamo_2026)\n\n---\n\n### 7. MATH-Perturb (ICML 2025)\n**VERIFIED.** All claims check out:\n- Published at **ICML 2025**.\n- Open code at **github.com/Kaffaljidhmah2/MATH-Perturb** -- confirmed.\n- **279 expert-crafted perturbations** -- confirmed. Each of the two subsets (MATH-P-Simple and MATH-P-Hard) contains 279 perturbed problems derived from level-5 MATH problems, crafted by 12 graduate-level experts.\n\nSources:\n- [GitHub: Kaffaljidhmah2/MATH-Perturb](https://github.com/Kaffaljidhmah2/MATH-Perturb)\n- [ICML 2025 Poster](https://icml.cc/virtual/2025/poster/45435)\n- [arXiv: 2502.06453](https://arxiv.org/abs/2502.06453)\n- [MATH-Perturb Project Page](https://math-perturb.github.io/)\n\n---\n\n### 8. MathCheck (ICLR 2025)\n**VERIFIED.** MathCheck is an ICLR 2025 paper titled \"Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist.\" Open code is confirmed at **github.com/PremiLab-Math/MathCheck**. Datasets are also on Hugging Face.\n\nSources:\n- [GitHub: PremiLab-Math/MathCheck](https://github.com/PremiLab-Math/MathCheck)\n- [Hugging Face: PremiLab-Math/MathCheck](https://huggingface.co/datasets/PremiLab-Math/MathCheck)\n- [arXiv: 2407.08733](https://arxiv.org/pdf/2407.08733)\n\n---\n\n### 9. Fox (2025, JEBS) -- IRT-BCSM\n**VERIFIED with a minor date nuance.** The paper \"Redefining Item Response Models for Small Samples\" by Jean-Paul Fox exists in the **Journal of Educational and Behavioral Statistics** (JEBS). It introduces the **IRT-BCSM** (IRT Bayesian Covariance Structure Model) for small samples of **N=50-100** persons. The DOI (10.3102/10769986241269886) indicates it was published online in 2024 but appears in JEBS Volume 50, Issue 2, 2025 (pp. 272-295). Citing it as \"Fox (2025)\" is consistent with the journal volume year. All substantive claims are accurate.\n\nSources:\n- [SAGE Journals: Redefining Item Response Models for Small Samples](https://journals.sagepub.com/doi/10.3102/10769986241269886)\n- [Fox PDF](https://www.jean-paulfox.com/Fox/documents/Papers/2024/fox-2024-redefining-item-response-models-for-small-samples.pdf)\n- [University of Twente Publication](https://research.utwente.nl/en/publications/redefining-item-response-models-for-small-samples)\n\n---\n\n## Summary\n\n| # | Claim | Verdict |\n|---|-------|---------|\n| 1 | AAAI 2027 deadlines (Jul 21 / Jul 28) | VERIFIED |\n| 2 | DeepSeek-R2 32B dense, MIT, single GPU, 92.7% AIME | VERIFIED |\n| 3 | Qwen3.6-27B, April 2026, Apache 2.0 | VERIFIED |\n| 4 | GLM-5.1 754B/40B active, MIT, Ascend 910B | VERIFIED |\n| 5 | DeepSeek-V4-Flash 284B | VERIFIED |\n| 6 | MathArena ~897 problems, includes AIME/HMMT/USAMO 2026 | **PARTIALLY -- competitions verified, but 897 problem count could not be corroborated** (paper says 162 in original; expanded version adds more but no source confirms ~897) |\n| 7 | MATH-Perturb ICML 2025, GitHub, 279 perturbations | VERIFIED |\n| 8 | MathCheck ICLR 2025, GitHub | VERIFIED |\n| 9 | Fox (2025, JEBS), IRT-BCSM, N=50-100 | VERIFIED |\n\nThe only claim that could not be fully verified is the MathArena problem count of ~897. All other claims are accurate based on available evidence."
      }
    ],
    "totalDurationMs": 120674,
    "totalTokens": 27312,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 23601,
      "output_tokens": 2819,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 891
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2819,
          "cache_read_input_tokens": 23601,
          "cache_creation_input_tokens": 891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 891,
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
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "aff85b37-00e8-486f-becf-802f1d2e612b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "3bdc3cd5-15c4-4efd-9240-720beaf0d8d0",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CRADE contamination-ability decomposition via gated IRT",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Tool result

_source line 18 · 2026-05-28T12:41:57.283Z_

<details><summary>↩ Tool result · `toolu_01YQUqHjX2v7kH8WhxNEijaV`</summary>

```text
I now have comprehensive evidence to provide a full verification report. Here is my analysis:

---

## Verification Report: Five Cited Papers

### 1. PSN-IRT (AAAI 2026 Oral)

**Paper exists: YES**

- **Title**: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" -- confirmed on [arXiv](https://arxiv.org/abs/2505.15055), [AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40814), and [GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT).
- **AAAI 2026 Oral**: CONFIRMED. ArXiv metadata states "Accepted to AAAI 2026 (Oral)."
- **4PL IRT**: CONFIRMED. The paper explicitly uses the "Four-Parameter Logistic (4PL) model" with parameters for difficulty (b), discriminability (a), guessing-rate (c), and feasibility (d).
- **Pseudo-Siamese neural estimation**: CONFIRMED. The framework is called "Pseudo-Siamese Network for Item Response Theory (PSN-IRT)."
- **12 LLMs on 41,871 items**: CONFIRMED. The GitHub repo states "evaluation results of 12 LLMs on 11 benchmarks, totaling 41,871 items."
- **Flags contamination via guessing-rate anomalies**: CONFIRMED. Finding 4 in the paper states: "Outlier-high guessing-rates in many benchmark items flag risks of data contamination."
- **Leaves contamination-corrected scoring as open question**: NOT CONFIRMED. The paper identifies contamination risks but does not explicitly frame contamination-corrected scoring as an open question or future work. The conclusion focuses on benchmark design improvements rather than remediation strategies. This claim appears to be an inference/interpretation rather than something the paper explicitly states.

**Verdict**: Paper and most claims verified. The claim about leaving "contamination-corrected scoring as an open question" is an overstatement -- the paper flags contamination but does not explicitly discuss corrected scoring.

---

### 2. DGM (Shu, Henson, Luecht, Psychometrika 2013)

**Paper exists: YES**

- **Title**: "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise" -- confirmed on [Springer](https://link.springer.com/article/10.1007/s11336-012-9311-3), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25106396/), and [ResearchGate](https://www.researchgate.net/publication/257678777).
- **Authors**: Zhan Shu, Robert Henson, Richard Luecht -- CONFIRMED (note: "Robert" not "R.A." but this is the same Robert A. Henson).
- **Published in Psychometrika 2013**: CONFIRMED. Psychometrika, Volume 78, Issue 3, pages 481-497, July 2013.
- **Gated IRT**: CONFIRMED. The paper introduces a "gated" function that decomposes performance.
- **Hierarchical MCMC**: CONFIRMED. "Hierarchical Markov Chain Monte Carlo is used as the model's estimation framework."
- **Decomposes performance into ability + preknowledge**: CONFIRMED. The gated function decomposes performance into "true ability distribution" and "cheating distribution" (cheating ability from preknowledge on exposed items). Note: the proposal's term "preknowledge" is accurate -- the paper uses the phrase "examinees having pre-knowledge on the exposed items." The decomposition is into "true ability" and "cheating ability" rather than literally "ability + preknowledge," but this is a fair characterization.

**Verdict**: Fully verified. All claims are accurate.

---

### 3. RankLLM (ICLR 2026)

**Paper exists: YES**

- **Title**: "Weighted Ranking of LLMs by Quantifying Question Difficulty" -- note the paper itself uses "RankLLM:" as a prefix. Confirmed on [arXiv](https://arxiv.org/abs/2602.12424) and [OpenReview](https://openreview.net/forum?id=jnX5GJIoYt).
- **ICLR 2026**: CONFIRMED, but it is a **Poster**, not a main conference paper or oral. OpenReview lists it as "ICLR 2026 Poster."
- **Non-parametric bidirectional score propagation**: CONFIRMED. The paper explicitly states: "RankLLM is non-parametric, avoids per-item logistic fits, and runs in linear time" and describes "bidirectional score propagation between models and questions."
- **90% human alignment**: CONFIRMED. The paper reports "90% agreement with human judgments."
- **30 models x 35,550 questions**: CONFIRMED. "We evaluate 30 models on 35,550 questions across multiple domains."
- **Robust to 50% model removal (rho=0.94)**: PARTIALLY ACCURATE. The actual reported value is mean Spearman rho = 0.9382 (SD = 0.0187) when 15 of 30 models are removed. Saying "rho=0.94" is a rounded approximation of 0.9382, which is reasonable but slightly inflated.

**Verdict**: Paper verified. The proposal's citation is missing the "Poster" distinction (just says "ICLR 2026"). The rho=0.94 claim is a slight rounding up from 0.9382. All other claims are accurate.

---

### 4. Wang et al. (ICLR 2026)

**Paper exists: YES**

- **Title**: "On The Fragility of Benchmark Contamination Detection in Reasoning Models" -- confirmed on [arXiv](https://arxiv.org/abs/2510.02386) and [OpenReview](https://openreview.net/forum?id=bhR00j6Mku).
- **Authors**: Han Wang, Haoyu Li, Brian Ko, Huan Zhang (UIUC and UW).
- **ICLR 2026**: CONFIRMED. Accepted as a **Poster** at ICLR 2026 (published January 26, 2026).
- **Proves likelihood-based detection fails on reasoning models**: PARTIALLY ACCURATE. The paper shows that detection methods relying on log-probability distributions fail after RL training (GRPO/PPO), because "log-prob distributions of members and non-members become increasingly similar." It is not limited to "likelihood-based" methods specifically -- it shows broader failure of memorization-based detection methods. The paper has a theoretical result (Theorem 3.1) showing clipping mechanisms inherently reduce member-nonmember separability.
- **AUROC approximately 50%**: CONFIRMED. Table 5 shows detection methods "consistently perform near random guess" with AUROC values clustered around 50-55% for post-RL models. Reference-free methods fall to near 50% AUROC after just 156 GRPO steps.

**Verdict**: Paper verified. The AUROC ~50% claim is accurate. The characterization as "likelihood-based detection" is slightly narrow -- the paper shows failure of multiple detection paradigms (memorization-based, log-probability-based) after RL training, not just likelihood-based methods per se.

---

### 5. JECS (arXiv May 2026)

**Paper exists: YES**

- **Title**: "Provable Joint Decontamination for Benchmarking Multiple Large Language Models" -- confirmed on [arXiv](https://arxiv.org/abs/2605.21543).
- **Authors**: Zhenlong Liu, Hao Zeng, Hongxin Wei.
- **arXiv May 2026**: CONFIRMED. Submitted May 20, 2026.
- **Proposes JECS**: CONFIRMED. The paper introduces "Joint Envelope Conformal Selection (JECS)" for controlling global contamination rate across multiple audited models.

**Verdict**: Fully verified. The paper exists and matches the description.

---

## Summary Table

| Paper | Exists? | Venue Correct? | Key Claims Accurate? | Issues Found |
|-------|---------|---------------|---------------------|--------------|
| PSN-IRT | Yes | Yes (AAAI 2026 Oral) | Mostly | "Contamination-corrected scoring as open question" is not explicitly stated in the paper |
| DGM | Yes | Yes (Psychometrika 2013) | Yes | None |
| RankLLM | Yes | Partially (ICLR 2026 Poster, not unspecified) | Mostly | rho=0.94 is rounded up from 0.9382 |
| Wang et al. | Yes | Partially (ICLR 2026 Poster) | Mostly | "Likelihood-based" is a narrower characterization than the paper's scope |
| JECS | Yes | Yes (arXiv May 2026) | Yes | None |

All five papers verifiably exist. Two minor accuracy issues were found: (1) the PSN-IRT paper does not explicitly frame contamination-corrected scoring as an open question, and (2) the RankLLM rho value is rounded up from 0.9382 to 0.94. Additionally, two papers (RankLLM and Wang et al.) are ICLR 2026 Posters specifically, which the proposal does not distinguish.

Sources:
- [PSN-IRT on arXiv](https://arxiv.org/abs/2505.15055)
- [PSN-IRT AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40814)
- [PSN-IRT GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT)
- [DGM on Springer](https://link.springer.com/article/10.1007/s11336-012-9311-3)
- [DGM on PubMed](https://pubmed.ncbi.nlm.nih.gov/25106396/)
- [RankLLM on arXiv](https://arxiv.org/abs/2602.12424)
- [RankLLM on OpenReview](https://openreview.net/forum?id=jnX5GJIoYt)
- [Wang et al. on arXiv](https://arxiv.org/abs/2510.02386)
- [Wang et al. on OpenReview](https://openreview.net/forum?id=bhR00j6Mku)
- [JECS on arXiv](https://arxiv.org/abs/2605.21543)

agentId: a5f681bcbfc7de52f (use SendMessage with to: 'a5f681bcbfc7de52f' to continue this agent)
&lt;usage>total_tokens: 24555
tool_uses: 20
duration_ms: 150558&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11f3a3d8-177d-4eeb-b72a-d0774ff270e7",
  "isSidechain": false,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "type": "user",
  "uuid": "080c5a6f-a8e6-4ea2-adfa-f0ef37c1d829",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal that cites several key papers. I need you to verify these specific papers exist and that the claims about them are accurate. Use WebSearch and WebFetch to verify each one.\n\n1. **PSN-IRT (AAAI 2026 Oral)**: \"Lost in Benchmarks? Rethinking LLM Benchmarking with Item Response Theory\" — Claims: 4PL IRT for 12 LLMs on 41,871 items via pseudo-Siamese neural estimation; flags contamination via guessing-rate anomalies but leaves corrected scoring as open question. Verify: Does this paper exist? Is it really AAAI 2026 Oral? Does it really use 12 models and 41,871 items? Does it really leave contamination-corrected scoring as open?\n\n2. **DGM (Shu, Henson, Luecht, Psychometrika 2013)**: \"Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise\" — Claims: gated IRT with hierarchical MCMC that decomposes performance into ability + preknowledge. Verify: Does this paper exist? Does it use gated IRT? Is it in Psychometrika 2013?\n\n3. **RankLLM (ICLR 2026)**: \"Weighted Ranking of LLMs by Quantifying Question Difficulty\" — Claims: non-parametric bidirectional score propagation achieving 90% human alignment on 30 models × 35,550 questions; robust to 50% model removal (ρ=0.94). Verify existence and claims.\n\n4. **Wang et al. (ICLR 2026)**: \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" — Claims: proves likelihood-based detection fails on reasoning models (AUROC ≈ 50%). Verify existence and claims.\n\n5. **JECS (arXiv May 2026)**: \"Provable Joint Decontamination for Benchmarking Multiple Large Language Models\" — Verify existence.\n\nSearch for each paper by title and by author names. Report what you find with specific evidence.",
    "agentId": "a5f681bcbfc7de52f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive evidence to provide a full verification report. Here is my analysis:\n\n---\n\n## Verification Report: Five Cited Papers\n\n### 1. PSN-IRT (AAAI 2026 Oral)\n\n**Paper exists: YES**\n\n- **Title**: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\" -- confirmed on [arXiv](https://arxiv.org/abs/2505.15055), [AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40814), and [GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT).\n- **AAAI 2026 Oral**: CONFIRMED. ArXiv metadata states \"Accepted to AAAI 2026 (Oral).\"\n- **4PL IRT**: CONFIRMED. The paper explicitly uses the \"Four-Parameter Logistic (4PL) model\" with parameters for difficulty (b), discriminability (a), guessing-rate (c), and feasibility (d).\n- **Pseudo-Siamese neural estimation**: CONFIRMED. The framework is called \"Pseudo-Siamese Network for Item Response Theory (PSN-IRT).\"\n- **12 LLMs on 41,871 items**: CONFIRMED. The GitHub repo states \"evaluation results of 12 LLMs on 11 benchmarks, totaling 41,871 items.\"\n- **Flags contamination via guessing-rate anomalies**: CONFIRMED. Finding 4 in the paper states: \"Outlier-high guessing-rates in many benchmark items flag risks of data contamination.\"\n- **Leaves contamination-corrected scoring as open question**: NOT CONFIRMED. The paper identifies contamination risks but does not explicitly frame contamination-corrected scoring as an open question or future work. The conclusion focuses on benchmark design improvements rather than remediation strategies. This claim appears to be an inference/interpretation rather than something the paper explicitly states.\n\n**Verdict**: Paper and most claims verified. The claim about leaving \"contamination-corrected scoring as an open question\" is an overstatement -- the paper flags contamination but does not explicitly discuss corrected scoring.\n\n---\n\n### 2. DGM (Shu, Henson, Luecht, Psychometrika 2013)\n\n**Paper exists: YES**\n\n- **Title**: \"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\" -- confirmed on [Springer](https://link.springer.com/article/10.1007/s11336-012-9311-3), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25106396/), and [ResearchGate](https://www.researchgate.net/publication/257678777).\n- **Authors**: Zhan Shu, Robert Henson, Richard Luecht -- CONFIRMED (note: \"Robert\" not \"R.A.\" but this is the same Robert A. Henson).\n- **Published in Psychometrika 2013**: CONFIRMED. Psychometrika, Volume 78, Issue 3, pages 481-497, July 2013.\n- **Gated IRT**: CONFIRMED. The paper introduces a \"gated\" function that decomposes performance.\n- **Hierarchical MCMC**: CONFIRMED. \"Hierarchical Markov Chain Monte Carlo is used as the model's estimation framework.\"\n- **Decomposes performance into ability + preknowledge**: CONFIRMED. The gated function decomposes performance into \"true ability distribution\" and \"cheating distribution\" (cheating ability from preknowledge on exposed items). Note: the proposal's term \"preknowledge\" is accurate -- the paper uses the phrase \"examinees having pre-knowledge on the exposed items.\" The decomposition is into \"true ability\" and \"cheating ability\" rather than literally \"ability + preknowledge,\" but this is a fair characterization.\n\n**Verdict**: Fully verified. All claims are accurate.\n\n---\n\n### 3. RankLLM (ICLR 2026)\n\n**Paper exists: YES**\n\n- **Title**: \"Weighted Ranking of LLMs by Quantifying Question Difficulty\" -- note the paper itself uses \"RankLLM:\" as a prefix. Confirmed on [arXiv](https://arxiv.org/abs/2602.12424) and [OpenReview](https://openreview.net/forum?id=jnX5GJIoYt).\n- **ICLR 2026**: CONFIRMED, but it is a **Poster**, not a main conference paper or oral. OpenReview lists it as \"ICLR 2026 Poster.\"\n- **Non-parametric bidirectional score propagation**: CONFIRMED. The paper explicitly states: \"RankLLM is non-parametric, avoids per-item logistic fits, and runs in linear time\" and describes \"bidirectional score propagation between models and questions.\"\n- **90% human alignment**: CONFIRMED. The paper reports \"90% agreement with human judgments.\"\n- **30 models x 35,550 questions**: CONFIRMED. \"We evaluate 30 models on 35,550 questions across multiple domains.\"\n- **Robust to 50% model removal (rho=0.94)**: PARTIALLY ACCURATE. The actual reported value is mean Spearman rho = 0.9382 (SD = 0.0187) when 15 of 30 models are removed. Saying \"rho=0.94\" is a rounded approximation of 0.9382, which is reasonable but slightly inflated.\n\n**Verdict**: Paper verified. The proposal's citation is missing the \"Poster\" distinction (just says \"ICLR 2026\"). The rho=0.94 claim is a slight rounding up from 0.9382. All other claims are accurate.\n\n---\n\n### 4. Wang et al. (ICLR 2026)\n\n**Paper exists: YES**\n\n- **Title**: \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" -- confirmed on [arXiv](https://arxiv.org/abs/2510.02386) and [OpenReview](https://openreview.net/forum?id=bhR00j6Mku).\n- **Authors**: Han Wang, Haoyu Li, Brian Ko, Huan Zhang (UIUC and UW).\n- **ICLR 2026**: CONFIRMED. Accepted as a **Poster** at ICLR 2026 (published January 26, 2026).\n- **Proves likelihood-based detection fails on reasoning models**: PARTIALLY ACCURATE. The paper shows that detection methods relying on log-probability distributions fail after RL training (GRPO/PPO), because \"log-prob distributions of members and non-members become increasingly similar.\" It is not limited to \"likelihood-based\" methods specifically -- it shows broader failure of memorization-based detection methods. The paper has a theoretical result (Theorem 3.1) showing clipping mechanisms inherently reduce member-nonmember separability.\n- **AUROC approximately 50%**: CONFIRMED. Table 5 shows detection methods \"consistently perform near random guess\" with AUROC values clustered around 50-55% for post-RL models. Reference-free methods fall to near 50% AUROC after just 156 GRPO steps.\n\n**Verdict**: Paper verified. The AUROC ~50% claim is accurate. The characterization as \"likelihood-based detection\" is slightly narrow -- the paper shows failure of multiple detection paradigms (memorization-based, log-probability-based) after RL training, not just likelihood-based methods per se.\n\n---\n\n### 5. JECS (arXiv May 2026)\n\n**Paper exists: YES**\n\n- **Title**: \"Provable Joint Decontamination for Benchmarking Multiple Large Language Models\" -- confirmed on [arXiv](https://arxiv.org/abs/2605.21543).\n- **Authors**: Zhenlong Liu, Hao Zeng, Hongxin Wei.\n- **arXiv May 2026**: CONFIRMED. Submitted May 20, 2026.\n- **Proposes JECS**: CONFIRMED. The paper introduces \"Joint Envelope Conformal Selection (JECS)\" for controlling global contamination rate across multiple audited models.\n\n**Verdict**: Fully verified. The paper exists and matches the description.\n\n---\n\n## Summary Table\n\n| Paper | Exists? | Venue Correct? | Key Claims Accurate? | Issues Found |\n|-------|---------|---------------|---------------------|--------------|\n| PSN-IRT | Yes | Yes (AAAI 2026 Oral) | Mostly | \"Contamination-corrected scoring as open question\" is not explicitly stated in the paper |\n| DGM | Yes | Yes (Psychometrika 2013) | Yes | None |\n| RankLLM | Yes | Partially (ICLR 2026 Poster, not unspecified) | Mostly | rho=0.94 is rounded up from 0.9382 |\n| Wang et al. | Yes | Partially (ICLR 2026 Poster) | Mostly | \"Likelihood-based\" is a narrower characterization than the paper's scope |\n| JECS | Yes | Yes (arXiv May 2026) | Yes | None |\n\nAll five papers verifiably exist. Two minor accuracy issues were found: (1) the PSN-IRT paper does not explicitly frame contamination-corrected scoring as an open question, and (2) the RankLLM rho value is rounded up from 0.9382 to 0.94. Additionally, two papers (RankLLM and Wang et al.) are ICLR 2026 Posters specifically, which the proposal does not distinguish.\n\nSources:\n- [PSN-IRT on arXiv](https://arxiv.org/abs/2505.15055)\n- [PSN-IRT AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40814)\n- [PSN-IRT GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT)\n- [DGM on Springer](https://link.springer.com/article/10.1007/s11336-012-9311-3)\n- [DGM on PubMed](https://pubmed.ncbi.nlm.nih.gov/25106396/)\n- [RankLLM on arXiv](https://arxiv.org/abs/2602.12424)\n- [RankLLM on OpenReview](https://openreview.net/forum?id=jnX5GJIoYt)\n- [Wang et al. on arXiv](https://arxiv.org/abs/2510.02386)\n- [Wang et al. on OpenReview](https://openreview.net/forum?id=bhR00j6Mku)\n- [JECS on arXiv](https://arxiv.org/abs/2605.21543)"
      }
    ],
    "totalDurationMs": 150558,
    "totalTokens": 24555,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 21063,
      "output_tokens": 2652,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2652,
          "cache_read_input_tokens": 21063,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 839,
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
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "11f3a3d8-177d-4eeb-b72a-d0774ff270e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T12:42:11.342Z_

<details><summary>↩ Tool result · `toolu_01XtRSQ4i1tV2D2sGwHEnYrw`</summary>

```text
Now I have all the information needed. Here is the comprehensive verification report.

---

## Verification Report for 8 Cited Papers

### 1. DCR (EMNLP 2025): "Quantifying Data Contamination in LLMs Evaluation"

- **Exists?** Yes. Published in Proceedings of EMNLP 2025, pages 23002-23020.
- **Venue correct?** Yes, EMNLP 2025 is correct. Available at [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1173/).
- **Claims verification:**
  - "Fuzzy inference across four contamination levels" -- **Accurate.** The four levels are semantic, informational, data, and label.
  - "Ad-hoc multiplicative correction Acc_adj = Acc x (1 - DCR Factor)" -- **Accurate.** This is the exact formula used in the paper, though the authors note it is not a "perfect" decontaminated score but rather one that "incorporates BDC risk considerations."
  - "r=0.66 on hard tasks" -- **Partially inaccurate / misleading.** The r=0.66 (specifically r=0.6569) is for the LIAR2 benchmark (fake news detection), not for "hard tasks" generically. The other benchmarks show much higher correlations: SST-2 (r=0.92) and GSM8K (r=0.86). The weaker LIAR2 correlation reflects that it is a newer 2024 benchmark with less contamination exposure, not that it is harder.

### 2. ConStat (NeurIPS 2024): "Performance-Based Contamination Detection in Large Language Models"

- **Exists?** Yes. Published at NeurIPS 2024.
- **Venue correct?** Yes. Available at [NeurIPS proceedings](https://neurips.cc/virtual/2024/poster/96266) and [OpenReview](https://openreview.net/forum?id=ALISPmDPCq).
- **Claims verification:**
  - "Detects contamination via performance gaps on rephrased samples" -- **Accurate.** ConStat detects performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.
  - "Against reference models" -- **Accurate.** The method compares performance between a primary and reference benchmark relative to a set of reference models.

### 3. RIDE (arXiv 2025): "Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning"

- **Exists?** Yes. Available at [arXiv:2511.04120](https://arxiv.org/abs/2511.04120).
- **Venue correct?** The arXiv preprint was posted January 31, 2026 (not 2025). The arXiv ID prefix 2511 suggests it was first submitted in November 2025, but the actual posting date is January 2026. Also submitted to OpenReview. Calling it "arXiv 2025" is borderline -- the submission may have been late 2025, but posting was 2026.
- **Claims verification:**
  - "Uses IRT as difficulty reward for RL-based question rewriting" -- **Accurate.** IRT-derived difficulty measurements serve as reward signals for RL.
  - "RIDE-8B" -- **Accurate.** The rewriting model is based on Qwen3-8B fine-tuned via SFT and RL, and is referred to as RIDE-8B in the paper. A RIDE-4B variant also exists.

### 4. PaCoST (arXiv 2024): "Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs"

- **Exists?** Yes. Available at [arXiv:2406.18326](https://arxiv.org/abs/2406.18326).
- **Venue correct?** Partially. The paper was posted on arXiv in June 2024, but it was also **accepted at EMNLP 2024 Findings**. Citing it as merely "arXiv 2024" understates its publication status.
- **Claims verification:**
  - "Paired original-perturbed items" -- **Accurate.** The method constructs counterparts for each data point with the same distribution and compares model confidence between original and perturbed versions using a paired statistical significance test.

### 5. "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration" (arXiv April 2026)

- **Exists?** Yes. Available at [arXiv:2604.12843](https://arxiv.org/abs/2604.12843), published April 15, 2026.
- **Venue correct?** Yes, arXiv April 2026 is correct.
- **Content summary:** Proposes a framework based on multidimensional IRT using anchor items and fixed parameter calibration to make LLM benchmarking extensible and efficient. Achieves 2-3% prediction error using only 100 anchor questions per dataset.

### 6. "The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models" (arXiv April 2026)

- **Exists?** Yes. Available at [arXiv:2603.22816](https://arxiv.org/abs/2603.22816).
- **Venue correct?** The arXiv ID prefix is 2603 (March 2026), and the posting date is April 6, 2026. Saying "arXiv April 2026" is approximately correct (it appeared in early April), though the ID suggests March 2026 submission.
- **Content summary:** Introduces step-level faithfulness evaluation for chain-of-thought reasoning. Identifies three modes: genuine reasoning, scaffolding, and decoration. Tests 13 frontier models across six domains.

### 7. San Martin et al. (Psychometrika 2024): "On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory"

- **Exists?** Yes. Published in Psychometrika, Volume 89, Issue 2, pages 486-516, June 2024.
- **Venue correct?** Yes, Psychometrika 2024 is correct.
- **Author attribution issue:** The paper is authored by **Noventa, Ye, Kelava, and Spoto** -- there is no author named "San Martin." San Martin is frequently *cited* within the paper as a researcher whose prior work on IRT identifiability is discussed, but he is not an author. **The attribution "San Martin et al." is incorrect.**

### 8. py-irt (IJOC 2023): "A Scalable Item Response Theory Library for Python"

- **Exists?** Yes. Published in INFORMS Journal on Computing, Volume 35, Issue 1, pages 5-13, January 2023.
- **Venue correct?** Yes, IJOC 2023 is correct. Available at [INFORMS](https://pubsonline.informs.org/doi/10.1287/ijoc.2022.1250).
- **Content:** Authored by John Patrick Lalor and Pedro Rodriguez. A Python library for fitting Bayesian IRT models, built on Pyro/PyTorch with GPU-accelerated training.

---

## Summary of Issues Found

| Paper | Exists | Venue Correct | Claims Accurate |
|-------|--------|---------------|-----------------|
| DCR | Yes | Yes (EMNLP 2025) | Mostly -- "r=0.66 on hard tasks" is misleading; r=0.66 is for LIAR2 (a newer benchmark), not "hard tasks" |
| ConStat | Yes | Yes (NeurIPS 2024) | Yes |
| RIDE | Yes | Borderline -- posted Jan 2026, not 2025 | Yes, including RIDE-8B |
| PaCoST | Yes | Understated -- also accepted at EMNLP 2024 Findings | Yes |
| Growing Pains | Yes | Yes (arXiv April 2026) | N/A (existence check only) |
| Illusion of Reasoning | Yes | Approximately (arXiv March/April 2026) | N/A (existence check only) |
| San Martin et al. | Yes (paper exists) | Yes (Psychometrika 2024) | **Wrong attribution** -- authors are Noventa, Ye, Kelava, and Spoto, not San Martin |
| py-irt | Yes | Yes (IJOC 2023) | N/A (existence check only) |

**Key red flag:** Paper 7 has an incorrect author attribution. The proposal cites it as "San Martin et al." but the actual authors are Noventa et al. (2024). San Martin is merely cited within that paper.

Sources:
- [DCR at ACL Anthology](https://aclanthology.org/2025.emnlp-main.1173/)
- [DCR on arXiv](https://arxiv.org/abs/2507.11405)
- [ConStat at OpenReview](https://openreview.net/forum?id=ALISPmDPCq)
- [ConStat at NeurIPS](https://neurips.cc/virtual/2024/poster/96266)
- [RIDE on arXiv](https://arxiv.org/abs/2511.04120)
- [PaCoST on arXiv](https://arxiv.org/abs/2406.18326)
- [Growing Pains on arXiv](https://arxiv.org/abs/2604.12843)
- [Illusion of Reasoning on arXiv](https://arxiv.org/abs/2603.22816)
- [Noventa et al. on PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11164782/)
- [Noventa et al. at Cambridge Core](https://www.cambridge.org/core/journals/psychometrika/article/on-the-identifiability-of-3-and-4parameter-item-response-theory-models-from-the-perspective-of-knowledge-space-theory/8CC5CF0869C7EBDE17CF4BAC34DECB06)
- [py-irt at INFORMS](https://pubsonline.informs.org/doi/10.1287/ijoc.2022.1250)
- [py-irt on arXiv](https://arxiv.org/abs/2203.01282)

agentId: a0ec8c40fd16e28d5 (use SendMessage with to: 'a0ec8c40fd16e28d5' to continue this agent)
&lt;usage>total_tokens: 23476
tool_uses: 18
duration_ms: 130551&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9d8379a-1aea-4b81-aab7-47f796bb6c4d",
  "isSidechain": false,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "type": "user",
  "uuid": "cfad1c99-d650-4c44-a24d-ba092e530497",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several papers cited in a research proposal. Use WebSearch and WebFetch to check each:\n\n1. **DCR (EMNLP 2025)**: \"Quantifying Data Contamination in LLMs Evaluation\" — Claims: fuzzy inference across four contamination levels, ad-hoc multiplicative correction Acc_adj = Acc × (1 − DCR Factor), r=0.66 on hard tasks. Verify it exists at EMNLP 2025 and check the claims.\n\n2. **ConStat (NeurIPS 2024)**: \"Performance-Based Contamination Detection in Large Language Models\" — Claims: detects contamination via performance gaps on rephrased samples against reference models. Verify.\n\n3. **RIDE (arXiv 2025)**: \"Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning\" — Claims: uses IRT as difficulty reward for RL-based question rewriting via RIDE-8B. Verify.\n\n4. **PaCoST (arXiv 2024)**: \"Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs\" — Verify existence and claims about paired original-perturbed items.\n\n5. **\"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\" (arXiv April 2026)** — Verify existence.\n\n6. **\"The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models\" (arXiv April 2026)** — Verify existence.\n\n7. **San Martin et al. (Psychometrika 2024)**: \"On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory\" — Verify.\n\n8. **py-irt (IJOC 2023)**: \"A Scalable Item Response Theory Library for Python\" — Verify existence.\n\nFor each, report: does it exist? Is the venue correct? Are the claims about its content accurate?",
    "agentId": "a0ec8c40fd16e28d5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here is the comprehensive verification report.\n\n---\n\n## Verification Report for 8 Cited Papers\n\n### 1. DCR (EMNLP 2025): \"Quantifying Data Contamination in LLMs Evaluation\"\n\n- **Exists?** Yes. Published in Proceedings of EMNLP 2025, pages 23002-23020.\n- **Venue correct?** Yes, EMNLP 2025 is correct. Available at [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1173/).\n- **Claims verification:**\n  - \"Fuzzy inference across four contamination levels\" -- **Accurate.** The four levels are semantic, informational, data, and label.\n  - \"Ad-hoc multiplicative correction Acc_adj = Acc x (1 - DCR Factor)\" -- **Accurate.** This is the exact formula used in the paper, though the authors note it is not a \"perfect\" decontaminated score but rather one that \"incorporates BDC risk considerations.\"\n  - \"r=0.66 on hard tasks\" -- **Partially inaccurate / misleading.** The r=0.66 (specifically r=0.6569) is for the LIAR2 benchmark (fake news detection), not for \"hard tasks\" generically. The other benchmarks show much higher correlations: SST-2 (r=0.92) and GSM8K (r=0.86). The weaker LIAR2 correlation reflects that it is a newer 2024 benchmark with less contamination exposure, not that it is harder.\n\n### 2. ConStat (NeurIPS 2024): \"Performance-Based Contamination Detection in Large Language Models\"\n\n- **Exists?** Yes. Published at NeurIPS 2024.\n- **Venue correct?** Yes. Available at [NeurIPS proceedings](https://neurips.cc/virtual/2024/poster/96266) and [OpenReview](https://openreview.net/forum?id=ALISPmDPCq).\n- **Claims verification:**\n  - \"Detects contamination via performance gaps on rephrased samples\" -- **Accurate.** ConStat detects performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.\n  - \"Against reference models\" -- **Accurate.** The method compares performance between a primary and reference benchmark relative to a set of reference models.\n\n### 3. RIDE (arXiv 2025): \"Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning\"\n\n- **Exists?** Yes. Available at [arXiv:2511.04120](https://arxiv.org/abs/2511.04120).\n- **Venue correct?** The arXiv preprint was posted January 31, 2026 (not 2025). The arXiv ID prefix 2511 suggests it was first submitted in November 2025, but the actual posting date is January 2026. Also submitted to OpenReview. Calling it \"arXiv 2025\" is borderline -- the submission may have been late 2025, but posting was 2026.\n- **Claims verification:**\n  - \"Uses IRT as difficulty reward for RL-based question rewriting\" -- **Accurate.** IRT-derived difficulty measurements serve as reward signals for RL.\n  - \"RIDE-8B\" -- **Accurate.** The rewriting model is based on Qwen3-8B fine-tuned via SFT and RL, and is referred to as RIDE-8B in the paper. A RIDE-4B variant also exists.\n\n### 4. PaCoST (arXiv 2024): \"Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs\"\n\n- **Exists?** Yes. Available at [arXiv:2406.18326](https://arxiv.org/abs/2406.18326).\n- **Venue correct?** Partially. The paper was posted on arXiv in June 2024, but it was also **accepted at EMNLP 2024 Findings**. Citing it as merely \"arXiv 2024\" understates its publication status.\n- **Claims verification:**\n  - \"Paired original-perturbed items\" -- **Accurate.** The method constructs counterparts for each data point with the same distribution and compares model confidence between original and perturbed versions using a paired statistical significance test.\n\n### 5. \"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\" (arXiv April 2026)\n\n- **Exists?** Yes. Available at [arXiv:2604.12843](https://arxiv.org/abs/2604.12843), published April 15, 2026.\n- **Venue correct?** Yes, arXiv April 2026 is correct.\n- **Content summary:** Proposes a framework based on multidimensional IRT using anchor items and fixed parameter calibration to make LLM benchmarking extensible and efficient. Achieves 2-3% prediction error using only 100 anchor questions per dataset.\n\n### 6. \"The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models\" (arXiv April 2026)\n\n- **Exists?** Yes. Available at [arXiv:2603.22816](https://arxiv.org/abs/2603.22816).\n- **Venue correct?** The arXiv ID prefix is 2603 (March 2026), and the posting date is April 6, 2026. Saying \"arXiv April 2026\" is approximately correct (it appeared in early April), though the ID suggests March 2026 submission.\n- **Content summary:** Introduces step-level faithfulness evaluation for chain-of-thought reasoning. Identifies three modes: genuine reasoning, scaffolding, and decoration. Tests 13 frontier models across six domains.\n\n### 7. San Martin et al. (Psychometrika 2024): \"On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory\"\n\n- **Exists?** Yes. Published in Psychometrika, Volume 89, Issue 2, pages 486-516, June 2024.\n- **Venue correct?** Yes, Psychometrika 2024 is correct.\n- **Author attribution issue:** The paper is authored by **Noventa, Ye, Kelava, and Spoto** -- there is no author named \"San Martin.\" San Martin is frequently *cited* within the paper as a researcher whose prior work on IRT identifiability is discussed, but he is not an author. **The attribution \"San Martin et al.\" is incorrect.**\n\n### 8. py-irt (IJOC 2023): \"A Scalable Item Response Theory Library for Python\"\n\n- **Exists?** Yes. Published in INFORMS Journal on Computing, Volume 35, Issue 1, pages 5-13, January 2023.\n- **Venue correct?** Yes, IJOC 2023 is correct. Available at [INFORMS](https://pubsonline.informs.org/doi/10.1287/ijoc.2022.1250).\n- **Content:** Authored by John Patrick Lalor and Pedro Rodriguez. A Python library for fitting Bayesian IRT models, built on Pyro/PyTorch with GPU-accelerated training.\n\n---\n\n## Summary of Issues Found\n\n| Paper | Exists | Venue Correct | Claims Accurate |\n|-------|--------|---------------|-----------------|\n| DCR | Yes | Yes (EMNLP 2025) | Mostly -- \"r=0.66 on hard tasks\" is misleading; r=0.66 is for LIAR2 (a newer benchmark), not \"hard tasks\" |\n| ConStat | Yes | Yes (NeurIPS 2024) | Yes |\n| RIDE | Yes | Borderline -- posted Jan 2026, not 2025 | Yes, including RIDE-8B |\n| PaCoST | Yes | Understated -- also accepted at EMNLP 2024 Findings | Yes |\n| Growing Pains | Yes | Yes (arXiv April 2026) | N/A (existence check only) |\n| Illusion of Reasoning | Yes | Approximately (arXiv March/April 2026) | N/A (existence check only) |\n| San Martin et al. | Yes (paper exists) | Yes (Psychometrika 2024) | **Wrong attribution** -- authors are Noventa, Ye, Kelava, and Spoto, not San Martin |\n| py-irt | Yes | Yes (IJOC 2023) | N/A (existence check only) |\n\n**Key red flag:** Paper 7 has an incorrect author attribution. The proposal cites it as \"San Martin et al.\" but the actual authors are Noventa et al. (2024). San Martin is merely cited within that paper.\n\nSources:\n- [DCR at ACL Anthology](https://aclanthology.org/2025.emnlp-main.1173/)\n- [DCR on arXiv](https://arxiv.org/abs/2507.11405)\n- [ConStat at OpenReview](https://openreview.net/forum?id=ALISPmDPCq)\n- [ConStat at NeurIPS](https://neurips.cc/virtual/2024/poster/96266)\n- [RIDE on arXiv](https://arxiv.org/abs/2511.04120)\n- [PaCoST on arXiv](https://arxiv.org/abs/2406.18326)\n- [Growing Pains on arXiv](https://arxiv.org/abs/2604.12843)\n- [Illusion of Reasoning on arXiv](https://arxiv.org/abs/2603.22816)\n- [Noventa et al. on PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11164782/)\n- [Noventa et al. at Cambridge Core](https://www.cambridge.org/core/journals/psychometrika/article/on-the-identifiability-of-3-and-4parameter-item-response-theory-models-from-the-perspective-of-knowledge-space-theory/8CC5CF0869C7EBDE17CF4BAC34DECB06)\n- [py-irt at INFORMS](https://pubsonline.informs.org/doi/10.1287/ijoc.2022.1250)\n- [py-irt on arXiv](https://arxiv.org/abs/2203.01282)"
      }
    ],
    "totalDurationMs": 130551,
    "totalTokens": 23476,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 20692,
      "output_tokens": 2596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 187
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2596,
          "cache_read_input_tokens": 20692,
          "cache_creation_input_tokens": 187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 187,
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
  "sourceToolAssistantUUID": "f9d8379a-1aea-4b81-aab7-47f796bb6c4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "cfad1c99-d650-4c44-a24d-ba092e530497",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CRADE contamination-ability decomposition via gated IRT",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Tool result

_source line 22 · 2026-05-28T12:42:11.922Z_

<details><summary>↩ Tool result · `toolu_01FdgRhANzbhX2LDb9xVfXXP`</summary>

```text
Now I have comprehensive results from all searches. Here is my full analysis.

---

## Adversarial Literature Search Report: CRADE (IRT + Contamination Detection + Adversarial Robustness)

I conducted 10 specified searches plus 7 follow-up targeted searches. Below are the findings organized by search query, followed by an overall competitive threat assessment.

---

### Search 1: "contamination-aware IRT" OR "contamination item response theory" LLM 2025 2026

**Found:** No paper uses the exact phrase "contamination-aware IRT." However, several papers apply IRT to LLM benchmarking:
- **PSN-IRT** (Zhou et al., AAAI 2026 Oral) -- uses IRT to audit benchmark quality and explicitly flags contaminated items as a quality problem. Does NOT model contamination as a latent variable or correct for it within the IRT framework.
- **IRT-Router** (Song et al., ACL 2025) -- uses IRT for LLM routing, no contamination angle.
- **Diagnosing LLM-as-a-Judge via IRT** (2026) -- applies IRT-GRM to judge reliability, no contamination.

**Three-way intersection?** No. PSN-IRT is closest (IRT + contamination awareness) but has no adversarial robustness component.

---

### Search 2: "benchmark contamination correction" "item response theory" 2026

**Found:** PSN-IRT again dominates. It identifies contaminated items and removes them to create cleaner benchmarks, but does not perform contamination *correction* within the IRT model itself (e.g., jointly estimating ability and contamination parameters). No adversarial component.

**Three-way intersection?** No.

---

### Search 3: "decontamination" "IRT" "large language model" 2026

**Found:** Two separate threads that do NOT intersect:
- **Inference-Time Decontamination (ITD)** and **DeconIEP** -- decontamination methods that operate at inference time by rewriting or perturbing leaked samples. No IRT component.
- **PSN-IRT** -- IRT-based benchmark analysis. No decontamination mechanism.

**Three-way intersection?** No.

---

### Search 4: "gated IRT" language model

**Found:** Only results for gated recurrent/convolutional language models from 2016-2019. No paper proposes a "gated IRT" model where a contamination gate modulates item parameters. This specific architectural idea appears novel.

**Three-way intersection?** No results at all.

---

### Search 5: site:arxiv.org "contamination" "adversarial" "IRT" LLM evaluation 2026

**Found:** No single paper addressing all three terms together. The results split into:
- Contamination detection surveys (Min-K%, ConStat, canary GUIDs)
- Adversarial evaluation (perturbation-based)
- IRT for benchmarking (PSN-IRT)

A critical find here: **"LLM Benchmark Datasets Should Be Contamination-Resistant"** (arxiv 2605.19999, May 2026) -- very recent, evaluates contamination resistance methods. No IRT component.

**Three-way intersection?** No.

---

### Search 6: site:openreview.net contamination IRT LLM evaluation 2026

**Found:** Multiple contamination-focused papers at ICLR 2026 and in review:
- **Auditing Test Data Contamination with Error Rate Control** (ICLR 2026)
- **The Emperor's New Clothes in Benchmarking** -- tests 20 mitigation strategies and finds none effectively balances fidelity and contamination resistance
- **Detecting Benchmark Contamination Through Watermarking**
- **Knowledge Distillation as Decontamination** (ICLR 2026)
- **LiveBench** -- contamination-limited benchmark

None of these use IRT. None combine IRT with contamination or adversarial robustness.

**Three-way intersection?** No.

---

### Search 7: "joint contamination ability" OR "contamination-adjusted scoring" LLM 2026

**Found:** The closest competitor in the contamination-adjustment space:
- **DCR: Data Contamination Rating** (EMNLP 2025) -- uses a fuzzy inference system to produce a contamination factor that adjusts raw accuracy. Validated on 9 LLMs. This is a contamination-adjusted scoring system, but it does NOT use IRT. It uses heuristic fuzzy logic, not psychometric measurement theory. No adversarial component.
- **"Silicon Bureaucracy and AI Test-Oriented Education"** (arxiv 2603.21636, March 2026) -- proposes an audit framework that compares clean vs. noisy conditions (where benchmark problems are deleted, rewritten, perturbed). This has contamination sensitivity + adversarial perturbation but NO IRT.

**Three-way intersection?** No, but these are the two most relevant partial competitors:
- DCR covers contamination-adjusted scoring (without IRT)
- Silicon Bureaucracy covers contamination + adversarial perturbation (without IRT)

---

### Search 8: "benchmark integrity" "measurement theory" LLM 2025 2026

**Found:**
- **Benchmark Health Index (BHI)** (Feb 2026) -- meta-analyzes 106 benchmarks across discrimination, saturation, and impact. Uses measurement concepts but NOT formal IRT. No contamination correction or adversarial robustness.
- **Quantifying Construct Validity in LLM Evaluations** (Feb 2026) -- applies validity theory to LLM benchmarks. Addresses measurement rigor but not contamination or adversarial robustness.

**Three-way intersection?** No.

---

### Search 9: "paired item" contamination LLM evaluation

**Found:**
- **PaCoST (Paired Confidence Significance Testing)** -- constructs paired counterparts to detect benchmark contamination via statistical confidence analysis. This is a contamination detection method using paired items but has NO IRT and NO adversarial robustness component.
- **"Quantifying Data Contamination in Psychometric Evaluations of LLMs"** (Han et al., EACL 2026 Findings) -- measures memorization and contamination in psychometric inventories (BFI-44, PVQ-40). Uses psychometric instruments but NOT IRT for ability estimation. Focuses on personality/values questionnaires, not capability benchmarks. No adversarial component.

**Three-way intersection?** No.

---

### Search 10: site:arxiv.org "psychometric" "contamination" "language model" 2026

**Found:** The Han et al. EACL 2026 paper again. This is the closest to combining psychometrics with contamination, but it studies contamination OF psychometric tests (whether LLMs have memorized personality questionnaires), not contamination-aware psychometric scoring of LLM ability. No IRT model is used; no adversarial component.

**Three-way intersection?** No.

---

### Follow-up: RIDE (IRT + Adversarial, most relevant partial overlap)

**RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning** (late 2025 / early 2026, OpenReview)

This is a significant find. RIDE uses IRT to measure question difficulty, then uses IRT-derived difficulty as a reward signal to train an adversarial question rewriter via reinforcement learning. It explicitly notes that strong benchmark performance may stem from contamination/memorization, and generates adversarial variants to test robustness. Average performance drops 21.73% across 26 models.

**RIDE covers two of the three legs: IRT + adversarial perturbation.** It mentions contamination as a motivation but does NOT model contamination as a latent variable, does NOT jointly estimate contamination and ability, and does NOT propose contamination-aware IRT parameters. It is an adversarial benchmark construction tool, not a contamination-correcting measurement framework.

---

## Overall Assessment

### Papers occupying partial intersections (ranked by threat level):

| Paper | IRT | Contamination | Adversarial | Threat to CRADE |
|-------|-----|---------------|-------------|-----------------|
| **RIDE** (2025-2026) | Yes (difficulty estimation) | Motivation only | Yes (adversarial rewriting) | **MODERATE** -- covers IRT + adversarial but not contamination modeling |
| **PSN-IRT** (AAAI 2026 Oral) | Yes (full IRT framework) | Identifies contaminated items | No | **MODERATE** -- covers IRT + contamination detection but not adversarial |
| **Silicon Bureaucracy** (Mar 2026) | No | Yes (sensitivity auditing) | Yes (perturbation-based) | **LOW-MODERATE** -- covers contamination + adversarial without IRT |
| **DCR** (EMNLP 2025) | No | Yes (contamination-adjusted scoring) | No | **LOW** -- contamination correction without IRT |
| **Han et al.** (EACL 2026) | No (psychometric but not IRT) | Yes (psychometric contamination) | No | **LOW** -- different domain (personality, not capability) |
| **BHI** (Feb 2026) | No (measurement-inspired but not IRT) | No | No | **NEGLIGIBLE** |

### Key Conclusion

**No paper was found that occupies the three-way intersection of IRT + contamination detection/correction + adversarial robustness.** The CRADE proposal's claim of novelty at this intersection appears to hold as of late May 2026.

However, the authors should be aware of and cite these partial competitors:

1. **RIDE** is the most dangerous near-miss -- it uses IRT-guided adversarial perturbation and is motivated by contamination concerns. A reviewer could argue RIDE is "close enough." CRADE must clearly differentiate by emphasizing its contamination-as-latent-variable modeling within IRT, which RIDE entirely lacks.

2. **PSN-IRT** (AAAI 2026 Oral) is a high-visibility paper that uses IRT and explicitly addresses contamination in benchmarks. CRADE must differentiate by showing that PSN-IRT only *detects and removes* contaminated items rather than *correcting for contamination within the model*.

3. **Silicon Bureaucracy** (March 2026) combines contamination auditing with adversarial perturbation. It lacks IRT but is conceptually adjacent. The CRADE authors should cite it.

4. **DCR** provides contamination-adjusted scoring, which is conceptually similar to what CRADE presumably does, but uses fuzzy logic rather than IRT. CRADE should position itself as the principled psychometric alternative.

---

Sources:
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026)](https://arxiv.org/abs/2505.15055)
- [PSN-IRT GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT)
- [IRT-Router (ACL 2025)](https://arxiv.org/abs/2506.01048)
- [Diagnosing LLM-as-a-Judge via IRT (2026)](https://arxiv.org/pdf/2602.00521)
- [RIDE: Difficulty Evolving Perturbation with IRT](https://arxiv.org/pdf/2511.04120)
- [Silicon Bureaucracy and AI Test-Oriented Education (2026)](https://arxiv.org/abs/2603.21636)
- [DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)](https://arxiv.org/abs/2507.11405)
- [Quantifying Data Contamination in Psychometric Evaluations of LLMs (EACL 2026)](https://arxiv.org/abs/2510.07175)
- [Benchmark Health Index (2026)](https://arxiv.org/pdf/2602.11674)
- [LLM Benchmark Datasets Should Be Contamination-Resistant (May 2026)](https://arxiv.org/html/2605.19999v1)
- [When Benchmarks Leak: Inference-Time Decontamination (2026)](https://arxiv.org/abs/2601.19334)
- [The Emperor's New Clothes in Benchmarking (OpenReview)](https://openreview.net/forum?id=TuvDxubEfE)
- [Auditing Test Data Contamination with Error Rate Control (OpenReview)](https://openreview.net/forum?id=YsoabhpS7z)
- [Detecting Benchmark Contamination Through Watermarking (OpenReview)](https://openreview.net/forum?id=WFGxFzFDmQ)
- [LiveBench (OpenReview)](https://openreview.net/forum?id=sKYHBTAxVa)
- [Towards Contamination Resistant Benchmarks](https://arxiv.org/pdf/2505.08389)
- [Quantifying Construct Validity in LLM Evaluations](https://arxiv.org/pdf/2602.15532)
- [Lifting the Benchmark Iceberg with IRT (OpenReview)](https://openreview.net/forum?id=ZyVQqK7mcP)
- [Knowledge Distillation as Decontamination (ICLR 2026)](https://openreview.net/pdf?id=W8VCH9x1HZ)
- [A Survey on Data Contamination for LLMs](https://arxiv.org/html/2502.14425v2)
- [Benchmarking LLMs Under Data Contamination: Static to Dynamic Evaluation](https://arxiv.org/html/2502.17521v2)

agentId: af89ed972f0b00e1c (use SendMessage with to: 'af89ed972f0b00e1c' to continue this agent)
&lt;usage>total_tokens: 28671
tool_uses: 21
duration_ms: 156119&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "998be71a-c8bd-445d-9112-6be1b38dc5fb",
  "isSidechain": false,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "type": "user",
  "uuid": "c483819b-0b94-4445-998a-d2f996e9844a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal called \"CRADE\" that combines IRT (Item Response Theory) with contamination detection and adversarial robustness for LLM evaluation. The proposal claims no existing work sits at this three-way intersection. I need you to do an adversarial search for competing or concurrent work that the authors may have missed.\n\nSearch for ALL of these queries using WebSearch:\n\n1. \"contamination-aware IRT\" OR \"contamination item response theory\" LLM 2025 2026\n2. \"benchmark contamination correction\" \"item response theory\" 2026\n3. \"decontamination\" \"IRT\" \"large language model\" 2026\n4. \"gated IRT\" language model\n5. site:arxiv.org \"contamination\" \"adversarial\" \"IRT\" LLM evaluation 2026\n6. site:openreview.net contamination IRT LLM evaluation 2026\n7. \"joint contamination ability\" OR \"contamination-adjusted scoring\" LLM 2026\n8. \"benchmark integrity\" \"measurement theory\" LLM 2025 2026\n9. \"paired item\" contamination LLM evaluation\n10. site:arxiv.org \"psychometric\" \"contamination\" \"language model\" 2026\n\nFor each search, report: what you found, whether any paper addresses the same three-way intersection (IRT + contamination + adversarial variants), and any paper that could be a direct competitor. Be thorough — the goal is to find work the proposal authors missed.",
    "agentId": "af89ed972f0b00e1c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive results from all searches. Here is my full analysis.\n\n---\n\n## Adversarial Literature Search Report: CRADE (IRT + Contamination Detection + Adversarial Robustness)\n\nI conducted 10 specified searches plus 7 follow-up targeted searches. Below are the findings organized by search query, followed by an overall competitive threat assessment.\n\n---\n\n### Search 1: \"contamination-aware IRT\" OR \"contamination item response theory\" LLM 2025 2026\n\n**Found:** No paper uses the exact phrase \"contamination-aware IRT.\" However, several papers apply IRT to LLM benchmarking:\n- **PSN-IRT** (Zhou et al., AAAI 2026 Oral) -- uses IRT to audit benchmark quality and explicitly flags contaminated items as a quality problem. Does NOT model contamination as a latent variable or correct for it within the IRT framework.\n- **IRT-Router** (Song et al., ACL 2025) -- uses IRT for LLM routing, no contamination angle.\n- **Diagnosing LLM-as-a-Judge via IRT** (2026) -- applies IRT-GRM to judge reliability, no contamination.\n\n**Three-way intersection?** No. PSN-IRT is closest (IRT + contamination awareness) but has no adversarial robustness component.\n\n---\n\n### Search 2: \"benchmark contamination correction\" \"item response theory\" 2026\n\n**Found:** PSN-IRT again dominates. It identifies contaminated items and removes them to create cleaner benchmarks, but does not perform contamination *correction* within the IRT model itself (e.g., jointly estimating ability and contamination parameters). No adversarial component.\n\n**Three-way intersection?** No.\n\n---\n\n### Search 3: \"decontamination\" \"IRT\" \"large language model\" 2026\n\n**Found:** Two separate threads that do NOT intersect:\n- **Inference-Time Decontamination (ITD)** and **DeconIEP** -- decontamination methods that operate at inference time by rewriting or perturbing leaked samples. No IRT component.\n- **PSN-IRT** -- IRT-based benchmark analysis. No decontamination mechanism.\n\n**Three-way intersection?** No.\n\n---\n\n### Search 4: \"gated IRT\" language model\n\n**Found:** Only results for gated recurrent/convolutional language models from 2016-2019. No paper proposes a \"gated IRT\" model where a contamination gate modulates item parameters. This specific architectural idea appears novel.\n\n**Three-way intersection?** No results at all.\n\n---\n\n### Search 5: site:arxiv.org \"contamination\" \"adversarial\" \"IRT\" LLM evaluation 2026\n\n**Found:** No single paper addressing all three terms together. The results split into:\n- Contamination detection surveys (Min-K%, ConStat, canary GUIDs)\n- Adversarial evaluation (perturbation-based)\n- IRT for benchmarking (PSN-IRT)\n\nA critical find here: **\"LLM Benchmark Datasets Should Be Contamination-Resistant\"** (arxiv 2605.19999, May 2026) -- very recent, evaluates contamination resistance methods. No IRT component.\n\n**Three-way intersection?** No.\n\n---\n\n### Search 6: site:openreview.net contamination IRT LLM evaluation 2026\n\n**Found:** Multiple contamination-focused papers at ICLR 2026 and in review:\n- **Auditing Test Data Contamination with Error Rate Control** (ICLR 2026)\n- **The Emperor's New Clothes in Benchmarking** -- tests 20 mitigation strategies and finds none effectively balances fidelity and contamination resistance\n- **Detecting Benchmark Contamination Through Watermarking**\n- **Knowledge Distillation as Decontamination** (ICLR 2026)\n- **LiveBench** -- contamination-limited benchmark\n\nNone of these use IRT. None combine IRT with contamination or adversarial robustness.\n\n**Three-way intersection?** No.\n\n---\n\n### Search 7: \"joint contamination ability\" OR \"contamination-adjusted scoring\" LLM 2026\n\n**Found:** The closest competitor in the contamination-adjustment space:\n- **DCR: Data Contamination Rating** (EMNLP 2025) -- uses a fuzzy inference system to produce a contamination factor that adjusts raw accuracy. Validated on 9 LLMs. This is a contamination-adjusted scoring system, but it does NOT use IRT. It uses heuristic fuzzy logic, not psychometric measurement theory. No adversarial component.\n- **\"Silicon Bureaucracy and AI Test-Oriented Education\"** (arxiv 2603.21636, March 2026) -- proposes an audit framework that compares clean vs. noisy conditions (where benchmark problems are deleted, rewritten, perturbed). This has contamination sensitivity + adversarial perturbation but NO IRT.\n\n**Three-way intersection?** No, but these are the two most relevant partial competitors:\n- DCR covers contamination-adjusted scoring (without IRT)\n- Silicon Bureaucracy covers contamination + adversarial perturbation (without IRT)\n\n---\n\n### Search 8: \"benchmark integrity\" \"measurement theory\" LLM 2025 2026\n\n**Found:**\n- **Benchmark Health Index (BHI)** (Feb 2026) -- meta-analyzes 106 benchmarks across discrimination, saturation, and impact. Uses measurement concepts but NOT formal IRT. No contamination correction or adversarial robustness.\n- **Quantifying Construct Validity in LLM Evaluations** (Feb 2026) -- applies validity theory to LLM benchmarks. Addresses measurement rigor but not contamination or adversarial robustness.\n\n**Three-way intersection?** No.\n\n---\n\n### Search 9: \"paired item\" contamination LLM evaluation\n\n**Found:**\n- **PaCoST (Paired Confidence Significance Testing)** -- constructs paired counterparts to detect benchmark contamination via statistical confidence analysis. This is a contamination detection method using paired items but has NO IRT and NO adversarial robustness component.\n- **\"Quantifying Data Contamination in Psychometric Evaluations of LLMs\"** (Han et al., EACL 2026 Findings) -- measures memorization and contamination in psychometric inventories (BFI-44, PVQ-40). Uses psychometric instruments but NOT IRT for ability estimation. Focuses on personality/values questionnaires, not capability benchmarks. No adversarial component.\n\n**Three-way intersection?** No.\n\n---\n\n### Search 10: site:arxiv.org \"psychometric\" \"contamination\" \"language model\" 2026\n\n**Found:** The Han et al. EACL 2026 paper again. This is the closest to combining psychometrics with contamination, but it studies contamination OF psychometric tests (whether LLMs have memorized personality questionnaires), not contamination-aware psychometric scoring of LLM ability. No IRT model is used; no adversarial component.\n\n**Three-way intersection?** No.\n\n---\n\n### Follow-up: RIDE (IRT + Adversarial, most relevant partial overlap)\n\n**RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning** (late 2025 / early 2026, OpenReview)\n\nThis is a significant find. RIDE uses IRT to measure question difficulty, then uses IRT-derived difficulty as a reward signal to train an adversarial question rewriter via reinforcement learning. It explicitly notes that strong benchmark performance may stem from contamination/memorization, and generates adversarial variants to test robustness. Average performance drops 21.73% across 26 models.\n\n**RIDE covers two of the three legs: IRT + adversarial perturbation.** It mentions contamination as a motivation but does NOT model contamination as a latent variable, does NOT jointly estimate contamination and ability, and does NOT propose contamination-aware IRT parameters. It is an adversarial benchmark construction tool, not a contamination-correcting measurement framework.\n\n---\n\n## Overall Assessment\n\n### Papers occupying partial intersections (ranked by threat level):\n\n| Paper | IRT | Contamination | Adversarial | Threat to CRADE |\n|-------|-----|---------------|-------------|-----------------|\n| **RIDE** (2025-2026) | Yes (difficulty estimation) | Motivation only | Yes (adversarial rewriting) | **MODERATE** -- covers IRT + adversarial but not contamination modeling |\n| **PSN-IRT** (AAAI 2026 Oral) | Yes (full IRT framework) | Identifies contaminated items | No | **MODERATE** -- covers IRT + contamination detection but not adversarial |\n| **Silicon Bureaucracy** (Mar 2026) | No | Yes (sensitivity auditing) | Yes (perturbation-based) | **LOW-MODERATE** -- covers contamination + adversarial without IRT |\n| **DCR** (EMNLP 2025) | No | Yes (contamination-adjusted scoring) | No | **LOW** -- contamination correction without IRT |\n| **Han et al.** (EACL 2026) | No (psychometric but not IRT) | Yes (psychometric contamination) | No | **LOW** -- different domain (personality, not capability) |\n| **BHI** (Feb 2026) | No (measurement-inspired but not IRT) | No | No | **NEGLIGIBLE** |\n\n### Key Conclusion\n\n**No paper was found that occupies the three-way intersection of IRT + contamination detection/correction + adversarial robustness.** The CRADE proposal's claim of novelty at this intersection appears to hold as of late May 2026.\n\nHowever, the authors should be aware of and cite these partial competitors:\n\n1. **RIDE** is the most dangerous near-miss -- it uses IRT-guided adversarial perturbation and is motivated by contamination concerns. A reviewer could argue RIDE is \"close enough.\" CRADE must clearly differentiate by emphasizing its contamination-as-latent-variable modeling within IRT, which RIDE entirely lacks.\n\n2. **PSN-IRT** (AAAI 2026 Oral) is a high-visibility paper that uses IRT and explicitly addresses contamination in benchmarks. CRADE must differentiate by showing that PSN-IRT only *detects and removes* contaminated items rather than *correcting for contamination within the model*.\n\n3. **Silicon Bureaucracy** (March 2026) combines contamination auditing with adversarial perturbation. It lacks IRT but is conceptually adjacent. The CRADE authors should cite it.\n\n4. **DCR** provides contamination-adjusted scoring, which is conceptually similar to what CRADE presumably does, but uses fuzzy logic rather than IRT. CRADE should position itself as the principled psychometric alternative.\n\n---\n\nSources:\n- [PSN-IRT: Lost in Benchmarks? (AAAI 2026)](https://arxiv.org/abs/2505.15055)\n- [PSN-IRT GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT)\n- [IRT-Router (ACL 2025)](https://arxiv.org/abs/2506.01048)\n- [Diagnosing LLM-as-a-Judge via IRT (2026)](https://arxiv.org/pdf/2602.00521)\n- [RIDE: Difficulty Evolving Perturbation with IRT](https://arxiv.org/pdf/2511.04120)\n- [Silicon Bureaucracy and AI Test-Oriented Education (2026)](https://arxiv.org/abs/2603.21636)\n- [DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)](https://arxiv.org/abs/2507.11405)\n- [Quantifying Data Contamination in Psychometric Evaluations of LLMs (EACL 2026)](https://arxiv.org/abs/2510.07175)\n- [Benchmark Health Index (2026)](https://arxiv.org/pdf/2602.11674)\n- [LLM Benchmark Datasets Should Be Contamination-Resistant (May 2026)](https://arxiv.org/html/2605.19999v1)\n- [When Benchmarks Leak: Inference-Time Decontamination (2026)](https://arxiv.org/abs/2601.19334)\n- [The Emperor's New Clothes in Benchmarking (OpenReview)](https://openreview.net/forum?id=TuvDxubEfE)\n- [Auditing Test Data Contamination with Error Rate Control (OpenReview)](https://openreview.net/forum?id=YsoabhpS7z)\n- [Detecting Benchmark Contamination Through Watermarking (OpenReview)](https://openreview.net/forum?id=WFGxFzFDmQ)\n- [LiveBench (OpenReview)](https://openreview.net/forum?id=sKYHBTAxVa)\n- [Towards Contamination Resistant Benchmarks](https://arxiv.org/pdf/2505.08389)\n- [Quantifying Construct Validity in LLM Evaluations](https://arxiv.org/pdf/2602.15532)\n- [Lifting the Benchmark Iceberg with IRT (OpenReview)](https://openreview.net/forum?id=ZyVQqK7mcP)\n- [Knowledge Distillation as Decontamination (ICLR 2026)](https://openreview.net/pdf?id=W8VCH9x1HZ)\n- [A Survey on Data Contamination for LLMs](https://arxiv.org/html/2502.14425v2)\n- [Benchmarking LLMs Under Data Contamination: Static to Dynamic Evaluation](https://arxiv.org/html/2502.17521v2)"
      }
    ],
    "totalDurationMs": 156119,
    "totalTokens": 28671,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2778,
      "cache_read_input_tokens": 22500,
      "output_tokens": 3392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2778
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3392,
          "cache_read_input_tokens": 22500,
          "cache_creation_input_tokens": 2778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2778,
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
  "sourceToolAssistantUUID": "998be71a-c8bd-445d-9112-6be1b38dc5fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T12:43:27.850Z_

<details><summary>↩ Tool result · `toolu_01W1wvBDyuuQx4N3Lr4RtVsB`</summary>

```text
Now I have enough information to provide a thorough, technically honest assessment. Let me synthesize everything.

---

## Technical Assessment: Gated 2PL IRT Model with 15-20 LLM Examinees

### Executive Summary

This model is pushing well beyond established boundaries for IRT estimation. The proposal faces serious estimation challenges that range from "difficult but potentially manageable with strong priors" (for the standard 2PL components) to "fundamentally problematic" (for the bilinear contamination gate). Below is a detailed breakdown.

---

### 1. The Standard 2PL Component: Extremely Small N, but Not Unprecedented Territory

**What the literature says about minimum N for 2PL:**

The consensus minimum sample size for reliable 2PL item parameter estimation is **N >= 500** with marginal maximum likelihood (MML). Bayesian hierarchical approaches have pushed this down significantly:

- The **optimized hierarchical Bayesian 2PL** (half-Cauchy or Exponential hyperpriors on variance components) achieves unbiased parameter estimates at **N = 50** -- the current state of the art for small-sample 2PL calibration.
- Fox (2025) introduced the **IRT-BCSM** (Bayesian Covariance Structure Model), which analytically integrates out the latent person variable, achieving "optimal performance" at **N = 50-100 persons with 5-10 items**.
- For the **Rasch (1PL) model**, samples as small as N = 30 have been shown to produce "useful, stable estimates" for well-targeted examinees.

**N = 15-20 is below every published minimum I found.** Even the most optimistic Bayesian small-sample IRT papers bottom out at N = 50. With N = 15, you are not in "small sample" territory -- you are in "case study" territory.

**However**, there is a critical asymmetry in this design that partially helps: with K = 1000 items, person parameter estimation (theta_j) should be quite precise because each person's ability is informed by 1000 binary observations. The problem is reversed from the usual IRT concern: **item parameters are the ones that suffer**, because each item's discrimination and difficulty are informed by only 15-20 observations.

---

### 2. Item Parameter Recovery with 15-20 Examinees

For each item, the model must estimate:
- **a_i** (discrimination): This is the most problematic parameter. With only 15-20 data points per item, estimating the slope of a logistic curve is severely underdetermined. Discrimination parameters are notoriously hard to estimate even at N = 200.
- **b_i** (difficulty): Somewhat easier but still problematic at N = 15-20.
- **delta_i** (variant shift): Estimated from variant-item responses only, so effectively even fewer observations.
- **eta_i** (item susceptibility): Part of the bilinear contamination term -- see below.

**Realistic expectation:** With only 15-20 observations per item, the item-level parameter estimates will be **dominated by the priors**. This means:

- Your "estimates" of a_i will largely reflect your prior beliefs about discrimination, with modest updating from data.
- The model will function more like a **prior-regularized scoring model** than a data-driven estimation.
- Individual item parameter estimates will have enormous posterior uncertainty.
- Shrinkage toward the hierarchical mean will be extreme.

This is not necessarily fatal if the **goal is person-level inference** (ranking LLMs by ability or contamination). The hierarchical structure borrows strength across items to estimate person parameters, which can still work. But if the goal is to make item-level claims (e.g., "this item has high discrimination" or "this item is susceptible to contamination"), those claims will be very weakly supported.

---

### 3. The Bilinear Contamination Gate: The Most Serious Problem

The gated component introduces:

P(Y=1) = xi_j * eta_i + (1 - xi_j * eta_i) * sigma(a_i(theta_j - b_i))

The product **xi_j * eta_i** is a bilinear/multiplicative interaction term. Let me address the identifiability argument directly.

**The counting argument (M+K-1 = 1014 free parameters, M*K = 15,000 observations) is misleading.** Here is why:

**(a) Non-identifiability of the product.** The product xi_j * eta_i has a fundamental **scaling indeterminacy**: you can multiply all xi_j by constant c and divide all eta_i by c, yielding the same product. This is the classic matrix factorization rotation/scaling problem. You need at least one constraint to fix the scale. But even with that constraint, the problem is deeper:

**(b) Effective information per parameter is tiny.** While there are 15,000 total cells in the M x K matrix, each xi_j is informed by observations across 1000 items (good), but each eta_i is informed by only 15-20 examinees (terrible). Furthermore, the bilinear term is only active for original items (not variant items), and its effect is confounded with the 2PL component -- you can only identify xi_j * eta_i to the extent that the "contamination boost" is distinguishable from simply having high ability theta_j.

**(c) Practical non-identifiability with the logistic component.** The gated model says: with probability xi_j * eta_i, the LLM gets the item right regardless of ability (contamination), and with the complementary probability, the standard 2PL applies. This is structurally similar to a **4PL model with a guessing/upper-asymptote parameter** -- and 4PL models are notorious for identifiability problems even at N = 500+. The literature explicitly warns that 4-parameter IRT models have "severe deficiencies related to possible unidentifiability." With N = 15, this problem is vastly amplified.

**(d) Separation from ability.** For the contamination gate to be identified separately from high ability, you need to observe the characteristic pattern: a contaminated model gets contaminated items right even when they are very difficult (high b_i), but struggles with similarly difficult non-contaminated items. With only 15-20 LLMs, the statistical power to detect this pattern for individual items is extremely limited.

**Bottom line on the bilinear term:** The xi_j * eta_i product will be **practically non-identifiable at the item level** (eta_i estimates will be almost entirely prior-driven) and only weakly identifiable at the person level (xi_j may be estimable if there is a clear enough signal across 1000 items, but this depends heavily on how many items are actually contaminated and how strong the contamination effect is).

---

### 4. Does Bayesian MCMC Help?

Bayesian estimation helps in the following ways:
- **Regularization through priors** prevents the extreme/degenerate estimates that MLE would produce (e.g., infinite discrimination, boundary parameter estimates).
- **Hierarchical structure** enables partial pooling, which stabilizes item parameters by borrowing strength across items.
- **Posterior uncertainty quantification** honestly represents how little you know about each item parameter.

Bayesian estimation does **not** help with:
- **Fundamental identifiability problems.** If the likelihood surface is essentially flat in some direction, the posterior will just reflect the prior in that direction. You get back what you put in.
- **Model misspecification.** Strong priors + weak data = estimates driven by priors, which are only as good as the prior specification.
- **MCMC convergence.** With the complex gated model, expect:
  - Slow mixing and high autocorrelation, especially for the discrimination and contamination parameters.
  - Potential divergent transitions in HMC/NUTS (NumPyro uses NUTS), particularly around the bilinear interaction term.
  - Strong posterior correlations between xi_j, eta_i, theta_j, and a_i, creating ridge-like geometries that are hard for NUTS to navigate.
  - The need for very careful parameterization (non-centered parameterizations, appropriate constraints).

---

### 5. Specific Risks and Practical Issues

**Risk 1: Prior dominance.** With N = 15-20 per item, the data contribute very little information per item parameter. The posterior will be overwhelmingly determined by the priors for a_i, delta_i, and especially eta_i. The results will be a **prior sensitivity analysis**, not a data-driven estimation. Any reviewer should ask: "How do results change with different priors?"

**Risk 2: Confounding of theta and xi.** A model that does well on contaminated items could either have high ability (high theta_j) or high contamination (high xi_j). Separating these requires the variant items (which are not contaminated by construction), but variant items only contribute to estimating theta_j through the shifted 2PL. If the number of variant items is small relative to original items, theta_j may be poorly pinned down, creating a cascade of confounding.

**Risk 3: MCMC diagnostics may look deceptively good.** With strong priors and few data, the sampler may converge quickly to a posterior that is close to the prior. Good Rhat and n_eff do not mean the data are informing the estimates -- they may just mean the prior is dominating and the sampler has no trouble exploring a prior-like distribution.

**Risk 4: Label switching / multimodality.** The bilinear term xi_j * eta_i can exhibit multimodal posteriors (different allocations of the "contamination" effect between person-level and item-level), which MCMC may not explore adequately.

**Risk 5: Lack of validation benchmarks.** There is no published literature on fitting models of this complexity with N = 15-20. You cannot appeal to existing simulation studies to argue the method works -- you would need to conduct your own simulation study with known ground truth to validate the estimation procedure at this sample size.

---

### 6. What Would Make This More Defensible

If you wanted to salvage the core idea, consider:

1. **Simplify the model.** Drop item-level eta_i and use a simpler contamination model -- e.g., a single contamination probability per person xi_j (no item-level susceptibility), which reduces the bilinear term to a per-person upper asymptote. This is far more identifiable with 15 examinees.

2. **Use a 1PL (Rasch) base.** Fix all a_i = 1 (or estimate a single common discrimination). This removes ~1000 parameters and is much more defensible at N = 15.

3. **Increase N.** Even going from 15 to 50-100 LLMs (by including more model variants, different quantizations, fine-tunes, etc.) would substantially improve estimation.

4. **Conduct a rigorous simulation study.** Generate data from the proposed model with known parameters at N = 15, fit the model, and evaluate parameter recovery. Report bias, RMSE, coverage of credible intervals, and sensitivity to prior specification. This is essential and non-negotiable for a model this far outside established practice.

5. **Report prior sensitivity analysis.** Show results under at least 2-3 meaningfully different prior specifications to demonstrate which conclusions are data-driven vs. prior-driven.

---

### Summary Assessment

| Component | Feasibility | Key Concern |
|-----------|------------|-------------|
| theta_j (ability) | **Likely feasible** | 1000 items per person provides substantial information |
| xi_j (contamination, person-level) | **Possibly feasible** with strong variant-item design | Confounded with theta_j; depends on variant item count |
| a_i (discrimination) | **Heavily prior-driven** | Only 15-20 obs per item; effectively unestimable from data alone |
| b_i (difficulty) | **Partially feasible** | Better than a_i but still very uncertain per item |
| delta_i (variant shift) | **Heavily prior-driven** | Estimated from even fewer observations |
| eta_i (item susceptibility) | **Practically non-identifiable** | 15-20 obs + bilinear confounding + logistic component confounding |

**Overall verdict:** The person-level parameters (theta_j and possibly xi_j) may be estimable in a meaningful sense because each person contributes 1000 observations. The item-level parameters, especially eta_i and a_i, will be almost entirely prior-driven at N = 15-20. The model will "fit" and MCMC will likely converge (especially with informative priors), but convergence does not equal validity. The proposal needs, at minimum, a simulation study demonstrating parameter recovery at the proposed sample size, and a thorough prior sensitivity analysis. Without these, the results are not interpretable.

---

Sources:
- [An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7262992/)
- [Robustness of the optimized hierarchical 2PL IRT model for small-sample calibration](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10700496/)
- [Bayesian Prior Choice in IRT Estimation Using MCMC and Variational Bayes (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5037236/)
- [Redefining Item Response Models for Small Samples - Fox, 2025](https://journals.sagepub.com/doi/10.3102/10769986241269886)
- [On the Identifiability of 3- and 4-Parameter IRT Models](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11164782/)
- [Benefits of the Curious Behavior of Bayesian Hierarchical IRT Models (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10846471/)
- [Item Parameter Recovery: Sensitivity to Prior Distribution (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11268390/)
- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT](https://arxiv.org/html/2505.15055v3)
- [Identifiability Scaling Laws in Bilinear Inverse Problems](https://arxiv.org/pdf/1402.2637)
- [Theoretical Analysis of Bayesian Matrix Factorization (JMLR)](https://jmlr.org/papers/v12/nakajima11a.html)
- [Sample-Size Planning in Item-Response Theory: A Tutorial (2025)](https://journals.sagepub.com/doi/10.1177/25152459251314798)
- [A Comparison of Estimation Techniques for IRT Models with Small Samples (ERIC)](https://eric.ed.gov/?id=EJ1208702)
- [HBMIRT: SAS macro for estimating IRT models in small samples (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11133100/)
- [Divergent transitions primer - Stan Forums](https://discourse.mc-stan.org/t/divergent-transitions-a-primer/17099)

agentId: a3a240c8aaa2bf188 (use SendMessage with to: 'a3a240c8aaa2bf188' to continue this agent)
&lt;usage>total_tokens: 29404
tool_uses: 19
duration_ms: 194087&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "166d1c79-cf26-46d5-89a7-f2a42dd2435e",
  "isSidechain": false,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "type": "user",
  "uuid": "ad3012d5-9e70-4d44-ae81-eb1598f4b8eb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a proposal that wants to fit a \"Gated 2PL IRT model\" with only 15-20 LLMs as examinees (but ~1000 items). The model is:\n- For variant items: P(Y=1) = σ(a_i(θ_j − b_i − δ_i)) — standard 2PL with difficulty shift\n- For original items: P(Y=1) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i)) — gated model\n- Parameters: θ_j (ability per model), ξ_j (contamination per model), η_i (item susceptibility), a_i (discrimination), b_i (difficulty), δ_i (variant shift)\n- Total free parameters: ~20 person parameters (θ, ξ) + ~4000 item parameters (a, b, δ, η for 1000 items)\n- Estimation: Bayesian MCMC via NumPyro, 4 chains × 2000+2000 samples\n\nSearch for information about:\n\n1. \"IRT small sample\" OR \"IRT few examinees\" Bayesian estimation — what's the minimum viable number of examinees for 2PL?\n2. \"Bayesian IRT\" \"small sample\" convergence — does Bayesian MCMC help with very small N?\n3. The identifiability claim: with M=15 models and K=1000 items, the bilinear product ξ_j·η_i has M+K-1 = 1014 free parameters constrained by M×K = 15,000 observations. Is this actually well-identified in practice?\n4. \"hierarchical IRT\" \"small sample size\" — does hierarchical prior structure help?\n5. Any practical issues with fitting IRT to 15-20 examinees — even with 1000+ items, are there known estimation problems?\n\nGive me a technically honest assessment: is this estimation feasible with 15-20 models? What are the realistic risks?",
    "agentId": "a3a240c8aaa2bf188",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to provide a thorough, technically honest assessment. Let me synthesize everything.\n\n---\n\n## Technical Assessment: Gated 2PL IRT Model with 15-20 LLM Examinees\n\n### Executive Summary\n\nThis model is pushing well beyond established boundaries for IRT estimation. The proposal faces serious estimation challenges that range from \"difficult but potentially manageable with strong priors\" (for the standard 2PL components) to \"fundamentally problematic\" (for the bilinear contamination gate). Below is a detailed breakdown.\n\n---\n\n### 1. The Standard 2PL Component: Extremely Small N, but Not Unprecedented Territory\n\n**What the literature says about minimum N for 2PL:**\n\nThe consensus minimum sample size for reliable 2PL item parameter estimation is **N >= 500** with marginal maximum likelihood (MML). Bayesian hierarchical approaches have pushed this down significantly:\n\n- The **optimized hierarchical Bayesian 2PL** (half-Cauchy or Exponential hyperpriors on variance components) achieves unbiased parameter estimates at **N = 50** -- the current state of the art for small-sample 2PL calibration.\n- Fox (2025) introduced the **IRT-BCSM** (Bayesian Covariance Structure Model), which analytically integrates out the latent person variable, achieving \"optimal performance\" at **N = 50-100 persons with 5-10 items**.\n- For the **Rasch (1PL) model**, samples as small as N = 30 have been shown to produce \"useful, stable estimates\" for well-targeted examinees.\n\n**N = 15-20 is below every published minimum I found.** Even the most optimistic Bayesian small-sample IRT papers bottom out at N = 50. With N = 15, you are not in \"small sample\" territory -- you are in \"case study\" territory.\n\n**However**, there is a critical asymmetry in this design that partially helps: with K = 1000 items, person parameter estimation (theta_j) should be quite precise because each person's ability is informed by 1000 binary observations. The problem is reversed from the usual IRT concern: **item parameters are the ones that suffer**, because each item's discrimination and difficulty are informed by only 15-20 observations.\n\n---\n\n### 2. Item Parameter Recovery with 15-20 Examinees\n\nFor each item, the model must estimate:\n- **a_i** (discrimination): This is the most problematic parameter. With only 15-20 data points per item, estimating the slope of a logistic curve is severely underdetermined. Discrimination parameters are notoriously hard to estimate even at N = 200.\n- **b_i** (difficulty): Somewhat easier but still problematic at N = 15-20.\n- **delta_i** (variant shift): Estimated from variant-item responses only, so effectively even fewer observations.\n- **eta_i** (item susceptibility): Part of the bilinear contamination term -- see below.\n\n**Realistic expectation:** With only 15-20 observations per item, the item-level parameter estimates will be **dominated by the priors**. This means:\n\n- Your \"estimates\" of a_i will largely reflect your prior beliefs about discrimination, with modest updating from data.\n- The model will function more like a **prior-regularized scoring model** than a data-driven estimation.\n- Individual item parameter estimates will have enormous posterior uncertainty.\n- Shrinkage toward the hierarchical mean will be extreme.\n\nThis is not necessarily fatal if the **goal is person-level inference** (ranking LLMs by ability or contamination). The hierarchical structure borrows strength across items to estimate person parameters, which can still work. But if the goal is to make item-level claims (e.g., \"this item has high discrimination\" or \"this item is susceptible to contamination\"), those claims will be very weakly supported.\n\n---\n\n### 3. The Bilinear Contamination Gate: The Most Serious Problem\n\nThe gated component introduces:\n\nP(Y=1) = xi_j * eta_i + (1 - xi_j * eta_i) * sigma(a_i(theta_j - b_i))\n\nThe product **xi_j * eta_i** is a bilinear/multiplicative interaction term. Let me address the identifiability argument directly.\n\n**The counting argument (M+K-1 = 1014 free parameters, M*K = 15,000 observations) is misleading.** Here is why:\n\n**(a) Non-identifiability of the product.** The product xi_j * eta_i has a fundamental **scaling indeterminacy**: you can multiply all xi_j by constant c and divide all eta_i by c, yielding the same product. This is the classic matrix factorization rotation/scaling problem. You need at least one constraint to fix the scale. But even with that constraint, the problem is deeper:\n\n**(b) Effective information per parameter is tiny.** While there are 15,000 total cells in the M x K matrix, each xi_j is informed by observations across 1000 items (good), but each eta_i is informed by only 15-20 examinees (terrible). Furthermore, the bilinear term is only active for original items (not variant items), and its effect is confounded with the 2PL component -- you can only identify xi_j * eta_i to the extent that the \"contamination boost\" is distinguishable from simply having high ability theta_j.\n\n**(c) Practical non-identifiability with the logistic component.** The gated model says: with probability xi_j * eta_i, the LLM gets the item right regardless of ability (contamination), and with the complementary probability, the standard 2PL applies. This is structurally similar to a **4PL model with a guessing/upper-asymptote parameter** -- and 4PL models are notorious for identifiability problems even at N = 500+. The literature explicitly warns that 4-parameter IRT models have \"severe deficiencies related to possible unidentifiability.\" With N = 15, this problem is vastly amplified.\n\n**(d) Separation from ability.** For the contamination gate to be identified separately from high ability, you need to observe the characteristic pattern: a contaminated model gets contaminated items right even when they are very difficult (high b_i), but struggles with similarly difficult non-contaminated items. With only 15-20 LLMs, the statistical power to detect this pattern for individual items is extremely limited.\n\n**Bottom line on the bilinear term:** The xi_j * eta_i product will be **practically non-identifiable at the item level** (eta_i estimates will be almost entirely prior-driven) and only weakly identifiable at the person level (xi_j may be estimable if there is a clear enough signal across 1000 items, but this depends heavily on how many items are actually contaminated and how strong the contamination effect is).\n\n---\n\n### 4. Does Bayesian MCMC Help?\n\nBayesian estimation helps in the following ways:\n- **Regularization through priors** prevents the extreme/degenerate estimates that MLE would produce (e.g., infinite discrimination, boundary parameter estimates).\n- **Hierarchical structure** enables partial pooling, which stabilizes item parameters by borrowing strength across items.\n- **Posterior uncertainty quantification** honestly represents how little you know about each item parameter.\n\nBayesian estimation does **not** help with:\n- **Fundamental identifiability problems.** If the likelihood surface is essentially flat in some direction, the posterior will just reflect the prior in that direction. You get back what you put in.\n- **Model misspecification.** Strong priors + weak data = estimates driven by priors, which are only as good as the prior specification.\n- **MCMC convergence.** With the complex gated model, expect:\n  - Slow mixing and high autocorrelation, especially for the discrimination and contamination parameters.\n  - Potential divergent transitions in HMC/NUTS (NumPyro uses NUTS), particularly around the bilinear interaction term.\n  - Strong posterior correlations between xi_j, eta_i, theta_j, and a_i, creating ridge-like geometries that are hard for NUTS to navigate.\n  - The need for very careful parameterization (non-centered parameterizations, appropriate constraints).\n\n---\n\n### 5. Specific Risks and Practical Issues\n\n**Risk 1: Prior dominance.** With N = 15-20 per item, the data contribute very little information per item parameter. The posterior will be overwhelmingly determined by the priors for a_i, delta_i, and especially eta_i. The results will be a **prior sensitivity analysis**, not a data-driven estimation. Any reviewer should ask: \"How do results change with different priors?\"\n\n**Risk 2: Confounding of theta and xi.** A model that does well on contaminated items could either have high ability (high theta_j) or high contamination (high xi_j). Separating these requires the variant items (which are not contaminated by construction), but variant items only contribute to estimating theta_j through the shifted 2PL. If the number of variant items is small relative to original items, theta_j may be poorly pinned down, creating a cascade of confounding.\n\n**Risk 3: MCMC diagnostics may look deceptively good.** With strong priors and few data, the sampler may converge quickly to a posterior that is close to the prior. Good Rhat and n_eff do not mean the data are informing the estimates -- they may just mean the prior is dominating and the sampler has no trouble exploring a prior-like distribution.\n\n**Risk 4: Label switching / multimodality.** The bilinear term xi_j * eta_i can exhibit multimodal posteriors (different allocations of the \"contamination\" effect between person-level and item-level), which MCMC may not explore adequately.\n\n**Risk 5: Lack of validation benchmarks.** There is no published literature on fitting models of this complexity with N = 15-20. You cannot appeal to existing simulation studies to argue the method works -- you would need to conduct your own simulation study with known ground truth to validate the estimation procedure at this sample size.\n\n---\n\n### 6. What Would Make This More Defensible\n\nIf you wanted to salvage the core idea, consider:\n\n1. **Simplify the model.** Drop item-level eta_i and use a simpler contamination model -- e.g., a single contamination probability per person xi_j (no item-level susceptibility), which reduces the bilinear term to a per-person upper asymptote. This is far more identifiable with 15 examinees.\n\n2. **Use a 1PL (Rasch) base.** Fix all a_i = 1 (or estimate a single common discrimination). This removes ~1000 parameters and is much more defensible at N = 15.\n\n3. **Increase N.** Even going from 15 to 50-100 LLMs (by including more model variants, different quantizations, fine-tunes, etc.) would substantially improve estimation.\n\n4. **Conduct a rigorous simulation study.** Generate data from the proposed model with known parameters at N = 15, fit the model, and evaluate parameter recovery. Report bias, RMSE, coverage of credible intervals, and sensitivity to prior specification. This is essential and non-negotiable for a model this far outside established practice.\n\n5. **Report prior sensitivity analysis.** Show results under at least 2-3 meaningfully different prior specifications to demonstrate which conclusions are data-driven vs. prior-driven.\n\n---\n\n### Summary Assessment\n\n| Component | Feasibility | Key Concern |\n|-----------|------------|-------------|\n| theta_j (ability) | **Likely feasible** | 1000 items per person provides substantial information |\n| xi_j (contamination, person-level) | **Possibly feasible** with strong variant-item design | Confounded with theta_j; depends on variant item count |\n| a_i (discrimination) | **Heavily prior-driven** | Only 15-20 obs per item; effectively unestimable from data alone |\n| b_i (difficulty) | **Partially feasible** | Better than a_i but still very uncertain per item |\n| delta_i (variant shift) | **Heavily prior-driven** | Estimated from even fewer observations |\n| eta_i (item susceptibility) | **Practically non-identifiable** | 15-20 obs + bilinear confounding + logistic component confounding |\n\n**Overall verdict:** The person-level parameters (theta_j and possibly xi_j) may be estimable in a meaningful sense because each person contributes 1000 observations. The item-level parameters, especially eta_i and a_i, will be almost entirely prior-driven at N = 15-20. The model will \"fit\" and MCMC will likely converge (especially with informative priors), but convergence does not equal validity. The proposal needs, at minimum, a simulation study demonstrating parameter recovery at the proposed sample size, and a thorough prior sensitivity analysis. Without these, the results are not interpretable.\n\n---\n\nSources:\n- [An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7262992/)\n- [Robustness of the optimized hierarchical 2PL IRT model for small-sample calibration](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10700496/)\n- [Bayesian Prior Choice in IRT Estimation Using MCMC and Variational Bayes (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5037236/)\n- [Redefining Item Response Models for Small Samples - Fox, 2025](https://journals.sagepub.com/doi/10.3102/10769986241269886)\n- [On the Identifiability of 3- and 4-Parameter IRT Models](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11164782/)\n- [Benefits of the Curious Behavior of Bayesian Hierarchical IRT Models (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10846471/)\n- [Item Parameter Recovery: Sensitivity to Prior Distribution (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11268390/)\n- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT](https://arxiv.org/html/2505.15055v3)\n- [Identifiability Scaling Laws in Bilinear Inverse Problems](https://arxiv.org/pdf/1402.2637)\n- [Theoretical Analysis of Bayesian Matrix Factorization (JMLR)](https://jmlr.org/papers/v12/nakajima11a.html)\n- [Sample-Size Planning in Item-Response Theory: A Tutorial (2025)](https://journals.sagepub.com/doi/10.1177/25152459251314798)\n- [A Comparison of Estimation Techniques for IRT Models with Small Samples (ERIC)](https://eric.ed.gov/?id=EJ1208702)\n- [HBMIRT: SAS macro for estimating IRT models in small samples (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11133100/)\n- [Divergent transitions primer - Stan Forums](https://discourse.mc-stan.org/t/divergent-transitions-a-primer/17099)"
      }
    ],
    "totalDurationMs": 194087,
    "totalTokens": 29404,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 2039,
      "cache_read_input_tokens": 22928,
      "output_tokens": 3692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 3692,
          "cache_read_input_tokens": 22928,
          "cache_creation_input_tokens": 2039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2039,
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
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "166d1c79-cf26-46d5-89a7-f2a42dd2435e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "ad3012d5-9e70-4d44-ae81-eb1598f4b8eb",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CRADE contamination-ability decomposition via gated IRT",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Assistant

_source line 26 · 2026-05-28T12:44:45.709Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive verification results from all five agents. Let me synthesize the findings to produce my review.

## Summary of findings:

### Reference verification:
- **PSN-IRT**: Verified (AAAI 2026 Oral). Minor issue: "contamination-corrected scoring as open question" is an inference, not explicitly stated.
- **DGM**: Fully verified (Psychometrika 2013).
- **RankLLM**: Verified (ICLR 2026 Poster, not just "ICLR 2026"). ρ=0.94 rounded up from 0.9382.


- **Wang et al.**: Verified (ICLR 2026 Poster).
- **JECS**: Verified (arXiv May 2026).
- **DCR**: Verified (EMNLP 2025), though the r=0.66 metric applies specifically to LIAR2 rather than broadly to hard tasks.
- **ConStat**: Verified (NeurIPS 2024).
- **RIDE**: Verified (arXiv January 2026, not 2025).
- **PaCoST**: Exists but is actually EMNLP 2024 Findings, not a standalone arXiv 2024 paper.
- **San Martin et al.**: This attribution is incorrect—the actual authors are Noventa, Ye, Kelava, and Spoto from Psychometrika 2024.
- **py-irt**: Verified (IJOC 2023).
- **Growing Pains**: Verified (arXiv April 2026).
- **Illusion of Reasoning**: Verified (arXiv March/April 2026).
- **Fox (2025, JEBS)**: Verified.
- **MATH-Perturb**: Verified (ICML 2025 with available code).
- **MathCheck**: Verified (ICLR 2025 with available code).

Now checking the model and dataset details—AAAI 2027 deadlines are confirmed with July 21 for abstracts and July 28 for papers, and DeepSeek-R2 32B is verified.

Looking at the model specifications: DeepSeek-R2 32B hits 92.7% on AIME, Qwen3.6-27B from April 2026 uses Apache 2.0 licensing, GLM-5.1 has 754B parameters with 40B active under MIT license on Ascend 910B hardware, and DeepSeek-V4-Flash 284B is confirmed. MathArena is only partially verified—the competitions check out but the ~897 problem count doesn't match the original paper's claim of 162 problems.

For competing work, I'm not finding any paper that combines all three elements of IRT, contamination correction, and adversarial variants together, though RIDE comes close by pairing IRT with adversarial approaches.

The IRT feasibility assessment reveals a critical problem: with only 15-20 samples per item, I'm well below the N=50 minimum that even optimistic Bayesian approaches require for 2PL models. The item-level parameters will be almost entirely determined by priors rather than data, and the bilinear contamination gate creates practical non-identifiability issues at the item level due to scaling indeterminacy. Person-level parameters might work better given the 1000 items per person, but the item-level constraints are genuinely problematic.

The proposal needs a simulation study to demonstrate parameter recovery with this novel gated IRT model at such a small sample size—this is essential for a psychometric paper and currently missing. There's also a citation error where San Martin et al. should be Noventa et al. (2024).

Looking at the feasibility more carefully, the main constraint is fitting a G-2PL with bilinear contamination at N=15-20, which is genuinely challenging territory.  The person-level parameters are the critical piece for ranking models by corrected ability, while item-level contamination susceptibility is less central to the core claims. The proposal has detailed estimation strategies (MCMC, neural, VI comparison) and acknowledges the prior-dependence issue, plus the compute budget of 210 H100-hours fits within constraints. A simulation study would strengthen this, but the framework is sound enough that feasibility hinges on whether the person-level inference holds up in practice. Score: 3/5.

The proposal is exceptionally clear and well-organized, with fully specified model and estimation details.

The validation approach is solid with causal, correlational, and ablative evidence plus concrete backup plans, though the verbosity makes it harder to extract the core contribution. The impact potential is significant—this would genuinely advance LLM evaluation methodology with formal rigor that existing ad-hoc approaches lack.

Averaging the scores gives 3.75, which falls short of the 4.0 threshold. The main issue is the missing simulation study to validate parameter recovery at the small sample sizes being proposed.

There are also concerns about item-level contamination susceptibility claims being undermined by practical non-identifiability when priors dominate at N=15-20, plus some minor issues with author attribution, unverifiable benchmark counts, and overgeneralized claims about task difficulty correlations.

The proposal has actually resolved all the critical and moderate issues from earlier review rounds, so this is round 3. The remaining problems are fixable—the simulation study is straightforward to add, and the non-identifiability issue is partially addressable. I'm weighing whether this warrants acceptance or a revision request.

The core novelty is solid, the three-way intersection is genuinely unoccupied, the theoretical foundation is sound, the validation plan is thorough, and the feasibility checks out. But the simulation study gap is a real problem—in psychometrics, you can't propose a new IRT model variant and apply it at sample sizes far below published precedent without demonstrating parameter recovery. That's non-negotiable. It's a straightforward fix though: just add a week of simulation work testing θ and ξ recovery across N=15, 20, and 30 with known parameters.

The non-identifiability of η_i is also a legitimate concern, though the proposal does acknowledge it somewhat through the model adequacy plan and residual analysis, and the main claims operate at the person level rather than the item level. Adding the simulation study would push this from borderline to solid. I'm leaning toward a revise recommendation with specific, actionable feedback rather than outright rejection.

Let me recalibrate the scores: novelty is genuinely strong at around 4.5 for the three-way intersection, feasibility sits at 3 due to the estimation challenges at small sample sizes without a simulation study, clarity is excellent at 4, and impact would be high if successful at 4. That puts the average at 3.75, which lands in revise territory.

The concrete feedback I'd give: run a simulation study to verify parameter recovery at N=15-20, add prior sensitivity analysis, consider dropping the item-level η_i in favor of a simpler person-level contamination gate, fix the San Martin attribution issue, and either verify the MathArena problem count or use a conservative estimate. The proposal actually has solid computational planning and backup strategies in place, which strengthens the feasibility case somewhat. The main issues I'm identifying are a missing simulation study to validate the approach, practical identifiability concerns around the person-level parameters, and a few minor problems with citations and dataset descriptions that need correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad3012d5-9e70-4d44-ae81-eb1598f4b8eb",
  "isSidechain": false,
  "requestId": "req_011CbUzBTCbWXCDtTsngaeyE",
  "type": "assistant",
  "uuid": "83e3cbe8-81f4-4507-87e3-1c934f251ffc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEp7dz9iYKNBKt66Mp2DRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18495,
      "cache_read_input_tokens": 27590,
      "output_tokens": 3829,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18495,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3829,
          "cache_read_input_tokens": 27590,
          "cache_creation_input_tokens": 18495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18495
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

_source line 27 · 2026-05-28T12:44:45.714Z_

Now let me do a few more targeted searches to verify specific technical claims and check for any missed competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83e3cbe8-81f4-4507-87e3-1c934f251ffc",
  "isSidechain": false,
  "requestId": "req_011CbUzBTCbWXCDtTsngaeyE",
  "type": "assistant",
  "uuid": "044e6ba2-dec2-4f06-9261-9aa911318296",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEp7dz9iYKNBKt66Mp2DRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18495,
      "cache_read_input_tokens": 27590,
      "output_tokens": 3829,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18495,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3829,
          "cache_read_input_tokens": 27590,
          "cache_creation_input_tokens": 18495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18495
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

_source line 28 · 2026-05-28T12:44:54.129Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Gy7rbeQeYfPr8zS3HQCXWJ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search Silicon Bureaucracy and recent IRT+LLM work",
  "prompt": "I need to check for two specific things:\n\n1. Search for \"Silicon Bureaucracy and AI Test-Oriented Education\" (arxiv 2603.21636, March 2026). This was identified as a potential competitor that combines contamination auditing with adversarial perturbation but without IRT. Use WebSearch to find it and WebFetch to read its abstract. Report what it does.\n\n2. Search for the most recent (April-May 2026) papers combining IRT with LLM evaluation:\n   - Search: \"item response theory\" \"large language model\" site:arxiv.org 2026\n   - Search: \"IRT\" \"benchmark\" \"contamination\" LLM 2026\n   - Any paper from April-May 2026 that uses IRT for LLM evaluation with contamination awareness\n\n3. Search for \"LEGO-IRT\" LLM evaluation — mentioned as a concurrent IRT-for-LLMs work. Verify if it exists.\n\n4. Search for \"Open LLM Leaderboard\" per-item response data availability — the proposal claims per-item results are available at huggingface.co/datasets/open-llm-leaderboard/results. Verify this claim.\n\nReport what you find for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "044e6ba2-dec2-4f06-9261-9aa911318296",
  "isSidechain": false,
  "requestId": "req_011CbUzBTCbWXCDtTsngaeyE",
  "type": "assistant",
  "uuid": "081abdd0-397d-427e-b91e-820abf4f29d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEp7dz9iYKNBKt66Mp2DRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18495,
      "cache_read_input_tokens": 27590,
      "output_tokens": 3829,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18495,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3829,
          "cache_read_input_tokens": 27590,
          "cache_creation_input_tokens": 18495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18495
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

_source line 29 · 2026-05-28T12:44:59.050Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Jn6TeGZkWY5zZMgv7Qin7D`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check MaSTer code availability",
  "prompt": "I need to verify whether the MaSTer code for adversarial math variant generation is available. \n\n1. Search for \"github.com/sustech-nlp/MaSTer\" — try to access this repo via WebFetch\n2. Search for \"MaSTer\" \"adversarial\" \"math\" \"variant\" github 2026\n3. Search for the MaSTer paper: \"Toward Automated Robustness Evaluation of Mathematical Reasoning\" arXiv 2026 — verify it exists and check if the paper mentions code availability\n\nAlso search for:\n4. Any other open-source adversarial math variant generation tools released in 2025-2026\n5. \"SymPy\" \"math problem\" \"perturbation\" OR \"variant\" generation — to assess whether SymPy-backed verification is standard practice\n\nReport what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "081abdd0-397d-427e-b91e-820abf4f29d2",
  "isSidechain": false,
  "requestId": "req_011CbUzBTCbWXCDtTsngaeyE",
  "type": "assistant",
  "uuid": "75437b28-1ec0-43a6-97f2-f67d5eb1024d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEp7dz9iYKNBKt66Mp2DRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18495,
      "cache_read_input_tokens": 27590,
      "output_tokens": 3829,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18495,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3829,
          "cache_read_input_tokens": 27590,
          "cache_creation_input_tokens": 18495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18495
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

_source line 30 · 2026-05-28T12:47:23.968Z_

<details><summary>↩ Tool result · `toolu_01Jn6TeGZkWY5zZMgv7Qin7D`</summary>

```text
I now have all the information needed. Here is the full report.

---

## Findings Report

### 1. MaSTer GitHub Repository (github.com/sustech-nlp/MaSTer)

**The repository does NOT currently exist.** WebFetch returns HTTP 404 for `https://github.com/sustech-nlp/MaSTer` (and lowercase/alternate-name variants like `master` and `AR-CHECKER`). I also checked the SUSTech-NLP GitHub organization page, which lists 24 repositories -- none of the visible ones are named MaSTer or relate to adversarial math variant generation.

However, the paper's HTML version at arXiv **explicitly states**: "Our code is released at https://github.com/sustech-nlp/MaSTer." This means the authors have declared the intent to release code at that URL, but the repository either has not been created yet, is set to private, or was taken down.

### 2. The MaSTer Paper

**The paper exists and is confirmed.** "Toward Automated Robustness Evaluation of Mathematical Reasoning" is available on arXiv as [2506.05038](https://arxiv.org/abs/2506.05038).

- **First submitted:** June 5, 2025
- **Last revised:** April 24, 2026 (v2)
- **Authors:** Yutao Hou, Zeguan Xiao, Fei Yu, Yihan Jiang, Ma Shuguang, Zhaoqian Dai, Hailiang Huang, Yun Chen, and Guanhua Chen
- **Affiliations:** Shanghai University of Finance and Economics, Ant Group, Southern University of Science and Technology (SUSTech)

**Methodology (MaSTer = Math Stress Tester):**
- A three-component loop: Rewriter, Verifier, and multi-round iteration
- Generates adversarial variants via a **multi-round rewrite-verify loop**
- Runs N independent parallel rewriting streams (default N=5) with up to K iterations each (default K=3)
- The **verifier is entirely LLM-based** (Qwen2.5-32B-Instruct, achieving 98% precision) -- it does NOT use SymPy or any symbolic computation library
- Verification checks two criteria: semantic preservation of the original question AND whether the target model's answer diverges from ground truth
- Tested on GSM8K, MATH-500, and extends to non-math tasks (MMLU, MMLU-Pro, CommonsenseQA)

**Key takeaway on code:** The paper claims code is released, but the URL returns 404. The code is **not publicly accessible** as of now.

### 3. Other Open-Source Adversarial Math Variant Generation Tools (2024-2026)

**a) Adversarial Math Word Problem Generation (EMNLP 2024)**
- Repository: [github.com/ruoyuxie/adversarial_mwps_generation](https://github.com/ruoyuxie/adversarial_mwps_generation)
- Paper: [arXiv:2402.17916](https://arxiv.org/abs/2402.17916)
- Uses GPT-4-turbo to convert math problems to Python code, then generates adversarial variants by editing numeric values via abstract syntax trees
- Apache-2.0 license, 7 stars, 9 commits, Python
- Does NOT use SymPy; relies on GPT-4-turbo API (~$0.01/problem)
- **This is actually available and public.**

**b) MSCR: Multi-Source Candidate Replacement**
- Paper: [arXiv:2511.08055](https://arxiv.org/pdf/2511.08055)
- Explores LLM mathematical reasoning vulnerability via systematic replacement strategies
- No confirmed public code repository found.

**c) MathAttack (2023)**
- Paper: [arXiv:2309.01686](https://arxiv.org/pdf/2309.01686)
- Proposes RobustMath dataset (300 adversarial math samples)
- Earlier work, predates 2025-2026 window.

### 4. SymPy-Backed Verification in Math Variant Generation

**SymPy-based verification IS becoming a recognized approach**, though it is not yet universal. Key findings:

**a) "Adaptive Problem Generation via Symbolic Representations" (Feb 2026)**
- Paper: [arXiv:2602.19187](https://arxiv.org/abs/2602.19187)
- This is the strongest example of SymPy-backed verification as standard practice
- Uses SymPy and SMT formulations to represent problems symbolically
- Three-step pipeline: (1) formalize seed problem into symbolic form, (2) mutate symbolically to create variants, (3) translate back to natural language
- Verification via `SymPy.simplify` (checking if difference reduces to zero) plus numeric validation with random variable substitution
- No public code repository found yet.

**b) Neuro-Symbolic Data Generation for Math Reasoning**
- Paper: [arXiv:2412.04857](https://arxiv.org/html/2412.04857v1)
- Uses symbolic representations for math data generation

**c) SymCode: Neurosymbolic Math via Verifiable Code Generation**
- Paper: [arXiv:2510.25975](https://arxiv.org/pdf/2510.25975)
- Reframes math problem-solving as verifiable code generation using SymPy

**Summary on SymPy:** SymPy-backed verification is gaining traction in the research community and is used for both variant generation and answer verification. However, purely LLM-based verification (as in MaSTer) and AST-based approaches (as in the EMNLP 2024 work) are also common. SymPy verification is not yet the dominant standard but is recognized as providing stronger guarantees (exact symbolic verification vs. probabilistic LLM judgment).

### Bottom Line

- **MaSTer code is NOT publicly available** despite the paper's claim. The declared GitHub URL returns 404.
- The only fully public and accessible adversarial math variant generation tool is [adversarial_mwps_generation](https://github.com/ruoyuxie/adversarial_mwps_generation) (EMNLP 2024).
- MaSTer's verification is purely LLM-based, not SymPy-based.
- SymPy-backed verification for math variant generation is an emerging practice (see the Feb 2026 "Adaptive Problem Generation" paper) but not yet the dominant approach.

agentId: a4dacba2e35e2827f (use SendMessage with to: 'a4dacba2e35e2827f' to continue this agent)
&lt;usage>total_tokens: 21684
tool_uses: 25
duration_ms: 144910&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75437b28-1ec0-43a6-97f2-f67d5eb1024d",
  "isSidechain": false,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "type": "user",
  "uuid": "25e29089-ec4d-443c-af7e-5845b123b24e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify whether the MaSTer code for adversarial math variant generation is available. \n\n1. Search for \"github.com/sustech-nlp/MaSTer\" — try to access this repo via WebFetch\n2. Search for \"MaSTer\" \"adversarial\" \"math\" \"variant\" github 2026\n3. Search for the MaSTer paper: \"Toward Automated Robustness Evaluation of Mathematical Reasoning\" arXiv 2026 — verify it exists and check if the paper mentions code availability\n\nAlso search for:\n4. Any other open-source adversarial math variant generation tools released in 2025-2026\n5. \"SymPy\" \"math problem\" \"perturbation\" OR \"variant\" generation — to assess whether SymPy-backed verification is standard practice\n\nReport what you find.",
    "agentId": "a4dacba2e35e2827f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is the full report.\n\n---\n\n## Findings Report\n\n### 1. MaSTer GitHub Repository (github.com/sustech-nlp/MaSTer)\n\n**The repository does NOT currently exist.** WebFetch returns HTTP 404 for `https://github.com/sustech-nlp/MaSTer` (and lowercase/alternate-name variants like `master` and `AR-CHECKER`). I also checked the SUSTech-NLP GitHub organization page, which lists 24 repositories -- none of the visible ones are named MaSTer or relate to adversarial math variant generation.\n\nHowever, the paper's HTML version at arXiv **explicitly states**: \"Our code is released at https://github.com/sustech-nlp/MaSTer.\" This means the authors have declared the intent to release code at that URL, but the repository either has not been created yet, is set to private, or was taken down.\n\n### 2. The MaSTer Paper\n\n**The paper exists and is confirmed.** \"Toward Automated Robustness Evaluation of Mathematical Reasoning\" is available on arXiv as [2506.05038](https://arxiv.org/abs/2506.05038).\n\n- **First submitted:** June 5, 2025\n- **Last revised:** April 24, 2026 (v2)\n- **Authors:** Yutao Hou, Zeguan Xiao, Fei Yu, Yihan Jiang, Ma Shuguang, Zhaoqian Dai, Hailiang Huang, Yun Chen, and Guanhua Chen\n- **Affiliations:** Shanghai University of Finance and Economics, Ant Group, Southern University of Science and Technology (SUSTech)\n\n**Methodology (MaSTer = Math Stress Tester):**\n- A three-component loop: Rewriter, Verifier, and multi-round iteration\n- Generates adversarial variants via a **multi-round rewrite-verify loop**\n- Runs N independent parallel rewriting streams (default N=5) with up to K iterations each (default K=3)\n- The **verifier is entirely LLM-based** (Qwen2.5-32B-Instruct, achieving 98% precision) -- it does NOT use SymPy or any symbolic computation library\n- Verification checks two criteria: semantic preservation of the original question AND whether the target model's answer diverges from ground truth\n- Tested on GSM8K, MATH-500, and extends to non-math tasks (MMLU, MMLU-Pro, CommonsenseQA)\n\n**Key takeaway on code:** The paper claims code is released, but the URL returns 404. The code is **not publicly accessible** as of now.\n\n### 3. Other Open-Source Adversarial Math Variant Generation Tools (2024-2026)\n\n**a) Adversarial Math Word Problem Generation (EMNLP 2024)**\n- Repository: [github.com/ruoyuxie/adversarial_mwps_generation](https://github.com/ruoyuxie/adversarial_mwps_generation)\n- Paper: [arXiv:2402.17916](https://arxiv.org/abs/2402.17916)\n- Uses GPT-4-turbo to convert math problems to Python code, then generates adversarial variants by editing numeric values via abstract syntax trees\n- Apache-2.0 license, 7 stars, 9 commits, Python\n- Does NOT use SymPy; relies on GPT-4-turbo API (~$0.01/problem)\n- **This is actually available and public.**\n\n**b) MSCR: Multi-Source Candidate Replacement**\n- Paper: [arXiv:2511.08055](https://arxiv.org/pdf/2511.08055)\n- Explores LLM mathematical reasoning vulnerability via systematic replacement strategies\n- No confirmed public code repository found.\n\n**c) MathAttack (2023)**\n- Paper: [arXiv:2309.01686](https://arxiv.org/pdf/2309.01686)\n- Proposes RobustMath dataset (300 adversarial math samples)\n- Earlier work, predates 2025-2026 window.\n\n### 4. SymPy-Backed Verification in Math Variant Generation\n\n**SymPy-based verification IS becoming a recognized approach**, though it is not yet universal. Key findings:\n\n**a) \"Adaptive Problem Generation via Symbolic Representations\" (Feb 2026)**\n- Paper: [arXiv:2602.19187](https://arxiv.org/abs/2602.19187)\n- This is the strongest example of SymPy-backed verification as standard practice\n- Uses SymPy and SMT formulations to represent problems symbolically\n- Three-step pipeline: (1) formalize seed problem into symbolic form, (2) mutate symbolically to create variants, (3) translate back to natural language\n- Verification via `SymPy.simplify` (checking if difference reduces to zero) plus numeric validation with random variable substitution\n- No public code repository found yet.\n\n**b) Neuro-Symbolic Data Generation for Math Reasoning**\n- Paper: [arXiv:2412.04857](https://arxiv.org/html/2412.04857v1)\n- Uses symbolic representations for math data generation\n\n**c) SymCode: Neurosymbolic Math via Verifiable Code Generation**\n- Paper: [arXiv:2510.25975](https://arxiv.org/pdf/2510.25975)\n- Reframes math problem-solving as verifiable code generation using SymPy\n\n**Summary on SymPy:** SymPy-backed verification is gaining traction in the research community and is used for both variant generation and answer verification. However, purely LLM-based verification (as in MaSTer) and AST-based approaches (as in the EMNLP 2024 work) are also common. SymPy verification is not yet the dominant standard but is recognized as providing stronger guarantees (exact symbolic verification vs. probabilistic LLM judgment).\n\n### Bottom Line\n\n- **MaSTer code is NOT publicly available** despite the paper's claim. The declared GitHub URL returns 404.\n- The only fully public and accessible adversarial math variant generation tool is [adversarial_mwps_generation](https://github.com/ruoyuxie/adversarial_mwps_generation) (EMNLP 2024).\n- MaSTer's verification is purely LLM-based, not SymPy-based.\n- SymPy-backed verification for math variant generation is an emerging practice (see the Feb 2026 \"Adaptive Problem Generation\" paper) but not yet the dominant approach."
      }
    ],
    "totalDurationMs": 144910,
    "totalTokens": 21684,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 361,
      "cache_read_input_tokens": 19713,
      "output_tokens": 1609,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 361
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1609,
          "cache_read_input_tokens": 19713,
          "cache_creation_input_tokens": 361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 361,
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
      "bashCount": 4,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "75437b28-1ec0-43a6-97f2-f67d5eb1024d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "25e29089-ec4d-443c-af7e-5845b123b24e",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CRADE contamination-ability decomposition via gated IRT",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Tool result

_source line 33 · 2026-05-28T12:47:30.451Z_

<details><summary>↩ Tool result · `toolu_01Gy7rbeQeYfPr8zS3HQCXWJ`</summary>

```text
Now I have comprehensive information on all four items. Here is my full report.

---

## Report

### 1. "Silicon Bureaucracy and AI Test-Oriented Education" (arXiv 2603.21636)

**Status: Confirmed to exist.**

- **Authors:** Yiliang Song, Hongjun An, Jiangan Chen, Xuanchen Yan, Huan Song, Jiawei Shao, Xuelong Li
- **Date:** March 23, 2026 (revised March 28, 2026)
- **Abstract:** The paper frames the benchmark-centered LLM evaluation regime as "Silicon Bureaucracy and AI Test-Oriented Education." It argues benchmark scores may conflate exam-oriented competence with genuine capability due to contamination and semantic leakage. They propose an audit framework using a **router-worker setup** that compares a clean-control condition with noisy conditions where benchmark problems are systematically deleted, rewritten, and perturbed. If a benchmark is clean, noisy conditions should not outperform the clean control. They find widespread above-baseline gains under noisy conditions across multiple models, indicating contamination-related memory reactivation.
- **Does it use IRT?** **No.** There is no mention of Item Response Theory. The method is purely based on adversarial perturbation and contamination sensitivity auditing.
- **Characterization as competitor:** The claim that it "combines contamination auditing with adversarial perturbation but without IRT" is **accurate**. It addresses contamination sensitivity and score confidence but through a perturbation-based audit framework, not psychometric modeling.

### 2. Recent (April-May 2026) Papers Combining IRT with LLM Evaluation

Two relevant papers were found:

**a) "An Interpretable and Scalable Framework for Evaluating Large Language Models" (arXiv 2605.07046, May 7, 2026)**
- Authors: Xinhao Qu, Qiang Heng, Hao Zeng, Xiaoqian Liu
- Uses IRT with a majorization-minimization optimization approach for scalable LLM evaluation. Tested on MATH-500 and six Open LLM Leaderboard benchmarks. Claims orders-of-magnitude speedups over competing IRT methods.
- **Does NOT address contamination.** Focuses on scalability and interpretability of IRT for LLM evaluation.

**b) "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" (arXiv 2505.15055, initially May 2025, updated to v3)**
- Authors: Hongli Zhou et al.
- Proposes **PSN-IRT** (Pseudo-Siamese Network for Item Response Theory), an enhanced IRT framework with rich item parameters. Analyzes 11 LLM benchmarks comprising 41,871 items with 70+ models.
- **Does NOT directly address contamination** in its abstract, though it focuses on measurement quality of benchmarks.

**No paper from April-May 2026 was found that combines IRT with contamination-aware LLM evaluation.** The IRT papers focus on scalability, interpretability, and measurement quality, while contamination papers use non-IRT methods.

### 3. LEGO-IRT

**Status: Confirmed to exist.**

- **Paper:** "Toward a unified framework for data-efficient evaluation of large language models" (arXiv 2510.04051, October 5, 2025)
- **Authors:** Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang
- **What it does:** LEGO-IRT is a unified IRT-based framework for data-efficient LLM evaluation. Key contributions:
  - Natively supports both **binary and continuous** evaluation metrics (previous IRT methods were limited to binary correctness)
  - Uses a **factorized architecture** that decomposes model ability into general and structure-specific (per-metric, per-benchmark) components
  - Achieves stable capability estimates using just **3% of total evaluation items** across 70 LLMs and 5 benchmarks
  - Leverages cross-benchmark structural knowledge (correlations across metrics/benchmarks)
- **Characterization as "concurrent IRT-for-LLMs work" is accurate.** It is a genuine IRT-based LLM evaluation framework, though it dates from October 2025 and does not address contamination.

### 4. Open LLM Leaderboard Per-Item Response Data

**Status: Partially verified -- the claim is directionally correct but needs nuance.**

- The dataset at `huggingface.co/datasets/open-llm-leaderboard/results` exists and contains **aggregate scores** (per-benchmark accuracy, stderr, etc.) for ~4,580 models. It does **not** contain per-item response data -- it is a summary leaderboard table.
- However, the Open LLM Leaderboard **does** maintain per-item data in a separate location: `huggingface.co/datasets/open-llm-leaderboard/details`. This dataset has **63 configurations** (one per evaluated task/subtask) and stores per-sample evaluation results. Individual model "details" repos (e.g., `open-llm-leaderboard-old/details_{model_name}`) also exist with per-task splits.
- The `details` dataset is currently behind authentication (HTTP 401) and the dataset viewer is disabled, but the data can be loaded programmatically via the HuggingFace `datasets` library. The older v1 leaderboard details are under the `open-llm-leaderboard-old` organization.
- **Bottom line:** Per-item response data **does exist** and is publicly available, but the specific URL cited (`open-llm-leaderboard/results`) contains only aggregate scores. The per-item data is at `open-llm-leaderboard/details` (and in the old v1 format, in individual `details_*` repos). The claim is **substantially correct** in spirit -- per-item data is available from the Open LLM Leaderboard ecosystem -- but the exact dataset path cited may be slightly wrong.

Sources:
- [Silicon Bureaucracy (arXiv 2603.21636)](https://arxiv.org/abs/2603.21636)
- [Interpretable and Scalable IRT Framework (arXiv 2605.07046)](https://arxiv.org/abs/2605.07046)
- [Lost in Benchmarks / PSN-IRT (arXiv 2505.15055)](https://arxiv.org/abs/2505.15055)
- [LEGO-IRT (arXiv 2510.04051)](https://arxiv.org/abs/2510.04051)
- [Open LLM Leaderboard Results Dataset](https://huggingface.co/datasets/open-llm-leaderboard/results)
- [Open LLM Leaderboard Details Dataset](https://huggingface.co/datasets/open-llm-leaderboard/details)
- [Open LLM Leaderboard Contents Dataset](https://huggingface.co/datasets/open-llm-leaderboard/contents)
- [Open LLM Leaderboard v1 Archive](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)

agentId: aed00bb7e643d84c5 (use SendMessage with to: 'aed00bb7e643d84c5' to continue this agent)
&lt;usage>total_tokens: 26729
tool_uses: 20
duration_ms: 156316&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "081abdd0-397d-427e-b91e-820abf4f29d2",
  "isSidechain": false,
  "promptId": "decd441a-6e6c-4374-80a6-b6e3a36a228b",
  "type": "user",
  "uuid": "be19b727-6ed8-480e-810b-9c8d2553b073",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to check for two specific things:\n\n1. Search for \"Silicon Bureaucracy and AI Test-Oriented Education\" (arxiv 2603.21636, March 2026). This was identified as a potential competitor that combines contamination auditing with adversarial perturbation but without IRT. Use WebSearch to find it and WebFetch to read its abstract. Report what it does.\n\n2. Search for the most recent (April-May 2026) papers combining IRT with LLM evaluation:\n   - Search: \"item response theory\" \"large language model\" site:arxiv.org 2026\n   - Search: \"IRT\" \"benchmark\" \"contamination\" LLM 2026\n   - Any paper from April-May 2026 that uses IRT for LLM evaluation with contamination awareness\n\n3. Search for \"LEGO-IRT\" LLM evaluation — mentioned as a concurrent IRT-for-LLMs work. Verify if it exists.\n\n4. Search for \"Open LLM Leaderboard\" per-item response data availability — the proposal claims per-item results are available at huggingface.co/datasets/open-llm-leaderboard/results. Verify this claim.\n\nReport what you find for each.",
    "agentId": "aed00bb7e643d84c5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all four items. Here is my full report.\n\n---\n\n## Report\n\n### 1. \"Silicon Bureaucracy and AI Test-Oriented Education\" (arXiv 2603.21636)\n\n**Status: Confirmed to exist.**\n\n- **Authors:** Yiliang Song, Hongjun An, Jiangan Chen, Xuanchen Yan, Huan Song, Jiawei Shao, Xuelong Li\n- **Date:** March 23, 2026 (revised March 28, 2026)\n- **Abstract:** The paper frames the benchmark-centered LLM evaluation regime as \"Silicon Bureaucracy and AI Test-Oriented Education.\" It argues benchmark scores may conflate exam-oriented competence with genuine capability due to contamination and semantic leakage. They propose an audit framework using a **router-worker setup** that compares a clean-control condition with noisy conditions where benchmark problems are systematically deleted, rewritten, and perturbed. If a benchmark is clean, noisy conditions should not outperform the clean control. They find widespread above-baseline gains under noisy conditions across multiple models, indicating contamination-related memory reactivation.\n- **Does it use IRT?** **No.** There is no mention of Item Response Theory. The method is purely based on adversarial perturbation and contamination sensitivity auditing.\n- **Characterization as competitor:** The claim that it \"combines contamination auditing with adversarial perturbation but without IRT\" is **accurate**. It addresses contamination sensitivity and score confidence but through a perturbation-based audit framework, not psychometric modeling.\n\n### 2. Recent (April-May 2026) Papers Combining IRT with LLM Evaluation\n\nTwo relevant papers were found:\n\n**a) \"An Interpretable and Scalable Framework for Evaluating Large Language Models\" (arXiv 2605.07046, May 7, 2026)**\n- Authors: Xinhao Qu, Qiang Heng, Hao Zeng, Xiaoqian Liu\n- Uses IRT with a majorization-minimization optimization approach for scalable LLM evaluation. Tested on MATH-500 and six Open LLM Leaderboard benchmarks. Claims orders-of-magnitude speedups over competing IRT methods.\n- **Does NOT address contamination.** Focuses on scalability and interpretability of IRT for LLM evaluation.\n\n**b) \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\" (arXiv 2505.15055, initially May 2025, updated to v3)**\n- Authors: Hongli Zhou et al.\n- Proposes **PSN-IRT** (Pseudo-Siamese Network for Item Response Theory), an enhanced IRT framework with rich item parameters. Analyzes 11 LLM benchmarks comprising 41,871 items with 70+ models.\n- **Does NOT directly address contamination** in its abstract, though it focuses on measurement quality of benchmarks.\n\n**No paper from April-May 2026 was found that combines IRT with contamination-aware LLM evaluation.** The IRT papers focus on scalability, interpretability, and measurement quality, while contamination papers use non-IRT methods.\n\n### 3. LEGO-IRT\n\n**Status: Confirmed to exist.**\n\n- **Paper:** \"Toward a unified framework for data-efficient evaluation of large language models\" (arXiv 2510.04051, October 5, 2025)\n- **Authors:** Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang\n- **What it does:** LEGO-IRT is a unified IRT-based framework for data-efficient LLM evaluation. Key contributions:\n  - Natively supports both **binary and continuous** evaluation metrics (previous IRT methods were limited to binary correctness)\n  - Uses a **factorized architecture** that decomposes model ability into general and structure-specific (per-metric, per-benchmark) components\n  - Achieves stable capability estimates using just **3% of total evaluation items** across 70 LLMs and 5 benchmarks\n  - Leverages cross-benchmark structural knowledge (correlations across metrics/benchmarks)\n- **Characterization as \"concurrent IRT-for-LLMs work\" is accurate.** It is a genuine IRT-based LLM evaluation framework, though it dates from October 2025 and does not address contamination.\n\n### 4. Open LLM Leaderboard Per-Item Response Data\n\n**Status: Partially verified -- the claim is directionally correct but needs nuance.**\n\n- The dataset at `huggingface.co/datasets/open-llm-leaderboard/results` exists and contains **aggregate scores** (per-benchmark accuracy, stderr, etc.) for ~4,580 models. It does **not** contain per-item response data -- it is a summary leaderboard table.\n- However, the Open LLM Leaderboard **does** maintain per-item data in a separate location: `huggingface.co/datasets/open-llm-leaderboard/details`. This dataset has **63 configurations** (one per evaluated task/subtask) and stores per-sample evaluation results. Individual model \"details\" repos (e.g., `open-llm-leaderboard-old/details_{model_name}`) also exist with per-task splits.\n- The `details` dataset is currently behind authentication (HTTP 401) and the dataset viewer is disabled, but the data can be loaded programmatically via the HuggingFace `datasets` library. The older v1 leaderboard details are under the `open-llm-leaderboard-old` organization.\n- **Bottom line:** Per-item response data **does exist** and is publicly available, but the specific URL cited (`open-llm-leaderboard/results`) contains only aggregate scores. The per-item data is at `open-llm-leaderboard/details` (and in the old v1 format, in individual `details_*` repos). The claim is **substantially correct** in spirit -- per-item data is available from the Open LLM Leaderboard ecosystem -- but the exact dataset path cited may be slightly wrong.\n\nSources:\n- [Silicon Bureaucracy (arXiv 2603.21636)](https://arxiv.org/abs/2603.21636)\n- [Interpretable and Scalable IRT Framework (arXiv 2605.07046)](https://arxiv.org/abs/2605.07046)\n- [Lost in Benchmarks / PSN-IRT (arXiv 2505.15055)](https://arxiv.org/abs/2505.15055)\n- [LEGO-IRT (arXiv 2510.04051)](https://arxiv.org/abs/2510.04051)\n- [Open LLM Leaderboard Results Dataset](https://huggingface.co/datasets/open-llm-leaderboard/results)\n- [Open LLM Leaderboard Details Dataset](https://huggingface.co/datasets/open-llm-leaderboard/details)\n- [Open LLM Leaderboard Contents Dataset](https://huggingface.co/datasets/open-llm-leaderboard/contents)\n- [Open LLM Leaderboard v1 Archive](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)"
      }
    ],
    "totalDurationMs": 156316,
    "totalTokens": 26729,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 24323,
      "output_tokens": 1759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 646
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1759,
          "cache_read_input_tokens": 24323,
          "cache_creation_input_tokens": 646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 646,
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
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "081abdd0-397d-427e-b91e-820abf4f29d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-28T12:48:11.772Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information from all searches. Let me synthesize everything for the final review.

Key additional findings:

1. **MaSTer code**: Confirmed unavailable (404). The proposal already addresses this with backup plans. However, a critical finding is that **MaSTer uses LLM-based verification, NOT SymPy**. The proposal says it will use "MaSTer-style multi-round rewrite-verify" with "SymPy answer verification" — this conflates MaSTer's approach with SymPy. MaSTer uses Qwen2.5-32B-Instruct for verification, not SymPy. 

The proposal's approach is actually inspired by MaSTer's pipeline but substitutes SymPy verification for MaSTer's LLM-based verification, which is a reasonable design choice but doesn't strictly replicate MaSTer's methodology.

2. **Silicon Bureaucracy**: Confirmed as non-IRT, no direct competitor.

3. **LEGO-IRT**: Exists (Oct 2025), is a concurrent IRT-for-LLMs work but doesn't address contamination. Should be cited but is not a competitor.

4. **Open LLM Leaderboard data**: Per-item data exists but at a different URL than cited.

5. **No new competing work found at the three-way intersection.**

6. **San Martin et al. attribution**: WRONG — should be Noventa et al. (2024).

The three-way intersection of IRT, contamination correction, and adversarial variants appears genuinely unoccupied, and the DGM extension creatively bridges psychometric test security to LLM evaluation. RIDE comes closest by combining IRT with adversarial items, but only uses IRT for difficulty estimation rather than contamination-ability decomposition. The gated IRT formulation with paired adversarial items is novel, though the individual components themselves aren't new—it's a synthesis that's valuable but not transformative.

Feasibility looks challenging...

the G-2PL estimation at N=15-20 falls well below published minimums (typically N≥50 even with Bayesian approaches), and while person-level parameters might hold up given 1000 items, item-level parameters especially will be heavily prior-driven. A simulation study validating parameter recovery at these sample sizes is critical but absent, and prior sensitivity analysis is missing too. The compute budget of 180-210 H100-hours is tight but workable, and the MaSTer backup plans are reasonable, but this core estimation challenge represents the biggest risk.

The proposal itself is exceptionally detailed and well-structured with clear equations and a fully specified estimation strategy, plus a three-pronged validation approach with causal evidence. The main weakness is verbosity—the core contribution could be stated more concisely.

**Impact**: 4

/5
If this works, it establishes a principled, measurement-theoretically grounded framework for contamination-corrected LLM evaluation that decomposes ability from contamination and generalizes across benchmarks. But whether the estimates are actually reliable at N=15-20 remains the critical uncertainty.

The overall score comes to 3.75, below the 4.0 threshold, so the proposal needs revision. The most pressing issues are the missing simulation study for parameter recovery at these sample sizes, the practical non-identifiability of item-level η_i parameters, a citation error (San Martin vs. Noventa), and clarifying that MaSTer uses LLM verification rather than symbolic methods.

Looking back at what's already there, the proposal actually covers a lot of ground—person-fit statistics, residual diagnostics, three different estimation approaches, comprehensive validation, and contingency plans for variant generation. The core gaps are really just the simulation study, prior sensitivity analysis, and an explicit acknowledgment that item-level conclusions may be unreliable at these sample sizes while person-level inferences could still hold. These are fixable additions that wouldn't require rethinking the whole approach. These gaps—missing simulation studies, prior sensitivity analysis, and explicit acknowledgment that item parameters will be heavily prior-dependent—are meaningful but not disqualifying. I'm settling on a revise recommendation and drafting the final assessment JSON.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be19b727-6ed8-480e-810b-9c8d2553b073",
  "isSidechain": false,
  "requestId": "req_011CbUzVLTYSCuWHFNKJZgM4",
  "type": "assistant",
  "uuid": "175e02a0-fc28-45fb-af1b-38b78d82148d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHcRgEFY8EYSMsi2mkgqzm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1711,
      "cache_creation_input_tokens": 5691,
      "cache_read_input_tokens": 46085,
      "output_tokens": 3433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1711,
          "output_tokens": 3433,
          "cache_read_input_tokens": 46085,
          "cache_creation_input_tokens": 5691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5691
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

_source line 35 · 2026-05-28T12:48:54.516Z_

Now I have comprehensive verification results from all agents. Let me synthesize my findings for the final review.

## Synthesis of Verification Results

**References verified:** 18/20 key references confirmed. Two issues: (1) "San Martin et al. (Psychometrika 2024)" is actually authored by **Noventa, Ye, Kelava, and Spoto** — wrong attribution; (2) PaCoST is EMNLP 2024 Findings, not just "arXiv 2024."

**Novelty verified:** Exhaustive search across 10+ query variations confirms **no paper occupies the three-way intersection** of IRT + contamination correction + adversarial variants. RIDE is closest (IRT + adversarial) but uses IRT only for difficulty rewards, not contamination decomposition.

**Critical technical finding:** MaSTer uses **LLM-based verification** (Qwen2.5-32B-Instruct), **not SymPy**. The proposal's "MaSTer-style + SymPy" is actually a hybrid not described in MaSTer.

**IRT feasibility concern:** N=15-20 is below **every published minimum** for 2PL IRT estimation. Even the most aggressive Bayesian small-sample papers (Fox 2025) bottom out at N=50. Item-level η_i will be practically non-identifiable (prior-dominated). Person-level θ_j and ξ_j may be viable due to 1000 items per person.

**MathArena count:** ~897 cannot be independently verified; original paper says 162, expanded version adds competitions but no source confirms 897.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "Three-way intersection (gated IRT + contamination correction + adversarial paired items) verified as genuinely unoccupied across arXiv, OpenReview, and Semantic Scholar through 10+ query variations. DGM extension from psychometric test security to LLM evaluation is a creative theoretical bridge. RIDE is closest competitor but uses IRT only for difficulty rewards, not contamination-ability decomposition."},
    "feasibility": {"score": 3, "rationale": "Core estimation challenge is severe: G-2PL at N=15-20 is far below any published minimum (even Bayesian methods require N≥50). Person-level parameters (θ_j, ξ_j) may be estimable via 1000 items, but item-level η_i will be dominated by priors. No simulation study or prior sensitivity analysis is planned — both are non-negotiable for a psychometric paper proposing a novel model at unprecedented sample sizes. Compute budget (180-210 H100-hrs) is tight but feasible; backup plans for MaSTer code are concrete."},
    "clarity": {"score": 4, "rationale": "Model specification is rigorous with clear equations, fully specified estimation strategy (MCMC priors, chains, convergence criteria), comprehensive three-pronged validation, and explicit backup plans. The identifiability argument is well-structured. Verbose but technically precise."},
    "impact": {"score": 4, "rationale": "If estimation challenges are resolved, this would establish the first principled measurement-theoretic framework for contamination-corrected LLM evaluation. The ability-contamination decomposition addresses a genuine and urgent need. Framework is applicable to any benchmark, not tied to a specific dataset. Impact is contingent on demonstrating reliable estimation at small N."}
  },
  "issues": [
    "MODERATE: No simulation study planned for G-2PL parameter recovery at N=15-20. This is non-negotiable for a psychometric paper. Standard practice requires: (1) generate data from G-2PL with known θ, ξ, η, a, b parameters at N=15 and N=20; (2) fit the model; (3) report bias, RMSE, and 95% credible interval coverage for each parameter type. Without this, reviewers cannot assess whether the model produces meaningful estimates at this unprecedented sample size. Budget: 1-2 days compute on CPU.",
    "MODERATE: Item-level η_i is practically non-identifiable at N=15-20 — each item's contamination susceptibility is estimated from only 15-20 binary observations, and the bilinear interaction ξ_j·η_i creates scaling indeterminacy. The proposal's model adequacy plan (Q3, lz*, residuals) tests model fit but does not address the fundamental issue that η_i estimates will be dominated by hierarchical priors. The proposal should explicitly acknowledge this limitation, report posterior shrinkage for η_i vs. θ_j, and consider an ablation with person-level-only contamination (dropping η_i, using a simpler ξ_j-only gate).",
    "MODERATE: No prior sensitivity analysis planned. With N=15-20 per item, posterior estimates for a_i, η_i, and δ_i will be heavily prior-driven. The proposal specifies priors (LogNormal(0,0.5) for a_i, hierarchical Beta for ξ_j/η_i) but does not test sensitivity. Must report results under at least 2-3 meaningfully different prior specifications (e.g., diffuse vs. informative) to demonstrate which conclusions are data-driven vs. prior-driven.",
    "MINOR: San Martin et al. (Psychometrika 2024) is incorrectly attributed — actual authors are Noventa, Ye, Kelava, and Spoto. San Martin is only cited within that paper.",
    "MINOR: MaSTer uses LLM-based verification (Qwen2.5-32B-Instruct at 98% precision), not SymPy. The proposal's 'MaSTer-style multi-round rewrite-verify with SymPy verification' is actually a novel hybrid — this should be stated clearly rather than characterized as following MaSTer.",
    "MINOR: LEGO-IRT (arXiv Oct 2025) is a concurrent IRT-for-LLMs framework (binary+continuous metrics, 70 LLMs, 3% item usage) that should be cited in the landscape analysis, even though it does not address contamination."
  ],
  "feedback": "The proposal is close to passing — the core idea is verified as novel, theoretically well-grounded, and addressing a real gap. Three additions would push it over the threshold:\n\n(1) **Add simulation study (Week 4, 1-2 days):** Generate 50 synthetic datasets from G-2PL with known parameters at N=15 and N=20. Vary contamination prevalence (10%, 30%, 50% of models contaminated) and contamination strength (weak/moderate/strong ξ). Report: (a) θ_j recovery (bias, RMSE, coverage), (b) ξ_j recovery, (c) η_i recovery, (d) ranking correlation of estimated θ with true θ. This is the single most important addition — without it, the paper will be rejected by any psychometric reviewer.\n\n(2) **Add prior sensitivity analysis:** Report G-2PL results under 3 prior specifications: (a) the proposed hierarchical Beta priors, (b) weakly informative priors (Beta(1,1) for ξ/η, LogNormal(0,1) for a), (c) strongly informative priors based on external contamination detectors (ConStat/PaCoST flags as informative priors on ξ_j). Show which conclusions change and which are robust.\n\n(3) **Explicitly scope item-level vs. person-level claims:** Acknowledge that η_i estimates will have wide posterior intervals and high shrinkage toward hierarchical mean. Frame the primary contribution as person-level decomposition (θ_j, ξ_j rankings) with item-level η_i as secondary/exploratory. Consider an ablation dropping η_i entirely (ξ_j-only gate: P = ξ_j·p_mem + (1-ξ_j)·2PL) — this has only M additional parameters and is far more identifiable.\n\nAlso fix: San Martin → Noventa et al. attribution, clarify MaSTer vs. SymPy verification distinction, cite LEGO-IRT.",
  "reason": "Genuinely novel three-way intersection verified, but the core IRT estimation at N=15-20 lacks the mandatory simulation study and prior sensitivity analysis needed to demonstrate viability at unprecedented sample sizes."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "175e02a0-fc28-45fb-af1b-38b78d82148d",
  "isSidechain": false,
  "requestId": "req_011CbUzVLTYSCuWHFNKJZgM4",
  "type": "assistant",
  "uuid": "6e015a35-c915-42c8-9405-cd6fd1715633",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHcRgEFY8EYSMsi2mkgqzm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1711,
      "cache_creation_input_tokens": 5691,
      "cache_read_input_tokens": 46085,
      "output_tokens": 3433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1711,
          "output_tokens": 3433,
          "cache_read_input_tokens": 46085,
          "cache_creation_input_tokens": 5691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5691
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "6e015a35-c915-42c8-9405-cd6fd1715633",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CRADE contamination-ability decomposition via gated IRT",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "6e015a35-c915-42c8-9405-cd6fd1715633",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CRADE contamination-ability decomposition via gated IRT",
  "sessionId": "5cac9770-19c9-4e54-bf3a-6f5cf7e1ebb4"
}
```

---
