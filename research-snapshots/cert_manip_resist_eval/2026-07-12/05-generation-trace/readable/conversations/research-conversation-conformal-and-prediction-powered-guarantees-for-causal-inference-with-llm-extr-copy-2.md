# Research conversation: Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders ## Description We p

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/7b79346c-83bc-4b4d-904c-08a80917a9e0.jsonl`
- **Structured JSON:** [`37b8b5e935f13ea1e80e.json`](../../sessions/37/37b8b5e935f13ea1e80e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:48:37.538Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:48:37.538Z",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "content": "# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders\n\n## Description\nWe propose ConformalPPITextCausal, a framework providing finite-sample coverage guarantees for treatment effects estimated using LLM-extracted text confounders. Current methods (DoubleLingo, Ma et al.) rely on asymptotic guarantees that break down when LLM extraction introduces unquantified heterogeneous noise. Our dual-track approach addresses this via: Track A (ITE intervals) — adapting modular conformal prediction (Zhang et al. 2025) to a causal two-stage pipeline where Stage 1 produces conformal prediction sets over LLM-extracted categorical confounders (with worst-case pseudo-outcome enumeration including explicit propensity score propagation, O(|C|) per unit) or low-dimensional Matryoshka embeddings (with ellipsoidal sets and convex relaxation restricted to smooth nuisance estimators), and Stage 2 constructs doubly robust treatment effect intervals with FWER-controlled coverage tighter than Bonferroni; Track B (ATE intervals) — extending conformal prediction-powered inference (Csillag et al. 2025) to the causal setting, where a small expert-labeled and large LLM-imputed dataset yield valid confidence intervals via Z-estimation with conformal set-predictors. Cross-conformal calibration (Gasparin & Ramdas, ICML 2025) reduces the three-way data split to two-way, improving sample efficiency for labeled-data-scarce settings. A pilot conservatism analysis shows practical viability: for K=5 confounder categories, interval widening is ~60% with conformal set size |C|=2 (good LLM) and ~100% with |C|=3 (decent LLM), driven primarily by propensity score variation across conformal set members. The method is practically useful when the LLM achieves small conformal sets and correctly signals insufficient information otherwise. We differentiate from Barnatchez et al. (2604.03772), who handle missing confounders at deployment via semiparametric debiasing — a complementary but distinct setting from our noisy-extraction framework. The genuine theoretical contribution is proving the modular residual decomposition holds under causal exchangeability conditions specific to doubly robust pseudo-outcomes with explicit propensity propagation. Experiments on semi-synthetic MIMIC-IV clinical notes, social media data, and synthetic benchmarks demonstrate maintained nominal coverage where bootstrap alternatives undercover, with a dedicated conservatism experiment varying |C|/K to validate the pilot analysis.\n\n## Core Problem\nCausal inference from observational text data (clinical notes, social media, policy documents) requires adjusting for confounders embedded in unstructured text. Modern LLMs can extract these confounders, but extraction is imperfect — introducing measurement error that invalidates standard causal estimators' asymptotic guarantees. No existing framework provides finite-sample coverage guarantees for treatment effect estimates when confounders are extracted by a fallible LLM. Naive approaches (plugging in LLM point predictions as if they were ground truth) can produce arbitrarily biased causal conclusions when extraction noise is heterogeneous across subpopulations.\n\n## Opportunity\nThree independent research threads have matured to the point where they can be unified into a principled solution: (1) modular conformal prediction for sequential pipelines (Zhang et al. 2025, arXiv 2510.04406) provides a residual decomposition framework that controls family-wise error across pipeline stages without resorting to loose Bonferroni corrections; (2) prediction-powered inference extended through conformal prediction (Csillag et al. 2025, arXiv 2510.16166) yields valid population-level confidence intervals when a prediction model (here, the LLM) imputes covariates on a large unlabeled set alongside a small human-labeled set; and (3) conformal meta-learners for individual treatment effects (Alaa et al. NeurIPS 2023) provide conformal intervals for heterogeneous effects but assume perfectly observed confounders. Additionally, Matryoshka embedding models (Qwen3-Embedding-8B) now support flexible dimensionality from 32 to 4096, making conformal prediction over embedding spaces tractable at reduced dimensions. Recent work on conformal prediction under confounding — including Barnatchez et al. (arXiv 2604.03772) on runtime confounding (missing confounders at deployment) and Vovk & Wang (arXiv 2603.11134) on conformal e-prediction — demonstrates growing interest but targets distinct problem settings from ours (noisy extraction vs. missing variables, and e-values for prediction vs. p-values for treatment effects). By bridging these threads, we can deliver both individual-level (ITE) and population-level (ATE) treatment effect intervals that honestly account for LLM extraction uncertainty — a capability no current method provides.\n\n## Landscape\nThe intersection of conformal prediction and causal inference has seen rapid growth (Systematic Review, arXiv 2509.21660, covering 11 key papers), but existing conformal ITE methods (Lei & Candès JRSS-B 2021; Alaa et al. NeurIPS 2023; KDD 2024 wTCP-DR) assume confounders are observed without error. The conformal prediction for NLP survey (Campos et al. TACL 2024) covers classification, QA, and generation quality but not downstream causal validity. Prediction-powered inference (Angelopoulos et al. Science 2023) and its causal extensions (arXiv 2502.06343; Kato arXiv 2511.08303 NeurIPS 2025) address the labeled/unlabeled split for treatment effects but do not incorporate conformal sets for the imputed covariates. Zhang et al. (2025) handle sequential model pipelines with modular conformal guarantees but do not treat the causal setting or weighted exchangeability. DoubleLingo (NAACL 2024) and Ma et al. (NeurIPS 2025) use LLMs within doubly robust causal estimators for text data but provide only asymptotic guarantees with no finite-sample uncertainty quantification for LLM extraction noise. Multi-variable conformal prediction (Lützow et al. arXiv 2605.12341, 2026) and ellipsoidal conformal sets (Xu et al. ICML 2024) now provide tractable geometric tools for moderate-dimensional conformal regions.\n\nTwo recent works merit explicit differentiation: Barnatchez et al. (arXiv 2604.03772, April 2026) address conformal prediction for counterfactual outcomes under 'runtime confounding' — where confounders measured in training are entirely MISSING at deployment. Their semiparametric debiasing approach marginalizes over unobserved confounders via multiply-robust influence functions, assuming Y(a)⊥S|V (systematic differences explained by the observed subset V). Our setting is fundamentally different: all confounders are present in the text and extracted by the LLM, but with NOISE — the confounders are measured with error, not missing entirely. Their debiasing marginalizes over missing variables; our conformal sets quantify extraction uncertainty over observed-but-noisy variables. Vovk & Wang (arXiv 2603.11134, March 2026) extend conformal e-prediction to handle observed confounding between X and Y using e-values (nonnegative random variables with expectation ≤ 1) rather than p-values. While e-values provide attractive anytime-valid guarantees under optional stopping, their framework targets prediction of Y given X under confounding, not treatment effect estimation. Our framework uses standard conformal prediction sets combined with PPI, targeting ITE/ATE estimation — a complementary but distinct goal. The e-value approach could be an interesting alternative foundation for future work.\n\nThe gap we fill is the integration of modular conformal prediction and conformal PPI into a unified framework for the two-stage pipeline of LLM confounder extraction followed by causal effect estimation, with proven finite-sample validity under noisy (not missing) confounder extraction.\n\n## Approach\nWe propose a dual-track framework, ConformalPPITextCausal, for valid causal inference when text confounders are extracted by an LLM.\n\n**Data Splitting and Sample Efficiency.** The baseline design uses a three-way data split: (S1) training data for fine-tuning the LLM extraction model and fitting nuisance functions (propensity score, outcome regression), (S2) calibration data for Stage 1 conformal sets on the extracted confounders, and (S3) calibration data for Stage 2 conformal intervals on treatment effects. To address sample efficiency — critical for clinical text datasets like MIMIC-IV where expert-labeled samples are expensive — we propose two improvements: (i) K-fold cross-fitting for nuisance function estimation within S1, following Chernozhukov et al. (2018) DML, which uses all training data for both estimation and evaluation; (ii) cross-conformal calibration for Stage 1, following Gasparin & Ramdas (ICML 2025, arXiv 2503.01495), which achieves coverage ≥ 1−2α₁ using K-fold rotation rather than a dedicated hold-out set, effectively merging S2 into S1 and reducing the three-way split to a two-way split (train+Stage1-calibrate vs. Stage2-calibrate). The coverage cost (1−2α₁ vs. 1−α₁) is manageable by setting α₁ conservatively (e.g., α₁=0.025 for effective 95% Stage 1 coverage). We discuss minimum sample size requirements: Stage 2 calibration requires n₃ ≥ ⌈1/α₂⌉ ≈ 100-200 for reliable conformal quantiles at α₂=0.05, and we recommend n_total ≥ 500 for the full pipeline, with n₃ ≥ 150 reserved for Stage 2. For very small labeled datasets (n < 300), Track B (PPI) is preferred as it leverages large unlabeled corpora.\n\n**Track A — Modular Conformal ITE Intervals.** We adapt the residual decomposition of Zhang et al. (2025), where the total prediction residual R decomposes as R ≤ ΔR₁ + R₂, with Stage 1 = LLM confounder extraction and Stage 2 = doubly robust pseudo-outcome estimation.\n\nIn the primary setting, the LLM extracts CATEGORICAL confounders (e.g., disease severity ∈ {mild, moderate, severe}, smoking status ∈ {never, former, current}) via prompted classification. Conformal prediction sets for classification are natural finite sets with guaranteed coverage.\n\n**Explicit Propensity Score Propagation.** The worst-case pseudo-outcome over the conformal set is computed by full enumeration with explicit propagation through BOTH the outcome regression AND the propensity score. For each possible confounder value c ∈ C(x), the DR pseudo-outcome is:\n\nφ̂(c; Yᵢ, Aᵢ) = [μ̂₁(c) − μ̂₀(c)] + Aᵢ·(Yᵢ − μ̂₁(c))/ê(c) − (1−Aᵢ)·(Yᵢ − μ̂₀(c))/(1−ê(c))\n\nCritically, different confounder values c yield different propensity scores ê(c), which enter the augmentation term as 1/ê(c) (for treated) or 1/(1−ê(c)) (for control). This propensity variation is a distinct and compounding source of uncertainty beyond outcome regression variation. The augmentation term amplifies when propensity scores are extreme: a confounder value with ê(c)=0.1 magnifies residuals 10×. The worst-case interval is [min_c φ̂(c), max_c φ̂(c)] with complexity O(|C|) per unit. We recommend propensity score trimming (truncating ê(c) to [0.05, 0.95]) to prevent a single extreme-propensity confounder value from dominating the interval.\n\n**Pilot Conservatism Analysis.** We provide a back-of-envelope quantification of interval widening due to worst-case enumeration. Consider a clinical setting with K=5 severity categories {none, mild, moderate, severe, critical} and realistic nuisance function values:\n\n| Category | μ̂₁(c) | μ̂₀(c) | ê(c) | CATE |\n|----------|--------|--------|-------|------|\n| none     | 0.40   | 0.30   | 0.50  | 0.10 |\n| mild     | 0.50   | 0.35   | 0.45  | 0.15 |\n| moderate | 0.60   | 0.40   | 0.40  | 0.20 |\n| severe   | 0.72   | 0.45   | 0.35  | 0.27 |\n| critical | 0.85   | 0.50   | 0.25  | 0.35 |\n\nFor a treated patient with Y=0.65 and true severity=moderate, the DR pseudo-outcomes across categories are: φ̂(none)=0.60, φ̂(mild)=0.48, φ̂(moderate)=0.33, φ̂(severe)=0.07, φ̂(critical)=−0.45. The variation is dominated by the augmentation term (Y−μ̂₁(c))/ê(c), where propensity changes from 0.50 to 0.25 amplify residuals 2×. The extraction uncertainty width (Δφ = max−min over C(x)) for different conformal set sizes:\n\n- |C|=1 (excellent LLM, singleton): Δφ=0, no widening vs. oracle.\n- |C|=2 (good LLM, e.g., {moderate, severe}): Δφ≈0.26, widening ≈ 60% over oracle CI width of ~0.40.\n- |C|=3 (decent LLM, e.g., {mild, moderate, severe}): Δφ≈0.41, widening ≈ 100% over oracle.\n- |C|=4+ (poor LLM): Δφ>1.0, intervals become vacuously wide — correctly reflecting that the LLM provides insufficient information for credible causal conclusions.\n\nThe general widening ratio is approximately W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle, where Δ_CATE is the CATE variation across the conformal set, |r| is the outcome residual magnitude, and Δ(1/ê) is the inverse propensity variation. Key practical determinants: (a) conformal set size |C|/K — the LLM quality directly controls conservatism; (b) propensity score stability across confounder categories — good overlap reduces widening; (c) outcome residual magnitude — well-fitted outcome models reduce augmentation-driven widening. The method is practically useful (W < 2) when the LLM achieves conformal set size |C| ≤ 2 for K=5 categories, and correctly signals 'insufficient information' otherwise.\n\nFor the secondary continuous track, we use Qwen3-Embedding-8B with Matryoshka dimensionality reduction to 128–256 dimensions, construct ellipsoidal conformal sets (Xu et al. ICML 2024; Lützow et al. 2026), and bound worst-case pseudo-outcomes via convex relaxation: local Lipschitz continuity of nuisance functions plus first-order Taylor expansion over the ellipsoid, following the decision-theoretic framework of Wang & Dobriban (arXiv 2602.00989, 2026). **Important restriction**: the convex relaxation via Lipschitz continuity and Taylor expansion requires smooth nuisance estimators. This is compatible with neural network outcome models (e.g., TARNet, DragonNet) and kernel methods, but NOT with tree-based models (gradient-boosted trees, random forests) that are piecewise constant with jump discontinuities. We therefore restrict the continuous embedding track to smooth nuisance estimators. Note that the categorical track (primary) works with ANY nuisance estimator, including tree-based methods, since worst-case computation is by direct enumeration without smoothness assumptions. The modular framework's FWER control across both stages yields provably tighter intervals than naive Bonferroni.\n\n**Track B — Conformal PPI for ATE Intervals.** We apply the conformal PPI framework of Csillag et al. (2025) to estimate average treatment effects. The LLM serves as the prediction model in the PPI sense: a small human-labeled dataset has expert-annotated confounders, and a large dataset has LLM-extracted confounders. The conformal set-predictor from Stage 1 replaces point imputation, yielding valid ATE confidence intervals via Z-estimation: E[inf φ(C(X))] − M·Err(C) ≤ ATE ≤ E[sup φ(C(X))] + M·Err(C), where M is the bounded range of the influence function and Err(C) is the conformal miscoverage rate. This extends PPI causal inference (arXiv 2502.06343) by using conformal rather than point imputation, providing finite-sample validity without distributional assumptions on the LLM. Track B is especially suited to small-labeled-data settings (MIMIC-IV) because it leverages large unlabeled corpora.\n\nWe evaluate on three benchmarks: (1) semi-synthetic MIMIC-IV clinical notes (treatment escalation effect on ICU outcomes, disease severity as text confounder), (2) semi-synthetic social media data (content moderation effect on engagement, toxicity level as confounder), and (3) fully synthetic data with known ground-truth for calibration validation. Key metrics: empirical coverage at 90%/95% nominal levels, interval width relative to oracle (perfectly observed confounders) and bootstrap baselines, widening ratio W as a function of conformal set size and propensity overlap, and sensitivity to LLM extraction quality via deliberately degraded models. We include a dedicated conservatism experiment varying |C|/K from 0.2 to 0.8 to empirically validate the pilot analysis above.\n\nWe are transparent that worst-case reasoning over conformal sets introduces conservatism relative to oracle methods. The honest framing: our intervals maintain nominal coverage where bootstrap intervals undercover due to LLM extraction noise, with comparable width when LLM quality is high (|C|=1-2). The conservatism correctly reflects true uncertainty in the LLM-as-measurement-instrument setting, and the pilot analysis above shows it is quantifiably bounded for reasonable LLM quality.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '200-300', 'timeline': '10 weeks (targeting AAAI 2027 July 28 deadline)', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'breakdown': 'Weeks 1-2: Formalize theoretical framework (modular decomposition under weighted exchangeability, conformal PPI ATE estimator, cross-conformal Stage 1 calibration). Weeks 3-4: Implement cross-fitted pipeline, categorical conformal extraction, worst-case enumeration with explicit propensity propagation. Weeks 5-6: Implement continuous embedding track (Matryoshka 128-256d, ellipsoidal sets, convex relaxation with smooth nuisance estimators) and PPI ATE track. Weeks 7-8: Experiments on MIMIC-IV, social media, synthetic benchmarks including conservatism analysis. Week 9: Ablations (LLM quality sensitivity via |C|/K sweep, propensity overlap analysis, embedding dimension, calibration set size, cross-conformal vs. split comparison). Week 10: Paper writing and proof polishing.'}, 'human_in_loop': {'gpu_hours': '200-300', 'timeline': '8 weeks', 'claude_api_cost': '$100-150', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'notes': 'AI assists with literature integration, boilerplate code, proof sketch verification. Human focuses on theoretical contributions (weighted exchangeability conditions, tight bounds for DR pseudo-outcomes, propensity propagation analysis) and experimental design. Requires ~5 hours domain expert time for confounder annotation guidelines.'}, 'auto_research': {'gpu_hours': '250-350', 'timeline': '5-6 weeks', 'claude_api_cost': '$250-350', 'estimated_gpu_cost': '$375-525 (A100 at ~$1.50/hr)', 'speed_bottleneck': 'Theoretical proof verification requires human mathematician; three-way split calibration across multiple seeds requires sequential experiment iterations; domain expert annotation for MIMIC-IV confounder labels cannot be automated'}}\n\n## Inspired By\nGap: Existing conformal causal methods assume error-free confounders; existing LLM conformal methods ignore causal settings; existing text-based causal methods provide only asymptotic guarantees; Barnatchez et al. handle missing confounders but not noisy extraction; Vovk & Wang handle confounding in prediction but not treatment effects. Pattern: Three converging literatures (modular CP, conformal PPI, conformal causal inference) that have not been connected. Key enablers: Zhang et al. (arXiv 2510.04406) modular residual decomposition framework; Csillag et al. (arXiv 2510.16166) conformal set-predictor for PPI; Alaa et al. (NeurIPS 2023) conformal meta-learners for ITE; Barber et al. (Annals of Statistics 2023) weighted exchangeability beyond standard CP assumptions.\n\n## Target Venues\n- AAAI 2027 (Primary — abstract July 21, full paper July 28, 2026; ~10 weeks from today)\n- ARR August 2026 cycle (Secondary — submission August 3, 2026) → EACL 2027 (commitment October 11, 2026)\n- AISTATS 2027 (Stretch — estimated deadline ~October 2026, not yet announced)\n\n## Key References\n- Zhang et al. 'Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition' (arXiv 2510.04406, 2025)\n- Csillag et al. 'Extending Prediction-Powered Inference through Conformal Prediction' (arXiv 2510.16166, 2025)\n- Angelopoulos et al. 'Prediction-Powered Inference' (Science, 2023)\n- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025)\n- Kato 'Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression' (arXiv 2511.08303, NeurIPS 2025)\n- Barber et al. 'Conformal prediction beyond exchangeability' (Annals of Statistics, 2023)\n- Alaa et al. 'Conformal Meta-learners for Predictive Inference of Individual Treatment Effects' (NeurIPS 2023)\n- Wang & Dobriban 'Optimal Decision-Making Based on Prediction Sets' (arXiv 2602.00989, 2026)\n- Lützow et al. 'Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting' (arXiv 2605.12341, 2026)\n- Xu et al. 'Conformal prediction for multi-dimensional time series by ellipsoidal sets' (ICML 2024)\n- Campos et al. 'Conformal Prediction for Natural Language Processing: A Survey' (TACL, 2024)\n- Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation (arXiv 2509.21660, 2025)\n- Lei & Candès 'Conformal Inference of Counterfactuals and Individual Treatment Effects' (JRSS-B, 2021)\n- DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)\n- Ma et al. 'LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding' (NeurIPS 2025)\n- Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)\n- Veitch et al. 'Adapting Text Embeddings for Causal Inference' (UAI 2020)\n- Barnatchez et al. 'Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding' (arXiv 2604.03772, 2026)\n- Vovk & Wang 'Conformal e-prediction in the presence of confounding' (arXiv 2603.11134, 2026)\n- Gasparin & Ramdas 'Improving the statistical efficiency of cross-conformal prediction' (arXiv 2503.01495, ICML 2025)\n- Chernozhukov et al. 'Double/debiased machine learning for treatment and structural parameters' (Econometrics Journal, 2018)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:48:37.544Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:48:37.544Z",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

## Round 1

57 recorded events

### User

_source line 3 · 2026-05-20T03:48:37.565Z_

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
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "61772c5d-d8aa-4fa4-824b-35eee4b50201",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:48:37.563Z_

```json
{
  "parentUuid": "61772c5d-d8aa-4fa4-824b-35eee4b50201",
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
  "uuid": "795177ff-a93d-434f-b316-d0706ec24c56",
  "timestamp": "2026-05-20T03:48:37.563Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:48:37.563Z_

```json
{
  "parentUuid": "795177ff-a93d-434f-b316-d0706ec24c56",
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
  "uuid": "d529879c-588c-49e0-a27f-09f0ec96f644",
  "timestamp": "2026-05-20T03:48:37.563Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T03:48:37.563Z_

```json
{
  "parentUuid": "d529879c-588c-49e0-a27f-09f0ec96f644",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d57a4f97-e2ef-4369-b7f3-50d18226f12a",
  "timestamp": "2026-05-20T03:48:37.563Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
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
  "lastPrompt": "# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Description We propose ConformalPPITextCausal, a framework providing finite-sample coverage g…",
  "leafUuid": "d57a4f97-e2ef-4369-b7f3-50d18226f12a",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Assistant

_source line 9 · 2026-05-20T03:48:45.434Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal as the 补救 agent (remedy agent), focusing exclusively on experimental design and technical execution completeness. I need to first do thorough literature research to understand the current experimental standards in this area before giving any suggestions.

Let me break down what I need to research:
1. How do recent papers in conformal prediction + causal inference design their experiments? What baselines, metrics, ablations?
2. Are the baselines mentioned (DoubleLingo, Ma et al.) still current? Any newer ones?
3. Are the datasets (MIMIC-IV, social media) standard? Any better alternatives?


4. What patterns emerge from similar papers' experimental setups?

I should start by searching the literature to see what's currently standard practice in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d57a4f97-e2ef-4369-b7f3-50d18226f12a",
  "isSidechain": false,
  "requestId": "req_011CbD8vcgBbDMmJKZMHHsVw",
  "type": "assistant",
  "uuid": "0684dd5e-7237-4571-98dc-76151e682df8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJQmqzPxTZrfEQRtTwmzqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11076,
      "cache_read_input_tokens": 10980,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 281,
          "cache_read_input_tokens": 10980,
          "cache_creation_input_tokens": 11076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11076
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

_source line 10 · 2026-05-20T03:48:45.543Z_

I need to do thorough literature research before making any experimental design recommendations. Let me search for the current experimental standards in this area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0684dd5e-7237-4571-98dc-76151e682df8",
  "isSidechain": false,
  "requestId": "req_011CbD8vcgBbDMmJKZMHHsVw",
  "type": "assistant",
  "uuid": "34351cf7-53b2-4383-807a-07bcf988bff4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJQmqzPxTZrfEQRtTwmzqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11076,
      "cache_read_input_tokens": 10980,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 281,
          "cache_read_input_tokens": 10980,
          "cache_creation_input_tokens": 11076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11076
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

_source line 11 · 2026-05-20T03:48:45.790Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012EKdPC3MHpA4BENzce3Fqz`</summary>

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
  "parentUuid": "34351cf7-53b2-4383-807a-07bcf988bff4",
  "isSidechain": false,
  "requestId": "req_011CbD8vcgBbDMmJKZMHHsVw",
  "type": "assistant",
  "uuid": "e85422b0-1ed4-40f1-93d7-a67ffde6197b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJQmqzPxTZrfEQRtTwmzqU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11076,
      "cache_read_input_tokens": 10980,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 281,
          "cache_read_input_tokens": 10980,
          "cache_creation_input_tokens": 11076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11076
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

_source line 12 · 2026-05-20T03:48:45.796Z_

<details><summary>↩ Tool result · `toolu_012EKdPC3MHpA4BENzce3Fqz`</summary>

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
  "parentUuid": "e85422b0-1ed4-40f1-93d7-a67ffde6197b",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "c8fc1d93-cffb-4b7e-bfa2-376b4dc3b814",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e85422b0-1ed4-40f1-93d7-a67ffde6197b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T03:48:48.456Z_

Now let me conduct my pre-research. I'll search for multiple topics in parallel to understand the experimental design standards in this area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8fc1d93-cffb-4b7e-bfa2-376b4dc3b814",
  "isSidechain": false,
  "requestId": "req_011CbD8wDyDCC8jv8zNjm8UD",
  "type": "assistant",
  "uuid": "32cdf281-e9ea-4c9d-aec7-0fb917ae1165",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017VPcUFQ3FP7T91QHLAWJvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 22056,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 22056,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 14 · 2026-05-20T03:48:49.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eqc8ha64EYoV4EUAD2pYX7`</summary>

```json
{
  "query": "conformal prediction causal inference treatment effects experiments baselines 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32cdf281-e9ea-4c9d-aec7-0fb917ae1165",
  "isSidechain": false,
  "requestId": "req_011CbD8wDyDCC8jv8zNjm8UD",
  "type": "assistant",
  "uuid": "36f77910-17a4-4d3b-8cbe-c566abd745a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017VPcUFQ3FP7T91QHLAWJvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 22056,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 22056,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 15 · 2026-05-20T03:48:55.906Z_

<details><summary>↩ Tool result · `toolu_01Eqc8ha64EYoV4EUAD2pYX7`</summary>

```text
Web search results for query: "conformal prediction causal inference treatment effects experiments baselines 2024 2025"

Links: [{"title":"Conformal prediction for causal effects of continuous treatments","url":"https://openreview.net/pdf?id=1nL84tQNnK"},{"title":"A Systematic Review of Conformal Inference Procedures for","url":"https://www.arxiv.org/pdf/2509.21660"},{"title":"Conformal prediction for causal effects of continuous treatments","url":"https://arxiv.org/html/2407.03094v2"},{"title":"A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation: Methods and Challenges","url":"https://arxiv.org/html/2509.21660"},{"title":"(PDF) Conformal Inference for Counterfactuals and Individual Treatment Effects with Experiment Attrition","url":"https://www.researchgate.net/publication/403430038_Conformal_Inference_for_Counterfactuals_and_Individual_Treatment_Effects_with_Experiment_Attrition"},{"title":"Conformal Inference for Counterfactuals and Individual Treatment Effects with Experiment Attrition","url":"https://arxiv.org/pdf/2604.00504"},{"title":"[2407.03094] Conformal Prediction for Causal Effects of Continuous Treatments","url":"https://arxiv.org/abs/2407.03094"}]

I found several relevant research papers and resources on conformal prediction for causal inference and treatment effects. Here's what the search revealed:

## Recent Developments (2024-2025)

Research in this area shows papers published between 2021 to 2025, with an increasing trend in the more recent years, mostly in 2024 and 2025.

## Key Methods and Approaches

Conformal prediction is a powerful approach for uncertainty quantification of causal effects with model-agnostic finite-sample guarantees, though existing methods for conformal prediction of causal effects are limited to binary/discrete treatments and make highly restrictive assumptions such as known propensity scores.

Recent work includes a conformal diffusion model for treatment effect estimation in observational studies that uses deep generative models to learn the conditional distribution of potential outcomes.

## Foundational Work and Baselines

Lei and Candès (2021) is identified as a foundational paper that most recent papers build upon or compare to, with subsequent work by Jin et al. (2022), Alaa et al. (2024), Cai et al. (2024), and Gao et al. (2025).

## Experimental Evaluation

Performance of models is typically measured with metrics of average interval widths and achieved coverage, using simulated data with heteroscedastic and homoscedastic error characteristics.

Researchers follow common practice in causal machine learning by evaluating methods using synthetic datasets because of the fundamental problem of causal inference where counterfactual outcomes are never observable in real-world datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36f77910-17a4-4d3b-8cbe-c566abd745a5",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "d3663720-96eb-482f-b6c4-6e41823bdeb9",
  "toolUseResult": {
    "query": "conformal prediction causal inference treatment effects experiments baselines 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012JP6pAMRdRtSyVaZRgXBMr",
        "content": [
          {
            "title": "Conformal prediction for causal effects of continuous treatments",
            "url": "https://openreview.net/pdf?id=1nL84tQNnK"
          },
          {
            "title": "A Systematic Review of Conformal Inference Procedures for",
            "url": "https://www.arxiv.org/pdf/2509.21660"
          },
          {
            "title": "Conformal prediction for causal effects of continuous treatments",
            "url": "https://arxiv.org/html/2407.03094v2"
          },
          {
            "title": "A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation: Methods and Challenges",
            "url": "https://arxiv.org/html/2509.21660"
          },
          {
            "title": "(PDF) Conformal Inference for Counterfactuals and Individual Treatment Effects with Experiment Attrition",
            "url": "https://www.researchgate.net/publication/403430038_Conformal_Inference_for_Counterfactuals_and_Individual_Treatment_Effects_with_Experiment_Attrition"
          },
          {
            "title": "Conformal Inference for Counterfactuals and Individual Treatment Effects with Experiment Attrition",
            "url": "https://arxiv.org/pdf/2604.00504"
          },
          {
            "title": "[2407.03094] Conformal Prediction for Causal Effects of Continuous Treatments",
            "url": "https://arxiv.org/abs/2407.03094"
          }
        ]
      },
      "I found several relevant research papers and resources on conformal prediction for causal inference and treatment effects. Here's what the search revealed:\n\n## Recent Developments (2024-2025)\n\nResearch in this area shows papers published between 2021 to 2025, with an increasing trend in the more recent years, mostly in 2024 and 2025.\n\n## Key Methods and Approaches\n\nConformal prediction is a powerful approach for uncertainty quantification of causal effects with model-agnostic finite-sample guarantees, though existing methods for conformal prediction of causal effects are limited to binary/discrete treatments and make highly restrictive assumptions such as known propensity scores.\n\nRecent work includes a conformal diffusion model for treatment effect estimation in observational studies that uses deep generative models to learn the conditional distribution of potential outcomes.\n\n## Foundational Work and Baselines\n\nLei and Candès (2021) is identified as a foundational paper that most recent papers build upon or compare to, with subsequent work by Jin et al. (2022), Alaa et al. (2024), Cai et al. (2024), and Gao et al. (2025).\n\n## Experimental Evaluation\n\nPerformance of models is typically measured with metrics of average interval widths and achieved coverage, using simulated data with heteroscedastic and homoscedastic error characteristics.\n\nResearchers follow common practice in causal machine learning by evaluating methods using synthetic datasets because of the fundamental problem of causal inference where counterfactual outcomes are never observable in real-world datasets."
    ],
    "durationSeconds": 6.835706284000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "36f77910-17a4-4d3b-8cbe-c566abd745a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T03:48:58.486Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FvEPnkaBhy5TrDV4W2nzes`</summary>

```json
{
  "query": "DoubleLingo NAACL 2024 LLM causal inference text confounders experiment design baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3663720-96eb-482f-b6c4-6e41823bdeb9",
  "isSidechain": false,
  "requestId": "req_011CbD8wxybV2eAq9aSJwz8t",
  "type": "assistant",
  "uuid": "724d1311-595b-4828-bb48-6c3f6471e1b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EUngvSMx69tnVkEpSbVckW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 22864,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 22864,
          "cache_creation_input_tokens": 822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 822
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

_source line 17 · 2026-05-20T03:49:05.248Z_

<details><summary>↩ Tool result · `toolu_01FvEPnkaBhy5TrDV4W2nzes`</summary>

```text
Web search results for query: "DoubleLingo NAACL 2024 LLM causal inference text confounders experiment design baselines"

Links: [{"title":"DoubleLingo: Causal Estimation with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-short.71/"},{"title":"[Quick Review] Causal Inference with Large Language Model: A Survey","url":"https://liner.com/review/causal-inference-with-large-language-model-survey"},{"title":"Causal Inference with Large Language Model: A Survey - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.327/"},{"title":"Can Large Language Models Infer Causal Relationships from Real-World Text?","url":"https://arxiv.org/pdf/2505.18931"},{"title":"Can Post-Training Transform LLMs into Causal Reasoners?","url":"https://arxiv.org/pdf/2602.06337"},{"title":"LLMs Are Prone to Fallacies in Causal Inference","url":"https://arxiv.org/pdf/2406.12158"},{"title":"DoubleLingo: Causal Estimation with Large Language ...","url":"https://aclanthology.org/2024.naacl-short.71.pdf"}]

Based on the search results, I found information about DoubleLingo, a NAACL 2024 paper on causal inference with LLMs:

## DoubleLingo: Causal Estimation with Large Language Models

DoubleLingo enables theoretically consistent estimation of causal effects using LLM-based nuisance models by incorporating them within the framework of Double Machine Learning.

### Problem and Motivation

When confounders include text data, existing causal inference methods struggle due to the high dimensionality of the text. Simple statistical models which have sufficient convergence criteria for causal estimation are not well-equipped to handle noisy unstructured text, but flexible large language models that excel at predictive tasks with text data do not meet the statistical assumptions necessary for causal estimation.

### Results

On the best available dataset for evaluating such methods, DoubleLingo achieves a 10.4% reduction in the relative absolute error for the estimated causal effect over existing methods.

### Experimental Baselines

Based on the PDF excerpt, the experimental baselines include Oracle and Unadjusted models using outcome regressions, a TF-IDF baseline, and DoubleLingo methods using Double Machine Learning (DML), with additional baselines including BERT+Adapter and Embedding+FFN approaches.

The full paper is available at the ACL Anthology for more detailed information about the experiment design and methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "724d1311-595b-4828-bb48-6c3f6471e1b5",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "e66020b1-6a8e-4f9b-8ec2-a7d2541eda1f",
  "toolUseResult": {
    "query": "DoubleLingo NAACL 2024 LLM causal inference text confounders experiment design baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HtxK65zEATbaTsPK5ccdps",
        "content": [
          {
            "title": "DoubleLingo: Causal Estimation with Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-short.71/"
          },
          {
            "title": "[Quick Review] Causal Inference with Large Language Model: A Survey",
            "url": "https://liner.com/review/causal-inference-with-large-language-model-survey"
          },
          {
            "title": "Causal Inference with Large Language Model: A Survey - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-naacl.327/"
          },
          {
            "title": "Can Large Language Models Infer Causal Relationships from Real-World Text?",
            "url": "https://arxiv.org/pdf/2505.18931"
          },
          {
            "title": "Can Post-Training Transform LLMs into Causal Reasoners?",
            "url": "https://arxiv.org/pdf/2602.06337"
          },
          {
            "title": "LLMs Are Prone to Fallacies in Causal Inference",
            "url": "https://arxiv.org/pdf/2406.12158"
          },
          {
            "title": "DoubleLingo: Causal Estimation with Large Language ...",
            "url": "https://aclanthology.org/2024.naacl-short.71.pdf"
          }
        ]
      },
      "Based on the search results, I found information about DoubleLingo, a NAACL 2024 paper on causal inference with LLMs:\n\n## DoubleLingo: Causal Estimation with Large Language Models\n\nDoubleLingo enables theoretically consistent estimation of causal effects using LLM-based nuisance models by incorporating them within the framework of Double Machine Learning.\n\n### Problem and Motivation\n\nWhen confounders include text data, existing causal inference methods struggle due to the high dimensionality of the text. Simple statistical models which have sufficient convergence criteria for causal estimation are not well-equipped to handle noisy unstructured text, but flexible large language models that excel at predictive tasks with text data do not meet the statistical assumptions necessary for causal estimation.\n\n### Results\n\nOn the best available dataset for evaluating such methods, DoubleLingo achieves a 10.4% reduction in the relative absolute error for the estimated causal effect over existing methods.\n\n### Experimental Baselines\n\nBased on the PDF excerpt, the experimental baselines include Oracle and Unadjusted models using outcome regressions, a TF-IDF baseline, and DoubleLingo methods using Double Machine Learning (DML), with additional baselines including BERT+Adapter and Embedding+FFN approaches.\n\nThe full paper is available at the ACL Anthology for more detailed information about the experiment design and methodology."
    ],
    "durationSeconds": 6.757814081,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "724d1311-595b-4828-bb48-6c3f6471e1b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T03:49:08.302Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019eHizeK5D1FqpT83W16JpE`</summary>

