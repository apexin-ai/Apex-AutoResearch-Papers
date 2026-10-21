# Idea Brief: EC-HTE: From Arm-Specific Rectifiers to Full CATE Estimation with LLM-Annotated Effect Modifiers


- **Idea ID**: `idea_037`
- **Created**: 2026-05-20
- **Approved**: 2026-05-20
- **Source**: foreign:be-idea-gen-0515-5
- **Level**: solid
- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026; commitment deadline: August 2, 2026) — tight but feasible for a focused 8-page paper, AAAI 2027 (abstract deadline: July 21, 2026; full paper: July 28, 2026) — primary target with sufficient development time, ICLR 2027 (estimated submission deadline: ~September 2026, based on ICLR 2026 pattern of Sep 19-24), AISTATS 2027 (estimated submission deadline: ~October 2026, based on AISTATS 2026 pattern of Oct 2)

## Seed Topic

web_research

## Core Problem

Mozer (2026) recently proved that pooled PPI rectifiers induce irreducible bias (δ₀ − δ₁) in ATE estimation under differential LLM prediction error, and proposed arm-specific rectifiers as the fix. But applied researchers need more than corrected ATEs — they need conditional average treatment effect (CATE) estimates that reveal for whom a treatment works. When a text-derived LLM annotation (e.g., 'interview expresses economic aspiration') serves as an effect modifier in CATE estimation, the measurement error problem goes beyond arm-level correction: misclassification of the effect modifier itself distorts the conditioning variable, causing causal forest splits and DR-learner pseudo-outcomes to inherit subgroup-specific bias that no arm-level rectifier can address. How should we correct LLM measurement error when the mismeasured variable defines the heterogeneity structure, not just the treatment contrast?

## Opportunity / Why Now

Mozer (2026) closes the gap for ATE under differential prediction error by connecting PPI to the survey-sampling difference estimator and recommending arm-specific rectifiers. However, arm-specific correction assumes the subgroup definitions (treatment arms) are cleanly observed — it corrects the outcome measurement, not the covariate measurement. When researchers use LLM-annotated text variables as effect modifiers (e.g., 'tweet contains policy framing,' 'interview expresses economic aspiration'), the subgroup labels themselves are noisy, and that noise is non-random across populations (Ashwin et al., 2025 show LLM error rates vary by refugee status, gender, and education level). This means: (1) observations are assigned to wrong CATE subgroups, (2) within-subgroup outcome corrections are applied to the wrong units, and (3) the resulting heterogeneity estimates are doubly contaminated — by both outcome measurement error and effect-modifier misclassification. Causal forests (Wager & Athey, 2018) and DR-learners (Kennedy, 2023) assume clean covariates. ForestIV (Bu et al., 2023) handles measurement error in ML-generated covariates for regression but not for CATE estimation. No existing work addresses this specific intersection: correcting LLM measurement error in effect modifiers for heterogeneous causal effect estimation.

## Landscape (SOTA & Limitations)

The landscape has evolved significantly since our initial proposal. **LLM debiasing for aggregate estimands**: DSL (Egami et al., 2024, NeurIPS) and PPI (Angelopoulos et al., 2023, Science) provide unbiased population-level estimates. Audinet de Pieuchon et al. (EMNLP 2025) benchmark both, finding DSL outperforms PPI on bias but is less consistent. Mozer (March 2026, arXiv:2603.19160) proves PPI is algebraically equivalent to the survey-sampling difference estimator, shows pooled rectifiers induce irreducible ATE bias under differential prediction error, and recommends arm-specific rectifiers — but explicitly limits analysis to average treatment effects and does not address CATE or effect-modifier measurement error. **Active/adaptive annotation**: Zrnic & Candès (2024, ICML) propose active statistical inference allocating labels where model uncertainty is highest; Mehrotra et al. (March 2026) introduce perspective-driven inference with adaptive sampling for subjective annotation tasks; Active Multiple-PPI (May 2026, arXiv:2605.08429) optimizes across multiple predictors. All target aggregate or perspective-level estimands, not CATE with mismeasured effect modifiers. **Covariate measurement error in causal inference**: Wen & Yan (2025, Statistics in Medicine) address covariate balancing under measurement error; ForestIV (Bu et al., 2023, INFORMS JDS) uses random-forest-generated instrumental variables to correct ML-covariate measurement error in regression models — but not in treatment effect heterogeneity estimation. **HTE estimation**: Wager & Athey (2018) causal forests and Kennedy (2023) DR-learners assume clean covariates. Persson et al. (Feb 2026) show CATE-to-GATE aggregation introduces group bias from aggregation mechanics, not measurement error. Feldman et al. (Feb 2026) handle causal effects with latent textual treatments but assume observed covariates are clean. Jerzak et al. (2025) propose Surrogate Representation Inference improving annotation efficiency but not addressing the effect-modifier case. **The verified gap**: no paper combines LLM measurement-error correction with heterogeneous effect estimation when the mismeasured variable is an effect modifier that defines subgroup structure.

