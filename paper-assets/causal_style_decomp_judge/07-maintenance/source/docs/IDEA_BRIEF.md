# Idea Brief: Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation


- **Idea ID**: `idea_028`
- **Created**: 2026-05-20
- **Approved**: 2026-05-20
- **Source**: foreign:be-idea-gen-0515-4
- **Level**: solid
- **Target Venues**: AAAI 2027 (abstract: July 21, full paper: July 28, 2026 — primary target, 10 weeks), ICLR 2027 (estimated deadline: September 24, 2026 — comfortable 18-week runway), ARR October 2026 cycle (estimated deadline: October 15, 2026 — tertiary option, 21-week runway)

## Seed Topic

web_research

## Core Problem

How can we isolate and remove the causal effect of surface-level style on LLM judge scores while preserving legitimate style-content associations, recovering a score that more faithfully reflects content quality?

## Opportunity / Why Now

Style bias is the dominant bias in LLM judges (effect size 0.76–0.92 across all models per Soumik 2026), vastly exceeding position bias (≤0.04), yet debiasing research overwhelmingly targets position bias. SOS-Bench (ICLR 2025) demonstrated that LLM judges prioritize style over factuality and safety across 152,380 data points. The 'Preference Leakage' paper (ICLR 2026) found judges rely heavily on 'stylistic regularities—tone consistency, sentence cadence, punctuation density.' FairJudge (arXiv Feb 2026) addresses style bias through judge retraining (SFT+DPO+GRPO), but this requires training a new judge model and does not apply to black-box commercial judges. Meanwhile, the CASSE study (Jan 2026) shows style features are 'deeply entangled rather than orthogonal'—prompting for conciseness significantly reduces perceived expertise—highlighting that naive style removal risks destroying legitimate quality signals. This creates a need for a principled causal method that can (a) apply to any black-box judge, (b) quantify per-response style contributions, and (c) distinguish bias from legitimate style-quality correlation. Causal intervention techniques for LLMs now achieve 92.3% style transfer accuracy while preserving content, and the RATE framework (ICML 2025) provides a double-rewrite protocol for unbiased estimation with imperfect counterfactuals, making this technically feasible.

## Landscape (SOTA & Limitations)

SOS-Bench (ICLR 2025) is the largest meta-benchmark documenting style-over-substance failure but proposes no fix. FairJudge (arXiv 2602.06625, Feb 2026) is the most directly relevant concurrent work: it trains a dedicated judge via SFT→DPO→GRPO on a curated 16K-instance dataset with contrastive perturbations along five non-semantic dimensions (position, length, format, reasoning style, model provenance), achieving 76.83% agreement on PandaLM and 78.82% on JudgeLM; however, it requires retraining a new judge model (Qwen3-VL 2B/4B/8B backbones) and cannot debias existing black-box commercial judges (GPT-4o, Claude, Gemini). Soumik (April 2026) tests 9 debiasing strategies across 5 judges but focuses on position/verbosity bias without systematic causal style removal. JudgeBiasBench (March 2026) uses Gemini-2.0-Flash for counterfactual bias injection but applies this to construct biased test instances rather than to estimate and remove style effects. RATE (ICML 2025) is the closest methodological precedent—it estimates causal effects of high-level attributes on reward model scores via a double-rewrite correction for imperfect counterfactuals—but targets reward model explainability, not judge debiasing. The ISE framework (Choi et al., NAACL 2024) argues ATE is inapplicable to text treatments due to positivity violations from high dimensionality, but this criticism applies to free-text treatments, not to well-defined binary style interventions where positivity holds by construction (Pryzant et al. 2021; Veitch et al. UAI 2020). Length-Controlled AlpacaEval (ICLR 2025) demonstrates effective post-hoc regression debiasing but only controls for a single dimension (length) at zero additional inference cost. Bias-Bounded Evaluation (arXiv March 2026) injects calibrated Gaussian noise for differential-privacy-inspired debiasing, retaining 61–99% ranking correlation on Arena-Hard-Auto. CyclicJudge (arXiv March 2026) uses round-robin judge assignment to reduce inter-judge variance but is style-agnostic. RBD (NeurIPS 2025) fine-tunes a reasoning-based bias detector achieving 18.5% accuracy improvement but without causal style decomposition. UDA (AAAI 2026) reduces inter-judge Elo divergence by 63.4% via adaptive K-factor calibration. The CASSE dataset (Jan 2026) documents cross-feature stylistic interactions across 12 style features, showing conciseness reduces perceived expertise, supporting our legitimacy-aware correction design. Causal Effect Estimation with Latent Textual Treatments (arXiv Feb 2026) proposes SAE-based causal estimation for latent text features but has not been applied to judge debiasing. Double Machine Learning (Chernozhukov et al. 2018) provides the partially linear model framework and DoubleML Python package we adopt for flexible decomposition. No arXiv preprint or OpenReview submission as of May 2026 proposes content-preserving binary style counterfactuals combined with doubly-robust DML estimation for black-box judge debiasing.