```json
{
  "query": "Ma et al NeurIPS 2025 \"LLM-Driven Treatment Effect\" text confounding experiments evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e66020b1-6a8e-4f9b-8ec2-a7d2541eda1f",
  "isSidechain": false,
  "requestId": "req_011CbD8xexQWfehpe5st1uES",
  "type": "assistant",
  "uuid": "a59a9360-1f28-4e42-861e-9bf3de6c5034",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qr6yS3mcUWWMe9iJ32bSH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 23686,
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
          "cache_read_input_tokens": 23686,
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

_source line 19 · 2026-05-20T03:49:15.685Z_

<details><summary>↩ Tool result · `toolu_019eHizeK5D1FqpT83W16JpE`</summary>

```text
Web search results for query: "Ma et al NeurIPS 2025 "LLM-Driven Treatment Effect" text confounding experiments evaluation"

Links: [{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding | OpenReview","url":"https://openreview.net/forum?id=sv41aaGTit"},{"title":"[2507.02843] LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://arxiv.org/abs/2507.02843"},{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://arxiv.org/pdf/2507.02843"},{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://arxiv.org/html/2507.02843"},{"title":"MCML - MCML at NeurIPS 2025","url":"https://mcml.ai/news/2025-11-28-papers-neurips2025/"},{"title":"LLM-based Agents for Automated Confounder Discovery and Subgroup Analysis in Causal Inference","url":"https://arxiv.org/pdf/2508.07221"},{"title":"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding","url":"https://openreview.net/pdf/91cde9dca622c2cb85a4f93a3342a05cadeed265.pdf"}]

I found the research paper you're looking for. Here's what I found:

The paper "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding" by Ma et al. was published at NeurIPS 2025 as a poster presentation.

**Paper Overview:**

The work formalizes an "inference time text confounding" problem, where confounders are fully observed during training time on well-structured medical datasets but only partially available through text at inference time (such as self-reported symptoms).

**Three Main Contributions:**

(1) The authors demonstrate that discrepancies between training and inference data can lead to biased treatment effect estimates and formalize this as an inference time text confounding problem.

(2) They propose a novel framework for estimating treatment effects that explicitly accounts for this problem, leveraging large language models together with a custom doubly robust learner to mitigate biases.

(3) The framework's effectiveness is demonstrated through a series of experiments in real-world applications.

**Key Experimental Finding:**

In their experiments, their approach (TCA) substantially outperforms a baseline that uses the same underlying doubly robust estimation technique but lacks their confounding adjustment framework, highlighting that the core innovation lies in their confounding adjustment framework.

The paper and code are available on arXiv (2507.02843) and GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a59a9360-1f28-4e42-861e-9bf3de6c5034",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "d2a4c28c-694d-40d5-8397-fb14c94dc044",
  "toolUseResult": {
    "query": "Ma et al NeurIPS 2025 \"LLM-Driven Treatment Effect\" text confounding experiments evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KccuakE8cGfjj9NfXdTu5U",
        "content": [
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding | OpenReview",
            "url": "https://openreview.net/forum?id=sv41aaGTit"
          },
          {
            "title": "[2507.02843] LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://arxiv.org/abs/2507.02843"
          },
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://arxiv.org/pdf/2507.02843"
          },
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://arxiv.org/html/2507.02843"
          },
          {
            "title": "MCML - MCML at NeurIPS 2025",
            "url": "https://mcml.ai/news/2025-11-28-papers-neurips2025/"
          },
          {
            "title": "LLM-based Agents for Automated Confounder Discovery and Subgroup Analysis in Causal Inference",
            "url": "https://arxiv.org/pdf/2508.07221"
          },
          {
            "title": "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding",
            "url": "https://openreview.net/pdf/91cde9dca622c2cb85a4f93a3342a05cadeed265.pdf"
          }
        ]
      },
      "I found the research paper you're looking for. Here's what I found:\n\nThe paper \"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding\" by Ma et al. was published at NeurIPS 2025 as a poster presentation.\n\n**Paper Overview:**\n\nThe work formalizes an \"inference time text confounding\" problem, where confounders are fully observed during training time on well-structured medical datasets but only partially available through text at inference time (such as self-reported symptoms).\n\n**Three Main Contributions:**\n\n(1) The authors demonstrate that discrepancies between training and inference data can lead to biased treatment effect estimates and formalize this as an inference time text confounding problem.\n\n(2) They propose a novel framework for estimating treatment effects that explicitly accounts for this problem, leveraging large language models together with a custom doubly robust learner to mitigate biases.\n\n(3) The framework's effectiveness is demonstrated through a series of experiments in real-world applications.\n\n**Key Experimental Finding:**\n\nIn their experiments, their approach (TCA) substantially outperforms a baseline that uses the same underlying doubly robust estimation technique but lacks their confounding adjustment framework, highlighting that the core innovation lies in their confounding adjustment framework.\n\nThe paper and code are available on arXiv (2507.02843) and GitHub."
    ],
    "durationSeconds": 7.379945430999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a59a9360-1f28-4e42-861e-9bf3de6c5034",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T03:49:18.125Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AtiWHEhAzBr9mhovq7KCtv`</summary>