## Proposed Approach

We propose EC-HTE (Error-Corrected Heterogeneous Treatment Effects), a framework for valid CATE estimation when LLM-annotated text variables serve as effect modifiers. Our contribution goes beyond Mozer (2026)'s arm-specific rectifiers by addressing mismeasurement of the conditioning variable itself, not just the outcome.

**Stage 1 — Hierarchical subgroup-stratified error correction.** We estimate subgroup-specific misclassification matrices (for the effect-modifier annotation) from the expert-labeled sample using a hierarchical Bayesian model with Dirichlet priors. Partial pooling across subgroups addresses the reviewer-identified sample-size concern: rather than requiring each of k subgroups to independently support a 2×2 confusion matrix, information is shared via a common Dirichlet hyperprior, with the degree of pooling determined by data. We require a minimum of n_min ≈ 30 expert labels per subgroup for identifiability, with the hierarchical model borrowing strength from the full expert sample (target: 2,000 total documents, k ≤ 8 subgroups, yielding ≥ 250 per subgroup). Per-subgroup corrected pseudo-outcomes are computed via matrix-adjusted doubly-robust estimators, extending the arm-specific rectifier logic of Mozer (2026) to the effect-modifier dimension.

**Stage 2 — Honest causal forest with error-variance-adjusted inference (not modified splitting).** A key revision from our initial proposal: we do NOT modify the splitting criterion of the causal forest, which would jeopardize the honesty and asymptotic normality guarantees of Wager & Athey (2018). Instead, we preserve the standard honest causal forest architecture — splitting sample determines tree structure, estimation sample provides leaf estimates — and make two targeted modifications: (a) the estimation sample uses corrected pseudo-outcomes from Stage 1, and (b) leaf-level confidence intervals are inflated using a sandwich variance estimator that accounts for the additional uncertainty from misclassification-matrix estimation. This preserves the honesty property (split selection is independent of estimation) and asymptotic normality (the corrected pseudo-outcomes are asymptotically equivalent to true outcomes under regularity conditions), while honestly reflecting the additional uncertainty from the debiasing step. We derive conditions under which the corrected forest is consistent and asymptotically normal, showing this holds when the misclassification matrix is estimated at √n-rate (guaranteed by the Bayesian posterior under mild conditions).

**Stage 3 — Adaptive expert-annotation allocation.** Building on but distinct from Zrnic & Candès (2024) active statistical inference and Mehrotra et al. (2026) perspective-driven sampling, our allocation targets CATE-relevant quantities. Specifically, we allocate additional expert labels to subgroups where: (i) the estimated misclassification rate is highest (from pilot confusion matrices), AND (ii) the estimated CATE magnitude is largest (from a pilot causal forest on uncorrected data) — because high-CATE, high-error subgroups contribute most to the overall bias in heterogeneity estimates. This joint criterion is novel: Zrnic & Candès optimize for population-level interval width, Mehrotra et al. optimize for perspective-distribution accuracy, and we optimize for CATE estimation accuracy.

**Finite-sample bias bounds.** We derive bounds showing that the bias of the stratified correction over global correction is proportional to the product of (effect-modifier misclassification heterogeneity across subgroups) × (true CATE heterogeneity). When either term is small, global correction suffices; when both are large, stratified correction is essential. This gives practitioners a diagnostic: estimate both quantities from pilot data to decide whether EC-HTE is needed.

**Motivating example — Immigration policy messaging.** Consider a field experiment evaluating the effect of a social media messaging campaign on attitudes toward immigration policy. Researchers use an LLM to annotate tweets as containing 'economic framing' vs. 'humanitarian framing' — the hypothesized effect modifier. The LLM achieves 85% accuracy overall but makes systematic errors: it misclassifies economic framing at 25% for tweets from right-leaning sources (confusing fiscal conservatism with humanitarian concern) vs. only 10% for left-leaning sources. Under global correction, the estimated CATE for economic-framing tweets shows a modest positive campaign effect (+0.08, p=0.12). Under stratified correction, the picture changes qualitatively: a strong positive effect for economic-framing tweets from right-leaning sources (+0.18, p=0.003) and a null effect for left-leaning sources (+0.02, p=0.71). The policy implication reverses: global analysis suggests the campaign is marginally ineffective; stratified analysis reveals it is highly effective for the exact subgroup with the highest annotation noise — precisely the subgroup that global correction mishandles. We will construct a semi-synthetic benchmark from real political-science tweet corpora that operationalizes this scenario with known ground-truth CATEs.

