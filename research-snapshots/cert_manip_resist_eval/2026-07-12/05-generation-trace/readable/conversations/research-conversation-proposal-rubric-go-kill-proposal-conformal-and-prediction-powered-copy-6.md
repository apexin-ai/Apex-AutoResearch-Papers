# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Conformal and Prediction-Powered 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/055a2254-e260-4571-babf-fffde7c84db5.jsonl`
- **Structured JSON:** [`973fd3164cc519926452.json`](../../sessions/97/973fd3164cc519926452.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:23:01.907Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:23:01.907Z",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders\n\n## Description\nWe propose ConformalPPITextCausal, a framework providing finite-sample coverage guarantees for treatment effects estimated using LLM-extracted text confounders. Current methods (DoubleLingo, Ma et al.) rely on asymptotic guarantees that break down when LLM extraction introduces unquantified heterogeneous noise. Our dual-track approach addresses this via: Track A (ITE intervals) — adapting modular conformal prediction (Zhang et al. 2025) to a causal two-stage pipeline where Stage 1 produces conformal prediction sets over LLM-extracted categorical confounders (with worst-case pseudo-outcome enumeration including explicit propensity score propagation, O(|C|) per unit) or low-dimensional Matryoshka embeddings (with ellipsoidal sets and convex relaxation restricted to smooth nuisance estimators), and Stage 2 constructs doubly robust treatment effect intervals with FWER-controlled coverage tighter than Bonferroni; Track B (ATE intervals) — extending conformal prediction-powered inference (Csillag et al. 2025) to the causal setting, where a small expert-labeled and large LLM-imputed dataset yield valid confidence intervals via Z-estimation with conformal set-predictors. Cross-conformal calibration (Gasparin & Ramdas, ICML 2025) reduces the three-way data split to two-way, improving sample efficiency for labeled-data-scarce settings. A pilot conservatism analysis shows practical viability: for K=5 confounder categories, interval widening is ~60% with conformal set size |C|=2 (good LLM) and ~100% with |C|=3 (decent LLM), driven primarily by propensity score variation across conformal set members. The method is practically useful when the LLM achieves small conformal sets and correctly signals insufficient information otherwise. We differentiate from Barnatchez et al. (2604.03772), who handle missing confounders at deployment via semiparametric debiasing — a complementary but distinct setting from our noisy-extraction framework. The genuine theoretical contribution is proving the modular residual decomposition holds under causal exchangeability conditions specific to doubly robust pseudo-outcomes with explicit propensity propagation. Experiments on semi-synthetic MIMIC-IV clinical notes, social media data, and synthetic benchmarks demonstrate maintained nominal coverage where bootstrap alternatives undercover, with a dedicated conservatism experiment varying |C|/K to validate the pilot analysis.\n\n## Core Problem\nCausal inference from observational text data (clinical notes, social media, policy documents) requires adjusting for confounders embedded in unstructured text. Modern LLMs can extract these confounders, but extraction is imperfect — introducing measurement error that invalidates standard causal estimators' asymptotic guarantees. No existing framework provides finite-sample coverage guarantees for treatment effect estimates when confounders are extracted by a fallible LLM. Naive approaches (plugging in LLM point predictions as if they were ground truth) can produce arbitrarily biased causal conclusions when extraction noise is heterogeneous across subpopulations.\n\n## Opportunity\nThree independent research threads have matured to the point where they can be unified into a principled solution: (1) modular conformal prediction for sequential pipelines (Zhang et al. 2025, arXiv 2510.04406) provides a residual decomposition framework that controls family-wise error across pipeline stages without resorting to loose Bonferroni corrections; (2) prediction-powered inference extended through conformal prediction (Csillag et al. 2025, arXiv 2510.16166) yields valid population-level confidence intervals when a prediction model (here, the LLM) imputes covariates on a large unlabeled set alongside a small human-labeled set; and (3) conformal meta-learners for individual treatment effects (Alaa et al. NeurIPS 2023) provide conformal intervals for heterogeneous effects but assume perfectly observed confounders. Additionally, Matryoshka embedding models (Qwen3-Embedding-8B) now support flexible dimensionality from 32 to 4096, making conformal prediction over embedding spaces tractable at reduced dimensions. Recent work on conformal prediction under confounding — including Barnatchez et al. (arXiv 2604.03772) on runtime confounding (missing confounders at deployment) and Vovk & Wang (arXiv 2603.11134) on conformal e-prediction — demonstrates growing interest but targets distinct problem settings from ours (noisy extraction vs. missing variables, and e-values for prediction vs. p-values for treatment effects). By bridging these threads, we can deliver both individual-level (ITE) and population-level (ATE) treatment effect intervals that honestly account for LLM extraction uncertainty — a capability no current method provides.\n\n## Landscape\nThe intersection of conformal prediction and causal inference has seen rapid growth (Systematic Review, arXiv 2509.21660, covering 11 key papers), but existing conformal ITE methods (Lei & Candès JRSS-B 2021; Alaa et al. NeurIPS 2023; KDD 2024 wTCP-DR) assume confounders are observed without error. The conformal prediction for NLP survey (Campos et al. TACL 2024) covers classification, QA, and generation quality but not downstream causal validity. Prediction-powered inference (Angelopoulos et al. Science 2023) and its causal extensions (arXiv 2502.06343; Kato arXiv 2511.08303 NeurIPS 2025) address the labeled/unlabeled split for treatment effects but do not incorporate conformal sets for the imputed covariates. Zhang et al. (2025) handle sequential model pipelines with modular conformal guarantees but do not treat the causal setting or weighted exchangeability. DoubleLingo (NAACL 2024) and Ma et al. (NeurIPS 2025) use LLMs within doubly robust causal estimators for text data but provide only asymptotic guarantees with no finite-sample uncertainty quantification for LLM extraction noise. Multi-variable conformal prediction (Lützow et al. arXiv 2605.12341, 2026) and ellipsoidal conformal sets (Xu et al. ICML 2024) now provide tractable geometric tools for moderate-dimensional conformal regions.\n\nTwo recent works merit explicit differentiation: Barnatchez et al. (arXiv 2604.03772, April 2026) address conformal prediction for counterfactual outcomes under 'runtime confounding' — where confounders measured in training are entirely MISSING at deployment. Their semiparametric debiasing approach marginalizes over unobserved confounders via multiply-robust influence functions, assuming Y(a)⊥S|V (systematic differences explained by the observed subset V). Our setting is fundamentally different: all confounders are present in the text and extracted by the LLM, but with NOISE — the confounders are measured with error, not missing entirely. Their debiasing marginalizes over missing variables; our conformal sets quantify extraction uncertainty over observed-but-noisy variables. Vovk & Wang (arXiv 2603.11134, March 2026) extend conformal e-prediction to handle observed confounding between X and Y using e-values (nonnegative random variables with expectation ≤ 1) rather than p-values. While e-values provide attractive anytime-valid guarantees under optional stopping, their framework targets prediction of Y given X under confounding, not treatment effect estimation. Our framework uses standard conformal prediction sets combined with PPI, targeting ITE/ATE estimation — a complementary but distinct goal. The e-value approach could be an interesting alternative foundation for future work.\n\nThe gap we fill is the integration of modular conformal prediction and conformal PPI into a unified framework for the two-stage pipeline of LLM confounder extraction followed by causal effect estimation, with proven finite-sample validity under noisy (not missing) confounder extraction.\n\n## Approach\nWe propose a dual-track framework, ConformalPPITextCausal, for valid causal inference when text confounders are extracted by an LLM.\n\n**Data Splitting and Sample Efficiency.** The baseline design uses a three-way data split: (S1) training data for fine-tuning the LLM extraction model and fitting nuisance functions (propensity score, outcome regression), (S2) calibration data for Stage 1 conformal sets on the extracted confounders, and (S3) calibration data for Stage 2 conformal intervals on treatment effects. To address sample efficiency — critical for clinical text datasets like MIMIC-IV where expert-labeled samples are expensive — we propose two improvements: (i) K-fold cross-fitting for nuisance function estimation within S1, following Chernozhukov et al. (2018) DML, which uses all training data for both estimation and evaluation; (ii) cross-conformal calibration for Stage 1, following Gasparin & Ramdas (ICML 2025, arXiv 2503.01495), which achieves coverage ≥ 1−2α₁ using K-fold rotation rather than a dedicated hold-out set, effectively merging S2 into S1 and reducing the three-way split to a two-way split (train+Stage1-calibrate vs. Stage2-calibrate). The coverage cost (1−2α₁ vs. 1−α₁) is manageable by setting α₁ conservatively (e.g., α₁=0.025 for effective 95% Stage 1 coverage). We discuss minimum sample size requirements: Stage 2 calibration requires n₃ ≥ ⌈1/α₂⌉ ≈ 100-200 for reliable conformal quantiles at α₂=0.05, and we recommend n_total ≥ 500 for the full pipeline, with n₃ ≥ 150 reserved for Stage 2. For very small labeled datasets (n < 300), Track B (PPI) is preferred as it leverages large unlabeled corpora.\n\n**Track A — Modular Conformal ITE Intervals.** We adapt the residual decomposition of Zhang et al. (2025), where the total prediction residual R decomposes as R ≤ ΔR₁ + R₂, with Stage 1 = LLM confounder extraction and Stage 2 = doubly robust pseudo-outcome estimation.\n\nIn the primary setting, the LLM extracts CATEGORICAL confounders (e.g., disease severity ∈ {mild, moderate, severe}, smoking status ∈ {never, former, current}) via prompted classification. Conformal prediction sets for classification are natural finite sets with guaranteed coverage.\n\n**Explicit Propensity Score Propagation.** The worst-case pseudo-outcome over the conformal set is computed by full enumeration with explicit propagation through BOTH the outcome regression AND the propensity score. For each possible confounder value c ∈ C(x), the DR pseudo-outcome is:\n\nφ̂(c; Yᵢ, Aᵢ) = [μ̂₁(c) − μ̂₀(c)] + Aᵢ·(Yᵢ − μ̂₁(c))/ê(c) − (1−Aᵢ)·(Yᵢ − μ̂₀(c))/(1−ê(c))\n\nCritically, different confounder values c yield different propensity scores ê(c), which enter the augmentation term as 1/ê(c) (for treated) or 1/(1−ê(c)) (for control). This propensity variation is a distinct and compounding source of uncertainty beyond outcome regression variation. The augmentation term amplifies when propensity scores are extreme: a confounder value with ê(c)=0.1 magnifies residuals 10×. The worst-case interval is [min_c φ̂(c), max_c φ̂(c)] with complexity O(|C|) per unit. We recommend propensity score trimming (truncating ê(c) to [0.05, 0.95]) to prevent a single extreme-propensity confounder value from dominating the interval.\n\n**Pilot Conservatism Analysis.** We provide a back-of-envelope quantification of interval widening due to worst-case enumeration. Consider a clinical setting with K=5 severity categories {none, mild, moderate, severe, critical} and realistic nuisance function values:\n\n| Category | μ̂₁(c) | μ̂₀(c) | ê(c) | CATE |\n|----------|--------|--------|-------|------|\n| none     | 0.40   | 0.30   | 0.50  | 0.10 |\n| mild     | 0.50   | 0.35   | 0.45  | 0.15 |\n| moderate | 0.60   | 0.40   | 0.40  | 0.20 |\n| severe   | 0.72   | 0.45   | 0.35  | 0.27 |\n| critical | 0.85   | 0.50   | 0.25  | 0.35 |\n\nFor a treated patient with Y=0.65 and true severity=moderate, the DR pseudo-outcomes across categories are: φ̂(none)=0.60, φ̂(mild)=0.48, φ̂(moderate)=0.33, φ̂(severe)=0.07, φ̂(critical)=−0.45. The variation is dominated by the augmentation term (Y−μ̂₁(c))/ê(c), where propensity changes from 0.50 to 0.25 amplify residuals 2×. The extraction uncertainty width (Δφ = max−min over C(x)) for different conformal set sizes:\n\n- |C|=1 (excellent LLM, singleton): Δφ=0, no widening vs. oracle.\n- |C|=2 (good LLM, e.g., {moderate, severe}): Δφ≈0.26, widening ≈ 60% over oracle CI width of ~0.40.\n- |C|=3 (decent LLM, e.g., {mild, moderate, severe}): Δφ≈0.41, widening ≈ 100% over oracle.\n- |C|=4+ (poor LLM): Δφ>1.0, intervals become vacuously wide — correctly reflecting that the LLM provides insufficient information for credible causal conclusions.\n\nThe general widening ratio is approximately W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle, where Δ_CATE is the CATE variation across the conformal set, |r| is the outcome residual magnitude, and Δ(1/ê) is the inverse propensity variation. Key practical determinants: (a) conformal set size |C|/K — the LLM quality directly controls conservatism; (b) propensity score stability across confounder categories — good overlap reduces widening; (c) outcome residual magnitude — well-fitted outcome models reduce augmentation-driven widening. The method is practically useful (W < 2) when the LLM achieves conformal set size |C| ≤ 2 for K=5 categories, and correctly signals 'insufficient information' otherwise.\n\nFor the secondary continuous track, we use Qwen3-Embedding-8B with Matryoshka dimensionality reduction to 128–256 dimensions, construct ellipsoidal conformal sets (Xu et al. ICML 2024; Lützow et al. 2026), and bound worst-case pseudo-outcomes via convex relaxation: local Lipschitz continuity of nuisance functions plus first-order Taylor expansion over the ellipsoid, following the decision-theoretic framework of Wang & Dobriban (arXiv 2602.00989, 2026). **Important restriction**: the convex relaxation via Lipschitz continuity and Taylor expansion requires smooth nuisance estimators. This is compatible with neural network outcome models (e.g., TARNet, DragonNet) and kernel methods, but NOT with tree-based models (gradient-boosted trees, random forests) that are piecewise constant with jump discontinuities. We therefore restrict the continuous embedding track to smooth nuisance estimators. Note that the categorical track (primary) works with ANY nuisance estimator, including tree-based methods, since worst-case computation is by direct enumeration without smoothness assumptions. The modular framework's FWER control across both stages yields provably tighter intervals than naive Bonferroni.\n\n**Track B — Conformal PPI for ATE Intervals.** We apply the conformal PPI framework of Csillag et al. (2025) to estimate average treatment effects. The LLM serves as the prediction model in the PPI sense: a small human-labeled dataset has expert-annotated confounders, and a large dataset has LLM-extracted confounders. The conformal set-predictor from Stage 1 replaces point imputation, yielding valid ATE confidence intervals via Z-estimation: E[inf φ(C(X))] − M·Err(C) ≤ ATE ≤ E[sup φ(C(X))] + M·Err(C), where M is the bounded range of the influence function and Err(C) is the conformal miscoverage rate. This extends PPI causal inference (arXiv 2502.06343) by using conformal rather than point imputation, providing finite-sample validity without distributional assumptions on the LLM. Track B is especially suited to small-labeled-data settings (MIMIC-IV) because it leverages large unlabeled corpora.\n\nWe evaluate on three benchmarks: (1) semi-synthetic MIMIC-IV clinical notes (treatment escalation effect on ICU outcomes, disease severity as text confounder), (2) semi-synthetic social media data (content moderation effect on engagement, toxicity level as confounder), and (3) fully synthetic data with known ground-truth for calibration validation. Key metrics: empirical coverage at 90%/95% nominal levels, interval width relative to oracle (perfectly observed confounders) and bootstrap baselines, widening ratio W as a function of conformal set size and propensity overlap, and sensitivity to LLM extraction quality via deliberately degraded models. We include a dedicated conservatism experiment varying |C|/K from 0.2 to 0.8 to empirically validate the pilot analysis above.\n\nWe are transparent that worst-case reasoning over conformal sets introduces conservatism relative to oracle methods. The honest framing: our intervals maintain nominal coverage where bootstrap intervals undercover due to LLM extraction noise, with comparable width when LLM quality is high (|C|=1-2). The conservatism correctly reflects true uncertainty in the LLM-as-measurement-instrument setting, and the pilot analysis above shows it is quantifiably bounded for reasonable LLM quality.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '200-300', 'timeline': '10 weeks (targeting AAAI 2027 July 28 deadline)', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'breakdown': 'Weeks 1-2: Formalize theoretical framework (modular decomposition under weighted exchangeability, conformal PPI ATE estimator, cross-conformal Stage 1 calibration). Weeks 3-4: Implement cross-fitted pipeline, categorical conformal extraction, worst-case enumeration with explicit propensity propagation. Weeks 5-6: Implement continuous embedding track (Matryoshka 128-256d, ellipsoidal sets, convex relaxation with smooth nuisance estimators) and PPI ATE track. Weeks 7-8: Experiments on MIMIC-IV, social media, synthetic benchmarks including conservatism analysis. Week 9: Ablations (LLM quality sensitivity via |C|/K sweep, propensity overlap analysis, embedding dimension, calibration set size, cross-conformal vs. split comparison). Week 10: Paper writing and proof polishing.'}, 'human_in_loop': {'gpu_hours': '200-300', 'timeline': '8 weeks', 'claude_api_cost': '$100-150', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'notes': 'AI assists with literature integration, boilerplate code, proof sketch verification. Human focuses on theoretical contributions (weighted exchangeability conditions, tight bounds for DR pseudo-outcomes, propensity propagation analysis) and experimental design. Requires ~5 hours domain expert time for confounder annotation guidelines.'}, 'auto_research': {'gpu_hours': '250-350', 'timeline': '5-6 weeks', 'claude_api_cost': '$250-350', 'estimated_gpu_cost': '$375-525 (A100 at ~$1.50/hr)', 'speed_bottleneck': 'Theoretical proof verification requires human mathematician; three-way split calibration across multiple seeds requires sequential experiment iterations; domain expert annotation for MIMIC-IV confounder labels cannot be automated'}}\n\n## Inspired By\nGap: Existing conformal causal methods assume error-free confounders; existing LLM conformal methods ignore causal settings; existing text-based causal methods provide only asymptotic guarantees; Barnatchez et al. handle missing confounders but not noisy extraction; Vovk & Wang handle confounding in prediction but not treatment effects. Pattern: Three converging literatures (modular CP, conformal PPI, conformal causal inference) that have not been connected. Key enablers: Zhang et al. (arXiv 2510.04406) modular residual decomposition framework; Csillag et al. (arXiv 2510.16166) conformal set-predictor for PPI; Alaa et al. (NeurIPS 2023) conformal meta-learners for ITE; Barber et al. (Annals of Statistics 2023) weighted exchangeability beyond standard CP assumptions.\n\n## Target Venues\n- AAAI 2027 (Primary — abstract July 21, full paper July 28, 2026; ~10 weeks from today)\n- ARR August 2026 cycle (Secondary — submission August 3, 2026) → EACL 2027 (commitment October 11, 2026)\n- AISTATS 2027 (Stretch — estimated deadline ~October 2026, not yet announced)\n\n## Key References\n- Zhang et al. 'Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition' (arXiv 2510.04406, 2025)\n- Csillag et al. 'Extending Prediction-Powered Inference through Conformal Prediction' (arXiv 2510.16166, 2025)\n- Angelopoulos et al. 'Prediction-Powered Inference' (Science, 2023)\n- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025)\n- Kato 'Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression' (arXiv 2511.08303, NeurIPS 2025)\n- Barber et al. 'Conformal prediction beyond exchangeability' (Annals of Statistics, 2023)\n- Alaa et al. 'Conformal Meta-learners for Predictive Inference of Individual Treatment Effects' (NeurIPS 2023)\n- Wang & Dobriban 'Optimal Decision-Making Based on Prediction Sets' (arXiv 2602.00989, 2026)\n- Lützow et al. 'Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting' (arXiv 2605.12341, 2026)\n- Xu et al. 'Conformal prediction for multi-dimensional time series by ellipsoidal sets' (ICML 2024)\n- Campos et al. 'Conformal Prediction for Natural Language Processing: A Survey' (TACL, 2024)\n- Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation (arXiv 2509.21660, 2025)\n- Lei & Candès 'Conformal Inference of Counterfactuals and Individual Treatment Effects' (JRSS-B, 2021)\n- DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)\n- Ma et al. 'LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding' (NeurIPS 2025)\n- Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)\n- Veitch et al. 'Adapting Text Embeddings for Causal Inference' (UAI 2020)\n- Barnatchez et al. 'Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding' (arXiv 2604.03772, 2026)\n- Vovk & Wang 'Conformal e-prediction in the presence of confounding' (arXiv 2603.11134, 2026)\n- Gasparin & Ramdas 'Improving the statistical efficiency of cross-conformal prediction' (arXiv 2503.01495, ICML 2025)\n- Chernozhukov et al. 'Double/debiased machine learning for treatment and structural parameters' (Econometrics Journal, 2018)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:23:01.925Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:23:01.925Z",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-20T03:23:02.417Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders

## Description
We propose ConformalPPITextCausal, a framework providing finite-sample coverage guarantees for treatment effects estimated using LLM-extracted text confounders. Current methods (DoubleLingo, Ma et al.) rely on asymptotic guarantees that break down when LLM extraction introduces unquantified heterogeneous noise. Our dual-track approach addresses this via: Track A (ITE intervals) — adapting modular conformal prediction (Zhang et al. 2025) to a causal two-stage pipeline where Stage 1 produces conformal prediction sets over LLM-extracted categorical confounders (with worst-case pseudo-outcome enumeration including explicit propensity score propagation, O(|C|) per unit) or low-dimensional Matryoshka embeddings (with ellipsoidal sets and convex relaxation restricted to smooth nuisance estimators), and Stage 2 constructs doubly robust treatment effect intervals with FWER-controlled coverage tighter than Bonferroni; Track B (ATE intervals) — extending conformal prediction-powered inference (Csillag et al. 2025) to the causal setting, where a small expert-labeled and large LLM-imputed dataset yield valid confidence intervals via Z-estimation with conformal set-predictors. Cross-conformal calibration (Gasparin & Ramdas, ICML 2025) reduces the three-way data split to two-way, improving sample efficiency for labeled-data-scarce settings. A pilot conservatism analysis shows practical viability: for K=5 confounder categories, interval widening is ~60% with conformal set size |C|=2 (good LLM) and ~100% with |C|=3 (decent LLM), driven primarily by propensity score variation across conformal set members. The method is practically useful when the LLM achieves small conformal sets and correctly signals insufficient information otherwise. We differentiate from Barnatchez et al. (2604.03772), who handle missing confounders at deployment via semiparametric debiasing — a complementary but distinct setting from our noisy-extraction framework. The genuine theoretical contribution is proving the modular residual decomposition holds under causal exchangeability conditions specific to doubly robust pseudo-outcomes with explicit propensity propagation. Experiments on semi-synthetic MIMIC-IV clinical notes, social media data, and synthetic benchmarks demonstrate maintained nominal coverage where bootstrap alternatives undercover, with a dedicated conservatism experiment varying |C|/K to validate the pilot analysis.

## Core Problem
Causal inference from observational text data (clinical notes, social media, policy documents) requires adjusting for confounders embedded in unstructured text. Modern LLMs can extract these confounders, but extraction is imperfect — introducing measurement error that invalidates standard causal estimators' asymptotic guarantees. No existing framework provides finite-sample coverage guarantees for treatment effect estimates when confounders are extracted by a fallible LLM. Naive approaches (plugging in LLM point predictions as if they were ground truth) can produce arbitrarily biased causal conclusions when extraction noise is heterogeneous across subpopulations.

## Opportunity
Three independent research threads have matured to the point where they can be unified into a principled solution: (1) modular conformal prediction for sequential pipelines (Zhang et al. 2025, arXiv 2510.04406) provides a residual decomposition framework that controls family-wise error across pipeline stages without resorting to loose Bonferroni corrections; (2) prediction-powered inference extended through conformal prediction (Csillag et al. 2025, arXiv 2510.16166) yields valid population-level confidence intervals when a prediction model (here, the LLM) imputes covariates on a large unlabeled set alongside a small human-labeled set; and (3) conformal meta-learners for individual treatment effects (Alaa et al. NeurIPS 2023) provide conformal intervals for heterogeneous effects but assume perfectly observed confounders. Additionally, Matryoshka embedding models (Qwen3-Embedding-8B) now support flexible dimensionality from 32 to 4096, making conformal prediction over embedding spaces tractable at reduced dimensions. Recent work on conformal prediction under confounding — including Barnatchez et al. (arXiv 2604.03772) on runtime confounding (missing confounders at deployment) and Vovk & Wang (arXiv 2603.11134) on conformal e-prediction — demonstrates growing interest but targets distinct problem settings from ours (noisy extraction vs. missing variables, and e-values for prediction vs. p-values for treatment effects). By bridging these threads, we can deliver both individual-level (ITE) and population-level (ATE) treatment effect intervals that honestly account for LLM extraction uncertainty — a capability no current method provides.

## Landscape
The intersection of conformal prediction and causal inference has seen rapid growth (Systematic Review, arXiv 2509.21660, covering 11 key papers), but existing conformal ITE methods (Lei & Candès JRSS-B 2021; Alaa et al. NeurIPS 2023; KDD 2024 wTCP-DR) assume confounders are observed without error. The conformal prediction for NLP survey (Campos et al. TACL 2024) covers classification, QA, and generation quality but not downstream causal validity. Prediction-powered inference (Angelopoulos et al. Science 2023) and its causal extensions (arXiv 2502.06343; Kato arXiv 2511.08303 NeurIPS 2025) address the labeled/unlabeled split for treatment effects but do not incorporate conformal sets for the imputed covariates. Zhang et al. (2025) handle sequential model pipelines with modular conformal guarantees but do not treat the causal setting or weighted exchangeability. DoubleLingo (NAACL 2024) and Ma et al. (NeurIPS 2025) use LLMs within doubly robust causal estimators for text data but provide only asymptotic guarantees with no finite-sample uncertainty quantification for LLM extraction noise. Multi-variable conformal prediction (Lützow et al. arXiv 2605.12341, 2026) and ellipsoidal conformal sets (Xu et al. ICML 2024) now provide tractable geometric tools for moderate-dimensional conformal regions.

Two recent works merit explicit differentiation: Barnatchez et al. (arXiv 2604.03772, April 2026) address conformal prediction for counterfactual outcomes under 'runtime confounding' — where confounders measured in training are entirely MISSING at deployment. Their semiparametric debiasing approach marginalizes over unobserved confounders via multiply-robust influence functions, assuming Y(a)⊥S|V (systematic differences explained by the observed subset V). Our setting is fundamentally different: all confounders are present in the text and extracted by the LLM, but with NOISE — the confounders are measured with error, not missing entirely. Their debiasing marginalizes over missing variables; our conformal sets quantify extraction uncertainty over observed-but-noisy variables. Vovk & Wang (arXiv 2603.11134, March 2026) extend conformal e-prediction to handle observed confounding between X and Y using e-values (nonnegative random variables with expectation ≤ 1) rather than p-values. While e-values provide attractive anytime-valid guarantees under optional stopping, their framework targets prediction of Y given X under confounding, not treatment effect estimation. Our framework uses standard conformal prediction sets combined with PPI, targeting ITE/ATE estimation — a complementary but distinct goal. The e-value approach could be an interesting alternative foundation for future work.

The gap we fill is the integration of modular conformal prediction and conformal PPI into a unified framework for the two-stage pipeline of LLM confounder extraction followed by causal effect estimation, with proven finite-sample validity under noisy (not missing) confounder extraction.

## Approach
We propose a dual-track framework, ConformalPPITextCausal, for valid causal inference when text confounders are extracted by an LLM.

**Data Splitting and Sample Efficiency.** The baseline design uses a three-way data split: (S1) training data for fine-tuning the LLM extraction model and fitting nuisance functions (propensity score, outcome regression), (S2) calibration data for Stage 1 conformal sets on the extracted confounders, and (S3) calibration data for Stage 2 conformal intervals on treatment effects. To address sample efficiency — critical for clinical text datasets like MIMIC-IV where expert-labeled samples are expensive — we propose two improvements: (i) K-fold cross-fitting for nuisance function estimation within S1, following Chernozhukov et al. (2018) DML, which uses all training data for both estimation and evaluation; (ii) cross-conformal calibration for Stage 1, following Gasparin & Ramdas (ICML 2025, arXiv 2503.01495), which achieves coverage ≥ 1−2α₁ using K-fold rotation rather than a dedicated hold-out set, effectively merging S2 into S1 and reducing the three-way split to a two-way split (train+Stage1-calibrate vs. Stage2-calibrate). The coverage cost (1−2α₁ vs. 1−α₁) is manageable by setting α₁ conservatively (e.g., α₁=0.025 for effective 95% Stage 1 coverage). We discuss minimum sample size requirements: Stage 2 calibration requires n₃ ≥ ⌈1/α₂⌉ ≈ 100-200 for reliable conformal quantiles at α₂=0.05, and we recommend n_total ≥ 500 for the full pipeline, with n₃ ≥ 150 reserved for Stage 2. For very small labeled datasets (n < 300), Track B (PPI) is preferred as it leverages large unlabeled corpora.

**Track A — Modular Conformal ITE Intervals.** We adapt the residual decomposition of Zhang et al. (2025), where the total prediction residual R decomposes as R ≤ ΔR₁ + R₂, with Stage 1 = LLM confounder extraction and Stage 2 = doubly robust pseudo-outcome estimation.

In the primary setting, the LLM extracts CATEGORICAL confounders (e.g., disease severity ∈ {mild, moderate, severe}, smoking status ∈ {never, former, current}) via prompted classification. Conformal prediction sets for classification are natural finite sets with guaranteed coverage.

**Explicit Propensity Score Propagation.** The worst-case pseudo-outcome over the conformal set is computed by full enumeration with explicit propagation through BOTH the outcome regression AND the propensity score. For each possible confounder value c ∈ C(x), the DR pseudo-outcome is:

φ̂(c; Yᵢ, Aᵢ) = [μ̂₁(c) − μ̂₀(c)] + Aᵢ·(Yᵢ − μ̂₁(c))/ê(c) − (1−Aᵢ)·(Yᵢ − μ̂₀(c))/(1−ê(c))

Critically, different confounder values c yield different propensity scores ê(c), which enter the augmentation term as 1/ê(c) (for treated) or 1/(1−ê(c)) (for control). This propensity variation is a distinct and compounding source of uncertainty beyond outcome regression variation. The augmentation term amplifies when propensity scores are extreme: a confounder value with ê(c)=0.1 magnifies residuals 10×. The worst-case interval is [min_c φ̂(c), max_c φ̂(c)] with complexity O(|C|) per unit. We recommend propensity score trimming (truncating ê(c) to [0.05, 0.95]) to prevent a single extreme-propensity confounder value from dominating the interval.

**Pilot Conservatism Analysis.** We provide a back-of-envelope quantification of interval widening due to worst-case enumeration. Consider a clinical setting with K=5 severity categories {none, mild, moderate, severe, critical} and realistic nuisance function values:

| Category | μ̂₁(c) | μ̂₀(c) | ê(c) | CATE |
|----------|--------|--------|-------|------|
| none     | 0.40   | 0.30   | 0.50  | 0.10 |
| mild     | 0.50   | 0.35   | 0.45  | 0.15 |
| moderate | 0.60   | 0.40   | 0.40  | 0.20 |
| severe   | 0.72   | 0.45   | 0.35  | 0.27 |
| critical | 0.85   | 0.50   | 0.25  | 0.35 |

For a treated patient with Y=0.65 and true severity=moderate, the DR pseudo-outcomes across categories are: φ̂(none)=0.60, φ̂(mild)=0.48, φ̂(moderate)=0.33, φ̂(severe)=0.07, φ̂(critical)=−0.45. The variation is dominated by the augmentation term (Y−μ̂₁(c))/ê(c), where propensity changes from 0.50 to 0.25 amplify residuals 2×. The extraction uncertainty width (Δφ = max−min over C(x)) for different conformal set sizes:

- |C|=1 (excellent LLM, singleton): Δφ=0, no widening vs. oracle.
- |C|=2 (good LLM, e.g., {moderate, severe}): Δφ≈0.26, widening ≈ 60% over oracle CI width of ~0.40.
- |C|=3 (decent LLM, e.g., {mild, moderate, severe}): Δφ≈0.41, widening ≈ 100% over oracle.
- |C|=4+ (poor LLM): Δφ>1.0, intervals become vacuously wide — correctly reflecting that the LLM provides insufficient information for credible causal conclusions.

The general widening ratio is approximately W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle, where Δ_CATE is the CATE variation across the conformal set, |r| is the outcome residual magnitude, and Δ(1/ê) is the inverse propensity variation. Key practical determinants: (a) conformal set size |C|/K — the LLM quality directly controls conservatism; (b) propensity score stability across confounder categories — good overlap reduces widening; (c) outcome residual magnitude — well-fitted outcome models reduce augmentation-driven widening. The method is practically useful (W < 2) when the LLM achieves conformal set size |C| ≤ 2 for K=5 categories, and correctly signals 'insufficient information' otherwise.

For the secondary continuous track, we use Qwen3-Embedding-8B with Matryoshka dimensionality reduction to 128–256 dimensions, construct ellipsoidal conformal sets (Xu et al. ICML 2024; Lützow et al. 2026), and bound worst-case pseudo-outcomes via convex relaxation: local Lipschitz continuity of nuisance functions plus first-order Taylor expansion over the ellipsoid, following the decision-theoretic framework of Wang & Dobriban (arXiv 2602.00989, 2026). **Important restriction**: the convex relaxation via Lipschitz continuity and Taylor expansion requires smooth nuisance estimators. This is compatible with neural network outcome models (e.g., TARNet, DragonNet) and kernel methods, but NOT with tree-based models (gradient-boosted trees, random forests) that are piecewise constant with jump discontinuities. We therefore restrict the continuous embedding track to smooth nuisance estimators. Note that the categorical track (primary) works with ANY nuisance estimator, including tree-based methods, since worst-case computation is by direct enumeration without smoothness assumptions. The modular framework's FWER control across both stages yields provably tighter intervals than naive Bonferroni.

**Track B — Conformal PPI for ATE Intervals.** We apply the conformal PPI framework of Csillag et al. (2025) to estimate average treatment effects. The LLM serves as the prediction model in the PPI sense: a small human-labeled dataset has expert-annotated confounders, and a large dataset has LLM-extracted confounders. The conformal set-predictor from Stage 1 replaces point imputation, yielding valid ATE confidence intervals via Z-estimation: E[inf φ(C(X))] − M·Err(C) ≤ ATE ≤ E[sup φ(C(X))] + M·Err(C), where M is the bounded range of the influence function and Err(C) is the conformal miscoverage rate. This extends PPI causal inference (arXiv 2502.06343) by using conformal rather than point imputation, providing finite-sample validity without distributional assumptions on the LLM. Track B is especially suited to small-labeled-data settings (MIMIC-IV) because it leverages large unlabeled corpora.

We evaluate on three benchmarks: (1) semi-synthetic MIMIC-IV clinical notes (treatment escalation effect on ICU outcomes, disease severity as text confounder), (2) semi-synthetic social media data (content moderation effect on engagement, toxicity level as confounder), and (3) fully synthetic data with known ground-truth for calibration validation. Key metrics: empirical coverage at 90%/95% nominal levels, interval width relative to oracle (perfectly observed confounders) and bootstrap baselines, widening ratio W as a function of conformal set size and propensity overlap, and sensitivity to LLM extraction quality via deliberately degraded models. We include a dedicated conservatism experiment varying |C|/K from 0.2 to 0.8 to empirically validate the pilot analysis above.

We are transparent that worst-case reasoning over conformal sets introduces conservatism relative to oracle methods. The honest framing: our intervals maintain nominal coverage where bootstrap intervals undercover due to LLM extraction noise, with comparable width when LLM quality is high (|C|=1-2). The conservatism correctly reflects true uncertainty in the LLM-as-measurement-instrument setting, and the pilot analysis above shows it is quantifiably bounded for reasonable LLM quality.

## Resource Estimate
{'manual': {'gpu_hours': '200-300', 'timeline': '10 weeks (targeting AAAI 2027 July 28 deadline)', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'breakdown': 'Weeks 1-2: Formalize theoretical framework (modular decomposition under weighted exchangeability, conformal PPI ATE estimator, cross-conformal Stage 1 calibration). Weeks 3-4: Implement cross-fitted pipeline, categorical conformal extraction, worst-case enumeration with explicit propensity propagation. Weeks 5-6: Implement continuous embedding track (Matryoshka 128-256d, ellipsoidal sets, convex relaxation with smooth nuisance estimators) and PPI ATE track. Weeks 7-8: Experiments on MIMIC-IV, social media, synthetic benchmarks including conservatism analysis. Week 9: Ablations (LLM quality sensitivity via |C|/K sweep, propensity overlap analysis, embedding dimension, calibration set size, cross-conformal vs. split comparison). Week 10: Paper writing and proof polishing.'}, 'human_in_loop': {'gpu_hours': '200-300', 'timeline': '8 weeks', 'claude_api_cost': '$100-150', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'notes': 'AI assists with literature integration, boilerplate code, proof sketch verification. Human focuses on theoretical contributions (weighted exchangeability conditions, tight bounds for DR pseudo-outcomes, propensity propagation analysis) and experimental design. Requires ~5 hours domain expert time for confounder annotation guidelines.'}, 'auto_research': {'gpu_hours': '250-350', 'timeline': '5-6 weeks', 'claude_api_cost': '$250-350', 'estimated_gpu_cost': '$375-525 (A100 at ~$1.50/hr)', 'speed_bottleneck': 'Theoretical proof verification requires human mathematician; three-way split calibration across multiple seeds requires sequential experiment iterations; domain expert annotation for MIMIC-IV confounder labels cannot be automated'}}

## Inspired By
Gap: Existing conformal causal methods assume error-free confounders; existing LLM conformal methods ignore causal settings; existing text-based causal methods provide only asymptotic guarantees; Barnatchez et al. handle missing confounders but not noisy extraction; Vovk & Wang handle confounding in prediction but not treatment effects. Pattern: Three converging literatures (modular CP, conformal PPI, conformal causal inference) that have not been connected. Key enablers: Zhang et al. (arXiv 2510.04406) modular residual decomposition framework; Csillag et al. (arXiv 2510.16166) conformal set-predictor for PPI; Alaa et al. (NeurIPS 2023) conformal meta-learners for ITE; Barber et al. (Annals of Statistics 2023) weighted exchangeability beyond standard CP assumptions.

## Target Venues
- AAAI 2027 (Primary — abstract July 21, full paper July 28, 2026; ~10 weeks from today)
- ARR August 2026 cycle (Secondary — submission August 3, 2026) → EACL 2027 (commitment October 11, 2026)
- AISTATS 2027 (Stretch — estimated deadline ~October 2026, not yet announced)

## Key References
- Zhang et al. 'Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition' (arXiv 2510.04406, 2025)
- Csillag et al. 'Extending Prediction-Powered Inference through Conformal Prediction' (arXiv 2510.16166, 2025)
- Angelopoulos et al. 'Prediction-Powered Inference' (Science, 2023)
- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025)
- Kato 'Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression' (arXiv 2511.08303, NeurIPS 2025)
- Barber et al. 'Conformal prediction beyond exchangeability' (Annals of Statistics, 2023)
- Alaa et al. 'Conformal Meta-learners for Predictive Inference of Individual Treatment Effects' (NeurIPS 2023)
- Wang & Dobriban 'Optimal Decision-Making Based on Prediction Sets' (arXiv 2602.00989, 2026)
- Lützow et al. 'Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting' (arXiv 2605.12341, 2026)
- Xu et al. 'Conformal prediction for multi-dimensional time series by ellipsoidal sets' (ICML 2024)
- Campos et al. 'Conformal Prediction for Natural Language Processing: A Survey' (TACL, 2024)
- Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation (arXiv 2509.21660, 2025)
- Lei & Candès 'Conformal Inference of Counterfactuals and Individual Treatment Effects' (JRSS-B, 2021)
- DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)
- Ma et al. 'LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding' (NeurIPS 2025)
- Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)
- Veitch et al. 'Adapting Text Embeddings for Causal Inference' (UAI 2020)
- Barnatchez et al. 'Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding' (arXiv 2604.03772, 2026)
- Vovk & Wang 'Conformal e-prediction in the presence of confounding' (arXiv 2603.11134, 2026)
- Gasparin & Ramdas 'Improving the statistical efficiency of cross-conformal prediction' (arXiv 2503.01495, ICML 2025)
- Chernozhukov et al. 'Double/debiased machine learning for treatment and structural parameters' (Econometrics Journal, 2018)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "affcd16d-01d2-456a-8bfd-5eefbc1400dc",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:23:02.410Z_