```json
{
  "query": "prediction-powered inference causal inference experiments 2025 2026 baselines evaluation metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2a4c28c-694d-40d5-8397-fb14c94dc044",
  "isSidechain": false,
  "requestId": "req_011CbD8yRUpMwmgowW6nEdJf",
  "type": "assistant",
  "uuid": "2f5f1ac7-0e5d-4f5d-812c-8834f53d0ab4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wJkXDRN3P9i9ZLo1wbdbZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 24437,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 24437,
          "cache_creation_input_tokens": 771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 771
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

_source line 21 · 2026-05-20T03:49:25.170Z_

<details><summary>↩ Tool result · `toolu_01AtiWHEhAzBr9mhovq7KCtv`</summary>

```text
Web search results for query: "prediction-powered inference causal inference experiments 2025 2026 baselines evaluation metrics"

Links: [{"title":"Prediction-powered inference | Science","url":"https://www.science.org/doi/10.1126/science.adi6000"},{"title":"[2502.06343] Prediction-Powered Causal Inferences","url":"https://arxiv.org/abs/2502.06343"},{"title":"Prediction-Powered Causal Inferences","url":"https://arxiv.org/html/2502.06343v3"},{"title":"[2508.01341] Debiasing Machine Learning Predictions for Causal Inference Without Additional Ground Truth Data: \"One Map, Many Trials\" in Satellite-Driven Poverty Analysis","url":"https://arxiv.org/abs/2508.01341"},{"title":"Prediction-powered inference | Request PDF","url":"https://www.researchgate.net/publication/375523918_Prediction-powered_inference"},{"title":"Prediction-powered Generalization of Causal Inferences","url":"https://arxiv.org/pdf/2406.02873"}]

I found relevant research on prediction-powered inference for causal inference. Here are the key findings:

## Recent Work on Prediction-Powered Causal Inference

Prediction-Powered Causal Inferences (PPCI) focuses on estimating treatment effects in unlabeled target experiments, relying on training data with the same outcome annotated but potentially different treatment or effect modifiers.

### Key Technical Approaches

Conditional calibration guarantees valid PPCI at population level, with a sufficient representation constraint transferring validity across experiments enforced through Deconfounded Empirical Risk Minimization, a model-agnostic training objective.

Recent causal inference extensions rely on counterfactual predictions, with PPCI focusing on imputing missing factual outcomes to generalize across similar experiments that are out-of-distribution.

### Validation and Applications

The method is validated on synthetic and real-world scientific data, solving problem instances that are impossible for standard Empirical Risk Minimization even with conventional invariance constraints.

Experimental data from randomized controlled trials (RCTs) is the gold standard for causal inference, but in addition to being time and cost-intensive, RCTs often exhibit limited external validity and their findings may not apply to target populations.

The recent research from 2025-2026 demonstrates growing interest in combining prediction models with causal inference to address practical constraints in experimental design and improve generalizability across different settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f5f1ac7-0e5d-4f5d-812c-8834f53d0ab4",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "c2e64d81-40ce-430d-936f-510bf6b02fc7",
  "toolUseResult": {
    "query": "prediction-powered inference causal inference experiments 2025 2026 baselines evaluation metrics",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BPxeQiwEKhHpoh2VZPtdzq",
        "content": [
          {
            "title": "Prediction-powered inference | Science",
            "url": "https://www.science.org/doi/10.1126/science.adi6000"
          },
          {
            "title": "[2502.06343] Prediction-Powered Causal Inferences",
            "url": "https://arxiv.org/abs/2502.06343"
          },
          {
            "title": "Prediction-Powered Causal Inferences",
            "url": "https://arxiv.org/html/2502.06343v3"
          },
          {
            "title": "[2508.01341] Debiasing Machine Learning Predictions for Causal Inference Without Additional Ground Truth Data: \"One Map, Many Trials\" in Satellite-Driven Poverty Analysis",
            "url": "https://arxiv.org/abs/2508.01341"
          },
          {
            "title": "Prediction-powered inference | Request PDF",
            "url": "https://www.researchgate.net/publication/375523918_Prediction-powered_inference"
          },
          {
            "title": "Prediction-powered Generalization of Causal Inferences",
            "url": "https://arxiv.org/pdf/2406.02873"
          }
        ]
      },
      "I found relevant research on prediction-powered inference for causal inference. Here are the key findings:\n\n## Recent Work on Prediction-Powered Causal Inference\n\nPrediction-Powered Causal Inferences (PPCI) focuses on estimating treatment effects in unlabeled target experiments, relying on training data with the same outcome annotated but potentially different treatment or effect modifiers.\n\n### Key Technical Approaches\n\nConditional calibration guarantees valid PPCI at population level, with a sufficient representation constraint transferring validity across experiments enforced through Deconfounded Empirical Risk Minimization, a model-agnostic training objective.\n\nRecent causal inference extensions rely on counterfactual predictions, with PPCI focusing on imputing missing factual outcomes to generalize across similar experiments that are out-of-distribution.\n\n### Validation and Applications\n\nThe method is validated on synthetic and real-world scientific data, solving problem instances that are impossible for standard Empirical Risk Minimization even with conventional invariance constraints.\n\nExperimental data from randomized controlled trials (RCTs) is the gold standard for causal inference, but in addition to being time and cost-intensive, RCTs often exhibit limited external validity and their findings may not apply to target populations.\n\nThe recent research from 2025-2026 demonstrates growing interest in combining prediction models with causal inference to address practical constraints in experimental design and improve generalizability across different settings."
    ],
    "durationSeconds": 7.039967615000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2f5f1ac7-0e5d-4f5d-812c-8834f53d0ab4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
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
  "lastPrompt": "# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Description We propose ConformalPPITextCausal, a framework providing finite-sample coverage g…",
  "leafUuid": "c2e64d81-40ce-430d-936f-510bf6b02fc7",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Tool call