**Validation.** Semi-synthetic benchmarks built from real political-science corpora with injected known heterogeneity, annotated by GPT-4.1 (proprietary) and Qwen 3.5 (open-source). We compare: (1) uncorrected causal forest, (2) globally-corrected causal forest (DSL/PPI with single rectifier), (3) arm-specific corrected forest (Mozer-style), (4) EC-HTE with stratified effect-modifier correction. Real-data validation on the Ashwin et al. (2025) Rohingya refugee interview dataset, where LLM annotation errors correlate with refugee status, gender, and education level.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$400-$600 (experiment orchestration, ablation sweeps, paper drafting)', 'estimated_gpu_cost': '$150-$250', 'gpu_hours': '60-90', 'speed_bottleneck': 'Expert annotation collection for validation — requires recruiting human coders for gold-standard labels on ~2,000 documents across subgroups; minimum 3-4 weeks regardless of automation. Hierarchical Bayesian model fitting adds ~1 week of compute iteration.', 'timeline': '2.5-3.5 months'}
- **human_in_loop**: {'claude_api_cost': '$150-$250 (proof verification, code review, experiment design iteration)', 'estimated_gpu_cost': '$150-$250', 'gpu_hours': '60-90', 'timeline': '3.5-4.5 months'}
- **manual**: {'estimated_gpu_cost': '$200-$350 (A100 at ~$2.50/hr)', 'gpu_hours': '80-120 (LLM annotation runs on political-science corpora + causal forest training + hierarchical Bayesian model fitting)', 'timeline': '5-6 months'}

## Key References

- PPI is the Difference Estimator: Recognizing the Survey Sampling Roots of Prediction-Powered Inference (Mozer, arXiv 2026) — CRITICAL: identifies differential prediction error bias for ATE in PPI, proposes arm-specific rectifiers; we extend to CATE with mismeasured effect modifiers
- Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models (Egami et al., NeurIPS 2023)
- Prediction-Powered Inference (Angelopoulos et al., Science 2023)
- Estimation and Inference of Heterogeneous Treatment Effects using Random Forests (Wager & Athey, JASA 2018)
- Towards Optimal Doubly Robust Estimation of Heterogeneous Causal Effects (Kennedy, Electronic Journal of Statistics 2023)
- Using Large Language Models for Qualitative Analysis can Introduce Serious Bias (Ashwin et al., Sociological Methods & Research 2025)
- Synthetic Replacements for Human Survey Data? The Perils of Large Language Models (Bisbee et al., Political Analysis 2024)
- Benchmarking Debiasing Methods for LLM-based Parameter Estimates (Audinet de Pieuchon et al., EMNLP 2025)
- Active Statistical Inference (Zrnic & Candès, ICML 2024)
- Achieving Reliable Causal Inference with Data-Mined Variables: A Random Forest Approach to the Measurement Error Problem (Bu et al., INFORMS JDS 2023)
- Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks (Mehrotra et al., arXiv 2026)
- Active Multiple-Prediction-Powered Inference (arXiv 2026)
- Detecting and Mitigating Group Bias in Heterogeneous Treatment Effects (Persson et al., arXiv 2026)
- Causal Effect Estimation with Latent Textual Treatments (Feldman et al., arXiv 2026)
- Covariate Balancing With Measurement Error (Wen & Yan, Statistics in Medicine 2025)
- Surrogate Representation Inference for Text and Image Annotations (Jerzak et al., arXiv 2025)
- Double/Debiased Machine Learning for Treatment and Structural Parameters (Chernozhukov et al., Econometrics Journal 2018)
- From Text to Treatment Effects: A Meta-Learning Approach to Handling Text-Based Confounding (CRL@NeurIPS 2024)

## Reviewer Evaluation

**Scores**:
  - entry_triage_x: **32.0**/5
  - exit_triage_z: **36.0**/5

## Human Review Note

## External Review — Verdict: PASS

- X (entry triage): 32.0%
- Y (terminal self-eval): 40.0%
- Z (exit triage): 36.0%
- Z interval: [30.0%, 42.0%]
- Real improvement (Z-X): +4.0 pp