## Proposed Approach

We propose Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework in four stages.

**Stage 1 — Binary Style Counterfactual Generation.** For each response under evaluation, generate style counterfactuals along three binary axes: (A1) formality (formal ↔ casual), (A2) verbosity (verbose ↔ terse), (A3) formatting (structured/markdown ↔ plain prose). These three axes are chosen for genuine independence: formality concerns register and word choice, verbosity concerns information density, and formatting concerns visual layout. We use Qwen3-32B with axis-specific prompts, applying the RATE double-rewrite protocol: for each axis, generate (i) a counterfactual x' by flipping the axis and (ii) a double-rewrite x'' by flipping x' back. This yields 6 rewrites per response (2 per axis). Content preservation is enforced via a conjunction of BERTScore ≥ 0.92, NLI entailment ≥ 0.95 (DeBERTa-v3-large-MNLI), GPT-4o-mini content-preservation verification, and human spot-checks on a 10% random sample. **Theoretical justification for binary ATE:** Unlike free-text treatments where positivity is structurally violated (Choi et al. NAACL 2024), binary style axes define well-posed interventions satisfying positivity—any text can be made formal or casual, verbose or terse, structured or plain—following the functional intervention framework (Pryzant et al. 2021; Veitch et al. UAI 2020). RATE's Assumption 1 (direction-independent rewrite noise) and Assumption 2 (additive decomposition of reward into attribute and noise components) provide sufficient conditions for unbiased ATE estimation under imperfect counterfactuals.

**Stage 2 — Doubly-Robust Causal Effect Estimation via DML.** Score each original response and its 6 counterfactuals with the target LLM judge (7 scorings per response). Estimate per-axis treatment effects using a Double Machine Learning partially linear model (Chernozhukov et al. 2018): score = β₁·formality + β₂·verbosity + β₃·formatting + g(content_features) + ε, where β coefficients capture interpretable style effects and g(·) is a nonparametric function of content features (estimated via gradient-boosted trees with 5-fold cross-fitting). This replaces the linear additive SCM: the partially linear form preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects, and the doubly-robust property ensures consistency if either the outcome model or propensity model is correctly specified. For handling residual axis correlations (e.g., formatting weakly correlating with verbosity), we use the multivariate treatment extension of DoubleML, jointly estimating all three β coefficients rather than decomposing them independently. We include ablations comparing: (i) linear additive, (ii) DML partially linear, and (iii) fully nonparametric (kernel-based) decompositions, plus an ISE-based continuous estimator as a methodological comparison.

**Stage 3 — Legitimacy-Aware Score Adjustment.** Rather than naively subtracting the full estimated style ATE (which risks over-correction when style legitimately signals quality—e.g., well-structured markdown for technical content), we introduce a conservatism parameter α ∈ [0,1]: debiased_score = raw_score − α · Σ β_k · style_k. We determine α by maximizing Spearman correlation with ground-truth quality on a held-out validation set. Additionally, we test domain-conditional α values: for each content domain (coding, reasoning, creative writing, factual QA), we estimate whether style-quality correlations are legitimate by checking if style effects are consistent across domains (bias) vs. domain-specific (potentially legitimate). Style effects that are large and domain-invariant are classified as bias; domain-specific effects are partially retained.