_source line 24 · 2026-05-20T03:49:28.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NwfCeajqo8eWckHFFmz5dq`</summary>

```json
{
  "query": "Zhang et al 2510.04406 modular conformal prediction sequential pipelines experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2e64d81-40ce-430d-936f-510bf6b02fc7",
  "isSidechain": false,
  "requestId": "req_011CbD8z86aeU9YBY9aAr4ZT",
  "type": "assistant",
  "uuid": "17ce5fb7-1277-47bf-901d-45f393c2a2ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLiQnRUM1PycXDN1u2pEPs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 25208,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 25208,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 25 · 2026-05-20T03:49:33.684Z_

<details><summary>↩ Tool result · `toolu_01NwfCeajqo8eWckHFFmz5dq`</summary>

```text
Web search results for query: "Zhang et al 2510.04406 modular conformal prediction sequential pipelines experiments"

Links: [{"title":"[2510.04406] Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/abs/2510.04406"},{"title":"[2510.04406v1] Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/abs/2510.04406v1"},{"title":"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/pdf/2510.04406"},{"title":"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/html/2510.04406v1"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/stat.ML/2025-10?skip=25&show=25"}]

Based on the search results, I found the paper you're looking for:

**Title:** Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition

**Authors:** William Zhang, Saurabh Amin, and Georgia Perakis

**Main Contribution:** The paper introduces a conformal prediction framework for two-stage sequential models, where an upstream predictor generates intermediate representations for a downstream model. By decomposing the overall prediction residual into stage-specific components, their method enables practitioners to attribute uncertainty to specific pipeline stages.

**Methods:** The authors develop a risk-controlled parameter selection procedure using family-wise error rate (FWER) control to calibrate stage-wise scaling parameters, and propose an adaptive extension for non-stationary settings that preserves long-run coverage guarantees.

**Experiments:** Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that their approach maintains coverage under conditions that degrade standard conformal methods, while providing interpretable stage-wise uncertainty attribution.

The paper was submitted on October 6, 2025, and is available on arXiv at https://arxiv.org/abs/2510.04406.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17ce5fb7-1277-47bf-901d-45f393c2a2ec",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "1aee1ed4-190e-4d81-93cc-df55c130e2f9",
  "toolUseResult": {
    "query": "Zhang et al 2510.04406 modular conformal prediction sequential pipelines experiments",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TsCw66YsABDwPaRCumsxVw",
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
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition\n\n**Authors:** William Zhang, Saurabh Amin, and Georgia Perakis\n\n**Main Contribution:** The paper introduces a conformal prediction framework for two-stage sequential models, where an upstream predictor generates intermediate representations for a downstream model. By decomposing the overall prediction residual into stage-specific components, their method enables practitioners to attribute uncertainty to specific pipeline stages.\n\n**Methods:** The authors develop a risk-controlled parameter selection procedure using family-wise error rate (FWER) control to calibrate stage-wise scaling parameters, and propose an adaptive extension for non-stationary settings that preserves long-run coverage guarantees.\n\n**Experiments:** Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that their approach maintains coverage under conditions that degrade standard conformal methods, while providing interpretable stage-wise uncertainty attribution.\n\nThe paper was submitted on October 6, 2025, and is available on arXiv at https://arxiv.org/abs/2510.04406."
    ],
    "durationSeconds": 5.629036545999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "17ce5fb7-1277-47bf-901d-45f393c2a2ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T03:49:36.204Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016W9vV4GhP5qpvc6e4Zcu9x`</summary>

```json
{
  "query": "Csillag et al 2510.16166 conformal prediction powered inference experiments evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aee1ed4-190e-4d81-93cc-df55c130e2f9",
  "isSidechain": false,
  "requestId": "req_011CbD8zkTrXkCXrRBPFEaR3",
  "type": "assistant",
  "uuid": "3106d479-2ca9-4b7f-a712-6e1e3e829907",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mfowL6cGgakZSzgTuc5Sm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 630,
      "cache_read_input_tokens": 25902,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 25902,
          "cache_creation_input_tokens": 630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 630
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

_source line 27 · 2026-05-20T03:49:42.446Z_

<details><summary>↩ Tool result · `toolu_016W9vV4GhP5qpvc6e4Zcu9x`</summary>

```text
Web search results for query: "Csillag et al 2510.16166 conformal prediction powered inference experiments evaluation"

Links: [{"title":"[2510.16166] Extending Prediction-Powered Inference through Conformal Prediction","url":"https://arxiv.org/abs/2510.16166"},{"title":"Published as a preprint EXTENDING PREDICTION-POWERED INFERENCE","url":"https://arxiv.org/pdf/2510.16166"},{"title":"Conformal Prediction Beyond the Horizon: Distribution-Free Inference for Policy Evaluation","url":"https://arxiv.org/html/2510.26026"},{"title":"Extending Prediction-Powered Inference through Conformal Prediction","url":"https://arxiv.org/html/2510.16166v1"},{"title":"Prediction-powered inference | Request PDF","url":"https://www.researchgate.net/publication/375523918_Prediction-powered_inference"},{"title":"Powerful batch conformal prediction for classification","url":"https://arxiv.org/pdf/2411.02239"}]

Based on the search results, I found the paper you're looking for:

The paper "Extending Prediction-Powered Inference through Conformal Prediction" by Csillag et al. (arXiv:2510.16166) is about prediction-powered inference as a recent methodology for the safe use of black-box ML models to impute missing data and strengthen inference of statistical parameters.

The main contribution is connecting prediction-powered inference with conformal prediction by performing imputation through a calibrated conformal set-predictor to attain validity while achieving additional guarantees.

The authors instantiate their procedure for the inference of means, Z- and M-estimation, as well as e-values and e-value-based procedures. Furthermore, in the case of e-values, theirs is the first general prediction-powered procedure that operates off-line.

By using a calibrated set-predictor for prediction-powered inference, the approach inherits additional properties from conformal calibration, allowing it to leverage the conformal prediction literature with additional guarantees spanning privacy, robustness to distribution shift, robustness to outliers, and censored/missing data.

The paper was published on October 17, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3106d479-2ca9-4b7f-a712-6e1e3e829907",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "17e5b87b-b1a2-4399-82fd-8e2af1dbd7ad",
  "toolUseResult": {
    "query": "Csillag et al 2510.16166 conformal prediction powered inference experiments evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SNjNFjTPyYDxzyZAc8nNZ7",
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
            "title": "Conformal Prediction Beyond the Horizon: Distribution-Free Inference for Policy Evaluation",
            "url": "https://arxiv.org/html/2510.26026"
          },
          {
            "title": "Extending Prediction-Powered Inference through Conformal Prediction",
            "url": "https://arxiv.org/html/2510.16166v1"
          },
          {
            "title": "Prediction-powered inference | Request PDF",
            "url": "https://www.researchgate.net/publication/375523918_Prediction-powered_inference"
          },
          {
            "title": "Powerful batch conformal prediction for classification",
            "url": "https://arxiv.org/pdf/2411.02239"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Extending Prediction-Powered Inference through Conformal Prediction\" by Csillag et al. (arXiv:2510.16166) is about prediction-powered inference as a recent methodology for the safe use of black-box ML models to impute missing data and strengthen inference of statistical parameters.\n\nThe main contribution is connecting prediction-powered inference with conformal prediction by performing imputation through a calibrated conformal set-predictor to attain validity while achieving additional guarantees.\n\nThe authors instantiate their procedure for the inference of means, Z- and M-estimation, as well as e-values and e-value-based procedures. Furthermore, in the case of e-values, theirs is the first general prediction-powered procedure that operates off-line.\n\nBy using a calibrated set-predictor for prediction-powered inference, the approach inherits additional properties from conformal calibration, allowing it to leverage the conformal prediction literature with additional guarantees spanning privacy, robustness to distribution shift, robustness to outliers, and censored/missing data.\n\nThe paper was published on October 17, 2025."
    ],
    "durationSeconds": 6.2375867410000065,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3106d479-2ca9-4b7f-a712-6e1e3e829907",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T03:49:45.042Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EgKJGTuk7iMUwzJpPj7hns`</summary>

```json
{
  "query": "MIMIC-IV causal inference text confounders benchmark semi-synthetic evaluation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17e5b87b-b1a2-4399-82fd-8e2af1dbd7ad",
  "isSidechain": false,
  "requestId": "req_011CbD91Pxb9JMybzzdJUGyB",
  "type": "assistant",
  "uuid": "e501b038-3882-4cd6-9782-c4131c060c40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJuxxcE69ux6K7pSQmrvKF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 26532,
      "output_tokens": 74,
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
          "output_tokens": 74,
          "cache_read_input_tokens": 26532,
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

_source line 29 · 2026-05-20T03:49:53.047Z_

<details><summary>↩ Tool result · `toolu_01EgKJGTuk7iMUwzJpPj7hns`</summary>

```text
Web search results for query: "MIMIC-IV causal inference text confounders benchmark semi-synthetic evaluation 2024 2025"

Links: [{"title":"Proximal Causal Inference With Text Data","url":"https://arxiv.org/pdf/2401.06687"},{"title":"Text Rationalization for Robust Causal Effect Estimation","url":"https://arxiv.org/pdf/2512.05373"},{"title":"Adjusting for Confounders with Text: Challenges and an Empirical   Evaluation Framework for Causal Inference","url":"https://arxiv.org/pdf/2009.09961"},{"title":"An Open Benchmark for Causal Inference Using the MIMIC ...","url":"http://mghassem.mit.edu/wp-content/uploads/2013/02/Ghassemi_OHDSI_Submission2016.pdf"},{"title":"CausalProfiler: Generating Synthetic Benchmarks for ...","url":"https://www.arxiv.org/pdf/2511.22842"},{"title":"Text and Causal Inference: A Review of Using Text to Remove Confounding   from Causal Estimates","url":"https://arxiv.org/pdf/2005.00649"}]

Based on the web search results, here are the key findings related to your query about MIMIC-IV, causal inference, text confounders, benchmarks, and semi-synthetic evaluation:

## Recent Research on Text-Based Causal Inference with MIMIC Data

A study on proximal causal inference with text data evaluated the method in semi-synthetic settings using real-world clinical notes from MIMIC-III and found that the method produces estimates with low bias.

Another recent framework called Confounding-Aware Token Rationalization (CATR) selects sparse subsets of tokens to preserve confounding information and mitigate observational-level positivity violations, stabilizing downstream causal effect estimators. Experiments using the MIMIC-III database demonstrate that CATR yields more accurate, stable, and interpretable causal effect estimates than existing baselines.

## Benchmark Development for Text-Based Causal Inference

While semi-synthetic benchmarks exist for medical causal inference, the first evaluation framework for causal inference with text was contributed in a comprehensive study. This framework consists of five semi-synthetic tasks (Linguistic Complexity, Signal Intensity, Strength of Selection Effect, Sample Size, and Placebo Test) generated from public social media users' profiles and perturbed with synthetic posts to create increasing levels of difficulty.

The search results primarily reference MIMIC-III rather than MIMIC-IV specifically, and focus on evaluations from 2020-2025. If you need more specific information about MIMIC-IV benchmarks, I can conduct an additional search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e501b038-3882-4cd6-9782-c4131c060c40",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "17b52aca-205b-4972-af44-52074faa8e8c",
  "toolUseResult": {
    "query": "MIMIC-IV causal inference text confounders benchmark semi-synthetic evaluation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011ZFnbW9H41iPo8ZhXCwfJs",
        "content": [
          {
            "title": "Proximal Causal Inference With Text Data",
            "url": "https://arxiv.org/pdf/2401.06687"
          },
          {
            "title": "Text Rationalization for Robust Causal Effect Estimation",
            "url": "https://arxiv.org/pdf/2512.05373"
          },
          {
            "title": "Adjusting for Confounders with Text: Challenges and an Empirical   Evaluation Framework for Causal Inference",
            "url": "https://arxiv.org/pdf/2009.09961"
          },
          {
            "title": "An Open Benchmark for Causal Inference Using the MIMIC ...",
            "url": "http://mghassem.mit.edu/wp-content/uploads/2013/02/Ghassemi_OHDSI_Submission2016.pdf"
          },
          {
            "title": "CausalProfiler: Generating Synthetic Benchmarks for ...",
            "url": "https://www.arxiv.org/pdf/2511.22842"
          },
          {
            "title": "Text and Causal Inference: A Review of Using Text to Remove Confounding   from Causal Estimates",
            "url": "https://arxiv.org/pdf/2005.00649"
          }
        ]
      },
      "Based on the web search results, here are the key findings related to your query about MIMIC-IV, causal inference, text confounders, benchmarks, and semi-synthetic evaluation:\n\n## Recent Research on Text-Based Causal Inference with MIMIC Data\n\nA study on proximal causal inference with text data evaluated the method in semi-synthetic settings using real-world clinical notes from MIMIC-III and found that the method produces estimates with low bias.\n\nAnother recent framework called Confounding-Aware Token Rationalization (CATR) selects sparse subsets of tokens to preserve confounding information and mitigate observational-level positivity violations, stabilizing downstream causal effect estimators. Experiments using the MIMIC-III database demonstrate that CATR yields more accurate, stable, and interpretable causal effect estimates than existing baselines.\n\n## Benchmark Development for Text-Based Causal Inference\n\nWhile semi-synthetic benchmarks exist for medical causal inference, the first evaluation framework for causal inference with text was contributed in a comprehensive study. This framework consists of five semi-synthetic tasks (Linguistic Complexity, Signal Intensity, Strength of Selection Effect, Sample Size, and Placebo Test) generated from public social media users' profiles and perturbed with synthetic posts to create increasing levels of difficulty.\n\nThe search results primarily reference MIMIC-III rather than MIMIC-IV specifically, and focus on evaluations from 2020-2025. If you need more specific information about MIMIC-IV benchmarks, I can conduct an additional search."
    ],
    "durationSeconds": 8.000957347000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e501b038-3882-4cd6-9782-c4131c060c40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T03:49:53.051Z_

```json
{
  "parentUuid": "17b52aca-205b-4972-af44-52074faa8e8c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "daa8c3dc-3b55-4ec9-b139-bac16bd32fb9",
  "timestamp": "2026-05-20T03:49:53.051Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T03:49:55.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E5brHxY8dXNtDKpTxUF2H6`</summary>

```json
{
  "query": "conformal prediction ITE individual treatment effects coverage width metrics ablation experiments 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daa8c3dc-3b55-4ec9-b139-bac16bd32fb9",
  "isSidechain": false,
  "requestId": "req_011CbD92BGdfU349HcRFWsa9",
  "type": "assistant",
  "uuid": "aefe455b-fac6-43ee-875e-e548756cebe8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjDjZKUmJqRN9EcWWrjiWu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 27155,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 27155,
          "cache_creation_input_tokens": 847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 847
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

_source line 32 · 2026-05-20T03:50:04.829Z_

<details><summary>↩ Tool result · `toolu_01E5brHxY8dXNtDKpTxUF2H6`</summary>

```text
Web search results for query: "conformal prediction ITE individual treatment effects coverage width metrics ablation experiments 2024 2025"

Links: [{"title":"[2402.04906v6] Conformal Convolution and Monte Carlo Meta-learners for Predictive Inference of Individual Treatment Effects","url":"https://arxiv.org/abs/2402.04906v6"},{"title":"Conformal Inference of Individual Treatment Effects Using Conditional Density","url":"https://ojs.aaai.org/index.php/AAAI/article/view/35397/37552"},{"title":"Conformal Inference of Individual Treatment Effects Using Conditional Density","url":"https://arxiv.org/pdf/2501.14933"},{"title":"Conformal Inference of Individual Treatment Effects Using Conditional Density Estimates","url":"https://arxiv.org/html/2501.14933v1"},{"title":"(PDF) Conformal Inference for Counterfactuals and Individual Treatment Effects with Experiment Attrition","url":"https://www.researchgate.net/publication/403430038_Conformal_Inference_for_Counterfactuals_and_Individual_Treatment_Effects_with_Experiment_Attrition"},{"title":"[2501.14933] Conformal Inference of Individual Treatment Effects Using Conditional Density Estimates","url":"https://arxiv.org/abs/2501.14933"},{"title":"A Systematic Review of Conformal Inference Procedures for","url":"https://www.arxiv.org/pdf/2509.21660"},{"title":"PREDICTION INTERVALS FOR INDIVIDUAL TREATMENT EFFECTS","url":"https://arxiv.org/pdf/2512.08828"},{"title":"(PDF) Conformal Meta-learners for Predictive Inference of Individual Treatment Effects","url":"https://www.researchgate.net/publication/373487555_Conformal_Meta-learners_for_Predictive_Inference_of_Individual_Treatment_Effects"},{"title":"Prediction Intervals for Individual Treatment Effects in a Multiple Decision Point Framework using Conformal Inference","url":"https://arxiv.org/html/2512.08828"}]

I found several relevant papers on conformal prediction for individual treatment effects (ITE) coverage and width metrics from 2024-2025. Here are the key findings:

## Recent Papers on Conformal Prediction for ITE

**1. Conformal Convolution and Monte Carlo Meta-learners (2024-2025)**

Jonkers and colleagues propose two novel methods: the conformal convolution T-learner (CCT) and the conformal Monte Carlo (CMC) meta-learner, that generate full predictive distributions of both potential outcomes and ITEs. Experiments on synthetic and semi-synthetic datasets demonstrate that the proposed methods achieve probabilistically calibrated predictive distributions while maintaining narrow prediction intervals and having performant continuous ranked probability scores. The CCT and CMC meta-learners show significant efficiency gains compared to other conformal approaches that produce prediction intervals for ITE with coverage guarantees.

**2. Conformal Inference Using Conditional Density Estimates (January 2025)**

A recent method shows that prediction intervals are not only marginally valid but are narrower than existing methods, with experimental results validating the usefulness of the approach. Although the conformal framework is model-agnostic and always achieves a coverage guarantee, the average length of resulting prediction intervals can highly rely on the choice of the score functions.

**3. Foundational Meta-Learner Approaches**

Conformal meta-learners based on commonly used CATE meta-learners, such as the doubly-robust learner, satisfy a model- and distribution-free stochastic dominance condition, making their conformal inferences valid for practically-relevant levels of target coverage. Numerical experiments show that conformal meta-learners provide valid intervals with competitive efficiency while retaining the favorable point estimation properties of CATE meta-learners.

**4. Longitudinal Settings (December 2025)**

Recent work extends conformal inference theory to the longitudinal, non-exchangeable setting for ITEs with novel theoretical contributions.

These papers collectively focus on achieving valid coverage while minimizing prediction interval width—key metrics for practical applications in healthcare, policy, and marketing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aefe455b-fac6-43ee-875e-e548756cebe8",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "8b1d2279-0342-4271-978c-7089eee2bda1",
  "toolUseResult": {
    "query": "conformal prediction ITE individual treatment effects coverage width metrics ablation experiments 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FDX1rCW2LbbnysYKxwZpx9",
        "content": [
          {
            "title": "[2402.04906v6] Conformal Convolution and Monte Carlo Meta-learners for Predictive Inference of Individual Treatment Effects",
            "url": "https://arxiv.org/abs/2402.04906v6"
          },
          {
            "title": "Conformal Inference of Individual Treatment Effects Using Conditional Density",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/35397/37552"
          },
          {
            "title": "Conformal Inference of Individual Treatment Effects Using Conditional Density",
            "url": "https://arxiv.org/pdf/2501.14933"
          },
          {
            "title": "Conformal Inference of Individual Treatment Effects Using Conditional Density Estimates",
            "url": "https://arxiv.org/html/2501.14933v1"
          },
          {
            "title": "(PDF) Conformal Inference for Counterfactuals and Individual Treatment Effects with Experiment Attrition",
            "url": "https://www.researchgate.net/publication/403430038_Conformal_Inference_for_Counterfactuals_and_Individual_Treatment_Effects_with_Experiment_Attrition"
          },
          {
            "title": "[2501.14933] Conformal Inference of Individual Treatment Effects Using Conditional Density Estimates",
            "url": "https://arxiv.org/abs/2501.14933"
          },
          {
            "title": "A Systematic Review of Conformal Inference Procedures for",
            "url": "https://www.arxiv.org/pdf/2509.21660"
          },
          {
            "title": "PREDICTION INTERVALS FOR INDIVIDUAL TREATMENT EFFECTS",
            "url": "https://arxiv.org/pdf/2512.08828"
          },
          {
            "title": "(PDF) Conformal Meta-learners for Predictive Inference of Individual Treatment Effects",
            "url": "https://www.researchgate.net/publication/373487555_Conformal_Meta-learners_for_Predictive_Inference_of_Individual_Treatment_Effects"
          },
          {
            "title": "Prediction Intervals for Individual Treatment Effects in a Multiple Decision Point Framework using Conformal Inference",
            "url": "https://arxiv.org/html/2512.08828"
          }
        ]
      },
      "I found several relevant papers on conformal prediction for individual treatment effects (ITE) coverage and width metrics from 2024-2025. Here are the key findings:\n\n## Recent Papers on Conformal Prediction for ITE\n\n**1. Conformal Convolution and Monte Carlo Meta-learners (2024-2025)**\n\nJonkers and colleagues propose two novel methods: the conformal convolution T-learner (CCT) and the conformal Monte Carlo (CMC) meta-learner, that generate full predictive distributions of both potential outcomes and ITEs. Experiments on synthetic and semi-synthetic datasets demonstrate that the proposed methods achieve probabilistically calibrated predictive distributions while maintaining narrow prediction intervals and having performant continuous ranked probability scores. The CCT and CMC meta-learners show significant efficiency gains compared to other conformal approaches that produce prediction intervals for ITE with coverage guarantees.\n\n**2. Conformal Inference Using Conditional Density Estimates (January 2025)**\n\nA recent method shows that prediction intervals are not only marginally valid but are narrower than existing methods, with experimental results validating the usefulness of the approach. Although the conformal framework is model-agnostic and always achieves a coverage guarantee, the average length of resulting prediction intervals can highly rely on the choice of the score functions.\n\n**3. Foundational Meta-Learner Approaches**\n\nConformal meta-learners based on commonly used CATE meta-learners, such as the doubly-robust learner, satisfy a model- and distribution-free stochastic dominance condition, making their conformal inferences valid for practically-relevant levels of target coverage. Numerical experiments show that conformal meta-learners provide valid intervals with competitive efficiency while retaining the favorable point estimation properties of CATE meta-learners.\n\n**4. Longitudinal Settings (December 2025)**\n\nRecent work extends conformal inference theory to the longitudinal, non-exchangeable setting for ITEs with novel theoretical contributions.\n\nThese papers collectively focus on achieving valid coverage while minimizing prediction interval width—key metrics for practical applications in healthcare, policy, and marketing."
    ],
    "durationSeconds": 9.072020734999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "aefe455b-fac6-43ee-875e-e548756cebe8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T03:50:07.452Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QEcE6U8cz5XmFJJP1Qvfqo`</summary>