```json
{
  "parentUuid": "affcd16d-01d2-456a-8bfd-5eefbc1400dc",
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
  "uuid": "ec2fdbbb-1acb-4fd1-9b1b-9814250ec9f7",
  "timestamp": "2026-05-20T03:23:02.410Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:23:02.410Z_

```json
{
  "parentUuid": "ec2fdbbb-1acb-4fd1-9b1b-9814250ec9f7",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "037bb6ff-8bd6-44a8-9059-a3b4b5f9bc5d",
  "timestamp": "2026-05-20T03:23:02.410Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T03:23:02.410Z_

```json
{
  "parentUuid": "037bb6ff-8bd6-44a8-9059-a3b4b5f9bc5d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a23f8bb1-ada6-4935-af85-90e7512dad51",
  "timestamp": "2026-05-20T03:23:02.410Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Descrip…",
  "leafUuid": "a23f8bb1-ada6-4935-af85-90e7512dad51",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

### Assistant

_source line 9 · 2026-05-20T03:23:06.775Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about combining conformal prediction with causal inference when using LLM-extracted text confounders. Before I can properly evaluate the idea quality, I need to do thorough literature research to understand the current landscape.

Let me first search for the key papers and concepts mentioned in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a23f8bb1-ada6-4935-af85-90e7512dad51",
  "isSidechain": false,
  "requestId": "req_011CbD6yTaLinnaF3734osrp",
  "type": "assistant",
  "uuid": "75fc1ce3-1a3a-4802-a658-1ff2e3d44b0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzMpsw2Yeh4B1TaGr6L6gV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8067,
      "cache_read_input_tokens": 13591,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 191,
          "cache_read_input_tokens": 13591,
          "cache_creation_input_tokens": 8067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8067
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

_source line 10 · 2026-05-20T03:23:07.317Z_

I need to conduct thorough literature research before evaluating this proposal. Let me search for the key papers and the current state of this research area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75fc1ce3-1a3a-4802-a658-1ff2e3d44b0d",
  "isSidechain": false,
  "requestId": "req_011CbD6yTaLinnaF3734osrp",
  "type": "assistant",
  "uuid": "d060b5f5-2d79-470d-a4b8-f0f6bb6eb0e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzMpsw2Yeh4B1TaGr6L6gV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8067,
      "cache_read_input_tokens": 13591,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 191,
          "cache_read_input_tokens": 13591,
          "cache_creation_input_tokens": 8067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8067
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

_source line 11 · 2026-05-20T03:23:07.726Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018H6YpRmGeKMcDn5Qy7rePY`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d060b5f5-2d79-470d-a4b8-f0f6bb6eb0e4",
  "isSidechain": false,
  "requestId": "req_011CbD6yTaLinnaF3734osrp",
  "type": "assistant",
  "uuid": "1e6ce2be-e105-4fb0-b128-bc525534a5ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzMpsw2Yeh4B1TaGr6L6gV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8067,
      "cache_read_input_tokens": 13591,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 191,
          "cache_read_input_tokens": 13591,
          "cache_creation_input_tokens": 8067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8067
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

_source line 12 · 2026-05-20T03:23:07.732Z_

<details><summary>↩ Tool result · `toolu_018H6YpRmGeKMcDn5Qy7rePY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e6ce2be-e105-4fb0-b128-bc525534a5ee",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "01f098b1-9f18-44fe-bfc7-95dae4242eb5",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "1e6ce2be-e105-4fb0-b128-bc525534a5ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T03:23:10.808Z_

Now let me conduct the required literature searches. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01f098b1-9f18-44fe-bfc7-95dae4242eb5",
  "isSidechain": false,
  "requestId": "req_011CbD6yr8QVM6FCEZ3pXj4n",
  "type": "assistant",
  "uuid": "33b78315-8acd-4d37-a2e7-473376c8b074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWFPNEPnY9cQpcRF5DAtZu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 21658,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 21658,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 14 · 2026-05-20T03:23:10.995Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TGzQLeSET7j1nC2EmEjeLY`</summary>

```json
{
  "query": "conformal prediction causal inference treatment effects 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33b78315-8acd-4d37-a2e7-473376c8b074",
  "isSidechain": false,
  "requestId": "req_011CbD6yr8QVM6FCEZ3pXj4n",
  "type": "assistant",
  "uuid": "14934476-1338-45b6-b687-cf9373d72703",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWFPNEPnY9cQpcRF5DAtZu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 21658,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 21658,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 15 · 2026-05-20T03:23:20.294Z_

<details><summary>↩ Tool result · `toolu_01TGzQLeSET7j1nC2EmEjeLY`</summary>

```text
Web search results for query: "conformal prediction causal inference treatment effects 2025 2026"

Links: [{"title":"CONFIDE: CONformal Free Inference for Distribution-Free Estimation in Causal Competing Risks","url":"https://www.mdpi.com/2227-7390/14/2/383"},{"title":"A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation: Methods and Challenges","url":"https://arxiv.org/html/2509.21660"},{"title":"Conformal prediction for causal effects of continuous treatments","url":"https://arxiv.org/html/2407.03094v3"},{"title":"[2407.03094] Conformal Prediction for Causal Effects of Continuous Treatments","url":"https://arxiv.org/abs/2407.03094"},{"title":"Conformal prediction for causal effects of continuous treatments | OpenReview","url":"https://openreview.net/forum?id=pVL4bYKOGM"},{"title":"(PDF) Conformal Inference for Counterfactuals and Individual Treatment Effects with Experiment Attrition","url":"https://www.researchgate.net/publication/403430038_Conformal_Inference_for_Counterfactuals_and_Individual_Treatment_Effects_with_Experiment_Attrition"},{"title":"Conformal Prediction for Causal Effects of Continuous Treatments","url":"https://arxiv.org/pdf/2407.03094"},{"title":"Conformal causal inference for cluster randomized trials: model-robust   inference without asymptotic approximations","url":"https://arxiv.org/pdf/2401.01977"}]

Here are the search results for conformal prediction in causal inference and treatment effects from 2025-2026:

## Key Recent Developments

**Systematic Review (2025)**
A comprehensive systematic review provides an overview of conformal prediction techniques for treatment effect estimation, with no other review paper existing for applying conformal prediction for treatment effect estimation. The application of conformal prediction for causal inference addresses the challenge that exchangeability is violated in causal inference due to unobserved counterfactuals, with weighted exchangeability enabling the handling of distributional shifts.

**Continuous Treatments (2025-2026)**
A novel conformal prediction method for potential outcomes of continuous treatments provides finite-sample prediction intervals with model-agnostic guarantees and accounts for uncertainty from propensity estimation, even when the propensity score is unknown.

**Causal Competing Risks (2026)**
CONFIDE provides individual-level prediction sets for time-to-event outcomes (published January 2026), offering more clinically actionable personalized treatment decisions by quantifying uncertainty in future patient outcomes rather than population averages.

**Surrogate Variables (2025)**
Recent work integrates surrogate variables as proxies for unobserved outcomes to enhance the calibration of prediction intervals for individual treatment effects.

**Cluster Randomized Trials**
While conformal prediction has been extended for causal inference in non-clustered data, applications to clustered data remain understudied because individual observations have marginal non-exchangeability due to intra-cluster correlation, requiring essential modifications to existing theory.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14934476-1338-45b6-b687-cf9373d72703",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "61ecf515-159b-4587-ab1f-88ca69e9e90d",
  "toolUseResult": {
    "query": "conformal prediction causal inference treatment effects 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SBzpx9DEsFtMssMj8EVSUT",
        "content": [
          {
            "title": "CONFIDE: CONformal Free Inference for Distribution-Free Estimation in Causal Competing Risks",
            "url": "https://www.mdpi.com/2227-7390/14/2/383"
          },
          {
            "title": "A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation: Methods and Challenges",
            "url": "https://arxiv.org/html/2509.21660"
          },
          {
            "title": "Conformal prediction for causal effects of continuous treatments",
            "url": "https://arxiv.org/html/2407.03094v3"
          },
          {
            "title": "[2407.03094] Conformal Prediction for Causal Effects of Continuous Treatments",
            "url": "https://arxiv.org/abs/2407.03094"
          },
          {
            "title": "Conformal prediction for causal effects of continuous treatments | OpenReview",
            "url": "https://openreview.net/forum?id=pVL4bYKOGM"
          },
          {
            "title": "(PDF) Conformal Inference for Counterfactuals and Individual Treatment Effects with Experiment Attrition",
            "url": "https://www.researchgate.net/publication/403430038_Conformal_Inference_for_Counterfactuals_and_Individual_Treatment_Effects_with_Experiment_Attrition"
          },
          {
            "title": "Conformal Prediction for Causal Effects of Continuous Treatments",
            "url": "https://arxiv.org/pdf/2407.03094"
          },
          {
            "title": "Conformal causal inference for cluster randomized trials: model-robust   inference without asymptotic approximations",
            "url": "https://arxiv.org/pdf/2401.01977"
          }
        ]
      },
      "Here are the search results for conformal prediction in causal inference and treatment effects from 2025-2026:\n\n## Key Recent Developments\n\n**Systematic Review (2025)**\nA comprehensive systematic review provides an overview of conformal prediction techniques for treatment effect estimation, with no other review paper existing for applying conformal prediction for treatment effect estimation. The application of conformal prediction for causal inference addresses the challenge that exchangeability is violated in causal inference due to unobserved counterfactuals, with weighted exchangeability enabling the handling of distributional shifts.\n\n**Continuous Treatments (2025-2026)**\nA novel conformal prediction method for potential outcomes of continuous treatments provides finite-sample prediction intervals with model-agnostic guarantees and accounts for uncertainty from propensity estimation, even when the propensity score is unknown.\n\n**Causal Competing Risks (2026)**\nCONFIDE provides individual-level prediction sets for time-to-event outcomes (published January 2026), offering more clinically actionable personalized treatment decisions by quantifying uncertainty in future patient outcomes rather than population averages.\n\n**Surrogate Variables (2025)**\nRecent work integrates surrogate variables as proxies for unobserved outcomes to enhance the calibration of prediction intervals for individual treatment effects.\n\n**Cluster Randomized Trials**\nWhile conformal prediction has been extended for causal inference in non-clustered data, applications to clustered data remain understudied because individual observations have marginal non-exchangeability due to intra-cluster correlation, requiring essential modifications to existing theory."
    ],
    "durationSeconds": 9.270699107,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "14934476-1338-45b6-b687-cf9373d72703",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T03:23:24.064Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JsXkaRavZ4H6pHB6HdBqJ6`</summary>

```json
{
  "query": "modular conformal prediction sequential pipelines Zhang 2025 arXiv 2510.04406"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61ecf515-159b-4587-ab1f-88ca69e9e90d",
  "isSidechain": false,
  "requestId": "req_011CbD6zmdpS2DjgakaEJTFb",
  "type": "assistant",
  "uuid": "4a0adf3e-4daa-479d-9db4-199a76bebf23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQssPjtiX2xiFTowasY773",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 22376,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 22376,
          "cache_creation_input_tokens": 872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 872
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

_source line 17 · 2026-05-20T03:23:30.571Z_

<details><summary>↩ Tool result · `toolu_01JsXkaRavZ4H6pHB6HdBqJ6`</summary>

```text
Web search results for query: "modular conformal prediction sequential pipelines Zhang 2025 arXiv 2510.04406"

Links: [{"title":"[2510.04406] Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/abs/2510.04406"},{"title":"[2510.04406v1] Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/abs/2510.04406v1"},{"title":"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/pdf/2510.04406"},{"title":"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/html/2510.04406v1"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/stat.ML/2025-10?skip=25&show=25"}]

I found the paper! Here are the details:

**Title:** Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition

**Authors:** William Zhang, Saurabh Amin, and Georgia Perakis

**Paper ID:** arXiv:2510.04406

**Submission Date:** October 7, 2025

**Overview:** The paper introduces a conformal prediction framework for two-stage sequential models, where an upstream predictor generates intermediate representations for a downstream model. Existing methods treat the entire modeling process as a black box, overlooking opportunities to exploit modular structure.

**Key Contribution:** By decomposing the overall prediction residual into stage-specific components, the method enables practitioners to attribute uncertainty to specific pipeline stages.

**Methodology:** The paper develops a risk-controlled parameter selection procedure using family-wise error rate (FWER) control to calibrate stage-wise scaling parameters, and proposes an adaptive extension for non-stationary settings that preserves long-run coverage guarantees.

**Experiments:** Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that the approach maintains coverage under conditions that degrade standard conformal methods, while providing interpretable stage-wise uncertainty attribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a0adf3e-4daa-479d-9db4-199a76bebf23",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "63d0b3cc-c6f4-4286-b473-1d9fc558aa82",
  "toolUseResult": {
    "query": "modular conformal prediction sequential pipelines Zhang 2025 arXiv 2510.04406",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PdqsrnB1ajvwccnjL1u2EZ",
        "content": [
          {
            "title": "[2510.04406] Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition",
            "url": "https://arxiv.org/abs/2510.04406"
          },
          {
            "title": "[2510.04406v1] Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition",
            "url": "https://arxiv.org/abs/2510.04406v1"
          },
          {
            "title": "Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition",
            "url": "https://arxiv.org/pdf/2510.04406"
          },
          {
            "title": "Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition",
            "url": "https://arxiv.org/html/2510.04406v1"
          },
          {
            "title": "Machine Learning Oct 2025",
            "url": "https://arxiv.org/list/stat.ML/2025-10?skip=25&show=25"
          }
        ]
      },
      "I found the paper! Here are the details:\n\n**Title:** Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition\n\n**Authors:** William Zhang, Saurabh Amin, and Georgia Perakis\n\n**Paper ID:** arXiv:2510.04406\n\n**Submission Date:** October 7, 2025\n\n**Overview:** The paper introduces a conformal prediction framework for two-stage sequential models, where an upstream predictor generates intermediate representations for a downstream model. Existing methods treat the entire modeling process as a black box, overlooking opportunities to exploit modular structure.\n\n**Key Contribution:** By decomposing the overall prediction residual into stage-specific components, the method enables practitioners to attribute uncertainty to specific pipeline stages.\n\n**Methodology:** The paper develops a risk-controlled parameter selection procedure using family-wise error rate (FWER) control to calibrate stage-wise scaling parameters, and proposes an adaptive extension for non-stationary settings that preserves long-run coverage guarantees.\n\n**Experiments:** Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that the approach maintains coverage under conditions that degrade standard conformal methods, while providing interpretable stage-wise uncertainty attribution."
    ],
    "durationSeconds": 6.502748485,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4a0adf3e-4daa-479d-9db4-199a76bebf23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T03:23:32.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GmoEmsq9qNA4nZqqtxJ671`</summary>

```json
{
  "query": "prediction-powered inference conformal prediction Csillag 2025 arXiv 2510.16166"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63d0b3cc-c6f4-4286-b473-1d9fc558aa82",
  "isSidechain": false,
  "requestId": "req_011CbD71XWnBfXt5c6kKcYn1",
  "type": "assistant",
  "uuid": "42dbba76-c25b-44ca-88b1-d10c69bd3583",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wpp2q1f1Q2i1E46f7u31Jx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 23248,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 23248,
          "cache_creation_input_tokens": 649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 649
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

_source line 19 · 2026-05-20T03:23:41.055Z_

<details><summary>↩ Tool result · `toolu_01GmoEmsq9qNA4nZqqtxJ671`</summary>

```text
Web search results for query: "prediction-powered inference conformal prediction Csillag 2025 arXiv 2510.16166"

Links: [{"title":"[2510.16166] Extending Prediction-Powered Inference through Conformal Prediction","url":"https://arxiv.org/abs/2510.16166"},{"title":"Published as a preprint EXTENDING PREDICTION-POWERED INFERENCE","url":"https://arxiv.org/pdf/2510.16166"},{"title":"Extending Prediction-Powered Inference through Conformal Prediction","url":"https://arxiv.org/html/2510.16166v1"},{"title":"Powerful batch conformal prediction for classification","url":"https://arxiv.org/pdf/2411.02239"},{"title":"Conformal Prediction for Signal Temporal Logic Inference","url":"https://arxiv.org/pdf/2509.25473"},{"title":"Predictive Inference with Feature Conformal Prediction","url":"https://arxiv.org/pdf/2210.00173"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Extending Prediction-Powered Inference through Conformal Prediction" by Daniel Csillag, Pedro Dall'Antonia, Claudio José Struchiner, and Guilherme Tegoni Goedert, submitted on October 17, 2025 (arXiv:2510.16166).

**Overview:**

Prediction-powered inference is a recent methodology for the safe use of black-box ML models to impute missing data, strengthening inference of statistical parameters. However, many applications require strong properties besides valid inference, such as privacy, robustness or validity under continuous distribution shifts. The paper resolves this issue by connecting prediction-powered inference with conformal prediction: by performing imputation through a calibrated conformal set-predictor, they attain validity while achieving additional guarantees in a natural manner.

**Scope and Applications:**

The procedure is instantiated for the inference of means, Z- and M-estimation, as well as e-values and e-value-based procedures, and in the case of e-values, it is the first general prediction-powered procedure that operates off-line.

**Key Advantages:**

The approach allows researchers to directly leverage the vast literature on conformal prediction with additional guarantees, spanning privacy, robustness to strategic and adversarial distribution shift, continuous distribution shift, robustness to outliers, and censored/missing data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42dbba76-c25b-44ca-88b1-d10c69bd3583",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "d7987b5a-ab6d-4327-a762-76b24f78b239",
  "toolUseResult": {
    "query": "prediction-powered inference conformal prediction Csillag 2025 arXiv 2510.16166",
    "results": [
      {
        "tool_use_id": "srvtoolu_014MNrwjyNkBYagA7oF23T3G",
        "content": [
          {
            "title": "[2510.16166] Extending Prediction-Powered Inference through Conformal Prediction",
            "url": "https://arxiv.org/abs/2510.16166"
          },
          {
            "title": "Published as a preprint EXTENDING PREDICTION-POWERED INFERENCE",
            "url": "https://arxiv.org/pdf/2510.16166"
          },
          {
            "title": "Extending Prediction-Powered Inference through Conformal Prediction",
            "url": "https://arxiv.org/html/2510.16166v1"
          },
          {
            "title": "Powerful batch conformal prediction for classification",
            "url": "https://arxiv.org/pdf/2411.02239"
          },
          {
            "title": "Conformal Prediction for Signal Temporal Logic Inference",
            "url": "https://arxiv.org/pdf/2509.25473"
          },
          {
            "title": "Predictive Inference with Feature Conformal Prediction",
            "url": "https://arxiv.org/pdf/2210.00173"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper is titled \"Extending Prediction-Powered Inference through Conformal Prediction\" by Daniel Csillag, Pedro Dall'Antonia, Claudio José Struchiner, and Guilherme Tegoni Goedert, submitted on October 17, 2025 (arXiv:2510.16166).\n\n**Overview:**\n\nPrediction-powered inference is a recent methodology for the safe use of black-box ML models to impute missing data, strengthening inference of statistical parameters. However, many applications require strong properties besides valid inference, such as privacy, robustness or validity under continuous distribution shifts. The paper resolves this issue by connecting prediction-powered inference with conformal prediction: by performing imputation through a calibrated conformal set-predictor, they attain validity while achieving additional guarantees in a natural manner.\n\n**Scope and Applications:**\n\nThe procedure is instantiated for the inference of means, Z- and M-estimation, as well as e-values and e-value-based procedures, and in the case of e-values, it is the first general prediction-powered procedure that operates off-line.\n\n**Key Advantages:**\n\nThe approach allows researchers to directly leverage the vast literature on conformal prediction with additional guarantees, spanning privacy, robustness to strategic and adversarial distribution shift, continuous distribution shift, robustness to outliers, and censored/missing data."
    ],
    "durationSeconds": 8.058522340000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "42dbba76-c25b-44ca-88b1-d10c69bd3583",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T03:23:43.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019CDmHKyP28AtGBCZ4iKcir`</summary>

```json
{
  "query": "LLM text confounders causal inference DoubleLingo NeurIPS 2025 Ma treatment effect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7987b5a-ab6d-4327-a762-76b24f78b239",
  "isSidechain": false,
  "requestId": "req_011CbD72JNnQP2NEcLVQ8Q7D",
  "type": "assistant",
  "uuid": "cd320986-40a1-4ec3-817b-05a4ee3e9597",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1APgaunfjxbo7MnAzuATt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 23897,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 23897,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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

_source line 21 · 2026-05-20T03:23:49.809Z_

<details><summary>↩ Tool result · `toolu_019CDmHKyP28AtGBCZ4iKcir`</summary>

```text
Web search results for query: "LLM text confounders causal inference DoubleLingo NeurIPS 2025 Ma treatment effect"

Links: [{"title":"Estimating Causal Effects of Text Interventions Leveraging LLMs","url":"https://arxiv.org/html/2410.21474"},{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding | OpenReview","url":"https://openreview.net/forum?id=sv41aaGTit"},{"title":"DoubleLingo: Causal Estimation with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-short.71/"},{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://arxiv.org/html/2507.02843"},{"title":"Using LLMs to Directly Guess Conditional Expectations Can Improve Efficiency in Causal Estimation","url":"https://arxiv.org/pdf/2510.09684"},{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://arxiv.org/pdf/2507.02843"},{"title":"Causal Representation Learning with Generative Artificial Intelligence: Application to Texts as Treatments","url":"https://arxiv.org/pdf/2410.00903"}]

Based on the search results, I found relevant information about your query:

The paper "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding" by Yuchen Ma and colleagues addresses the challenge of estimating treatment effects in clinical practice, where models are trained on well-structured medical datasets but at inference time must make predictions using textual descriptions like self-reported symptoms, which are incomplete representations of the original patient information.

The work formalizes this as an "inference time text confounding" problem, where confounders are fully observed during training time but only partially available through text at inference time.

To address this problem, the authors propose a novel framework for estimating treatment effects that explicitly accounts for inference time text confounding by leveraging large language models together with a custom doubly robust learner to mitigate biases caused by the inference time text confounding.

Additionally, the DoubleLingo method (from a separate work) addresses the challenge that when confounders include text data, existing causal inference methods struggle due to the high dimensionality of text, and proposes enabling theoretically consistent estimation of causal effects using LLM-based nuisance models by incorporating them within the framework of Double Machine Learning.

The Ma et al. work was published at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd320986-40a1-4ec3-817b-05a4ee3e9597",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "597d40ab-9302-44be-b7b2-892e7e78bd7d",
  "toolUseResult": {
    "query": "LLM text confounders causal inference DoubleLingo NeurIPS 2025 Ma treatment effect",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EDFZYQAWRQyme2Re7VpNTG",
        "content": [
          {
            "title": "Estimating Causal Effects of Text Interventions Leveraging LLMs",
            "url": "https://arxiv.org/html/2410.21474"
          },
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding | OpenReview",
            "url": "https://openreview.net/forum?id=sv41aaGTit"
          },
          {
            "title": "DoubleLingo: Causal Estimation with Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-short.71/"
          },
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://arxiv.org/html/2507.02843"
          },
          {
            "title": "Using LLMs to Directly Guess Conditional Expectations Can Improve Efficiency in Causal Estimation",
            "url": "https://arxiv.org/pdf/2510.09684"
          },
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://arxiv.org/pdf/2507.02843"
          },
          {
            "title": "Causal Representation Learning with Generative Artificial Intelligence: Application to Texts as Treatments",
            "url": "https://arxiv.org/pdf/2410.00903"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query:\n\nThe paper \"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding\" by Yuchen Ma and colleagues addresses the challenge of estimating treatment effects in clinical practice, where models are trained on well-structured medical datasets but at inference time must make predictions using textual descriptions like self-reported symptoms, which are incomplete representations of the original patient information.\n\nThe work formalizes this as an \"inference time text confounding\" problem, where confounders are fully observed during training time but only partially available through text at inference time.\n\nTo address this problem, the authors propose a novel framework for estimating treatment effects that explicitly accounts for inference time text confounding by leveraging large language models together with a custom doubly robust learner to mitigate biases caused by the inference time text confounding.\n\nAdditionally, the DoubleLingo method (from a separate work) addresses the challenge that when confounders include text data, existing causal inference methods struggle due to the high dimensionality of text, and proposes enabling theoretically consistent estimation of causal effects using LLM-based nuisance models by incorporating them within the framework of Double Machine Learning.\n\nThe Ma et al. work was published at NeurIPS 2025."
    ],
    "durationSeconds": 6.253270172999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cd320986-40a1-4ec3-817b-05a4ee3e9597",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Descrip…",
  "leafUuid": "597d40ab-9302-44be-b7b2-892e7e78bd7d",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

### Tool call

_source line 24 · 2026-05-20T03:23:52.554Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HVrbQJrCvBv3Hdyz6M7cVB`</summary>

```json
{
  "query": "Barnatchez conformal prediction counterfactual outcomes runtime confounding arXiv 2604.03772 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "597d40ab-9302-44be-b7b2-892e7e78bd7d",
  "isSidechain": false,
  "requestId": "req_011CbD72wo4XVgQuwK8h7HMn",
  "type": "assistant",
  "uuid": "fab2d67c-4615-4ac8-80ea-53a918bc5998",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hr236Locfc2MQ8qA217v5X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 24580,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 24580,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 25 · 2026-05-20T03:23:58.848Z_

<details><summary>↩ Tool result · `toolu_01HVrbQJrCvBv3Hdyz6M7cVB`</summary>

```text
Web search results for query: "Barnatchez conformal prediction counterfactual outcomes runtime confounding arXiv 2604.03772 2026"

Links: [{"title":"[2604.03772] Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/abs/2604.03772"},{"title":"[2604.03772v1] Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/abs/2604.03772v1"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/html/2604.03772"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/pdf/2604.03772"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding - AI Research Paper Analysis | ArxivLens - Arxivlens","url":"https://arxivlens.com/PaperView/Details/debiased-machine-learning-for-conformal-prediction-of-counterfactual-outcomes-under-runtime-confounding-3519-d149b03f"}]

I found the research paper you're looking for. Here's what the search returned:

The paper is titled "Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding" by Keith Barnatchez, Kevin P. Josey, Rachel C. Nethery, and Giovanni Parmigiani.

The paper discusses how conformal prediction has become a popular method for producing assumption-lean prediction intervals for counterfactual outcomes that would arise under different treatment decisions in the target population of interest. However, existing methods require that every confounding factor of the treatment-outcome relationship used for training on the source data is additionally measured in the target population, risking miscoverage if important confounders are unmeasured in the target population.

The paper introduces a computationally efficient debiased machine learning framework that allows for valid prediction intervals when only a subset of confounders is measured in the target population, a common challenge referred to as runtime confounding. The prediction intervals achieve desired coverage rates with faster convergence compared to standard methods.

The paper was posted to arXiv on April 4, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fab2d67c-4615-4ac8-80ea-53a918bc5998",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "56419b00-4f4e-47dc-ac6d-a9e7a2995159",
  "toolUseResult": {
    "query": "Barnatchez conformal prediction counterfactual outcomes runtime confounding arXiv 2604.03772 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EEut5B1ragGaZnez5aSKdH",
        "content": [
          {
            "title": "[2604.03772] Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding",
            "url": "https://arxiv.org/abs/2604.03772"
          },
          {
            "title": "[2604.03772v1] Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding",
            "url": "https://arxiv.org/abs/2604.03772v1"
          },
          {
            "title": "Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding",
            "url": "https://arxiv.org/html/2604.03772"
          },
          {
            "title": "Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding",
            "url": "https://arxiv.org/pdf/2604.03772"
          },
          {
            "title": "Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding - AI Research Paper Analysis | ArxivLens - Arxivlens",
            "url": "https://arxivlens.com/PaperView/Details/debiased-machine-learning-for-conformal-prediction-of-counterfactual-outcomes-under-runtime-confounding-3519-d149b03f"
          }
        ]
      },
      "I found the research paper you're looking for. Here's what the search returned:\n\nThe paper is titled \"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding\" by Keith Barnatchez, Kevin P. Josey, Rachel C. Nethery, and Giovanni Parmigiani.\n\nThe paper discusses how conformal prediction has become a popular method for producing assumption-lean prediction intervals for counterfactual outcomes that would arise under different treatment decisions in the target population of interest. However, existing methods require that every confounding factor of the treatment-outcome relationship used for training on the source data is additionally measured in the target population, risking miscoverage if important confounders are unmeasured in the target population.\n\nThe paper introduces a computationally efficient debiased machine learning framework that allows for valid prediction intervals when only a subset of confounders is measured in the target population, a common challenge referred to as runtime confounding. The prediction intervals achieve desired coverage rates with faster convergence compared to standard methods.\n\nThe paper was posted to arXiv on April 4, 2026."
    ],
    "durationSeconds": 6.291140627000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fab2d67c-4615-4ac8-80ea-53a918bc5998",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T03:24:01.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0134BLqbtCEQKcnJnV9xUwVP`</summary>

```json
{
  "query": "conformal prediction noisy covariates measurement error confounders finite-sample 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56419b00-4f4e-47dc-ac6d-a9e7a2995159",
  "isSidechain": false,
  "requestId": "req_011CbD73cRGDhvrXNHKKDX8m",
  "type": "assistant",
  "uuid": "06eb2628-1456-470a-bc49-b83cb2410ce4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1TFYcYEwCj2YcbXkfxo7V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 25307,
      "output_tokens": 73,
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
          "output_tokens": 73,
          "cache_read_input_tokens": 25307,
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T03:24:09.530Z_

<details><summary>↩ Tool result · `toolu_0134BLqbtCEQKcnJnV9xUwVP`</summary>

```text
Web search results for query: "conformal prediction noisy covariates measurement error confounders finite-sample 2025 2026"

Links: [{"title":"Conformal Prediction for Astronomy Data with Measurement Error","url":"https://arxiv.org/html/2412.10544"},{"title":"Conformal Prediction for Astronomy Data with Measurement Error","url":"https://arxiv.org/pdf/2412.10544"},{"title":"[2412.10544] Conformal Prediction for Astronomy Data with Measurement Error","url":"https://arxiv.org/abs/2412.10544"},{"title":"Conformal prediction for astronomy data with measurement error | Monthly Notices of the Royal Astronomical Society | Oxford Academic","url":"https://academic.oup.com/mnras/article/539/2/1372/8102943"},{"title":"Conformal prediction for astronomy data with measurement error - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025MNRAS.539.1372S/abstract"},{"title":"Identification of confounder in epidemiologic data contaminated by measurement error in covariates","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4870765/"},{"title":"Conformal e-prediction in the presence of confounding","url":"https://arxiv.org/pdf/2603.11134"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/pdf/2604.03772"}]

Based on the web search results, I found several relevant recent papers on conformal prediction with measurement error and confounding:

## Key Findings

**Conformal Prediction for Measurement Error (2025):**
A recent paper by Singer, Williams, and Ghosh published in the Monthly Notices of the Royal Astronomical Society (May 2025) addresses conformal prediction for astronomy data with measurement error, noting that few techniques exist to construct prediction intervals with finite sample coverage guarantees. The method provides finite sample control over Type I error probabilities under a variety of assumptions on measurement errors in the observed data.

**Conformal E-Prediction with Confounding (2026):**
A March 2026 paper by Vovk and Wang extends conformal e-prediction to cases with observed confounding between the random object X and its label Y, applying this approach to obtain finite-sample guarantees of validity.

**Debiased Machine Learning for Conformal Prediction (2025):**
A 2025 paper on debiased machine learning for conformal prediction of counterfactual outcomes under runtime confounding is situated at the intersection of causal inference and conformal prediction, being the first to extend the problem to constructing prediction intervals through semiparametric efficient conformal prediction.

These papers represent recent advances (2025-2026) addressing the intersection of conformal prediction with measurement error, noisy covariates, and confounding variables while maintaining finite-sample guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06eb2628-1456-470a-bc49-b83cb2410ce4",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "4714a2a6-c6dd-4506-82db-2984012683dc",
  "toolUseResult": {
    "query": "conformal prediction noisy covariates measurement error confounders finite-sample 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E2EjqxTjLiHac2DNV8D8AU",
        "content": [
          {
            "title": "Conformal Prediction for Astronomy Data with Measurement Error",
            "url": "https://arxiv.org/html/2412.10544"
          },
          {
            "title": "Conformal Prediction for Astronomy Data with Measurement Error",
            "url": "https://arxiv.org/pdf/2412.10544"
          },
          {
            "title": "[2412.10544] Conformal Prediction for Astronomy Data with Measurement Error",
            "url": "https://arxiv.org/abs/2412.10544"
          },
          {
            "title": "Conformal prediction for astronomy data with measurement error | Monthly Notices of the Royal Astronomical Society | Oxford Academic",
            "url": "https://academic.oup.com/mnras/article/539/2/1372/8102943"
          },
          {
            "title": "Conformal prediction for astronomy data with measurement error - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025MNRAS.539.1372S/abstract"
          },
          {
            "title": "Identification of confounder in epidemiologic data contaminated by measurement error in covariates",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4870765/"
          },
          {
            "title": "Conformal e-prediction in the presence of confounding",
            "url": "https://arxiv.org/pdf/2603.11134"
          },
          {
            "title": "Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding",
            "url": "https://arxiv.org/pdf/2604.03772"
          }
        ]
      },
      "Based on the web search results, I found several relevant recent papers on conformal prediction with measurement error and confounding:\n\n## Key Findings\n\n**Conformal Prediction for Measurement Error (2025):**\nA recent paper by Singer, Williams, and Ghosh published in the Monthly Notices of the Royal Astronomical Society (May 2025) addresses conformal prediction for astronomy data with measurement error, noting that few techniques exist to construct prediction intervals with finite sample coverage guarantees. The method provides finite sample control over Type I error probabilities under a variety of assumptions on measurement errors in the observed data.\n\n**Conformal E-Prediction with Confounding (2026):**\nA March 2026 paper by Vovk and Wang extends conformal e-prediction to cases with observed confounding between the random object X and its label Y, applying this approach to obtain finite-sample guarantees of validity.\n\n**Debiased Machine Learning for Conformal Prediction (2025):**\nA 2025 paper on debiased machine learning for conformal prediction of counterfactual outcomes under runtime confounding is situated at the intersection of causal inference and conformal prediction, being the first to extend the problem to constructing prediction intervals through semiparametric efficient conformal prediction.\n\nThese papers represent recent advances (2025-2026) addressing the intersection of conformal prediction with measurement error, noisy covariates, and confounding variables while maintaining finite-sample guarantees."
    ],
    "durationSeconds": 7.913663804999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "06eb2628-1456-470a-bc49-b83cb2410ce4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T03:24:12.257Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PWtFPxthQBiZWTKAU5XHaW`</summary>

```json
{
  "query": "prediction-powered inference causal inference treatment effect arXiv 2502.06343 Kato 2511.08303"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4714a2a6-c6dd-4506-82db-2984012683dc",
  "isSidechain": false,
  "requestId": "req_011CbD74QALzyATW1uxkxJrQ",
  "type": "assistant",
  "uuid": "5b366c73-9a7c-4440-ac61-ac87514cd465",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018nBZz7zeE2xsjHwv6pCFWF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 26013,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 26013,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 29 · 2026-05-20T03:24:19.223Z_

<details><summary>↩ Tool result · `toolu_01PWtFPxthQBiZWTKAU5XHaW`</summary>

```text
Web search results for query: "prediction-powered inference causal inference treatment effect arXiv 2502.06343 Kato 2511.08303"

Links: [{"title":"[2502.06343] Prediction-Powered Causal Inferences","url":"https://arxiv.org/abs/2502.06343"},{"title":"Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates for Prediction-Powered Causal Inference","url":"https://arxiv.org/html/2511.08303"},{"title":"Prediction-Powered Causal Inferences","url":"https://arxiv.org/html/2502.06343"},{"title":"Causal Lifting of Neural Representations: Zero-Shot Generalization for Causal Inferences","url":"https://arxiv.org/html/2502.06343v2"},{"title":"Causal Representation Learning with Generative Artificial Intelligence: Application to Texts as Treatments","url":"https://arxiv.org/pdf/2410.00903"},{"title":"Causal Effect Inference for Structured Treatments","url":"https://arxiv.org/pdf/2106.01939"},{"title":"Black Box Causal Inference: Effect Estimation via Meta Prediction","url":"https://arxiv.org/pdf/2503.05985"},{"title":"Causal machine learning for predicting treatment outcomes","url":"https://arxiv.org/pdf/2410.08770"},{"title":"Prediction-powered Generalization of Causal Inferences","url":"https://arxiv.org/html/2406.02873v1"}]

Based on the search results, I found information about both papers you mentioned:

## arXiv 2502.06343 - Prediction-Powered Causal Inferences

This paper focuses on Prediction-Powered Causal Inferences (PPCI), which involves estimating the treatment effect in an unlabeled target experiment, relying on training data with the same outcome annotated but potentially different treatment or effect modifiers. The authors show that conditional calibration guarantees valid PPCI at population level, and introduce a sufficient representation constraint transferring validity across experiments through Deconfounded Empirical Risk Minimization, a model-agnostic training objective.

## arXiv 2511.08303 - Semi-Supervised Treatment Effect Estimation

This paper by Masahiro Kato investigates treatment effect estimation in the semi-supervised setting (which can be interpreted as prediction-powered inference), where researchers can use not only the standard triple of covariates, treatment indicator, and outcome, but also unlabeled auxiliary covariates. The work develops efficiency bounds and efficient estimators whose asymptotic variance aligns with the efficiency bound.

Both papers address the challenge of leveraging unlabeled or auxiliary data to improve causal inference and treatment effect estimation in settings where full labels are unavailable or expensive to obtain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b366c73-9a7c-4440-ac61-ac87514cd465",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "29d838f2-e9de-4ddf-948d-ee8fef60b642",
  "toolUseResult": {
    "query": "prediction-powered inference causal inference treatment effect arXiv 2502.06343 Kato 2511.08303",
    "results": [
      {
        "tool_use_id": "srvtoolu_015WrZ6q7uLnFQoawiwFp8ii",
        "content": [
          {
            "title": "[2502.06343] Prediction-Powered Causal Inferences",
            "url": "https://arxiv.org/abs/2502.06343"
          },
          {
            "title": "Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates for Prediction-Powered Causal Inference",
            "url": "https://arxiv.org/html/2511.08303"
          },
          {
            "title": "Prediction-Powered Causal Inferences",
            "url": "https://arxiv.org/html/2502.06343"
          },
          {
            "title": "Causal Lifting of Neural Representations: Zero-Shot Generalization for Causal Inferences",
            "url": "https://arxiv.org/html/2502.06343v2"
          },
          {
            "title": "Causal Representation Learning with Generative Artificial Intelligence: Application to Texts as Treatments",
            "url": "https://arxiv.org/pdf/2410.00903"
          },
          {
            "title": "Causal Effect Inference for Structured Treatments",
            "url": "https://arxiv.org/pdf/2106.01939"
          },
          {
            "title": "Black Box Causal Inference: Effect Estimation via Meta Prediction",
            "url": "https://arxiv.org/pdf/2503.05985"
          },
          {
            "title": "Causal machine learning for predicting treatment outcomes",
            "url": "https://arxiv.org/pdf/2410.08770"
          },
          {
            "title": "Prediction-powered Generalization of Causal Inferences",
            "url": "https://arxiv.org/html/2406.02873v1"
          }
        ]
      },
      "Based on the search results, I found information about both papers you mentioned:\n\n## arXiv 2502.06343 - Prediction-Powered Causal Inferences\n\nThis paper focuses on Prediction-Powered Causal Inferences (PPCI), which involves estimating the treatment effect in an unlabeled target experiment, relying on training data with the same outcome annotated but potentially different treatment or effect modifiers. The authors show that conditional calibration guarantees valid PPCI at population level, and introduce a sufficient representation constraint transferring validity across experiments through Deconfounded Empirical Risk Minimization, a model-agnostic training objective.\n\n## arXiv 2511.08303 - Semi-Supervised Treatment Effect Estimation\n\nThis paper by Masahiro Kato investigates treatment effect estimation in the semi-supervised setting (which can be interpreted as prediction-powered inference), where researchers can use not only the standard triple of covariates, treatment indicator, and outcome, but also unlabeled auxiliary covariates. The work develops efficiency bounds and efficient estimators whose asymptotic variance aligns with the efficiency bound.\n\nBoth papers address the challenge of leveraging unlabeled or auxiliary data to improve causal inference and treatment effect estimation in settings where full labels are unavailable or expensive to obtain."
    ],
    "durationSeconds": 6.9619386189999934,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5b366c73-9a7c-4440-ac61-ac87514cd465",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T03:24:19.230Z_

```json
{
  "parentUuid": "29d838f2-e9de-4ddf-948d-ee8fef60b642",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5a1be286-ff29-47a0-b714-c18e1c291c27",
  "timestamp": "2026-05-20T03:24:19.230Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T03:24:22.273Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZTNr6QX4uhwTH2udow6k8`</summary>

```json
{
  "query": "cross-conformal prediction Gasparin Ramdas ICML 2025 sample efficiency arXiv 2503.01495"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a1be286-ff29-47a0-b714-c18e1c291c27",
  "isSidechain": false,
  "requestId": "req_011CbD757aUnAeBF5r7rEjtS",
  "type": "assistant",
  "uuid": "dcac9ad9-85d4-494b-ba48-10c23c5ce43b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fx75A47VZG6cxp34KLFv9o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 26818,
      "output_tokens": 82,
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
          "output_tokens": 82,
          "cache_read_input_tokens": 26818,
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T03:24:32.288Z_

<details><summary>↩ Tool result · `toolu_01QZTNr6QX4uhwTH2udow6k8`</summary>

```text
Web search results for query: "cross-conformal prediction Gasparin Ramdas ICML 2025 sample efficiency arXiv 2503.01495"

Links: [{"title":"CAOS: Conformal Aggregation of One-Shot Predictors","url":"https://arxiv.org/html/2601.05219v2"},{"title":"Statistics Mar 2025","url":"https://arxiv.org/list/stat/2025-03?skip=25&show=500"},{"title":"[2503.01495] Improving the statistical efficiency of cross-conformal prediction","url":"https://arxiv.org/abs/2503.01495"},{"title":"[2503.01495] Improving the statistical efficiency of cross-conformal prediction","url":"https://ar5iv.labs.arxiv.org/html/2503.01495"},{"title":"Machine Learning Mar 2025 - stat.ML","url":"https://www.arxiv.org/list/stat.ML/2025-03"},{"title":"Applications Mar 2025","url":"https://arxiv.org/list/stat.AP/2025-03?skip=100&show=50"},{"title":"Improving the statistical efficiency of cross-conformal prediction","url":"https://arxiv.org/pdf/2503.01495"},{"title":"ICML Poster Improving the Statistical Efficiency of Cross-Conformal Prediction","url":"https://icml.cc/virtual/2025/poster/44129"}]

Based on the search results, I found information about the paper you're looking for:

The paper "Improving the statistical efficiency of cross-conformal prediction" by Matteo Gasparin and Aaditya Ramdas addresses cross-conformal prediction, a modification of split conformal designed to improve the width of prediction sets.

The original cross-conformal method by Vovk (2015) ensures a marginal coverage of at least 1 - 2α - 2(1-α)(K-1)/(n+K), where n is the number of observations and K denotes the number of folds. A simple modification achieves coverage of at least 1-2α. The authors propose new variants of both methods that yield smaller prediction sets without compromising these theoretical guarantees.

The proposed methods are based on recent results deriving more statistically efficient combination of p-values that leverage exchangeability and randomization.

The paper was presented as a poster at ICML on July 15, 2025. The arXiv preprint is available at arXiv:2503.01495.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcac9ad9-85d4-494b-ba48-10c23c5ce43b",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "9768d34e-d790-4ccc-b55d-1a3d11f362ec",
  "toolUseResult": {
    "query": "cross-conformal prediction Gasparin Ramdas ICML 2025 sample efficiency arXiv 2503.01495",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UtQWvcheuirSYUaREHVt22",
        "content": [
          {
            "title": "CAOS: Conformal Aggregation of One-Shot Predictors",
            "url": "https://arxiv.org/html/2601.05219v2"
          },
          {
            "title": "Statistics Mar 2025",
            "url": "https://arxiv.org/list/stat/2025-03?skip=25&show=500"
          },
          {
            "title": "[2503.01495] Improving the statistical efficiency of cross-conformal prediction",
            "url": "https://arxiv.org/abs/2503.01495"
          },
          {
            "title": "[2503.01495] Improving the statistical efficiency of cross-conformal prediction",
            "url": "https://ar5iv.labs.arxiv.org/html/2503.01495"
          },
          {
            "title": "Machine Learning Mar 2025 - stat.ML",
            "url": "https://www.arxiv.org/list/stat.ML/2025-03"
          },
          {
            "title": "Applications Mar 2025",
            "url": "https://arxiv.org/list/stat.AP/2025-03?skip=100&show=50"
          },
          {
            "title": "Improving the statistical efficiency of cross-conformal prediction",
            "url": "https://arxiv.org/pdf/2503.01495"
          },
          {
            "title": "ICML Poster Improving the Statistical Efficiency of Cross-Conformal Prediction",
            "url": "https://icml.cc/virtual/2025/poster/44129"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nThe paper \"Improving the statistical efficiency of cross-conformal prediction\" by Matteo Gasparin and Aaditya Ramdas addresses cross-conformal prediction, a modification of split conformal designed to improve the width of prediction sets.\n\nThe original cross-conformal method by Vovk (2015) ensures a marginal coverage of at least 1 - 2α - 2(1-α)(K-1)/(n+K), where n is the number of observations and K denotes the number of folds. A simple modification achieves coverage of at least 1-2α. The authors propose new variants of both methods that yield smaller prediction sets without compromising these theoretical guarantees.\n\nThe proposed methods are based on recent results deriving more statistically efficient combination of p-values that leverage exchangeability and randomization.\n\nThe paper was presented as a poster at ICML on July 15, 2025. The arXiv preprint is available at arXiv:2503.01495."
    ],
    "durationSeconds": 10.010086509,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dcac9ad9-85d4-494b-ba48-10c23c5ce43b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T03:24:35.296Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TnwVRoQzQ3wxF7vhN6dQHi`</summary>

```json
{
  "query": "conformal prediction LLM extraction uncertainty NLP pipeline finite-sample guarantee 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9768d34e-d790-4ccc-b55d-1a3d11f362ec",
  "isSidechain": false,
  "requestId": "req_011CbD7665xrHfwZEiwbcKdE",
  "type": "assistant",
  "uuid": "e6eb3608-e19e-4354-b784-cd848c307b8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQi6bm6y4MChLcd1EkhYcm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 711,
      "cache_read_input_tokens": 27702,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 27702,
          "cache_creation_input_tokens": 711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 711
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

_source line 34 · 2026-05-20T03:24:42.679Z_

<details><summary>↩ Tool result · `toolu_01TnwVRoQzQ3wxF7vhN6dQHi`</summary>

```text
Web search results for query: "conformal prediction LLM extraction uncertainty NLP pipeline finite-sample guarantee 2025 2026"

Links: [{"title":"Conformal Prediction and Verification of Large Language Model Extractions in","url":"https://ojs.aaai.org/index.php/AAAI-SS/article/download/36929/39067/41006"},{"title":"Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains","url":"https://arxiv.org/html/2603.00924"},{"title":"An Empirical Study of Conformal Prediction in LLM with ASP Scaffolds for Robust Reasoning","url":"https://arxiv.org/html/2503.05439v1"},{"title":"Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains","url":"https://arxiv.org/pdf/2603.00924"},{"title":"Conformal Prediction Beyond the Seen: A Missing Mass Perspective for Uncertainty Quantification in Generative Models","url":"https://arxiv.org/html/2506.05497v1"},{"title":"Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations","url":"https://arxiv.org/html/2604.16217v1"},{"title":"ConU: Conformal Uncertainty in Large Language Models with Correctness   Coverage Guarantees","url":"https://arxiv.org/pdf/2407.00499"},{"title":"TECP: Token-Entropy Conformal Prediction for LLMs","url":"https://www.mdpi.com/2227-7390/13/20/3351"}]

I've found several highly relevant results on conformal prediction for LLM extraction with uncertainty quantification and finite-sample guarantees. Here are the key findings:

## Recent Work on Conformal Prediction for LLM Extraction

A conformal prediction framework provides statistical guarantees on the reliability of LLM-based extractions, combining probabilistic calibration, nonconformity scoring, and finite-sample guarantees to ensure that the expected proportion of incorrect extractions remains below a pre-specified risk level.

A conformal prediction framework based on risk-controlling prediction sets provides finite-sample false discovery rate (FDR) guarantees for LLM-based extraction across clinical domains.

## Addressing Uncertainty in NLP Pipelines

Deploying LLMs in clinical settings requires not only high accuracy but also reliable uncertainty quantification, as a model that assigns high confidence to incorrect extractions can lead to silent errors propagating through clinical decision pipelines.

Conformal prediction addresses challenges by converting raw model scores into accept/reject decisions with finite-sample guarantees under only an exchangeability assumption.

## Recent 2025-2026 Advances

An approach exploits the recently proposed Conformal Language Modelling to systematically address scaffold generation challenges in reasoning pipelines.

A finite-sample algorithm integrates the estimation of missing mass into the conformal prediction pipeline while provably maintaining valid, distribution-free coverage guarantees.

Token-Entropy Conformal Prediction (TECP) treats a log-probability-based token-entropy statistic as a nonconformity score and integrates it with split conformal prediction to construct prediction sets with finite-sample coverage guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6eb3608-e19e-4354-b784-cd848c307b8f",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "981340b4-f9ab-4f93-a83c-92bfd9c6d79a",
  "toolUseResult": {
    "query": "conformal prediction LLM extraction uncertainty NLP pipeline finite-sample guarantee 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012b8yhS8xAjo6C2EVNPx4rD",
        "content": [
          {
            "title": "Conformal Prediction and Verification of Large Language Model Extractions in",
            "url": "https://ojs.aaai.org/index.php/AAAI-SS/article/download/36929/39067/41006"
          },
          {
            "title": "Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains",
            "url": "https://arxiv.org/html/2603.00924"
          },
          {
            "title": "An Empirical Study of Conformal Prediction in LLM with ASP Scaffolds for Robust Reasoning",
            "url": "https://arxiv.org/html/2503.05439v1"
          },
          {
            "title": "Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains",
            "url": "https://arxiv.org/pdf/2603.00924"
          },
          {
            "title": "Conformal Prediction Beyond the Seen: A Missing Mass Perspective for Uncertainty Quantification in Generative Models",
            "url": "https://arxiv.org/html/2506.05497v1"
          },
          {
            "title": "Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations",
            "url": "https://arxiv.org/html/2604.16217v1"
          },
          {
            "title": "ConU: Conformal Uncertainty in Large Language Models with Correctness   Coverage Guarantees",
            "url": "https://arxiv.org/pdf/2407.00499"
          },
          {
            "title": "TECP: Token-Entropy Conformal Prediction for LLMs",
            "url": "https://www.mdpi.com/2227-7390/13/20/3351"
          }
        ]
      },
      "I've found several highly relevant results on conformal prediction for LLM extraction with uncertainty quantification and finite-sample guarantees. Here are the key findings:\n\n## Recent Work on Conformal Prediction for LLM Extraction\n\nA conformal prediction framework provides statistical guarantees on the reliability of LLM-based extractions, combining probabilistic calibration, nonconformity scoring, and finite-sample guarantees to ensure that the expected proportion of incorrect extractions remains below a pre-specified risk level.\n\nA conformal prediction framework based on risk-controlling prediction sets provides finite-sample false discovery rate (FDR) guarantees for LLM-based extraction across clinical domains.\n\n## Addressing Uncertainty in NLP Pipelines\n\nDeploying LLMs in clinical settings requires not only high accuracy but also reliable uncertainty quantification, as a model that assigns high confidence to incorrect extractions can lead to silent errors propagating through clinical decision pipelines.\n\nConformal prediction addresses challenges by converting raw model scores into accept/reject decisions with finite-sample guarantees under only an exchangeability assumption.\n\n## Recent 2025-2026 Advances\n\nAn approach exploits the recently proposed Conformal Language Modelling to systematically address scaffold generation challenges in reasoning pipelines.\n\nA finite-sample algorithm integrates the estimation of missing mass into the conformal prediction pipeline while provably maintaining valid, distribution-free coverage guarantees.\n\nToken-Entropy Conformal Prediction (TECP) treats a log-probability-based token-entropy statistic as a nonconformity score and integrates it with split conformal prediction to construct prediction sets with finite-sample coverage guarantees."
    ],
    "durationSeconds": 7.378022864999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e6eb3608-e19e-4354-b784-cd848c307b8f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Descrip…",
  "leafUuid": "981340b4-f9ab-4f93-a83c-92bfd9c6d79a",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

### Tool call

_source line 37 · 2026-05-20T03:24:45.764Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EexdmfM7BZM7JG589YTvW4`</summary>

```json
{
  "query": "CoRL 2026 conference on robot learning acceptance rate topics scope"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "981340b4-f9ab-4f93-a83c-92bfd9c6d79a",
  "isSidechain": false,
  "requestId": "req_011CbD76qrVA5DagPsw5GvQ1",
  "type": "assistant",
  "uuid": "b75846fd-96f9-4616-a0d3-acfee34f06a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCw1ScGQPZDf2PBTp1frbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 28413,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 28413,
          "cache_creation_input_tokens": 865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 865
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

_source line 38 · 2026-05-20T03:24:53.207Z_

<details><summary>↩ Tool result · `toolu_01EexdmfM7BZM7JG589YTvW4`</summary>

```text
Web search results for query: "CoRL 2026 conference on robot learning acceptance rate topics scope"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"Conference on Robot Learning on X: \"#CoRL got 671 submissions this year. This is huge! See below for the development. 👇 (this number is already without obvious desk rejections) https://t.co/HfrSQ2ILyO\" / X","url":"https://x.com/corl_conf/status/1801514565236076868"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"GitHub - Po-Jen/Robotics-Conference-Acceptance-Rate: Statistics of acceptance rate for the main robotics conference · GitHub","url":"https://github.com/Po-Jen/Robotics-Conference-Acceptance-Rate"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Towards Cognitive Robots That People Accept in Their Home","url":"https://arxiv.org/pdf/2204.04260"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conference on Robot Learning (@corl_conf) · X","url":"https://twitter.com/corl_conf"}]

Based on the search results, I found information about CoRL 2026's scope and topics, but I didn't find specific acceptance rate information for 2026. Here's what I found:

## Conference Scope and Topics

CoRL is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics. CoRL 2026 will be held in Austin, Texas, US.

CoRL welcomes papers in areas such as: learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, and applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics.

The conference also covers robot systems, hardware, and sensors for learning and data-driven approaches, as well as theoretical foundations of robot learning, including generalization theory and uncertainty quantification.

## Acceptance Rate

Unfortunately, the search results do not contain information about the acceptance rate specifically for CoRL 2026. The search results reference 671 submissions for a recent year of CoRL but don't provide the corresponding acceptance rate or final decision statistics for 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b75846fd-96f9-4616-a0d3-acfee34f06a8",
  "isSidechain": false,
  "promptId": "2ebf30b7-2d5d-4252-a445-b901c2ae9c31",
  "type": "user",
  "uuid": "a2ed8af3-2055-442d-8b35-491e4ee6394a",
  "toolUseResult": {
    "query": "CoRL 2026 conference on robot learning acceptance rate topics scope",
    "results": [
      {
        "tool_use_id": "srvtoolu_013ovwqNZkc4GSinrdDp3NFj",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "2025 Conference on Robot Learning - CoRL",
            "url": "https://www.corl.org/home"
          },
          {
            "title": "Conference on Robot Learning on X: \"#CoRL got 671 submissions this year. This is huge! See below for the development. 👇 (this number is already without obvious desk rejections) https://t.co/HfrSQ2ILyO\" / X",
            "url": "https://x.com/corl_conf/status/1801514565236076868"
          },
          {
            "title": "CoRL 2026 - About CoRL",
            "url": "https://www.corl.org/about-corl"
          },
          {
            "title": "GitHub - Po-Jen/Robotics-Conference-Acceptance-Rate: Statistics of acceptance rate for the main robotics conference · GitHub",
            "url": "https://github.com/Po-Jen/Robotics-Conference-Acceptance-Rate"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "Towards Cognitive Robots That People Accept in Their Home",
            "url": "https://arxiv.org/pdf/2204.04260"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) · X",
            "url": "https://twitter.com/corl_conf"
          }
        ]
      },
      "Based on the search results, I found information about CoRL 2026's scope and topics, but I didn't find specific acceptance rate information for 2026. Here's what I found:\n\n## Conference Scope and Topics\n\nCoRL is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics. CoRL 2026 will be held in Austin, Texas, US.\n\nCoRL welcomes papers in areas such as: learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, and applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics.\n\nThe conference also covers robot systems, hardware, and sensors for learning and data-driven approaches, as well as theoretical foundations of robot learning, including generalization theory and uncertainty quantification.\n\n## Acceptance Rate\n\nUnfortunately, the search results do not contain information about the acceptance rate specifically for CoRL 2026. The search results reference 671 submissions for a recent year of CoRL but don't provide the corresponding acceptance rate or final decision statistics for 2026."
    ],
    "durationSeconds": 7.437748301,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b75846fd-96f9-4616-a0d3-acfee34f06a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T03:25:35.615Z_

<details><summary>Logged reasoning block</summary>

```text
Wait - the user said this is for CoRL 2026 (Conference on Robot Learning). But the proposal is about conformal prediction for causal inference with LLM-extracted text confounders. This is fundamentally a statistics/causal inference/NLP paper, NOT a robotics paper. CoRL is a robotics conference. This is a critical mismatch.

Let me re-read the user's instructions: "评估其投稿 CoRL 2026 主会的中稿潜力" - they're asking about CoRL 2026 specifically.

But the proposal itself lists target venues as:


- AAAI 2027 (Primary)
- ARR August 2026 cycle → EACL 2027
- AISTATS 2027

None of these are CoRL. The proposal is about causal inference with text confounders extracted by LLMs - this is squarely an AI/ML statistics paper, not a robotics paper. CoRL focuses on robot learning: perception, control, manipulation, navigation, locomotion, driving, flight. This work on conformal prediction for causal inference from text data has essentially zero relevance to the CoRL community.

Even their theoretical foundations track is about robot learning theory, not general statistical methodology. This is a fundamental venue mismatch that would almost certainly result in a desk rejection. I need to flag this prominently.

Setting aside the venue issue, let me evaluate the core idea itself: combining modular conformal prediction with prediction-powered inference to handle sequential pipelines in causal inference.

The proposal does identify a real gap—existing conformal causal methods assume clean confounders while LLM+causal approaches only offer asymptotic guarantees. The combination of modular CP, conformal PPI, and causal inference is novel, though it's primarily stitching together existing frameworks. The technical novelty hinges on whether proving the modular residual decomposition under causal exchangeability conditions with doubly robust pseudo-outcomes is genuinely non-trivial, which the proposal doesn't detail enough to assess. The pilot conservatism analysis is a nice touch, but overall the novelty feels incremental.

I should also consider whether simpler alternatives would work just as well—like using bootstrap on LLM predictions, applying conformal prediction as a black box to the end-to-end pipeline, or leveraging standard measurement error correction methods from causal inference. The modular approach claims tighter bounds, but without empirical evidence that's hard to evaluate. The problem itself is important and timely given how common LLM-based confounder extraction has become, though the solution feels somewhat incremental.

The practical impact hinges on interval width, and the pilot results showing 60-100% widening for small conformal sets is concerning for real-world adoption. The paper sits at an interesting intersection of multiple active research areas, which could help it gain traction. The related work section demonstrates strong awareness of recent literature and clearly differentiates from prior work like Barnatchez et al.

That said, submitting this to CoRL would be a mistake—it has no connection to robotics or robot learning, and the proposal itself doesn't even list CoRL as a target venue. It would almost certainly face desk rejection there. Setting venue aside and evaluating the core idea, there's a genuine gap being addressed and the approach is technically sound, though the practical utility remains uncertain.

The main tension I'm seeing is that this feels like a "combining existing tools" paper rather than introducing fundamentally new methods. The theoretical contribution—showing that modular decomposition works under causal exchangeability—might be more of a natural consequence than a surprising insight. There's also the question of whether reviewers would find the result obvious once presented, plus the continuous embedding track is constrained to smooth nuisance estimators, and the overall proposal is dense enough that clarity in presentation could be challenging.

For a top-tier venue like AAAI or NeurIPS, I'd estimate this sits in the 25-35% range—the direction is sound and there's genuine novelty in the integration, but it's incremental rather than groundbreaking. For CoRL specifically, it's much weaker at 5-10% because the scope doesn't align well with the conference's focus. I'm also noticing the proposal targets AAAI 2027 and ARR August 2026 for EACL 2027, so there's a significant mismatch if the evaluation is meant for CoRL 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2ed8af3-2055-442d-8b35-491e4ee6394a",
  "isSidechain": false,
  "requestId": "req_011CbD77cpvvZ4rD6AJW9d7n",
  "type": "assistant",
  "uuid": "1dffdd88-7bf6-4021-b942-ae9d6fab9f4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJymZwnNXW9onQLstZt3TR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 29278,
      "output_tokens": 6940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6940,
          "cache_read_input_tokens": 29278,
          "cache_creation_input_tokens": 802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 802
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

_source line 40 · 2026-05-20T03:27:23.411Z_

Now I have sufficient research to make an informed assessment. Let me compile my analysis.

---

```
【阶段】: Triage

⚠️ 关键前置问题：严重的 VENUE MISMATCH ⚠️

本 proposal 被要求评估投稿 CoRL 2026（Conference on Robot Learning）的中稿潜力。
然而 CoRL 的核心 scope 是：robotic perception, control, manipulation, navigation, 
locomotion, driving, imitation learning, reinforcement learning for physical robots, 
robot foundation models 等。

本 proposal 是关于 conformal prediction + prediction-powered inference 用于 LLM
文本 confounder 提取后的因果推断——这是一篇纯粹的 统计方法论/因果推断/NLP 论文，
与机器人学习没有任何关联。proposal 自身列出的 target venues 也是 AAAI 2027、
ARR→EACL 2027、AISTATS 2027，均不包含 CoRL。

这篇论文投 CoRL 几乎必定 desk reject（scope 不匹配）。

以下评估将分两部分：(A) venue-agnostic 的 idea 质量评估，(B) CoRL 2026 特定概率。

═══════════════════════════════════════════════════
(A) VENUE-AGNOSTIC IDEA 质量评估（适用于 AAAI/AISTATS/NeurIPS 等）
═══════════════════════════════════════════════════

【领域调研】:
- Zhang et al. "Modular and Adaptive Conformal Prediction for Sequential Models 
  via Residual Decomposition" (arXiv 2510.04406, 2025): 本 proposal 的 Track A 
  核心基础。提出了 two-stage pipeline 的模块化 conformal prediction 框架，通过 
  residual decomposition 实现 stage-wise 不确定性归因。原文应用于 supply chain 
  和 stock market，未涉及因果推断。proposal 的贡献是将其扩展到 causal setting 
  with weighted exchangeability。
  
- Csillag et al. "Extending Prediction-Powered Inference through Conformal 
  Prediction" (arXiv 2510.16166, 2025): Track B 的核心基础。将 PPI 与 conformal 
  set-predictor 结合，实现 Z-estimation 和 M-estimation 的有效推断。原文是通用 
  统计框架，未专门处理因果推断场景。proposal 将其扩展到 ATE 估计。

- Barnatchez et al. "Debiased ML for Conformal Prediction of Counterfactual 
  Outcomes Under Runtime Confounding" (arXiv 2604.03772, April 2026): 最直接的
  竞争工作。但处理的是 confounders MISSING at deployment（缺失）而非 noisy 
  extraction（有噪声）。proposal 对此区分是清晰且成立的。

- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025): 将 PPI 扩展到
  因果场景，使用 conditional calibration。但未使用 conformal set-predictor。

- Kato "Semi-Supervised Treatment Effect Estimation" (arXiv 2511.08303, 
  NeurIPS 2025): 理论上建立了 semi-supervised setting 下 treatment effect 
  estimation 的 efficiency bounds。是 PPI+causal 方向的理论基础。

- DoubleLingo (NAACL 2024): 在 DML 框架内使用 LLM 做 nuisance estimation，
  仅提供渐近保证。

- Ma et al. "LLM-Driven Treatment Effect Estimation Under Inference Time Text 
  Confounding" (NeurIPS 2025): 处理 LLM 文本 confounding，但同样仅有渐近保证。

- Conformal Prediction for Medical Entity Extraction (arXiv 2603.00924, 2026): 
  将 conformal prediction 用于 LLM 医学实体提取，提供 FDR 保证。但仅处理
  extraction quality，未连接到下游因果推断。

- Gasparin & Ramdas "Improving Statistical Efficiency of Cross-Conformal 
  Prediction" (ICML 2025): proposal 用于减少 data split 的工具，是成熟技术。

- Singer et al. "Conformal Prediction for Astronomy Data with Measurement 
  Error" (MNRAS 2025): 唯一直接处理 measurement error + conformal prediction 
  的工作，但领域完全不同（天文学），且不涉及因果推断。

- 调研总结: 这个领域处于 conformal prediction × causal inference × LLM-based 
  text processing 三者交汇处，2025-2026 年各两两交叉都有活跃进展，但三者的
  完整统一（特别是 noisy extraction 而非 missing confounders）确实尚无直接先例。
  Proposal 的 gap identification 是准确的。

【Trivial Alternative 检验】:

存在两个需要认真回答的 trivial alternative 威胁：

1. **End-to-end black-box conformal prediction**: 不做模块化分解，直接对整个 
   pipeline（LLM extraction → causal estimation）做 black-box conformal 
   prediction。这会更简单，且同样提供 finite-sample 保证。Proposal 的增量价值
   在于：(a) 模块化分解可以 attribute uncertainty 到具体 stage，(b) 声称 FWER 
   控制比 Bonferroni 更 tight。但问题是：(a) 是 interpretability 收益（nice to 
   have 但非 essential），(b) 需要实验证明 tightness 提升有多大。如果 black-box 
   approach 的 interval 只宽 10-20%，模块化方法的复杂性就难以 justify。

2. **Standard measurement error correction + bootstrap**: 传统因果推断文献中
   有成熟的 measurement error correction 方法（SIMEX, regression calibration）。
   虽然这些是渐近方法，但配合 bootstrap 可能在实际中表现不差。proposal 声称 
   bootstrap "undercovers"，但这是需要实验验证的 claim，不是不证自明的。

增量价值结论：proposal 的真正增量在于 finite-sample guarantee 本身（vs 渐近
保证），以及对 noisy extraction 的 honest uncertainty quantification。但 trivial 
alternative 威胁是实质性的——必须在实验中展示 black-box CP 和 bootstrap 的 
interval 质量确实显著劣于模块化方法，否则 reviewers 会质疑复杂性是否 justified。

【前提假设检验】:

核心逻辑链中有以下未经验证的关键假设：

1. **"模块化 residual decomposition 在 causal exchangeability 条件下成立"** 
   —— 这是 proposal 声称的核心理论贡献，但 proposal 只说 "proving the modular 
   residual decomposition holds"，未给出证明思路或困难程度评估。Zhang et al. 
   (2025) 的原始 decomposition 假设标准 exchangeability，而 causal setting 
   需要 weighted exchangeability (Barber et al. 2023)。这个扩展是否 
   straightforward 还是 non-trivial，proposal 没有给出信号。如果证明是 trivial 
   的，理论贡献就很薄；如果证明是困难的，可能 10 周内无法完成。

2. **"Worst-case enumeration over conformal sets 产生的 conservatism 是可接受的"** 
   —— pilot analysis 显示 |C|=2 时 widening 60%，|C|=3 时 100%。这些数字是
   基于一个特定数值例子的 back-of-envelope 计算，不是一般性结果。实际数据中
   propensity score 分布和 outcome 函数形状可能导致更大或更小的 widening。
   关键假设是 "好的 LLM 通常能 achieve |C|≤2"，但这取决于 calibration 数据量
   和 LLM quality，在 clinical text 等困难场景中未必成立。

3. **"Conformal PPI 的 Z-estimation bound 在因果 setting 中不会过于 loose"** 
   —— Track B 的 ATE interval bound 包含 M·Err(C) 项，其中 M 是 influence 
   function 的 bounded range。在 doubly robust estimation 中，influence function 
   涉及 1/propensity score，如果 propensity 接近 0/1，M 可以很大，使得 
   bound 变得 vacuous。

4. **"连续 embedding track 的 ellipsoidal conformal sets + convex relaxation 
   在 128-256 维度是 tractable 且 meaningful 的"** —— 高维 conformal sets 
   体积随维度指数增长（curse of dimensionality），128-256 维的 ellipsoidal 
   sets 可能覆盖了 embedding space 的大部分，使 worst-case bounds trivially 
   wide。proposal 承认限制于 smooth nuisance estimators，但未分析维度对 
   interval width 的影响。

【3 维度打分】:

1. Novelty: 【中】
   理由：proposal 准确识别了一个真实存在的 gap——三个成熟子领域（modular CP, 
   conformal PPI, LLM-based causal inference）的交汇处确实没有被直接 addressed。
   与 Barnatchez et al. (2604.03772) 的区分（noisy vs. missing confounders）是
   清晰且有意义的。然而，核心方法论是 "将 Zhang et al. 2025 的框架 + Csillag 
   et al. 2025 的框架应用到 causal setting"——这是 combination novelty 而非 
   conceptual novelty。审稿人看到这篇论文时，反应更可能是 "yes, this combination 
   makes sense and someone should do it" 而不是 "this is a surprising insight I 
   wouldn't have thought of"。Singer et al. (MNRAS 2025) 已在天文学中处理了
   measurement error + CP 的组合（虽然不涉及因果推断），说明 "CP for noisy 
   covariates" 不是全新概念。Novelty 的实质深度取决于 weighted exchangeability 
   proof 的 non-triviality，但 proposal 未提供足够信息判断。

2. Significance: 【中偏强】
   理由：研究问题本身很重要——LLM-based confounder extraction 正在成为 text-based 
   causal inference 的标准实践（DoubleLingo NAACL 2024, Ma et al. NeurIPS 2025），
   而这些方法都缺乏 finite-sample guarantee。随着 LLM 在 clinical NLP 和 social 
   science 中的部署扩大，对 extraction noise 的 honest UQ 有明确需求。但 
   significance 受限于：(a) 实际用户群体较窄（做 text-based causal inference 的
   人本身就是小众），(b) interval widening 60-100% 可能让 practitioners 觉得
   方法 "too conservative to be useful"，(c) 如果核心发现是 "conformal methods 
   maintain coverage but with wider intervals"，这几乎是 by construction 的结论，
   不 surprising。

3. Related Work: 【强】
   理由：这是 proposal 最突出的优点。对近期文献（直到 2026 年 4-6 月）的覆盖非常
   全面，包括 Barnatchez et al. (April 2026), Vovk & Wang (March 2026), 
   Lützow et al. (2026), Gasparin & Ramdas (ICML 2025) 等非常新的工作。与
   最相关竞争工作的 differentiation 清晰且有说服力（特别是 noisy extraction 
   vs. missing confounders 的区分）。引用的论文经验证均真实存在且描述准确。
   Landscape section 对三个子领域的 gap 分析是系统性的。

═══════════════════════════════════════════════════
(B) CoRL 2026 特定评估
═══════════════════════════════════════════════════

CoRL (Conference on Robot Learning) 的 scope 是 robot learning：robotic 
perception, control, manipulation, navigation, locomotion, driving, flight, 
imitation learning, RL for physical robots, robot foundation models 等。

本 proposal 是关于 conformal prediction 用于 LLM 文本 confounder 提取后的
因果推断——与机器人学习没有任何实质性关联。proposal 自身的 target venues 
(AAAI 2027, ARR→EACL 2027, AISTATS 2027) 也不包含 CoRL。

即使忽略 scope 问题只看 idea 质量，这篇论文在 CoRL 也找不到合适的 reviewer——
该社区的审稿人不具备评审 causal inference + conformal prediction 理论贡献
的背景。

【概率估计 — CoRL 2026】: [1% - 5%] 中位 2%
【估计理由 — CoRL】: 
Scope 完全不匹配是 decisive factor。CoRL 关注 robot learning，本文是纯粹的
统计方法论/因果推断/NLP 工作。极高概率 desk reject。即使进入 review，reviewer 
pool 也不匹配，无法获得公正评审。1-5% 的非零下界仅反映 "AC 误判 scope" 的
极小概率。

【概率估计 — Venue-Agnostic（AAAI/AISTATS 级别会议）】: [20% - 35%] 中位 27%
【估计理由 — Venue-Agnostic】: 
Idea 的 novelty 是 combination-level（中），将两个现有框架 extend 到新 setting，
gap identification 准确但 "someone should do this" 性质明显。Significance 中偏强
（问题重要但用户群窄、interval widening 可能 limit 实际价值）。Related work 
coverage 强——这是最好的维度。上界受限于 novelty 维度：核心发现若 positive，
审稿人更可能说 "makes sense" 而非 "surprising"。下界由 significance 和 related 
work 支撑——问题真实、gap 确实存在、执行如果 solid 可以 pass。对于 AAAI/AISTATS 
这类会议，combination novelty + solid execution 可以中稿，但需要实验显著超越 
trivial alternatives。

【主要风险】:
1. **[Scope — CoRL 致命风险] 论文与 CoRL 的 scope 完全不匹配**，几乎必定 
   desk reject。这不是 idea 质量问题，而是 venue 选择错误。建议维持原定的 
   AAAI 2027 / AISTATS 2027 投稿计划。
   
2. **[Idea 层面 — Trivial Alternative 威胁] Black-box end-to-end conformal 
   prediction 可能以远低的复杂度达到类似效果**。如果模块化分解相比 black-box 
   CP 的 interval width 改善不显著（<15-20%），整个方法论复杂性的 justification 
   就会被审稿人质疑。这是实验无法完全补救的 idea 层面问题——如果 black-box 
   approach 效果相近，说明模块化分解在这个 application 中 value-add 有限。

3. **[Idea 层面 — Conservatism 可能使方法实际无用] 60-100% interval widening 
   在实际临床决策中可能被视为 too conservative**。如果主要实验结果是 "our method 
   has correct coverage but intervals are 2x wider than oracle"，reviewers 可能
   认为这是一个 "correct but useless" 的方法。
```

**总结**：这是一篇 idea 质量中等偏上的 combination paper，gap identification 准确，related work 覆盖优秀，但核心 novelty 是 framework integration 而非 conceptual breakthrough。**然而投稿 CoRL 2026 是严重的 venue mismatch**——CoRL 是机器人学习会议，本文是统计方法论/因果推断工作，几乎必定被 desk reject。强烈建议维持 proposal 自身原定的 target venues（AAAI 2027 / AISTATS 2027）。

Sources:
- [Modular and Adaptive Conformal Prediction for Sequential Models (Zhang et al. 2025)](https://arxiv.org/abs/2510.04406)
- [Extending Prediction-Powered Inference through Conformal Prediction (Csillag et al. 2025)](https://arxiv.org/abs/2510.16166)
- [Debiased ML for Conformal Prediction Under Runtime Confounding (Barnatchez et al. 2026)](https://arxiv.org/abs/2604.03772)
- [Prediction-Powered Causal Inferences (2025)](https://arxiv.org/abs/2502.06343)
- [Semi-Supervised Treatment Effect Estimation (Kato, NeurIPS 2025)](https://arxiv.org/abs/2511.08303)
- [Improving Statistical Efficiency of Cross-Conformal Prediction (Gasparin & Ramdas, ICML 2025)](https://arxiv.org/abs/2503.01495)
- [Systematic Review of Conformal Inference for Treatment Effects](https://arxiv.org/html/2509.21660)
- [DoubleLingo: Causal Estimation with LLMs (NAACL 2024)](https://aclanthology.org/2024.naacl-short.71/)
- [LLM-Driven Treatment Effect Estimation (Ma et al. NeurIPS 2025)](https://openreview.net/forum?id=sv41aaGTit)
- [Conformal Prediction for Astronomy with Measurement Error (MNRAS 2025)](https://arxiv.org/abs/2412.10544)
- [Conformal e-prediction under confounding (Vovk & Wang 2026)](https://arxiv.org/pdf/2603.11134)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)
- [Conformal Prediction for Medical Entity Extraction (2026)](https://arxiv.org/html/2603.00924)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dffdd88-7bf6-4021-b942-ae9d6fab9f4f",
  "isSidechain": false,
  "requestId": "req_011CbD77cpvvZ4rD6AJW9d7n",
  "type": "assistant",
  "uuid": "b49e9889-589e-4c54-aa25-397afb75e2a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJymZwnNXW9onQLstZt3TR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 29278,
      "output_tokens": 6940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6940,
          "cache_read_input_tokens": 29278,
          "cache_creation_input_tokens": 802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 802
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Descrip…",
  "leafUuid": "b49e9889-589e-4c54-aa25-397afb75e2a7",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Descrip…",
  "leafUuid": "b49e9889-589e-4c54-aa25-397afb75e2a7",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "055a2254-e260-4571-babf-fffde7c84db5"
}
```

---
