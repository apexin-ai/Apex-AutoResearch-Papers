# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Gated Many-Facet Rasch Measuremen

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/977d3218-5d4c-413b-bde4-7aea9ef6099b.jsonl`
- **Structured JSON:** [`f6e6dc01c65d09be5d76.json`](../../sessions/f6/f6e6dc01c65d09be5d76.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:17:41.798Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:17:41.798Z",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation\n\n## Description\nWe propose the Gated Many-Facet Rasch Model (G-MFRM), which extends the standard MFRM from educational measurement with a DG-IRT-inspired contamination gating mechanism to jointly calibrate model ability, item difficulty, judge severity, and contamination susceptibility within a single psychometric framework. The central methodological contribution is threefold. First, we identify a previously uncharacterized estimation pathology: judge severity and contamination susceptibility are confounded in sequential approaches — bias-only methods absorb contamination inflation into ability estimates, while contamination-only methods misattribute severity effects to lower contamination — and we provide a semi-formal proposition showing that sequential two-stage estimators yield asymptotically biased θ̂_n when d_j and c_n · e_i covary across items, with bias direction determined by the sign of their covariance (proof sketch in appendix; Fiedler's sign-reversal failure mode [arXiv:2605.06939] is characterized as a specific instance). Second, we design a hierarchical contamination parameterization via multiplicative gating c_n · e_i (N+I parameters), following the LLTM (Fischer 1973) / AMMI tradition with established identifiability guarantees. Third, we solve the fundamental obstacle to applying DG-IRT (Shu, Henson & Luecht, Psychometrika 2013) in the LLM domain: DG-IRT assumes exposure status is known to the test administrator, which is fundamentally inapplicable when no one knows which models saw which benchmark items during training. Our Stage 2 external anchoring pipeline — combining ConStat reference benchmark comparison (NeurIPS 2024, r²=0.94 on factual benchmarks), temporal pre/post-cutoff signals, and LogProber Safe Scores — constitutes a core methodological contribution that resolves this inapplicability, not merely an adaptation.\n\nThe DG-IRT cross-domain transfer involves three structural differences requiring new design decisions: (1) DG-IRT uses binary exposure indicators, but LLM contamination is continuous → continuous e_i; (2) DG-IRT operates in single-rater settings → MFRM d_j integration; (3) DG-IRT assumes known exposure → Stage 2 external anchoring. We acknowledge the rank-1 assumption (c_n · e_i) as a simplification: a single scalar c_n assumes homogeneous contamination susceptibility across task domains, whereas in reality a model may be highly contaminated on coding tasks but clean on reasoning tasks (e.g., due to domain-specific training data). We discuss conditions under which rank-1 is a good approximation (contamination from a single dominant data source), note that person-fit diagnostics (infit/outfit MNSQ) can detect rank-1 violations, and leave rank-k extensions to future work.\n\nBeyond ranking correction, G-MFRM yields interpretable multi-dimensional output: c_n for training pipeline auditing, d_j for judge selection, e_i for benchmark item retirement, and b_i for difficulty calibration. It is important to distinguish G-MFRM's examinee-side contamination (model performance inflated by training on benchmark items) from Preference Leakage's (ICLR 2026, arXiv:2502.01534) judge-side contamination (judge biased by relatedness to generator): these are mechanistically distinct phenomena. Preference Leakage's relatedness bias is partially captured by G-MFRM's d_j facet when a related model serves as judge.\n\n## Core Problem\nCan a hierarchical psychometric measurement model jointly estimate model ability, item difficulty, judge severity, and contamination susceptibility — with the contamination facet decomposed into identifiable per-model and per-item components anchored by external exposure proxies — to produce bias-and-contamination-corrected evaluation scores that outperform both siloed corrections and naive sequential pipelines? Is joint estimation methodologically necessary because judge severity and contamination susceptibility are confounded in sequential approaches, as evidenced by Fiedler's (arXiv:2605.06939) sign-reversal failure mode and formalized in our confounding proposition?\n\n## Opportunity\nThe LLM-as-a-judge evaluation literature has bifurcated into two silos using different formalisms and research communities: (1) judge bias correction (CyclicJudge, Bias-Bounded Evaluation, Soumik's 9-strategy comparison, UDA neural calibration, Fiedler's diagnostics) and (2) contamination detection/adjustment (DCR Factor, ConStat, Preference Leakage calibration). No existing work jointly models judge severity and contamination susceptibility within a single calibration framework. This gap is not merely organizational but methodological: sequential correction introduces estimation bias because each step cannot distinguish its target effect from the other's confounding influence. Fiedler (arXiv:2605.06939) has documented sign-reversal failure modes — a symptom of this confounding. The field is trending from ad-hoc metrics toward principled measurement frameworks — MFRM for rater effects (arXiv:2505.18486), IRT for benchmark analysis (PSN-IRT, AAAI 2026), formal diagnostics (Fiedler) — but no work yet unifies all identified measurement artifacts (judge bias, contamination, item difficulty) in a single generative model. G-MFRM provides this unification.\n\nRecent work applying MFRM to LLM raters (arXiv:2505.18486) diagnoses rater effects only, without contamination modeling. Casabianca & Beiting-Parrish (arXiv:2602.22585) use MFRM to correct human rater effects but focus on human raters and ignore contamination. \"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" (arXiv:2510.07175) studies contamination in psychological scales (Big Five, PVQ-40) where LLMs are test-takers — detection only, no correction, no judge modeling, distinct from our LLM-as-a-judge benchmark setting. DG-IRT (Psychometrika 2013) provides the gating mechanism but assumes administrator-known exposure, fundamentally inapplicable to LLM evaluation.\n\n## Landscape\n**Judge bias silo:** CyclicJudge (March 2026) eliminates judge bias via round-robin but ignores contamination. IRT-GRM for judge reliability (Feb 2026) diagnoses consistency without contamination modeling. Casabianca & Beiting-Parrish (arXiv:2602.22585, Feb 2026) correct human rater severity via MFRM — human raters only, no contamination. 'Judging the Judges' (Soumik, arXiv:2604.23178, April 2026) compares 9 debiasing strategies, finds style bias dominant (0.76–0.92), but explicitly lacks an explanatory measurement model. Fiedler (arXiv:2605.06939, May 2026) introduces J/delta-J diagnostics and sign-reversal failure modes, stays within classical test theory. BiasScope (ICLR 2026) automates post-hoc bias discovery. Bias-Bounded Evaluation (arXiv:2603.05485, March 2026) provides formal (τ, δ)-bias-bounded guarantees, 61–99% ranking correlation on Arena-Hard-Auto. JudgeBiasBench (March 2026): 12 bias types, 4 dimensions. UDA (AAAI 2026): neural K-factor Elo adjustment, inter-judge SD reduced 63.4%. Rogan-Gladen estimator (arXiv:2511.21140): bias correction under distribution shift for classification-based evaluation. **Contamination silo:** DCR Factor (EMNLP 2025): fuzzy inference contamination adjustment, ignores judge effects. Preference Leakage (ICLR 2026, arXiv:2502.01534): quantifies judge-side relatedness bias (generator-judge contamination), post-hoc calibration only — mechanistically distinct from examinee-side contamination modeled by G-MFRM. ConStat (NeurIPS 2024): reference benchmark comparison, r²=0.94 on factual benchmarks, fully black-box. LogProber (2024): token log-probability memorization indicators. Wang et al. (ICLR 2026): RL post-training obscures contamination signals. arXiv:2510.07175: contamination in psychological scales (detection only, no correction, no judge modeling). **IRT for LLMs:** PSN-IRT (AAAI 2026): neural 4PL IRT for benchmark evaluation, τ=0.9048 with Arena. MFRM applied to 10 LLM raters (arXiv:2505.18486) and ChatGPT-4 essay scoring (RMAL 2024). arXiv:2605.07046: identifies IRT numerical instability in LLM evaluation, proposes majorization-minimization solutions. **Gap:** No work jointly models judge severity and contamination in a single psychometric framework; DG-IRT gating never adapted to LLM contamination; sequential methods are theoretically biased due to severity-contamination confounding.\n\n## Approach\n**Why joint estimation is necessary, not merely convenient.** A naive two-stage pipeline (e.g., CyclicJudge → DCR) suffers from: (a) Bias propagation — CyclicJudge cannot distinguish genuine ability from contamination inflation, producing biased \"debiased scores\"; DCR then underestimates contamination for models judged by strict judges. (b) No uncertainty propagation — point estimates from step 1 enter step 2 as fixed inputs, causing confidence intervals to undercover. We formalize this as a proposition: under non-orthogonality of d_j and c_n · e_i across items, sequential estimators are asymptotically biased with bias direction determined by the covariance sign (proof sketch in appendix). Joint Bayesian estimation in a single likelihood resolves both problems.\n\n**Model formulation.**\n\n  logit(P_nij) = θ_n − b_i − d_j + c_n · e_i\n\nθ_n: model ability, b_i: item difficulty, d_j: judge severity, c_n: per-model contamination susceptibility, e_i: per-item exposure level. The multiplicative gating c_n · e_i follows the LLTM (Fischer 1973) / AMMI rank-1 decomposition (N+I parameters, identifiable). When e_i ≈ 0, the model reduces to standard 3-facet MFRM; when e_i > 0, performance is inflated by c_n · e_i. Rank-1 limitation: c_n assumes domain-homogeneous contamination susceptibility; violations detectable via person-fit diagnostics (infit/outfit); rank-k extensions left to future work.\n\n**Three-stage estimation.**\n\n*Stage 1 — Standard 3-facet MFRM:* Fit θ_n, b_i, d_j via Bayesian MCMC (NumPyro), ignoring contamination. Produces initial estimates and person-fit statistics (lz, EMRi).\n\n*Stage 2 — External exposure estimation (core contribution resolving DG-IRT inapplicability):* DG-IRT assumes administrator-known exposure — inapplicable when no one knows which models saw which benchmark items. We estimate e_i from external proxies independent of the MFRM fit:\n  (a) ConStat delta scores (black-box, r²=0.94 on factual benchmarks). For open-ended generation benchmarks (Arena-Hard, WildBench): task-specific checklist generation with ≥90% overlap; equivalence validation by ≥3 annotators, Fleiss' κ ≥ 0.7; same judge panel for original/rephrased variants. A dedicated ConStat validity study on open-ended tasks precedes the main experiments: delta scores on 2-3 known-contaminated open-weight models must distinguish contaminated vs. clean; if r² is significantly lower than 0.94, ConStat is downweighted in the composite and temporal/LogProber signals take primary role.\n  (b) Temporal signals: pre/post-cutoff performance gaps.\n  (c) LogProber Safe Scores (gray-box, for models exposing logprobs).\n  Weighted composite produces ê_i. Inter-indicator agreement (ConStat vs. temporal vs. LogProber correlation) reported. Person-fit statistics from Stage 1 serve as validation only (not used in estimation).\n\n*Stage 3 — Joint Gated MFRM:* Refit full model with ê_i fixed, c_n latent, Stage 1 priors. Constraints: sum(c_n) = 0, ê_i scale fixed from Stage 2. Yields fair scores θ̂_n.\n\n**MCMC convergence and identifiability protocol.** Convergence diagnostics: R̂ < 1.01, ESS > 400 for all parameters, trace plots, posterior predictive checks. Parameter recovery simulation on synthetic data with known ground-truth (θ_n, b_i, d_j, c_n, e_i): report mean absolute error and 95% credible interval coverage. Boundary conditions tested: low-contamination (e_i ≈ 0), low c_n variance, small N (≤10 models). IRT numerical instability considerations per arXiv:2605.07046 addressed via informative priors and Stage 1 warm-starting.\n\n**N-gram overlap.** Dropped for proprietary models. Supplementary validation for open-weight models (DeepSeek-V4, Kimi K2.6, Qwen3, Llama 4).\n\n**Validation design.**\n\n*Benchmarks:* Primary: Arena-Hard (arXiv:2406.11939) and WildBench. Supplementary: MT-Bench (ceiling effects acknowledged; item discrimination screening applied — items with discrimination below threshold excluded from parameter estimation, score distributions reported transparently).\n\n*Evaluated models (examinees):* 15–20 LLMs spanning frontier proprietary (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, Gemini 2.5 Pro), frontier open-weight (DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Llama 4 Maverick), and mid-tier (Qwen3.6-27B, Llama 4 Scout, Mistral Medium 3, DeepSeek-V4-Base, etc.) for sufficient score variance.\n\n*LLM judges:* 8 models (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick). Leave-one-out when judge = examinee.\n\n*Controlled contamination injection:* Fine-tune 2-3 open-weight models on specific benchmark item subsets to create known-contamination ground truth. Verify G-MFRM correctly recovers pre-contamination ranking and assigns high c_n to injected models. This provides ground truth independent of Chatbot Arena (which may itself contain contamination effects).\n\n*Baselines (8 methods + vanilla IRT):* (1) vanilla Rasch/2PL IRT (no judge facet, no contamination — most basic reference), (2) raw multi-judge averages, (3) CyclicJudge, (4) DCR Factor, (5) Preference Leakage calibration, (6) UDA (pairwise Elo converted to ranking; conversion method documented; bidirectional comparison: G-MFRM θ̂_n also converted to pairwise win probabilities for Arena pairwise outcome comparison), (7) Bias-Bounded Evaluation, (8) Rogan-Gladen estimator (arXiv:2511.21140), (9) naive two-stage pipeline (CyclicJudge → DCR). Ablation gradient: vanilla IRT → 3-facet MFRM (Stage 1) → G-MFRM (Stage 3).\n\n*Metrics:* Primary: Kendall-τ with held-out Chatbot Arena votes, reported with bootstrap 95% CIs and permutation tests for pairwise method differences. Secondary: Spearman-ρ, weighted τ_w, top-k accuracy (k=3, 5), pairwise accuracy. Qualitative: 2-3 per-model case studies with largest correction. Category-specific correlation on Arena sub-leaderboards where possible.\n\n*Ablations:* (a) Exposure indicator contribution ablation. (b) Multiplicative vs. additive gating: c_n · e_i vs. c_n + e_i. (c) Sequential order-dependence: three-way comparison — Sequential A (CyclicJudge → DCR), Sequential B (DCR → CyclicJudge), Joint G-MFRM — testing whether sequential orderings produce different rankings (order-dependence) and whether G-MFRM eliminates this, directly corresponding to Fiedler's sign-reversal finding. (d) Judge count sensitivity (2, 4, 6, 8). (e) Facet fit statistics (infit/outfit MNSQ). (f) Person-fit validation: lz/EMRi vs. c_n consistency. (g) Adversarial robustness per Wang et al. (ICLR 2026).\n\n*Efficiency analysis:* Efficiency-improvement tradeoff table (API calls, GPU hours, human annotation hours, Kendall-τ per method). Pareto frontier visualization (compute cost vs. τ). Distinction between one-time setup cost (reference benchmark construction) and per-evaluation incremental cost (new model MCMC fitting). G-MFRM positioned for high-stakes leaderboard evaluation.\n\n## Resource Estimate\nGPU hours: 200–280 (open-source judge inference ~130h A100-80GB; ConStat reference variants + evaluation ~30h; controlled contamination fine-tuning ~20h; Bayesian MCMC fitting + parameter recovery simulation ~25h; ablations ~50h; additional baselines ~25h). Human annotation: ~$3,000–5,000 (stratified sampling: 100-150 prompts full human equivalence validation, remainder LLM-assisted checklist validation). Timeline: 11–13 weeks (implementation + ConStat integration 3w, reference benchmark construction + human validation + ConStat validity study 3w, multi-judge data collection 3w, experiments and analysis 2w, paper writing 2w). Compute cost: $500–700 GPU (A100 spot) + ~$900–1,200 proprietary API calls.\n\n## Inspired By\nDG-IRT (Shu et al., Psychometrika 2013) gating mechanism; MFRM multi-facet calibration; LLTM (Fischer 1973) design-matrix decomposition; ConStat (NeurIPS 2024) external exposure estimation; Fiedler (arXiv:2605.06939) sign-reversal diagnostics motivating joint estimation necessity.\n\n## Target Venues\n- AAAI 2027 (full paper: July 28, 2026)\n- ACL 2027 (ARR submission: August 3, 2026)\n- EACL 2027 (ARR submission: August 3, 2026)\n- NAACL 2027 (ARR submission: October 15, 2026)\n\n## Key References\n- Using Deterministic, Gated IRT Model to Detect Test Cheating due to Item Compromise (Shu, Henson & Luecht, Psychometrika 2013)\n- Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model (arXiv:2505.18486, May 2025)\n- Correcting Human Labels for Rater Effects in AI Evaluation: An Item Response Theory Approach (Casabianca & Beiting-Parrish, arXiv:2602.22585, Feb 2026)\n- ConStat: Statistical Detection and Quantification of Benchmark Contamination (NeurIPS 2024)\n- CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation (arXiv 2026)\n- Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory (arXiv 2026)\n- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026, arXiv:2502.01534)\n- DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)\n- Bias and Uncertainty in LLM-as-a-Judge Estimation (Fiedler, arXiv:2605.06939, May 2026)\n- Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies (Soumik, arXiv:2604.23178, April 2026)\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models (Wang et al., ICLR 2026)\n- BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation (ICLR 2026)\n- LogProber: Detecting Data Contamination via Token Log-Probability Analysis (arXiv 2024)\n- An application of many-facet Rasch measurement: ChatGPT-4.0 essay scoring (RMAL 2024)\n- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv:2603.05485, March 2026)\n- JudgeBiasBench: Evaluating and Mitigating Bias in LLM-Based Judges (arXiv 2026)\n- The Linear Logistic Test Model (Fischer, Psychometrika 1973)\n- Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT (AAAI 2026)\n- Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (NeurIPS 2023)\n- py-irt: A Scalable Item Response Theory Library for Python (INFORMS JoC 2023)\n- UDA: Unsupervised Debiasing Alignment for LLM Judges (AAAI 2026)\n- Evaluating Rater Effects of Large Language Models in Automated Essay Scoring (Educational Measurement 2026)\n- Quantifying Data Contamination in Psychometric Evaluations of LLMs (arXiv:2510.07175, 2025)\n- How to Correctly Report LLM-as-a-Judge Evaluations (arXiv:2511.21140)\n- An Interpretable and Scalable Framework for Evaluating LLMs (arXiv:2605.07046)\n- Arena-Hard-Auto: An Automatic LLM Benchmark (arXiv:2406.11939)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:17:41.804Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:17:41.804Z",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

## Round 1

49 recorded events

### User

_source line 3 · 2026-05-20T05:17:41.818Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation

## Description
We propose the Gated Many-Facet Rasch Model (G-MFRM), which extends the standard MFRM from educational measurement with a DG-IRT-inspired contamination gating mechanism to jointly calibrate model ability, item difficulty, judge severity, and contamination susceptibility within a single psychometric framework. The central methodological contribution is threefold. First, we identify a previously uncharacterized estimation pathology: judge severity and contamination susceptibility are confounded in sequential approaches — bias-only methods absorb contamination inflation into ability estimates, while contamination-only methods misattribute severity effects to lower contamination — and we provide a semi-formal proposition showing that sequential two-stage estimators yield asymptotically biased θ̂_n when d_j and c_n · e_i covary across items, with bias direction determined by the sign of their covariance (proof sketch in appendix; Fiedler's sign-reversal failure mode [arXiv:2605.06939] is characterized as a specific instance). Second, we design a hierarchical contamination parameterization via multiplicative gating c_n · e_i (N+I parameters), following the LLTM (Fischer 1973) / AMMI tradition with established identifiability guarantees. Third, we solve the fundamental obstacle to applying DG-IRT (Shu, Henson & Luecht, Psychometrika 2013) in the LLM domain: DG-IRT assumes exposure status is known to the test administrator, which is fundamentally inapplicable when no one knows which models saw which benchmark items during training. Our Stage 2 external anchoring pipeline — combining ConStat reference benchmark comparison (NeurIPS 2024, r²=0.94 on factual benchmarks), temporal pre/post-cutoff signals, and LogProber Safe Scores — constitutes a core methodological contribution that resolves this inapplicability, not merely an adaptation.

The DG-IRT cross-domain transfer involves three structural differences requiring new design decisions: (1) DG-IRT uses binary exposure indicators, but LLM contamination is continuous → continuous e_i; (2) DG-IRT operates in single-rater settings → MFRM d_j integration; (3) DG-IRT assumes known exposure → Stage 2 external anchoring. We acknowledge the rank-1 assumption (c_n · e_i) as a simplification: a single scalar c_n assumes homogeneous contamination susceptibility across task domains, whereas in reality a model may be highly contaminated on coding tasks but clean on reasoning tasks (e.g., due to domain-specific training data). We discuss conditions under which rank-1 is a good approximation (contamination from a single dominant data source), note that person-fit diagnostics (infit/outfit MNSQ) can detect rank-1 violations, and leave rank-k extensions to future work.

Beyond ranking correction, G-MFRM yields interpretable multi-dimensional output: c_n for training pipeline auditing, d_j for judge selection, e_i for benchmark item retirement, and b_i for difficulty calibration. It is important to distinguish G-MFRM's examinee-side contamination (model performance inflated by training on benchmark items) from Preference Leakage's (ICLR 2026, arXiv:2502.01534) judge-side contamination (judge biased by relatedness to generator): these are mechanistically distinct phenomena. Preference Leakage's relatedness bias is partially captured by G-MFRM's d_j facet when a related model serves as judge.

## Core Problem
Can a hierarchical psychometric measurement model jointly estimate model ability, item difficulty, judge severity, and contamination susceptibility — with the contamination facet decomposed into identifiable per-model and per-item components anchored by external exposure proxies — to produce bias-and-contamination-corrected evaluation scores that outperform both siloed corrections and naive sequential pipelines? Is joint estimation methodologically necessary because judge severity and contamination susceptibility are confounded in sequential approaches, as evidenced by Fiedler's (arXiv:2605.06939) sign-reversal failure mode and formalized in our confounding proposition?

## Opportunity
The LLM-as-a-judge evaluation literature has bifurcated into two silos using different formalisms and research communities: (1) judge bias correction (CyclicJudge, Bias-Bounded Evaluation, Soumik's 9-strategy comparison, UDA neural calibration, Fiedler's diagnostics) and (2) contamination detection/adjustment (DCR Factor, ConStat, Preference Leakage calibration). No existing work jointly models judge severity and contamination susceptibility within a single calibration framework. This gap is not merely organizational but methodological: sequential correction introduces estimation bias because each step cannot distinguish its target effect from the other's confounding influence. Fiedler (arXiv:2605.06939) has documented sign-reversal failure modes — a symptom of this confounding. The field is trending from ad-hoc metrics toward principled measurement frameworks — MFRM for rater effects (arXiv:2505.18486), IRT for benchmark analysis (PSN-IRT, AAAI 2026), formal diagnostics (Fiedler) — but no work yet unifies all identified measurement artifacts (judge bias, contamination, item difficulty) in a single generative model. G-MFRM provides this unification.

Recent work applying MFRM to LLM raters (arXiv:2505.18486) diagnoses rater effects only, without contamination modeling. Casabianca & Beiting-Parrish (arXiv:2602.22585) use MFRM to correct human rater effects but focus on human raters and ignore contamination. "Quantifying Data Contamination in Psychometric Evaluations of LLMs" (arXiv:2510.07175) studies contamination in psychological scales (Big Five, PVQ-40) where LLMs are test-takers — detection only, no correction, no judge modeling, distinct from our LLM-as-a-judge benchmark setting. DG-IRT (Psychometrika 2013) provides the gating mechanism but assumes administrator-known exposure, fundamentally inapplicable to LLM evaluation.

## Landscape
**Judge bias silo:** CyclicJudge (March 2026) eliminates judge bias via round-robin but ignores contamination. IRT-GRM for judge reliability (Feb 2026) diagnoses consistency without contamination modeling. Casabianca & Beiting-Parrish (arXiv:2602.22585, Feb 2026) correct human rater severity via MFRM — human raters only, no contamination. 'Judging the Judges' (Soumik, arXiv:2604.23178, April 2026) compares 9 debiasing strategies, finds style bias dominant (0.76–0.92), but explicitly lacks an explanatory measurement model. Fiedler (arXiv:2605.06939, May 2026) introduces J/delta-J diagnostics and sign-reversal failure modes, stays within classical test theory. BiasScope (ICLR 2026) automates post-hoc bias discovery. Bias-Bounded Evaluation (arXiv:2603.05485, March 2026) provides formal (τ, δ)-bias-bounded guarantees, 61–99% ranking correlation on Arena-Hard-Auto. JudgeBiasBench (March 2026): 12 bias types, 4 dimensions. UDA (AAAI 2026): neural K-factor Elo adjustment, inter-judge SD reduced 63.4%. Rogan-Gladen estimator (arXiv:2511.21140): bias correction under distribution shift for classification-based evaluation. **Contamination silo:** DCR Factor (EMNLP 2025): fuzzy inference contamination adjustment, ignores judge effects. Preference Leakage (ICLR 2026, arXiv:2502.01534): quantifies judge-side relatedness bias (generator-judge contamination), post-hoc calibration only — mechanistically distinct from examinee-side contamination modeled by G-MFRM. ConStat (NeurIPS 2024): reference benchmark comparison, r²=0.94 on factual benchmarks, fully black-box. LogProber (2024): token log-probability memorization indicators. Wang et al. (ICLR 2026): RL post-training obscures contamination signals. arXiv:2510.07175: contamination in psychological scales (detection only, no correction, no judge modeling). **IRT for LLMs:** PSN-IRT (AAAI 2026): neural 4PL IRT for benchmark evaluation, τ=0.9048 with Arena. MFRM applied to 10 LLM raters (arXiv:2505.18486) and ChatGPT-4 essay scoring (RMAL 2024). arXiv:2605.07046: identifies IRT numerical instability in LLM evaluation, proposes majorization-minimization solutions. **Gap:** No work jointly models judge severity and contamination in a single psychometric framework; DG-IRT gating never adapted to LLM contamination; sequential methods are theoretically biased due to severity-contamination confounding.

## Approach
**Why joint estimation is necessary, not merely convenient.** A naive two-stage pipeline (e.g., CyclicJudge → DCR) suffers from: (a) Bias propagation — CyclicJudge cannot distinguish genuine ability from contamination inflation, producing biased "debiased scores"; DCR then underestimates contamination for models judged by strict judges. (b) No uncertainty propagation — point estimates from step 1 enter step 2 as fixed inputs, causing confidence intervals to undercover. We formalize this as a proposition: under non-orthogonality of d_j and c_n · e_i across items, sequential estimators are asymptotically biased with bias direction determined by the covariance sign (proof sketch in appendix). Joint Bayesian estimation in a single likelihood resolves both problems.

**Model formulation.**

  logit(P_nij) = θ_n − b_i − d_j + c_n · e_i

θ_n: model ability, b_i: item difficulty, d_j: judge severity, c_n: per-model contamination susceptibility, e_i: per-item exposure level. The multiplicative gating c_n · e_i follows the LLTM (Fischer 1973) / AMMI rank-1 decomposition (N+I parameters, identifiable). When e_i ≈ 0, the model reduces to standard 3-facet MFRM; when e_i > 0, performance is inflated by c_n · e_i. Rank-1 limitation: c_n assumes domain-homogeneous contamination susceptibility; violations detectable via person-fit diagnostics (infit/outfit); rank-k extensions left to future work.

**Three-stage estimation.**

*Stage 1 — Standard 3-facet MFRM:* Fit θ_n, b_i, d_j via Bayesian MCMC (NumPyro), ignoring contamination. Produces initial estimates and person-fit statistics (lz, EMRi).

*Stage 2 — External exposure estimation (core contribution resolving DG-IRT inapplicability):* DG-IRT assumes administrator-known exposure — inapplicable when no one knows which models saw which benchmark items. We estimate e_i from external proxies independent of the MFRM fit:
  (a) ConStat delta scores (black-box, r²=0.94 on factual benchmarks). For open-ended generation benchmarks (Arena-Hard, WildBench): task-specific checklist generation with ≥90% overlap; equivalence validation by ≥3 annotators, Fleiss' κ ≥ 0.7; same judge panel for original/rephrased variants. A dedicated ConStat validity study on open-ended tasks precedes the main experiments: delta scores on 2-3 known-contaminated open-weight models must distinguish contaminated vs. clean; if r² is significantly lower than 0.94, ConStat is downweighted in the composite and temporal/LogProber signals take primary role.
  (b) Temporal signals: pre/post-cutoff performance gaps.
  (c) LogProber Safe Scores (gray-box, for models exposing logprobs).
  Weighted composite produces ê_i. Inter-indicator agreement (ConStat vs. temporal vs. LogProber correlation) reported. Person-fit statistics from Stage 1 serve as validation only (not used in estimation).

*Stage 3 — Joint Gated MFRM:* Refit full model with ê_i fixed, c_n latent, Stage 1 priors. Constraints: sum(c_n) = 0, ê_i scale fixed from Stage 2. Yields fair scores θ̂_n.

**MCMC convergence and identifiability protocol.** Convergence diagnostics: R̂ < 1.01, ESS > 400 for all parameters, trace plots, posterior predictive checks. Parameter recovery simulation on synthetic data with known ground-truth (θ_n, b_i, d_j, c_n, e_i): report mean absolute error and 95% credible interval coverage. Boundary conditions tested: low-contamination (e_i ≈ 0), low c_n variance, small N (≤10 models). IRT numerical instability considerations per arXiv:2605.07046 addressed via informative priors and Stage 1 warm-starting.

**N-gram overlap.** Dropped for proprietary models. Supplementary validation for open-weight models (DeepSeek-V4, Kimi K2.6, Qwen3, Llama 4).

**Validation design.**

*Benchmarks:* Primary: Arena-Hard (arXiv:2406.11939) and WildBench. Supplementary: MT-Bench (ceiling effects acknowledged; item discrimination screening applied — items with discrimination below threshold excluded from parameter estimation, score distributions reported transparently).

*Evaluated models (examinees):* 15–20 LLMs spanning frontier proprietary (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, Gemini 2.5 Pro), frontier open-weight (DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Llama 4 Maverick), and mid-tier (Qwen3.6-27B, Llama 4 Scout, Mistral Medium 3, DeepSeek-V4-Base, etc.) for sufficient score variance.

*LLM judges:* 8 models (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick). Leave-one-out when judge = examinee.

*Controlled contamination injection:* Fine-tune 2-3 open-weight models on specific benchmark item subsets to create known-contamination ground truth. Verify G-MFRM correctly recovers pre-contamination ranking and assigns high c_n to injected models. This provides ground truth independent of Chatbot Arena (which may itself contain contamination effects).

*Baselines (8 methods + vanilla IRT):* (1) vanilla Rasch/2PL IRT (no judge facet, no contamination — most basic reference), (2) raw multi-judge averages, (3) CyclicJudge, (4) DCR Factor, (5) Preference Leakage calibration, (6) UDA (pairwise Elo converted to ranking; conversion method documented; bidirectional comparison: G-MFRM θ̂_n also converted to pairwise win probabilities for Arena pairwise outcome comparison), (7) Bias-Bounded Evaluation, (8) Rogan-Gladen estimator (arXiv:2511.21140), (9) naive two-stage pipeline (CyclicJudge → DCR). Ablation gradient: vanilla IRT → 3-facet MFRM (Stage 1) → G-MFRM (Stage 3).

*Metrics:* Primary: Kendall-τ with held-out Chatbot Arena votes, reported with bootstrap 95% CIs and permutation tests for pairwise method differences. Secondary: Spearman-ρ, weighted τ_w, top-k accuracy (k=3, 5), pairwise accuracy. Qualitative: 2-3 per-model case studies with largest correction. Category-specific correlation on Arena sub-leaderboards where possible.

*Ablations:* (a) Exposure indicator contribution ablation. (b) Multiplicative vs. additive gating: c_n · e_i vs. c_n + e_i. (c) Sequential order-dependence: three-way comparison — Sequential A (CyclicJudge → DCR), Sequential B (DCR → CyclicJudge), Joint G-MFRM — testing whether sequential orderings produce different rankings (order-dependence) and whether G-MFRM eliminates this, directly corresponding to Fiedler's sign-reversal finding. (d) Judge count sensitivity (2, 4, 6, 8). (e) Facet fit statistics (infit/outfit MNSQ). (f) Person-fit validation: lz/EMRi vs. c_n consistency. (g) Adversarial robustness per Wang et al. (ICLR 2026).

*Efficiency analysis:* Efficiency-improvement tradeoff table (API calls, GPU hours, human annotation hours, Kendall-τ per method). Pareto frontier visualization (compute cost vs. τ). Distinction between one-time setup cost (reference benchmark construction) and per-evaluation incremental cost (new model MCMC fitting). G-MFRM positioned for high-stakes leaderboard evaluation.

## Resource Estimate
GPU hours: 200–280 (open-source judge inference ~130h A100-80GB; ConStat reference variants + evaluation ~30h; controlled contamination fine-tuning ~20h; Bayesian MCMC fitting + parameter recovery simulation ~25h; ablations ~50h; additional baselines ~25h). Human annotation: ~$3,000–5,000 (stratified sampling: 100-150 prompts full human equivalence validation, remainder LLM-assisted checklist validation). Timeline: 11–13 weeks (implementation + ConStat integration 3w, reference benchmark construction + human validation + ConStat validity study 3w, multi-judge data collection 3w, experiments and analysis 2w, paper writing 2w). Compute cost: $500–700 GPU (A100 spot) + ~$900–1,200 proprietary API calls.

## Inspired By
DG-IRT (Shu et al., Psychometrika 2013) gating mechanism; MFRM multi-facet calibration; LLTM (Fischer 1973) design-matrix decomposition; ConStat (NeurIPS 2024) external exposure estimation; Fiedler (arXiv:2605.06939) sign-reversal diagnostics motivating joint estimation necessity.

## Target Venues
- AAAI 2027 (full paper: July 28, 2026)
- ACL 2027 (ARR submission: August 3, 2026)
- EACL 2027 (ARR submission: August 3, 2026)
- NAACL 2027 (ARR submission: October 15, 2026)

## Key References
- Using Deterministic, Gated IRT Model to Detect Test Cheating due to Item Compromise (Shu, Henson & Luecht, Psychometrika 2013)
- Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model (arXiv:2505.18486, May 2025)
- Correcting Human Labels for Rater Effects in AI Evaluation: An Item Response Theory Approach (Casabianca & Beiting-Parrish, arXiv:2602.22585, Feb 2026)
- ConStat: Statistical Detection and Quantification of Benchmark Contamination (NeurIPS 2024)
- CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation (arXiv 2026)
- Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory (arXiv 2026)
- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026, arXiv:2502.01534)
- DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)
- Bias and Uncertainty in LLM-as-a-Judge Estimation (Fiedler, arXiv:2605.06939, May 2026)
- Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies (Soumik, arXiv:2604.23178, April 2026)
- On The Fragility of Benchmark Contamination Detection in Reasoning Models (Wang et al., ICLR 2026)
- BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation (ICLR 2026)
- LogProber: Detecting Data Contamination via Token Log-Probability Analysis (arXiv 2024)
- An application of many-facet Rasch measurement: ChatGPT-4.0 essay scoring (RMAL 2024)
- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv:2603.05485, March 2026)
- JudgeBiasBench: Evaluating and Mitigating Bias in LLM-Based Judges (arXiv 2026)
- The Linear Logistic Test Model (Fischer, Psychometrika 1973)
- Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT (AAAI 2026)
- Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (NeurIPS 2023)
- py-irt: A Scalable Item Response Theory Library for Python (INFORMS JoC 2023)
- UDA: Unsupervised Debiasing Alignment for LLM Judges (AAAI 2026)
- Evaluating Rater Effects of Large Language Models in Automated Essay Scoring (Educational Measurement 2026)
- Quantifying Data Contamination in Psychometric Evaluations of LLMs (arXiv:2510.07175, 2025)
- How to Correctly Report LLM-as-a-Judge Evaluations (arXiv:2511.21140)
- An Interpretable and Scalable Framework for Evaluating LLMs (arXiv:2605.07046)
- Arena-Hard-Auto: An Automatic LLM Benchmark (arXiv:2406.11939)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "9adc4d34-3f2d-42fe-a700-dc95ce578622",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:17:41.817Z_

```json
{
  "parentUuid": "9adc4d34-3f2d-42fe-a700-dc95ce578622",
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
  "uuid": "22398437-0741-414f-9b06-2e9184e11c6a",
  "timestamp": "2026-05-20T05:17:41.817Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:17:41.817Z_

```json
{
  "parentUuid": "22398437-0741-414f-9b06-2e9184e11c6a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b14a3441-84bc-4605-bbd8-6502ca4876d5",
  "timestamp": "2026-05-20T05:17:41.817Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation  ## Descr…",
  "leafUuid": "b14a3441-84bc-4605-bbd8-6502ca4876d5",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint judge bias and contamination correction via gated Rasch model",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:17:49.515Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for EMNLP 2026 submission. I need to first conduct thorough literature research before scoring. Let me start by searching for the key topics in this proposal.

The proposal is about "Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation" - it combines psychometric models (MFRM, DG-IRT) to jointly calibrate judge bias and contamination in LLM-as-a-judge evaluation.

Let me search for:
1. Recent work on MFRM/IRT in LLM evaluation


2. Joint judge bias and contamination correction approaches
3. DG-IRT applications and related work
4. ConStat and other contamination detection methods
5. The specific papers cited (Fiedler, CyclicJudge, etc.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b14a3441-84bc-4605-bbd8-6502ca4876d5",
  "isSidechain": false,
  "requestId": "req_011CbDFiZcN5wz7iEZNea5r9",
  "type": "assistant",
  "uuid": "da6e350a-715e-40cb-9a27-67dabd26720e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXzARNPX5DB2Wt9is6VEvi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7101,
      "cache_read_input_tokens": 13882,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 13882,
          "cache_creation_input_tokens": 7101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7101
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

_source line 9 · 2026-05-20T05:17:49.567Z_

I'll start by conducting thorough literature research before making any evaluation. Let me search for the key topics in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da6e350a-715e-40cb-9a27-67dabd26720e",
  "isSidechain": false,
  "requestId": "req_011CbDFiZcN5wz7iEZNea5r9",
  "type": "assistant",
  "uuid": "2823622a-93b3-47a1-b936-41ff50abdad3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXzARNPX5DB2Wt9is6VEvi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7101,
      "cache_read_input_tokens": 13882,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 13882,
          "cache_creation_input_tokens": 7101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7101
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

_source line 10 · 2026-05-20T05:17:50.065Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RwWHu55tLwi6ygmWe6Tfgr`</summary>

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
  "parentUuid": "2823622a-93b3-47a1-b936-41ff50abdad3",
  "isSidechain": false,
  "requestId": "req_011CbDFiZcN5wz7iEZNea5r9",
  "type": "assistant",
  "uuid": "5e97f3aa-2115-4cb2-a89a-5cda435b3de4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXzARNPX5DB2Wt9is6VEvi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7101,
      "cache_read_input_tokens": 13882,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 13882,
          "cache_creation_input_tokens": 7101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7101
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

_source line 11 · 2026-05-20T05:17:50.072Z_

<details><summary>↩ Tool result · `toolu_01RwWHu55tLwi6ygmWe6Tfgr`</summary>

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
  "parentUuid": "5e97f3aa-2115-4cb2-a89a-5cda435b3de4",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "d65340f2-53b1-4501-8796-1e2db3261f7b",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "5e97f3aa-2115-4cb2-a89a-5cda435b3de4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:17:52.491Z_

Now let me conduct the required literature searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d65340f2-53b1-4501-8796-1e2db3261f7b",
  "isSidechain": false,
  "requestId": "req_011CbDFjBZLZZacAb4L9hEXr",
  "type": "assistant",
  "uuid": "72a7269e-c7a2-46cd-91a6-142d1d9d117c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFqzJzasX9TqicmV4xgojt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 20983,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 20983,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
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

_source line 13 · 2026-05-20T05:17:52.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GNZSfKAxb9vKH48wSPodcq`</summary>

```json
{
  "query": "Many-Facet Rasch Model LLM evaluation judge bias 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72a7269e-c7a2-46cd-91a6-142d1d9d117c",
  "isSidechain": false,
  "requestId": "req_011CbDFjBZLZZacAb4L9hEXr",
  "type": "assistant",
  "uuid": "70ed1048-79d1-440d-b0f3-f98798554f53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFqzJzasX9TqicmV4xgojt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 20983,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 20983,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
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

_source line 14 · 2026-05-20T05:17:53.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SH3dodD9hAxXms3Rws59cz`</summary>

```json
{
  "query": "DG-IRT gated item response theory contamination detection LLM benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70ed1048-79d1-440d-b0f3-f98798554f53",
  "isSidechain": false,
  "requestId": "req_011CbDFjBZLZZacAb4L9hEXr",
  "type": "assistant",
  "uuid": "c14e4bea-76d6-4131-b016-f10aec01d9b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFqzJzasX9TqicmV4xgojt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 20983,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 20983,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
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

_source line 15 · 2026-05-20T05:17:54.416Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SR5CEc4JP9wPgMWzsfut96`</summary>

```json
{
  "query": "joint judge bias contamination correction LLM-as-a-judge psychometric framework 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c14e4bea-76d6-4131-b016-f10aec01d9b2",
  "isSidechain": false,
  "requestId": "req_011CbDFjBZLZZacAb4L9hEXr",
  "type": "assistant",
  "uuid": "6ea96a2d-528b-4ca0-a516-5263e8d41204",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFqzJzasX9TqicmV4xgojt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 20983,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 20983,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
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

_source line 16 · 2026-05-20T05:17:54.942Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EcNBD7ei2NMvh4TfztATUy`</summary>

```json
{
  "query": "ConStat benchmark contamination detection NeurIPS 2024 LLM evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ea96a2d-528b-4ca0-a516-5263e8d41204",
  "isSidechain": false,
  "requestId": "req_011CbDFjBZLZZacAb4L9hEXr",
  "type": "assistant",
  "uuid": "49ea051b-d6b1-4367-bc39-5e4ef2ed0b67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFqzJzasX9TqicmV4xgojt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 20983,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 20983,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
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

_source line 17 · 2026-05-20T05:17:55.465Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MPUH137HncFNnQ8pweLiZM`</summary>

```json
{
  "query": "Fiedler LLM judge bias sign-reversal arXiv 2605.06939 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49ea051b-d6b1-4367-bc39-5e4ef2ed0b67",
  "isSidechain": false,
  "requestId": "req_011CbDFjBZLZZacAb4L9hEXr",
  "type": "assistant",
  "uuid": "af7c29cb-2d5f-4621-8a32-d0a3dacd6c15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LFqzJzasX9TqicmV4xgojt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 20983,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 20983,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
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

_source line 18 · 2026-05-20T05:17:59.860Z_

<details><summary>↩ Tool result · `toolu_01GNZSfKAxb9vKH48wSPodcq`</summary>

```text
Web search results for query: "Many-Facet Rasch Model LLM evaluation judge bias 2025 2026"

Links: [{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline","url":"https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"},{"title":"[2506.22316] Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/abs/2506.22316"},{"title":"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/pdf/2603.01865"},{"title":"BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation","url":"https://arxiv.org/pdf/2602.09383"},{"title":"The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation","url":"https://arxiv.org/pdf/2602.07996"},{"title":"Curse of Knowledge: When Complex Evaluation Context Benefits yet Biases LLM Judges","url":"https://arxiv.org/pdf/2509.03419"}]

Based on the search results, here's what recent research shows about LLM evaluation and judge bias in 2025-2026:

## Key Findings on Judge Bias in LLM Evaluation

**Widespread Bias Issues:**
Studies published in 2025 and early 2026 have systematically documented where LLM judges fail, why they fail, and how often. LLM judges are systematically biased: some models are consistently lenient, others strict, with additional position, verbosity, and self-preference effects.

**Specific Biases Identified:**
Both models exhibit a strong recency bias, systematically favoring "new" responses over "old", as well as a clear provenance hierarchy (EXPERT > HUMAN > LLM > UNKNOWN). Common types include gender bias, length bias, self-bias, position bias, and so on.

**Reliability Concerns:**
LLM judges hit 80% accuracy in controlled tests. In production, frontier models exceeded 50% error rates on bias tests.

**Mitigation Strategies:**
CyclicJudge, a round-robin assignment of judges to scenarios, is demonstrated to be the optimal strategy for a fixed judge-call budget. It eliminates bias precisely while requiring each judge only once per cycle, matching the cost of single-judge evaluation.

The research indicates that while LLM-as-a-judge evaluation is now mainstream, addressing systematic bias has become a critical priority for the field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70ed1048-79d1-440d-b0f3-f98798554f53",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "4753b836-c3a4-4533-95ec-dd59bbc174e1",
  "toolUseResult": {
    "query": "Many-Facet Rasch Model LLM evaluation judge bias 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ED3dmtSCR8AUPTWBLNvy5c",
        "content": [
          {
            "title": "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2509.26072"
          },
          {
            "title": "LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests | Adaline",
            "url": "https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias"
          },
          {
            "title": "[2506.22316] Evaluating Scoring Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2506.22316"
          },
          {
            "title": "CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation",
            "url": "https://arxiv.org/pdf/2603.01865"
          },
          {
            "title": "BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation",
            "url": "https://arxiv.org/pdf/2602.09383"
          },
          {
            "title": "The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation",
            "url": "https://arxiv.org/pdf/2602.07996"
          },
          {
            "title": "Curse of Knowledge: When Complex Evaluation Context Benefits yet Biases LLM Judges",
            "url": "https://arxiv.org/pdf/2509.03419"
          }
        ]
      },
      "Based on the search results, here's what recent research shows about LLM evaluation and judge bias in 2025-2026:\n\n## Key Findings on Judge Bias in LLM Evaluation\n\n**Widespread Bias Issues:**\nStudies published in 2025 and early 2026 have systematically documented where LLM judges fail, why they fail, and how often. LLM judges are systematically biased: some models are consistently lenient, others strict, with additional position, verbosity, and self-preference effects.\n\n**Specific Biases Identified:**\nBoth models exhibit a strong recency bias, systematically favoring \"new\" responses over \"old\", as well as a clear provenance hierarchy (EXPERT > HUMAN > LLM > UNKNOWN). Common types include gender bias, length bias, self-bias, position bias, and so on.\n\n**Reliability Concerns:**\nLLM judges hit 80% accuracy in controlled tests. In production, frontier models exceeded 50% error rates on bias tests.\n\n**Mitigation Strategies:**\nCyclicJudge, a round-robin assignment of judges to scenarios, is demonstrated to be the optimal strategy for a fixed judge-call budget. It eliminates bias precisely while requiring each judge only once per cycle, matching the cost of single-judge evaluation.\n\nThe research indicates that while LLM-as-a-judge evaluation is now mainstream, addressing systematic bias has become a critical priority for the field."
    ],
    "durationSeconds": 6.857561421000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "70ed1048-79d1-440d-b0f3-f98798554f53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T05:17:59.907Z_

<details><summary>↩ Tool result · `toolu_01SH3dodD9hAxXms3Rws59cz`</summary>

```text
Web search results for query: "DG-IRT gated item response theory contamination detection LLM benchmark 2025 2026"

Links: [{"title":"[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"(PDF) Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise","url":"https://www.researchgate.net/publication/257678777_Using_Deterministic_Gated_Item_Response_Theory_Model_to_Detect_Test_Cheating_due_to_Item_Compromise"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"}]

Based on the search results, I found relevant information about Item Response Theory (IRT) applications to LLM benchmarking, though the specific "DG-IRT" acronym you mentioned doesn't appear in these recent results. However, here's what I found:

## Key Findings:

**PSN-IRT Framework for LLM Benchmarks:**
PSN-IRT is a framework that combines psychometrics with neural networks to analyze LLM benchmarks, demonstrating that current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination.

**Data Contamination Detection:**
LLM benchmarks exhibit data contamination in numerous items, compromising their reliability, and model rankings derived from high-quality datasets selected by PSN-IRT are more consistent with human preference and offer stronger discriminability among top models.

**Recent Applications:**
PSN-IRT has been utilized for analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.

**IRT for Medical LLM Evaluation:**
A computerized adaptive testing (CAT) framework grounded in item response theory (IRT) has been proposed for efficient assessment of standardized medical knowledge in LLMs.

The search results show active research into IRT-based contamination detection for LLM benchmarks in 2025-2026, though I didn't find a paper specifically titled with "DG-IRT" in these results. If you're looking for a specific paper with that exact acronym, you might want to search for it directly or provide additional context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c14e4bea-76d6-4131-b016-f10aec01d9b2",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "65821f22-9f31-40a4-8e60-3dfa9bf139d8",
  "toolUseResult": {
    "query": "DG-IRT gated item response theory contamination detection LLM benchmark 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013h7kecvySC8R51GhuoYVxt",
        "content": [
          {
            "title": "[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v2"
          },
          {
            "title": "(PDF) Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise",
            "url": "https://www.researchgate.net/publication/257678777_Using_Deterministic_Gated_Item_Response_Theory_Model_to_Detect_Test_Cheating_due_to_Item_Compromise"
          },
          {
            "title": "Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking",
            "url": "https://arxiv.org/pdf/2603.23506"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40814"
          },
          {
            "title": "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory",
            "url": "https://arxiv.org/pdf/2602.00521"
          }
        ]
      },
      "Based on the search results, I found relevant information about Item Response Theory (IRT) applications to LLM benchmarking, though the specific \"DG-IRT\" acronym you mentioned doesn't appear in these recent results. However, here's what I found:\n\n## Key Findings:\n\n**PSN-IRT Framework for LLM Benchmarks:**\nPSN-IRT is a framework that combines psychometrics with neural networks to analyze LLM benchmarks, demonstrating that current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination.\n\n**Data Contamination Detection:**\nLLM benchmarks exhibit data contamination in numerous items, compromising their reliability, and model rankings derived from high-quality datasets selected by PSN-IRT are more consistent with human preference and offer stronger discriminability among top models.\n\n**Recent Applications:**\nPSN-IRT has been utilized for analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.\n\n**IRT for Medical LLM Evaluation:**\nA computerized adaptive testing (CAT) framework grounded in item response theory (IRT) has been proposed for efficient assessment of standardized medical knowledge in LLMs.\n\nThe search results show active research into IRT-based contamination detection for LLM benchmarks in 2025-2026, though I didn't find a paper specifically titled with \"DG-IRT\" in these results. If you're looking for a specific paper with that exact acronym, you might want to search for it directly or provide additional context."
    ],
    "durationSeconds": 6.434166108000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c14e4bea-76d6-4131-b016-f10aec01d9b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T05:18:01.648Z_

<details><summary>↩ Tool result · `toolu_01EcNBD7ei2NMvh4TfztATUy`</summary>

```text
Web search results for query: "ConStat benchmark contamination detection NeurIPS 2024 LLM evaluation"

Links: [{"title":"[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"},{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/96266"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/html/2405.16281v1"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language   Models","url":"https://arxiv.org/pdf/2405.16281"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/dekoninck2024constat"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2405.16281"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://constat.ai/"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"}]

Based on the search results, here's what I found about ConStat:

## Overview

ConStat is a statistical test presented at NeurIPS 2024 for detecting and quantifying benchmark contamination in LLMs. ConStat is a statistical method that reliably detects and quantifies contamination by comparing performance between a primary and reference benchmark relative to a set of reference models.

## Key Innovation

The work defines contamination based on artificially inflated, non-generalizing benchmark performance rather than solely on training data inclusion, proposing a novel performance-based definition of benchmark contamination. This perspective enables detection of any model with inflated performance, i.e., performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.

## How It Works

ConStat evaluates performance by comparing a target model's actual performance to its expected performance, predicted using a difficulty correction function derived from reference models.

## Key Findings

ConStat found high levels of contamination in multiple popular models including Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models. ConStat demonstrated effectiveness in detecting and quantifying contamination across various scenarios, outperforming prior methods.

The research was authored by Jasper Dekoninck, Mark Niklas Müller, and Martin Vechev, and the code is publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49ea051b-d6b1-4367-bc39-5e4ef2ed0b67",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "6ab0b66f-1125-4fea-8077-5102ae673d04",
  "toolUseResult": {
    "query": "ConStat benchmark contamination detection NeurIPS 2024 LLM evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AYUP5cQPa1m3XT5tDpc1r6",
        "content": [
          {
            "title": "[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"
          },
          {
            "title": "NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://neurips.cc/virtual/2024/poster/96266"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/html/2405.16281v1"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language   Models",
            "url": "https://arxiv.org/pdf/2405.16281"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models | SRI Lab",
            "url": "https://www.sri.inf.ethz.ch/publications/dekoninck2024constat"
          },
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/abs/2405.16281"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://constat.ai/"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about ConStat:\n\n## Overview\n\nConStat is a statistical test presented at NeurIPS 2024 for detecting and quantifying benchmark contamination in LLMs. ConStat is a statistical method that reliably detects and quantifies contamination by comparing performance between a primary and reference benchmark relative to a set of reference models.\n\n## Key Innovation\n\nThe work defines contamination based on artificially inflated, non-generalizing benchmark performance rather than solely on training data inclusion, proposing a novel performance-based definition of benchmark contamination. This perspective enables detection of any model with inflated performance, i.e., performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.\n\n## How It Works\n\nConStat evaluates performance by comparing a target model's actual performance to its expected performance, predicted using a difficulty correction function derived from reference models.\n\n## Key Findings\n\nConStat found high levels of contamination in multiple popular models including Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models. ConStat demonstrated effectiveness in detecting and quantifying contamination across various scenarios, outperforming prior methods.\n\nThe research was authored by Jasper Dekoninck, Mark Niklas Müller, and Martin Vechev, and the code is publicly available."
    ],
    "durationSeconds": 6.701903107,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "49ea051b-d6b1-4367-bc39-5e4ef2ed0b67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation  ## Descr…",
  "leafUuid": "6ab0b66f-1125-4fea-8077-5102ae673d04",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint judge bias and contamination correction via gated Rasch model",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

### Tool result

_source line 23 · 2026-05-20T05:18:02.747Z_

<details><summary>↩ Tool result · `toolu_01SR5CEc4JP9wPgMWzsfut96`</summary>

```text
Web search results for query: "joint judge bias contamination correction LLM-as-a-judge psychometric framework 2026"

Links: [{"title":"[2511.21140] How to Correctly Report LLM-as-a-Judge Evaluations","url":"https://arxiv.org/abs/2511.21140"},{"title":"How to Correctly Report LLM-as-a-Judge Evaluations","url":"https://arxiv.org/pdf/2511.21140"},{"title":"How to Correctly Report LLM-as-a-Judge Evaluations","url":"https://arxiv.org/html/2511.21140v3"},{"title":"LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data","url":"https://labelyourdata.com/articles/llm-as-a-judge"},{"title":"Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2506.22316v1"},{"title":"Assistant-Guided Mitigation of Teacher Preference Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2505.19176"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.02736v1"}]

Based on the search results, I found several highly relevant papers and resources addressing your query about LLM-as-a-judge bias, contamination correction, and related frameworks from 2026:

## Key Findings:

**Bias Correction Framework (February 2026)**

The imperfect sensitivity and specificity of LLM judges induce bias in naive evaluation scores, and a plug-in framework has been proposed that corrects this bias and enables statistically principled uncertainty quantification. The framework constructs confidence intervals that account for uncertainty from both the test dataset and a human-labeled calibration dataset, and uses an adaptive strategy to allocate calibration samples for tighter intervals.

**Robustness to Distribution Shift**

Existing methods can become biased under distribution shift between the test and calibration datasets, which can arise in LLM-as-a-judge settings, while an estimator based on the method of Rogan & Gladen (1978) remains unbiased under such shifts.

**Related Approaches**

A framework called AGDe-Judge incorporates an additional assistant model to complement training data, introducing a three-stage framework designed to debias from both labels and feedbacks, effectively reducing teacher preference bias while maintaining strong performance across evaluation benchmarks.

**Bias Quantification**

A framework called Calm identifies 12 key potential biases and systematically quantifies and analyzes each type of bias in LLM-as-a-Judge using automated and principle-guided modification.

These papers appear to represent the cutting edge of research on addressing bias and contamination issues in LLM-as-a-judge systems as of early 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ea96a2d-528b-4ca0-a516-5263e8d41204",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "d36794cd-1192-46b6-8686-298d642bcbc8",
  "toolUseResult": {
    "query": "joint judge bias contamination correction LLM-as-a-judge psychometric framework 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013GE6cvqFiqQkccJbLEdsyS",
        "content": [
          {
            "title": "[2511.21140] How to Correctly Report LLM-as-a-Judge Evaluations",
            "url": "https://arxiv.org/abs/2511.21140"
          },
          {
            "title": "How to Correctly Report LLM-as-a-Judge Evaluations",
            "url": "https://arxiv.org/pdf/2511.21140"
          },
          {
            "title": "How to Correctly Report LLM-as-a-Judge Evaluations",
            "url": "https://arxiv.org/html/2511.21140v3"
          },
          {
            "title": "LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data",
            "url": "https://labelyourdata.com/articles/llm-as-a-judge"
          },
          {
            "title": "Evaluating Scoring Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2506.22316v1"
          },
          {
            "title": "Assistant-Guided Mitigation of Teacher Preference Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2505.19176"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2410.02736v1"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers and resources addressing your query about LLM-as-a-judge bias, contamination correction, and related frameworks from 2026:\n\n## Key Findings:\n\n**Bias Correction Framework (February 2026)**\n\nThe imperfect sensitivity and specificity of LLM judges induce bias in naive evaluation scores, and a plug-in framework has been proposed that corrects this bias and enables statistically principled uncertainty quantification. The framework constructs confidence intervals that account for uncertainty from both the test dataset and a human-labeled calibration dataset, and uses an adaptive strategy to allocate calibration samples for tighter intervals.\n\n**Robustness to Distribution Shift**\n\nExisting methods can become biased under distribution shift between the test and calibration datasets, which can arise in LLM-as-a-judge settings, while an estimator based on the method of Rogan & Gladen (1978) remains unbiased under such shifts.\n\n**Related Approaches**\n\nA framework called AGDe-Judge incorporates an additional assistant model to complement training data, introducing a three-stage framework designed to debias from both labels and feedbacks, effectively reducing teacher preference bias while maintaining strong performance across evaluation benchmarks.\n\n**Bias Quantification**\n\nA framework called Calm identifies 12 key potential biases and systematically quantifies and analyzes each type of bias in LLM-as-a-Judge using automated and principle-guided modification.\n\nThese papers appear to represent the cutting edge of research on addressing bias and contamination issues in LLM-as-a-judge systems as of early 2026."
    ],
    "durationSeconds": 8.328277912999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6ea96a2d-528b-4ca0-a516-5263e8d41204",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T05:18:02.802Z_

<details><summary>↩ Tool result · `toolu_01MPUH137HncFNnQ8pweLiZM`</summary>

```text
Web search results for query: "Fiedler LLM judge bias sign-reversal arXiv 2605.06939 2026"

Links: [{"title":"[2605.06939] Bias and Uncertainty in LLM-as-a-Judge Estimation","url":"https://arxiv.org/abs/2605.06939"},{"title":"Bias and Uncertainty in LLM-as-a-Judge Estimation","url":"https://arxiv.org/html/2605.06939"},{"title":"Evaluating and Mitigating LLM-as-a-judge Bias in Communication Systems","url":"https://arxiv.org/html/2510.12462v3"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"Contrastive Decoding Mitigates Score Range Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2510.18196"},{"title":"Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2506.22316"},{"title":"Evaluating and Mitigating LLM-as-a-judge Bias in Communication Systems","url":"https://arxiv.org/pdf/2510.12462"}]

Based on the search results, I found the paper you're looking for:

"Bias and Uncertainty in LLM-as-a-Judge Estimation" is a paper by James Fiedler from Indeed Inc., published on May 7, 2026 (arXiv:2605.06939).

The paper addresses how characterizing performance via raw judge outputs is systematically biased, and notes that while recent work has proposed estimators to correct this bias, their reliability depends critically on judge quality and calibration stability. 

A key finding is that sharing calibration across compared models can introduce severe bias, including cases where the comparison estimate points in the wrong direction with high apparent confidence.

The authors study these failure modes through analytical results, simulations over judge quality and cross-model calibration instability, and a real-data MMLU-Pro case study with sign reversal. They propose judge quality and calibration instability as diagnostics for when corrected estimates are likely unreliable.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af7c29cb-2d5f-4621-8a32-d0a3dacd6c15",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "aed54cd0-f09c-4717-8a00-bab4b0dccab5",
  "toolUseResult": {
    "query": "Fiedler LLM judge bias sign-reversal arXiv 2605.06939 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BCySCMy1Ji11rTSWe6wADs",
        "content": [
          {
            "title": "[2605.06939] Bias and Uncertainty in LLM-as-a-Judge Estimation",
            "url": "https://arxiv.org/abs/2605.06939"
          },
          {
            "title": "Bias and Uncertainty in LLM-as-a-Judge Estimation",
            "url": "https://arxiv.org/html/2605.06939"
          },
          {
            "title": "Evaluating and Mitigating LLM-as-a-judge Bias in Communication Systems",
            "url": "https://arxiv.org/html/2510.12462v3"
          },
          {
            "title": "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2509.26072"
          },
          {
            "title": "Contrastive Decoding Mitigates Score Range Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2510.18196"
          },
          {
            "title": "Evaluating Scoring Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2506.22316"
          },
          {
            "title": "Evaluating and Mitigating LLM-as-a-judge Bias in Communication Systems",
            "url": "https://arxiv.org/pdf/2510.12462"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Bias and Uncertainty in LLM-as-a-Judge Estimation\" is a paper by James Fiedler from Indeed Inc., published on May 7, 2026 (arXiv:2605.06939).\n\nThe paper addresses how characterizing performance via raw judge outputs is systematically biased, and notes that while recent work has proposed estimators to correct this bias, their reliability depends critically on judge quality and calibration stability. \n\nA key finding is that sharing calibration across compared models can introduce severe bias, including cases where the comparison estimate points in the wrong direction with high apparent confidence.\n\nThe authors study these failure modes through analytical results, simulations over judge quality and cross-model calibration instability, and a real-data MMLU-Pro case study with sign reversal. They propose judge quality and calibration instability as diagnostics for when corrected estimates are likely unreliable."
    ],
    "durationSeconds": 7.334452936000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "af7c29cb-2d5f-4621-8a32-d0a3dacd6c15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T05:18:06.400Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've gathered initial information. Let me now search for more specific papers that are directly relevant to this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aed54cd0-f09c-4717-8a00-bab4b0dccab5",
  "isSidechain": false,
  "requestId": "req_011CbDFk7L7Yrbzdkt9pBzUS",
  "type": "assistant",
  "uuid": "829b56d5-8193-445b-af43-a2cec5082dd9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165dRycaQSdxRtus2PUY3HH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 21828,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21828,
          "cache_creation_input_tokens": 4052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4052
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

_source line 26 · 2026-05-20T05:18:07.400Z_

Good, I have initial results. Let me do a few more targeted searches to fill gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "829b56d5-8193-445b-af43-a2cec5082dd9",
  "isSidechain": false,
  "requestId": "req_011CbDFk7L7Yrbzdkt9pBzUS",
  "type": "assistant",
  "uuid": "c94dd15f-bf25-4df4-9893-473ff745a228",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165dRycaQSdxRtus2PUY3HH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 21828,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21828,
          "cache_creation_input_tokens": 4052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4052
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

_source line 27 · 2026-05-20T05:18:08.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013J2yzcojtqVRrWdso9uDYv`</summary>

```json
{
  "query": "CyclicJudge round-robin LLM judge bias elimination 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c94dd15f-bf25-4df4-9893-473ff745a228",
  "isSidechain": false,
  "requestId": "req_011CbDFk7L7Yrbzdkt9pBzUS",
  "type": "assistant",
  "uuid": "d6076507-4cbe-4c9e-afa4-a536ecfa903b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165dRycaQSdxRtus2PUY3HH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 21828,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21828,
          "cache_creation_input_tokens": 4052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4052
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

_source line 28 · 2026-05-20T05:18:08.922Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TN51LVQqNAnihef8JZ1U8Z`</summary>

```json
{
  "query": "DCR Factor data contamination correction LLM EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6076507-4cbe-4c9e-afa4-a536ecfa903b",
  "isSidechain": false,
  "requestId": "req_011CbDFk7L7Yrbzdkt9pBzUS",
  "type": "assistant",
  "uuid": "33eb1513-6117-4f22-b8b5-02642287ddbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165dRycaQSdxRtus2PUY3HH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 21828,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21828,
          "cache_creation_input_tokens": 4052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4052
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

_source line 29 · 2026-05-20T05:18:09.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lj6irectqPU9cy22Dex53t`</summary>

```json
{
  "query": "UDA unsupervised debiasing alignment LLM judges AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33eb1513-6117-4f22-b8b5-02642287ddbe",
  "isSidechain": false,
  "requestId": "req_011CbDFk7L7Yrbzdkt9pBzUS",
  "type": "assistant",
  "uuid": "8ea5f1cf-9c41-48ca-a427-6ab8d2873347",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165dRycaQSdxRtus2PUY3HH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 21828,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21828,
          "cache_creation_input_tokens": 4052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4052
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

_source line 30 · 2026-05-20T05:18:10.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UTHB1GGTjEPvx5yX5jH83i`</summary>

```json
{
  "query": "IRT item response theory LLM benchmark evaluation numerical instability 2026 arXiv 2605.07046"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ea5f1cf-9c41-48ca-a427-6ab8d2873347",
  "isSidechain": false,
  "requestId": "req_011CbDFk7L7Yrbzdkt9pBzUS",
  "type": "assistant",
  "uuid": "f6912ec6-2f45-4472-92b7-8eeeb3d76158",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165dRycaQSdxRtus2PUY3HH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4052,
      "cache_read_input_tokens": 21828,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 21828,
          "cache_creation_input_tokens": 4052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4052
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

_source line 31 · 2026-05-20T05:18:15.543Z_

<details><summary>↩ Tool result · `toolu_01TN51LVQqNAnihef8JZ1U8Z`</summary>

```text
Web search results for query: "DCR Factor data contamination correction LLM EMNLP 2025"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/pdf/2507.11405"},{"title":"[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/abs/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/html/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"}]

Based on the search results, here's information about the DCR Factor and data contamination correction for LLMs at EMNLP 2025:

## Overview

The Data Contamination Risk (DCR) framework is a lightweight, interpretable pipeline designed to detect and quantify benchmark data contamination (BDC) risk across four granular levels: semantic, informational, data, and label.

## The DCR Factor

By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance. The DCR Factor is a novel metric that quantifies BDC risk more intuitively during benchmark evaluations.

## Validation Results

The DCR framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, with accuracy adjusted using the DCR Factor to within 4% average error across the three benchmarks compared to the uncontaminated baseline.

## Key Features

The DCR framework not only detects hidden contamination signals but also calibrates evaluation metrics to counterbalance memorization effects, with the quantitative adjustments provided by the DCR Factor resulting in more robust and fair evaluation of model's real generalization.

The paper was presented at EMNLP 2025 in November 2025 and is available through the ACL Anthology and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33eb1513-6117-4f22-b8b5-02642287ddbe",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "d58b6fe8-d7dc-4bc5-b76d-a4c25199bee0",
  "toolUseResult": {
    "query": "DCR Factor data contamination correction LLM EMNLP 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_016qgBQZbmrrt1JfxT8hXrqX",
        "content": [
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1173/"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/pdf/2507.11405"
          },
          {
            "title": "[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/abs/2507.11405"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/html/2507.11405"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://aclanthology.org/2025.emnlp-main.1173.pdf"
          }
        ]
      },
      "Based on the search results, here's information about the DCR Factor and data contamination correction for LLMs at EMNLP 2025:\n\n## Overview\n\nThe Data Contamination Risk (DCR) framework is a lightweight, interpretable pipeline designed to detect and quantify benchmark data contamination (BDC) risk across four granular levels: semantic, informational, data, and label.\n\n## The DCR Factor\n\nBy synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance. The DCR Factor is a novel metric that quantifies BDC risk more intuitively during benchmark evaluations.\n\n## Validation Results\n\nThe DCR framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, with accuracy adjusted using the DCR Factor to within 4% average error across the three benchmarks compared to the uncontaminated baseline.\n\n## Key Features\n\nThe DCR framework not only detects hidden contamination signals but also calibrates evaluation metrics to counterbalance memorization effects, with the quantitative adjustments provided by the DCR Factor resulting in more robust and fair evaluation of model's real generalization.\n\nThe paper was presented at EMNLP 2025 in November 2025 and is available through the ACL Anthology and arXiv."
    ],
    "durationSeconds": 6.6171652260000045,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "33eb1513-6117-4f22-b8b5-02642287ddbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T05:18:16.618Z_

<details><summary>↩ Tool result · `toolu_013J2yzcojtqVRrWdso9uDYv`</summary>

```text
Web search results for query: "CyclicJudge round-robin LLM judge bias elimination 2026 arXiv"

Links: [{"title":"[2603.01865] CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/abs/2603.01865"},{"title":"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/pdf/2603.01865"},{"title":"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation","url":"https://arxiv.org/html/2603.01865"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/abs/2604.23178"}]

I found the paper! Here are the search results:

CyclicJudge is a round-robin assignment of judges that is demonstrated to be the optimal allocation strategy, eliminating bias precisely while requiring each judge only once per cycle, maintaining the cost of single-judge evaluation.

The paper, authored by Ziyi Zhu, Olivier Tieleman, Alexey Bukhtiyarov, and Jinghong Chen, addresses how LLM-as-judge evaluation has become standard practice for open-ended model assessment, though judges exhibit systematic biases that cannot be eliminated by increasing the number of scenarios or generations.

The work introduces a variance decomposition partitioning benchmark score variance into components, and based on this analysis, CyclicJudge demonstrates optimal strategy for a fixed judge-call budget, eliminating bias precisely while requiring each judge only once per cycle.

Empirical results on MT-Bench and MindEval validate the effectiveness of CyclicJudge across both general-purpose and domain-specific evaluation settings.

The paper was published on arXiv on March 2, 2026 (arXiv ID: 2603.01865).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6076507-4cbe-4c9e-afa4-a536ecfa903b",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "cab86c7b-b0f7-4843-a500-c390379b34a2",
  "toolUseResult": {
    "query": "CyclicJudge round-robin LLM judge bias elimination 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DABzgXXnX8q1Xq3FhNiQPu",
        "content": [
          {
            "title": "[2603.01865] CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation",
            "url": "https://arxiv.org/abs/2603.01865"
          },
          {
            "title": "CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation",
            "url": "https://arxiv.org/pdf/2603.01865"
          },
          {
            "title": "CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation",
            "url": "https://arxiv.org/html/2603.01865"
          },
          {
            "title": "The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2509.26072"
          },
          {
            "title": "[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/abs/2604.23178"
          }
        ]
      },
      "I found the paper! Here are the search results:\n\nCyclicJudge is a round-robin assignment of judges that is demonstrated to be the optimal allocation strategy, eliminating bias precisely while requiring each judge only once per cycle, maintaining the cost of single-judge evaluation.\n\nThe paper, authored by Ziyi Zhu, Olivier Tieleman, Alexey Bukhtiyarov, and Jinghong Chen, addresses how LLM-as-judge evaluation has become standard practice for open-ended model assessment, though judges exhibit systematic biases that cannot be eliminated by increasing the number of scenarios or generations.\n\nThe work introduces a variance decomposition partitioning benchmark score variance into components, and based on this analysis, CyclicJudge demonstrates optimal strategy for a fixed judge-call budget, eliminating bias precisely while requiring each judge only once per cycle.\n\nEmpirical results on MT-Bench and MindEval validate the effectiveness of CyclicJudge across both general-purpose and domain-specific evaluation settings.\n\nThe paper was published on arXiv on March 2, 2026 (arXiv ID: 2603.01865)."
    ],
    "durationSeconds": 8.246705643,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d6076507-4cbe-4c9e-afa4-a536ecfa903b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T05:18:17.043Z_

<details><summary>↩ Tool result · `toolu_01UTHB1GGTjEPvx5yX5jH83i`</summary>

```text
Web search results for query: "IRT item response theory LLM benchmark evaluation numerical instability 2026 arXiv 2605.07046"

Links: [{"title":"[2605.07046] An Interpretable and Scalable Framework for Evaluating Large Language Models","url":"https://arxiv.org/abs/2605.07046"},{"title":"An Interpretable and Scalable Framework for Evaluating Large Language Models","url":"https://arxiv.org/html/2605.07046"},{"title":"Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory","url":"https://arxiv.org/html/2605.00238"},{"title":"[2605.00238] Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory","url":"https://arxiv.org/abs/2605.00238"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"}]

The search found the paper you're looking for. Here's what I found:

Item Response Theory (IRT) offers a principled framework for modeling latent model abilities and item characteristics, but conventional methods are computationally expensive and numerically unstable, limiting large-scale implementations. 

Traditional IRT-based evaluation methods that rely on the expectation-maximization (EM) algorithm suffer from critical limitations, most notably computational inefficiency and numerical instability, with performance extremely sensitive to singular data configurations such as near-constant responses and collinearity.

To address these challenges, the paper proposes an interpretable and scalable framework for LLM evaluation based on the majorization-minimization principle, reformulating the problem as a sequence of constrained matrix factorization subproblems to enable stable and efficient parameter estimation with theoretical guarantees for identifiability and convergence.

The experiments on synthetic and real-world datasets, including MATH-500 and six Open LLM Leaderboard benchmarks, demonstrate that the method achieves superior scalability and interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6912ec6-2f45-4472-92b7-8eeeb3d76158",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "81435375-d342-48b3-853f-e2add0e70683",
  "toolUseResult": {
    "query": "IRT item response theory LLM benchmark evaluation numerical instability 2026 arXiv 2605.07046",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PtfsPWBDfMo3Z84Ah3HepK",
        "content": [
          {
            "title": "[2605.07046] An Interpretable and Scalable Framework for Evaluating Large Language Models",
            "url": "https://arxiv.org/abs/2605.07046"
          },
          {
            "title": "An Interpretable and Scalable Framework for Evaluating Large Language Models",
            "url": "https://arxiv.org/html/2605.07046"
          },
          {
            "title": "Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory",
            "url": "https://arxiv.org/html/2605.00238"
          },
          {
            "title": "[2605.00238] Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory",
            "url": "https://arxiv.org/abs/2605.00238"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/pdf/2505.15055"
          },
          {
            "title": "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory",
            "url": "https://arxiv.org/pdf/2602.00521"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v2"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/pdf/2511.04689"
          }
        ]
      },
      "The search found the paper you're looking for. Here's what I found:\n\nItem Response Theory (IRT) offers a principled framework for modeling latent model abilities and item characteristics, but conventional methods are computationally expensive and numerically unstable, limiting large-scale implementations. \n\nTraditional IRT-based evaluation methods that rely on the expectation-maximization (EM) algorithm suffer from critical limitations, most notably computational inefficiency and numerical instability, with performance extremely sensitive to singular data configurations such as near-constant responses and collinearity.\n\nTo address these challenges, the paper proposes an interpretable and scalable framework for LLM evaluation based on the majorization-minimization principle, reformulating the problem as a sequence of constrained matrix factorization subproblems to enable stable and efficient parameter estimation with theoretical guarantees for identifiability and convergence.\n\nThe experiments on synthetic and real-world datasets, including MATH-500 and six Open LLM Leaderboard benchmarks, demonstrate that the method achieves superior scalability and interpretability."
    ],
    "durationSeconds": 6.389460631999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f6912ec6-2f45-4472-92b7-8eeeb3d76158",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation  ## Descr…",
  "leafUuid": "81435375-d342-48b3-853f-e2add0e70683",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint judge bias and contamination correction via gated Rasch model",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

### Tool result

_source line 36 · 2026-05-20T05:18:19.042Z_

<details><summary>↩ Tool result · `toolu_01Lj6irectqPU9cy22Dex53t`</summary>

```text
Web search results for query: "UDA unsupervised debiasing alignment LLM judges AAAI 2026"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"}]

I found the paper! Here's what I found:

"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge" was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 40(41), 34854–34861.

The paper addresses preference bias in pairwise LLM evaluation, where judges systematically favor certain outputs and this bias leads to inconsistent and skewed rankings across different judges.

UDA is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where a compact neural network learns to adaptively set the K-factor and refine win probabilities. It operates in a fully unsupervised manner, guided solely by minimizing the dispersion among the Elo trajectories of all judges, forcing an alignment towards a collective consensus which serves as an unsupervised proxy for more stable and reproducible evaluation.

The paper is authored by Zhang, Y., Wang, C., Wu, L., Yu, W., Wang, Y., Bao, G., & Tang, J.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ea5f1cf-9c41-48ca-a427-6ab8d2873347",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "5862e05e-9e4f-438b-8632-fe61160d05e3",
  "toolUseResult": {
    "query": "UDA unsupervised debiasing alignment LLM judges AAAI 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RwigBnUtgUZXqVmXj7rLZR",
        "content": [
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2508.09724"
          },
          {
            "title": "(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"
          },
          {
            "title": "[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2508.09724"
          }
        ]
      },
      "I found the paper! Here's what I found:\n\n\"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge\" was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 40(41), 34854–34861.\n\nThe paper addresses preference bias in pairwise LLM evaluation, where judges systematically favor certain outputs and this bias leads to inconsistent and skewed rankings across different judges.\n\nUDA is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where a compact neural network learns to adaptively set the K-factor and refine win probabilities. It operates in a fully unsupervised manner, guided solely by minimizing the dispersion among the Elo trajectories of all judges, forcing an alignment towards a collective consensus which serves as an unsupervised proxy for more stable and reproducible evaluation.\n\nThe paper is authored by Zhang, Y., Wang, C., Wu, L., Yu, W., Wang, Y., Bao, G., & Tang, J."
    ],
    "durationSeconds": 9.121958081,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8ea5f1cf-9c41-48ca-a427-6ab8d2873347",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-20T05:18:19.046Z_

```json
{
  "parentUuid": "5862e05e-9e4f-438b-8632-fe61160d05e3",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e5a82b66-6504-4664-b3fa-3dbe33ca03de",
  "timestamp": "2026-05-20T05:18:19.046Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-20T05:18:23.718Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the landscape. Let me also search for the Preference Leakage paper and the MFRM applied to LLM raters paper to complete my picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5a82b66-6504-4664-b3fa-3dbe33ca03de",
  "isSidechain": false,
  "requestId": "req_011CbDFmJiFWkCMQfh22sjsv",
  "type": "assistant",
  "uuid": "dd161f19-5d74-45fe-9b41-aeab19ebdd65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3tLXcMF3R6cgZ2ceHrvaj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 673,
      "cache_creation_input_tokens": 2238,
      "cache_read_input_tokens": 25880,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 673,
          "output_tokens": 281,
          "cache_read_input_tokens": 25880,
          "cache_creation_input_tokens": 2238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2238
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

_source line 39 · 2026-05-20T05:18:24.235Z_

Let me do one more round of searches to complete the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd161f19-5d74-45fe-9b41-aeab19ebdd65",
  "isSidechain": false,
  "requestId": "req_011CbDFmJiFWkCMQfh22sjsv",
  "type": "assistant",
  "uuid": "efbb2010-1e95-4dbc-919c-bfc6dc896182",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3tLXcMF3R6cgZ2ceHrvaj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 673,
      "cache_creation_input_tokens": 2238,
      "cache_read_input_tokens": 25880,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 673,
          "output_tokens": 281,
          "cache_read_input_tokens": 25880,
          "cache_creation_input_tokens": 2238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2238
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

_source line 40 · 2026-05-20T05:18:25.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016zceHChjxCEEpwxB5rKwsc`</summary>

```json
{
  "query": "Preference Leakage contamination LLM-as-a-judge ICLR 2026 arXiv 2502.01534"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efbb2010-1e95-4dbc-919c-bfc6dc896182",
  "isSidechain": false,
  "requestId": "req_011CbDFmJiFWkCMQfh22sjsv",
  "type": "assistant",
  "uuid": "ca669efd-1760-4ee1-abff-885483c141b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3tLXcMF3R6cgZ2ceHrvaj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 673,
      "cache_creation_input_tokens": 2238,
      "cache_read_input_tokens": 25880,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 673,
          "output_tokens": 281,
          "cache_read_input_tokens": 25880,
          "cache_creation_input_tokens": 2238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2238
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

_source line 41 · 2026-05-20T05:18:26.252Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GTMXKo4LYCCCUxwzf7j7Q9`</summary>

```json
{
  "query": "MFRM LLM raters arXiv 2505.18486 comparing human AI rater effects many-facet Rasch"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca669efd-1760-4ee1-abff-885483c141b7",
  "isSidechain": false,
  "requestId": "req_011CbDFmJiFWkCMQfh22sjsv",
  "type": "assistant",
  "uuid": "d7b0f16f-568d-4199-9fdb-e615adc70136",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3tLXcMF3R6cgZ2ceHrvaj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 673,
      "cache_creation_input_tokens": 2238,
      "cache_read_input_tokens": 25880,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 673,
          "output_tokens": 281,
          "cache_read_input_tokens": 25880,
          "cache_creation_input_tokens": 2238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2238
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

_source line 42 · 2026-05-20T05:18:27.156Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019zSqwKuYPkPzJZ76qhVuws`</summary>

```json
{
  "query": "Bias-Bounded Evaluation LLM judges provably unbiased arXiv 2603.05485"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7b0f16f-568d-4199-9fdb-e615adc70136",
  "isSidechain": false,
  "requestId": "req_011CbDFmJiFWkCMQfh22sjsv",
  "type": "assistant",
  "uuid": "8cfe051c-0a3c-4972-955e-ff088aef478d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3tLXcMF3R6cgZ2ceHrvaj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 673,
      "cache_creation_input_tokens": 2238,
      "cache_read_input_tokens": 25880,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 673,
          "output_tokens": 281,
          "cache_read_input_tokens": 25880,
          "cache_creation_input_tokens": 2238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2238
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

_source line 43 · 2026-05-20T05:18:31.479Z_

<details><summary>↩ Tool result · `toolu_016zceHChjxCEEpwxB5rKwsc`</summary>

```text
Web search results for query: "Preference Leakage contamination LLM-as-a-judge ICLR 2026 arXiv 2502.01534"

Links: [{"title":"[Paper Note] Preference Leakage: A Contamination Problem in LLM-as-a-judge - 📚 AI Paper Notes","url":"https://en.papernotes.org/ICLR2026/llm_evaluation/preference_leakage_a_contamination_problem_in_llm-as-a-judge/"},{"title":"[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534"},{"title":"[2502.01534v1] Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/abs/2502.01534v1"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge | Pap…","url":"https://www.opentrain.ai/papers/preference-leakage-a-contamination-problem-in-llm-as-a-judge--arxiv-2502.01534/"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://arxiv.org/html/2502.01534v3"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"(PDF) Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://www.researchgate.net/publication/388685541_Preference_Leakage_A_Contamination_Problem_in_LLM-as-a-judge"},{"title":"Preference Leakage: A Contamination Problem in LLM-as-a-judge","url":"https://howiehwong.github.io/preference_leakage.pdf"}]

Based on the search results, I found the paper you were looking for. Here's what the research is about:

## Preference Leakage: A Contamination Problem in LLM-as-a-Judge

The paper (arXiv:2502.01534) was submitted on February 3, 2025 and last revised on March 4, 2026, with authors including Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, and Huan Liu. The paper is being presented at ICLR 2026.

**Main Contribution:**

Large Language Models (LLMs) as judges and LLM-based data synthesis have emerged as two fundamental LLM-driven data annotation methods in model development, and while their combination significantly enhances the efficiency of model training and evaluation, little attention has been given to the potential contamination brought by this new model development paradigm.

The paper exposes preference leakage, a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators, defining three common relatednesses between data generator LLM and judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family.

**Empirical Findings:**

Through extensive experiments, the authors empirically confirm the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks.

The code repository is available at David-Li0406/Preference-Leakage on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca669efd-1760-4ee1-abff-885483c141b7",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "d734df4e-c018-4f16-8cf1-0ef3473347d0",
  "toolUseResult": {
    "query": "Preference Leakage contamination LLM-as-a-judge ICLR 2026 arXiv 2502.01534",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A5FYsdRVQu4NPQvTHJESbf",
        "content": [
          {
            "title": "[Paper Note] Preference Leakage: A Contamination Problem in LLM-as-a-judge - 📚 AI Paper Notes",
            "url": "https://en.papernotes.org/ICLR2026/llm_evaluation/preference_leakage_a_contamination_problem_in_llm-as-a-judge/"
          },
          {
            "title": "[2502.01534] Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://arxiv.org/abs/2502.01534"
          },
          {
            "title": "[2502.01534v1] Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://arxiv.org/abs/2502.01534v1"
          },
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as-a-judge | Pap…",
            "url": "https://www.opentrain.ai/papers/preference-leakage-a-contamination-problem-in-llm-as-a-judge--arxiv-2502.01534/"
          },
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://arxiv.org/html/2502.01534v3"
          },
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as- ...",
            "url": "https://arxiv.org/pdf/2502.01534"
          },
          {
            "title": "(PDF) Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://www.researchgate.net/publication/388685541_Preference_Leakage_A_Contamination_Problem_in_LLM-as-a-judge"
          },
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as-a-judge",
            "url": "https://howiehwong.github.io/preference_leakage.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you were looking for. Here's what the research is about:\n\n## Preference Leakage: A Contamination Problem in LLM-as-a-Judge\n\nThe paper (arXiv:2502.01534) was submitted on February 3, 2025 and last revised on March 4, 2026, with authors including Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, and Huan Liu. The paper is being presented at ICLR 2026.\n\n**Main Contribution:**\n\nLarge Language Models (LLMs) as judges and LLM-based data synthesis have emerged as two fundamental LLM-driven data annotation methods in model development, and while their combination significantly enhances the efficiency of model training and evaluation, little attention has been given to the potential contamination brought by this new model development paradigm.\n\nThe paper exposes preference leakage, a contamination problem in LLM-as-a-judge caused by the relatedness between the synthetic data generators and LLM-based evaluators, defining three common relatednesses between data generator LLM and judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family.\n\n**Empirical Findings:**\n\nThrough extensive experiments, the authors empirically confirm the bias of judges towards their related student models caused by preference leakage across multiple LLM baselines and benchmarks.\n\nThe code repository is available at David-Li0406/Preference-Leakage on GitHub."
    ],
    "durationSeconds": 6.221225901000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ca669efd-1760-4ee1-abff-885483c141b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T05:18:32.149Z_

<details><summary>↩ Tool result · `toolu_01GTMXKo4LYCCCUxwzf7j7Q9`</summary>

```text
Web search results for query: "MFRM LLM raters arXiv 2505.18486 comparing human AI rater effects many-facet Rasch"

Links: [{"title":"[2505.18486] Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model","url":"https://arxiv.org/abs/2505.18486"},{"title":"Many-facet Rasch measurement | 8 | Implications for rater-mediated lan","url":"https://www.taylorfrancis.com/chapters/edit/10.4324/9781315187815-8/many-facet-rasch-measurement-thomas-eckes"},{"title":"A Bayesian many-facet Rasch model with Markov modeling for rater severity drift - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/36284065/"},{"title":"(PDF) Many-facet Rasch measurement","url":"https://www.researchgate.net/publication/228465956_Many-facet_Rasch_measurement"},{"title":"A Bayesian many-facet Rasch model with Markov modeling for rater severity drift","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10615980/"},{"title":"A Bayesian many-facet Rasch model with Markov modeling for rater severity drift | Behavior Research Methods | Springer Nature Link","url":"https://link.springer.com/article/10.3758/s13428-022-01997-z"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=4175&show=2000"},{"title":"(PDF) Using Multi-Facet Rasch Model (MFRM) in Rater-Mediated Assessment","url":"https://www.academia.edu/66891875/Using_Multi_Facet_Rasch_Model_MFRM_in_Rater_Mediated_Assessment"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=1325&show=500"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model"

**Authors:** Hong Jiao, Dan Song, Won-Chan Lee

**Overview:** The paper explores large language models (LLMs) for automated scoring in low-stakes assessment.

**Study Design:** The study compared ten LLMs (ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, DeepSeek V3, and DeepSeek R1) with human expert raters in scoring two types of writing tasks.

**Methodology:** The accuracy of the holistic and analytic scores from LLMs compared with human raters was evaluated using Quadratic Weighted Kappa, intra-rater consistency across prompts was compared using Cronbach Alpha, and rater effects of LLMs were evaluated and compared with human raters using the Many-Facet Rasch model.

**Key Findings:** The results in general supported the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet with high scoring accuracy, better rater reliability, and less rater effects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7b0f16f-568d-4199-9fdb-e615adc70136",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "de3127ac-c7b9-445c-aefe-39a604837103",
  "toolUseResult": {
    "query": "MFRM LLM raters arXiv 2505.18486 comparing human AI rater effects many-facet Rasch",
    "results": [
      {
        "tool_use_id": "srvtoolu_018MUw1bRd4zgpMK9ayGE2Rq",
        "content": [
          {
            "title": "[2505.18486] Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model",
            "url": "https://arxiv.org/abs/2505.18486"
          },
          {
            "title": "Many-facet Rasch measurement | 8 | Implications for rater-mediated lan",
            "url": "https://www.taylorfrancis.com/chapters/edit/10.4324/9781315187815-8/many-facet-rasch-measurement-thomas-eckes"
          },
          {
            "title": "A Bayesian many-facet Rasch model with Markov modeling for rater severity drift - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/36284065/"
          },
          {
            "title": "(PDF) Many-facet Rasch measurement",
            "url": "https://www.researchgate.net/publication/228465956_Many-facet_Rasch_measurement"
          },
          {
            "title": "A Bayesian many-facet Rasch model with Markov modeling for rater severity drift",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10615980/"
          },
          {
            "title": "A Bayesian many-facet Rasch model with Markov modeling for rater severity drift | Behavior Research Methods | Springer Nature Link",
            "url": "https://link.springer.com/article/10.3758/s13428-022-01997-z"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-05?skip=4175&show=2000"
          },
          {
            "title": "(PDF) Using Multi-Facet Rasch Model (MFRM) in Rater-Mediated Assessment",
            "url": "https://www.academia.edu/66891875/Using_Multi_Facet_Rasch_Model_MFRM_in_Rater_Mediated_Assessment"
          },
          {
            "title": "Computation and Language May 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-05?skip=1325&show=500"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** \"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\"\n\n**Authors:** Hong Jiao, Dan Song, Won-Chan Lee\n\n**Overview:** The paper explores large language models (LLMs) for automated scoring in low-stakes assessment.\n\n**Study Design:** The study compared ten LLMs (ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, DeepSeek V3, and DeepSeek R1) with human expert raters in scoring two types of writing tasks.\n\n**Methodology:** The accuracy of the holistic and analytic scores from LLMs compared with human raters was evaluated using Quadratic Weighted Kappa, intra-rater consistency across prompts was compared using Cronbach Alpha, and rater effects of LLMs were evaluated and compared with human raters using the Many-Facet Rasch model.\n\n**Key Findings:** The results in general supported the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet with high scoring accuracy, better rater reliability, and less rater effects."
    ],
    "durationSeconds": 5.893412036000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d7b0f16f-568d-4199-9fdb-e615adc70136",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T05:18:33.480Z_

<details><summary>↩ Tool result · `toolu_019zSqwKuYPkPzJZ76qhVuws`</summary>

```text
Web search results for query: "Bias-Bounded Evaluation LLM judges provably unbiased arXiv 2603.05485"

Links: [{"title":"[2603.05485] Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/abs/2603.05485"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/html/2603.05485"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/pdf/2603.05485"},{"title":"LLM Judges: A Bias-Bounded Evaluation Framework (CS 2026) - Studocu","url":"https://www.studocu.com/in/document/chirec-international-school/mathematics-applications-and-interpretation-sl/llm-judges-a-bias-bounded-evaluation-framework-cs-2026/155334241"},{"title":"Evaluating Scoring Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2506.22316"}]

Based on the search results, I found the paper you're looking for:

## Paper Summary

The paper "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation" is authored by Benjamin Feuer (Stanford University/Oumi.AI), Lucas Rosenblatt (New York University), and Oussama Elachqar (Oumi.AI), submitted to arXiv on March 5, 2026.

### Main Contribution

The paper proposes average bias-boundedness (A-BB), an algorithmic framework which formally guarantees reductions of harm/impact as a result of any measurable bias in an LLM judge.

### Key Results

When evaluated on Arena-Hard-Auto with four LLM judges, they achieve (τ = 0.5, δ = 0.01)-bias-bounded guarantees while retaining 61–99% correlation with original rankings across formatting and schematic bias settings, with most judge-bias combinations exceeding 80%.

The code to reproduce their findings is available at https://github.com/penfever/bias-bounded-evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cfe051c-0a3c-4972-955e-ff088aef478d",
  "isSidechain": false,
  "promptId": "30acf6f5-c185-45e7-96d6-2b3e91769af5",
  "type": "user",
  "uuid": "1b8be29e-a5b7-42a8-a191-6c5783f575e5",
  "toolUseResult": {
    "query": "Bias-Bounded Evaluation LLM judges provably unbiased arXiv 2603.05485",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NAmGZvogaFgK3HMwwPCiUK",
        "content": [
          {
            "title": "[2603.05485] Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/abs/2603.05485"
          },
          {
            "title": "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/html/2603.05485"
          },
          {
            "title": "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/pdf/2603.05485"
          },
          {
            "title": "LLM Judges: A Bias-Bounded Evaluation Framework (CS 2026) - Studocu",
            "url": "https://www.studocu.com/in/document/chirec-international-school/mathematics-applications-and-interpretation-sl/llm-judges-a-bias-bounded-evaluation-framework-cs-2026/155334241"
          },
          {
            "title": "Evaluating Scoring Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2506.22316"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n## Paper Summary\n\nThe paper \"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation\" is authored by Benjamin Feuer (Stanford University/Oumi.AI), Lucas Rosenblatt (New York University), and Oussama Elachqar (Oumi.AI), submitted to arXiv on March 5, 2026.\n\n### Main Contribution\n\nThe paper proposes average bias-boundedness (A-BB), an algorithmic framework which formally guarantees reductions of harm/impact as a result of any measurable bias in an LLM judge.\n\n### Key Results\n\nWhen evaluated on Arena-Hard-Auto with four LLM judges, they achieve (τ = 0.5, δ = 0.01)-bias-bounded guarantees while retaining 61–99% correlation with original rankings across formatting and schematic bias settings, with most judge-bias combinations exceeding 80%.\n\nThe code to reproduce their findings is available at https://github.com/penfever/bias-bounded-evaluation."
    ],
    "durationSeconds": 6.321585714000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8cfe051c-0a3c-4972-955e-ff088aef478d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-20T05:19:27.603Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the landscape. Let me synthesize all this information and produce my evaluation.

Key observations from my research:

1. **The judge bias silo is very active**: CyclicJudge (March 2026), UDA (AAAI 2026), Bias-Bounded Evaluation (March 2026), Fiedler's diagnostics (May 2026), BiasScope (ICLR 2026), JudgeBiasBench, and the "Judging the Judges" survey (April 2026) all address judge bias from different angles.


2. **The contamination silo is equally vibrant**: DCR Factor (EMNLP 2025), ConStat (NeurIPS 2024), Preference Leakage (ICLR 2026), LogProber, and recent work on how RL post-training can obscure contamination signals are all pushing this area forward.
3. **IRT and MFRM frameworks are gaining traction for LLM evaluation**: Several papers from 2026 are applying these psychometric approaches to understand rater behavior and model performance more rigorously.
4. **The gap is real**: I haven't encountered any work that simultaneously models judge severity and contamination susceptibility within a unified psychometric framework—this genuinely appears to be an opening.
5. **DG-IRT's adaptation is novel**: The original framework detected test cheating through known item exposure, but applying it to LLM evaluation where exposure is unknown represents a meaningful methodological shift.

Looking at the proposal's strengths, the gap identification holds up well, the confounding between judge severity and contamination susceptibility is theoretically grounded, and the experimental setup is thorough with multiple baselines and ablations across a principled three-stage pipeline that distinguishes between examinee-side and judge-side contamination effects.

On the concerns side, the model's complexity across three stages with external anchoring and multiple exposure proxies might draw scrutiny about whether the gains justify the added machinery. ConStat's validity is particularly uncertain for open-ended tasks like Arena-Hard and WildBench despite the proposal's planned validity study, which represents a notable risk. The ground truth validation approach also needs careful consideration. Arena as the primary gold standard is problematic because:
   - Arena votes themselves may be biased or contaminated
   - The proposal acknowledges this with controlled contamination injection, which helps
   - But the primary metric is still Kendall-τ with Arena

4. **The confounding proposition**: The proposal claims to provide a "semi-formal proposition" with a "proof sketch in appendix." This could be seen as either a strength (mathematical rigor) or a weakness (not a full formal proof). For EMNLP, this level of formalization is probably adequate.

5. **Scale limitations**: 15-20 models with 8 judges is a relatively small sample size for psychometric modeling. The proposal doesn't deeply address how MCMC will behave with this small N.

6. **The rank-1 assumption**: The proposal acknowledges this limitation honestly, which is good. But reviewers might push back on whether this simplification is too severe for real-world contamination patterns.

7. **Three-stage vs. joint estimation**: The proposal argues for joint estimation but then uses a three-stage approach where e_i is fixed from external proxies in Stage 2. This isn't truly "joint" in the MLE/Bayesian sense—it's still sequential since Stage 2 feeds into Stage 3. Though I need to reconsider: the key distinction is that G-MFRM estimates bias and ability jointly with contamination in a single likelihood, whereas purely sequential approaches treat each stage's effects as noise. The fixation of e_i externally is a different kind of constraint than sequential estimation.

8. **Novelty depth**: The core model is straightforward—starting with MFRM's logit(P) = θ - b - d and adding a contamination term c·e with external proxies for e. It's elegant but conceptually moderate in novelty, with main contributions being the identification of the confounding problem, the external anchoring pipeline, and empirical validation.

**Overall Assessment:**

The proposal identifies a genuine gap and takes a principled, methodologically rigorous approach with thorough experimental design. For EMNLP 2026, the research question is timely, the method bridges measurement theory and NLP evaluation meaningfully, and the experimental completeness is above average. The main concerns are whether the added complexity justifies the gains over simpler alternatives like CyclicJudge, uncertainty around ConStat's validity on open-ended tasks, and the small sample size for psychometric estimation. I'd put this around 30-40% acceptance probability—it's solid and well-reasoned with genuine contributions, but the complexity and multiple assumptions introduce meaningful risk.

Reconsidering the estimate more carefully: the genuinely novel joint framework, the real insight about confounding, and the exceptionally comprehensive experimental design are significant strengths. But given EMNLP's typical 20-25% acceptance rate, a 35-45% probability does suggest this is well above average. The key question is whether the novelty and rigor of the confounding argument and experimental design truly outweigh the complexity concerns enough to justify that positioning.

The proactive acknowledgment of limitations actually strengthens the proposal, and the controlled contamination injection provides independent ground truth validation. The ablation design directly tests the core confounding hypothesis. Balancing these genuine strengths against the execution risks—particularly around Stage 2 external anchoring for open-ended tasks and the small psychometric sample—I'd estimate 32-42%, with a median around 37%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b8be29e-a5b7-42a8-a191-6c5783f575e5",
  "isSidechain": false,
  "requestId": "req_011CbDFnNSWsxUy4fa1HM4wA",
  "type": "assistant",
  "uuid": "ebf0f926-309d-433d-853a-1f420b7de3f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLTvtGUqsn96yZvCed8tEo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3431,
      "cache_read_input_tokens": 28118,
      "output_tokens": 7736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7736,
          "cache_read_input_tokens": 28118,
          "cache_creation_input_tokens": 3431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3431
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

_source line 47 · 2026-05-20T05:21:34.135Z_

Now I have sufficient information to produce a comprehensive evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- Fiedler, "Bias and Uncertainty in LLM-as-a-Judge Estimation" (arXiv:2605.06939, May 2026): 直接上游工作。提出 J/delta-J 诊断指标和 sign-reversal 失效模式（跨模型校准共享导致估计方向反转）。停留在经典测试理论（CTT）层面，未提供统一测量模型。G-MFRM 将 sign-reversal 定性为其 confounding proposition 的特例，合理。
- CyclicJudge (arXiv:2603.01865, March 2026): 通过 round-robin 评审分配消除 judge bias，MT-Bench/MindEval 验证有效。但完全忽略 contamination。是 proposal 的主要 baseline 之一。
- DCR Factor (EMNLP 2025, ACL Anthology): 通过 fuzzy inference 量化 benchmark contamination 并调整准确率，9 个 LLM 验证，误差 ~4%。但完全忽略 judge effects。是 proposal 的另一主要 baseline。
- ConStat (NeurIPS 2024): 基于 reference benchmark 比较的 contamination 统计检测，r²=0.94（factual benchmarks）。是 G-MFRM Stage 2 的核心外部锚定工具。在 open-ended generation tasks 上的有效性尚未验证——proposal 注意到此风险并规划了 validity study。
- Preference Leakage (ICLR 2026, arXiv:2502.01534): 量化 judge-side relatedness bias（generator-judge contamination），属于 judge 端污染而非 examinee 端。与 G-MFRM 建模的是机制上不同的现象——proposal 正确地做了区分。
- UDA (AAAI 2026): 神经 K-factor Elo 调整，降低 inter-judge SD 63.4%。无监督方式对齐多 judge Elo 轨迹。不涉及 contamination。
- Bias-Bounded Evaluation (arXiv:2603.05485, March 2026): 提供形式化的 (τ, δ)-bias-bounded 保证，Arena-Hard-Auto 上保持 61-99% ranking correlation。理论保证强但不建模 contamination。
- PSN-IRT (AAAI 2026): Neural 4PL IRT 用于 benchmark 分析，τ=0.9048 与 Arena。揭示 benchmark 中广泛的 contamination 和 measurement 问题。不涉及 judge facet。
- Jiao et al., "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model" (arXiv:2505.18486, May 2025): 将 MFRM 应用于 10 个 LLM rater 与人类 rater 的比较，评估打分准确性和 rater effects。仅诊断 rater effects，无 contamination 建模。是最直接的同方向前驱工作。
- Casabianca & Beiting-Parrish (arXiv:2602.22585, Feb 2026): MFRM 矫正人类 rater severity，聚焦人类评审，未涉及 contamination。
- arXiv:2605.07046 (May 2026): 识别 IRT 在 LLM evaluation 中的数值不稳定性，提出 majorization-minimization 解决方案。G-MFRM 通过 informative priors 和 warm-starting 应对此问题。
- Wang et al. (ICLR 2026): RL post-training 遮蔽 contamination 信号，对 contamination 检测构成挑战。G-MFRM 的 adversarial robustness ablation 针对此场景。

- 调研总结: LLM-as-a-judge 评估领域已形成明确的 judge bias 和 contamination detection 两个研究竖井，各有多项成熟工作。然而，**没有任何现有工作在单一心理测量框架中联合建模 judge severity 和 examinee-side contamination**——这一 gap 经调研确认属实。G-MFRM 的定位在现有文献格局中是独特的，填补了一个真实存在的方法论空白。

【整体印象】:
作为审稿人，我的第一反应是"这是一个认真、深入、且有真实 novelty 的工作"。Proposal 展现出对两个相关但分离的文献体系（judge bias correction 和 contamination detection）的深刻理解，并提出了一个理论上合理的统一框架。confounding argument 是一个真实的洞察——sequential correction 中 judge severity 和 contamination susceptibility 确实可能混淆——这不是人为制造的问题。实验设计异常详尽，9 个 baselines + 7 项 ablations + controlled contamination injection 远超平均水平。

但我也有顾虑：(1) 模型复杂度高，三阶段 pipeline 的每个环节都有假设和潜在失效点；(2) Stage 2 external anchoring 对 ConStat 在 open-ended tasks 上的有效性依赖较重，这是一个经验性赌注；(3) 15-20 个模型的样本量对心理测量建模偏小。总体倾向 weak accept / borderline。

【核心贡献】:
核心贡献有三层：
1. **问题识别（概念层面）**: 首次指出并形式化了 judge severity 与 contamination susceptibility 在 sequential estimation 中的 confounding 问题，将 Fiedler (2026) 的 sign-reversal 现象定性为此 confounding 的特例。
2. **方法论（技术层面）**: 设计 Gated MFRM (logit(P) = θ - b - d + c·e)，通过 multiplicative gating 将 DG-IRT 的 contamination 机制集成到 MFRM 中，并通过 external anchoring pipeline 解决 DG-IRT 在 LLM 领域的不可用问题（unknown exposure）。
3. **实践层面**: 产出多维可解释参数（c_n 用于 training pipeline 审计，d_j 用于 judge 选择，e_i 用于 benchmark item 退役）。

贡献的价值中等偏上。问题识别是最强的贡献——如果 confounding 问题确实在实践中导致显著偏差，这对整个 LLM evaluation 社区都有意义。方法论贡献扎实但不算突破性——本质上是将两个已有框架（MFRM + DG-IRT gating）组合，加上实用的 external anchoring。

【方法合理性】:
方法整体合理，但有几个需要审视的点：

**合理之处**:
- MFRM 是 rater-mediated assessment 的标准工具，用于 LLM judge modeling 有天然适配性
- Multiplicative gating c_n · e_i 遵循 LLTM/AMMI 传统，identifiability 有理论保证
- 三阶段估计中固定 e_i 进行 joint estimation 在技术上避免了 likelihood 中的不可识别性
- 将 DG-IRT 从 binary known exposure 扩展到 continuous unknown exposure 是必要且合理的适配

**潜在问题**:
1. **"Joint" 的程度**: Proposal 强调 joint estimation 的必要性，但 Stage 2 中 e_i 是独立于 MFRM likelihood 估计的（来自 ConStat/temporal/LogProber），然后在 Stage 3 中作为 fixed input。这实际上仍然是 partial sequential——只是 "joint" 的是 θ, b, d, c 四个参数（给定 e_i）。这与 proposal 批评的 fully sequential pipeline 有区别，但审稿人可能会质疑这是否真正消除了 confounding。回应：e_i 来自外部独立信号（不依赖 judge 评分），所以不存在 θ/d 与 e 的循环依赖，confounding argument 的核心（d_j 和 c_n·e_i 在 judge 评分中混淆）确实被解决了。这一辩护是合理的，但需要清晰表述。

2. **Rank-1 假设**: c_n 是标量意味着每个模型的 contamination susceptibility 跨 task domain 是同质的。Proposal 承认这是简化并提出了 person-fit 诊断来检测违反。但对于大型模型（如 DeepSeek-V4 可能在代码上高度 contaminated 但在推理上干净），这可能是严重的 misspecification。

3. **更简单的替代方案**: 一个审稿人可能会问——为什么不直接在 standard MFRM 中加入 contamination covariates 作为 fixed effects，而需要如此复杂的 gating 机制？回应：fixed effect 不能分离 per-model 和 per-item 的贡献（会有 N×I 参数的不可识别性），multiplicative decomposition 将其压缩为 N+I 参数。这一回应是有效的。

【5 维度打分】:

  1. 研究问题: [强] — 联合校正 judge bias 和 contamination 是一个真实存在的、尚未被解决的问题。两个研究竖井的存在经调研确认属实（CyclicJudge/UDA/Bias-Bounded 只做 judge bias；DCR/ConStat 只做 contamination），confounding 的理论论证合理（Fiedler 2026 的 sign-reversal 提供了实证支持）。这个问题对 LLM evaluation 社区有广泛意义，因为几乎所有 leaderboard 和 benchmark 都同时面临这两个问题。

  2. 方法与创新: [中] — 方法在技术上合理，但核心创新是两个已有框架（MFRM + DG-IRT gating）的组合。Multiplicative gating c_n·e_i 遵循成熟的 LLTM/AMMI 传统（Fischer 1973），不是全新的技术。真正的新贡献在于 external anchoring pipeline（用 ConStat+temporal+LogProber 估计 e_i）和 confounding 的形式化论证。与 Jiao et al. (arXiv:2505.18486) 相比，G-MFRM 增加了 contamination facet；与 DCR (EMNLP 2025) 相比，增加了 judge facet；与 DG-IRT (Psychometrika 2013) 相比，解决了 unknown exposure 问题。差异化清晰但深度属于 "thoughtful combination" 而非 "paradigm shift"。

  3. 实验设计: [强] — 这是 proposal 最突出的亮点。9 个 baselines（含 vanilla IRT 作为最基本参照）、7 项 ablations（含 sequential order-dependence 的三向比较，直接对应 Fiedler sign-reversal）、controlled contamination injection 提供独立于 Arena 的 ground truth、ConStat validity study 先行验证假设、parameter recovery simulation、convergence diagnostics protocol——这一实验设计的完备程度在同类 proposal 中属于上乘。与 PSN-IRT (AAAI 2026) 相比，baseline 覆盖更广；与 CyclicJudge 相比，增加了 contamination 维度的验证；与 DCR Factor (EMNLP 2025) 相比，增加了 judge facet 的对比。效率分析和 Pareto frontier 可视化也是加分项。

  4. 可行性: [中] — 资源估计（200-280 GPU hours, $500-700 + $900-1200 API, 11-13 weeks）在学术实验室范围内可行。但存在执行风险：(a) ConStat 在 open-ended tasks 上的有效性是核心赌注，如果 validity study 失败需要重新设计 Stage 2；(b) 15-20 models × 8 judges 的 MCMC convergence 在如此多参数下可能需要大量调试；(c) controlled contamination injection 需要 fine-tune open-weight models 并验证 contamination 效果，可能比预期耗时更多；(d) 同时依赖多家 proprietary API（GPT-5.5, Claude Opus 4.7, Gemini 2.5 Pro）增加了工程不确定性。

  5. 写作与呈现: [强] — Proposal 的组织结构清晰，从问题识别到方法设计到实验规划逻辑连贯。对已有工作的定位精准且公平（正确区分 Preference Leakage 的 judge-side vs. examinee-side contamination，准确描述 CyclicJudge/DCR 的局限性）。对自身局限性的坦诚（rank-1 假设、MT-Bench ceiling effects、ConStat open-ended validity）增强了可信度。文献覆盖极为全面，包含截至 2026 年 5 月的最新工作。唯一的呈现风险是论文版本中需要控制长度——如此多的内容压入 8 页正文可能导致关键细节不足。

【概率估计】: [30% - 42%] 中位 35%

【估计理由】:
向上的力量：(1) Gap 真实存在且经调研确认，no prior work 联合建模 judge severity + contamination；(2) confounding argument 是一个有理论价值的洞察；(3) 实验设计的完备程度显著高于同领域平均水平；(4) 话题高度时效（2026 年 LLM evaluation 是热点方向）。

向下的力量：(1) 核心方法论创新属于 "principled combination" 而非突破性技术贡献，两位审稿人中至少一位可能认为 novelty 不够 strong；(2) 三阶段 pipeline 的复杂度较高，reviewers 可能质疑是否 over-engineered；(3) 对 ConStat open-ended validity 的依赖引入了不可控风险——如果 validity study 结果不佳，整个 Stage 2 需要重新设计；(4) 心理测量背景的审稿人可能质疑 15-20 个 examinees 对 MFRM 的估计精度（传统 MFRM 研究通常有数百 examinees）；(5) 最终效果可能是 Kendall-τ 的小幅提升（如从 0.85 到 0.88），审稿人可能认为 improvement 不足以justify 复杂度。

综合：这是一篇 solid 的投稿，有真实贡献，但不属于"一定会中"的级别。中位 35% 反映了"方向正确、执行完备、但 novelty 深度和实证 impact 存在不确定性"的判断。

【主要风险】:
1. **Novelty 深度不足**: 核心模型 logit(P) = θ - b - d + c·e 的技术贡献被审稿人视为 "straightforward extension"——将已有的 MFRM 加上已有的 DG-IRT gating，缺乏足够的方法论深度来支撑 top venue。如果审稿人认为 confounding argument 只是 "well-known statistical principle applied to a new domain"，novelty 评分可能不利。
2. **Stage 2 External Anchoring 的脆弱性**: ConStat 在 factual benchmarks 上 r²=0.94 但在 open-ended generation（Arena-Hard, WildBench）上的表现未知；temporal signals 和 LogProber 的信号强度在最新模型上可能因 RL post-training (Wang et al., ICLR 2026) 而减弱。如果 ê_i 估计质量低，整个 c_n 估计都会受影响，导致 G-MFRM 相对于 simpler baselines 的优势消失。

【实施评估】:
  - 计算资源: 200-280 A100 GPU hours（中等规模），主要用于 judge inference (~130h) 和 ablations (~50h)。MCMC fitting 本身计算开销不大 (~25h)。需要 A100-80GB 以运行大型 open-weight 模型。
  - 数据需求: Arena-Hard (~500 prompts), WildBench, MT-Bench 均为公开数据集。需要 Chatbot Arena votes 作为 gold standard（可通过 LMSYS API 获取）。ConStat reference benchmarks 需要构建（rephrase/synthetic variants）。
  - 人工介入: ~$3,000-5,000 用于 100-150 prompts 的 human equivalence validation + ConStat validity study 的 annotator agreement（Fleiss' κ ≥ 0.7）。规模合理但需要管理 annotator quality。
  - 训练需求: 需要 fine-tune 2-3 个 open-weight models 进行 controlled contamination injection (~20h GPU)。不需要训练核心模型。MCMC fitting 使用 NumPyro，属于 inference 而非 training。
  - 新 Benchmark: 不构建新 benchmark，但需要为 ConStat 构建 reference benchmark variants（rephrased/synthetic）——这本身是一个非平凡的工作量。
  - 预估周期: 11-13 weeks。时间线紧凑但可行，前提是 ConStat validity study 不需要多轮迭代。最大瓶颈可能在 multi-judge data collection（需要运行 15-20 models × 8 judges × 多个 benchmarks）。
```

Sources:
- [Bias and Uncertainty in LLM-as-a-Judge Estimation (Fiedler, 2026)](https://arxiv.org/abs/2605.06939)
- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)
- [DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1173/)
- [ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)](https://arxiv.org/abs/2405.16281)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)](https://arxiv.org/abs/2502.01534)
- [UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/40788)
- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/abs/2603.05485)
- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486)
- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/40814)
- [An Interpretable and Scalable Framework for Evaluating Large Language Models](https://arxiv.org/abs/2605.07046)
- [How to Correctly Report LLM-as-a-Judge Evaluations](https://arxiv.org/abs/2511.21140)
- [Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178)
- [BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2602.09383)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf0f926-309d-433d-853a-1f420b7de3f0",
  "isSidechain": false,
  "requestId": "req_011CbDFnNSWsxUy4fa1HM4wA",
  "type": "assistant",
  "uuid": "01fcc88f-18dd-4c3d-a4f1-a12a6f4dcc64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLTvtGUqsn96yZvCed8tEo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3431,
      "cache_read_input_tokens": 28118,
      "output_tokens": 7736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7736,
          "cache_read_input_tokens": 28118,
          "cache_creation_input_tokens": 3431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3431
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

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation  ## Descr…",
  "leafUuid": "01fcc88f-18dd-4c3d-a4f1-a12a6f4dcc64",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint judge bias and contamination correction via gated Rasch model",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation  ## Descr…",
  "leafUuid": "01fcc88f-18dd-4c3d-a4f1-a12a6f4dcc64",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint judge bias and contamination correction via gated Rasch model",
  "sessionId": "977d3218-5d4c-413b-bde4-7aea9ef6099b"
}
```

---