**Stage 4 — Amortized Deployment (optional).** To reduce the ~7x overhead of full CSD for large-scale deployment, we train a lightweight amortized style-effect predictor: a small regression model (e.g., linear probe on text embeddings from a frozen encoder) trained on the counterfactual data from Stage 1–2 to predict per-response style attribution vectors from response features alone. At deployment, this predictor estimates style effects without generating new counterfactuals, reducing marginal cost to near-zero. We validate that the amortized predictor recovers ≥90% of the debiasing improvement of the full pipeline.

**Evaluation.** We evaluate across five LLM judges (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Llama-3.3-70B, Qwen3-32B) on four benchmarks: (1) SOS-Bench—measuring whether debiased scores better correlate with objective correctness on constituent benchmarks (IFEval, MMLU-Pro, GPQA) rather than style; (2) LLMBar adversarial set—measuring whether debiased judges resist choosing wrong-but-polished over correct-but-plain responses; (3) RewardBench—domain-specific analysis across chat-hard, safety, and reasoning subsets; (4) RubricBench—1,147 pairwise comparisons with expert-annotated atomic rubrics targeting misleading surface bias. We additionally conduct a 200-response pilot human annotation study with separate 5-point Likert scales for content quality and presentation quality, providing direct validation that debiased scores correlate with content ratings while discounting presentation ratings. Baselines: FairJudge-8B, Length-Controlled AlpacaEval regression, Bias-Bounded Evaluation, raw (undebiased) judges, and a 'format normalization' baseline that strips all markdown before judging.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$500–750 (Sonnet 4.6 for experiment orchestration, automated counterfactual quality filtering, DML cross-fitting, statistical analysis, and full paper drafting)', 'estimated_gpu_cost': '$375–550 + $300–450 commercial judge API + $150–200 GPT-4o-mini + $800–1200 annotation study', 'gpu_hours': '150–220 A100-80GB hours (additional ablations: linear vs. DML vs. nonparametric, ISE comparison, α sensitivity sweeps, domain-conditional analysis, amortized predictor architectures)', 'speed_bottleneck': 'Sequential dependency chain: style counterfactual generation → content-preservation validation (including human spot-checks) → judge scoring → DML estimation; human annotation study runs in parallel but requires ~2 weeks for annotator recruitment and completion', 'timeline': '5–7 weeks'}
- **human_in_loop**: {'claude_api_cost': '$150–300 (Sonnet 4.6 at $3/$15 per MTok for prompt engineering, counterfactual quality analysis, DML specification, ablation design, and paper drafting)', 'estimated_gpu_cost': '$250–350 + $200–350 commercial judge API + $100–150 GPT-4o-mini + $800–1200 annotation study', 'gpu_hours': '100–140 A100-80GB hours', 'timeline': '9–11 weeks'}
- **manual**: {'estimated_gpu_cost': '$250–350 (A100 spot ~$2.50/hr) + $200–350 commercial judge API costs (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro) + $100–150 GPT-4o-mini content verification + $800–1200 pilot annotation study (200 responses × 3 annotators)', 'gpu_hours': '100–140 A100-80GB hours (style counterfactual generation with Qwen3-32B: 6 rewrites/response × ~2K responses ≈ 30h; content verification BERTScore/NLI: 3h; open-source judge inference: 25h; DML estimation and ablations: 5h; amortized model training: 2h; iteration buffer: 35–75h)', 'timeline': '12–14 weeks'}

## Key References

- Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking (ICLR 2025)
- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)
- FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge (arXiv 2602.06625, Feb 2026)
- Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines (arXiv 2026)
- Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization (arXiv 2026)
- RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025)
- Double/Debiased Machine Learning for Treatment and Structural Parameters (Chernozhukov et al., Econometrics Journal 2018)
- Causal Inference for Human-Language Model Collaboration (Choi et al., NAACL 2024)
- Adapting Text Embeddings for Causal Inference (Veitch, Sridhar & Blei, UAI 2020)
- Causal Effects of Linguistic Properties (Pryzant et al., NAACL 2021)
- A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents (CASSE, arXiv 2601.10809, Jan 2026)
- Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2025)
- Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (ICLR 2025)
- Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector (NeurIPS 2025)
- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2026)
- CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025)
- RubricBench: Aligning Model-Generated Rubrics with Human Standards (arXiv 2603.01562, March 2026)
- Estimating Causal Effects of Text Interventions Leveraging LLMs (Findings of AACL-IJCNLP 2025)
- Causal Effect Estimation with Latent Textual Treatments (arXiv 2026)
- How to Make Causal Inferences Using Texts (Egami et al., Science Advances 2022)

## Reviewer Evaluation

**Scores**:
  - entry_triage_x: **31.0**/5
  - exit_triage_z: **39.0**/5

## Human Review Note

## External Review — Verdict: PASS

- X (entry triage): 31.0%
- Y (terminal self-eval): 44.0%
- Z (exit triage): 39.0%
- Z interval: [33.0%, 44.0%]
- Real improvement (Z-X): +8.0 pp

### Optimization Suggestions
【优化方案】

1. **[§1 Related Work 全局] — 补充 9 篇遗漏关键文献，建立完整的因果去偏研究景观并显式差异化** — [Related Work 致命遗漏修复 + Novelty 锐化]
   原始 proposal 遗漏了与 CSD 高度相关的近期工作，审稿人极可能以"missing critical related work + overclaimed novelty"扣分。补充以下文献并逐篇建立差异化：
   - arXiv:2604.27495 (Causally Motivated Inference-Time Intervention, Apr 2026): white-box neuron 干预 → CSD 为 black-box，无需模型内部访问
   - arXiv:2512.19908 (Counterfactual Rhetorical Style, Dec 2025): 方法管线高度相似（LLM counterfactual rewrite + 统计聚合）但只量化不校正 → CSD 完成量化→校正闭环
   - arXiv:2409.17407 (Post-hoc Reward Calibration, ICLR 2025): 单维度 observational locally-weighted regression → CSD 为多维 interventional causal identification
   - arXiv:2604.13833 (CROME, Apr 2026): training-time causal data augmentation → CSD 为 post-hoc，无需重训 judge
   - arXiv:2506.16507 (Causal Rubrics, ICML 2025): causal+neutral augmentations 训练 robust RM → 白盒 training-time，CSD 为黑盒 post-hoc
   - arXiv:2507.15698 (CoLD, Jul 2025): counterfactual 因果去偏 PRM，但 training-time + 单维度(length) + white-box → CSD 三个维度均超越
   - arXiv:2508.09724 (UDA, AAAI 2026): 黑盒后处理 judge 去偏，但需多 judge 共识驱动 → CSD 在单个 judge 上工作
   - arXiv:2601.21816 (DMLRANK, Jan 2026): DML 用于 LLM ranking estimation → 共享方法论基础但目标不同，强化"DML 在 LLM 评估中正成为一个研究方向"的叙事
   - arXiv:2604.23178 (Soumik, Apr 2026): 9 种去偏策略的全面对比 → CSD 应与其 best strategy（combined budget, +11.2pp）直接对比
   这些文献构成"causal debiasing for LLM evaluation"的完整景观。CSD 精确填补 **black-box + post-hoc + multi-dimensional + score correction** 的交叉空白——每篇竞争者至少在一个维度上缺失。

