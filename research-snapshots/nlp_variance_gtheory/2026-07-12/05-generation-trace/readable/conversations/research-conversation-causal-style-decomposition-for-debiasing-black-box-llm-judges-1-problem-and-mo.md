# Research conversation: Causal Style Decomposition for Debiasing Black-Box LLM Judges ### 1. Problem and Motivation LLM-as-a-Judge pipelines are

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/8066299f-2afc-43d1-9d5b-37b6e29a5e5a.jsonl`
- **Structured JSON:** [`57b458d4864e0fbf6597.json`](../../sessions/57/57b458d4864e0fbf6597.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:20:21.263Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:20:21.263Z",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "content": "## Causal Style Decomposition for Debiasing Black-Box LLM Judges\n\n### 1. Problem and Motivation\n\nLLM-as-a-Judge pipelines are increasingly used for automated evaluation, but suffer from systematic style biases. SOS-Bench (arXiv:2409.15268) demonstrates that surface-level style features dominate substance in judge scoring. CASSE (arXiv:2601.10809) identifies 12 cross-correlated style features inducing evaluation side effects, with the core finding that style features are deeply entangled rather than orthogonal. Preference Leakage (ICLR 2026, arXiv:2502.01534) shows style-driven contamination propagates through training pipelines—from judge preferences to reward models to policy models. Soumik (arXiv:2604.23178) quantifies style bias at 0.76–0.92 across 5 judges, far exceeding position bias (≤0.04). Earlier work on LLM evaluation bias (NAACL 2024) and RubricBench (arXiv:2603.01562) further document how surface features mislead judges, revealing a 27% accuracy gap between model-generated and human rubrics on hard samples with misleading surface bias.\n\nCrucially, this is not merely an evaluation problem. Preference Leakage (ICLR 2026) demonstrates that style bias in judges propagates downstream: biased preference labels enter RLHF/DPO training data, contaminating reward models and ultimately policy models. Debiasing judges at the evaluation stage therefore has cascading benefits for the entire LLM alignment pipeline.\n\nExisting debiasing approaches each have fundamental limitations:\n\n- **Training-based**: FairJudge (arXiv:2602.06625) uses SFT→DPO→GRPO to retrain judges, requiring white-box access and per-judge retraining, inapplicable to proprietary models.\n- **Observational regression**: Length-Controlled AlpacaEval (ICLR 2025, arXiv:2404.04475) regresses out length effects at zero cost; Post-hoc Reward Calibration (ICLR 2025, arXiv:2409.17407) extends this via locally weighted regression across 33 reward models. Both handle only a single dimension and rely on observational associations that conflate genuine quality correlates with spurious confounding.\n- **Perturbation-based**: Bias-Bounded Evaluation (BBE, arXiv:2603.05485) injects DP-inspired Gaussian noise for formal bias bounds but destroys signal alongside bias; RATE (ICML 2025, arXiv:2410.11348) uses a double-rewrite protocol for causal explainability of reward models, providing the key insight that single-rewrite counterfactuals are imperfect and introduce substantial bias, but requires ~25x inference overhead and does not produce corrected scores.\n- **Reasoning-based**: RBD (NeurIPS 2025, arXiv:2505.17100) is a plug-in module that detects biased evaluations and guides self-correction via structured reasoning (+18.5% accuracy), but operates at the prompt level without disentangling specific style dimensions.\n- **Statistical**: PRECISE (AAAI 2026, arXiv:2601.18777) extends prediction-powered inference to combine human annotations with LLM judgments for debiased ranking estimation, but requires human labels and does not identify which style dimensions drive bias.\n- **Prompt-engineering**: Soumik (arXiv:2604.23178) evaluates 9 prompt-based strategies; the best (\"combined budget\") achieves +7.2 to +11.2pp on select model-strategy pairs.\n\nA parallel line of causal approaches targets reward model debiasing, all requiring white-box access or training-time intervention: Causally Motivated Inference-Time Intervention (arXiv:2604.27495) decomposes Bradley-Terry reward models via total effect / controlled direct effect and intervenes at the neuron level. CROME (arXiv:2604.13833) uses causal data augmentation to suppress prompt-independent shortcuts. Causal Rubrics (arXiv:2506.16507, ICML 2025) employs causal augmentations (pairs isolating causal attribute changes) and neutral augmentations (tie-labeled pairs varying spurious attributes) to train robust reward models, improving RewardBench accuracy by up to 5.4%. CoLD (arXiv:2507.15698) applies counterfactual reasoning and causal graph analysis for length debiasing of process reward models, but is limited to training-time, single-dimension (length), and white-box settings. Causal Reward Modeling (CRM; ICLR 2027, arXiv:2501.09620) enforces counterfactual invariance in reward predictions. CMBE (AAAI 2027, arXiv:2505.16522) proposes simultaneous multi-bias causal effect estimation and elimination.\n\nSeparately, counterfactual LLM-based style measurement (arXiv:2512.19908) demonstrates that LLM-generated counterfactual rewrites combined with Bradley-Terry aggregation can robustly quantify rhetorical style effects at scale (>250K counterfactuals on 8,485 ICLR papers)—but quantifies style without correcting for it.\n\nFoundational work on causal effects of linguistic properties (Pryzant et al., NAACL 2021) established methods for estimating causal effects of text attributes using distant supervision and pre-trained language models, providing the methodological precedent for CSD's approach.\n\n**The open gap**: No existing method provides principled, multi-dimensional causal debiasing for black-box LLM judges while preserving legitimate style-quality associations. White-box causal methods (Causal Rubrics, CoLD, arXiv:2604.27495) cannot be applied to proprietary judge APIs. Black-box methods remain limited to observational regression (LC-AlpacaEval) or prompt engineering (RBD, Soumik). CSD fills this gap by bridging two independently developing literatures: (1) the NLP evaluation community's empirical documentation of style biases with ad-hoc fixes, and (2) the causal inference / econometrics community's principled frameworks (Double Machine Learning; Chernozhukov et al. 2018) that have not yet been systematically applied to black-box LLM judge debiasing.\n\n### 2. Core Contributions\n\n1. **Causal Style Decomposition (CSD) framework**: A black-box, post-hoc method that decomposes LLM judge scores into content-driven and style-driven components via targeted counterfactual interventions along three style axes, using a dual-layer causal identification strategy: counterfactual intervention for first-stage identification, DML (Chernozhukov et al. 2018) for second-stage robustness against imperfect counterfactuals.\n\n2. **Legitimacy-aware correction**: Unlike all prior debiasing methods that implicitly assume style effects should be fully removed, CSD introduces a domain-conditional α parameter distinguishing domain-invariant style bias from domain-specific legitimate style-quality associations—addressing CASSE's (arXiv:2601.10809) finding that style removal has unintended side effects. This is a conceptual advance: the question is not just \"how much style bias exists\" but \"which portion of style influence is bias vs. signal.\"\n\n3. **Interventional Style Effect (ISE) metric**: A standardized, causal diagnostic for per-axis judge bias auditing. Unlike observational bias scores (e.g., Soumik's style bias metric of 0.76–0.92), ISE measures interventional causal sensitivity, enabling principled cross-judge comparison (\"GPT-4o's formality ISE is 2.3× Claude's\"), cross-domain analysis, and version-tracking of judge bias. ISE has potential as a community-standard bias reporting metric analogous to FID for image generation.\n\n4. **Empirical validation** across 5 judges × 5 benchmarks with 8 baselines, comprehensive ablations, compute-normalized comparisons, counterfactual quality auditing, and human evaluation.\n\n### 3. Method\n\n#### 3.1 Counterfactual Style Generation\n\nFor each response $r$, generate 6 counterfactuals by intervening on 3 style axes in 2 directions each:\n- **Formality**: formal ↔ informal tone (preserving content)\n- **Verbosity**: concise ↔ verbose (preserving information content)\n- **Formatting**: heavy markdown/structure ↔ plain text\n\nRewriter: Qwen3-32B (default). When the target judge is Qwen3-32B, use an independent rewriter (Llama-3.3-70B) to prevent rewriter-evaluator confounding, following the independence principle in RATE (ICML 2025, arXiv:2410.11348).\n\n**Content preservation gates**: Counterfactuals must pass BERTScore ≥ 0.92 AND NLI entailment score ≥ 0.95 relative to the original. Failing samples are re-generated (up to 3 retries) or excluded.\n\n**Three-axis design rationale**: Formality, verbosity, and formatting capture the dominant style variation documented in SOS-Bench (arXiv:2409.15268) and CASSE (arXiv:2601.10809). We treat their approximate independence as an empirical hypothesis to be verified (via correlation analysis of ISE estimates across axes), not an a priori assumption—important given CASSE's finding of style feature entanglement. Coverage analysis (fraction of total style variance these 3 axes explain) is included as an ablation. The framework extends to additional axes at linear cost.\n\n#### 3.2 Dual-Layer Causal Identification via DML\n\n**Why DML on top of counterfactual intervention?** A natural question is: given paired data (original + 6 counterfactuals), why not simply compute mean paired score differences as ATE estimates? The answer is that content preservation gates (BERTScore ≥ 0.92, NLI ≥ 0.95) are imperfect—residual content leakage inevitably passes through. RATE (ICML 2025, arXiv:2410.11348) demonstrated that imperfect counterfactuals introduce substantial bias in causal estimates, solving this via a double-rewrite protocol (rewriting the rewrite to cancel rewrite-induced bias). CSD takes an alternative approach with stronger theoretical guarantees:\n\n- **First layer (counterfactual intervention)**: Provides approximate do-calculus identification by actively manipulating style while holding content approximately fixed.\n- **Second layer (DML)**: The nuisance function $g(Content, Style_{-d})$ captures and partials out residual content variation that leaked through imperfect gates, providing doubly-robust, $\\sqrt{n}$-consistent estimation even if either the treatment or outcome model is misspecified.\n\nThis dual-layer design means CSD is robust to the imperfect-counterfactual problem that RATE solves via double-rewrite, but at ~7x inference cost (vs. RATE's ~25x) and with formal semiparametric efficiency guarantees.\n\nFor each style axis $d \\in \\{formality, verbosity, formatting\\}$, estimate the causal effect $\\beta_d$:\n\n$$Score = \\beta_d \\cdot Style_d + g(Content, Style_{-d}) + \\epsilon$$\n\nwhere $g(\\cdot)$ is estimated via gradient-boosted trees with 5-fold cross-fitting per Chernozhukov et al. (2018). Building on the causal identification logic of Pryzant et al. (NAACL 2021), this framework estimates the direct causal effect of each style dimension on judge scores while controlling for content quality and other style axes.\n\n#### 3.3 Legitimacy-Aware Correction\n\n$$Score_{debiased} = Score_{original} - \\sum_{d} (1 - \\alpha_d) \\cdot \\hat{\\beta}_d \\cdot (Style_d - Style_{ref})$$\n\nwhere $\\alpha_d \\in [0,1]$ is domain-conditional. $\\alpha_d = 0$: full debiasing; $\\alpha_d = 1$: no debiasing.\n\n**α calibration protocol**: Leave-one-benchmark-out cross-validation. Sensitivity analysis reports performance across α ∈ {0.0, 0.1, ..., 1.0}.\n\n#### 3.4 Format Adaptation\n\nCSD adapts to different evaluation formats: (a) **Pointwise** (MT-Bench): debias each response's score independently; (b) **Pairwise** (Arena-Hard-Auto, SOS-Bench): debias both chosen and rejected responses, then re-rank; (c) **Multi-choice** (RewardBench, RewardBench 2): debias each candidate's score independently, then select the highest-scoring candidate. Inference cost scales with the number of candidates per instance.\n\n#### 3.5 Inference Cost\n\nCSD requires 7 judge calls per response (1 original + 6 counterfactuals), ~7x overhead. This compares favorably to RATE's ~25x, while providing actionable score correction rather than only explainability.\n\n### 4. Experimental Design\n\n#### 4.1 Judges (5)\n\nGPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Qwen3-32B, Llama-4-Maverick. Covers 4 provider families and both proprietary and open-weight models.\n\n#### 4.2 Benchmarks (5)\n\n- **SOS-Bench** (arXiv:2409.15268): Style-substance separation evaluation\n- **RewardBench**: Standard reward model evaluation\n- **RewardBench 2** (arXiv:2506.01937): Updated with factuality and precise instruction following domains\n- **MT-Bench**: Multi-turn dialogue quality\n- **Arena-Hard-Auto**: Challenging single-turn evaluation\n\n#### 4.3 Baselines (8)\n\n| Baseline | Type | Extra cost | Applicability |\n|---|---|---|---|\n| Raw Judge | No debiasing | 1x | All judges |\n| LC-AlpacaEval (ICLR 2025, arXiv:2404.04475) | Single-dim observational regression | 1x | All judges |\n| Multi-Reg | Multi-dim observational regression | 1x | All judges |\n| BBE (arXiv:2603.05485) | DP noise injection | 1x | All judges |\n| Prompt-Debiasing (Soumik, arXiv:2604.23178) | Combined budget prompt strategy | 1x | All judges |\n| RATE-corrected (ICML 2025, arXiv:2410.11348) | Double-rewrite causal estimation + CSD-style correction | ~25x | All judges |\n| FairJudge (arXiv:2602.06625) | Training-based (SFT→DPO→GRPO) | 1x post-train | Open-weight only |\n| 7-Call Majority Vote | Same-budget sampling | 7x | All judges |\n\nMulti-Reg uses automated style feature extractors (markdown density, word count, Flesch-Kincaid readability) as covariates for multivariate regression—the most direct observational alternative to CSD. RATE-corrected applies RATE's double-rewrite causal estimates with CSD's correction formula, enabling direct comparison of the two causal identification strategies at different compute budgets. 7-Call Majority Vote controls for inference budget fairness. Results tables clearly distinguish all-judge-applicable baselines from open-weight-only methods (FairJudge) to avoid misleading comparison.\n\n#### 4.4 Metrics\n\n- **Primary**: Pairwise accuracy, Spearman/Kendall-τ correlation with ground-truth quality\n- **Diagnostic**: ISE per axis per judge (causal bias magnitude)\n- **Efficiency**: Accuracy-per-judge-call curve (1x, 3x, 5x, 7x, 25x budget)\n\n#### 4.5 Ablations\n\n1. **Decomposition method**: Linear regression vs. DML vs. nonparametric kernel estimation for β\n2. **Per-axis importance**: Single-axis (3 runs) + pairwise combinations (3 runs) + full 3-axis\n3. **Content preservation thresholds**: BERTScore ∈ {0.85, 0.88, 0.90, 0.92, 0.95} × NLI ∈ {0.90, 0.93, 0.95, 0.97}\n4. **Cross-rewriter consistency**: ISE and accuracy using Qwen3-32B vs. Llama-3.3-70B vs. Claude as rewriter\n5. **Axis coverage**: Variance decomposition—fraction of judge score variance explained by 3 axes vs. residual\n6. **α sensitivity**: Full grid α ∈ [0,1], per-domain performance landscape\n7. **ISE-based cross-judge comparison**: ISE estimates across judges and domains\n8. **Manipulation check**: Per-axis style metric effect sizes (Cohen's d) on automated proxies—formality → Flesch-Kincaid / formality classifier; verbosity → word count ratio; formatting → markdown element density. Validates that counterfactual interventions produce sufficient style variation for reliable ISE estimation.\n9. **DML robustness check** (supplementary): Nuisance estimator comparison (GBT vs. Random Forest vs. Lasso), per-cell effective sample size, and DML standard error analysis. Discussion of statistical power for smaller benchmarks (e.g., MT-Bench ~80 multi-turn dialogues).\n\n#### 4.6 Human Evaluation\n\n**Quality evaluation (200 responses)**: Stratified by divergence between CSD and raw judge rankings—sampled from top-20% (high divergence), middle 40%, and bottom 40% by divergence magnitude. 3 annotators per response, 5-point Likert scale evaluating content quality and presentation quality independently. Inter-annotator agreement target: Krippendorff's α ≥ 0.6, reported with bootstrap 95% CI. Annotation rubric includes operationalized definitions and anchor examples, following RubricBench (arXiv:2603.01562) best practices.\n\n**Counterfactual quality audit (100–150 pairs)**: ~50 per style axis, annotators judge: (1) whether target axis was successfully changed (binary), (2) whether non-target axes were unintentionally changed (Likert 1–5), (3) whether content semantics were preserved (Likert 1–5). Report Cohen's κ between automated gates (BERTScore + NLI) and human judgment, plus false positive/negative rates of the automated gates. This validates CSD's core assumption of content-preserving style intervention and addresses CASSE's (arXiv:2601.10809) entanglement concern.\n\n#### 4.7 Statistical Analysis\n\n- Pairwise accuracy differences: paired bootstrap test (10,000 resamples), 95% CIs\n- Correlation differences: Fisher r-to-z transformation for Spearman, bootstrap CIs for Kendall-τ\n- DML coefficients: asymptotic standard errors and p-values per Chernozhukov et al. (2018)\n- All main results include 95% confidence intervals\n\n### 5. Expected Outcome and Broader Impact\n\nCSD is expected to demonstrate that dual-layer causal identification (counterfactual intervention + DML) provides debiasing gains beyond observational regression (LC-AlpacaEval, Multi-Reg), perturbation methods (BBE), and prompt engineering (Soumik), particularly in domains where style-content confounding is strong. Comparison with RATE-corrected will isolate the efficiency advantage (7x vs. 25x) and compare robustness to imperfect counterfactuals (DML nuisance absorption vs. double-rewrite cancellation). The legitimacy-aware α mechanism is expected to show selective debiasing outperforms both full debiasing and no debiasing.\n\n**Broader impact on alignment pipelines**: Beyond evaluation, CSD can serve as a data quality intervention in RLHF/DPO pipelines. Preference Leakage (ICLR 2026, arXiv:2502.01534) demonstrated that style-biased judge labels contaminate reward models and downstream policies. Applying CSD to debias preference labels before they enter training could break this contamination chain at its source. While validating this downstream effect is beyond the scope of the current experiments, the framework is directly applicable to preference data curation, and we discuss this as a concrete direction for future work.\n\n**Acknowledged limitations**: (1) 3-axis coverage may miss residual style bias from uncovered dimensions; (2) counterfactual quality depends on rewriter capability; (3) 7x inference cost may be prohibitive for large-scale deployment, though axis-selective application reduces cost."
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:20:21.267Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:20:21.267Z",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-20T05:20:21.278Z_

## Causal Style Decomposition for Debiasing Black-Box LLM Judges

### 1. Problem and Motivation

LLM-as-a-Judge pipelines are increasingly used for automated evaluation, but suffer from systematic style biases. SOS-Bench (arXiv:2409.15268) demonstrates that surface-level style features dominate substance in judge scoring. CASSE (arXiv:2601.10809) identifies 12 cross-correlated style features inducing evaluation side effects, with the core finding that style features are deeply entangled rather than orthogonal. Preference Leakage (ICLR 2026, arXiv:2502.01534) shows style-driven contamination propagates through training pipelines—from judge preferences to reward models to policy models. Soumik (arXiv:2604.23178) quantifies style bias at 0.76–0.92 across 5 judges, far exceeding position bias (≤0.04). Earlier work on LLM evaluation bias (NAACL 2024) and RubricBench (arXiv:2603.01562) further document how surface features mislead judges, revealing a 27% accuracy gap between model-generated and human rubrics on hard samples with misleading surface bias.

Crucially, this is not merely an evaluation problem. Preference Leakage (ICLR 2026) demonstrates that style bias in judges propagates downstream: biased preference labels enter RLHF/DPO training data, contaminating reward models and ultimately policy models. Debiasing judges at the evaluation stage therefore has cascading benefits for the entire LLM alignment pipeline.

Existing debiasing approaches each have fundamental limitations:

- **Training-based**: FairJudge (arXiv:2602.06625) uses SFT→DPO→GRPO to retrain judges, requiring white-box access and per-judge retraining, inapplicable to proprietary models.
- **Observational regression**: Length-Controlled AlpacaEval (ICLR 2025, arXiv:2404.04475) regresses out length effects at zero cost; Post-hoc Reward Calibration (ICLR 2025, arXiv:2409.17407) extends this via locally weighted regression across 33 reward models. Both handle only a single dimension and rely on observational associations that conflate genuine quality correlates with spurious confounding.
- **Perturbation-based**: Bias-Bounded Evaluation (BBE, arXiv:2603.05485) injects DP-inspired Gaussian noise for formal bias bounds but destroys signal alongside bias; RATE (ICML 2025, arXiv:2410.11348) uses a double-rewrite protocol for causal explainability of reward models, providing the key insight that single-rewrite counterfactuals are imperfect and introduce substantial bias, but requires ~25x inference overhead and does not produce corrected scores.
- **Reasoning-based**: RBD (NeurIPS 2025, arXiv:2505.17100) is a plug-in module that detects biased evaluations and guides self-correction via structured reasoning (+18.5% accuracy), but operates at the prompt level without disentangling specific style dimensions.
- **Statistical**: PRECISE (AAAI 2026, arXiv:2601.18777) extends prediction-powered inference to combine human annotations with LLM judgments for debiased ranking estimation, but requires human labels and does not identify which style dimensions drive bias.
- **Prompt-engineering**: Soumik (arXiv:2604.23178) evaluates 9 prompt-based strategies; the best ("combined budget") achieves +7.2 to +11.2pp on select model-strategy pairs.

A parallel line of causal approaches targets reward model debiasing, all requiring white-box access or training-time intervention: Causally Motivated Inference-Time Intervention (arXiv:2604.27495) decomposes Bradley-Terry reward models via total effect / controlled direct effect and intervenes at the neuron level. CROME (arXiv:2604.13833) uses causal data augmentation to suppress prompt-independent shortcuts. Causal Rubrics (arXiv:2506.16507, ICML 2025) employs causal augmentations (pairs isolating causal attribute changes) and neutral augmentations (tie-labeled pairs varying spurious attributes) to train robust reward models, improving RewardBench accuracy by up to 5.4%. CoLD (arXiv:2507.15698) applies counterfactual reasoning and causal graph analysis for length debiasing of process reward models, but is limited to training-time, single-dimension (length), and white-box settings. Causal Reward Modeling (CRM; ICLR 2027, arXiv:2501.09620) enforces counterfactual invariance in reward predictions. CMBE (AAAI 2027, arXiv:2505.16522) proposes simultaneous multi-bias causal effect estimation and elimination.

Separately, counterfactual LLM-based style measurement (arXiv:2512.19908) demonstrates that LLM-generated counterfactual rewrites combined with Bradley-Terry aggregation can robustly quantify rhetorical style effects at scale (>250K counterfactuals on 8,485 ICLR papers)—but quantifies style without correcting for it.

Foundational work on causal effects of linguistic properties (Pryzant et al., NAACL 2021) established methods for estimating causal effects of text attributes using distant supervision and pre-trained language models, providing the methodological precedent for CSD's approach.

**The open gap**: No existing method provides principled, multi-dimensional causal debiasing for black-box LLM judges while preserving legitimate style-quality associations. White-box causal methods (Causal Rubrics, CoLD, arXiv:2604.27495) cannot be applied to proprietary judge APIs. Black-box methods remain limited to observational regression (LC-AlpacaEval) or prompt engineering (RBD, Soumik). CSD fills this gap by bridging two independently developing literatures: (1) the NLP evaluation community's empirical documentation of style biases with ad-hoc fixes, and (2) the causal inference / econometrics community's principled frameworks (Double Machine Learning; Chernozhukov et al. 2018) that have not yet been systematically applied to black-box LLM judge debiasing.

### 2. Core Contributions

1. **Causal Style Decomposition (CSD) framework**: A black-box, post-hoc method that decomposes LLM judge scores into content-driven and style-driven components via targeted counterfactual interventions along three style axes, using a dual-layer causal identification strategy: counterfactual intervention for first-stage identification, DML (Chernozhukov et al. 2018) for second-stage robustness against imperfect counterfactuals.

2. **Legitimacy-aware correction**: Unlike all prior debiasing methods that implicitly assume style effects should be fully removed, CSD introduces a domain-conditional α parameter distinguishing domain-invariant style bias from domain-specific legitimate style-quality associations—addressing CASSE's (arXiv:2601.10809) finding that style removal has unintended side effects. This is a conceptual advance: the question is not just "how much style bias exists" but "which portion of style influence is bias vs. signal."

3. **Interventional Style Effect (ISE) metric**: A standardized, causal diagnostic for per-axis judge bias auditing. Unlike observational bias scores (e.g., Soumik's style bias metric of 0.76–0.92), ISE measures interventional causal sensitivity, enabling principled cross-judge comparison ("GPT-4o's formality ISE is 2.3× Claude's"), cross-domain analysis, and version-tracking of judge bias. ISE has potential as a community-standard bias reporting metric analogous to FID for image generation.

4. **Empirical validation** across 5 judges × 5 benchmarks with 8 baselines, comprehensive ablations, compute-normalized comparisons, counterfactual quality auditing, and human evaluation.

### 3. Method

#### 3.1 Counterfactual Style Generation

For each response $r$, generate 6 counterfactuals by intervening on 3 style axes in 2 directions each:
- **Formality**: formal ↔ informal tone (preserving content)
- **Verbosity**: concise ↔ verbose (preserving information content)
- **Formatting**: heavy markdown/structure ↔ plain text

Rewriter: Qwen3-32B (default). When the target judge is Qwen3-32B, use an independent rewriter (Llama-3.3-70B) to prevent rewriter-evaluator confounding, following the independence principle in RATE (ICML 2025, arXiv:2410.11348).

**Content preservation gates**: Counterfactuals must pass BERTScore ≥ 0.92 AND NLI entailment score ≥ 0.95 relative to the original. Failing samples are re-generated (up to 3 retries) or excluded.

**Three-axis design rationale**: Formality, verbosity, and formatting capture the dominant style variation documented in SOS-Bench (arXiv:2409.15268) and CASSE (arXiv:2601.10809). We treat their approximate independence as an empirical hypothesis to be verified (via correlation analysis of ISE estimates across axes), not an a priori assumption—important given CASSE's finding of style feature entanglement. Coverage analysis (fraction of total style variance these 3 axes explain) is included as an ablation. The framework extends to additional axes at linear cost.

#### 3.2 Dual-Layer Causal Identification via DML

**Why DML on top of counterfactual intervention?** A natural question is: given paired data (original + 6 counterfactuals), why not simply compute mean paired score differences as ATE estimates? The answer is that content preservation gates (BERTScore ≥ 0.92, NLI ≥ 0.95) are imperfect—residual content leakage inevitably passes through. RATE (ICML 2025, arXiv:2410.11348) demonstrated that imperfect counterfactuals introduce substantial bias in causal estimates, solving this via a double-rewrite protocol (rewriting the rewrite to cancel rewrite-induced bias). CSD takes an alternative approach with stronger theoretical guarantees:

- **First layer (counterfactual intervention)**: Provides approximate do-calculus identification by actively manipulating style while holding content approximately fixed.
- **Second layer (DML)**: The nuisance function $g(Content, Style_{-d})$ captures and partials out residual content variation that leaked through imperfect gates, providing doubly-robust, $\sqrt{n}$-consistent estimation even if either the treatment or outcome model is misspecified.

This dual-layer design means CSD is robust to the imperfect-counterfactual problem that RATE solves via double-rewrite, but at ~7x inference cost (vs. RATE's ~25x) and with formal semiparametric efficiency guarantees.

For each style axis $d \in \{formality, verbosity, formatting\}$, estimate the causal effect $\beta_d$:

$$Score = \beta_d \cdot Style_d + g(Content, Style_{-d}) + \epsilon$$

where $g(\cdot)$ is estimated via gradient-boosted trees with 5-fold cross-fitting per Chernozhukov et al. (2018). Building on the causal identification logic of Pryzant et al. (NAACL 2021), this framework estimates the direct causal effect of each style dimension on judge scores while controlling for content quality and other style axes.

#### 3.3 Legitimacy-Aware Correction

$$Score_{debiased} = Score_{original} - \sum_{d} (1 - \alpha_d) \cdot \hat{\beta}_d \cdot (Style_d - Style_{ref})$$

where $\alpha_d \in [0,1]$ is domain-conditional. $\alpha_d = 0$: full debiasing; $\alpha_d = 1$: no debiasing.

**α calibration protocol**: Leave-one-benchmark-out cross-validation. Sensitivity analysis reports performance across α ∈ {0.0, 0.1, ..., 1.0}.

#### 3.4 Format Adaptation

CSD adapts to different evaluation formats: (a) **Pointwise** (MT-Bench): debias each response's score independently; (b) **Pairwise** (Arena-Hard-Auto, SOS-Bench): debias both chosen and rejected responses, then re-rank; (c) **Multi-choice** (RewardBench, RewardBench 2): debias each candidate's score independently, then select the highest-scoring candidate. Inference cost scales with the number of candidates per instance.

#### 3.5 Inference Cost

CSD requires 7 judge calls per response (1 original + 6 counterfactuals), ~7x overhead. This compares favorably to RATE's ~25x, while providing actionable score correction rather than only explainability.

### 4. Experimental Design

#### 4.1 Judges (5)

GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Qwen3-32B, Llama-4-Maverick. Covers 4 provider families and both proprietary and open-weight models.

#### 4.2 Benchmarks (5)

- **SOS-Bench** (arXiv:2409.15268): Style-substance separation evaluation
- **RewardBench**: Standard reward model evaluation
- **RewardBench 2** (arXiv:2506.01937): Updated with factuality and precise instruction following domains
- **MT-Bench**: Multi-turn dialogue quality
- **Arena-Hard-Auto**: Challenging single-turn evaluation

#### 4.3 Baselines (8)

| Baseline | Type | Extra cost | Applicability |
|---|---|---|---|
| Raw Judge | No debiasing | 1x | All judges |
| LC-AlpacaEval (ICLR 2025, arXiv:2404.04475) | Single-dim observational regression | 1x | All judges |
| Multi-Reg | Multi-dim observational regression | 1x | All judges |
| BBE (arXiv:2603.05485) | DP noise injection | 1x | All judges |
| Prompt-Debiasing (Soumik, arXiv:2604.23178) | Combined budget prompt strategy | 1x | All judges |
| RATE-corrected (ICML 2025, arXiv:2410.11348) | Double-rewrite causal estimation + CSD-style correction | ~25x | All judges |
| FairJudge (arXiv:2602.06625) | Training-based (SFT→DPO→GRPO) | 1x post-train | Open-weight only |
| 7-Call Majority Vote | Same-budget sampling | 7x | All judges |

Multi-Reg uses automated style feature extractors (markdown density, word count, Flesch-Kincaid readability) as covariates for multivariate regression—the most direct observational alternative to CSD. RATE-corrected applies RATE's double-rewrite causal estimates with CSD's correction formula, enabling direct comparison of the two causal identification strategies at different compute budgets. 7-Call Majority Vote controls for inference budget fairness. Results tables clearly distinguish all-judge-applicable baselines from open-weight-only methods (FairJudge) to avoid misleading comparison.

#### 4.4 Metrics

- **Primary**: Pairwise accuracy, Spearman/Kendall-τ correlation with ground-truth quality
- **Diagnostic**: ISE per axis per judge (causal bias magnitude)
- **Efficiency**: Accuracy-per-judge-call curve (1x, 3x, 5x, 7x, 25x budget)

#### 4.5 Ablations

1. **Decomposition method**: Linear regression vs. DML vs. nonparametric kernel estimation for β
2. **Per-axis importance**: Single-axis (3 runs) + pairwise combinations (3 runs) + full 3-axis
3. **Content preservation thresholds**: BERTScore ∈ {0.85, 0.88, 0.90, 0.92, 0.95} × NLI ∈ {0.90, 0.93, 0.95, 0.97}
4. **Cross-rewriter consistency**: ISE and accuracy using Qwen3-32B vs. Llama-3.3-70B vs. Claude as rewriter
5. **Axis coverage**: Variance decomposition—fraction of judge score variance explained by 3 axes vs. residual
6. **α sensitivity**: Full grid α ∈ [0,1], per-domain performance landscape
7. **ISE-based cross-judge comparison**: ISE estimates across judges and domains
8. **Manipulation check**: Per-axis style metric effect sizes (Cohen's d) on automated proxies—formality → Flesch-Kincaid / formality classifier; verbosity → word count ratio; formatting → markdown element density. Validates that counterfactual interventions produce sufficient style variation for reliable ISE estimation.
9. **DML robustness check** (supplementary): Nuisance estimator comparison (GBT vs. Random Forest vs. Lasso), per-cell effective sample size, and DML standard error analysis. Discussion of statistical power for smaller benchmarks (e.g., MT-Bench ~80 multi-turn dialogues).

#### 4.6 Human Evaluation

**Quality evaluation (200 responses)**: Stratified by divergence between CSD and raw judge rankings—sampled from top-20% (high divergence), middle 40%, and bottom 40% by divergence magnitude. 3 annotators per response, 5-point Likert scale evaluating content quality and presentation quality independently. Inter-annotator agreement target: Krippendorff's α ≥ 0.6, reported with bootstrap 95% CI. Annotation rubric includes operationalized definitions and anchor examples, following RubricBench (arXiv:2603.01562) best practices.

**Counterfactual quality audit (100–150 pairs)**: ~50 per style axis, annotators judge: (1) whether target axis was successfully changed (binary), (2) whether non-target axes were unintentionally changed (Likert 1–5), (3) whether content semantics were preserved (Likert 1–5). Report Cohen's κ between automated gates (BERTScore + NLI) and human judgment, plus false positive/negative rates of the automated gates. This validates CSD's core assumption of content-preserving style intervention and addresses CASSE's (arXiv:2601.10809) entanglement concern.

#### 4.7 Statistical Analysis

- Pairwise accuracy differences: paired bootstrap test (10,000 resamples), 95% CIs
- Correlation differences: Fisher r-to-z transformation for Spearman, bootstrap CIs for Kendall-τ
- DML coefficients: asymptotic standard errors and p-values per Chernozhukov et al. (2018)
- All main results include 95% confidence intervals

### 5. Expected Outcome and Broader Impact

CSD is expected to demonstrate that dual-layer causal identification (counterfactual intervention + DML) provides debiasing gains beyond observational regression (LC-AlpacaEval, Multi-Reg), perturbation methods (BBE), and prompt engineering (Soumik), particularly in domains where style-content confounding is strong. Comparison with RATE-corrected will isolate the efficiency advantage (7x vs. 25x) and compare robustness to imperfect counterfactuals (DML nuisance absorption vs. double-rewrite cancellation). The legitimacy-aware α mechanism is expected to show selective debiasing outperforms both full debiasing and no debiasing.

**Broader impact on alignment pipelines**: Beyond evaluation, CSD can serve as a data quality intervention in RLHF/DPO pipelines. Preference Leakage (ICLR 2026, arXiv:2502.01534) demonstrated that style-biased judge labels contaminate reward models and downstream policies. Applying CSD to debias preference labels before they enter training could break this contamination chain at its source. While validating this downstream effect is beyond the scope of the current experiments, the framework is directly applicable to preference data curation, and we discuss this as a concrete direction for future work.

**Acknowledged limitations**: (1) 3-axis coverage may miss residual style bias from uncovered dimensions; (2) counterfactual quality depends on rewriter capability; (3) 7x inference cost may be prohibitive for large-scale deployment, though axis-selective application reduces cost.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "4a108d23-8f5b-40a9-91b5-e695dc23f58d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:20:21.277Z_

```json
{
  "parentUuid": "4a108d23-8f5b-40a9-91b5-e695dc23f58d",
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
  "uuid": "32fb8954-e0a0-48b0-a64c-7bc9a104c6c4",
  "timestamp": "2026-05-20T05:20:21.277Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:20:21.277Z_

```json
{
  "parentUuid": "32fb8954-e0a0-48b0-a64c-7bc9a104c6c4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bf607db9-70b3-4e32-a9ab-c37a5f3cb192",
  "timestamp": "2026-05-20T05:20:21.277Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
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
  "lastPrompt": "## Causal Style Decomposition for Debiasing Black-Box LLM Judges  ### 1. Problem and Motivation  LLM-as-a-Judge pipelines are increasingly used for automated evaluation, but suffer from systematic sty…",
  "leafUuid": "bf607db9-70b3-4e32-a9ab-c37a5f3cb192",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Causal style decomposition for debiasing LLM judges",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:20:28.544Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal for EMNLP 2026. As the "发掘 agent," I need to focus on:

1. **Novelty** - How novel is the core contribution compared to recent work?
2. **Significance** - How important is the research problem?
3. **Related Work differentiation** - Is the positioning clear and are there missed related works?

Before giving any suggestions, I need to do thorough literature research. Let me search for the most relevant recent work in this area.

Let me start by searching for:
1. Recent work on LLM judge debiasing (especially causal approaches)


2. DML applied to NLP/LLM evaluation
3. Counterfactual style intervention for evaluation
4. The specific papers mentioned in the proposal to verify claims
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf607db9-70b3-4e32-a9ab-c37a5f3cb192",
  "isSidechain": false,
  "requestId": "req_011CbDFvKSANioAFS27QHbvf",
  "type": "assistant",
  "uuid": "6667b06d-7d7c-4dc7-9a20-2c12f913c367",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSoxbNgTY7jTPZZ5Gi1X63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6442,
      "cache_read_input_tokens": 14549,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 6442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6442
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

_source line 9 · 2026-05-20T05:20:28.891Z_

I need to do thorough literature research before making any assessments. Let me search for the most relevant recent work across several dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6667b06d-7d7c-4dc7-9a20-2c12f913c367",
  "isSidechain": false,
  "requestId": "req_011CbDFvKSANioAFS27QHbvf",
  "type": "assistant",
  "uuid": "acf79e63-4a25-4f3c-83a3-f6078a408c5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSoxbNgTY7jTPZZ5Gi1X63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6442,
      "cache_read_input_tokens": 14549,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 6442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6442
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

_source line 10 · 2026-05-20T05:20:29.432Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NDhgDHKd92eyBjyP7eiPx5`</summary>

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
  "parentUuid": "acf79e63-4a25-4f3c-83a3-f6078a408c5f",
  "isSidechain": false,
  "requestId": "req_011CbDFvKSANioAFS27QHbvf",
  "type": "assistant",
  "uuid": "bd9d9bb5-e142-4759-a2c3-deca35cf7164",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSoxbNgTY7jTPZZ5Gi1X63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6442,
      "cache_read_input_tokens": 14549,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 6442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6442
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

_source line 11 · 2026-05-20T05:20:29.439Z_

<details><summary>↩ Tool result · `toolu_01NDhgDHKd92eyBjyP7eiPx5`</summary>

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
  "parentUuid": "bd9d9bb5-e142-4759-a2c3-deca35cf7164",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "915bb774-6d54-4565-9327-1749c4cd67bd",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "bd9d9bb5-e142-4759-a2c3-deca35cf7164",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:20:32.348Z_

Now let me conduct my front-loaded literature research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "915bb774-6d54-4565-9327-1749c4cd67bd",
  "isSidechain": false,
  "requestId": "req_011CbDFvvoQkPauJFZV1Ye3s",
  "type": "assistant",
  "uuid": "731cf77c-2b46-43a6-8d39-69d1d4fe3155",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D621wAXBVE3PSFbErCzMfR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 20991,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 20991,
          "cache_creation_input_tokens": 827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 827
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

_source line 13 · 2026-05-20T05:20:32.859Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01McM3dBSf6bPfuW45HBG17F`</summary>

```json
{
  "query": "causal debiasing LLM judge style bias 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "731cf77c-2b46-43a6-8d39-69d1d4fe3155",
  "isSidechain": false,
  "requestId": "req_011CbDFvvoQkPauJFZV1Ye3s",
  "type": "assistant",
  "uuid": "e53bcef8-60e3-4dc0-b959-d8955b49c3fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D621wAXBVE3PSFbErCzMfR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 20991,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 20991,
          "cache_creation_input_tokens": 827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 827
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

_source line 14 · 2026-05-20T05:20:39.928Z_

<details><summary>↩ Tool result · `toolu_01McM3dBSf6bPfuW45HBG17F`</summary>

```text
Web search results for query: "causal debiasing LLM judge style bias 2025 2026"

Links: [{"title":"Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector | OpenReview","url":"https://openreview.net/forum?id=sLNz60fJFF"},{"title":"LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline","url":"https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"},{"title":"LLM-Based Judge Model","url":"https://www.emergentmind.com/topics/llm-based-judge-model"},{"title":"[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/abs/2604.23178"},{"title":"[2505.17100] Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector","url":"https://arxiv.org/abs/2505.17100"},{"title":"Causal-Guided Active Learning for Debiasing Large Language Models","url":"https://arxiv.org/pdf/2408.12942"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"Causal Prompting: Debiasing Large Language Model Prompting based on   Front-Door Adjustment","url":"https://arxiv.org/pdf/2403.02738"}]

Based on the search results, here's what recent research shows about causal debiasing, LLM judges, and style bias in 2025-2026:

## Key Research Findings

**Bias Types in LLM Judges:**
LLM-based judges remain susceptible to prompt injection, position/length bias, and agreeableness bias even at the highest model scales. Position bias causes evaluators to disproportionately prefer outputs in specific positions regardless of quality, while verbosity bias leads to higher ratings for longer responses even when quality is similar to briefer alternatives.

**Debiasing Approaches:**
One recent approach called RBD (Reasoning-based Bias Detector) operates externally through an iterative process of bias detection and feedback-driven revision, and was presented at NeurIPS 2025. Current debiasing strategies including prompt augmentation, ensembling, and counterfactual audits are necessary but insufficient, particularly for domain- and language-general evaluation.

**Causal Debiasing Methods:**
Causal inference-based methods have become popular due to their strict theoretical guarantees and good generalization, and only need to calibrate prediction results in the inference stage, making them suitable for prompt-based learning scenarios.

**Open Challenges:**
Causal origins of scoring bias, integration of multi-modal judgment, and transitivity/consistency guarantees for pairwise and listwise evaluation systems remain open problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e53bcef8-60e3-4dc0-b959-d8955b49c3fc",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "2929eb31-e53d-4371-a467-d6c2dd3015c3",
  "toolUseResult": {
    "query": "causal debiasing LLM judge style bias 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016DKeH3UGM5QfUdKsxAMNaV",
        "content": [
          {
            "title": "Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector | OpenReview",
            "url": "https://openreview.net/forum?id=sLNz60fJFF"
          },
          {
            "title": "LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline",
            "url": "https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"
          },
          {
            "title": "LLM-Based Judge Model",
            "url": "https://www.emergentmind.com/topics/llm-based-judge-model"
          },
          {
            "title": "[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/abs/2604.23178"
          },
          {
            "title": "[2505.17100] Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector",
            "url": "https://arxiv.org/abs/2505.17100"
          },
          {
            "title": "Causal-Guided Active Learning for Debiasing Large Language Models",
            "url": "https://arxiv.org/pdf/2408.12942"
          },
          {
            "title": "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2509.26072"
          },
          {
            "title": "Causal Prompting: Debiasing Large Language Model Prompting based on   Front-Door Adjustment",
            "url": "https://arxiv.org/pdf/2403.02738"
          }
        ]
      },
      "Based on the search results, here's what recent research shows about causal debiasing, LLM judges, and style bias in 2025-2026:\n\n## Key Research Findings\n\n**Bias Types in LLM Judges:**\nLLM-based judges remain susceptible to prompt injection, position/length bias, and agreeableness bias even at the highest model scales. Position bias causes evaluators to disproportionately prefer outputs in specific positions regardless of quality, while verbosity bias leads to higher ratings for longer responses even when quality is similar to briefer alternatives.\n\n**Debiasing Approaches:**\nOne recent approach called RBD (Reasoning-based Bias Detector) operates externally through an iterative process of bias detection and feedback-driven revision, and was presented at NeurIPS 2025. Current debiasing strategies including prompt augmentation, ensembling, and counterfactual audits are necessary but insufficient, particularly for domain- and language-general evaluation.\n\n**Causal Debiasing Methods:**\nCausal inference-based methods have become popular due to their strict theoretical guarantees and good generalization, and only need to calibrate prediction results in the inference stage, making them suitable for prompt-based learning scenarios.\n\n**Open Challenges:**\nCausal origins of scoring bias, integration of multi-modal judgment, and transitivity/consistency guarantees for pairwise and listwise evaluation systems remain open problems."
    ],
    "durationSeconds": 7.0627830660000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e53bcef8-60e3-4dc0-b959-d8955b49c3fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:20:46.887Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RsjBg62iFHTNAKMGYNhaTw`</summary>

```json
{
  "query": "Double Machine Learning DML text NLP causal inference counterfactual 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2929eb31-e53d-4371-a467-d6c2dd3015c3",
  "isSidechain": false,
  "requestId": "req_011CbDFwh1iiLCiMbcwrUktt",
  "type": "assistant",
  "uuid": "45a97ed4-a69f-4821-8e11-827f5710ded6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lyn34SmR4eqJMgEQbuhYS7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 21818,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 21818,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 858
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

_source line 16 · 2026-05-20T05:20:53.749Z_

<details><summary>↩ Tool result · `toolu_01RsjBg62iFHTNAKMGYNhaTw`</summary>

```text
Web search results for query: "Double Machine Learning DML text NLP causal inference counterfactual 2024 2025"

Links: [{"title":"Double Machine Learning for Causal Inference under Shared-State Interference","url":"https://ideas.repec.org/p/arx/papers/2504.08836.html"},{"title":"Anytime-Valid Inference for Double/Debiased Machine Learning of Causal   Parameters","url":"https://arxiv.org/pdf/2408.09598"},{"title":"Double Machine Learning for Causal Inference on High-Dimensional Data: A Flexible and Robust Approach to Causal Estimation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-6465-1_9"},{"title":"Counterfactually Fair Regression with Double Machine Learning","url":"https://arxiv.org/pdf/2303.11529"},{"title":"Better Think Thrice: Learning to Reason Causally with Double Counterfactual Consistency","url":"https://arxiv.org/pdf/2602.16787"},{"title":"Double Debiased Machine Learning Nonparametric Inference with Continuous   Treatments","url":"https://arxiv.org/pdf/2004.03036"},{"title":"Hyperparameter Tuning for Causal Inference with Double Machine Learning:   A Simulation Study","url":"https://arxiv.org/pdf/2402.04674"}]

Based on the web search results, here's what I found on Double Machine Learning (DML) in recent research:

## Key Findings on DML

**Core Framework and Applications:**
Double machine learning (DML) is a methodological framework that applies machine learning to reduce omitted variable bias in causal inference. DML combines the strengths of machine learning for prediction with estimation and inference of causal parameters.

**Recent Developments (2024-2025):**

1. **Inference Methods**: Double (debiased) machine learning (DML) has seen widespread use in recent years for learning causal/structural parameters, in part due to its flexibility and adaptability to high-dimensional nuisance functions as well as its ability to avoid bias from regularization or overfitting.

2. **Advanced Extensions**: Recent work extends the double machine learning theorem providing conditions for achieving efficient inference under shared-state interference.

3. **Counterfactual Applications**: The use of double machine learning allows for a model that can fit more complex functions with machine learning methods just as sophisticated as the final prediction algorithm under theoretical guarantees.

4. **Continuous Treatments**: DML estimators for the average dose-response function and partial effects are asymptotically normal with nonparametric convergence rates.

**Practical Considerations:**
Research provides empirical insights on the role of hyperparameter tuning and other practical decisions for causal estimation with DML, including the importance of data splitting schemes for tuning ML learners and how the choice of ML methods and hyperparameters impacts estimation performance.

The search results show active research in DML applications to causal inference, though specific NLP-focused applications weren't prominent in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45a97ed4-a69f-4821-8e11-827f5710ded6",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "9d937020-e69f-41dd-a733-f15cc1481f0c",
  "toolUseResult": {
    "query": "Double Machine Learning DML text NLP causal inference counterfactual 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012smb8DmtAZNcRyu41TsQFv",
        "content": [
          {
            "title": "Double Machine Learning for Causal Inference under Shared-State Interference",
            "url": "https://ideas.repec.org/p/arx/papers/2504.08836.html"
          },
          {
            "title": "Anytime-Valid Inference for Double/Debiased Machine Learning of Causal   Parameters",
            "url": "https://arxiv.org/pdf/2408.09598"
          },
          {
            "title": "Double Machine Learning for Causal Inference on High-Dimensional Data: A Flexible and Robust Approach to Causal Estimation | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-981-95-6465-1_9"
          },
          {
            "title": "Counterfactually Fair Regression with Double Machine Learning",
            "url": "https://arxiv.org/pdf/2303.11529"
          },
          {
            "title": "Better Think Thrice: Learning to Reason Causally with Double Counterfactual Consistency",
            "url": "https://arxiv.org/pdf/2602.16787"
          },
          {
            "title": "Double Debiased Machine Learning Nonparametric Inference with Continuous   Treatments",
            "url": "https://arxiv.org/pdf/2004.03036"
          },
          {
            "title": "Hyperparameter Tuning for Causal Inference with Double Machine Learning:   A Simulation Study",
            "url": "https://arxiv.org/pdf/2402.04674"
          }
        ]
      },
      "Based on the web search results, here's what I found on Double Machine Learning (DML) in recent research:\n\n## Key Findings on DML\n\n**Core Framework and Applications:**\nDouble machine learning (DML) is a methodological framework that applies machine learning to reduce omitted variable bias in causal inference. DML combines the strengths of machine learning for prediction with estimation and inference of causal parameters.\n\n**Recent Developments (2024-2025):**\n\n1. **Inference Methods**: Double (debiased) machine learning (DML) has seen widespread use in recent years for learning causal/structural parameters, in part due to its flexibility and adaptability to high-dimensional nuisance functions as well as its ability to avoid bias from regularization or overfitting.\n\n2. **Advanced Extensions**: Recent work extends the double machine learning theorem providing conditions for achieving efficient inference under shared-state interference.\n\n3. **Counterfactual Applications**: The use of double machine learning allows for a model that can fit more complex functions with machine learning methods just as sophisticated as the final prediction algorithm under theoretical guarantees.\n\n4. **Continuous Treatments**: DML estimators for the average dose-response function and partial effects are asymptotically normal with nonparametric convergence rates.\n\n**Practical Considerations:**\nResearch provides empirical insights on the role of hyperparameter tuning and other practical decisions for causal estimation with DML, including the importance of data splitting schemes for tuning ML learners and how the choice of ML methods and hyperparameters impacts estimation performance.\n\nThe search results show active research in DML applications to causal inference, though specific NLP-focused applications weren't prominent in these results."
    ],
    "durationSeconds": 6.856828581999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "45a97ed4-a69f-4821-8e11-827f5710ded6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:20:56.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CjogkdEXwrmxZeoFiRFzks`</summary>

```json
{
  "query": "counterfactual style rewriting LLM evaluation reward model debiasing 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d937020-e69f-41dd-a733-f15cc1481f0c",
  "isSidechain": false,
  "requestId": "req_011CbDFxi6EWap4ZLU4UR9ai",
  "type": "assistant",
  "uuid": "f7be6945-848d-4cff-accd-80925aaf2c38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FoHCHRgnnCfFzwoptGMP9K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 22676,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 22676,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 18 · 2026-05-20T05:21:05.327Z_

<details><summary>↩ Tool result · `toolu_01CjogkdEXwrmxZeoFiRFzks`</summary>

```text
Web search results for query: "counterfactual style rewriting LLM evaluation reward model debiasing 2025 2026 arXiv"

Links: [{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://www.arxiv.org/pdf/2507.15698"},{"title":"Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/html/2604.27495"},{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/html/2507.15698v1"},{"title":"[2507.15698] CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/abs/2507.15698"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/html/2512.19908v1"},{"title":"[2512.19908] Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/abs/2512.19908"},{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning","url":"https://arxiv.org/pdf/2602.06475"}]

Based on the web search results, here are several highly relevant papers from arXiv in 2025-2026 that address the intersection of counterfactual reasoning, style rewriting, LLM evaluation, reward models, and debiasing:

## Key Papers Found:

1. **CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models** (July 2025)
   - Proposes CoLD, a framework that mitigates length bias through an explicit length-penalty adjustment, a learned bias estimator, and a joint training strategy that enforces length-invariance in reward predictions
   - The approach is grounded in counterfactual reasoning and informed by causal graph analysis, with experiments showing it reduces reward-length correlation and improves accuracy in step selection

2. **Debiasing Reward Models via Causally Motivated Inference-Time Intervention** (Recently updated, 2026)
   - Addresses counterfactual questions like "What would the rewards be if the responses were equivalent with respect to these biases?"
   - Addresses biases in stylistic cues including length, bold text, exclamation marks, and lists

3. **Counterfactual LLM-based Framework for Measuring Rhetorical Style** (December 2025)
   - Introduces a counterfactual framework where multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, with an LLM judge comparing them through pairwise evaluations

4. **Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning** (February 2026)
   - Proposes an episodic causal counterfactual reward that captures robustness and effectiveness, with token-level advantages optimized to encourage LLMs to favor counterfactually robust reasoning patterns

These papers collectively address counterfactual methods for evaluating and debiasing LLM reward models through style and content analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7be6945-848d-4cff-accd-80925aaf2c38",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "5de48a52-6b13-431b-87c0-32f12d7b575a",
  "toolUseResult": {
    "query": "counterfactual style rewriting LLM evaluation reward model debiasing 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CELhD9Wpo86RKvUmehJwdi",
        "content": [
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://www.arxiv.org/pdf/2507.15698"
          },
          {
            "title": "Debiasing Reward Models via Causally Motivated Inference-Time Intervention",
            "url": "https://arxiv.org/html/2604.27495"
          },
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/html/2507.15698v1"
          },
          {
            "title": "[2507.15698] CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/abs/2507.15698"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/html/2512.19908v1"
          },
          {
            "title": "[2512.19908] Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/abs/2512.19908"
          },
          {
            "title": "Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2602.06475"
          }
        ]
      },
      "Based on the web search results, here are several highly relevant papers from arXiv in 2025-2026 that address the intersection of counterfactual reasoning, style rewriting, LLM evaluation, reward models, and debiasing:\n\n## Key Papers Found:\n\n1. **CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models** (July 2025)\n   - Proposes CoLD, a framework that mitigates length bias through an explicit length-penalty adjustment, a learned bias estimator, and a joint training strategy that enforces length-invariance in reward predictions\n   - The approach is grounded in counterfactual reasoning and informed by causal graph analysis, with experiments showing it reduces reward-length correlation and improves accuracy in step selection\n\n2. **Debiasing Reward Models via Causally Motivated Inference-Time Intervention** (Recently updated, 2026)\n   - Addresses counterfactual questions like \"What would the rewards be if the responses were equivalent with respect to these biases?\"\n   - Addresses biases in stylistic cues including length, bold text, exclamation marks, and lists\n\n3. **Counterfactual LLM-based Framework for Measuring Rhetorical Style** (December 2025)\n   - Introduces a counterfactual framework where multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, with an LLM judge comparing them through pairwise evaluations\n\n4. **Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning** (February 2026)\n   - Proposes an episodic causal counterfactual reward that captures robustness and effectiveness, with token-level advantages optimized to encourage LLMs to favor counterfactually robust reasoning patterns\n\nThese papers collectively address counterfactual methods for evaluating and debiasing LLM reward models through style and content analysis."
    ],
    "durationSeconds": 8.819240444000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f7be6945-848d-4cff-accd-80925aaf2c38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:21:14.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HD4QtaTGJd662AK7zHhpJB`</summary>

```json
{
  "query": "RATE reward model causal explainability double rewrite arXiv 2410.11348"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5de48a52-6b13-431b-87c0-32f12d7b575a",
  "isSidechain": false,
  "requestId": "req_011CbDFyZc35vrqyXcSTBVhR",
  "type": "assistant",
  "uuid": "179365e0-e5be-4fc2-bbd7-410702be4a33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ryy9x7Y2VpbFg2NSSQ4Edv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 23505,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 912,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 23505,
          "cache_creation_input_tokens": 912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 912
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Causal Style Decomposition for Debiasing Black-Box LLM Judges  ### 1. Problem and Motivation  LLM-as-a-Judge pipelines are increasingly used for automated evaluation, but suffer from systematic sty…",
  "leafUuid": "179365e0-e5be-4fc2-bbd7-410702be4a33",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Causal style decomposition for debiasing LLM judges",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

### Tool result

_source line 22 · 2026-05-20T05:21:21.103Z_

<details><summary>↩ Tool result · `toolu_01HD4QtaTGJd662AK7zHhpJB`</summary>

```text
Web search results for query: "RATE reward model causal explainability double rewrite arXiv 2410.11348"

Links: [{"title":"[2410.11348] RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/abs/2410.11348"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/pdf/2410.11348"},{"title":"[2410.11348v1] RATE: Score Reward Models with Imperfect Rewrites of Rewrites","url":"https://arxiv.org/abs/2410.11348v1"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals | OpenReview","url":"https://openreview.net/forum?id=rL3uxe5a0c"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://arxiv.org/html/2410.11348"},{"title":"ICML Poster RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://icml.cc/virtual/2025/poster/43898"},{"title":"RATE: Score Reward Models with Imperfect Rewrites of Rewrites","url":"https://arxiv.org/html/2410.11348v1/"},{"title":"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals","url":"https://proceedings.mlr.press/v267/reber25a.html"},{"title":"Robust Reward Modeling for Large Language Models via Causal Decomposition","url":"https://arxiv.org/html/2604.13833"}]

I found the paper! Here's the information about arXiv paper 2410.11348:

**RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals**

The paper develops Rewrite-based Attribute Treatment Estimator (RATE) as a method for measuring the sensitivity of a reward model to high-level attributes of responses, such as sentiment, helpfulness, or complexity.

**Key Problem:**
Reward models are widely used as proxies for human preferences when aligning or evaluating LLMs, but they are black boxes where it is often unclear what they are actually rewarding.

**The Double Rewrite Approach:**
RATE uses LLMs to rewrite responses to produce imperfect counterfactual examples that can be used to measure causal effects. A key challenge is that these rewrites are imperfect in a manner that can induce substantial bias in the estimated sensitivity of the reward model to the target attribute. The core idea of RATE is to adjust for this imperfect-rewrite effect by rewriting twice.

**Authors:** David Reber, Sean M. Richardson, Todd Nief, Cristina Garbacea, and Victor Veitch

The paper was submitted in October 2024 and was recently published at ICML 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "179365e0-e5be-4fc2-bbd7-410702be4a33",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "ee39225f-80ba-4813-99ca-24bbbfe23dac",
  "toolUseResult": {
    "query": "RATE reward model causal explainability double rewrite arXiv 2410.11348",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QHcvVEJCFT92aNuAJE3PEN",
        "content": [
          {
            "title": "[2410.11348] RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://arxiv.org/abs/2410.11348"
          },
          {
            "title": "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://arxiv.org/pdf/2410.11348"
          },
          {
            "title": "[2410.11348v1] RATE: Score Reward Models with Imperfect Rewrites of Rewrites",
            "url": "https://arxiv.org/abs/2410.11348v1"
          },
          {
            "title": "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals | OpenReview",
            "url": "https://openreview.net/forum?id=rL3uxe5a0c"
          },
          {
            "title": "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://arxiv.org/html/2410.11348"
          },
          {
            "title": "ICML Poster RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://icml.cc/virtual/2025/poster/43898"
          },
          {
            "title": "RATE: Score Reward Models with Imperfect Rewrites of Rewrites",
            "url": "https://arxiv.org/html/2410.11348v1/"
          },
          {
            "title": "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals",
            "url": "https://proceedings.mlr.press/v267/reber25a.html"
          },
          {
            "title": "Robust Reward Modeling for Large Language Models via Causal Decomposition",
            "url": "https://arxiv.org/html/2604.13833"
          }
        ]
      },
      "I found the paper! Here's the information about arXiv paper 2410.11348:\n\n**RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals**\n\nThe paper develops Rewrite-based Attribute Treatment Estimator (RATE) as a method for measuring the sensitivity of a reward model to high-level attributes of responses, such as sentiment, helpfulness, or complexity.\n\n**Key Problem:**\nReward models are widely used as proxies for human preferences when aligning or evaluating LLMs, but they are black boxes where it is often unclear what they are actually rewarding.\n\n**The Double Rewrite Approach:**\nRATE uses LLMs to rewrite responses to produce imperfect counterfactual examples that can be used to measure causal effects. A key challenge is that these rewrites are imperfect in a manner that can induce substantial bias in the estimated sensitivity of the reward model to the target attribute. The core idea of RATE is to adjust for this imperfect-rewrite effect by rewriting twice.\n\n**Authors:** David Reber, Sean M. Richardson, Todd Nief, Cristina Garbacea, and Victor Veitch\n\nThe paper was submitted in October 2024 and was recently published at ICML 2025."
    ],
    "durationSeconds": 6.279149772000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "179365e0-e5be-4fc2-bbd7-410702be4a33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T05:21:23.291Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ev6xhyH88Gmi2X5UXo4uV7`</summary>

```json
{
  "query": "preference leakage style bias RLHF DPO reward model contamination arXiv 2502.01534"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee39225f-80ba-4813-99ca-24bbbfe23dac",
  "isSidechain": false,
  "requestId": "req_011CbDFzj55ebAhjRZNsXBq2",
  "type": "assistant",
  "uuid": "61af445b-a23b-4073-acfe-9c8cc9e6f8e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QMz6wPcfXW9s4ZRzeAJDK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 24417,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 24417,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 866
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

_source line 24 · 2026-05-20T05:21:28.882Z_

<details><summary>↩ Tool result · `toolu_01Ev6xhyH88Gmi2X5UXo4uV7`</summary>

```text
Web search results for query: "preference leakage style bias RLHF DPO reward model contamination arXiv 2502.01534"

Links: [{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"[2510.05526] Provably Mitigating Corruption, Overoptimization, and Verbosity Simultaneously in Offline and Online RLHF/DPO Alignment","url":"https://arxiv.org/abs/2510.05526"},{"title":"Uncertainty-Penalized Direct Preference Optimization","url":"https://arxiv.org/pdf/2410.20187"},{"title":"Disentangling Length Bias in Preference Learning via Response-Conditioned Modeling","url":"https://arxiv.org/html/2502.00814"},{"title":"Detecting Prefix Bias in LLM-based Reward Models","url":"https://arxiv.org/pdf/2505.13487"},{"title":"On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization","url":"https://arxiv.org/pdf/2405.16455"}]

Based on the search results, I found the paper you're looking for. Preference Leakage is a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators.

The research defines three common relatednesses between the data generator LLM and the judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family. Through extensive experiments, the authors empirically confirm the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks.

The analysis suggests that preference leakage is a pervasive and real-world problem that is harder to detect compared to previously identified biases in LLM-as-a-judge scenarios.

The arXiv paper (2502.01534) was last updated on March 4, 2026, and the authors have released their code and data publicly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61af445b-a23b-4073-acfe-9c8cc9e6f8e2",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "0e0ceb32-69e3-4666-8e7f-cf32d8f96af7",
  "toolUseResult": {
    "query": "preference leakage style bias RLHF DPO reward model contamination arXiv 2502.01534",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HTaDnwosLN9HKtTooXJpnu",
        "content": [
          {
            "title": "[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://arxiv.org/abs/2502.01534"
          },
          {
            "title": "[2510.05526] Provably Mitigating Corruption, Overoptimization, and Verbosity Simultaneously in Offline and Online RLHF/DPO Alignment",
            "url": "https://arxiv.org/abs/2510.05526"
          },
          {
            "title": "Uncertainty-Penalized Direct Preference Optimization",
            "url": "https://arxiv.org/pdf/2410.20187"
          },
          {
            "title": "Disentangling Length Bias in Preference Learning via Response-Conditioned Modeling",
            "url": "https://arxiv.org/html/2502.00814"
          },
          {
            "title": "Detecting Prefix Bias in LLM-based Reward Models",
            "url": "https://arxiv.org/pdf/2505.13487"
          },
          {
            "title": "On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization",
            "url": "https://arxiv.org/pdf/2405.16455"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Preference Leakage is a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators.\n\nThe research defines three common relatednesses between the data generator LLM and the judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family. Through extensive experiments, the authors empirically confirm the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks.\n\nThe analysis suggests that preference leakage is a pervasive and real-world problem that is harder to detect compared to previously identified biases in LLM-as-a-judge scenarios.\n\nThe arXiv paper (2502.01534) was last updated on March 4, 2026, and the authors have released their code and data publicly."
    ],
    "durationSeconds": 5.587087806999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "61af445b-a23b-4073-acfe-9c8cc9e6f8e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:21:32.332Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUBUzpfZDFzfN3NVvtYkHY`</summary>

```json
{
  "query": "CASSE cross-correlated style features evaluation side effects arXiv 2601.10809 causal rubrics reward model arXiv 2506.16507"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e0ceb32-69e3-4666-8e7f-cf32d8f96af7",
  "isSidechain": false,
  "requestId": "req_011CbDG1JK5ZP3DdW7Ninx1r",
  "type": "assistant",
  "uuid": "75ecfd7b-77c5-43b4-9f35-113309821951",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01569Y8wk266mmUvWqdChBcY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 25283,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 25283,
          "cache_creation_input_tokens": 638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 638
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

_source line 26 · 2026-05-20T05:21:41.393Z_

<details><summary>↩ Tool result · `toolu_01WUBUzpfZDFzfN3NVvtYkHY`</summary>

```text
Web search results for query: "CASSE cross-correlated style features evaluation side effects arXiv 2601.10809 causal rubrics reward model arXiv 2506.16507"

Links: [{"title":"[2601.10809] A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/abs/2601.10809"},{"title":"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/html/2601.10809"},{"title":"Improved Style Transfer by Respecting Inter-layer Correlations","url":"https://arxiv.org/pdf/1801.01933"},{"title":"Style is NOT a single variable: Case Studies for Cross-Style Language   Understanding","url":"https://arxiv.org/pdf/1911.03663"},{"title":"Domain Generalization with Correlated Style Uncertainty","url":"https://arxiv.org/pdf/2212.09950"},{"title":"Cross‐validated permutation feature importance considering correlation between features","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10989554/"}]

Links: [{"title":"[2506.16507] Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/abs/2506.16507"},{"title":"[Quick Review] Robust Reward Modeling via Causal Rubrics","url":"https://liner.com/review/robust-reward-modeling-via-causal-rubrics"},{"title":"arXiv:2506.16507v1 [cs.LG] 19 Jun 2025 2025-6-23","url":"https://arxiv.org/pdf/2506.16507"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://www.researchgate.net/publication/392918827_Robust_Reward_Modeling_via_Causal_Rubrics"},{"title":"Paper page - Robust Reward Modeling via Causal Rubrics","url":"https://huggingface.co/papers/2506.16507"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://openreview.net/pdf/e7492c345d3d76fb992f683c7e6a2725b2ab1002.pdf"},{"title":"Machine Learning Jun 2025","url":"https://arxiv.org/list/cs.LG/2025-06?skip=1750&show=25"}]

Based on the web search results, I found detailed information about both papers:

## CASSE: Cross-Correlated Style Features Evaluation (arXiv 2601.10809)

The work presents the first systematic study of cross-feature stylistic side effects. Style features such as friendly, helpful, or concise are widely used in prompts to steer the behavior of Large Language Model (LLM) conversational agents, yet their unintended side effects remain poorly understood.

The researchers conducted a comprehensive survey of 127 conversational agent papers from ACL Anthology and identified 12 frequently used style features, using controlled, synthetic dialogues across task-oriented and open domain settings to quantify how prompting for one style feature causally affects others via a pairwise LLM as a Judge evaluation framework. 

Their results reveal consistent and structured side effects, such as prompting for conciseness significantly reduces perceived expertise, and demonstrate that style features are deeply entangled rather than orthogonal. CASSE is a dataset that includes 12,200 synthetically generated messages annotated with 12 style features.

## Causal Rubrics Reward Model (arXiv 2506.16507)

The paper introduces Crome (Causally Robust Reward Modeling), a novel framework grounded in an explicit causal model designed to mitigate reward hacking. Reward models tend to latch on to superficial or spurious attributes, such as response length or formatting, mistaking these cues learned from correlations in training data for the true causal drivers of quality (e.g., factuality, relevance).

Crome employs synthetic targeted augmentations during training, including Causal Augmentations which are pairs that differ along specific causal attributes, produced without any knowledge of spurious factors, via answer interventions only along causal rubrics. Empirically, Crome significantly outperforms standard baselines on RewardBench, improving average accuracy by up to 5.4%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75ecfd7b-77c5-43b4-9f35-113309821951",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "c08c9e3c-1575-44e4-b821-d10ef084fe2a",
  "toolUseResult": {
    "query": "CASSE cross-correlated style features evaluation side effects arXiv 2601.10809 causal rubrics reward model arXiv 2506.16507",
    "results": [
      {
        "tool_use_id": "srvtoolu_017JBww8sjm8amc2FmLK3Pk7",
        "content": [
          {
            "title": "[2601.10809] A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://arxiv.org/abs/2601.10809"
          },
          {
            "title": "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://arxiv.org/html/2601.10809"
          },
          {
            "title": "Improved Style Transfer by Respecting Inter-layer Correlations",
            "url": "https://arxiv.org/pdf/1801.01933"
          },
          {
            "title": "Style is NOT a single variable: Case Studies for Cross-Style Language   Understanding",
            "url": "https://arxiv.org/pdf/1911.03663"
          },
          {
            "title": "Domain Generalization with Correlated Style Uncertainty",
            "url": "https://arxiv.org/pdf/2212.09950"
          },
          {
            "title": "Cross‐validated permutation feature importance considering correlation between features",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10989554/"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01HWQSjGs9hj7efgxjGfhEGj",
        "content": [
          {
            "title": "[2506.16507] Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/abs/2506.16507"
          },
          {
            "title": "[Quick Review] Robust Reward Modeling via Causal Rubrics",
            "url": "https://liner.com/review/robust-reward-modeling-via-causal-rubrics"
          },
          {
            "title": "arXiv:2506.16507v1 [cs.LG] 19 Jun 2025 2025-6-23",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://www.researchgate.net/publication/392918827_Robust_Reward_Modeling_via_Causal_Rubrics"
          },
          {
            "title": "Paper page - Robust Reward Modeling via Causal Rubrics",
            "url": "https://huggingface.co/papers/2506.16507"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://openreview.net/pdf/e7492c345d3d76fb992f683c7e6a2725b2ab1002.pdf"
          },
          {
            "title": "Machine Learning Jun 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-06?skip=1750&show=25"
          }
        ]
      },
      "Based on the web search results, I found detailed information about both papers:\n\n## CASSE: Cross-Correlated Style Features Evaluation (arXiv 2601.10809)\n\nThe work presents the first systematic study of cross-feature stylistic side effects. Style features such as friendly, helpful, or concise are widely used in prompts to steer the behavior of Large Language Model (LLM) conversational agents, yet their unintended side effects remain poorly understood.\n\nThe researchers conducted a comprehensive survey of 127 conversational agent papers from ACL Anthology and identified 12 frequently used style features, using controlled, synthetic dialogues across task-oriented and open domain settings to quantify how prompting for one style feature causally affects others via a pairwise LLM as a Judge evaluation framework. \n\nTheir results reveal consistent and structured side effects, such as prompting for conciseness significantly reduces perceived expertise, and demonstrate that style features are deeply entangled rather than orthogonal. CASSE is a dataset that includes 12,200 synthetically generated messages annotated with 12 style features.\n\n## Causal Rubrics Reward Model (arXiv 2506.16507)\n\nThe paper introduces Crome (Causally Robust Reward Modeling), a novel framework grounded in an explicit causal model designed to mitigate reward hacking. Reward models tend to latch on to superficial or spurious attributes, such as response length or formatting, mistaking these cues learned from correlations in training data for the true causal drivers of quality (e.g., factuality, relevance).\n\nCrome employs synthetic targeted augmentations during training, including Causal Augmentations which are pairs that differ along specific causal attributes, produced without any knowledge of spurious factors, via answer interventions only along causal rubrics. Empirically, Crome significantly outperforms standard baselines on RewardBench, improving average accuracy by up to 5.4%."
    ],
    "durationSeconds": 9.058505741999994,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "75ecfd7b-77c5-43b4-9f35-113309821951",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:21:44.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JaZYPgcA56TG3kT9m5sCWM`</summary>

```json
{
  "query": "\"black-box\" LLM judge debiasing causal inference post-hoc correction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c08c9e3c-1575-44e4-b821-d10ef084fe2a",
  "isSidechain": false,
  "requestId": "req_011CbDG2DqUmuzEb8xgV6i7S",
  "type": "assistant",
  "uuid": "0824efe5-b9af-4e9c-9740-c161c23568b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1VcYk3K9vkmNVjFUuZks5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 25921,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 25921,
          "cache_creation_input_tokens": 1190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1190
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

_source line 28 · 2026-05-20T05:21:51.720Z_

<details><summary>↩ Tool result · `toolu_01JaZYPgcA56TG3kT9m5sCWM`</summary>

```text
Web search results for query: ""black-box" LLM judge debiasing causal inference post-hoc correction 2025 2026"

Links: [{"title":"Efficient Inference for Noisy LLM-as-a-Judge Evaluation","url":"https://arxiv.org/pdf/2601.05420"},{"title":"LLM-as-a-Judge Scoring","url":"https://www.emergentmind.com/topics/llm-as-a-judge-scoring"},{"title":"LLM-Based Judge Model","url":"https://www.emergentmind.com/topics/llm-based-judge-model"},{"title":"Mitigating Spurious Correlations in LLMs via Causality-Aware Post-Training","url":"https://arxiv.org/pdf/2506.09433"},{"title":"BlackboxNLP 2025","url":"https://blackboxnlp.github.io/2025/accepted_papers/"},{"title":"Information Gain-Guided Causal Intervention for Autonomous Debiasing Large Language Models","url":"https://arxiv.org/pdf/2504.12898"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"}]

I found several relevant results on this topic. Here's a summary of recent research on black-box LLM judges, debiasing, causal inference, and post-hoc correction methods from 2025-2026:

## Key Findings:

**Debiasing LLM-as-a-Judge Systems:**
Methods for debiasing are not standardized or fully effective, particularly for implicit and subtle biases, though frameworks such as CALM provide systematic bias measurement.

**Post-hoc Correction Approaches:**
Quantitative post-hoc models freeze the base judge, embed rationale, and train lightweight GLMs (least-squares, multinomial, Bradley-Terry-Luce) to better align judge outputs with human scores using a small labeled dataset.

**Causal Analysis for Bias Detection:**
Existing mitigation approaches typically treat models as black boxes and apply static interventions that do not persist as the model evolves; using paired counterfactual input, causal tracking techniques can localize internal features that are causally responsible for biased behavior.

**Measurement Error Correction:**
Lee et al. [2025] provides a recipe for applying measurement-error corrections to LLM-as-a-judge settings, along with approaches like PPI (Prediction-Powered Inference) and Rogan-Gladen estimators.

**Open Challenges:**
Causal origins of scoring bias, integration of multi-modal judgment, and transitivity/consistency guarantees for pairwise and listwise evaluation systems remain open.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0824efe5-b9af-4e9c-9740-c161c23568b1",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "5aa5e07c-c1eb-4ac8-86b1-d2ddb05fbe41",
  "toolUseResult": {
    "query": "\"black-box\" LLM judge debiasing causal inference post-hoc correction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HGaaL2sfd6KzV2GZkivH8k",
        "content": [
          {
            "title": "Efficient Inference for Noisy LLM-as-a-Judge Evaluation",
            "url": "https://arxiv.org/pdf/2601.05420"
          },
          {
            "title": "LLM-as-a-Judge Scoring",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-scoring"
          },
          {
            "title": "LLM-Based Judge Model",
            "url": "https://www.emergentmind.com/topics/llm-based-judge-model"
          },
          {
            "title": "Mitigating Spurious Correlations in LLMs via Causality-Aware Post-Training",
            "url": "https://arxiv.org/pdf/2506.09433"
          },
          {
            "title": "BlackboxNLP 2025",
            "url": "https://blackboxnlp.github.io/2025/accepted_papers/"
          },
          {
            "title": "Information Gain-Guided Causal Intervention for Autonomous Debiasing Large Language Models",
            "url": "https://arxiv.org/pdf/2504.12898"
          },
          {
            "title": "(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"
          }
        ]
      },
      "I found several relevant results on this topic. Here's a summary of recent research on black-box LLM judges, debiasing, causal inference, and post-hoc correction methods from 2025-2026:\n\n## Key Findings:\n\n**Debiasing LLM-as-a-Judge Systems:**\nMethods for debiasing are not standardized or fully effective, particularly for implicit and subtle biases, though frameworks such as CALM provide systematic bias measurement.\n\n**Post-hoc Correction Approaches:**\nQuantitative post-hoc models freeze the base judge, embed rationale, and train lightweight GLMs (least-squares, multinomial, Bradley-Terry-Luce) to better align judge outputs with human scores using a small labeled dataset.\n\n**Causal Analysis for Bias Detection:**\nExisting mitigation approaches typically treat models as black boxes and apply static interventions that do not persist as the model evolves; using paired counterfactual input, causal tracking techniques can localize internal features that are causally responsible for biased behavior.\n\n**Measurement Error Correction:**\nLee et al. [2025] provides a recipe for applying measurement-error corrections to LLM-as-a-judge settings, along with approaches like PPI (Prediction-Powered Inference) and Rogan-Gladen estimators.\n\n**Open Challenges:**\nCausal origins of scoring bias, integration of multi-modal judgment, and transitivity/consistency guarantees for pairwise and listwise evaluation systems remain open."
    ],
    "durationSeconds": 7.665363348999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0824efe5-b9af-4e9c-9740-c161c23568b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T05:21:51.723Z_

```json
{
  "parentUuid": "5aa5e07c-c1eb-4ac8-86b1-d2ddb05fbe41",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "77630685-b68f-4628-9a7f-de5651583e72",
  "timestamp": "2026-05-20T05:21:51.723Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T05:21:56.419Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013pXssbLX2WKupntgBvVaZJ`</summary>

```json
{
  "query": "CMBE simultaneous multi-bias causal effect estimation arXiv 2505.16522 CRM counterfactual invariance reward arXiv 2501.09620"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77630685-b68f-4628-9a7f-de5651583e72",
  "isSidechain": false,
  "requestId": "req_011CbDG2yzpJ6HKkvyGiDeBp",
  "type": "assistant",
  "uuid": "f3c03b72-8b05-4534-a8b0-fa210dd393fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJ6U6jKhMXaKfnSCdRLBmX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 27111,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 27111,
          "cache_creation_input_tokens": 909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 909
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

_source line 31 · 2026-05-20T05:22:03.110Z_

<details><summary>↩ Tool result · `toolu_013pXssbLX2WKupntgBvVaZJ`</summary>

```text
Web search results for query: "CMBE simultaneous multi-bias causal effect estimation arXiv 2505.16522 CRM counterfactual invariance reward arXiv 2501.09620"

Links: [{"title":"[2505.16522] Benchmarking and Pushing the Multi-Bias Elimination Boundary of LLMs via Causal Effect Estimation-guided Debiasing","url":"https://arxiv.org/abs/2505.16522"},{"title":"Benchmarking and Pushing the Multi-Bias Elimination Boundary of LLMs via Causal Effect Estimation-guided Debiasing","url":"https://arxiv.org/html/2505.16522"},{"title":"Benchmarking and Pushing the Multi-Bias Elimination ...","url":"https://arxiv.org/pdf/2505.16522"},{"title":"Benchmarking and Pushing the Multi-Bias Elimination Boundary ...","url":"https://www.arxiv.org/pdf/2505.16522v1"},{"title":"A roadmap for systematic identification and analysis of multiple biases in causal inference","url":"https://arxiv.org/pdf/2504.08263"},{"title":"Estimating the effect of joint interventions from observational data in   sparse high-dimensional settings","url":"https://arxiv.org/pdf/1407.2451"},{"title":"Disentangled Latent Representation Learning for Tackling the Confounding   M-Bias Problem in Causal Inference","url":"https://arxiv.org/pdf/2312.05404"},{"title":"Multiple Treatments Causal Effects Estimation with Task Embeddings and Balanced Representation Learning","url":"https://arxiv.org/html/2511.09814v1"}]

Links: [{"title":"arXiv:2501.09620v2 [cs.LG] 29 May 2025","url":"https://arxiv.org/pdf/2501.09620"},{"title":"[Literature Review] Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://www.themoonlight.io/en/review/beyond-reward-hacking-causal-rewards-for-large-language-model-alignment"},{"title":"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/html/2501.09620v1"},{"title":"[2501.09620] Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/abs/2501.09620"},{"title":"Paper page - Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://huggingface.co/papers/2501.09620"},{"title":"arXiv:2506.16507v1 [cs.LG] 19 Jun 2025 2025-6-23","url":"https://arxiv.org/pdf/2506.16507"}]

Based on the search results, here's information about both papers:

## CMBE (arXiv 2505.16522)

CMBE is a causal effect estimation-guided multi-bias elimination method for large language models. The method first estimates the causal effect of multiple types of biases simultaneously, and subsequently eliminates the causal effect of biases from the total causal effect exerted by both the semantic information and biases during inference.

The paper proposes a multi-bias benchmark where each piece of data contains five types of biases. Experimental results show that CMBE can effectively eliminate multiple types of bias simultaneously to enhance the generalizability of LLMs.

## CRM (arXiv 2501.09620)

By leveraging causal inference techniques, researchers developed a causal reward model (CRM) that is robust to spurious correlations and captures the true causal relationship of responses on human preferences. 

Central to the method is the concept of counterfactual invariance, which ensures that the reward model's predictions remain consistent under interventions on irrelevant aspects of the input, thereby reducing the irreducible error caused by spurious correlations. The approach addresses biases such as length bias, sycophancy, conceptual bias, and discrimination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3c03b72-8b05-4534-a8b0-fa210dd393fc",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "ae91bae3-b0e7-4927-82ef-b3608ca8ec4c",
  "toolUseResult": {
    "query": "CMBE simultaneous multi-bias causal effect estimation arXiv 2505.16522 CRM counterfactual invariance reward arXiv 2501.09620",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U7nmcHA7FPB6rq96SVQQdt",
        "content": [
          {
            "title": "[2505.16522] Benchmarking and Pushing the Multi-Bias Elimination Boundary of LLMs via Causal Effect Estimation-guided Debiasing",
            "url": "https://arxiv.org/abs/2505.16522"
          },
          {
            "title": "Benchmarking and Pushing the Multi-Bias Elimination Boundary of LLMs via Causal Effect Estimation-guided Debiasing",
            "url": "https://arxiv.org/html/2505.16522"
          },
          {
            "title": "Benchmarking and Pushing the Multi-Bias Elimination ...",
            "url": "https://arxiv.org/pdf/2505.16522"
          },
          {
            "title": "Benchmarking and Pushing the Multi-Bias Elimination Boundary ...",
            "url": "https://www.arxiv.org/pdf/2505.16522v1"
          },
          {
            "title": "A roadmap for systematic identification and analysis of multiple biases in causal inference",
            "url": "https://arxiv.org/pdf/2504.08263"
          },
          {
            "title": "Estimating the effect of joint interventions from observational data in   sparse high-dimensional settings",
            "url": "https://arxiv.org/pdf/1407.2451"
          },
          {
            "title": "Disentangled Latent Representation Learning for Tackling the Confounding   M-Bias Problem in Causal Inference",
            "url": "https://arxiv.org/pdf/2312.05404"
          },
          {
            "title": "Multiple Treatments Causal Effects Estimation with Task Embeddings and Balanced Representation Learning",
            "url": "https://arxiv.org/html/2511.09814v1"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01StBuhzAeyh4Q4oEdR2Yvcq",
        "content": [
          {
            "title": "arXiv:2501.09620v2 [cs.LG] 29 May 2025",
            "url": "https://arxiv.org/pdf/2501.09620"
          },
          {
            "title": "[Literature Review] Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://www.themoonlight.io/en/review/beyond-reward-hacking-causal-rewards-for-large-language-model-alignment"
          },
          {
            "title": "Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/html/2501.09620v1"
          },
          {
            "title": "[2501.09620] Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/abs/2501.09620"
          },
          {
            "title": "Paper page - Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://huggingface.co/papers/2501.09620"
          },
          {
            "title": "arXiv:2506.16507v1 [cs.LG] 19 Jun 2025 2025-6-23",
            "url": "https://arxiv.org/pdf/2506.16507"
          }
        ]
      },
      "Based on the search results, here's information about both papers:\n\n## CMBE (arXiv 2505.16522)\n\nCMBE is a causal effect estimation-guided multi-bias elimination method for large language models. The method first estimates the causal effect of multiple types of biases simultaneously, and subsequently eliminates the causal effect of biases from the total causal effect exerted by both the semantic information and biases during inference.\n\nThe paper proposes a multi-bias benchmark where each piece of data contains five types of biases. Experimental results show that CMBE can effectively eliminate multiple types of bias simultaneously to enhance the generalizability of LLMs.\n\n## CRM (arXiv 2501.09620)\n\nBy leveraging causal inference techniques, researchers developed a causal reward model (CRM) that is robust to spurious correlations and captures the true causal relationship of responses on human preferences. \n\nCentral to the method is the concept of counterfactual invariance, which ensures that the reward model's predictions remain consistent under interventions on irrelevant aspects of the input, thereby reducing the irreducible error caused by spurious correlations. The approach addresses biases such as length bias, sycophancy, conceptual bias, and discrimination."
    ],
    "durationSeconds": 6.687090379999995,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "f3c03b72-8b05-4534-a8b0-fa210dd393fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Causal Style Decomposition for Debiasing Black-Box LLM Judges  ### 1. Problem and Motivation  LLM-as-a-Judge pipelines are increasingly used for automated evaluation, but suffer from systematic sty…",
  "leafUuid": "ae91bae3-b0e7-4927-82ef-b3608ca8ec4c",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Causal style decomposition for debiasing LLM judges",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

### Tool call

_source line 34 · 2026-05-20T05:22:06.357Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013uYG36C6F7vRgGgtfp7oAh`</summary>

```json
{
  "query": "UDA unsupervised debiasing alignment pairwise LLM judge 2025 post-hoc reward calibration locally weighted regression arXiv 2409.17407"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae91bae3-b0e7-4927-82ef-b3608ca8ec4c",
  "isSidechain": false,
  "requestId": "req_011CbDG3ptQhGeDr59zB5jKY",
  "type": "assistant",
  "uuid": "feff4ee6-e642-4092-865f-e44f699ffdd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017b87YeLM4S7EJx8rHBFMQ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 28020,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 28020,
          "cache_creation_input_tokens": 1120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1120
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

_source line 35 · 2026-05-20T05:22:12.682Z_

<details><summary>↩ Tool result · `toolu_013uYG36C6F7vRgGgtfp7oAh`</summary>

```text
Web search results for query: "UDA unsupervised debiasing alignment pairwise LLM judge 2025 post-hoc reward calibration locally weighted regression arXiv 2409.17407"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"Privileged Pairwise Judges","url":"https://www.emergentmind.com/topics/privileged-pairwise-judges"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"}]

Based on the search results, here's what I found:

UDA (Unsupervised Debiasing Alignment) is a framework designed to address preference bias in pairwise evaluation of Large Language Models, reducing inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities.

UDA operates in a fully unsupervised manner, guided solely by minimizing the dispersion among the Elo trajectories of all judges, forcing an alignment towards a collective consensus that serves as an unsupervised proxy for more stable and reproducible evaluation.

Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.

**Note:** The search results indicate the paper is arXiv:2508.09724 (published August 2025), not 2409.17407 as mentioned in your query. The framework addresses preference bias through consensus-based debiasing rather than the specific post-hoc reward calibration and locally weighted regression methods you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feff4ee6-e642-4092-865f-e44f699ffdd3",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "3bdbca46-6673-4ac3-bc66-c599242b0abb",
  "toolUseResult": {
    "query": "UDA unsupervised debiasing alignment pairwise LLM judge 2025 post-hoc reward calibration locally weighted regression arXiv 2409.17407",
    "results": [
      {
        "tool_use_id": "srvtoolu_011ymRJsjt2aF91SRsF9geAM",
        "content": [
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          },
          {
            "title": "[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788"
          },
          {
            "title": "Privileged Pairwise Judges",
            "url": "https://www.emergentmind.com/topics/privileged-pairwise-judges"
          },
          {
            "title": "(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nUDA (Unsupervised Debiasing Alignment) is a framework designed to address preference bias in pairwise evaluation of Large Language Models, reducing inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities.\n\nUDA operates in a fully unsupervised manner, guided solely by minimizing the dispersion among the Elo trajectories of all judges, forcing an alignment towards a collective consensus that serves as an unsupervised proxy for more stable and reproducible evaluation.\n\nExperiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.\n\n**Note:** The search results indicate the paper is arXiv:2508.09724 (published August 2025), not 2409.17407 as mentioned in your query. The framework addresses preference bias through consensus-based debiasing rather than the specific post-hoc reward calibration and locally weighted regression methods you mentioned in your query."
    ],
    "durationSeconds": 6.320739877,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "feff4ee6-e642-4092-865f-e44f699ffdd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T05:22:16.212Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SDtG7RubMdagxzoCxL4iEV`</summary>

```json
{
  "query": "FairJudge SFT DPO GRPO retrain LLM judge debiasing arXiv 2602.06625 bias-bounded evaluation BBE arXiv 2603.05485"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bdbca46-6673-4ac3-bc66-c599242b0abb",
  "isSidechain": false,
  "requestId": "req_011CbDG4XbsUEkqFJS5mo57v",
  "type": "assistant",
  "uuid": "bdba9845-692e-47aa-828a-b508790fb260",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vL4VzTywxSBXXJyeH8Wiy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 29140,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 29140,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

_source line 37 · 2026-05-20T05:22:26.294Z_

<details><summary>↩ Tool result · `toolu_01SDtG7RubMdagxzoCxL4iEV`</summary>

```text
Web search results for query: "FairJudge SFT DPO GRPO retrain LLM judge debiasing arXiv 2602.06625 bias-bounded evaluation BBE arXiv 2603.05485"

Links: [{"title":"[2602.06625] FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/abs/2602.06625"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/pdf/2602.06625"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/html/2602.06625"},{"title":"FairJudge: MLLM Judging for Social-Attributes and Prompt–Image Alignment","url":"https://arxiv.org/html/2510.22827"},{"title":"On the Shelf Life of Fine-Tuned LLM Judges: Future Proofing, Backward Compatibility, and Question Generalization","url":"https://arxiv.org/pdf/2509.23542"}]

Links: [{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/html/2603.05485"},{"title":"[2603.05485] Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/abs/2603.05485"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/pdf/2603.05485"},{"title":"Evaluation adjustment factoring for bias","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12555077"},{"title":"Bias in Evaluation Processes: An Optimization-Based Model","url":"https://arxiv.org/pdf/2310.17489"}]

Based on the search results, here's information about both papers:

## FairJudge (arXiv 2602.06625)

Existing LLM-as-a-Judge systems suffer from three fundamental limitations: limited adaptivity to task- and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes (e.g., pointwise versus pairwise).

FairJudge is an adaptive, debiased, and consistent LLM-as-a-Judge that models judging behavior itself as a learnable and regularized policy. The approach constructs a high-information-density judging dataset that explicitly injects supervision signals aligned with evaluation behavior, and adopts a curriculum-style SFT-DPO-GRPO training paradigm that progressively aligns rubric adherence, bias mitigation, and cross-mode consistency, while avoiding catastrophic forgetting.

## Bias-Bounded Evaluation (arXiv 2603.05485)

Although LLM judges continue to improve, the literature has yet to introduce systems capable of enforcing standards with strong guarantees, particularly when bias vectors are unknown or adversarially discovered. To remedy this issue, the paper proposes average bias-boundedness (A-BB), an algorithmic framework which formally guarantees reductions of harm/impact as a result of any measurable bias in an LLM judge.

BBE (Bias-Bounded Evaluation) measures how sensitive an LLM judge is to biases and then renders that sensitivity in the judgment scores, injecting calibrated Gaussian noise to the judge's scores to mitigate the effects of the bias using the A-BB mechanism.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdba9845-692e-47aa-828a-b508790fb260",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "34ce91d1-dd48-4180-8e85-f583b7910d9b",
  "toolUseResult": {
    "query": "FairJudge SFT DPO GRPO retrain LLM judge debiasing arXiv 2602.06625 bias-bounded evaluation BBE arXiv 2603.05485",
    "results": [
      {
        "tool_use_id": "srvtoolu_011gJ7eb5fTmx1F8zeDHSaxD",
        "content": [
          {
            "title": "[2602.06625] FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2602.06625"
          },
          {
            "title": "FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2602.06625"
          },
          {
            "title": "FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2602.06625"
          },
          {
            "title": "FairJudge: MLLM Judging for Social-Attributes and Prompt–Image Alignment",
            "url": "https://arxiv.org/html/2510.22827"
          },
          {
            "title": "On the Shelf Life of Fine-Tuned LLM Judges: Future Proofing, Backward Compatibility, and Question Generalization",
            "url": "https://arxiv.org/pdf/2509.23542"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01XnKuZ4H4T2XC1VUcdFBZPr",
        "content": [
          {
            "title": "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/html/2603.05485"
          },
          {
            "title": "[2603.05485] Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/abs/2603.05485"
          },
          {
            "title": "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/pdf/2603.05485"
          },
          {
            "title": "Evaluation adjustment factoring for bias",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12555077"
          },
          {
            "title": "Bias in Evaluation Processes: An Optimization-Based Model",
            "url": "https://arxiv.org/pdf/2310.17489"
          }
        ]
      },
      "Based on the search results, here's information about both papers:\n\n## FairJudge (arXiv 2602.06625)\n\nExisting LLM-as-a-Judge systems suffer from three fundamental limitations: limited adaptivity to task- and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes (e.g., pointwise versus pairwise).\n\nFairJudge is an adaptive, debiased, and consistent LLM-as-a-Judge that models judging behavior itself as a learnable and regularized policy. The approach constructs a high-information-density judging dataset that explicitly injects supervision signals aligned with evaluation behavior, and adopts a curriculum-style SFT-DPO-GRPO training paradigm that progressively aligns rubric adherence, bias mitigation, and cross-mode consistency, while avoiding catastrophic forgetting.\n\n## Bias-Bounded Evaluation (arXiv 2603.05485)\n\nAlthough LLM judges continue to improve, the literature has yet to introduce systems capable of enforcing standards with strong guarantees, particularly when bias vectors are unknown or adversarially discovered. To remedy this issue, the paper proposes average bias-boundedness (A-BB), an algorithmic framework which formally guarantees reductions of harm/impact as a result of any measurable bias in an LLM judge.\n\nBBE (Bias-Bounded Evaluation) measures how sensitive an LLM judge is to biases and then renders that sensitivity in the judgment scores, injecting calibrated Gaussian noise to the judge's scores to mitigate the effects of the bias using the A-BB mechanism."
    ],
    "durationSeconds": 10.076823479999991,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "bdba9845-692e-47aa-828a-b508790fb260",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T05:22:29.503Z_

Now let me do one final search to check if there's any very recent work that directly overlaps with CSD's core idea of using DML for black-box judge debiasing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34ce91d1-dd48-4180-8e85-f583b7910d9b",
  "isSidechain": false,
  "requestId": "req_011CbDG5XmpX7N9UePjHehu1",
  "type": "assistant",
  "uuid": "18029330-5c0f-49ab-9094-6b62dd0a9f61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4vfTmXDUGGG4JHuXCPKsF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 29934,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 29934,
          "cache_creation_input_tokens": 1057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1057
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

_source line 39 · 2026-05-20T05:22:30.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PVTPLKHvb7cu8yaiCMPzgF`</summary>

```json
{
  "query": "double machine learning semiparametric debiasing LLM evaluation style confounding black-box 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18029330-5c0f-49ab-9094-6b62dd0a9f61",
  "isSidechain": false,
  "requestId": "req_011CbDG5XmpX7N9UePjHehu1",
  "type": "assistant",
  "uuid": "90f994b1-ed77-485d-8acc-fc2fbd3b3b19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K4vfTmXDUGGG4JHuXCPKsF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 29934,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 29934,
          "cache_creation_input_tokens": 1057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1057
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

_source line 40 · 2026-05-20T05:22:36.926Z_

<details><summary>↩ Tool result · `toolu_01PVTPLKHvb7cu8yaiCMPzgF`</summary>

```text
Web search results for query: "double machine learning semiparametric debiasing LLM evaluation style confounding black-box 2025 2026"

Links: [{"title":"On Doubly Robust Inference for Double Machine Learning in Semiparametric   Regression","url":"https://arxiv.org/pdf/2107.06124"},{"title":"Estimating Causal Effects with Double Machine Learning - A Method Evaluation","url":"https://arxiv.org/html/2403.14385v1"},{"title":"Nonparametric LLM Evaluation from Preference Data","url":"https://arxiv.org/pdf/2601.21816"},{"title":"Double/debiased machine learning for treatment and structural parameters | Request PDF","url":"https://www.researchgate.net/publication/318162496_Doubledebiased_machine_learning_for_treatment_and_structural_parameters"},{"title":"On Doubly Robust Inference for Double Machine Learning in Semiparametric Regression","url":"https://www.jmlr.org/papers/v25/22-1233.html"},{"title":"Estimating Causal Effects with Double Machine Learning -- A Method   Evaluation","url":"https://arxiv.org/pdf/2403.14385"}]

I found several relevant research papers on your search topic. Here are the key results:

**Double Machine Learning and Semiparametric Debiasing:**

Double/debiased machine learning (DML) is a prominent method that allows researchers to use flexible ML methods to adequately adjust for observed confounding variables. Progress has been made via proposals like targeted minimum loss estimation (TMLE) and double machine learning, which rely on learning the conditional mean of both the outcome and exposure.

Exposure effect estimators that rely on machine learning predictions are generally subject to so-called plug-in bias, which can render naive p-values and confidence intervals invalid.

**LLM Evaluation Application:**

A particularly recent and relevant paper (2026) applies these concepts: Building on debiased machine learning (DML), statistically efficient estimators can be derived with confidence intervals that remain valid when preference probabilities are estimated with black-box machine learning methods. This approach can incorporate external judges such as LLM-as-judge, or other pre-trained LLM evaluators.

**Key Advantages:**

The application of suitably flexible machine learning algorithms within DML improves the adjustment for various nonlinear confounding relationships, enabling a departure from traditional functional form assumptions typically necessary in causal effect estimation.

The most recent paper directly addressing LLM evaluation with these debiasing techniques is "Nonparametric LLM Evaluation from Preference Data" (2025/2026), which extends classical DML methods to the domain of LLM ranking and evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90f994b1-ed77-485d-8acc-fc2fbd3b3b19",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "317629df-9ebe-482f-a761-5f498071c6f5",
  "toolUseResult": {
    "query": "double machine learning semiparametric debiasing LLM evaluation style confounding black-box 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FHkGiQgRx2Zgvei59d8v6s",
        "content": [
          {
            "title": "On Doubly Robust Inference for Double Machine Learning in Semiparametric   Regression",
            "url": "https://arxiv.org/pdf/2107.06124"
          },
          {
            "title": "Estimating Causal Effects with Double Machine Learning - A Method Evaluation",
            "url": "https://arxiv.org/html/2403.14385v1"
          },
          {
            "title": "Nonparametric LLM Evaluation from Preference Data",
            "url": "https://arxiv.org/pdf/2601.21816"
          },
          {
            "title": "Double/debiased machine learning for treatment and structural parameters | Request PDF",
            "url": "https://www.researchgate.net/publication/318162496_Doubledebiased_machine_learning_for_treatment_and_structural_parameters"
          },
          {
            "title": "On Doubly Robust Inference for Double Machine Learning in Semiparametric Regression",
            "url": "https://www.jmlr.org/papers/v25/22-1233.html"
          },
          {
            "title": "Estimating Causal Effects with Double Machine Learning -- A Method   Evaluation",
            "url": "https://arxiv.org/pdf/2403.14385"
          }
        ]
      },
      "I found several relevant research papers on your search topic. Here are the key results:\n\n**Double Machine Learning and Semiparametric Debiasing:**\n\nDouble/debiased machine learning (DML) is a prominent method that allows researchers to use flexible ML methods to adequately adjust for observed confounding variables. Progress has been made via proposals like targeted minimum loss estimation (TMLE) and double machine learning, which rely on learning the conditional mean of both the outcome and exposure.\n\nExposure effect estimators that rely on machine learning predictions are generally subject to so-called plug-in bias, which can render naive p-values and confidence intervals invalid.\n\n**LLM Evaluation Application:**\n\nA particularly recent and relevant paper (2026) applies these concepts: Building on debiased machine learning (DML), statistically efficient estimators can be derived with confidence intervals that remain valid when preference probabilities are estimated with black-box machine learning methods. This approach can incorporate external judges such as LLM-as-judge, or other pre-trained LLM evaluators.\n\n**Key Advantages:**\n\nThe application of suitably flexible machine learning algorithms within DML improves the adjustment for various nonlinear confounding relationships, enabling a departure from traditional functional form assumptions typically necessary in causal effect estimation.\n\nThe most recent paper directly addressing LLM evaluation with these debiasing techniques is \"Nonparametric LLM Evaluation from Preference Data\" (2025/2026), which extends classical DML methods to the domain of LLM ranking and evaluation."
    ],
    "durationSeconds": 6.45831730000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "90f994b1-ed77-485d-8acc-fc2fbd3b3b19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T05:22:39.761Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014DFZ5hK6AUhMuiCM3wH5SD`</summary>

```json
{
  "query": "\"legitimacy-aware\" OR \"legitimate style\" OR \"style-quality association\" debiasing evaluation LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "317629df-9ebe-482f-a761-5f498071c6f5",
  "isSidechain": false,
  "requestId": "req_011CbDG6KdbgFTB2M8FsXEfW",
  "type": "assistant",
  "uuid": "6073b0eb-5a4e-4528-8b33-e290f24bec35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHTGJ7H9v3khSLGpUeJYkV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 30991,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 789,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 30991,
          "cache_creation_input_tokens": 789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 789
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

_source line 42 · 2026-05-20T05:22:46.954Z_

<details><summary>↩ Tool result · `toolu_014DFZ5hK6AUhMuiCM3wH5SD`</summary>

```text
Web search results for query: ""legitimacy-aware" OR "legitimate style" OR "style-quality association" debiasing evaluation LLM 2025 2026"

Links: [{"title":"Could you be wrong: Debiasing LLMs using a metacognitive prompt for improving human decision making","url":"https://arxiv.org/pdf/2507.10124"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"When Style Breaks Safety: Defending LLMs Against Superficial Style Alignment","url":"https://arxiv.org/pdf/2506.07452"},{"title":"Towards trustworthy LLMs: a review on debiasing and dehallucinating in large language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-024-10896-y"},{"title":"LLM Bias Detection and Mitigation through the Lens of ...","url":"https://aclanthology.org/2025.emnlp-main.76.pdf"},{"title":"LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline","url":"https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"}]

Based on the search results, I found relevant research on debiasing evaluation in LLMs from 2025-2026. Here are the key findings:

## LLM Evaluation Bias and Debiasing (2025-2026)

LLM judges are vulnerable to systematic biases, with position bias where evaluators disproportionately prefer outputs appearing in a specific position, regardless of content quality and verbosity bias where longer responses receive higher ratings even when their quality is similar to briefer alternatives.

Recent 2025-2026 research has documented these evaluation problems extensively. Studies published in 2025 and early 2026 have systematically documented where LLM judges fail, why they fail, and how often. 

On debiasing approaches, SFT establishes the base judge behavior; DPO targets non-semantic biases, including position, format, and length; GRPO enforces consistency across scoring modes.

Additionally, research on style-related issues shows that style patterns in malicious queries may undermine safety-aligned LLMs, as the superficial alignment hypothesis posits that alignment tuning may lead models to imitate style patterns without internalizing deeper safety principles.

While the exact terms "legitimacy-aware" or "legitimate style" don't appear in these results, the research does address how LLM evaluation can be biased by surface-level features like format and style rather than actual quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6073b0eb-5a4e-4528-8b33-e290f24bec35",
  "isSidechain": false,
  "promptId": "30ddb7af-6d60-44e6-a56e-d3d1dd68d8b6",
  "type": "user",
  "uuid": "0e6d348e-287d-41d5-b555-b1fd355e763c",
  "toolUseResult": {
    "query": "\"legitimacy-aware\" OR \"legitimate style\" OR \"style-quality association\" debiasing evaluation LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uo8DTViv9Sf522rSzN3rAB",
        "content": [
          {
            "title": "Could you be wrong: Debiasing LLMs using a metacognitive prompt for improving human decision making",
            "url": "https://arxiv.org/pdf/2507.10124"
          },
          {
            "title": "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2509.26072"
          },
          {
            "title": "When Style Breaks Safety: Defending LLMs Against Superficial Style Alignment",
            "url": "https://arxiv.org/pdf/2506.07452"
          },
          {
            "title": "Towards trustworthy LLMs: a review on debiasing and dehallucinating in large language models | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-024-10896-y"
          },
          {
            "title": "LLM Bias Detection and Mitigation through the Lens of ...",
            "url": "https://aclanthology.org/2025.emnlp-main.76.pdf"
          },
          {
            "title": "LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline",
            "url": "https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"
          }
        ]
      },
      "Based on the search results, I found relevant research on debiasing evaluation in LLMs from 2025-2026. Here are the key findings:\n\n## LLM Evaluation Bias and Debiasing (2025-2026)\n\nLLM judges are vulnerable to systematic biases, with position bias where evaluators disproportionately prefer outputs appearing in a specific position, regardless of content quality and verbosity bias where longer responses receive higher ratings even when their quality is similar to briefer alternatives.\n\nRecent 2025-2026 research has documented these evaluation problems extensively. Studies published in 2025 and early 2026 have systematically documented where LLM judges fail, why they fail, and how often. \n\nOn debiasing approaches, SFT establishes the base judge behavior; DPO targets non-semantic biases, including position, format, and length; GRPO enforces consistency across scoring modes.\n\nAdditionally, research on style-related issues shows that style patterns in malicious queries may undermine safety-aligned LLMs, as the superficial alignment hypothesis posits that alignment tuning may lead models to imitate style patterns without internalizing deeper safety principles.\n\nWhile the exact terms \"legitimacy-aware\" or \"legitimate style\" don't appear in these results, the research does address how LLM evaluation can be biased by surface-level features like format and style rather than actual quality."
    ],
    "durationSeconds": 7.181317416999984,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6073b0eb-5a4e-4528-8b33-e290f24bec35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T05:23:55.582Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the landscape. Let me synthesize my findings and analyze this proposal as the 发掘 agent.

Key observations from my research:

1. **The gap is real**: No existing work combines (a) black-box applicability, (b) multi-dimensional causal debiasing, and (c) legitimacy-aware correction. This is verified by my searches.

2. **The DML application is novel in this context**: DML has been used extensively in econometrics and is starting to appear in NLP (Nonparametric LLM Evaluation from Preference Data), but applying it specifically as a second layer on top of counterfactual interventions for judge debiasing is genuinely novel.


3. **RATE is the natural comparison point**: The proposal positions itself well against RATE—achieving similar debiasing at a fraction of the computational cost while offering score correction rather than just explainability.

4. **The legitimacy-aware correction mechanism** introduces a meaningful conceptual advance by addressing the style entanglement issues that CASSE identified, allowing for more nuanced control over which biases get corrected.

5. **ISE as a diagnostic metric** could become a useful standardized tool for measuring debiasing effectiveness across different contexts.

The main question is whether there's a simpler alternative—multivariate observational regression is the obvious candidate, and I'm glad the proposal includes it as a baseline to demonstrate why the causal approach adds value.

The critical tension is whether the counterfactual identification plus DML actually delivers enough improvement over plain observational regression to justify the added complexity, or if Multi-Reg performs nearly as well and undermines the whole framework. The proposal claims observational regression conflates genuine quality signals with spurious confounding, but that's an empirical claim that needs validation.

The core assumptions also matter: the content preservation thresholds (BERTScore ≥ 0.92 and NLI ≥ 0.95) are supposed to keep the first layer clean, with DML handling residual leakage in the second layer. But if content leakage is systematic rather than random, DML might not fully correct it. Similarly, reducing style to three dimensions—formality, verbosity, formatting—is a simplification that could miss important variation, though the proposal does acknowledge this limitation.

There are several angles that feel underdeveloped. The ISE metric itself could be positioned as a community standard for bias reporting, similar to how FID became standard for image generation—that's potentially a bigger contribution than just the debiasing method. The dual-layer identification strategy (counterfactuals plus DML) is actually a general methodology applicable to any setting with imperfect interventions, not just style debiasing, and that generalizability deserves more emphasis. And the connection to RLHF and DPO pipelines is mentioned only in passing, but given the Preference Leakage work, the cascading benefit of debiasing judges upstream is a strong significance argument that should be developed more fully.

The legitimacy-aware correction with the α parameter is a genuine conceptual advance—most debiasing assumes style effects are purely spurious, but in technical writing, formatting actually contributes to quality. This connects to fairness literature's distinction between legitimate and illegitimate decision factors, and the framing could be sharper there.

On the gaps side, there's UDA from arXiv:2508.09724, an unsupervised debiasing method for pairwise LLM judges that reduces disagreement—that's a relevant baseline missing from the proposal. And CMBE is mentioned but only positioned as a white-box method, though there's more nuance there.

CMBE's simultaneous multi-bias causal effect estimation is conceptually similar to what CSD does, so the differentiation needs to be clearer. There's also the Nonparametric LLM Evaluation paper using DML-style debiasing for ranking from preference data—it's a related but distinct application, so the proposal should acknowledge and distinguish itself from it rather than ignore it.

The current framing about providing principled multi-dimensional debiasing for black-box judges is solid, but it misses the deeper methodological contribution: imperfect counterfactual interventions alone aren't enough (as RATE demonstrated), yet instead of relying on expensive double-rewrites to cancel bias, semiparametric statistics through DML can absorb the bias more efficiently with stronger theoretical guarantees. That's the real insight worth emphasizing.

Overall, this proposal is remarkably polished—it has a clear problem statement, thorough related work, well-motivated methodology with solid theory, and thoughtfully designed experiments.

Looking at where I can genuinely strengthen this: the dual-layer identification strategy is the most novel contribution, but I'm framing it as a solution to imperfect counterfactuals rather than positioning it as a broader methodological insight about bringing semiparametric efficiency theory into LLM evaluation. The ISE metric deserves more development as its own contribution with the FID analogy. I should also incorporate recent work like UDA and the nonparametric LLM evaluation paper, and connect the legitimacy-aware correction to fairness literature concepts like equalized odds versus demographic parity to give it more theoretical grounding.

This is a solid proposal overall, though I want to sharpen the novelty framing and strengthen some of the theoretical positioning. But I'm realizing I need to think more carefully about the trivial alternative problem. The obvious baseline is just using multivariate observational regression on automated style features—essentially extending what LC-AlpacaEval does for length to multiple dimensions. I'm including this as a baseline, which is good, but the key question is what theoretical argument justifies why CSD should outperform it. The core claim is that observational regression suffers from omitted variable bias and conflates correlation with causation—a high-quality response might legitimately be longer because it's more thorough, and naive regression would incorrectly attribute part of that length effect to bias and over-correct. But I need to think through whether CSD actually solves this problem or just shifts it.

The counterfactual approach does have a genuine advantage here. By actively intervening on style while holding content approximately fixed through the preservation gates, I'm getting closer to the causal ideal that observational regression simply can't achieve. Observational methods can't distinguish "long because thorough" from "long because verbose," but the intervention-based approach can, at least in principle. This is actually the core novelty and it holds up—the proposal articulates this well.

Now I'm checking whether any existing paper does exactly what CSD proposes. Looking through the literature, I don't find anything that combines all these elements: black-box post-hoc intervention, counterfactual style manipulation, DML for robustness, multi-dimensional debiasing, and legitimacy-aware correction. The closest work like RATE uses counterfactual rewrites but lacks the DML layer and correction mechanism, while observational approaches like LC-AlpacaEval aren't causal, and training-time methods like Causal Rubrics are white-box. So the gap is real and the novelty claim actually holds.

I'm wondering if there's a broader perspective I'm missing. The framing focuses on style bias in judges, but really the core issue is that judges have preferences misaligned with human preferences—style is just one dimension. That could be a more powerful framing, positioning CSD as a general debiasing framework for black-box judges. But then again, the counterfactual intervention approach is specifically suited to style because you can generate style variants; you can't easily create counterfactuals for other biases like position or self-enhancement bias. So the style-specific framing might actually be more honest and grounded. I should also consider whether the proposal connects to the style transfer literature in NLP, since counterfactual style rewriting sits at that intersection.

Overall, the proposal is quite solid with room to sharpen the novelty framing and significance argument in a few specific places.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e6d348e-287d-41d5-b555-b1fd355e763c",
  "isSidechain": false,
  "requestId": "req_011CbDG748DjRuasZMxsXUt8",
  "type": "assistant",
  "uuid": "6575c370-feb3-44f2-a06e-7645426ec6c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2MiowfvRTKsheVH5RBi9s",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 31780,
      "output_tokens": 6755,
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
          "output_tokens": 6755,
          "cache_read_input_tokens": 31780,
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

### Assistant

_source line 44 · 2026-05-20T05:25:24.145Z_

Now I have sufficient research to make a well-grounded assessment. Let me synthesize my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- **RATE (arXiv:2410.11348, ICML 2025)**: 最接近的因果方法。通过 double-rewrite 协议解决不完美反事实问题，但仅提供可解释性（不提供校正分数），且推理成本 ~25x。CSD 与 RATE 的差异化定位清晰且合理——DML 吸收 vs. double-rewrite 抵消是两种不同的因果识别策略。
- **Causal Rubrics / CROME (arXiv:2506.16507, ICML 2025)**: 通过因果数据增强（causal augmentations + neutral augmentations）训练鲁棒 reward model，RewardBench 提升 5.4%。白盒、训练时，与 CSD 的黑盒、后处理定位形成互补而非竞争。
- **CoLD (arXiv:2507.15698)**: 反事实推理 + 因果图分析用于 process reward model 的长度去偏。限于训练时、单维度（长度）、白盒，进一步确认了 CSD 所声称的 gap 的真实性。
- **CMBE (arXiv:2505.16522, AAAI 2027)**: 同时估计多种偏差的因果效应并在推理时消除。概念上最接近 CSD 的多维因果去偏，但限于白盒模型。CSD 应更清晰地与 CMBE 区分——不仅是黑盒 vs. 白盒，更是因果识别策略的差异（CMBE 依赖模型内部表示，CSD 依赖外部反事实干预）。
- **UDA (arXiv:2508.09724, AAAI 2026)**: 通过自适应调整 Elo K-factor 实现无监督的 pairwise judge 去偏，降低 judge 间分歧 63.4%。黑盒、后处理，但机制完全不同（共识驱动 vs. 因果识别）。**Proposal 未引用此工作，可能构成 related work 遗漏。**
- **Nonparametric LLM Evaluation from Preference Data (arXiv:2601.21816, 2026)**: 将 DML 风格的去偏估计器应用于 LLM 排名，从偏好数据中导出半参数有效估计。与 CSD 共享 DML 方法论基础但目标不同（ranking 估计 vs. 分数去偏）。**Proposal 未引用此工作，可能被审稿人视为 DML-in-LLM-evaluation 方向的遗漏。**
- **CASSE (arXiv:2601.10809)**: 12 种风格特征深度纠缠的实证发现，为 CSD 的三轴独立性假设提供了重要背景。Proposal 已合理引用并讨论。
- **Counterfactual LLM-based Style Measurement (arXiv:2512.19908)**: 用 LLM 反事实重写 + Bradley-Terry 聚合量化修辞风格效应（>250K 反事实），但只量化不校正。与 CSD 的第一层（反事实生成）方法论相近，但 CSD 增加了 DML 校正层。
- 调研总结：该领域当前呈现两条平行发展的技术路线——(1) 白盒因果方法（内部表示干预、训练时增强）快速发展但无法应用于闭源模型；(2) 黑盒方法仍停留在观测回归或 prompt 工程层面。CSD 的核心定位——将半参数因果推断引入黑盒 judge 去偏——在调研中未发现直接竞争者，gap 是真实的。

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: Proposal 当前将 "dual-layer causal identification" 主要呈现为解决 "imperfect counterfactual" 这一技术难题的方案。但这低估了它的方法论深度。更有力的 framing 是：**CSD 建立了一个从经济计量学的半参数效率理论到 NLP 评估去偏的桥梁，证明反事实干预 + DML 交叉拟合不仅解决了不完美反事实问题，还提供了 RATE 的 double-rewrite 策略所不具备的理论属性——$\sqrt{n}$-一致性和半参数效率界。** 当前写法中 DML 的理论优势（doubly-robust、semiparametric efficiency）被淹没在技术细节中，没有被提升为核心差异化论点。建议在 Core Contributions 部分明确对比：RATE 的 double-rewrite 是 **algorithmic bias correction**（依赖重写偏差的对称性假设），而 CSD 的 DML 是 **statistical bias correction**（依赖半参数统计理论，对偏差结构的假设更弱）。这不仅是效率之争（7x vs 25x），而是因果识别 paradigm 的差异。
- 价值: 直接强化 Novelty 维度。审稿人在面对 "counterfactual + regression" 的组合时，容易将其视为 engineering contribution。将核心贡献提升到 **methodological bridging** 的高度——从经济计量学到 NLP 评估的跨领域方法论迁移——能显著提高 novelty 的感知度，让审稿人认识到这不仅是 "又一个去偏方法"，而是引入了一个更强的理论工具。
- 调研依据: RATE (ICML 2025) 的 double-rewrite 依赖 "rewriting the rewrite cancels rewrite-induced bias" 这一对称性假设，这在 RATE 论文中被讨论为核心 assumption。CSD 的 DML 路线绕过了这一假设，但 proposal 未充分挖掘这一理论优势的 framing 价值。

【发掘点 2】
- 维度: significance 提升
- 内容: ISE (Interventional Style Effect) 作为标准化诊断指标的潜力被严重低估。当前 proposal 在 Contribution 3 中仅用一段话描述 ISE，并以 "potential as a community-standard bias reporting metric analogous to FID" 一笔带过。建议将 ISE 的意义从 "诊断副产品" 提升为 **独立的、可能影响评估实践范式的贡献**。具体来说：(1) ISE 提供了第一个 **可跨 judge、跨域、跨版本对比的因果偏差量化标准**——这与 Soumik (arXiv:2604.23178) 的观测性 style bias score（0.76-0.92）形成鲜明对比，后者无法区分因果效应和相关性；(2) ISE 可以作为 **judge 选型的定量依据**（"在此任务上选择 formality ISE 最低的 judge"），这是目前 LLM judge 选型缺乏的；(3) ISE 可以 **追踪模型版本迭代中偏差的变化**（"GPT-4o → GPT-5 的 verbosity ISE 降低了 40%"），为模型提供商提供可操作的偏差审计工具。建议在 paper 中用一个小节专门讨论 ISE 的应用场景和标准化潜力，并论证为什么因果量化（而非观测相关性）对偏差报告至关重要。
- 价值: 直接提升 Significance。即使 CSD 的去偏效果增量有限，ISE 作为独立的偏差审计标准仍有独立价值。这为 paper 提供了"双保险"的贡献结构——即使审稿人对去偏效果的增量存疑，ISE 本身就值得发表。
- 调研依据: Soumik (arXiv:2604.23178) 量化了 style bias 为 0.76-0.92，但这是观测性指标。当前领域缺乏统一的、因果性的偏差量化标准，审稿人对 "bias 很大" 的判断依赖各自的 ad-hoc 指标。ISE 填补的不仅是技术空白，更是评估范式的空白。

【发掘点 3】
- 维度: related work 差异化
- 内容: Proposal 遗漏了两篇与 CSD 方法论或应用场景直接相关的工作：**(1) UDA (arXiv:2508.09724, AAAI 2026)**——同为黑盒、后处理的 judge 去偏方法，通过自适应 Elo K-factor 降低 judge 间分歧。虽然机制完全不同（共识驱动 vs. 因果识别），但审稿人很可能将其视为同一赛道的竞争者。Proposal 应明确讨论并区分：UDA 通过 judge 集成实现去偏（需要多个 judge），CSD 通过因果分解实现去偏（在单个 judge 上工作），两者互补。**(2) Nonparametric LLM Evaluation from Preference Data (arXiv:2601.21816)**——同样在 LLM 评估中使用 DML 风格的半参数推断。虽然目标不同（ranking 估计 vs. 分数去偏），但共享 DML 方法论基础，审稿人可能追问 CSD 与此工作的关系。
- 价值: 直接提升 Related Work 差异化，预防审稿人的 "missing related work" 质疑。UDA 的遗漏尤其危险，因为它在 AAAI 2026 发表，知名度高，且同属黑盒 judge 去偏这一赛道。
- 调研依据: UDA (arXiv:2508.09724) 和 Nonparametric LLM Evaluation (arXiv:2601.21816) 均在调研中发现，与 CSD 在方法论或应用场景上存在交叉。

【发掘点 4】
- 维度: novelty 锐化
- 内容: Legitimacy-aware correction（α 参数）是一个被低估的概念贡献。当前 proposal 将其呈现为 "domain-conditional parameter"，但其思想内核远不止于此。建议将 α 参数与公平性文献中的经典区分——**legitimate vs. illegitimate factors in decision-making**——显式关联。在因果公平性框架（Kilbertus et al. 2017, Nabi & Shpitser 2018）中，路径特定的因果效应被分为 "通过合法路径的效应" 和 "通过非法路径的效应"。CSD 的 α 机制本质上做的是同一件事：在 judge 评分中区分 **通过合法路径的风格影响**（如：技术文档中格式确实反映组织能力）和 **通过非法路径的风格偏差**（如：judge 对 markdown 格式的无差别偏好）。这个类比不仅增强 α 的理论根基，还将 CSD 的贡献连接到更广泛的因果公平性研究，扩大论文的受众面。
- 价值: 同时提升 Novelty（将 engineering parameter 提升为概念框架）和 Significance（连接到更广泛的因果公平性领域）。这个连接是有实质内容的，不是生硬嫁接——judge 去偏和公平性文献面对的核心问题是一样的：哪些影响因素是应该保留的，哪些是应该消除的。
- 调研依据: 基于领域整体趋势判断。当前 LLM 去偏文献（LC-AlpacaEval、BBE、RBD 等）均采用 "风格效应 = 偏差，应完全消除" 的隐含假设。CASSE (arXiv:2601.10809) 实证发现移除风格有 unintended side effects，但没有提出区分合法/非法风格影响的框架。CSD 的 α 机制是该领域第一个系统性地处理这一区分的尝试。

Sources:
- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://arxiv.org/abs/2410.11348)
- [Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies (Soumik)](https://arxiv.org/abs/2604.23178)
- [RBD: Debiasing with a Reasoning-based Bias Detector](https://arxiv.org/abs/2505.17100)
- [CASSE: Side Effects of Style Features](https://arxiv.org/abs/2601.10809)
- [Causal Rubrics / CROME](https://arxiv.org/abs/2506.16507)
- [CoLD: Counterfactually-Guided Length Debiasing](https://arxiv.org/abs/2507.15698)
- [Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495)
- [CMBE: Multi-Bias Elimination via Causal Effect Estimation](https://arxiv.org/abs/2505.16522)
- [CRM: Beyond Reward Hacking via Causal Rewards](https://arxiv.org/abs/2501.09620)
- [FairJudge](https://arxiv.org/abs/2602.06625)
- [BBE: Bias-Bounded Evaluation](https://arxiv.org/abs/2603.05485)
- [UDA: Unsupervised Debiasing Alignment](https://arxiv.org/abs/2508.09724)
- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/abs/2512.19908)
- [Preference Leakage](https://arxiv.org/abs/2502.01534)
- [Nonparametric LLM Evaluation from Preference Data](https://arxiv.org/abs/2601.21816)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6575c370-feb3-44f2-a06e-7645426ec6c6",
  "isSidechain": false,
  "requestId": "req_011CbDG748DjRuasZMxsXUt8",
  "type": "assistant",
  "uuid": "d4a252b8-1171-40e4-881d-083797a89a27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2MiowfvRTKsheVH5RBi9s",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 31780,
      "output_tokens": 6755,
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
          "output_tokens": 6755,
          "cache_read_input_tokens": 31780,
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

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Causal Style Decomposition for Debiasing Black-Box LLM Judges  ### 1. Problem and Motivation  LLM-as-a-Judge pipelines are increasingly used for automated evaluation, but suffer from systematic sty…",
  "leafUuid": "d4a252b8-1171-40e4-881d-083797a89a27",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Causal style decomposition for debiasing LLM judges",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "## Causal Style Decomposition for Debiasing Black-Box LLM Judges  ### 1. Problem and Motivation  LLM-as-a-Judge pipelines are increasingly used for automated evaluation, but suffer from systematic sty…",
  "leafUuid": "d4a252b8-1171-40e4-881d-083797a89a27",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Causal style decomposition for debiasing LLM judges",
  "sessionId": "8066299f-2afc-43d1-9d5b-37b6e29a5e5a"
}
```

---