```json
{
  "query": "Barnatchez 2604.03772 conformal counterfactual runtime confounding experiments baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b1d2279-0342-4271-978c-7089eee2bda1",
  "isSidechain": false,
  "requestId": "req_011CbD933eGpbd6WQtSEMeNN",
  "type": "assistant",
  "uuid": "86914393-d2fb-4323-944c-daf80b2b8f7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZWkNmZJKJFhVRMHTNwjck",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 28002,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 28002,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1083
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

_source line 34 · 2026-05-20T03:50:12.919Z_

<details><summary>↩ Tool result · `toolu_01QEcE6U8cz5XmFJJP1Qvfqo`</summary>

```text
Web search results for query: "Barnatchez 2604.03772 conformal counterfactual runtime confounding experiments baselines"

Links: [{"title":"[2604.03772] Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/abs/2604.03772"},{"title":"[2604.03772v1] Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/abs/2604.03772v1"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/html/2604.03772"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/pdf/2604.03772"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding - AI Research Paper Analysis | ArxivLens - Arxivlens","url":"https://arxivlens.com/PaperView/Details/debiased-machine-learning-for-conformal-prediction-of-counterfactual-outcomes-under-runtime-confounding-3519-d149b03f"}]

The search has located the paper you're looking for. Here are the details:

The paper is titled "Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding" by Keith Barnatchez, Kevin P. Josey, Rachel C. Nethery, and Giovanni Parmigiani.

The paper introduces a computationally efficient debiased machine learning framework that allows for valid prediction intervals when only a subset of confounders is measured in the target population, a common challenge referred to as runtime confounding. Grounded in semiparametric efficiency theory, the resulting prediction intervals achieve desired coverage rates with faster convergence compared to standard methods.

The paper was submitted on April 4, 2026, and is available on arXiv at https://arxiv.org/abs/2604.03772.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86914393-d2fb-4323-944c-daf80b2b8f7a",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "6038fe6c-4a1a-4b07-be83-7192c27ab04f",
  "toolUseResult": {
    "query": "Barnatchez 2604.03772 conformal counterfactual runtime confounding experiments baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F3m5Zadm3oR8GmemYB5MHY",
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
      "The search has located the paper you're looking for. Here are the details:\n\nThe paper is titled \"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding\" by Keith Barnatchez, Kevin P. Josey, Rachel C. Nethery, and Giovanni Parmigiani.\n\nThe paper introduces a computationally efficient debiased machine learning framework that allows for valid prediction intervals when only a subset of confounders is measured in the target population, a common challenge referred to as runtime confounding. Grounded in semiparametric efficiency theory, the resulting prediction intervals achieve desired coverage rates with faster convergence compared to standard methods.\n\nThe paper was submitted on April 4, 2026, and is available on arXiv at https://arxiv.org/abs/2604.03772."
    ],
    "durationSeconds": 5.463280293000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "86914393-d2fb-4323-944c-daf80b2b8f7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
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
  "lastPrompt": "# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Description We propose ConformalPPITextCausal, a framework providing finite-sample coverage g…",
  "leafUuid": "6038fe6c-4a1a-4b07-be83-7192c27ab04f",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Tool call

_source line 37 · 2026-05-20T03:50:16.093Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Su2CSNpKxGcvtbLZ86Htn`</summary>

```json
{
  "query": "Alaa et al NeurIPS 2023 conformal meta-learners ITE experiments datasets IHDP ACIC baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6038fe6c-4a1a-4b07-be83-7192c27ab04f",
  "isSidechain": false,
  "requestId": "req_011CbD93eXVmBXVXbDCU2bGE",
  "type": "assistant",
  "uuid": "a4f7c3e3-add5-42e4-9d17-50c29c125c35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2hMVRehUZ6q2UsDrqt2US",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 29085,
      "output_tokens": 83,
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
          "output_tokens": 83,
          "cache_read_input_tokens": 29085,
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

### Tool result

_source line 38 · 2026-05-20T03:50:22.520Z_

<details><summary>↩ Tool result · `toolu_017Su2CSNpKxGcvtbLZ86Htn`</summary>

```text
Web search results for query: "Alaa et al NeurIPS 2023 conformal meta-learners ITE experiments datasets IHDP ACIC baselines"

Links: [{"title":"Conformal Inference of Individual Treatment Effects Using Conditional Density","url":"https://ojs.aaai.org/index.php/AAAI/article/download/35397/37552"},{"title":"GitHub - AlaaLab/conformal-metalearners: [ NeurIPS 2023 ] Official Codebase for \"Conformal Meta-learners for Predictive Inference of Individual Treatment Effects\"","url":"https://github.com/AlaaLab/conformal-metalearners"},{"title":"Conformal Meta-learners for Predictive Inference of ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/94ab02a30b0e4a692a42ccd0b4c55399-Paper-Conference.pdf"},{"title":"(PDF) Conformal Meta-learners for Predictive Inference of Individual Treatment Effects","url":"https://www.researchgate.net/publication/373487555_Conformal_Meta-learners_for_Predictive_Inference_of_Individual_Treatment_Effects"},{"title":"NeurIPS Poster Conformal Meta-learners for Predictive Inference of Individual Treatment Effects","url":"https://neurips.cc/virtual/2023/poster/72090"},{"title":"Conformal Meta-learners for Predictive Inference of Individual Treatment   Effects","url":"https://arxiv.org/pdf/2308.14895"},{"title":"Conformal Convolution and Monte Carlo Meta-learners for Predictive Inference of Individual Treatment Effects","url":"https://arxiv.org/pdf/2402.04906"},{"title":"Conformal Meta-learners for Predictive Inference of ...","url":"https://nips.cc/virtual/2023/oral/73862"}]

I found relevant information about the Alaa et al. NeurIPS 2023 paper on conformal meta-learners. Here are the key findings:

## Paper Overview

The paper "Conformal Meta-learners for Predictive Inference of Individual Treatment Effects" by Ahmed M. Alaa, Zaid Ahmad, and Mark van der Laan develops a general framework for issuing predictive intervals for ITEs by applying conformal prediction on top of CATE meta-learners.

## Datasets Used

The experiments use three dataset types: "Synthetic", "IHDP", and "NLSM". The IHDP (Infant Health and Development Program) dataset and the ACIC (Atlantic Causal Inference Conference) datasets were used in the experiments.

## Meta-learner Baselines

The meta-learner baselines tested are "X", "DR" (doubly-robust), and "IPW" (inverse probability weighting).

## Key Experimental Results

The DR-learner outperforms all baselines on the IHDP dataset in terms of RMSE and interval efficiency, while achieving the desired coverage of 90%. The numerical experiments show that conformal meta-learners provide valid intervals with competitive efficiency while retaining the favorable point estimation properties of CATE meta-learners.

## Code Availability

The official codebase is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4f7c3e3-add5-42e4-9d17-50c29c125c35",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "40699e84-e5ed-487f-b61c-7151e63a38f1",
  "toolUseResult": {
    "query": "Alaa et al NeurIPS 2023 conformal meta-learners ITE experiments datasets IHDP ACIC baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WJzh7p9c3wVvXDvSTi18rS",
        "content": [
          {
            "title": "Conformal Inference of Individual Treatment Effects Using Conditional Density",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/download/35397/37552"
          },
          {
            "title": "GitHub - AlaaLab/conformal-metalearners: [ NeurIPS 2023 ] Official Codebase for \"Conformal Meta-learners for Predictive Inference of Individual Treatment Effects\"",
            "url": "https://github.com/AlaaLab/conformal-metalearners"
          },
          {
            "title": "Conformal Meta-learners for Predictive Inference of ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/94ab02a30b0e4a692a42ccd0b4c55399-Paper-Conference.pdf"
          },
          {
            "title": "(PDF) Conformal Meta-learners for Predictive Inference of Individual Treatment Effects",
            "url": "https://www.researchgate.net/publication/373487555_Conformal_Meta-learners_for_Predictive_Inference_of_Individual_Treatment_Effects"
          },
          {
            "title": "NeurIPS Poster Conformal Meta-learners for Predictive Inference of Individual Treatment Effects",
            "url": "https://neurips.cc/virtual/2023/poster/72090"
          },
          {
            "title": "Conformal Meta-learners for Predictive Inference of Individual Treatment   Effects",
            "url": "https://arxiv.org/pdf/2308.14895"
          },
          {
            "title": "Conformal Convolution and Monte Carlo Meta-learners for Predictive Inference of Individual Treatment Effects",
            "url": "https://arxiv.org/pdf/2402.04906"
          },
          {
            "title": "Conformal Meta-learners for Predictive Inference of ...",
            "url": "https://nips.cc/virtual/2023/oral/73862"
          }
        ]
      },
      "I found relevant information about the Alaa et al. NeurIPS 2023 paper on conformal meta-learners. Here are the key findings:\n\n## Paper Overview\n\nThe paper \"Conformal Meta-learners for Predictive Inference of Individual Treatment Effects\" by Ahmed M. Alaa, Zaid Ahmad, and Mark van der Laan develops a general framework for issuing predictive intervals for ITEs by applying conformal prediction on top of CATE meta-learners.\n\n## Datasets Used\n\nThe experiments use three dataset types: \"Synthetic\", \"IHDP\", and \"NLSM\". The IHDP (Infant Health and Development Program) dataset and the ACIC (Atlantic Causal Inference Conference) datasets were used in the experiments.\n\n## Meta-learner Baselines\n\nThe meta-learner baselines tested are \"X\", \"DR\" (doubly-robust), and \"IPW\" (inverse probability weighting).\n\n## Key Experimental Results\n\nThe DR-learner outperforms all baselines on the IHDP dataset in terms of RMSE and interval efficiency, while achieving the desired coverage of 90%. The numerical experiments show that conformal meta-learners provide valid intervals with competitive efficiency while retaining the favorable point estimation properties of CATE meta-learners.\n\n## Code Availability\n\nThe official codebase is available on GitHub."
    ],
    "durationSeconds": 6.424133923000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a4f7c3e3-add5-42e4-9d17-50c29c125c35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T03:50:25.418Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YL9bBKChyRhZ42a2BgeWV1`</summary>

```json
{
  "query": "Kato 2511.08303 semi-supervised treatment effect PPI NeurIPS 2025 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40699e84-e5ed-487f-b61c-7151e63a38f1",
  "isSidechain": false,
  "requestId": "req_011CbD94MFhvTXHHDom5M3vc",
  "type": "assistant",
  "uuid": "080e4beb-4bf7-4bee-b0b2-a35d0eb60f52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyJivMH9Dbf9QoTwJttvsY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 29724,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 29724,
          "cache_creation_input_tokens": 900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 900
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

_source line 40 · 2026-05-20T03:50:31.534Z_

<details><summary>↩ Tool result · `toolu_01YL9bBKChyRhZ42a2BgeWV1`</summary>

```text
Web search results for query: "Kato 2511.08303 semi-supervised treatment effect PPI NeurIPS 2025 experiments"

Links: [{"title":"[2511.08303] Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression","url":"https://arxiv.org/abs/2511.08303"},{"title":"Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates for Prediction-Powered Causal Inference","url":"https://arxiv.org/html/2511.08303"},{"title":"Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression","url":"https://arxiv.org/html/2511.08303v1"},{"title":"NeurIPS Poster Prediction-Powered Semi-Supervised Learning with Online Power Tuning","url":"https://neurips.cc/virtual/2025/poster/116027"},{"title":"Counterfactual Propagation for Semi-Supervised Individual Treatment   Effect Estimation","url":"https://arxiv.org/pdf/2005.05099"},{"title":"Semi-supervised inference for treatment heterogeneity","url":"https://arxiv.org/pdf/2509.05048"}]

Based on the search results, I found relevant information about the paper you're asking about:

The paper investigates treatment effect estimation in the semi-supervised setting, where it uses not only the standard triple of covariates, treatment indicator, and outcome, but also unlabeled auxiliary covariates. 

The study develops efficiency bounds and efficient estimators whose asymptotic variance aligns with the efficiency bound.

The paper presents two different data-generating scenarios: the one-sample setting where treatment indicators and outcomes can be observed for a part of the dataset (called the censoring setting), and the two-sample setting which considers two independent datasets with labeled and unlabeled data (also called the case-control setting or the stratified setting).

In both settings, the paper finds that by incorporating auxiliary covariates, the efficiency bound can be lowered and an estimator with an asymptotic variance smaller than that without can be obtained.

The paper was posted on arXiv on November 11, 2025, and is authored by Masahiro Kato. While I found references to the paper's content, the search results don't contain detailed information about specific numerical experiments or NeurIPS 2025 presentation details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "080e4beb-4bf7-4bee-b0b2-a35d0eb60f52",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "0dda3cb8-8874-4e59-be77-59d372fd325f",
  "toolUseResult": {
    "query": "Kato 2511.08303 semi-supervised treatment effect PPI NeurIPS 2025 experiments",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S9QRRWXGmQsg9dSPFbzH8h",
        "content": [
          {
            "title": "[2511.08303] Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression",
            "url": "https://arxiv.org/abs/2511.08303"
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
            "title": "NeurIPS Poster Prediction-Powered Semi-Supervised Learning with Online Power Tuning",
            "url": "https://neurips.cc/virtual/2025/poster/116027"
          },
          {
            "title": "Counterfactual Propagation for Semi-Supervised Individual Treatment   Effect Estimation",
            "url": "https://arxiv.org/pdf/2005.05099"
          },
          {
            "title": "Semi-supervised inference for treatment heterogeneity",
            "url": "https://arxiv.org/pdf/2509.05048"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper you're asking about:\n\nThe paper investigates treatment effect estimation in the semi-supervised setting, where it uses not only the standard triple of covariates, treatment indicator, and outcome, but also unlabeled auxiliary covariates. \n\nThe study develops efficiency bounds and efficient estimators whose asymptotic variance aligns with the efficiency bound.\n\nThe paper presents two different data-generating scenarios: the one-sample setting where treatment indicators and outcomes can be observed for a part of the dataset (called the censoring setting), and the two-sample setting which considers two independent datasets with labeled and unlabeled data (also called the case-control setting or the stratified setting).\n\nIn both settings, the paper finds that by incorporating auxiliary covariates, the efficiency bound can be lowered and an estimator with an asymptotic variance smaller than that without can be obtained.\n\nThe paper was posted on arXiv on November 11, 2025, and is authored by Masahiro Kato. While I found references to the paper's content, the search results don't contain detailed information about specific numerical experiments or NeurIPS 2025 presentation details."
    ],
    "durationSeconds": 6.110939169000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "080e4beb-4bf7-4bee-b0b2-a35d0eb60f52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T03:50:34.059Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VCRhBtPz8cRXyesUyLq1pe`</summary>

```json
{
  "query": "conformal prediction text classification NLP LLM extraction uncertainty quantification experiments 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dda3cb8-8874-4e59-be77-59d372fd325f",
  "isSidechain": false,
  "requestId": "req_011CbD951pCK9Lyp5gxJKueW",
  "type": "assistant",
  "uuid": "cd29ff87-9df7-4026-8f3b-606c16a7799a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvNaFxbKpjdqF8Sk5KPk5p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 30624,
      "output_tokens": 72,
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
          "output_tokens": 72,
          "cache_read_input_tokens": 30624,
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

_source line 42 · 2026-05-20T03:50:47.246Z_

<details><summary>↩ Tool result · `toolu_01VCRhBtPz8cRXyesUyLq1pe`</summary>

```text
Web search results for query: "conformal prediction text classification NLP LLM extraction uncertainty quantification experiments 2024 2025"

Links: [{"title":"Conformal Prediction and Verification of Large Language Model Extractions in","url":"https://ojs.aaai.org/index.php/AAAI-SS/article/download/36929/39067/41006"},{"title":"Benchmarking LLMs via Uncertainty Quantification Fanghua Ye1,2 Mingming Yang1","url":"https://discovery.ucl.ac.uk/id/eprint/10217368/1/1565_Benchmarking_LLMs_via_Unc.pdf"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/html/2405.01976"},{"title":"Benchmarking LLMs via Uncertainty Quantification","url":"https://arxiv.org/html/2401.12794v3"},{"title":"COPU: Conformal Prediction for Uncertainty Quantification in Natural   Language Generation","url":"https://arxiv.org/pdf/2502.12601"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/pdf/2405.01976"},{"title":"Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction","url":"https://arxiv.org/pdf/2509.18658"}]

I found relevant research on conformal prediction for NLP and LLM tasks. Here are the key findings:

## Recent Research (2024-2025)

The rapid proliferation of LLMs and NLP applications creates a need for uncertainty quantification. Conformal prediction is emerging as a theoretically sound and practically useful framework with strong statistical guarantees, and its model-agnostic and distribution-free nature makes it particularly promising to address current NLP shortcomings from the absence of uncertainty quantification.

## Key Advantages of Conformal Prediction

Conformal prediction offers multiple advantages including ease of implementation, high efficiency, distribution-free and model-agnostic nature, and statistically rigorous estimation of uncertainty rather than heuristic approximation.

## Applications and Experiments

Recent work includes:

1. **Text Classification & Extraction**: Conformal predictors output prediction sets (for classification) or intervals (for regression) calibrated to contain the true value with a user-specified probability, with no assumption of normal distributions.

2. **Benchmarking LLMs**: Studies benchmark LLMs across five typical NLP tasks: question answering, reading comprehension, commonsense inference, dialogue response selection, and document summarization.

3. **Natural Language Generation**: Recent experiments with six LLMs on four NLG tasks show conformal prediction methods outperform baselines in calibrating error rates and empirical coverage rates across a wide range of error rates.

4. **LLM-as-a-Judge Applications**: Recent works apply conformal prediction to classification tasks such as multiple-choice question answering and response selection for factual consistency.

These studies demonstrate active research into applying conformal prediction for uncertainty quantification in various NLP and LLM tasks through 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd29ff87-9df7-4026-8f3b-606c16a7799a",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "988c7c8d-dc71-42a0-9392-dcb9aed9a822",
  "toolUseResult": {
    "query": "conformal prediction text classification NLP LLM extraction uncertainty quantification experiments 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TtK4xRHncn9JA6rmqqZv4n",
        "content": [
          {
            "title": "Conformal Prediction and Verification of Large Language Model Extractions in",
            "url": "https://ojs.aaai.org/index.php/AAAI-SS/article/download/36929/39067/41006"
          },
          {
            "title": "Benchmarking LLMs via Uncertainty Quantification Fanghua Ye1,2 Mingming Yang1",
            "url": "https://discovery.ucl.ac.uk/id/eprint/10217368/1/1565_Benchmarking_LLMs_via_Unc.pdf"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/html/2405.01976"
          },
          {
            "title": "Benchmarking LLMs via Uncertainty Quantification",
            "url": "https://arxiv.org/html/2401.12794v3"
          },
          {
            "title": "COPU: Conformal Prediction for Uncertainty Quantification in Natural   Language Generation",
            "url": "https://arxiv.org/pdf/2502.12601"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/pdf/2405.01976"
          },
          {
            "title": "Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction",
            "url": "https://arxiv.org/pdf/2509.18658"
          }
        ]
      },
      "I found relevant research on conformal prediction for NLP and LLM tasks. Here are the key findings:\n\n## Recent Research (2024-2025)\n\nThe rapid proliferation of LLMs and NLP applications creates a need for uncertainty quantification. Conformal prediction is emerging as a theoretically sound and practically useful framework with strong statistical guarantees, and its model-agnostic and distribution-free nature makes it particularly promising to address current NLP shortcomings from the absence of uncertainty quantification.\n\n## Key Advantages of Conformal Prediction\n\nConformal prediction offers multiple advantages including ease of implementation, high efficiency, distribution-free and model-agnostic nature, and statistically rigorous estimation of uncertainty rather than heuristic approximation.\n\n## Applications and Experiments\n\nRecent work includes:\n\n1. **Text Classification & Extraction**: Conformal predictors output prediction sets (for classification) or intervals (for regression) calibrated to contain the true value with a user-specified probability, with no assumption of normal distributions.\n\n2. **Benchmarking LLMs**: Studies benchmark LLMs across five typical NLP tasks: question answering, reading comprehension, commonsense inference, dialogue response selection, and document summarization.\n\n3. **Natural Language Generation**: Recent experiments with six LLMs on four NLG tasks show conformal prediction methods outperform baselines in calibrating error rates and empirical coverage rates across a wide range of error rates.\n\n4. **LLM-as-a-Judge Applications**: Recent works apply conformal prediction to classification tasks such as multiple-choice question answering and response selection for factual consistency.\n\nThese studies demonstrate active research into applying conformal prediction for uncertainty quantification in various NLP and LLM tasks through 2024-2025."
    ],
    "durationSeconds": 13.181615923000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cd29ff87-9df7-4026-8f3b-606c16a7799a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T03:50:50.052Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T51RYSjwvJJ5SeXxH8aZfz`</summary>

```json
{
  "query": "cross-conformal prediction Gasparin Ramdas ICML 2025 sample efficiency experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "988c7c8d-dc71-42a0-9392-dcb9aed9a822",
  "isSidechain": false,
  "requestId": "req_011CbD96B1sCxiMAwqHufGHD",
  "type": "assistant",
  "uuid": "020726cd-c28e-4a89-84a5-1a13f3153601",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTBPsX79prQnT8vFAAg6wL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 31303,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 31303,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 852
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

_source line 44 · 2026-05-20T03:50:55.772Z_

<details><summary>↩ Tool result · `toolu_01T51RYSjwvJJ5SeXxH8aZfz`</summary>

```text
Web search results for query: "cross-conformal prediction Gasparin Ramdas ICML 2025 sample efficiency experiments"

Links: [{"title":"Publications - Matteo Gasparin","url":"https://matteogaspa.github.io/publications/"},{"title":"ICML Poster Improving the Statistical Efficiency of Cross-Conformal Prediction","url":"https://icml.cc/virtual/2025/poster/44129"},{"title":"[2503.01495] Improving the statistical efficiency of cross-conformal prediction","url":"https://arxiv.org/abs/2503.01495"},{"title":"Track: Poster Session 2 East","url":"https://icml.cc/virtual/2025/session/50264"},{"title":"Improving the Statistical Efficiency of Cross-Conformal Prediction | OpenReview","url":"https://openreview.net/forum?id=mxNEWzqXFH"},{"title":"Cross-conformal predictors","url":"https://arxiv.org/pdf/1208.0806"},{"title":"Symmetric Aggregation of Conformity Scores for Efficient Uncertainty Sets","url":"https://www.arxiv.org/pdf/2512.06945"},{"title":"provably reliable conformal prediction sets","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"}]

Based on the web search results, I found relevant information about the Gasparin and Ramdas paper on cross-conformal prediction at ICML 2025:

## Paper Overview

Gasparin and Ramdas (2025) published "Improving the statistical efficiency of cross-conformal prediction" at ICML 2025 (the 42nd International Conference on Machine Learning).

## Key Contributions

The work builds on Vovk's (2015) cross-conformal prediction method, which is a modification of split conformal designed to improve the width of prediction sets. The paper proposes new variants of both methods that yield smaller prediction sets without compromising theoretical guarantees, based on recent results deriving more statistically efficient combination of p-values that leverage exchangeability and randomization.

## Experiments

Simulations confirm the theoretical findings and bring out some important tradeoffs.

The paper is available on arXiv (arxiv:2503.01495) and through the ICML proceedings, with an OpenReview page providing additional details about the work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "020726cd-c28e-4a89-84a5-1a13f3153601",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "36ba9096-cf9c-437b-aedc-d24d77cfc229",
  "toolUseResult": {
    "query": "cross-conformal prediction Gasparin Ramdas ICML 2025 sample efficiency experiments",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UekhSwM8Qqe271DSpvw1tC",
        "content": [
          {
            "title": "Publications - Matteo Gasparin",
            "url": "https://matteogaspa.github.io/publications/"
          },
          {
            "title": "ICML Poster Improving the Statistical Efficiency of Cross-Conformal Prediction",
            "url": "https://icml.cc/virtual/2025/poster/44129"
          },
          {
            "title": "[2503.01495] Improving the statistical efficiency of cross-conformal prediction",
            "url": "https://arxiv.org/abs/2503.01495"
          },
          {
            "title": "Track: Poster Session 2 East",
            "url": "https://icml.cc/virtual/2025/session/50264"
          },
          {
            "title": "Improving the Statistical Efficiency of Cross-Conformal Prediction | OpenReview",
            "url": "https://openreview.net/forum?id=mxNEWzqXFH"
          },
          {
            "title": "Cross-conformal predictors",
            "url": "https://arxiv.org/pdf/1208.0806"
          },
          {
            "title": "Symmetric Aggregation of Conformity Scores for Efficient Uncertainty Sets",
            "url": "https://www.arxiv.org/pdf/2512.06945"
          },
          {
            "title": "provably reliable conformal prediction sets",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the web search results, I found relevant information about the Gasparin and Ramdas paper on cross-conformal prediction at ICML 2025:\n\n## Paper Overview\n\nGasparin and Ramdas (2025) published \"Improving the statistical efficiency of cross-conformal prediction\" at ICML 2025 (the 42nd International Conference on Machine Learning).\n\n## Key Contributions\n\nThe work builds on Vovk's (2015) cross-conformal prediction method, which is a modification of split conformal designed to improve the width of prediction sets. The paper proposes new variants of both methods that yield smaller prediction sets without compromising theoretical guarantees, based on recent results deriving more statistically efficient combination of p-values that leverage exchangeability and randomization.\n\n## Experiments\n\nSimulations confirm the theoretical findings and bring out some important tradeoffs.\n\nThe paper is available on arXiv (arxiv:2503.01495) and through the ICML proceedings, with an OpenReview page providing additional details about the work."
    ],
    "durationSeconds": 5.717422005999979,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "020726cd-c28e-4a89-84a5-1a13f3153601",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-20T03:50:58.550Z_

Now let me search for a few more specific areas to round out my understanding of the experimental landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36ba9096-cf9c-437b-aedc-d24d77cfc229",
  "isSidechain": false,
  "requestId": "req_011CbD96oRNHR6GqwAP4fGiB",
  "type": "assistant",
  "uuid": "b1fbd220-60d8-43f6-8a27-c61c2c879ddb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFFiXpSienAHeKsxzgJNsn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 32155,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 32155,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 46 · 2026-05-20T03:50:59.129Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jh3kxETaALUMWhTb8G4RqK`</summary>

```json
{
  "query": "Veitch et al UAI 2020 text embeddings causal inference experiments semi-synthetic benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1fbd220-60d8-43f6-8a27-c61c2c879ddb",
  "isSidechain": false,
  "requestId": "req_011CbD96oRNHR6GqwAP4fGiB",
  "type": "assistant",
  "uuid": "3631901d-1407-40eb-914e-01f6451ea670",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFFiXpSienAHeKsxzgJNsn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 32155,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 32155,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 47 · 2026-05-20T03:51:04.283Z_

<details><summary>↩ Tool result · `toolu_01Jh3kxETaALUMWhTb8G4RqK`</summary>

```text
Web search results for query: "Veitch et al UAI 2020 text embeddings causal inference experiments semi-synthetic benchmark"

Links: [{"title":"Adapting Text Embeddings for Causal Inference","url":"https://proceedings.mlr.press/v124/veitch20a.html"},{"title":"Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings and Deep Learning","url":"https://arxiv.org/html/2601.01511"},{"title":"Adapting Text Embeddings for Causal Inference","url":"https://papertalk.org/papertalks/13750"},{"title":"Adapting Text Embeddings for Causal Inference | Dhanya Sridhar","url":"https://dsridhar91.github.io/publication/uai-20/"},{"title":"Adapting Text Embeddings for Causal Inference","url":"https://arxiv.org/pdf/1905.12741"},{"title":"Using Text Embeddings for Causal Inference","url":"https://www.arxiv.org/pdf/1905.12741v1"},{"title":"[PDF] Using Text Embeddings for Causal Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Using-Text-Embeddings-for-Causal-Inference-Veitch-Sridhar/298b72096b8a770b0cdb263dd53cf2463b8a1a1d"},{"title":"Dhanya Sridhar - Adapting Text Embeddings for Causal Inference","url":"https://www.dsridhar.com/publications/6361-adapting-text-embeddings-for-causal-inference"},{"title":"Adapting Text Embeddings for Causal Inference Victor Veitch∗ Dhanya Sridhar∗","url":"http://www.cs.columbia.edu/~blei/papers/VeitchSridharBlei2020.pdf"},{"title":"[1905.12741] Adapting Text Embeddings for Causal Inference","url":"https://arxiv.org/abs/1905.12741"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Adapting Text Embeddings for Causal Inference" by Veitch, Sridhar, and Blei, published in the Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence (UAI) in 2020.

The paper develops a method to estimate causal effects from observational text data by adjusting for confounding features, using causally sufficient embeddings—low-dimensional document representations that preserve sufficient information for causal identification.

The researchers studied causally sufficient embeddings with semi-synthetic datasets and found that they improve causal estimation over related embedding methods.

The paper illustrates the methods by answering two motivating questions: the effect of a theorem on paper acceptance and the effect of a gender label on post popularity.

Code and data are available at github.com/vveitch/causal-text-embeddings-tf2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3631901d-1407-40eb-914e-01f6451ea670",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "29b76f5a-aa74-4c49-91e8-0b1e56481214",
  "toolUseResult": {
    "query": "Veitch et al UAI 2020 text embeddings causal inference experiments semi-synthetic benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Cxbtu3eTtoBbDobgW4Tokv",
        "content": [
          {
            "title": "Adapting Text Embeddings for Causal Inference",
            "url": "https://proceedings.mlr.press/v124/veitch20a.html"
          },
          {
            "title": "Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings and Deep Learning",
            "url": "https://arxiv.org/html/2601.01511"
          },
          {
            "title": "Adapting Text Embeddings for Causal Inference",
            "url": "https://papertalk.org/papertalks/13750"
          },
          {
            "title": "Adapting Text Embeddings for Causal Inference | Dhanya Sridhar",
            "url": "https://dsridhar91.github.io/publication/uai-20/"
          },
          {
            "title": "Adapting Text Embeddings for Causal Inference",
            "url": "https://arxiv.org/pdf/1905.12741"
          },
          {
            "title": "Using Text Embeddings for Causal Inference",
            "url": "https://www.arxiv.org/pdf/1905.12741v1"
          },
          {
            "title": "[PDF] Using Text Embeddings for Causal Inference | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Using-Text-Embeddings-for-Causal-Inference-Veitch-Sridhar/298b72096b8a770b0cdb263dd53cf2463b8a1a1d"
          },
          {
            "title": "Dhanya Sridhar - Adapting Text Embeddings for Causal Inference",
            "url": "https://www.dsridhar.com/publications/6361-adapting-text-embeddings-for-causal-inference"
          },
          {
            "title": "Adapting Text Embeddings for Causal Inference Victor Veitch∗ Dhanya Sridhar∗",
            "url": "http://www.cs.columbia.edu/~blei/papers/VeitchSridharBlei2020.pdf"
          },
          {
            "title": "[1905.12741] Adapting Text Embeddings for Causal Inference",
            "url": "https://arxiv.org/abs/1905.12741"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper is titled \"Adapting Text Embeddings for Causal Inference\" by Veitch, Sridhar, and Blei, published in the Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence (UAI) in 2020.\n\nThe paper develops a method to estimate causal effects from observational text data by adjusting for confounding features, using causally sufficient embeddings—low-dimensional document representations that preserve sufficient information for causal identification.\n\nThe researchers studied causally sufficient embeddings with semi-synthetic datasets and found that they improve causal estimation over related embedding methods.\n\nThe paper illustrates the methods by answering two motivating questions: the effect of a theorem on paper acceptance and the effect of a gender label on post popularity.\n\nCode and data are available at github.com/vveitch/causal-text-embeddings-tf2."
    ],
    "durationSeconds": 5.15029293700002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3631901d-1407-40eb-914e-01f6451ea670",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
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
  "lastPrompt": "# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Description We propose ConformalPPITextCausal, a framework providing finite-sample coverage g…",
  "leafUuid": "29b76f5a-aa74-4c49-91e8-0b1e56481214",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Tool call

_source line 50 · 2026-05-20T03:51:06.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qwubrcz98NSt8uXvwYMNSv`</summary>

```json
{
  "query": "\"wTCP-DR\" KDD 2024 conformal counterfactual hidden confounding experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29b76f5a-aa74-4c49-91e8-0b1e56481214",
  "isSidechain": false,
  "requestId": "req_011CbD97RxonzH1XSzXLdvXW",
  "type": "assistant",
  "uuid": "e2fc0589-6a7a-4683-840e-c3fcedf1a4b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1uK2Gs9zd9mGHBFDCizgx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 32854,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 32854,
          "cache_creation_input_tokens": 854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 854
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

_source line 51 · 2026-05-20T03:51:13.887Z_

<details><summary>↩ Tool result · `toolu_01Qwubrcz98NSt8uXvwYMNSv`</summary>

```text
Web search results for query: ""wTCP-DR" KDD 2024 conformal counterfactual hidden confounding experiments"

Links: [{"title":"[PDF] Conformal Prediction for Causal Effects of Continuous Treatments | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Conformal-Prediction-for-Causal-Effects-of-Schroder-Frauen/fd698208bd8084945ecd857cc88c99c3c70ad86c"},{"title":"(PDF) Conformal Counterfactual Inference under Hidden Confounding","url":"https://www.researchgate.net/publication/380757276_Conformal_Counterfactual_Inference_under_Hidden_Confounding"},{"title":"Conformal Counterfactual Inference under Hidden Confounding Zonghao Chen∗†","url":"https://dl.acm.org/doi/pdf/10.1145/3637528.3671976"},{"title":"Conformal Counterfactual Inference under Hidden Confounding | Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining","url":"https://dl.acm.org/doi/10.1145/3637528.3671976"},{"title":"[Quick Review] Conformal Counterfactual Inference under Hidden Confounding","url":"https://liner.com/review/conformal-counterfactual-inference-under-hidden-confounding"},{"title":"Conformal Counterfactual Inference under Hidden Confounding","url":"https://arxiv.org/html/2405.12387v1"},{"title":"[2405.12387] Conformal Counterfactual Inference under Hidden Confounding","url":"https://arxiv.org/abs/2405.12387"},{"title":"Conformal Counterfactual Inference under Hidden Confounding","url":"https://arxiv.org/pdf/2405.12387"},{"title":"KDD 2024 Workshop - Causal Inference and Machine Learning in Practice | KDD 2024 Workshop - Causal Inference and Machine Learning in Practice","url":"https://causal-machine-learning.github.io/kdd2024-workshop/"},{"title":"dblp: KDD 2024","url":"https://dblp.org/db/conf/kdd/kdd2024.html"}]

Based on the web search results, I found relevant information about wTCP-DR and the KDD 2024 paper on conformal counterfactual inference.

## Overview

The paper "Conformal Counterfactual Inference under Hidden Confounding" was authored by Zonghao Chen, Ruocheng Guo, Jean-Francois Ton, and Yang Liu, and presented at KDD 2024.

## The wTCP-DR Method

wTCP-DR is a novel approach based on transductive weighted conformal prediction that provides confidence intervals for counterfactual outcomes with marginal coverage guarantees, even under hidden confounding. The method provides confidence intervals for counterfactual outcomes with marginal coverage guarantees under hidden confounding, with less restrictive assumptions requiring access to a fraction of interventional data from randomized controlled trials to account for the covariate shift from observational distribution to interventional distribution.

## Key Features and Variants

The researchers also propose wSCP-DR, a two-stage variant of wTCP-DR based on split conformal prediction with same marginal coverage guarantees but at a significantly lower computational cost. The methods can be applied to potential outcomes to effectively construct confidence intervals for individual treatment effects.

## Experiments

The method was demonstrated across synthetic and real-world data, including recommendation systems, to verify the methods in terms of both coverage and efficiency. Theoretical results demonstrate conditions where wTCP-DR is strictly advantageous over naive methods, particularly regarding confidence interval width when observational data are abundant.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2fc0589-6a7a-4683-840e-c3fcedf1a4b0",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "e3241eae-3bff-4503-be9e-d3032f23b5f6",
  "toolUseResult": {
    "query": "\"wTCP-DR\" KDD 2024 conformal counterfactual hidden confounding experiments",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R89xtmCjdGA8zicRyZXAJU",
        "content": [
          {
            "title": "[PDF] Conformal Prediction for Causal Effects of Continuous Treatments | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Conformal-Prediction-for-Causal-Effects-of-Schroder-Frauen/fd698208bd8084945ecd857cc88c99c3c70ad86c"
          },
          {
            "title": "(PDF) Conformal Counterfactual Inference under Hidden Confounding",
            "url": "https://www.researchgate.net/publication/380757276_Conformal_Counterfactual_Inference_under_Hidden_Confounding"
          },
          {
            "title": "Conformal Counterfactual Inference under Hidden Confounding Zonghao Chen∗†",
            "url": "https://dl.acm.org/doi/pdf/10.1145/3637528.3671976"
          },
          {
            "title": "Conformal Counterfactual Inference under Hidden Confounding | Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining",
            "url": "https://dl.acm.org/doi/10.1145/3637528.3671976"
          },
          {
            "title": "[Quick Review] Conformal Counterfactual Inference under Hidden Confounding",
            "url": "https://liner.com/review/conformal-counterfactual-inference-under-hidden-confounding"
          },
          {
            "title": "Conformal Counterfactual Inference under Hidden Confounding",
            "url": "https://arxiv.org/html/2405.12387v1"
          },
          {
            "title": "[2405.12387] Conformal Counterfactual Inference under Hidden Confounding",
            "url": "https://arxiv.org/abs/2405.12387"
          },
          {
            "title": "Conformal Counterfactual Inference under Hidden Confounding",
            "url": "https://arxiv.org/pdf/2405.12387"
          },
          {
            "title": "KDD 2024 Workshop - Causal Inference and Machine Learning in Practice | KDD 2024 Workshop - Causal Inference and Machine Learning in Practice",
            "url": "https://causal-machine-learning.github.io/kdd2024-workshop/"
          },
          {
            "title": "dblp: KDD 2024",
            "url": "https://dblp.org/db/conf/kdd/kdd2024.html"
          }
        ]
      },
      "Based on the web search results, I found relevant information about wTCP-DR and the KDD 2024 paper on conformal counterfactual inference.\n\n## Overview\n\nThe paper \"Conformal Counterfactual Inference under Hidden Confounding\" was authored by Zonghao Chen, Ruocheng Guo, Jean-Francois Ton, and Yang Liu, and presented at KDD 2024.\n\n## The wTCP-DR Method\n\nwTCP-DR is a novel approach based on transductive weighted conformal prediction that provides confidence intervals for counterfactual outcomes with marginal coverage guarantees, even under hidden confounding. The method provides confidence intervals for counterfactual outcomes with marginal coverage guarantees under hidden confounding, with less restrictive assumptions requiring access to a fraction of interventional data from randomized controlled trials to account for the covariate shift from observational distribution to interventional distribution.\n\n## Key Features and Variants\n\nThe researchers also propose wSCP-DR, a two-stage variant of wTCP-DR based on split conformal prediction with same marginal coverage guarantees but at a significantly lower computational cost. The methods can be applied to potential outcomes to effectively construct confidence intervals for individual treatment effects.\n\n## Experiments\n\nThe method was demonstrated across synthetic and real-world data, including recommendation systems, to verify the methods in terms of both coverage and efficiency. Theoretical results demonstrate conditions where wTCP-DR is strictly advantageous over naive methods, particularly regarding confidence interval width when observational data are abundant."
    ],
    "durationSeconds": 6.920756961000007,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e2fc0589-6a7a-4683-840e-c3fcedf1a4b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T03:51:16.481Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016iRwP4AVPaBdMMvqnQJMNK`</summary>

```json
{
  "query": "causal inference measurement error confounders misclassification sensitivity analysis bootstrap coverage 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3241eae-3bff-4503-be9e-d3032f23b5f6",
  "isSidechain": false,
  "requestId": "req_011CbD988sSPnJtxBnFQkyr4",
  "type": "assistant",
  "uuid": "6148fd23-37fe-4303-b6fd-8e92cfd5c0d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HGYE1J4qnowNPgpaMxp1on",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 33708,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 33708,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 53 · 2026-05-20T03:51:23.706Z_

<details><summary>↩ Tool result · `toolu_016iRwP4AVPaBdMMvqnQJMNK`</summary>

```text
Web search results for query: "causal inference measurement error confounders misclassification sensitivity analysis bootstrap coverage 2024 2025"

Links: [{"title":"Sensitivity analysis for causal inference under unmeasured confounding and measurement error problems - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/24246288/"},{"title":"Estimation of Causal Effect Measures in the Presence of Measurement Error in Confounders - Statistics in Biosciences","url":"https://link.springer.com/article/10.1007/s12561-018-9213-8"},{"title":"Sensitivity Analysis for Causal Inference under Unmeasured Confounding and Measurement Error Problems | Request PDF","url":"https://www.researchgate.net/publication/258640909_Sensitivity_Analysis_for_Causal_Inference_under_Unmeasured_Confounding_and_Measurement_Error_Problems"},{"title":"$L^{\\infty}$- and $L^2$-sensitivity analysis for causal inference with   unmeasured confounding","url":"https://arxiv.org/pdf/2211.04697"},{"title":"Sensitivity analysis for bias due to a misclassfied confounding variable   in marginal structural models","url":"https://arxiv.org/pdf/1912.05800"},{"title":"Measurement Error-Robust Causal Inference via Constructed Instrumental   Variables","url":"https://arxiv.org/pdf/2406.00940"},{"title":"Optimization-based Sensitivity Analysis for Unmeasured Confounding using Partial Correlations","url":"https://arxiv.org/pdf/2301.00040"}]

Based on the search results, here's what I found on causal inference with measurement error, confounders, misclassification, sensitivity analysis, and bootstrap methods:

## Key Research Areas

**Measurement Error in Confounders:**
Estimation of causal effect measures is often challenged by error-contaminated confounders, with researchers proposing methods that consistently estimate causal odds ratios, risk ratios, and risk differences for settings with error-prone confounders. Bootstrap-based procedures have been developed to construct estimators with improved asymptotic efficiency.

**Measurement Error Bias:**
When a true confounder is measured with error in ordinary least squares regression for causal inference, the estimator of the treatment effect will be biased toward the crude estimate.

**Sensitivity Analysis Approaches:**
Sensitivity analysis for the unconfoundedness assumption is crucial for observational studies, with the marginal sensitivity model becoming increasingly popular due to its interpretability and mathematical properties. Multiplier bootstrap can be applied to construct simultaneous confidence bands for the average treatment effect.

**Misclassification and Bootstrap Coverage:**
In marginal structural models with inverse probability weighting, confidence intervals for treatment effects are generally wider with higher coverage of the true treatment effect, ranging from overcoverage with no classification error to smaller undercoverage when there is classification error.

The search results primarily contain foundational and recent methodological work (through 2024) addressing these interconnected topics in causal inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6148fd23-37fe-4303-b6fd-8e92cfd5c0d5",
  "isSidechain": false,
  "promptId": "9192db98-e90c-4c39-89f5-4f11b82e45b2",
  "type": "user",
  "uuid": "797a7292-21dc-4a67-8392-e76e8560f51a",
  "toolUseResult": {
    "query": "causal inference measurement error confounders misclassification sensitivity analysis bootstrap coverage 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KpyPDnyTdXVfCcxupyLZqW",
        "content": [
          {
            "title": "Sensitivity analysis for causal inference under unmeasured confounding and measurement error problems - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/24246288/"
          },
          {
            "title": "Estimation of Causal Effect Measures in the Presence of Measurement Error in Confounders - Statistics in Biosciences",
            "url": "https://link.springer.com/article/10.1007/s12561-018-9213-8"
          },
          {
            "title": "Sensitivity Analysis for Causal Inference under Unmeasured Confounding and Measurement Error Problems | Request PDF",
            "url": "https://www.researchgate.net/publication/258640909_Sensitivity_Analysis_for_Causal_Inference_under_Unmeasured_Confounding_and_Measurement_Error_Problems"
          },
          {
            "title": "$L^{\\infty}$- and $L^2$-sensitivity analysis for causal inference with   unmeasured confounding",
            "url": "https://arxiv.org/pdf/2211.04697"
          },
          {
            "title": "Sensitivity analysis for bias due to a misclassfied confounding variable   in marginal structural models",
            "url": "https://arxiv.org/pdf/1912.05800"
          },
          {
            "title": "Measurement Error-Robust Causal Inference via Constructed Instrumental   Variables",
            "url": "https://arxiv.org/pdf/2406.00940"
          },
          {
            "title": "Optimization-based Sensitivity Analysis for Unmeasured Confounding using Partial Correlations",
            "url": "https://arxiv.org/pdf/2301.00040"
          }
        ]
      },
      "Based on the search results, here's what I found on causal inference with measurement error, confounders, misclassification, sensitivity analysis, and bootstrap methods:\n\n## Key Research Areas\n\n**Measurement Error in Confounders:**\nEstimation of causal effect measures is often challenged by error-contaminated confounders, with researchers proposing methods that consistently estimate causal odds ratios, risk ratios, and risk differences for settings with error-prone confounders. Bootstrap-based procedures have been developed to construct estimators with improved asymptotic efficiency.\n\n**Measurement Error Bias:**\nWhen a true confounder is measured with error in ordinary least squares regression for causal inference, the estimator of the treatment effect will be biased toward the crude estimate.\n\n**Sensitivity Analysis Approaches:**\nSensitivity analysis for the unconfoundedness assumption is crucial for observational studies, with the marginal sensitivity model becoming increasingly popular due to its interpretability and mathematical properties. Multiplier bootstrap can be applied to construct simultaneous confidence bands for the average treatment effect.\n\n**Misclassification and Bootstrap Coverage:**\nIn marginal structural models with inverse probability weighting, confidence intervals for treatment effects are generally wider with higher coverage of the true treatment effect, ranging from overcoverage with no classification error to smaller undercoverage when there is classification error.\n\nThe search results primarily contain foundational and recent methodological work (through 2024) addressing these interconnected topics in causal inference."
    ],
    "durationSeconds": 7.219270996000007,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6148fd23-37fe-4303-b6fd-8e92cfd5c0d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54 · 2026-05-20T03:51:23.709Z_

```json
{
  "parentUuid": "797a7292-21dc-4a67-8392-e76e8560f51a",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e3317bcf-df48-415e-8db7-bf4ab54739f3",
  "timestamp": "2026-05-20T03:51:23.709Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 55 · 2026-05-20T03:54:08.910Z_

Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **Alaa et al. "Conformal Meta-learners for Predictive Inference of Individual Treatment Effects" (NeurIPS 2023)**: 使用 IHDP、NLSM、synthetic 三类数据集；baseline 包括 X-learner、DR-learner、IPW-learner 的 conformal 版本；指标为 marginal coverage、conditional coverage、interval width、RMSE；ablation 包括 meta-learner 选择和 base model 选择。这是 conformal ITE 领域的标准实验设计范式。
- **Chen et al. "Conformal Counterfactual Inference under Hidden Confounding" (KDD 2024, wTCP-DR)**: 使用 synthetic + 推荐系统真实数据；baseline 包括 naive conformal、split conformal、weighted CP 变体；关键指标为 coverage + interval width trade-off；ablation 包括 hidden confounding 程度、RCT 数据量。
- **DoubleLingo (NAACL 2024)**: 使用 semi-synthetic 数据；baseline 包括 Oracle、Unadjusted、TF-IDF、BERT+Adapter、Embedding+FFN；指标为 ATE relative absolute error；证明了 DML 框架下 LLM 的有效性。
- **Ma et al. "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding" (NeurIPS 2025)**: 使用真实医疗数据集；baseline 包括 standard doubly robust learner without confounding adjustment；关键创新是 inference-time confounding adjustment framework。
- **Csillag et al. "Extending PPI through Conformal Prediction" (arXiv 2510.16166, 2025)**: 实例化了 mean estimation、Z-estimation、M-estimation；实验展示了 conformal set-predictor 如何比 point imputation PPI 获得更强的有效性保证；包括 privacy、robustness 等额外保证。
- **Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025)**: 使用 synthetic + 真实数据验证 PPI 在因果推断场景下的有效性；关键是 conditional calibration 和 cross-distribution validity。
- **Zhang et al. "Modular CP for Sequential Models" (arXiv 2510.04406, 2025)**: 实验在 synthetic distribution shift、supply chain、stock market 数据上；通过 stage-wise attribution 展示了 modular decomposition 的优势；baseline 为 standard (non-modular) conformal methods。
- **Gasparin & Ramdas "Improving Cross-Conformal Prediction" (ICML 2025)**: 展示了 cross-conformal vs. split conformal 的 efficiency tradeoff；实验验证了更小的 prediction sets 在不损失 coverage 的前提下的可行性。
- **Veitch et al. "Adapting Text Embeddings for Causal Inference" (UAI 2020)**: 使用 semi-synthetic 数据（paper acceptance、Reddit post popularity）；这是文本因果推断领域的经典 benchmark 设计范式。

- **调研总结**: 该领域当前实验设计标准要求：(1) 在 synthetic 数据（可控 ground truth）+ semi-synthetic 数据（真实文本、合成 treatment assignment）两层验证；(2) 核心指标为 empirical coverage vs. nominal level + interval width（越窄越好）的 trade-off；(3) baseline 必须包括 oracle (perfectly observed confounders)、naive plug-in (LLM point prediction as ground truth)、以及 bootstrap/asymptotic CI 作为对照；(4) ablation 需覆盖 LLM 质量、calibration set size、propensity overlap 等关键参数；(5) 审稿人普遍期望看到 coverage-width Pareto frontier 图和 calibration 诊断图。

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: Proposal 的实验部分提到了与 "oracle (perfectly observed confounders)" 和 "bootstrap baselines" 的比较，但 **缺乏对以下关键 baseline 的明确列举和对比**：(1) **Naive plug-in baseline**：直接将 LLM 的 point prediction 当作 ground truth 进行标准因果推断（不进行任何不确定性校正），这是证明本框架存在价值的最重要对照——如果 naive plug-in 的 coverage 没有显著 undercover，整个框架的 motivation 就会被质疑；(2) **DoubleLingo (NAACL 2024) 和 Ma et al. (NeurIPS 2025)** 作为最直接的现有方法，proposal 中反复提到它们"只提供 asymptotic guarantees"，但实验中 **没有明确计划将它们的 asymptotic CI 作为 baseline 进行 coverage 对比**；(3) **Lei & Candès (2021) 和 Alaa et al. (NeurIPS 2023)** 的标准 conformal ITE 方法（假设 confounders 无误）——作为"oracle conformal"baseline 来量化 extraction noise 带来的额外 cost；(4) **wTCP-DR (KDD 2024)** 作为另一个 conformal + causal 的近期方法。
- 严重度: 可补救
- 补救方案: 明确列出以下 baseline 层级并纳入实验计划：
  - **Layer 0 (Oracle)**: 使用 ground-truth confounders 的标准 DR estimator + conformal ITE intervals (Alaa et al. 2023 风格) → 提供 coverage 和 width 的理论上限参照
  - **Layer 1 (Naive plug-in)**: LLM point prediction 作为 ground truth → 标准 DR estimator + bootstrap CI 或 conformal ITE → 预期 undercover，这是动机验证的核心
  - **Layer 2 (Asymptotic methods)**: DoubleLingo / Ma et al. 的 asymptotic CI → 预期在 heterogeneous extraction noise 下 undercover
  - **Layer 3 (Proposed)**: ConformalPPITextCausal Track A / Track B
  - 在所有 benchmark 上报告每个 layer 的 coverage rate 和 interval width，并画出 coverage-width trade-off 图
- 调研依据: Alaa et al. (NeurIPS 2023) 使用了 X-learner、DR-learner、IPW-learner 的 conformal 变体作为 baseline；wTCP-DR (KDD 2024) 与 naive conformal 和 split conformal 对比；DoubleLingo 和 Ma et al. 是 proposal 自己指出的最直接竞争方法但未纳入 baseline

【缺陷 2】
- 类别: 实验设计不足
- 问题: Proposal 提到使用 semi-synthetic MIMIC-IV 数据集，但 **没有给出 semi-synthetic 数据生成过程的具体设计**。Semi-synthetic 因果推断 benchmark 的核心是如何从真实文本生成 treatment assignment 和 potential outcomes，使得 ground-truth treatment effects 已知。目前 proposal 仅说"treatment escalation effect on ICU outcomes, disease severity as text confounder"，但缺少：(1) treatment assignment mechanism 的具体参数化（如何通过 disease severity 影响 treatment probability？propensity score 模型是什么？）；(2) potential outcome 生成函数（Y(0), Y(1) 如何依赖于 confounders？CATE 的 heterogeneity 设计？）；(3) LLM extraction noise 的注入方式（是使用真实 LLM 的 extraction 结果，还是通过 synthetic noise injection 控制错误率？）。这直接影响实验结论的可信度和可复现性。另外，proposal 提到 MIMIC-IV 但调研发现现有文本因果推断文献主要使用 MIMIC-III。需确认 MIMIC-IV 的 clinical notes 是否已经公开可用且具备必要的文本字段。
- 严重度: 可补救
- 补救方案: 
  - 参考 Veitch et al. (UAI 2020) 和 DoubleLingo (NAACL 2024) 的 semi-synthetic 数据生成范式，明确给出：(a) 从 MIMIC 临床笔记中提取真实 text features 的流程；(b) treatment assignment model p(A=1|C_true) = σ(β₀ + β₁·severity + ...)；(c) potential outcome model Y(a) = f(C_true, a) + ε，明确 CATE heterogeneity 的设计；(d) LLM extraction noise 的两种实验模式——真实 LLM extraction（使用 GPT-4 / Claude / Llama 对同一批文本提取）和 controlled noise injection（系统性改变 misclassification rate 以扫描 LLM 质量参数空间）
  - 确认使用 MIMIC-IV（v3.0+）的 discharge summaries / radiology notes 是否可行，或降级至 MIMIC-III 的 NOTEEVENTS 表（更成熟的 benchmark）
  - 对社交媒体数据集同样需要给出类似的 semi-synthetic 生成细节
- 调研依据: Veitch et al. (UAI 2020) 是文本因果推断 semi-synthetic benchmark 的标准范式；现有文献主要使用 MIMIC-III 而非 MIMIC-IV

【缺陷 3】
- 类别: ablation 不完整
- 问题: Proposal 提到了几项 ablation（LLM quality sensitivity via |C|/K sweep、propensity overlap analysis、embedding dimension、calibration set size、cross-conformal vs. split comparison），覆盖面合理但 **缺少以下关键 ablation**：
  - (1) **Stage 1 vs. Stage 2 的 uncertainty attribution**: Zhang et al. (2025) 的核心卖点是 modular residual decomposition 能 attribute uncertainty to specific stages。Proposal 应该展示：在最终 interval width 中，多少来自 Stage 1 (LLM extraction uncertainty)、多少来自 Stage 2 (outcome estimation uncertainty)？这是验证 modular approach 价值的关键证据。
  - (2) **Track A vs. Track B 的 head-to-head comparison**: Proposal 同时提出两个 track 但 **没有明确计划在相同设置下直接对比它们**。Track A (ITE) 和 Track B (ATE) 的 target 不同，但至少在 ATE 这个共同可比指标上，应该展示 Track A aggregated ITE intervals vs. Track B direct ATE intervals 的 coverage 和 width 差异。
  - (3) **Nuisance estimator 选择的 sensitivity**: Proposal 的 continuous embedding track 限制在 smooth nuisance estimators，但没有计划展示在 categorical track 上使用不同 nuisance estimators (tree-based vs. neural) 时的 performance 差异。
  - (4) **Labeled data size (n_labeled) 的 sensitivity curve**: 对于 Track B (PPI track)，labeled data size 是核心瓶颈，应该画出 n_labeled 从极少（50）到充足（500+）时的 coverage 和 width 变化曲线。
- 严重度: 可补救
- 补救方案:
  - 添加 "uncertainty source decomposition" 实验：对每个测试样本，分别报告 Stage 1 contribution (Δφ from conformal set enumeration) 和 Stage 2 contribution (conformal quantile of pseudo-outcome residuals)，画出分布图
  - 添加 Track A vs. Track B 在 ATE estimation 上的直接对比表
  - 添加 nuisance estimator sensitivity 实验：categorical track 下比较 GBM、Random Forest、TARNet、DragonNet
  - 添加 n_labeled sensitivity curve for Track B，x 轴为 labeled sample size，y 轴为 coverage 和 width
- 调研依据: Zhang et al. (2510.04406) 在实验中展示了 stage-wise uncertainty attribution，这是 modular CP 的核心价值；Alaa et al. (NeurIPS 2023) 比较了不同 meta-learner 的 sensitivity

【缺陷 4】
- 类别: 评估方案缺陷
- 问题: Proposal 的评估指标提到 "empirical coverage at 90%/95% nominal levels, interval width relative to oracle and bootstrap baselines, widening ratio W"，但 **缺少以下重要评估维度**：
  - (1) **Conditional coverage 分析**: Marginal coverage 可以通过 trivial 方式满足（e.g., 无限宽的 intervals），领域标准（如 Alaa et al. 2023、Lei & Candès 2021）要求展示 coverage 在不同 subgroup 上的条件表现。特别是在本 proposal 中，coverage 应按 LLM extraction difficulty（easy vs. hard cases）、propensity score region（high overlap vs. low overlap）、confounder category 分层报告。如果只报告 marginal coverage = 95% 但某些 subgroup 严重 undercover，审稿人几乎必然会指出这一点。
  - (2) **Calibration diagnostic plots**: 领域标准要求画出 nominal coverage level (x 轴) vs. empirical coverage (y 轴) 的校准图，覆盖 80%-99% 的 nominal levels，而不仅仅报告 90% 和 95% 两个点。
  - (3) **Computational cost comparison**: 提到了 worst-case enumeration 的 O(|C|) complexity，但没有计划报告 wall-clock time comparison 与 baseline 方法（bootstrap resampling 等）的对比。
- 严重度: 可补救
- 补救方案:
  - 添加 conditional coverage 分析：按 LLM conformal set size (|C|=1 vs. 2 vs. 3+)、propensity score quintile、treatment group 分层报告 coverage
  - 添加 calibration plot：sweep nominal level α from 0.01 to 0.20，画出 empirical coverage curve
  - 添加 computational cost table：报告每个方法的 per-sample inference time 和 total calibration time
- 调研依据: Alaa et al. (NeurIPS 2023) 报告了 conditional coverage 和 calibration 分析；Jonkers et al. (2024, Conformal Convolution) 展示了 full calibration curves；wTCP-DR (KDD 2024) 包含了 computational cost 对比

【缺陷 5】
- 类别: 可行性问题
- 问题: **Continuous embedding track (Matryoshka + ellipsoidal sets) 的可行性存在显著风险**。Proposal 提到使用 128-256 维 Matryoshka embeddings 构建 ellipsoidal conformal sets，然后通过 convex relaxation (Lipschitz + Taylor expansion) bound worst-case pseudo-outcomes。但存在以下实际问题：
  - (1) 即使降至 128 维，ellipsoidal conformal sets 在高维空间中的 volume 可能非常大，导致 worst-case bounds 极度 conservative（远超 categorical track 的 60-100% widening），使得该 track 在实际中 vacuously wide。Proposal 的 pilot conservatism analysis 只覆盖了 categorical track，**没有对 continuous track 给出类似的 back-of-envelope viability analysis**。
  - (2) Lipschitz constant 的估计在 128+ 维空间中本身就是 computationally expensive 且 typically pessimistic 的，local Lipschitz estimation 需要额外的 computation budget。
  - (3) 限制 nuisance estimators 为 smooth models 是一个实际约束——在因果推断文献中，GBM/Random Forest 仍然是常用且表现优秀的 nuisance estimator（特别是在 DML 框架下），这个限制可能导致 continuous track 在实际中不被采用。
- 严重度: 可补救（但需要调整期望和实验设计）
- 补救方案:
  - **在提交前先做一个 feasibility pilot**：在 synthetic 数据上，以 128 维 embedding 构建 ellipsoidal set，估算 worst-case pseudo-outcome interval 的宽度。如果在合理的 LLM 质量下 interval width 已经 >5× oracle，应考虑将 continuous track 降级为"探索性实验"或"future work"，将 paper 的主要 claim 集中在 categorical track
  - 补充 continuous track 的 pilot conservatism analysis，至少给出量级估计
  - 如果 continuous track 可行性不高，可以替代为：将 embeddings 通过 learned discretization（如 VQ-VAE 风格的 codebook lookup）转化为 categorical variables，从而复用 categorical track 的 enumeration 框架
  - 明确说明 smooth nuisance estimator 的限制及其实际影响，报告 smooth (TARNet/DragonNet) vs. tree-based (GBM) 在 categorical track 上的性能差距，让读者了解这个 restriction 的 cost
- 调研依据: Xu et al. (ICML 2024) 和 Lützow et al. (2026) 提供了 ellipsoidal set 的理论工具，但其实验主要在 moderate 维度（time series）而非 128+ 维 text embeddings；基于领域实验规范判断，高维 ellipsoidal sets 的 conservatism 在因果推断场景下可能不可接受

【缺陷 6】
- 类别: compute 公平性问题
- 问题: Proposal 计划在 coverage 和 width 上与 bootstrap baselines 进行对比，声称 "bootstrap alternatives undercover"。但 **bootstrap 的 coverage 性能高度依赖于 bootstrap 的变体和实现**。Standard nonparametric bootstrap CI 在有限样本下确实可能 undercover，但 bias-corrected bootstrap (BCa)、double bootstrap、或 Bayesian bootstrap 在适当设置下可以获得更好的 coverage。如果 proposal 只与最基础的 percentile bootstrap 对比，审稿人可能会质疑 comparison 的公平性。此外，asymptotic CI（如 DoubleLingo 的 DML-based CI）的 coverage breakdown 应该在理论上可以预期的条件下（如 sample size、LLM noise level）进行量化。
- 严重度: 可补救
- 补救方案:
  - Bootstrap baseline 应至少包括：(a) percentile bootstrap、(b) BCa bootstrap、(c) wild bootstrap（适用于异方差场景，与 LLM extraction noise 的 heterogeneous 特性匹配）
  - 对于 asymptotic CI baseline，需要在不同的 sample size (n = 200, 500, 1000, 2000) 和 LLM noise level 下展示 coverage breakdown curve，验证 asymptotic guarantees 何时开始 hold
  - 明确声明："我们的 finite-sample guarantee 的优势在 moderate sample sizes (n < 1000) 和 heterogeneous LLM noise 条件下最为显著；在大样本和均匀 noise 下，asymptotic methods 可能表现相当"——这种 honest framing 反而增加可信度
- 调研依据: 基于领域实验规范判断——DML 文献中 bootstrap CI 的 standard practice 包括多种变体；审稿人通常期望 against strongest possible baseline

【缺陷 7】
- 类别: 实验设计不足
- 问题: Proposal 提到三个 benchmarks（MIMIC-IV、social media、fully synthetic），但 **fully synthetic benchmark 的设计没有给出任何细节**。Fully synthetic data 是 conformal causal inference 论文的 **核心验证层**——因为只有在完全已知 DGP 的情况下，才能精确验证 coverage guarantee 是否 hold、interval width 是否 tight。审稿人通常期望看到：(1) 至少 2-3 种不同的 DGP 设计（e.g., 不同程度的 treatment effect heterogeneity、不同 propensity score overlap 条件、不同 confounder-outcome relationship 复杂度）；(2) 可控的 LLM extraction noise 注入（misclassification rate sweep）；(3) 大量 repetitions (≥100 seeds) 以获得 coverage 的准确估计。Proposal 仅提到 "fully synthetic data with known ground-truth for calibration validation"，过于模糊。
- 严重度: 可补救
- 补救方案: 设计至少 3 个 synthetic DGP scenarios：
  - **Scenario 1 (Benign)**: 5 categorical confounders, moderate propensity overlap (e(c) ∈ [0.25, 0.75]), smooth CATE, low extraction noise (5% misclassification)
  - **Scenario 2 (Challenging propensity)**: same confounders, poor overlap (e(c) ∈ [0.1, 0.9]), LLM tends to confuse categories with extreme propensities
  - **Scenario 3 (Heterogeneous noise)**: extraction error rate varies by subgroup (easy cases 2%, hard cases 30%), testing whether conformal sets properly adapt
  - 每个 scenario 运行 200+ seeds，报告 coverage 的 mean ± std
  - 在 Scenario 1-3 上扫描 misclassification rate 从 0% 到 50%，画出 "noise level vs. coverage" 和 "noise level vs. width" 曲线
- 调研依据: Alaa et al. (NeurIPS 2023) 使用了 multiple synthetic DGPs；wTCP-DR (KDD 2024) 设计了 varying hidden confounding strength 的 synthetic experiments

【缺陷 8】
- 类别: 可行性问题
- 问题: Proposal 的 resource estimate 中 timeline 为 10 weeks（targeting AAAI 2027 deadline），但目标投稿会议中同时列出了 AAAI 2027 (July 28) 和 ARR August 2026 cycle (August 3)——两个 deadline 仅相隔约一周。更关键的是，**实验涉及的工程量可能被低估**：(1) 理论部分（modular residual decomposition under weighted exchangeability, conformal PPI ATE estimator）分配了 2 周，但证明 weighted exchangeability conditions 下的 modular decomposition 可能需要大量的 technical effort，特别是需要处理 propensity score weighting 对 exchangeability 的破坏；(2) MIMIC-IV 数据需要 PhysioNet credentialed access，申请流程可能需要 2-4 周；(3) expert annotation for MIMIC-IV confounder labels (listed as "~5 hours domain expert time") 可能严重低估——医学领域的 annotation guidelines 制定、pilot annotation、inter-annotator agreement 计算、disagreement resolution 通常需要 20-40 hours of domain expert time。
- 严重度: 可补救
- 补救方案:
  - 如果尚未获得 MIMIC-IV access，**立即开始申请**（PhysioNet credentialing 可能需要 2-4 weeks），同时用 MIMIC-III（access 流程更快且更成熟）作为 backup
  - 将 expert annotation 时间估计调整为 20-40 hours，或考虑使用 MIMIC 已有的结构化变量（如 ICD codes、lab values）作为 ground-truth confounders，而非要求新的人工标注
  - 如果时间紧张，考虑在初始提交时将 continuous embedding track 标记为 "preliminary results"，集中精力在 categorical track 和 PPI track 的完整实验上
  - 调整 timeline：Weeks 1-3 理论，Weeks 4-6 实现 categorical + PPI tracks，Weeks 7-8 核心实验，Week 9 ablation + continuous track pilot，Week 10 writing
- 调研依据: 基于领域实验规范判断——MIMIC access 和 clinical annotation 的时间常被低估；Proximal Causal Inference with Text Data (arXiv 2401.06687) 使用 MIMIC-III 而非 MIMIC-IV

---

**总结**: 这份 proposal 的实验框架有合理的骨架（三层 benchmark、覆盖 ITE 和 ATE、包含 conservatism analysis），但在 baseline 完整性、semi-synthetic 数据生成细节、conditional coverage 评估、continuous track 可行性、和 synthetic DGP 设计方面存在需要补足的缺口。上述 8 个缺陷均为可补救项，没有方向性致命问题。补救后实验设计可以达到 EMNLP 主会的 soundness 门槛。最紧迫的行动项是：(1) 补全 baseline 层级设计、(2) 做 continuous embedding track 的 feasibility pilot、(3) 确认 MIMIC 数据 access 状态。

Sources:
- [Alaa et al. NeurIPS 2023 - Conformal Meta-learners](https://github.com/AlaaLab/conformal-metalearners)
- [Systematic Review of Conformal Inference for Treatment Effects](https://arxiv.org/html/2509.21660)
- [DoubleLingo: Causal Estimation with LLMs (NAACL 2024)](https://aclanthology.org/2024.naacl-short.71/)
- [Ma et al. LLM-Driven Treatment Effect Estimation (NeurIPS 2025)](https://arxiv.org/abs/2507.02843)
- [Csillag et al. Extending PPI through Conformal Prediction](https://arxiv.org/abs/2510.16166)
- [Zhang et al. Modular CP for Sequential Models](https://arxiv.org/abs/2510.04406)
- [Gasparin & Ramdas - Cross-Conformal Prediction (ICML 2025)](https://arxiv.org/abs/2503.01495)
- [Veitch et al. Adapting Text Embeddings for Causal Inference (UAI 2020)](https://proceedings.mlr.press/v124/veitch20a.html)
- [Chen et al. Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)](https://dl.acm.org/doi/10.1145/3637528.3671976)
- [Barnatchez et al. Debiased ML for Conformal Prediction under Runtime Confounding](https://arxiv.org/abs/2604.03772)
- [Prediction-Powered Causal Inferences](https://arxiv.org/abs/2502.06343)
- [Kato - Semi-Supervised Treatment Effect Estimation (NeurIPS 2025)](https://arxiv.org/abs/2511.08303)
- [Jonkers et al. Conformal Convolution Meta-learners](https://arxiv.org/abs/2402.04906v6)
- [Conformal Prediction for NLP Survey (TACL 2024)](https://arxiv.org/abs/2405.01976)
- [Proximal Causal Inference with Text Data](https://arxiv.org/pdf/2401.06687)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3317bcf-df48-415e-8db7-bf4ab54739f3",
  "isSidechain": false,
  "requestId": "req_011CbD98rrJbjQ4KENEDpbsG",
  "type": "assistant",
  "uuid": "ab664ba3-505b-4d00-bbb4-91eb2b182d28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdfoNaESLUCAngpWLZNwjb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 34727,
      "output_tokens": 7736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7736,
          "cache_read_input_tokens": 34727,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 925
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

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Description We propose ConformalPPITextCausal, a framework providing finite-sample coverage g…",
  "leafUuid": "ab664ba3-505b-4d00-bbb4-91eb2b182d28",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders  ## Description We propose ConformalPPITextCausal, a framework providing finite-sample coverage g…",
  "leafUuid": "ab664ba3-505b-4d00-bbb4-91eb2b182d28",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction for LLM-extracted text confounders",
  "sessionId": "7b79346c-83bc-4b4d-904c-08a80917a9e0"
}
```

---
