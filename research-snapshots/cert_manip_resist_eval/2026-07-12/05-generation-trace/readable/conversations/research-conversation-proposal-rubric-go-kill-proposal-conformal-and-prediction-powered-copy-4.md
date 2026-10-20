# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Conformal and Prediction-Powered 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd.jsonl`
- **Structured JSON:** [`b3cb15d0e9d6373305a5.json`](../../sessions/b3/b3cb15d0e9d6373305a5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:40:47.450Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:40:47.450Z",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders\n\n## Description\nWe propose ConformalPPITextCausal, a framework providing finite-sample coverage guarantees for treatment effects estimated using LLM-extracted text confounders. Current methods (DoubleLingo, Ma et al.) rely on asymptotic guarantees that break down when LLM extraction introduces unquantified heterogeneous noise. Our dual-track approach addresses this via: Track A (ITE intervals) — adapting modular conformal prediction (Zhang et al. 2025) to a causal two-stage pipeline where Stage 1 produces conformal prediction sets over LLM-extracted categorical confounders (with worst-case pseudo-outcome enumeration including explicit propensity score propagation, O(|C|) per unit) or low-dimensional Matryoshka embeddings (with ellipsoidal sets and convex relaxation restricted to smooth nuisance estimators), and Stage 2 constructs doubly robust treatment effect intervals with FWER-controlled coverage tighter than Bonferroni; Track B (ATE intervals) — extending conformal prediction-powered inference (Csillag et al. 2025) to the causal setting, where a small expert-labeled and large LLM-imputed dataset yield valid confidence intervals via Z-estimation with conformal set-predictors. Cross-conformal calibration (Gasparin & Ramdas, ICML 2025) reduces the three-way data split to two-way, improving sample efficiency for labeled-data-scarce settings. A pilot conservatism analysis shows practical viability: for K=5 confounder categories, interval widening is ~60% with conformal set size |C|=2 (good LLM) and ~100% with |C|=3 (decent LLM), driven primarily by propensity score variation across conformal set members. The method is practically useful when the LLM achieves small conformal sets and correctly signals insufficient information otherwise. We differentiate from Barnatchez et al. (2604.03772), who handle missing confounders at deployment via semiparametric debiasing — a complementary but distinct setting from our noisy-extraction framework. The genuine theoretical contribution is proving the modular residual decomposition holds under causal exchangeability conditions specific to doubly robust pseudo-outcomes with explicit propensity propagation. Experiments on semi-synthetic MIMIC-IV clinical notes, social media data, and synthetic benchmarks demonstrate maintained nominal coverage where bootstrap alternatives undercover, with a dedicated conservatism experiment varying |C|/K to validate the pilot analysis.\n\n## Core Problem\nCausal inference from observational text data (clinical notes, social media, policy documents) requires adjusting for confounders embedded in unstructured text. Modern LLMs can extract these confounders, but extraction is imperfect — introducing measurement error that invalidates standard causal estimators' asymptotic guarantees. No existing framework provides finite-sample coverage guarantees for treatment effect estimates when confounders are extracted by a fallible LLM. Naive approaches (plugging in LLM point predictions as if they were ground truth) can produce arbitrarily biased causal conclusions when extraction noise is heterogeneous across subpopulations.\n\n## Opportunity\nThree independent research threads have matured to the point where they can be unified into a principled solution: (1) modular conformal prediction for sequential pipelines (Zhang et al. 2025, arXiv 2510.04406) provides a residual decomposition framework that controls family-wise error across pipeline stages without resorting to loose Bonferroni corrections; (2) prediction-powered inference extended through conformal prediction (Csillag et al. 2025, arXiv 2510.16166) yields valid population-level confidence intervals when a prediction model (here, the LLM) imputes covariates on a large unlabeled set alongside a small human-labeled set; and (3) conformal meta-learners for individual treatment effects (Alaa et al. NeurIPS 2023) provide conformal intervals for heterogeneous effects but assume perfectly observed confounders. Additionally, Matryoshka embedding models (Qwen3-Embedding-8B) now support flexible dimensionality from 32 to 4096, making conformal prediction over embedding spaces tractable at reduced dimensions. Recent work on conformal prediction under confounding — including Barnatchez et al. (arXiv 2604.03772) on runtime confounding (missing confounders at deployment) and Vovk & Wang (arXiv 2603.11134) on conformal e-prediction — demonstrates growing interest but targets distinct problem settings from ours (noisy extraction vs. missing variables, and e-values for prediction vs. p-values for treatment effects). By bridging these threads, we can deliver both individual-level (ITE) and population-level (ATE) treatment effect intervals that honestly account for LLM extraction uncertainty — a capability no current method provides.\n\n## Landscape\nThe intersection of conformal prediction and causal inference has seen rapid growth (Systematic Review, arXiv 2509.21660, covering 11 key papers), but existing conformal ITE methods (Lei & Candès JRSS-B 2021; Alaa et al. NeurIPS 2023; KDD 2024 wTCP-DR) assume confounders are observed without error. The conformal prediction for NLP survey (Campos et al. TACL 2024) covers classification, QA, and generation quality but not downstream causal validity. Prediction-powered inference (Angelopoulos et al. Science 2023) and its causal extensions (arXiv 2502.06343; Kato arXiv 2511.08303 NeurIPS 2025) address the labeled/unlabeled split for treatment effects but do not incorporate conformal sets for the imputed covariates. Zhang et al. (2025) handle sequential model pipelines with modular conformal guarantees but do not treat the causal setting or weighted exchangeability. DoubleLingo (NAACL 2024) and Ma et al. (NeurIPS 2025) use LLMs within doubly robust causal estimators for text data but provide only asymptotic guarantees with no finite-sample uncertainty quantification for LLM extraction noise. Multi-variable conformal prediction (Lützow et al. arXiv 2605.12341, 2026) and ellipsoidal conformal sets (Xu et al. ICML 2024) now provide tractable geometric tools for moderate-dimensional conformal regions.\n\nTwo recent works merit explicit differentiation: Barnatchez et al. (arXiv 2604.03772, April 2026) address conformal prediction for counterfactual outcomes under 'runtime confounding' — where confounders measured in training are entirely MISSING at deployment. Their semiparametric debiasing approach marginalizes over unobserved confounders via multiply-robust influence functions, assuming Y(a)⊥S|V (systematic differences explained by the observed subset V). Our setting is fundamentally different: all confounders are present in the text and extracted by the LLM, but with NOISE — the confounders are measured with error, not missing entirely. Their debiasing marginalizes over missing variables; our conformal sets quantify extraction uncertainty over observed-but-noisy variables. Vovk & Wang (arXiv 2603.11134, March 2026) extend conformal e-prediction to handle observed confounding between X and Y using e-values (nonnegative random variables with expectation ≤ 1) rather than p-values. While e-values provide attractive anytime-valid guarantees under optional stopping, their framework targets prediction of Y given X under confounding, not treatment effect estimation. Our framework uses standard conformal prediction sets combined with PPI, targeting ITE/ATE estimation — a complementary but distinct goal. The e-value approach could be an interesting alternative foundation for future work.\n\nThe gap we fill is the integration of modular conformal prediction and conformal PPI into a unified framework for the two-stage pipeline of LLM confounder extraction followed by causal effect estimation, with proven finite-sample validity under noisy (not missing) confounder extraction.\n\n## Approach\nWe propose a dual-track framework, ConformalPPITextCausal, for valid causal inference when text confounders are extracted by an LLM.\n\n**Data Splitting and Sample Efficiency.** The baseline design uses a three-way data split: (S1) training data for fine-tuning the LLM extraction model and fitting nuisance functions (propensity score, outcome regression), (S2) calibration data for Stage 1 conformal sets on the extracted confounders, and (S3) calibration data for Stage 2 conformal intervals on treatment effects. To address sample efficiency — critical for clinical text datasets like MIMIC-IV where expert-labeled samples are expensive — we propose two improvements: (i) K-fold cross-fitting for nuisance function estimation within S1, following Chernozhukov et al. (2018) DML, which uses all training data for both estimation and evaluation; (ii) cross-conformal calibration for Stage 1, following Gasparin & Ramdas (ICML 2025, arXiv 2503.01495), which achieves coverage ≥ 1−2α₁ using K-fold rotation rather than a dedicated hold-out set, effectively merging S2 into S1 and reducing the three-way split to a two-way split (train+Stage1-calibrate vs. Stage2-calibrate). The coverage cost (1−2α₁ vs. 1−α₁) is manageable by setting α₁ conservatively (e.g., α₁=0.025 for effective 95% Stage 1 coverage). We discuss minimum sample size requirements: Stage 2 calibration requires n₃ ≥ ⌈1/α₂⌉ ≈ 100-200 for reliable conformal quantiles at α₂=0.05, and we recommend n_total ≥ 500 for the full pipeline, with n₃ ≥ 150 reserved for Stage 2. For very small labeled datasets (n < 300), Track B (PPI) is preferred as it leverages large unlabeled corpora.\n\n**Track A — Modular Conformal ITE Intervals.** We adapt the residual decomposition of Zhang et al. (2025), where the total prediction residual R decomposes as R ≤ ΔR₁ + R₂, with Stage 1 = LLM confounder extraction and Stage 2 = doubly robust pseudo-outcome estimation.\n\nIn the primary setting, the LLM extracts CATEGORICAL confounders (e.g., disease severity ∈ {mild, moderate, severe}, smoking status ∈ {never, former, current}) via prompted classification. Conformal prediction sets for classification are natural finite sets with guaranteed coverage.\n\n**Explicit Propensity Score Propagation.** The worst-case pseudo-outcome over the conformal set is computed by full enumeration with explicit propagation through BOTH the outcome regression AND the propensity score. For each possible confounder value c ∈ C(x), the DR pseudo-outcome is:\n\nφ̂(c; Yᵢ, Aᵢ) = [μ̂₁(c) − μ̂₀(c)] + Aᵢ·(Yᵢ − μ̂₁(c))/ê(c) − (1−Aᵢ)·(Yᵢ − μ̂₀(c))/(1−ê(c))\n\nCritically, different confounder values c yield different propensity scores ê(c), which enter the augmentation term as 1/ê(c) (for treated) or 1/(1−ê(c)) (for control). This propensity variation is a distinct and compounding source of uncertainty beyond outcome regression variation. The augmentation term amplifies when propensity scores are extreme: a confounder value with ê(c)=0.1 magnifies residuals 10×. The worst-case interval is [min_c φ̂(c), max_c φ̂(c)] with complexity O(|C|) per unit. We recommend propensity score trimming (truncating ê(c) to [0.05, 0.95]) to prevent a single extreme-propensity confounder value from dominating the interval.\n\n**Pilot Conservatism Analysis.** We provide a back-of-envelope quantification of interval widening due to worst-case enumeration. Consider a clinical setting with K=5 severity categories {none, mild, moderate, severe, critical} and realistic nuisance function values:\n\n| Category | μ̂₁(c) | μ̂₀(c) | ê(c) | CATE |\n|----------|--------|--------|-------|------|\n| none     | 0.40   | 0.30   | 0.50  | 0.10 |\n| mild     | 0.50   | 0.35   | 0.45  | 0.15 |\n| moderate | 0.60   | 0.40   | 0.40  | 0.20 |\n| severe   | 0.72   | 0.45   | 0.35  | 0.27 |\n| critical | 0.85   | 0.50   | 0.25  | 0.35 |\n\nFor a treated patient with Y=0.65 and true severity=moderate, the DR pseudo-outcomes across categories are: φ̂(none)=0.60, φ̂(mild)=0.48, φ̂(moderate)=0.33, φ̂(severe)=0.07, φ̂(critical)=−0.45. The variation is dominated by the augmentation term (Y−μ̂₁(c))/ê(c), where propensity changes from 0.50 to 0.25 amplify residuals 2×. The extraction uncertainty width (Δφ = max−min over C(x)) for different conformal set sizes:\n\n- |C|=1 (excellent LLM, singleton): Δφ=0, no widening vs. oracle.\n- |C|=2 (good LLM, e.g., {moderate, severe}): Δφ≈0.26, widening ≈ 60% over oracle CI width of ~0.40.\n- |C|=3 (decent LLM, e.g., {mild, moderate, severe}): Δφ≈0.41, widening ≈ 100% over oracle.\n- |C|=4+ (poor LLM): Δφ>1.0, intervals become vacuously wide — correctly reflecting that the LLM provides insufficient information for credible causal conclusions.\n\nThe general widening ratio is approximately W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle, where Δ_CATE is the CATE variation across the conformal set, |r| is the outcome residual magnitude, and Δ(1/ê) is the inverse propensity variation. Key practical determinants: (a) conformal set size |C|/K — the LLM quality directly controls conservatism; (b) propensity score stability across confounder categories — good overlap reduces widening; (c) outcome residual magnitude — well-fitted outcome models reduce augmentation-driven widening. The method is practically useful (W < 2) when the LLM achieves conformal set size |C| ≤ 2 for K=5 categories, and correctly signals 'insufficient information' otherwise.\n\nFor the secondary continuous track, we use Qwen3-Embedding-8B with Matryoshka dimensionality reduction to 128–256 dimensions, construct ellipsoidal conformal sets (Xu et al. ICML 2024; Lützow et al. 2026), and bound worst-case pseudo-outcomes via convex relaxation: local Lipschitz continuity of nuisance functions plus first-order Taylor expansion over the ellipsoid, following the decision-theoretic framework of Wang & Dobriban (arXiv 2602.00989, 2026). **Important restriction**: the convex relaxation via Lipschitz continuity and Taylor expansion requires smooth nuisance estimators. This is compatible with neural network outcome models (e.g., TARNet, DragonNet) and kernel methods, but NOT with tree-based models (gradient-boosted trees, random forests) that are piecewise constant with jump discontinuities. We therefore restrict the continuous embedding track to smooth nuisance estimators. Note that the categorical track (primary) works with ANY nuisance estimator, including tree-based methods, since worst-case computation is by direct enumeration without smoothness assumptions. The modular framework's FWER control across both stages yields provably tighter intervals than naive Bonferroni.\n\n**Track B — Conformal PPI for ATE Intervals.** We apply the conformal PPI framework of Csillag et al. (2025) to estimate average treatment effects. The LLM serves as the prediction model in the PPI sense: a small human-labeled dataset has expert-annotated confounders, and a large dataset has LLM-extracted confounders. The conformal set-predictor from Stage 1 replaces point imputation, yielding valid ATE confidence intervals via Z-estimation: E[inf φ(C(X))] − M·Err(C) ≤ ATE ≤ E[sup φ(C(X))] + M·Err(C), where M is the bounded range of the influence function and Err(C) is the conformal miscoverage rate. This extends PPI causal inference (arXiv 2502.06343) by using conformal rather than point imputation, providing finite-sample validity without distributional assumptions on the LLM. Track B is especially suited to small-labeled-data settings (MIMIC-IV) because it leverages large unlabeled corpora.\n\nWe evaluate on three benchmarks: (1) semi-synthetic MIMIC-IV clinical notes (treatment escalation effect on ICU outcomes, disease severity as text confounder), (2) semi-synthetic social media data (content moderation effect on engagement, toxicity level as confounder), and (3) fully synthetic data with known ground-truth for calibration validation. Key metrics: empirical coverage at 90%/95% nominal levels, interval width relative to oracle (perfectly observed confounders) and bootstrap baselines, widening ratio W as a function of conformal set size and propensity overlap, and sensitivity to LLM extraction quality via deliberately degraded models. We include a dedicated conservatism experiment varying |C|/K from 0.2 to 0.8 to empirically validate the pilot analysis above.\n\nWe are transparent that worst-case reasoning over conformal sets introduces conservatism relative to oracle methods. The honest framing: our intervals maintain nominal coverage where bootstrap intervals undercover due to LLM extraction noise, with comparable width when LLM quality is high (|C|=1-2). The conservatism correctly reflects true uncertainty in the LLM-as-measurement-instrument setting, and the pilot analysis above shows it is quantifiably bounded for reasonable LLM quality.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '200-300', 'timeline': '10 weeks (targeting AAAI 2027 July 28 deadline)', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'breakdown': 'Weeks 1-2: Formalize theoretical framework (modular decomposition under weighted exchangeability, conformal PPI ATE estimator, cross-conformal Stage 1 calibration). Weeks 3-4: Implement cross-fitted pipeline, categorical conformal extraction, worst-case enumeration with explicit propensity propagation. Weeks 5-6: Implement continuous embedding track (Matryoshka 128-256d, ellipsoidal sets, convex relaxation with smooth nuisance estimators) and PPI ATE track. Weeks 7-8: Experiments on MIMIC-IV, social media, synthetic benchmarks including conservatism analysis. Week 9: Ablations (LLM quality sensitivity via |C|/K sweep, propensity overlap analysis, embedding dimension, calibration set size, cross-conformal vs. split comparison). Week 10: Paper writing and proof polishing.'}, 'human_in_loop': {'gpu_hours': '200-300', 'timeline': '8 weeks', 'claude_api_cost': '$100-150', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'notes': 'AI assists with literature integration, boilerplate code, proof sketch verification. Human focuses on theoretical contributions (weighted exchangeability conditions, tight bounds for DR pseudo-outcomes, propensity propagation analysis) and experimental design. Requires ~5 hours domain expert time for confounder annotation guidelines.'}, 'auto_research': {'gpu_hours': '250-350', 'timeline': '5-6 weeks', 'claude_api_cost': '$250-350', 'estimated_gpu_cost': '$375-525 (A100 at ~$1.50/hr)', 'speed_bottleneck': 'Theoretical proof verification requires human mathematician; three-way split calibration across multiple seeds requires sequential experiment iterations; domain expert annotation for MIMIC-IV confounder labels cannot be automated'}}\n\n## Inspired By\nGap: Existing conformal causal methods assume error-free confounders; existing LLM conformal methods ignore causal settings; existing text-based causal methods provide only asymptotic guarantees; Barnatchez et al. handle missing confounders but not noisy extraction; Vovk & Wang handle confounding in prediction but not treatment effects. Pattern: Three converging literatures (modular CP, conformal PPI, conformal causal inference) that have not been connected. Key enablers: Zhang et al. (arXiv 2510.04406) modular residual decomposition framework; Csillag et al. (arXiv 2510.16166) conformal set-predictor for PPI; Alaa et al. (NeurIPS 2023) conformal meta-learners for ITE; Barber et al. (Annals of Statistics 2023) weighted exchangeability beyond standard CP assumptions.\n\n## Target Venues\n- AAAI 2027 (Primary — abstract July 21, full paper July 28, 2026; ~10 weeks from today)\n- ARR August 2026 cycle (Secondary — submission August 3, 2026) → EACL 2027 (commitment October 11, 2026)\n- AISTATS 2027 (Stretch — estimated deadline ~October 2026, not yet announced)\n\n## Key References\n- Zhang et al. 'Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition' (arXiv 2510.04406, 2025)\n- Csillag et al. 'Extending Prediction-Powered Inference through Conformal Prediction' (arXiv 2510.16166, 2025)\n- Angelopoulos et al. 'Prediction-Powered Inference' (Science, 2023)\n- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025)\n- Kato 'Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression' (arXiv 2511.08303, NeurIPS 2025)\n- Barber et al. 'Conformal prediction beyond exchangeability' (Annals of Statistics, 2023)\n- Alaa et al. 'Conformal Meta-learners for Predictive Inference of Individual Treatment Effects' (NeurIPS 2023)\n- Wang & Dobriban 'Optimal Decision-Making Based on Prediction Sets' (arXiv 2602.00989, 2026)\n- Lützow et al. 'Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting' (arXiv 2605.12341, 2026)\n- Xu et al. 'Conformal prediction for multi-dimensional time series by ellipsoidal sets' (ICML 2024)\n- Campos et al. 'Conformal Prediction for Natural Language Processing: A Survey' (TACL, 2024)\n- Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation (arXiv 2509.21660, 2025)\n- Lei & Candès 'Conformal Inference of Counterfactuals and Individual Treatment Effects' (JRSS-B, 2021)\n- DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)\n- Ma et al. 'LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding' (NeurIPS 2025)\n- Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)\n- Veitch et al. 'Adapting Text Embeddings for Causal Inference' (UAI 2020)\n- Barnatchez et al. 'Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding' (arXiv 2604.03772, 2026)\n- Vovk & Wang 'Conformal e-prediction in the presence of confounding' (arXiv 2603.11134, 2026)\n- Gasparin & Ramdas 'Improving the statistical efficiency of cross-conformal prediction' (arXiv 2503.01495, ICML 2025)\n- Chernozhukov et al. 'Double/debiased machine learning for treatment and structural parameters' (Econometrics Journal, 2018)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:40:47.467Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:40:47.467Z",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-20T03:40:47.712Z_

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
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "ba62a2b6-3e3d-4d94-9943-bce30c419952",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:40:47.705Z_

```json
{
  "parentUuid": "ba62a2b6-3e3d-4d94-9943-bce30c419952",
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
  "uuid": "2cf491f2-c2dd-4188-ab8b-4887ea75eb00",
  "timestamp": "2026-05-20T03:40:47.705Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:40:47.705Z_

```json
{
  "parentUuid": "2cf491f2-c2dd-4188-ab8b-4887ea75eb00",
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
  "uuid": "45f81248-9695-4281-a10d-8864f436a7b9",
  "timestamp": "2026-05-20T03:40:47.705Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T03:40:47.705Z_

```json
{
  "parentUuid": "45f81248-9695-4281-a10d-8864f436a7b9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1513a877-2376-441c-ae44-4126e90a67b3",
  "timestamp": "2026-05-20T03:40:47.705Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
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
  "leafUuid": "1513a877-2376-441c-ae44-4126e90a67b3",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted causal confounders",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

### Assistant

_source line 9 · 2026-05-20T03:40:54.707Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed proposal for "Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders." I need to evaluate its idea quality for EMNLP 2026 submission potential.

Let me first do the required web searches to understand the current landscape before making any judgments.

Let me search for:
1. Recent work on conformal prediction + causal inference + LLMs
2. The key papers cited (Zhang et al. 2025, Csillag et al. 2025)
3. DoubleLingo and Ma et al. NeurIPS 2025


4. Barnatchez et al. 2026 and the broader landscape of LLM-based causal inference from text

I'll launch these searches now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1513a877-2376-441c-ae44-4126e90a67b3",
  "isSidechain": false,
  "requestId": "req_011CbD8KzZbDZGMmjsJGWnxv",
  "type": "assistant",
  "uuid": "57b19a33-75a5-4fc7-9703-636619c1959b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUgh41eLSmYjkiEZKSAzSZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11026,
      "cache_read_input_tokens": 10980,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 304,
          "cache_read_input_tokens": 10980,
          "cache_creation_input_tokens": 11026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11026
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

_source line 10 · 2026-05-20T03:40:54.835Z_

I need to do thorough web research before evaluating this proposal. Let me search for the key papers and the current landscape in this area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57b19a33-75a5-4fc7-9703-636619c1959b",
  "isSidechain": false,
  "requestId": "req_011CbD8KzZbDZGMmjsJGWnxv",
  "type": "assistant",
  "uuid": "bfb23491-24ce-472d-919b-24bf5527baec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUgh41eLSmYjkiEZKSAzSZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11026,
      "cache_read_input_tokens": 10980,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 304,
          "cache_read_input_tokens": 10980,
          "cache_creation_input_tokens": 11026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11026
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

_source line 11 · 2026-05-20T03:40:55.129Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014baYk7KuJQkgh9Zj3GLLwj`</summary>

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
  "parentUuid": "bfb23491-24ce-472d-919b-24bf5527baec",
  "isSidechain": false,
  "requestId": "req_011CbD8KzZbDZGMmjsJGWnxv",
  "type": "assistant",
  "uuid": "cb14e23d-c31e-488f-8cb4-4e3dff30d212",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUgh41eLSmYjkiEZKSAzSZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11026,
      "cache_read_input_tokens": 10980,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11026,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 304,
          "cache_read_input_tokens": 10980,
          "cache_creation_input_tokens": 11026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11026
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

_source line 12 · 2026-05-20T03:40:55.136Z_

<details><summary>↩ Tool result · `toolu_014baYk7KuJQkgh9Zj3GLLwj`</summary>

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
  "parentUuid": "cb14e23d-c31e-488f-8cb4-4e3dff30d212",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "ded28224-11dc-48ed-ac20-664cfc105bb7",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "cb14e23d-c31e-488f-8cb4-4e3dff30d212",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T03:40:57.857Z_

Now let me launch multiple searches in parallel to understand the landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ded28224-11dc-48ed-ac20-664cfc105bb7",
  "isSidechain": false,
  "requestId": "req_011CbD8LXiLMzqSngcwFqtKt",
  "type": "assistant",
  "uuid": "71a7a04e-61bb-4def-a405-7d5700adc3a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyL1hNBZDAbimht63Ujfbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 22006,
      "output_tokens": 252,
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
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 22006,
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

### Tool call

_source line 14 · 2026-05-20T03:40:57.863Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EqSAitGMLvg6UoXsNQVjAF`</summary>

```json
{
  "query": "conformal prediction causal inference LLM text confounders 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71a7a04e-61bb-4def-a405-7d5700adc3a7",
  "isSidechain": false,
  "requestId": "req_011CbD8LXiLMzqSngcwFqtKt",
  "type": "assistant",
  "uuid": "01cf322b-7b84-4988-b5d0-ab021ac308a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyL1hNBZDAbimht63Ujfbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 22006,
      "output_tokens": 252,
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
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 22006,
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

### Tool call

_source line 15 · 2026-05-20T03:40:58.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gc2NHGtT35pkNT2BaLFhH7`</summary>

```json
{
  "query": "DoubleLingo causal estimation large language models NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01cf322b-7b84-4988-b5d0-ab021ac308a4",
  "isSidechain": false,
  "requestId": "req_011CbD8LXiLMzqSngcwFqtKt",
  "type": "assistant",
  "uuid": "2ad2ca1e-c901-418f-8abd-6012108a5a4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyL1hNBZDAbimht63Ujfbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 22006,
      "output_tokens": 252,
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
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 22006,
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

### Tool call

_source line 16 · 2026-05-20T03:40:59.274Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PxFpYXemMQGMBSUGh3owKX`</summary>

```json
{
  "query": "Zhang et al modular conformal prediction sequential models residual decomposition arXiv 2510.04406"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ad2ca1e-c901-418f-8abd-6012108a5a4e",
  "isSidechain": false,
  "requestId": "req_011CbD8LXiLMzqSngcwFqtKt",
  "type": "assistant",
  "uuid": "9b087464-7c6c-4c78-b00c-aa0ead4e9a7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyL1hNBZDAbimht63Ujfbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 22006,
      "output_tokens": 252,
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
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 22006,
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

### Tool call

_source line 17 · 2026-05-20T03:40:59.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ew1o3JzJdUXyB3dzpiTcsY`</summary>

```json
{
  "query": "Csillag et al prediction-powered inference conformal prediction arXiv 2510.16166 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b087464-7c6c-4c78-b00c-aa0ead4e9a7c",
  "isSidechain": false,
  "requestId": "req_011CbD8LXiLMzqSngcwFqtKt",
  "type": "assistant",
  "uuid": "bc2e6020-560a-42d7-90ed-0d3105eb089e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyL1hNBZDAbimht63Ujfbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 22006,
      "output_tokens": 252,
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
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 22006,
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

_source line 18 · 2026-05-20T03:41:04.075Z_

<details><summary>↩ Tool result · `toolu_01Gc2NHGtT35pkNT2BaLFhH7`</summary>

```text
Web search results for query: "DoubleLingo causal estimation large language models NAACL 2024"

Links: [{"title":"DoubleLingo: Causal Estimation with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-short.71/"},{"title":"DoubleLingo: Causal Estimation with Large Language ...","url":"https://aclanthology.org/2024.naacl-short.71.pdf"},{"title":"DoubleLingo: Causal Estimation with Large Language Models","url":"https://openreview.net/pdf?id=4eYtU3qOO0"},{"title":"[Quick Review] Causal Inference with Large Language Model: A Survey","url":"https://liner.com/review/causal-inference-with-large-language-model-survey"},{"title":"Optimizing Prompts for Large Language Models: A Causal Approach","url":"https://arxiv.org/pdf/2602.01711"},{"title":"Prompting or Fine-tuning? Exploring Large Language Models for Causal   Graph Validation","url":"https://arxiv.org/pdf/2406.16899"},{"title":"Understanding Causality with Large Language Models: Feasibility and   Opportunities","url":"https://arxiv.org/pdf/2304.05524"}]

Based on the search results, I found information about the DoubleLingo paper:

DoubleLingo: Causal Estimation with Large Language Models was published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL), as a short paper in Mexico City.

The paper addresses the problem that simple statistical models have sufficient convergence criteria for causal estimation but aren't equipped to handle noisy unstructured text, while flexible large language models excel at predictive tasks with text but don't meet statistical assumptions necessary for causal estimation. The method enables theoretically consistent estimation of causal effects using LLM-based nuisance models by incorporating them within the framework of Double Machine Learning.

On the best available dataset for evaluating such methods, the paper obtains a 10.4% reduction in the relative absolute error for the estimated causal effect over existing methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ad2ca1e-c901-418f-8abd-6012108a5a4e",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "92644bb1-65c6-4731-8263-8a17e0f77e11",
  "toolUseResult": {
    "query": "DoubleLingo causal estimation large language models NAACL 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EqDBLa6jw8K34o62D8V6H5",
        "content": [
          {
            "title": "DoubleLingo: Causal Estimation with Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-short.71/"
          },
          {
            "title": "DoubleLingo: Causal Estimation with Large Language ...",
            "url": "https://aclanthology.org/2024.naacl-short.71.pdf"
          },
          {
            "title": "DoubleLingo: Causal Estimation with Large Language Models",
            "url": "https://openreview.net/pdf?id=4eYtU3qOO0"
          },
          {
            "title": "[Quick Review] Causal Inference with Large Language Model: A Survey",
            "url": "https://liner.com/review/causal-inference-with-large-language-model-survey"
          },
          {
            "title": "Optimizing Prompts for Large Language Models: A Causal Approach",
            "url": "https://arxiv.org/pdf/2602.01711"
          },
          {
            "title": "Prompting or Fine-tuning? Exploring Large Language Models for Causal   Graph Validation",
            "url": "https://arxiv.org/pdf/2406.16899"
          },
          {
            "title": "Understanding Causality with Large Language Models: Feasibility and   Opportunities",
            "url": "https://arxiv.org/pdf/2304.05524"
          }
        ]
      },
      "Based on the search results, I found information about the DoubleLingo paper:\n\nDoubleLingo: Causal Estimation with Large Language Models was published in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL), as a short paper in Mexico City.\n\nThe paper addresses the problem that simple statistical models have sufficient convergence criteria for causal estimation but aren't equipped to handle noisy unstructured text, while flexible large language models excel at predictive tasks with text but don't meet statistical assumptions necessary for causal estimation. The method enables theoretically consistent estimation of causal effects using LLM-based nuisance models by incorporating them within the framework of Double Machine Learning.\n\nOn the best available dataset for evaluating such methods, the paper obtains a 10.4% reduction in the relative absolute error for the estimated causal effect over existing methods."
    ],
    "durationSeconds": 5.731734822999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2ad2ca1e-c901-418f-8abd-6012108a5a4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T03:41:04.291Z_

<details><summary>↩ Tool result · `toolu_01PxFpYXemMQGMBSUGh3owKX`</summary>

```text
Web search results for query: "Zhang et al modular conformal prediction sequential models residual decomposition arXiv 2510.04406"

Links: [{"title":"[2510.04406] Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/abs/2510.04406"},{"title":"[2510.04406v1] Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/abs/2510.04406v1"},{"title":"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/html/2510.04406v1"},{"title":"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/pdf/2510.04406"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/stat.ML/2025-10?skip=25&show=25"}]

I found the paper! Here are the search results for arXiv 2510.04406:

**Title:** Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition

**Authors:** William Zhang, Saurabh Amin, and Georgia Perakis from Massachusetts Institute of Technology

**Key Contributions:**

The paper introduces a conformal prediction framework for two-stage sequential models, where an upstream predictor generates intermediate representations for a downstream model. By decomposing the overall prediction residual into stage-specific components, the method enables practitioners to attribute uncertainty to specific pipeline stages.

The authors develop a risk-controlled parameter selection procedure using family-wise error rate (FWER) control to calibrate stage-wise scaling parameters, and propose an adaptive extension for non-stationary settings that preserves long-run coverage guarantees.

**Applications:** Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that their approach maintains coverage under conditions that degrade standard conformal methods.

The paper was published on October 6-7, 2025, and consists of 11 pages with 37 pages including the appendix.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b087464-7c6c-4c78-b00c-aa0ead4e9a7c",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "ec90d430-6c78-46fe-9d69-7c113c18cf4f",
  "toolUseResult": {
    "query": "Zhang et al modular conformal prediction sequential models residual decomposition arXiv 2510.04406",
    "results": [
      {
        "tool_use_id": "srvtoolu_019XQ2NykKdoLsq5GcL4RxYM",
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
            "url": "https://arxiv.org/html/2510.04406v1"
          },
          {
            "title": "Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition",
            "url": "https://arxiv.org/pdf/2510.04406"
          },
          {
            "title": "Machine Learning Oct 2025",
            "url": "https://arxiv.org/list/stat.ML/2025-10?skip=25&show=25"
          }
        ]
      },
      "I found the paper! Here are the search results for arXiv 2510.04406:\n\n**Title:** Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition\n\n**Authors:** William Zhang, Saurabh Amin, and Georgia Perakis from Massachusetts Institute of Technology\n\n**Key Contributions:**\n\nThe paper introduces a conformal prediction framework for two-stage sequential models, where an upstream predictor generates intermediate representations for a downstream model. By decomposing the overall prediction residual into stage-specific components, the method enables practitioners to attribute uncertainty to specific pipeline stages.\n\nThe authors develop a risk-controlled parameter selection procedure using family-wise error rate (FWER) control to calibrate stage-wise scaling parameters, and propose an adaptive extension for non-stationary settings that preserves long-run coverage guarantees.\n\n**Applications:** Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that their approach maintains coverage under conditions that degrade standard conformal methods.\n\nThe paper was published on October 6-7, 2025, and consists of 11 pages with 37 pages including the appendix."
    ],
    "durationSeconds": 5.013883727999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9b087464-7c6c-4c78-b00c-aa0ead4e9a7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T03:41:05.409Z_

<details><summary>↩ Tool result · `toolu_01EqSAitGMLvg6UoXsNQVjAF`</summary>

```text
Web search results for query: "conformal prediction causal inference LLM text confounders 2025 2026"

Links: [{"title":"arXiv:2507.02928v1 [cs.CL] 26 Jun 2025","url":"https://arxiv.org/pdf/2507.02928"},{"title":"Conformal Counterfactual Inference under Hidden Confounding | Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining","url":"https://dl.acm.org/doi/10.1145/3637528.3671976"},{"title":"Do LLMs Act as Repositories of Causal Knowledge?","url":"https://arxiv.org/pdf/2412.10635"},{"title":"Conformal e-prediction in the presence of confounding","url":"https://arxiv.org/pdf/2603.11134"},{"title":"Using LLMs to Directly Guess Conditional Expectations Can Improve Efficiency in Causal Estimation","url":"https://arxiv.org/pdf/2510.09684"},{"title":"Causal Representation Learning with Generative Artificial Intelligence: Application to Texts as Treatments","url":"https://arxiv.org/pdf/2410.00903"}]

I found several relevant research papers on this topic. Here's what the search revealed:

## Key Research Areas

**LLMs for Confounder Generation in Causal Inference:**
Recent work uses LLMs to generate missing confounders and impute their individual-level values for causal treatment effect estimation, leveraging semantic and world knowledge in variable generation and value imputation.

**Conformal Prediction with Hidden Confounding:**
A novel approach called wTCP-DR (weighted transductive conformal prediction) provides confidence intervals for counterfactual outcomes with marginal coverage guarantees, even under hidden confounding.

**Conformal e-prediction in Causal Inference:**
Recent work extends conformal e-prediction to cover cases with observed confounding, applying conformal e-prediction to causal inference prediction problems in order to obtain finite-sample guarantees of validity.

**LLMs for Improving Causal Estimation:**
In double machine learning, predictions made by generative models can improve the performance of conditional expectation function estimators relative to approaches that solely rely on adjusting for embeddings.

**Text as Treatment in Causal Inference:**
Large language models can be used to efficiently generate treatments and their internal representations can help disentangle treatment features of interest from confounding features.

**Limitations of LLMs for Causal Knowledge:**
LLM judgment on confounder status is highly inconsistent across models and prompts, and LLMs do not yet have the ability to automate reliable reporting of causal links.

The search results include papers from 2025-2026, showing active recent research in this intersection of conformal prediction, causal inference, and LLM applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01cf322b-7b84-4988-b5d0-ab021ac308a4",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "17651c7e-77c6-4f5e-a2be-68214909a606",
  "toolUseResult": {
    "query": "conformal prediction causal inference LLM text confounders 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ci66KR2cCd2i11F8vW54ZL",
        "content": [
          {
            "title": "arXiv:2507.02928v1 [cs.CL] 26 Jun 2025",
            "url": "https://arxiv.org/pdf/2507.02928"
          },
          {
            "title": "Conformal Counterfactual Inference under Hidden Confounding | Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining",
            "url": "https://dl.acm.org/doi/10.1145/3637528.3671976"
          },
          {
            "title": "Do LLMs Act as Repositories of Causal Knowledge?",
            "url": "https://arxiv.org/pdf/2412.10635"
          },
          {
            "title": "Conformal e-prediction in the presence of confounding",
            "url": "https://arxiv.org/pdf/2603.11134"
          },
          {
            "title": "Using LLMs to Directly Guess Conditional Expectations Can Improve Efficiency in Causal Estimation",
            "url": "https://arxiv.org/pdf/2510.09684"
          },
          {
            "title": "Causal Representation Learning with Generative Artificial Intelligence: Application to Texts as Treatments",
            "url": "https://arxiv.org/pdf/2410.00903"
          }
        ]
      },
      "I found several relevant research papers on this topic. Here's what the search revealed:\n\n## Key Research Areas\n\n**LLMs for Confounder Generation in Causal Inference:**\nRecent work uses LLMs to generate missing confounders and impute their individual-level values for causal treatment effect estimation, leveraging semantic and world knowledge in variable generation and value imputation.\n\n**Conformal Prediction with Hidden Confounding:**\nA novel approach called wTCP-DR (weighted transductive conformal prediction) provides confidence intervals for counterfactual outcomes with marginal coverage guarantees, even under hidden confounding.\n\n**Conformal e-prediction in Causal Inference:**\nRecent work extends conformal e-prediction to cover cases with observed confounding, applying conformal e-prediction to causal inference prediction problems in order to obtain finite-sample guarantees of validity.\n\n**LLMs for Improving Causal Estimation:**\nIn double machine learning, predictions made by generative models can improve the performance of conditional expectation function estimators relative to approaches that solely rely on adjusting for embeddings.\n\n**Text as Treatment in Causal Inference:**\nLarge language models can be used to efficiently generate treatments and their internal representations can help disentangle treatment features of interest from confounding features.\n\n**Limitations of LLMs for Causal Knowledge:**\nLLM judgment on confounder status is highly inconsistent across models and prompts, and LLMs do not yet have the ability to automate reliable reporting of causal links.\n\nThe search results include papers from 2025-2026, showing active recent research in this intersection of conformal prediction, causal inference, and LLM applications."
    ],
    "durationSeconds": 7.542068080999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "01cf322b-7b84-4988-b5d0-ab021ac308a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T03:41:06.541Z_

<details><summary>↩ Tool result · `toolu_01Ew1o3JzJdUXyB3dzpiTcsY`</summary>

```text
Web search results for query: "Csillag et al prediction-powered inference conformal prediction arXiv 2510.16166 2025"

Links: [{"title":"[2510.16166] Extending Prediction-Powered Inference through Conformal Prediction","url":"https://arxiv.org/abs/2510.16166"},{"title":"Extending Prediction-Powered Inference through Conformal Prediction","url":"https://arxiv.org/html/2510.16166v1"},{"title":"Published as a preprint EXTENDING PREDICTION-POWERED INFERENCE","url":"https://arxiv.org/pdf/2510.16166"},{"title":"Powerful batch conformal prediction for classification","url":"https://arxiv.org/pdf/2411.02239"},{"title":"Post-selection Inference for Conformal Prediction: Trading off Coverage   for Precision","url":"https://arxiv.org/pdf/2304.06158"}]

Based on the search results, I found the paper you're looking for:

The paper "Extending Prediction-Powered Inference through Conformal Prediction" was submitted on October 17, 2025, with authors Daniel Csillag, Pedro Dall'Antonia, Claudio José Struchiner, and Guilherme Tegoni Goedert.

**Overview:**

The paper addresses prediction-powered inference, which is a methodology for the safe use of black-box ML models to impute missing data and strengthen inference of statistical parameters. 

**Key Contribution:**

The authors resolve the issue of adding strong properties to prediction-powered inference by connecting it with conformal prediction, using calibrated conformal set-predictors to attain validity while achieving additional guarantees.

**Applications:**

The procedure is instantiated for the inference of means, Z- and M-estimation, as well as e-values and e-value-based procedures, with the first general prediction-powered procedure that operates off-line in the case of e-values.

**Additional Guarantees:**

The approach allows leveraging the conformal prediction literature with additional guarantees spanning privacy, robustness to strategic and adversarial distribution shift, continuous distribution shift, robustness to outliers, and censored/missing data.

You can access the full paper at https://arxiv.org/abs/2510.16166.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc2e6020-560a-42d7-90ed-0d3105eb089e",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "49a3d38d-54d9-425b-ba5a-5f6bd1c18ee9",
  "toolUseResult": {
    "query": "Csillag et al prediction-powered inference conformal prediction arXiv 2510.16166 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VWBLD6JJWU5dsXEbcb67hL",
        "content": [
          {
            "title": "[2510.16166] Extending Prediction-Powered Inference through Conformal Prediction",
            "url": "https://arxiv.org/abs/2510.16166"
          },
          {
            "title": "Extending Prediction-Powered Inference through Conformal Prediction",
            "url": "https://arxiv.org/html/2510.16166v1"
          },
          {
            "title": "Published as a preprint EXTENDING PREDICTION-POWERED INFERENCE",
            "url": "https://arxiv.org/pdf/2510.16166"
          },
          {
            "title": "Powerful batch conformal prediction for classification",
            "url": "https://arxiv.org/pdf/2411.02239"
          },
          {
            "title": "Post-selection Inference for Conformal Prediction: Trading off Coverage   for Precision",
            "url": "https://arxiv.org/pdf/2304.06158"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Extending Prediction-Powered Inference through Conformal Prediction\" was submitted on October 17, 2025, with authors Daniel Csillag, Pedro Dall'Antonia, Claudio José Struchiner, and Guilherme Tegoni Goedert.\n\n**Overview:**\n\nThe paper addresses prediction-powered inference, which is a methodology for the safe use of black-box ML models to impute missing data and strengthen inference of statistical parameters. \n\n**Key Contribution:**\n\nThe authors resolve the issue of adding strong properties to prediction-powered inference by connecting it with conformal prediction, using calibrated conformal set-predictors to attain validity while achieving additional guarantees.\n\n**Applications:**\n\nThe procedure is instantiated for the inference of means, Z- and M-estimation, as well as e-values and e-value-based procedures, with the first general prediction-powered procedure that operates off-line in the case of e-values.\n\n**Additional Guarantees:**\n\nThe approach allows leveraging the conformal prediction literature with additional guarantees spanning privacy, robustness to strategic and adversarial distribution shift, continuous distribution shift, robustness to outliers, and censored/missing data.\n\nYou can access the full paper at https://arxiv.org/abs/2510.16166."
    ],
    "durationSeconds": 7.142150235999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bc2e6020-560a-42d7-90ed-0d3105eb089e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
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
  "leafUuid": "49a3d38d-54d9-425b-ba5a-5f6bd1c18ee9",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted causal confounders",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

### Assistant

_source line 24 · 2026-05-20T03:41:09.132Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed the key papers exist. Let me now search for more specific competitors and the most recent works.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49a3d38d-54d9-425b-ba5a-5f6bd1c18ee9",
  "isSidechain": false,
  "requestId": "req_011CbD8MNKZGh5Gqs978GkJs",
  "type": "assistant",
  "uuid": "3e61b271-b39a-4a23-bffb-323a40d289a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDnshe5GnHXn3wxiCAhRh7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2698,
      "cache_read_input_tokens": 22837,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 22837,
          "cache_creation_input_tokens": 2698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2698
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

_source line 25 · 2026-05-20T03:41:09.133Z_

Good, the key papers are confirmed. Let me search for more specific competitors and recent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e61b271-b39a-4a23-bffb-323a40d289a3",
  "isSidechain": false,
  "requestId": "req_011CbD8MNKZGh5Gqs978GkJs",
  "type": "assistant",
  "uuid": "9015dfb2-edd2-4582-b635-70d20b64c547",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDnshe5GnHXn3wxiCAhRh7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2698,
      "cache_read_input_tokens": 22837,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 22837,
          "cache_creation_input_tokens": 2698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2698
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

_source line 26 · 2026-05-20T03:41:10.080Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0117UCZ3PMuhXF61xYCPas1t`</summary>

```json
{
  "query": "Ma et al \"LLM-Driven Treatment Effect Estimation\" text confounding NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9015dfb2-edd2-4582-b635-70d20b64c547",
  "isSidechain": false,
  "requestId": "req_011CbD8MNKZGh5Gqs978GkJs",
  "type": "assistant",
  "uuid": "2fee118e-d7c2-48fd-a0ad-fa94ced815c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDnshe5GnHXn3wxiCAhRh7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2698,
      "cache_read_input_tokens": 22837,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 22837,
          "cache_creation_input_tokens": 2698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2698
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

_source line 27 · 2026-05-20T03:41:10.544Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C3UA248eekswjuNCZd5FDk`</summary>

```json
{
  "query": "Barnatchez \"conformal prediction counterfactual outcomes runtime confounding\" arXiv 2604.03772 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fee118e-d7c2-48fd-a0ad-fa94ced815c9",
  "isSidechain": false,
  "requestId": "req_011CbD8MNKZGh5Gqs978GkJs",
  "type": "assistant",
  "uuid": "53578172-f008-4bc6-874d-322ff6281a19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDnshe5GnHXn3wxiCAhRh7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2698,
      "cache_read_input_tokens": 22837,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 22837,
          "cache_creation_input_tokens": 2698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2698
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

_source line 28 · 2026-05-20T03:41:10.984Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014B495uQh19R12n9d74WtgE`</summary>

```json
{
  "query": "prediction-powered inference causal inference treatment effects 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53578172-f008-4bc6-874d-322ff6281a19",
  "isSidechain": false,
  "requestId": "req_011CbD8MNKZGh5Gqs978GkJs",
  "type": "assistant",
  "uuid": "358cd5a0-30c5-495b-9f20-c18487ddce36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDnshe5GnHXn3wxiCAhRh7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2698,
      "cache_read_input_tokens": 22837,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 22837,
          "cache_creation_input_tokens": 2698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2698
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

_source line 29 · 2026-05-20T03:41:17.277Z_

<details><summary>↩ Tool result · `toolu_01C3UA248eekswjuNCZd5FDk`</summary>

```text
Web search results for query: "Barnatchez "conformal prediction counterfactual outcomes runtime confounding" arXiv 2604.03772 2026"

Links: [{"title":"[2604.03772] Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/abs/2604.03772"},{"title":"[2604.03772v1] Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/abs/2604.03772v1"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/html/2604.03772"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/pdf/2604.03772"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding - AI Research Paper Analysis | ArxivLens - Arxivlens","url":"https://arxivlens.com/PaperView/Details/debiased-machine-learning-for-conformal-prediction-of-counterfactual-outcomes-under-runtime-confounding-3519-d149b03f"}]

I found the paper you're looking for. Here are the key details:

**Title:** Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding

**Authors:** Keith Barnatchez, Kevin P. Josey, Rachel C. Nethery, Giovanni Parmigiani

**arXiv ID:** 2604.03772

**Publication Date:** April 4, 2026

**Summary:** Conformal prediction has arisen as a popular method for producing assumption-lean prediction intervals for counterfactual outcomes that would arise under different treatment decisions in the target population of interest. However, existing methods require that every confounding factor of the treatment-outcome relationship used for training on the source data is additionally measured in the target population, risking miscoverage if important confounders are unmeasured in the target population. 

The paper's main contribution is that the authors introduce a computationally efficient debiased machine learning framework that allows for valid prediction intervals when only a subset of confounders is measured in the target population, a common challenge referred to as runtime confounding.

The paper is available on arXiv at https://arxiv.org/abs/2604.03772


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53578172-f008-4bc6-874d-322ff6281a19",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "405d2edf-17ae-41ed-a99d-0d21b321a4bb",
  "toolUseResult": {
    "query": "Barnatchez \"conformal prediction counterfactual outcomes runtime confounding\" arXiv 2604.03772 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RfwiU1onhxATzrGtGmAbyg",
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
      "I found the paper you're looking for. Here are the key details:\n\n**Title:** Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding\n\n**Authors:** Keith Barnatchez, Kevin P. Josey, Rachel C. Nethery, Giovanni Parmigiani\n\n**arXiv ID:** 2604.03772\n\n**Publication Date:** April 4, 2026\n\n**Summary:** Conformal prediction has arisen as a popular method for producing assumption-lean prediction intervals for counterfactual outcomes that would arise under different treatment decisions in the target population of interest. However, existing methods require that every confounding factor of the treatment-outcome relationship used for training on the source data is additionally measured in the target population, risking miscoverage if important confounders are unmeasured in the target population. \n\nThe paper's main contribution is that the authors introduce a computationally efficient debiased machine learning framework that allows for valid prediction intervals when only a subset of confounders is measured in the target population, a common challenge referred to as runtime confounding.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2604.03772"
    ],
    "durationSeconds": 6.730085110000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "53578172-f008-4bc6-874d-322ff6281a19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T03:41:17.484Z_

<details><summary>↩ Tool result · `toolu_0117UCZ3PMuhXF61xYCPas1t`</summary>

```text
Web search results for query: "Ma et al "LLM-Driven Treatment Effect Estimation" text confounding NeurIPS 2025"

Links: [{"title":"[2507.02843] LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://arxiv.org/abs/2507.02843"},{"title":"[2507.02843v1] LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"http://arxiv.org/abs/2507.02843v1"},{"title":"Estimating Causal Effects of Text Interventions Leveraging LLMs","url":"https://arxiv.org/html/2410.21474"},{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding | OpenReview","url":"https://openreview.net/forum?id=sv41aaGTit"},{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://arxiv.org/pdf/2507.02843"},{"title":"[Literature Review] LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://www.themoonlight.io/en/review/llm-driven-treatment-effect-estimation-under-inference-time-text-confounding"},{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://openreview.net/pdf/91cde9dca622c2cb85a4f93a3342a05cadeed265.pdf"}]

I found the paper you're looking for! Here are the key details about this research:

**Paper Title:** LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding

**Authors:** Yuchen Ma, Dennis Frauen, Jonas Schweisthal & Stefan Feuerriegel from Munich Center for Machine Learning LMU Munich

**Conference/Venue:** NeurIPS 2025 poster

**Main Contribution:** The paper formalizes an inference time text confounding problem, where confounders are fully observed during training time but only partially available through text at inference time.

**The Problem:** At training time, models for estimating treatment effects are typically trained on well-structured medical datasets that contain detailed patient information. However, at inference time, predictions are often made using textual descriptions (e.g., descriptions with self-reported symptoms), which are incomplete representations of the original patient information.

**The Solution:** The paper proposes a novel framework for estimating treatment effects that explicitly accounts for inference time text confounding, leveraging large language models together with a custom doubly robust learner to mitigate biases caused by the inference time text confounding.

**Availability:** The paper is available on arXiv as arXiv preprint arXiv:2507.02843


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fee118e-d7c2-48fd-a0ad-fa94ced815c9",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "35541339-8772-4db9-9f57-dafd5eb13261",
  "toolUseResult": {
    "query": "Ma et al \"LLM-Driven Treatment Effect Estimation\" text confounding NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kz3XVMBDznoRuC9nF59R5o",
        "content": [
          {
            "title": "[2507.02843] LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://arxiv.org/abs/2507.02843"
          },
          {
            "title": "[2507.02843v1] LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "http://arxiv.org/abs/2507.02843v1"
          },
          {
            "title": "Estimating Causal Effects of Text Interventions Leveraging LLMs",
            "url": "https://arxiv.org/html/2410.21474"
          },
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding | OpenReview",
            "url": "https://openreview.net/forum?id=sv41aaGTit"
          },
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://arxiv.org/pdf/2507.02843"
          },
          {
            "title": "[Literature Review] LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://www.themoonlight.io/en/review/llm-driven-treatment-effect-estimation-under-inference-time-text-confounding"
          },
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://openreview.net/pdf/91cde9dca622c2cb85a4f93a3342a05cadeed265.pdf"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about this research:\n\n**Paper Title:** LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding\n\n**Authors:** Yuchen Ma, Dennis Frauen, Jonas Schweisthal & Stefan Feuerriegel from Munich Center for Machine Learning LMU Munich\n\n**Conference/Venue:** NeurIPS 2025 poster\n\n**Main Contribution:** The paper formalizes an inference time text confounding problem, where confounders are fully observed during training time but only partially available through text at inference time.\n\n**The Problem:** At training time, models for estimating treatment effects are typically trained on well-structured medical datasets that contain detailed patient information. However, at inference time, predictions are often made using textual descriptions (e.g., descriptions with self-reported symptoms), which are incomplete representations of the original patient information.\n\n**The Solution:** The paper proposes a novel framework for estimating treatment effects that explicitly accounts for inference time text confounding, leveraging large language models together with a custom doubly robust learner to mitigate biases caused by the inference time text confounding.\n\n**Availability:** The paper is available on arXiv as arXiv preprint arXiv:2507.02843"
    ],
    "durationSeconds": 7.399939161999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2fee118e-d7c2-48fd-a0ad-fa94ced815c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T03:41:18.019Z_

<details><summary>↩ Tool result · `toolu_014B495uQh19R12n9d74WtgE`</summary>

```text
Web search results for query: "prediction-powered inference causal inference treatment effects 2025 2026"

Links: [{"title":"[2502.06343] Prediction-Powered Causal Inferences","url":"https://arxiv.org/abs/2502.06343"},{"title":"NeurIPS Poster Prediction-Powered Causal Inferences","url":"https://neurips.cc/virtual/2025/poster/118896"},{"title":"Prediction-powered Generalization of Causal Inferences","url":"https://arxiv.org/html/2406.02873v1"},{"title":"Prediction-powered inference for clinical trials: application to linear covariate adjustment - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12395788/"},{"title":"Prediction-powered generalization of causal inferences | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692483"},{"title":"Prediction-powered Generalization of Causal Inferences","url":"https://arxiv.org/pdf/2406.02873"},{"title":"Foundation Models for Causal Inference via Prior-Data ...","url":"https://arxiv.org/pdf/2506.10914"}]

Based on the search results, here's what I found about prediction-powered inference and causal inference treatment effects in 2025-2026:

## Recent Research on Prediction-Powered Causal Inference

Prediction-Powered Causal Inferences (PPCI) focuses on estimating treatment effects in unlabeled target experiments, relying on training data with the same outcome annotated but potentially different treatment or effect modifiers.

In many scientific experiments, data annotation costs constrain the pace for testing novel hypotheses, but modern machine learning pipelines offer a promising solution, provided their predictions yield correct conclusions.

### Recent Applications

Prediction-powered inference (PPI) and its development called PPI++ provide a novel approach to statistical estimation, leveraging machine learning systems to enhance unlabeled data with predictions, which has been applied in clinical trials. The proposed method would empower clinical trials by providing untreated digital twins of treated patients while remaining statistically valid.

### Generalization of Causal Effects

Combining trial data with potentially biased observational data, such as from electronic health records, can power better generalization, with generalization algorithms supplementing trial data with prediction models learned from additional observational studies.

A recent paper on this topic was presented at NeurIPS in December 2025, and updates to foundational work were made as recently as October 2025, indicating this is an actively developing research area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "358cd5a0-30c5-495b-9f20-c18487ddce36",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "ca9df21b-1e57-441d-9e02-739cf445ae1e",
  "toolUseResult": {
    "query": "prediction-powered inference causal inference treatment effects 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TKcT361bikDCXWFUPVtJA8",
        "content": [
          {
            "title": "[2502.06343] Prediction-Powered Causal Inferences",
            "url": "https://arxiv.org/abs/2502.06343"
          },
          {
            "title": "NeurIPS Poster Prediction-Powered Causal Inferences",
            "url": "https://neurips.cc/virtual/2025/poster/118896"
          },
          {
            "title": "Prediction-powered Generalization of Causal Inferences",
            "url": "https://arxiv.org/html/2406.02873v1"
          },
          {
            "title": "Prediction-powered inference for clinical trials: application to linear covariate adjustment - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12395788/"
          },
          {
            "title": "Prediction-powered generalization of causal inferences | Proceedings of the 41st International Conference on Machine Learning",
            "url": "https://dl.acm.org/doi/10.5555/3692070.3692483"
          },
          {
            "title": "Prediction-powered Generalization of Causal Inferences",
            "url": "https://arxiv.org/pdf/2406.02873"
          },
          {
            "title": "Foundation Models for Causal Inference via Prior-Data ...",
            "url": "https://arxiv.org/pdf/2506.10914"
          }
        ]
      },
      "Based on the search results, here's what I found about prediction-powered inference and causal inference treatment effects in 2025-2026:\n\n## Recent Research on Prediction-Powered Causal Inference\n\nPrediction-Powered Causal Inferences (PPCI) focuses on estimating treatment effects in unlabeled target experiments, relying on training data with the same outcome annotated but potentially different treatment or effect modifiers.\n\nIn many scientific experiments, data annotation costs constrain the pace for testing novel hypotheses, but modern machine learning pipelines offer a promising solution, provided their predictions yield correct conclusions.\n\n### Recent Applications\n\nPrediction-powered inference (PPI) and its development called PPI++ provide a novel approach to statistical estimation, leveraging machine learning systems to enhance unlabeled data with predictions, which has been applied in clinical trials. The proposed method would empower clinical trials by providing untreated digital twins of treated patients while remaining statistically valid.\n\n### Generalization of Causal Effects\n\nCombining trial data with potentially biased observational data, such as from electronic health records, can power better generalization, with generalization algorithms supplementing trial data with prediction models learned from additional observational studies.\n\nA recent paper on this topic was presented at NeurIPS in December 2025, and updates to foundational work were made as recently as October 2025, indicating this is an actively developing research area."
    ],
    "durationSeconds": 7.032661522999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "358cd5a0-30c5-495b-9f20-c18487ddce36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-20T03:41:18.025Z_

```json
{
  "parentUuid": "ca9df21b-1e57-441d-9e02-739cf445ae1e",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8a83888f-a9b1-408f-9343-00436469c2df",
  "timestamp": "2026-05-20T03:41:18.025Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-20T03:41:22.154Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me search for a few more things to complete my understanding:
1. Whether there's already existing work that specifically combines conformal prediction with LLM-extracted confounders for causal inference
2. The Kato NeurIPS 2025 paper on semi-supervised treatment effects
3. Any very recent work (2026) that might directly compete
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a83888f-a9b1-408f-9343-00436469c2df",
  "isSidechain": false,
  "requestId": "req_011CbD8NDMLg7Kki5WVP3dak",
  "type": "assistant",
  "uuid": "9cbd548a-511a-47ee-bf80-c312df5196e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JsvJ7FkmU5mUiDkyPc6DU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2403,
      "cache_read_input_tokens": 25535,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 25535,
          "cache_creation_input_tokens": 2403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2403
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

_source line 34 · 2026-05-20T03:41:22.633Z_

Let me do a couple more targeted searches to complete the landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cbd548a-511a-47ee-bf80-c312df5196e0",
  "isSidechain": false,
  "requestId": "req_011CbD8NDMLg7Kki5WVP3dak",
  "type": "assistant",
  "uuid": "55c0d5b9-80d1-492d-a8cc-b30116acac08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JsvJ7FkmU5mUiDkyPc6DU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2403,
      "cache_read_input_tokens": 25535,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 25535,
          "cache_creation_input_tokens": 2403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2403
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

_source line 35 · 2026-05-20T03:41:23.642Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WxwaVu1TkN9aoscbq59JLg`</summary>

```json
{
  "query": "finite-sample coverage guarantees treatment effects measurement error confounders conformal 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55c0d5b9-80d1-492d-a8cc-b30116acac08",
  "isSidechain": false,
  "requestId": "req_011CbD8NDMLg7Kki5WVP3dak",
  "type": "assistant",
  "uuid": "8d31c51f-bd6c-437e-a464-c92c4bdee69e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JsvJ7FkmU5mUiDkyPc6DU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2403,
      "cache_read_input_tokens": 25535,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 25535,
          "cache_creation_input_tokens": 2403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2403
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

_source line 36 · 2026-05-20T03:41:24.349Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LM2xHqdTLUBN9JwJVKTb8g`</summary>

```json
{
  "query": "Kato \"semi-supervised treatment effect\" unlabeled covariates Riesz regression arXiv 2511.08303 NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d31c51f-bd6c-437e-a464-c92c4bdee69e",
  "isSidechain": false,
  "requestId": "req_011CbD8NDMLg7Kki5WVP3dak",
  "type": "assistant",
  "uuid": "f9604612-3ad8-48ff-9bc2-3ba15ddab78b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JsvJ7FkmU5mUiDkyPc6DU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2403,
      "cache_read_input_tokens": 25535,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2403,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 25535,
          "cache_creation_input_tokens": 2403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2403
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

_source line 37 · 2026-05-20T03:41:32.892Z_

<details><summary>↩ Tool result · `toolu_01WxwaVu1TkN9aoscbq59JLg`</summary>

```text
Web search results for query: "finite-sample coverage guarantees treatment effects measurement error confounders conformal 2025 2026"

Links: [{"title":"[2509.21660] A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation: Methods and Challenges","url":"https://arxiv.org/abs/2509.21660"},{"title":"Probabilistic Conformal Coverage Guarantees in Small-Data Settings","url":"https://arxiv.org/html/2509.15349"},{"title":"A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation: Methods and Challenges","url":"https://arxiv.org/html/2509.21660v1"},{"title":"Conformal Inference of Counterfactuals and Individual Treatment Effects","url":"https://arxiv.org/pdf/2006.06138"},{"title":"Conformal prediction intervals for the individual treatment effect","url":"https://arxiv.org/pdf/2006.01474"},{"title":"(PDF) Conformal Prediction for Causal Effects of Continuous Treatments","url":"https://www.researchgate.net/publication/381960657_Conformal_Prediction_for_Causal_Effects_of_Continuous_Treatments"},{"title":"Conformal Prediction for Continuous Treatments","url":"https://www.emergentmind.com/papers/2407.03094"},{"title":"CONFIDE: CONformal Free Inference for Distribution-Free Estimation in Causal Competing Risks","url":"https://www.mdpi.com/2227-7390/14/2/383"},{"title":"Conformal Convolution and Monte Carlo Meta-learners for Predictive Inference of Individual Treatment Effects","url":"https://arxiv.org/pdf/2402.04906"}]

I found several highly relevant research papers on finite-sample coverage guarantees for treatment effect estimation with conformal prediction. Here's what the search revealed:

## Key Recent Developments (2025-2026)

Recent advancements in conformal prediction provide frequentist, finite-sample coverage guarantees under minimal assumptions for any point-predictor model, while allowing for distribution shifts.

A systematic review on conformal prediction methods for treatment effect estimation was published in September 2025, providing necessary theoretical background.

## Treatment Effects and Measurement Issues

Naive conformal prediction intervals for treatment effects become marginally invalid and lose their finite-sample coverage guarantees, necessitating methodological adaptations that explicitly account for distributional differences between treated and untreated units.

For randomized experiments with perfect compliance, intervals have guaranteed average coverage in finite samples regardless of the unknown data generating mechanism. For observational studies under strong ignorability assumptions, intervals satisfy a doubly robust property where average coverage is approximately controlled if either the propensity score or the conditional quantiles of potential outcomes can be estimated accurately.

## Continuous Treatments and Propensity Estimation

Recent work provides novel conformal prediction methods for potential outcomes of continuous treatments while accounting for the additional uncertainty introduced through propensity estimation, ensuring validity even if the propensity score is unknown.

## Very Recent 2026 Work

A January 2026 paper introduces CONFIDE, a framework that bridges causal inference and conformal prediction to construct valid prediction sets for cause-specific cumulative incidence functions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d31c51f-bd6c-437e-a464-c92c4bdee69e",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "67060621-83a6-478d-90d2-41ad92471033",
  "toolUseResult": {
    "query": "finite-sample coverage guarantees treatment effects measurement error confounders conformal 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PZMeNhiXUDVMZBTVrgAKhm",
        "content": [
          {
            "title": "[2509.21660] A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation: Methods and Challenges",
            "url": "https://arxiv.org/abs/2509.21660"
          },
          {
            "title": "Probabilistic Conformal Coverage Guarantees in Small-Data Settings",
            "url": "https://arxiv.org/html/2509.15349"
          },
          {
            "title": "A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation: Methods and Challenges",
            "url": "https://arxiv.org/html/2509.21660v1"
          },
          {
            "title": "Conformal Inference of Counterfactuals and Individual Treatment Effects",
            "url": "https://arxiv.org/pdf/2006.06138"
          },
          {
            "title": "Conformal prediction intervals for the individual treatment effect",
            "url": "https://arxiv.org/pdf/2006.01474"
          },
          {
            "title": "(PDF) Conformal Prediction for Causal Effects of Continuous Treatments",
            "url": "https://www.researchgate.net/publication/381960657_Conformal_Prediction_for_Causal_Effects_of_Continuous_Treatments"
          },
          {
            "title": "Conformal Prediction for Continuous Treatments",
            "url": "https://www.emergentmind.com/papers/2407.03094"
          },
          {
            "title": "CONFIDE: CONformal Free Inference for Distribution-Free Estimation in Causal Competing Risks",
            "url": "https://www.mdpi.com/2227-7390/14/2/383"
          },
          {
            "title": "Conformal Convolution and Monte Carlo Meta-learners for Predictive Inference of Individual Treatment Effects",
            "url": "https://arxiv.org/pdf/2402.04906"
          }
        ]
      },
      "I found several highly relevant research papers on finite-sample coverage guarantees for treatment effect estimation with conformal prediction. Here's what the search revealed:\n\n## Key Recent Developments (2025-2026)\n\nRecent advancements in conformal prediction provide frequentist, finite-sample coverage guarantees under minimal assumptions for any point-predictor model, while allowing for distribution shifts.\n\nA systematic review on conformal prediction methods for treatment effect estimation was published in September 2025, providing necessary theoretical background.\n\n## Treatment Effects and Measurement Issues\n\nNaive conformal prediction intervals for treatment effects become marginally invalid and lose their finite-sample coverage guarantees, necessitating methodological adaptations that explicitly account for distributional differences between treated and untreated units.\n\nFor randomized experiments with perfect compliance, intervals have guaranteed average coverage in finite samples regardless of the unknown data generating mechanism. For observational studies under strong ignorability assumptions, intervals satisfy a doubly robust property where average coverage is approximately controlled if either the propensity score or the conditional quantiles of potential outcomes can be estimated accurately.\n\n## Continuous Treatments and Propensity Estimation\n\nRecent work provides novel conformal prediction methods for potential outcomes of continuous treatments while accounting for the additional uncertainty introduced through propensity estimation, ensuring validity even if the propensity score is unknown.\n\n## Very Recent 2026 Work\n\nA January 2026 paper introduces CONFIDE, a framework that bridges causal inference and conformal prediction to construct valid prediction sets for cause-specific cumulative incidence functions."
    ],
    "durationSeconds": 9.245699118000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8d31c51f-bd6c-437e-a464-c92c4bdee69e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Descrip…",
  "leafUuid": "67060621-83a6-478d-90d2-41ad92471033",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted causal confounders",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

### Tool result

_source line 40 · 2026-05-20T03:41:33.769Z_

<details><summary>↩ Tool result · `toolu_01LM2xHqdTLUBN9JwJVKTb8g`</summary>

```text
Web search results for query: "Kato "semi-supervised treatment effect" unlabeled covariates Riesz regression arXiv 2511.08303 NeurIPS 2025"

Links: [{"title":"[2511.08303] Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression","url":"https://arxiv.org/abs/2511.08303"},{"title":"(PDF) Don't Forget Its Variance! The Minimum Path ...","url":"https://arxiv.org/pdf/2602.00834"},{"title":"Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates for Prediction-Powered Causal Inference","url":"https://arxiv.org/html/2511.08303"},{"title":"Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression","url":"https://arxiv.org/html/2511.08303v1"},{"title":"Riesz Regression As Direct Density Ratio Estimation","url":"https://arxiv.org/html/2511.04568v1"},{"title":"[2511.04568v1] Riesz Regression As Direct Density Ratio Estimation","url":"https://arxiv.org/abs/2511.04568v1"},{"title":"[2511.04568] Riesz Regression As Direct Density Ratio Estimation","url":"https://arxiv.org/abs/2511.04568"}]

I found the paper you're looking for. Here's what I found:

## Paper Details

The paper investigates treatment effect estimation in the semi-supervised setting, where one can use not only the standard triple of covariates, treatment indicator, and outcome, but also unlabeled auxiliary covariates.

**Key Contributions:**

The study develops efficiency bounds and efficient estimators whose asymptotic variance aligns with the efficiency bound. The analysis introduces two different data-generating processes: the one-sample setting (censoring setting) where treatment indicators and outcomes are observed for part of the dataset, and the two-sample setting (case-control or stratified setting) with two independent datasets of labeled and unlabeled data.

By incorporating auxiliary covariates, the efficiency bound can be lowered and an estimator with an asymptotic variance smaller than that without auxiliary covariates can be obtained.

**Methodological Approach:**

The paper employs generalized Riesz regression, which generalizes the Riesz regression in Chernozhukov et al. (2021), and further extends it to the semi-supervised setting.

The paper arXiv:2511.08303 was posted on November 11, 2025, and appears to be authored by Masahiro Kato.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9604612-3ad8-48ff-9bc2-3ba15ddab78b",
  "isSidechain": false,
  "promptId": "9f6e0ede-5b25-497f-a8b0-bb9d7a50a74f",
  "type": "user",
  "uuid": "1f6cf52e-e964-4458-9396-532c93215c9f",
  "toolUseResult": {
    "query": "Kato \"semi-supervised treatment effect\" unlabeled covariates Riesz regression arXiv 2511.08303 NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TobJrTvyU4jTgH5aDG3RSd",
        "content": [
          {
            "title": "[2511.08303] Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression",
            "url": "https://arxiv.org/abs/2511.08303"
          },
          {
            "title": "(PDF) Don't Forget Its Variance! The Minimum Path ...",
            "url": "https://arxiv.org/pdf/2602.00834"
          },
          {
            "title": "Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates for Prediction-Powered Causal Inference",
            "url": "https://arxiv.org/html/2511.08303"
          },
          {
            "title": "Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression",
            "url": "https://arxiv.org/html/2511.08303v1"
          },
          {
            "title": "Riesz Regression As Direct Density Ratio Estimation",
            "url": "https://arxiv.org/html/2511.04568v1"
          },
          {
            "title": "[2511.04568v1] Riesz Regression As Direct Density Ratio Estimation",
            "url": "https://arxiv.org/abs/2511.04568v1"
          },
          {
            "title": "[2511.04568] Riesz Regression As Direct Density Ratio Estimation",
            "url": "https://arxiv.org/abs/2511.04568"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I found:\n\n## Paper Details\n\nThe paper investigates treatment effect estimation in the semi-supervised setting, where one can use not only the standard triple of covariates, treatment indicator, and outcome, but also unlabeled auxiliary covariates.\n\n**Key Contributions:**\n\nThe study develops efficiency bounds and efficient estimators whose asymptotic variance aligns with the efficiency bound. The analysis introduces two different data-generating processes: the one-sample setting (censoring setting) where treatment indicators and outcomes are observed for part of the dataset, and the two-sample setting (case-control or stratified setting) with two independent datasets of labeled and unlabeled data.\n\nBy incorporating auxiliary covariates, the efficiency bound can be lowered and an estimator with an asymptotic variance smaller than that without auxiliary covariates can be obtained.\n\n**Methodological Approach:**\n\nThe paper employs generalized Riesz regression, which generalizes the Riesz regression in Chernozhukov et al. (2021), and further extends it to the semi-supervised setting.\n\nThe paper arXiv:2511.08303 was posted on November 11, 2025, and appears to be authored by Masahiro Kato."
    ],
    "durationSeconds": 9.417232653,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f9604612-3ad8-48ff-9bc2-3ba15ddab78b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T03:42:23.562Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of the landscape. Let me synthesize my understanding and provide the evaluation.

Let me think about this proposal carefully:

**What the proposal does:**
The proposal combines three threads:
1. Modular conformal prediction (Zhang et al. 2025) for sequential pipelines
2. Prediction-powered inference with conformal prediction (Csillag et al. 2025)
3. Conformal meta-learners for ITE (Alaa et al. NeurIPS 2023)

Into a framework that provides finite-sample coverage guarantees for treatment effects when confounders are extracted by LLMs from text.


The key insight is that existing approaches like DoubleLingo only guarantee coverage asymptotically, whereas this framework achieves finite-sample guarantees by maintaining conformal prediction sets throughout the causal pipeline and explicitly tracking how uncertainty in LLM-extracted confounders propagates through propensity score estimation. The genuine novelty lies in this specific combination of modular conformal prediction with causal inference on LLM-extracted features, plus the technical contribution of proving that modular residual decomposition holds under causal exchangeability.

That said, this is fundamentally assembling three existing pieces—modular conformal prediction for sequential pipelines, conformal PPI, and conformal ITE—with LLM-based confounder extraction. The integration is legitimate but not groundbreaking, and the worst-case enumeration over conformal sets follows straightforwardly from the framework. I'm wondering whether a simpler bootstrap or Bayesian approach to quantifying LLM extraction noise would suffice in practice, since the paper acknowledges bootstrap undercoverage but doesn't clearly establish how large the gap between bootstrap and conformal coverage actually is empirically.

The stronger argument is that finite-sample guarantees are the whole point here—this is a methodological paper about principled uncertainty quantification, not just chasing empirical performance. But I'm also noticing some shaky foundational assumptions: the exchangeability requirement for conformal prediction is quite strong in observational text settings where LLM extraction patterns might vary systematically across subpopulations, and the framing assumes LLM extraction noise is the main error source when unmeasured confounders in the text itself could be the bigger problem.

The categorical confounder track is solid, but the continuous embedding approach with Lipschitz smoothness feels restrictive and might not generalize well in practice. On the positive side, the problem itself matters—as LLMs get used more in text-based causal work, having principled coverage guarantees is genuinely valuable, and the dual-track analysis with honest guidance on when the method actually helps is a strength. The real limitation is that this sits at a fairly narrow intersection of people doing causal inference from text with LLM extraction who specifically care about finite-sample guarantees rather than asymptotic ones.

The conservatism analysis is sobering—when LLMs extract only 3 out of 5 confounders, intervals roughly double in width, which could render the method impractical for many applications. The theoretical contribution, while solid, is more of an adaptation of existing tools to a new setting than a fundamental advance. The related work section is comprehensive and clearly positions the work against Barnatchez et al. and Vovk & Wang, but it could engage more deeply with the classical measurement error literature from econometrics and the broader sensitivity analysis frameworks like Rosenbaum bounds.

Stepping back, this is technically sound work that fills a genuine gap where causal inference, conformal prediction, and NLP intersect. But the novelty is primarily in the integration rather than fundamental innovation—the core techniques already exist, and the practical utility is constrained by the worst-case conservatism that makes the method most useful precisely when the LLM is already so accurate that correction may be unnecessary. The audience is quite specialized, and while the theoretical contribution is real, it's fundamentally incremental. For EMNLP specifically, this sits at the intersection of NLP and statistical methodology. EMNLP does accept methodological papers related to NLP applications, but this leans heavily toward the statistics/ML theory side. The NLP component (LLM-extracted text confounders) is the application domain, not the core contribution. The core contribution is in conformal prediction theory for causal inference.

Wait, I was told not to evaluate venue fit. Let me focus purely on the idea quality.

The idea is sound and fills a real gap, with moderate novelty as an integration of existing frameworks. Significance is moderate-to-weak for a top venue given the niche audience and limited practical impact from the conservatism trade-off. Reviewers would likely see this as a natural, expected combination rather than something surprising, especially since the pilot analysis already hints at the results.

Reconsidering the acceptance landscape — EMNLP typically sits around 20-25% acceptance, so a paper needs to be in that top tier. This one has a clear problem, principled approach, and honest limitations, but the novelty is primarily in combining existing methods rather than fundamental innovation, and the NLP piece serves mainly as an application domain for the statistical contribution. I'd place this in the 20-30% range — solid work that lacks the excitement needed to stand out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f6cf52e-e964-4458-9396-532c93215c9f",
  "isSidechain": false,
  "requestId": "req_011CbD8PNgSc5je3kEF1gEgs",
  "type": "assistant",
  "uuid": "59d2f69a-4c45-4e77-9c52-e7fc132e1edd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZP9grw66FMYs8BEPVk1R2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1762,
      "cache_read_input_tokens": 27938,
      "output_tokens": 5959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5959,
          "cache_read_input_tokens": 27938,
          "cache_creation_input_tokens": 1762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1762
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

_source line 42 · 2026-05-20T03:43:47.873Z_

Now I have sufficient information from the literature to make a well-grounded evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Zhang et al. "Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition"](https://arxiv.org/abs/2510.04406) (arXiv 2025): 本 proposal Track A 的核心方法论基础。提出了针对两阶段 sequential pipeline 的模块化残差分解框架，支持 FWER 控制的逐阶段不确定性归因。原文面向供应链/股票等场景，未涉及因果推断或加权可交换性。Proposal 声称的 extension（将其适配到 DR pseudo-outcome + propensity propagation 的因果 pipeline）是成立的且非 trivial。

- [Csillag et al. "Extending Prediction-Powered Inference through Conformal Prediction"](https://arxiv.org/abs/2510.16166) (arXiv 2025): Track B 的核心基础。将 conformal set-predictor 引入 PPI 框架，赋予 PPI 有限样本保证。原文处理通用 Z/M-estimation，未特别处理因果估计中 DR estimator 的特殊结构。Proposal 将其扩展到 ATE 估计场景，逻辑上是自洽的 application。

- [DoubleLingo: Causal Estimation with LLMs](https://aclanthology.org/2024.naacl-short.71/) (NAACL 2024): 在 Double Machine Learning 框架中使用 LLM 进行 nuisance function 估计。提供渐近保证但无有限样本 coverage guarantee。是本 proposal 明确要超越的 baseline。

- [Ma et al. "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding"](https://arxiv.org/abs/2507.02843) (NeurIPS 2025): 处理"推理时文本混淆"——训练时有完整 confounders，推理时只有文本描述。其 doubly robust learner 同样只提供渐近保证。注意：Ma et al. 的 problem setting（training vs. inference time mismatch）与本 proposal（LLM extraction noise）有本质不同。

- [Barnatchez et al. "Debiased ML for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding"](https://arxiv.org/abs/2604.03772) (arXiv April 2026): 最直接的竞争者。处理"runtime confounding"——confounders 在部署时完全缺失。使用 semiparametric debiasing 进行边缘化。Proposal 正确指出二者的关键区别：missing vs. noisy extraction。这一区分是成立的——缺失变量需要边缘化，有噪声的变量需要量化测量误差。

- [Alaa et al. "Conformal Meta-learners for Predictive Inference of ITE"](https://proceedings.neurips.cc/paper_files/paper/2023/) (NeurIPS 2023): Conformal ITE 的标杆工作，但假设 confounders 无误差观测。

- [Systematic Review of Conformal Inference for Treatment Effects](https://arxiv.org/abs/2509.21660) (arXiv 2025): 综述覆盖 11 篇关键论文，确认现有 conformal causal 方法均假设 confounders perfectly observed——验证了 proposal 声称的 gap 存在。

- [Prediction-Powered Causal Inferences](https://arxiv.org/abs/2502.06343) (arXiv 2025, NeurIPS 2025): PPI 在因果推断的直接扩展，但使用 point prediction 而非 conformal sets。

- [Kato "Semi-Supervised Treatment Effect Estimation"](https://arxiv.org/abs/2511.08303) (arXiv 2025): 处理半监督因果估计中的 unlabeled covariates，使用 Riesz regression。与本 proposal 互补但非直接竞争。

- 调研总结: 这一细分领域（conformal prediction × causal inference × LLM text extraction）处于三个成熟文献流交汇的 "空白地带"。现有 conformal causal 方法假设 confounders 无误差；现有 LLM causal 方法只提供渐近保证；现有 conformal PPI 方法未 specialize 到 causal estimation。**Gap 确实存在**，但这个 gap 的大小（即：将现有工具 "拼接" 到这个交叉场景的技术难度和概念新颖性）是需要审慎评估的。

【Trivial Alternative 检验】:
存在若干 lower-cost alternatives 需要考量：

1. **Bootstrap/重采样方法**: 对 LLM extraction 进行多次采样（例如 temperature > 0 的多次 prompting），用 bootstrap 估计 extraction variance，然后在 doubly robust 估计中 propagate 这个 variance。这不能提供 finite-sample 保证，但在实际样本量合理时可能 coverage 表现相当接近。Proposal 自己承认 "bootstrap undercoverage" 但这在 n 足够大时可能只差几个百分点。
2. **Sensitivity analysis approach**: 将 LLM extraction noise 视为一种 measurement error，用经典的 errors-in-variables 或 sensitivity analysis 框架（如 Rosenbaum bounds 的变体）来量化 robustness，而非构建完整的 conformal pipeline。
3. **直接 ensemble calibration**: 用多个 LLM 或 prompt 变体提取 confounders，对 disagreement 做 empirical calibration。

**增量价值**: Proposal 的核心增量在于 **finite-sample coverage guarantee**（而非仅渐近保证），这对于高风险决策场景（临床、政策）有理论上的严格性优势。但 trivial alternative 威胁是真实的——实践中 bootstrap + 合理样本量可能 "够用"，finite-sample guarantee 的实际价值取决于使用者是否真正需要这种严格性。

【前提假设检验】:
核心逻辑链中有以下未充分验证的环节：

1. **(Weighted) Exchangeability 假设**: Conformal prediction 的有效性依赖于 calibration data 和 test data 之间的（加权）可交换性。在 observational text data 中，LLM extraction 的噪声模式可能与文本的子群体（如不同科室的临床笔记、不同人群的社交媒体文本）系统性相关，破坏可交换性。Proposal 提到 "weighted exchangeability" 但未具体讨论在什么条件下这一假设成立。
2. **Confounder completeness 假设**: 框架假设所有相关 confounders 都 *存在于文本中* 且 LLM 的问题仅是提取噪声。但实际中更严重的问题可能是 **text 中根本未记录某些 confounders**（如医生未记录的临床观察），这是 unmeasured confounding 而非 measurement error，conformal 框架无法解决。
3. **Worst-case 的实际合理性**: Track A 的 worst-case enumeration 取所有 conformal set members 的极值。这假设任何 c ∈ C(x) 都是同等可能的。实际上 conformal set 中不同 members 的 posterior probability 差异很大，worst-case 推理可能导致不必要的保守性。Proposal 的 pilot analysis 已经展示了这个问题（|C|=3 时 widening ~100%），但没有讨论是否可以利用 set 内部的概率信息来收紧 bounds。

【3 维度打分】:
1. Novelty: 中 — 核心贡献是将三个已有框架（modular CP, conformal PPI, conformal ITE）拼接到一个新的应用场景（LLM-extracted text confounders for causal inference）。每个组件都已发表（Zhang et al. 2025, Csillag et al. 2025, Alaa et al. 2023），拼接过程非 trivial（需要证明 modular decomposition 在 causal exchangeability + DR pseudo-outcomes 下成立、需要处理 propensity propagation），但概念层面属于"自然的 next step"而非"surprising connection"。The pilot conservatism analysis 和 explicit propensity propagation 分析是有价值的 technical contribution，但这是分析现有框架在新场景下的行为，而非方法论上的根本创新。与 Barnatchez et al. (2604.03772) 的区分（missing vs. noisy）逻辑上成立，但这也意味着二者共同占据了这个 space，进一步削弱了 novelty claim 的独占性。

2. Significance: 中偏弱 — 问题本身（为 LLM-extracted confounders 提供 valid uncertainty quantification）是重要的，但实际影响受限于多个因素：(a) 目标用户极度 niche——同时需要 text-based causal inference + 使用 LLM extraction + 关心 finite-sample 而非 asymptotic guarantee 的研究者/实践者很少；(b) pilot analysis 诚实地揭示了一个根本性张力——当 LLM 足够好（|C|=1, singleton）时不需要 correction，当 LLM 不够好（|C|≥3）时 correction 使 intervals 过宽以致 impractical——方法的 "sweet spot" (|C|=2) 相当窄；(c) 核心结果如果 positive（conformal coverage is maintained），reviewers 会说 "this is expected given the theoretical guarantees"，缺乏 surprise。如果结果能展示 bootstrap 严重 undercover 而 conformal 保持 nominal，则有一定实证价值，但这仍是 "the theory works as predicted"。

3. Related Work: 强 — 文献覆盖非常全面且 up-to-date（包含 2026 年 4 月的 Barnatchez et al. 和 2026 年 3 月的 Vovk & Wang）。与最直接竞争者的差异化（missing vs. noisy, prediction vs. treatment effects）清晰且逻辑自洽。对 DoubleLingo, Ma et al., Alaa et al. 等 baseline 的定位准确。唯一缺憾是未充分讨论经典 measurement error 文献（如 Carroll et al. errors-in-variables, SIMEX）在因果推断中的应用，这些方法处理的正是 "noisy covariate" 问题，只是不使用 conformal 工具。

【概率估计】: [18% - 30%] 中位 24%

【估计理由】: 
Novelty 是限制上界的主要维度——这是一个 integration paper，将已有组件适配到新场景，技术上非 trivial 但概念上不 surprising。Significance 进一步约束了上界——practical sweet spot 过窄（只在 LLM "pretty good but not great" 时有价值），且 positive results 不会带来 surprise（conformal guarantees are expected to hold by construction）。Related work 是最强维度，展示了对领域的深刻理解和 honest positioning。综合来看，这是一篇在 25-35% 概率区间的 "has real novelty delta but reviewers would say 'I would have guessed this'" 类型论文的下半区。中位 24% 反映了 integration novelty 的 ceiling 和 narrow practical impact 之间的张力。若能在实验中展示 bootstrap 在现实场景中严重 undercover（例如 10-15 个百分点的 coverage gap），概率可上移到 28-30%；若 coverage gap 很小（2-3 个百分点），则 finite-sample guarantee 的实际价值被严重削弱。

【主要风险】:
1. **"Natural combination, limited surprise" 风险**: 审稿人认为这是将已有工具直接 apply 到新 setting 的 straightforward extension，核心 theorem 是 Zhang et al. (2025) 在加权版本下的 routine generalization，拒稿理由："The theoretical contribution is a relatively straightforward adaptation of existing modular conformal prediction to the causal setting."
2. **Practical relevance 风险**: 审稿人指出 useful operating region 过窄——当 |C|/K > 0.4 时 intervals 过宽（proposal 自己承认的 ~100% widening），当 |C|/K ≈ 0.2 时 LLM 已经足够好以至于 plug-in approach 可能 "够用"。挑战将是 "Why would a practitioner choose this over simply trusting a well-calibrated LLM + standard asymptotic inference?"
```

Sources:
- [Zhang et al. "Modular and Adaptive Conformal Prediction for Sequential Models"](https://arxiv.org/abs/2510.04406)
- [Csillag et al. "Extending Prediction-Powered Inference through Conformal Prediction"](https://arxiv.org/abs/2510.16166)
- [DoubleLingo: Causal Estimation with Large Language Models](https://aclanthology.org/2024.naacl-short.71/)
- [Ma et al. "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding"](https://arxiv.org/abs/2507.02843)
- [Barnatchez et al. "Debiased ML for Conformal Prediction Under Runtime Confounding"](https://arxiv.org/abs/2604.03772)
- [Prediction-Powered Causal Inferences](https://arxiv.org/abs/2502.06343)
- [Kato "Semi-Supervised Treatment Effect Estimation"](https://arxiv.org/abs/2511.08303)
- [Systematic Review of Conformal Inference for Treatment Effects](https://arxiv.org/abs/2509.21660)
- [Vovk & Wang "Conformal e-prediction in the presence of confounding"](https://arxiv.org/pdf/2603.11134)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59d2f69a-4c45-4e77-9c52-e7fc132e1edd",
  "isSidechain": false,
  "requestId": "req_011CbD8PNgSc5je3kEF1gEgs",
  "type": "assistant",
  "uuid": "3e7c934c-9331-49cc-b1bd-ed0d65d2b15a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZP9grw66FMYs8BEPVk1R2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1762,
      "cache_read_input_tokens": 27938,
      "output_tokens": 5959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5959,
          "cache_read_input_tokens": 27938,
          "cache_creation_input_tokens": 1762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1762
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Descrip…",
  "leafUuid": "3e7c934c-9331-49cc-b1bd-ed0d65d2b15a",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted causal confounders",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Descrip…",
  "leafUuid": "3e7c934c-9331-49cc-b1bd-ed0d65d2b15a",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted causal confounders",
  "sessionId": "d0bbdb3c-f9cb-4bec-8c7b-7c2fa68f19fd"
}
```

---