2. **[§1 Motivation 第 1-2 段] — 重构核心 framing：桥接两个文献体系 + RLHF pipeline significance** — [Significance 天花板提升]
   原始 framing 是"给黑盒 judge 去偏"。优化为双层 significance 叙事：
   - **跨领域桥梁**：NLP 评估社区大量记录了 style bias 但修复方式 ad-hoc（regression、prompt engineering）；因果推断/经济计量学社区有成熟的 DML 框架但未系统应用于黑盒 LLM judge。CSD 是两者的 principled integration。
   - **RLHF pipeline 影响**：引用 Preference Leakage (ICLR 2026, arXiv:2502.01534) 论证 style bias 从 judge → preference data → reward model → policy model 的传播链。CSD 不仅修正 evaluation，还能在 preference data curation 阶段截断 style contamination 传播。在 §5 Expected Outcome 中作为 broader impact 讨论（不过度声称，因为 downstream RLHF 效果超出当前实验范围）。

3. **[§3.2 Method 核心] — 新增 dual-layer causal identification 论证，堵住两个 trivial alternative** — [Novelty 最关键防线]
   原始 proposal 仅说"DML 有 doubly-robust 性质"，未论证其在 counterfactual 设计下的增量价值。优化为显式双层论证：
   - **Trivial Alternative 1（"直接算配对差"）**：RATE (ICML 2025) 证明 imperfect counterfactuals 引入 substantial bias。CSD 的 DML nuisance function 作为 second-stage robustness 吸收残余 content leakage，提供 $\sqrt{n}$-consistent + doubly-robust 的统计保证。对比 RATE 的 double-rewrite（依赖 rewrite 偏差对称性假设，algorithmic correction）vs. CSD 的 DML（依赖半参数统计理论，statistical correction，假设更弱）。
   - **Trivial Alternative 2（"多维观测回归"）**：直接扩展 LC-AlpacaEval 到多维特征的 observational regression 无法区分 confounded style-quality association（如高质量技术文档天然需要结构化格式）。CSD 的 counterfactual intervention 通过 do-calculus 打破混杂。在实验中纳入 Multi-Reg baseline 直接展示增量。

4. **[§2 Contribution 2] — 将 legitimacy-aware correction (α) 从方法细节提升为核心概念贡献** — [Novelty 锐化]
   原始 proposal 将 α 作为 cal

_Reviewed by external pipeline (batch7), 2026-05-20_


## MVP Validation Results

- **Date**: 2026-05-20
- **Hypothesis Supported**: Yes

### Key Metrics

Formality pairwise: 69.1% formal win rate (p=0.006, n=55 consistent pairs) | Formality Likert: ATE=0.102, d=0.104, p=0.332 | H1 NLI pass: formality 88%, verbosity 65% | Direction asymmetry: 78.8% vs 54.5% | Original preference: ~12.2%

### Summary

MVP 测试了两个假设：H1（binary style counterfactuals 保内容改 style）和 H2（LLM judge 对 style 变化显示显著 ATE）。

H1 结果：Formality axis PASS（NLI≥0.90 pass rate: 8B 95%, 32B 88%）。Verbosity axis FAIL（NLI 65%，根本原因：verbosity 改变信息量与 RATE 内容保持假设冲突）。

H2 结果：Formality Likert FAIL（ATE=0.102, d=0.104, p=0.332 — 整数粒度掩盖效应）。Formality Pairwise CONDITIONAL PASS（69.1% formal win rate, p=0.006 — 双向 position-controlled，n=55 一致 pairs）。方向不对称：formal→casual 78.8% (p=0.001) vs casual→formal 54.5% (p=0.832)，original preference ~12.2%。

核心发现：(1) GPT-4o 对 formal writing 有 causal preference premium；(2) Likert 整数粒度掩盖 sub-integer style effects，pairwise 是更敏感的检测方法；(3) RATE counterfactual 方法仅适用于不改变信息量的 style axis（formality yes, verbosity no）。

### Recommendation

进入 research 阶段。单轴 formality conditional PASS + verbosity 方法边界发现。Paper framing 以 C3（Likert vs pairwise 测量洞察）为 primary contribution，扩展 3+ judges、2+ benchmarks、测试 tone/register axis。目标 EMNLP 2026 ARR。