### Optimization Suggestions
【优化方案】

**一、核心 Claim / Framing 层面（命中 Novelty + Significance）**

1. [标题 + Abstract + Introduction 第1–2段] — **将核心定位从"Mozer arm-specific rectifiers 的扩展"重构为"发现并形式化一类新的偏差机制"**。原始 proposal 的叙事重心是"arm-specific rectifiers 不够用，需要 effect-modifier-level correction"，容易被审稿人读作 incremental extension。重写后的定位是：当 LLM misclassification rate 与 true CATE 在子群间协变时，产生一种此前未被识别的 measurement-error × causal-heterogeneity confounding，且全局校正在结构上不可能解决。这是 problem-level discovery 而非 technique-level extension。 — Novelty（从"中"拉至"强"）+ Significance（问题的根本性）

2. [Introduction 新增段落，Motivation 之后] — **新增显式 proposition："Global correction can actively worsen CATE estimates"**。构造 two-subgroup 分析例子（Subgroup A: 25% misclassification + 0.5 SD CATE; Subgroup B: 5% + 0.1 SD），展示 pooled confusion matrix (~15%) 对 A 校正不足、对 B 过度校正，净效果是 globally-corrected CATE bias > uncorrected bias。这个反直觉发现（"debiasing introduces more bias"）大幅提升 surprise value。 — Novelty（审稿人 summary 可写出 crisp insight）+ Significance（揭示当前实践的系统性风险）

3. [Contributions 章节] — **将 bias bound 从 Stage 2 附属描述提升为独立核心贡献**（Contribution 2）。原始 proposal 中 bias ∝ (misclassification heterogeneity × CATE heterogeneity) 的 bound 被埋在方法描述里。重写后将其定位为 paper 的 signature result + actionable diagnostic criterion：任何研究者在做 CATE 分析前都可以用 pilot data 计算这个乘积来判断是否需要 stratified correction。强调该诊断标准具有独立于 EC-HTE 框架的 standalone value。 — Novelty（不可替代的理论贡献）+ Significance（独立可用的诊断工具）

4. [Introduction 尾段] — **新增 trivial alternative 防御**。显式论证"为什么不直接在 expert-labeled 子样本上跑 causal forest"不可行：2,000 expert labels / k subgroups → honest causal forest 进一步对半分 → 每 cell ~1,000/k 样本 → k≥4 时检测中等 heterogeneity 的 power 不足。EC-HTE 的 value proposition 是 bias-variance tradeoff 的最优组合：用全量 LLM data 获得 low-variance CATE estimate，用 expert labels 仅做 calibration。 — Novelty + Significance（预防最可能的审稿人 pushback）

**二、Related Work 层面（命中 Related Work 差异化）**

5. [Related Work] — **新增 Sui et al. (arXiv:2603.05575) PPCI 差异化讨论**。PPCI 将 PPI 扩展到 conditional functionals 使用 kernel-based localization，是审稿人最可能 flag 的"这不是已经做了吗？"威胁。明确区分：PPCI 处理 out

_Reviewed by external pipeline (batch7), 2026-05-20_


## MVP Validation Results

- **Date**: 2026-05-20
- **Hypothesis Supported**: Yes

### Key Metrics

Extreme regime, n=500, Subgroup B: EC-HTE RMSE (0.063, 0.066) vs Global (0.100, 0.093) — 37%/29% 改善; EC-HTE |bias| < 0.015 vs Global |bias| 0.055-0.070; EC-HTE coverage 97% vs Global 88-90%; "去偏反而加偏": Global |bias_z0|=0.070 vs Naive 0.009 (7.8x 恶化); Do no harm: homogeneous regime EC-HTE ≈ Global ✓

### Summary

核心假设验证：当 LLM effect-modifier 误分类率跨子群异质时，全局校正对低误差子群造成系统性伤害（bias 恶化 7.8 倍），EC-HTE 分层校正有效修复。三轮模拟（v1 CausalForest 子群分析、v2 差分估计边际验证、100 MC runs）共同确认：(1) "去偏反而加偏"机制在子群水平清晰成立；(2) EC-HTE 子群内 bias < 0.015，覆盖率 92-97%（n≥250）；(3) 方差问题指向层级贝叶斯 partial pooling 为核心必要组件。

### Recommendation

GO — 进入 research 阶段。核心 insight 验证通过且具备 surprise value（"debiasing can hurt"）。Research 第一优先级：层级贝叶斯 partial pooling 混淆矩阵估计器（解决高误差子群方差问题）。投稿目标 EMNLP 2026。
