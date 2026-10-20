# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Real LLM annotations exhibit substantial misclassification heterogeneity on 

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/8c906e6c-7366-4d44-99bf-450a9e8cb9b4.jsonl`
- **Structured JSON:** [`56ce1710e470142739b3.json`](../../sessions/56/56ce1710e470142739b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:31:41.716Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:31:41.716Z",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Real LLM annotations exhibit substantial misclassification heterogeneity on CSS tasks; semi-synthetic and real-data experiments confirm bias mechanism at practical magnitudes; all three claims validated with explicit boundary conditions\n核心假设：['GPT-4.1 misclassification rates vary ≥0.12 (max−min) across text-feature subgroups on TweetEval sentiment', 'Semi-synthetic with real LLM labels replicates bias amplification ≥2x in majority of high-heterogeneity configs', 'EC-HTE RMSE competitive with global at n_expert ≥ 500 for K=4 (ratio ≤ 1.2)', 'Diagnostic criterion, after refinement (max-subgroup product or weighted aggregation), achieves cross-validated setting-level AUC ≥ 0.70', 'UC Berkeley hate speech real-data case study shows ≥1 subgroup with CATE shift > 2 SE between global and EC-HTE', 'ec_hte_ppci composition replicates near-zero bias on semi-synthetic with mixed covariate+outcome error']\n关键指标范围：{'semi_synth_llm_delta_pi': [0.12, 0.25], 'semi_synth_llm_bias_amplification_median': [2.0, 4.0], 'ec_hte_bias_reduction_pct_n500': [55, 80], 'ec_hte_rmse_ratio_n500_k4': [1.0, 1.2], 'diagnostic_cv_auc_setting': [0.7, 0.85], 'diagnostic_cv_auc_subgroup': [0.83, 0.95], 'real_data_max_cate_shift_se': [2.0, 5.0], 'coverage_ec_hte_95': [0.9, 0.97], 'ec_hte_ppci_bias_reduction_vs_ec_hte_dgpC': [80, 97]}\n叙事方向：Original framing fully intact. Lead with bias identity theorem (exact, R²≥0.97) and 'debiasing can hurt' proposition as problem-level discovery. Headline: 'global correction worsens subgroup CATE bias by 2-3x; EC-HTE reduces to near-zero with 250-500 expert labels.' Three claims at full strength with boundary conditions (n_expert/K ≥ 25, det(Ĉ_k) ≠ 0). Diagnostic criterion positioned as practitioner decision rule. EC-HTE+PPCI complementarity elevated in abstract. Paper structure standard: theory → method → synthetic → semi-synthetic (real LLM) → real data. exp-008/009 in appendix. Four main-text figures as planned.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ec_hte_llm_annotation\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 2-3x (median across configurations), with extreme cases exceeding 20x. Global correction increases subgroup-level bias in ~50% of the parameter space.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction in moderate-sized subgroups by borrowing strength across groups (classic James-Stein shrinkage). **Boundary condition**: when expert labels per subgroup < ~25 (e.g., n_expert=50 with 12% minority subgroup → ~6 labels) AND subgroup parameter is far from group mean, shrinkage can be harmful — stratified MLE is preferred. Recommended: n_expert such that smallest subgroup contains ≥25 expert labels. **NOTE**: exact improvement magnitudes pending full 100 MC confirmation (current estimates from n_mc=2 dry-run). Demonstrated with both difference-in-means and CausalForestDML (exp-011: consistent bias reduction pattern, ec_hte_forest |bias|=0.06 vs naive 0.16). CausalForest amplifies the debiasing-hurts effect (up to 5.9x in K=4/extreme) due to nonlinear CATE estimation.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis across computational social science (CSS) — e.g., sentiment framing moderates message effectiveness, hate speech type moderates intervention impact. LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education; documented across CSS tasks including sentiment, stance, toxicity). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as \"problem identification + principled solution\" not \"new estimation technique.\"\n\n- **Headline result template**: \"On semi-synthetic CSS benchmarks (sentiment analysis, hate speech detection), global correction worsens subgroup CATE bias by 2-3x (median), with up to 20x in extreme cases; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels.\"\n\n- **Oracle framing**: When reporting DGP C results where ec_hte_ppci outperforms oracle, always use \"covariate-oracle\" (true Z + observed Y), never unqualified \"oracle\". Frame as \"composite correction is necessary and sufficient when both error types coexist\" — NOT \"beats oracle\". The result is by construction (ec_hte_ppci corrects both error types; covariate-oracle only corrects one), not surprising.\n\n## Key Contributions (ordered for paper)\n\n1. **Bias decomposition identity**: Exact population-level identity: bias ∝ misclassification heterogeneity × CATE heterogeneity (Δπ×Δτ product form). NOT a bound — it is an exact identity under A1–A4; finite-sample R² measures MC noise, not bound looseness. Includes \"debiasing can hurt\" proposition with constructive example. Frame as \"bias decomposition\" or \"bias identity\" throughout — never \"bias bound.\" (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **EC-HTE + PPCI complementarity**: EC-HTE is a structured correction exploiting mixing matrix structure for covariate-side error; PPCI rectifier is a general-purpose residual correction that captures any systematic error (including outcome-side). They are complementary, not orthogonal — PPCI alone can partially correct covariate error but less efficiently than M⁻¹; in composition, EC-HTE handles the structured covariate error precisely, and the residual rectifier handles remaining outcome error. Composition achieves best-of-both when both error types are present. Elevate in abstract and contributions list. (Method + Empirical)\n5. **Comprehensive validation**: Synthetic + semi-synthetic + real-data case study (pattern consistency, not ground-truth benchmark) with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI / DSL?\"** — PPCI rectifier is a general-purpose correction that captures any systematic error (covariate + outcome); EC-HTE is a structured correction exploiting mixing matrix structure specifically for covariate-side error. They are complementary: EC-HTE alone is more efficient for covariate error (uses M⁻¹ structure), PPCI alone can partially correct covariate error but with higher variance (limited by gold subset). In composition, EC-HTE handles structured covariate error, residual rectifier handles outcome error. DSL applied per-subgroup is a valid baseline but lacks cross-subgroup shrinkage, operates at estimand level rather than measurement model level, and has strictly higher variance under partial pooling. Do NOT say \"DSL cannot do subgroup correction\" — say it lacks the principled shrinkage mechanism.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — exp-006 provides precise RMSE crossover points: K=2/extreme n_expert=250, K=4/extreme n=1000, K=4/moderate n=2000, K=2/moderate never crosses (global always better on RMSE). Paper needs \"Expert Budget Recommendation\" subsection with per-K guidelines. Key message: when diagnostic criterion flags high heterogeneity (extreme regime), EC-HTE is worth the investment at moderate budgets; when heterogeneity is low, global correction is the safer choice. This honest framing connects Claim 2 (EC-HTE method) to Claim 3 (diagnostic criterion) — the diagnostic decides the correction strategy.\n\n6. **\"How does this differ from Carroll et al. (2006) / classical measurement error?\"** — The qualitative insight that misspecified corrections can amplify MSE is classical (Fuller 1987, Sec. 2.3). Our specific contributions beyond this are: (a) the quantitative Δπ×Δτ product form for CATE estimation with effect-modifier misclassification, (b) demonstrating this failure mode occurs *by default* in standard LLM annotation workflows, and (c) providing a computable diagnostic and correction framework. Must explicitly cite and contextualize: Fuller (1987), Carroll et al. (2006 Ch. 4), Gustafson (2003), Hu & Schennach (2008), Imai & Yamamoto (2010). Also cite Bayesian annotation models: Dawid & Skene, Passonneau & Carpenter (2014), Hovy et al. (2013). **Bibliography target: 30-35 references** spanning measurement error, Bayesian estimation, causal inference, LLM-as-annotator (Tornberg 2024, Gilardi et al. 2023, Ziems et al. 2024), HTE methods (Wager & Athey 2018, Kennedy 2023, Chernozhukov et al. 2018).\n\n7. **\"Methodological novelty is modest\"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. HB partial pooling provides meaningful RMSE reduction for moderate subgroups but is NOT \"never worse than global\" — it is a James-Stein shrinkage estimator with known boundary conditions. **Recommended condition**: n_expert per subgroup ≥ ~25 (e.g., n_expert ≥ 100 for K=4 with 12% minority). Below this, stratified MLE is preferred. This honest limitation strengthens credibility. State conditions explicitly using per-subgroup formulation, not just total n_expert.\n\n8. **\"Why no figures?\"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use cases (sentiment analysis, hate speech detection, refugee interview coding), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track. **NOTE**: Framing broadened from \"political-science\" to \"CSS\" (D004b) — TweetEval stance tasks too small (N<1000), sentiment (N=45K) usable but not political science. CSS is more accurate and equally strong for EMNLP.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n## Writing Requirements (Dream Round 2 consensus)\n\n1. **\"Bias decomposition\" NOT \"bias bound\"** — Theorem 1 is an exact identity at population level. R² < 1.0 in verification reflects finite-sample MC noise, not bound looseness.\n2. **Bibliography: 30-35 references minimum** — Must span 5 literatures: classical measurement error, Bayesian estimation, causal inference, LLM-as-annotator, CSS. Critical citations: Fuller 1987, Wager & Athey 2018, Imai & Yamamoto 2010.\n3. **3+ figures in main text** — (a) bias mechanism schematic, (b) Δπ×Δτ amplification heatmap, (c) diagnostic ROC curve, (d) budget crossover curves. Move exp-008/exp-009 tables to appendix.\n4. **Semi-synthetic DGP fully specified** — outcome generation, treatment assignment, CATE injection mechanism.\n5. **Real-data framed as pattern consistency** — NOT ground-truth benchmark. No bias/RMSE against unknown true CATEs.\n6. **EC-HTE advantage is conditional, not universal** — ec_hte dominates when misclassification heterogeneity is high (extreme regime) OR n_expert is large (≥500). In moderate regime with small n_expert (~100), global correction can outperform ec_hte because per-subgroup CM estimation noise exceeds the benefit of stratification. This connects to Claim 3: the diagnostic criterion (Δπ×Δτ) predicts when EC-HTE is needed. Unified condition: n_expert/K ≥ ~25-50 experts per subgroup.\n11. **RMSE tradeoff must be disclosed** — ec_hte has higher RMSE than global/naive in K=4/n≤100 configs (up to 3.5x in extreme cases) due to noisy per-subgroup CM estimation. Bias is lower but variance is higher. Must report both bias AND RMSE; include bias-RMSE tradeoff analysis. At n_expert≥500, ec_hte RMSE becomes competitive.\n12. **K-dependence of debiasing-hurts** — K=2 extreme magnification ~2.7x; K=4 extreme ~5.9x. More subgroups → larger π heterogeneity → more severe global correction damage. Report this scaling.\n7. **Confusion matrix invertibility** — State det(Ĉ_k) ≠ 0 assumption explicitly.\n8. **Diagnostic AUC cross-validated** — Leave-one-setting-out or held-out evaluation, not in-sample.\n9. **Hyperprior values stated + sensitivity analysis** — Gamma(α, β) for Dirichlet concentration; report sensitivity to 2× changes.\n10. **PPCI complementarity elevated** — Highlight in abstract and contributions. Frame as \"complementary\" not \"orthogonal\": EC-HTE is structured covariate-error correction; PPCI rectifier is general residual correction. Composition = EC-HTE handles structured part + rectifier handles remainder (primarily outcome error).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2. MUST report full MCMC diagnostics: sampler (PyMC\n    NUTS), chains (≥4), warmup (≥1000), R̂ (<1.01), ESS (>200), runtime vs MLE. Report\n    SEs/CIs for all metrics from MC runs. Monitor coverage calibration — if systematic\n    undercoverage, diagnose cause.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example. MUST include K>2 extension: verify bias formula empirically for K=4 subgroups;\n    add Remark after Proposition 1 discussing general-K case (sum-of-products form).\n    Report R² of analytic prediction vs MC, bound tightness ratio, and CIs on all\n    bias estimates.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim: 1,2,3\n  description: 'Semi-synthetic benchmark: use real CSS tweet corpus — TweetEval sentiment\n    (N=45K, primary) for exp-003. Framing broadened from ''political-science'' to\n    ''CSS'' per D004b (stance tasks N<1000 unusable). Inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 (API) and optionally Qwen3-235B-A22B (GPU), measure\n    subgroup-specific misclassification rates, apply EC-HTE vs baselines. Subgroup\n    variables: text features (has_hashtag, text_length) for semi-synthetic; demographic\n    subgroups reserved for exp-004. MUST fully specify DGP in paper: (a) outcome generation\n    model, (b) treatment assignment mechanism, (c) how true CATEs are injected. MUST\n    run LLM annotation pilot (~1000 samples) before committing to verify per-subgroup\n    misclassification heterogeneity exists.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim: 1,2\n  description: 'Real-data case study (pattern consistency, NOT ground-truth validation):\n    apply EC-HTE to real CSS dataset with subgroup-varying LLM misclassification.\n    Show: (a) global vs EC-HTE produce qualitatively different CATE distributions,\n    (b) EC-HTE results consistent with domain knowledge (demographic effect direction),\n    (c) bootstrap CIs on point estimate differences. Frame as ''illustrative application''\n    not ''ground-truth benchmark''. Reviewer confirmed: real data has no ground truth\n    CATE, CV-based ground truth is circular. PRIMARY: UC Berkeley Measuring Hate Speech\n    corpus (public, rich demographic subgroups). NICE-TO-HAVE: Ashwin et al. (2025)\n    if obtainable (requires author email + IRB, not feasible within 5-day DDL).'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference) or API\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: UC Berkeley dataset causal framework (T,Y,Z,S) mapping needs design\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold. MUST use\n    cross-validation or held-out evaluation (NOT in-sample AUC on own experiments).\n    Dream Round 2 flagged in-sample AUC as methodological weakness across best and\n    median tiers.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1,2\n  description: 'PPCI + DSL baseline comparison: (a) PPCI kernel-based conditional\n    correction vs EC-HTE on covariate-side vs outcome-side error; (b) per-subgroup\n    DSL as additional baseline (DSL applied independently per subgroup, no cross-subgroup\n    shrinkage — shows EC-HTE''s partial pooling advantage); (c) EC-HTE+PPCI composition\n    for simultaneous covariate+outcome error; (d) CRITICAL: include ''pure covariate-error,\n    zero outcome-error'' control condition to demonstrate EC-HTE advantage when covariate-side\n    error dominates (PPCI should be ineffective here). Paper framing: DSL per-subgroup\n    is a valid baseline but lacks cross-subgroup shrinkage and operates at estimand\n    level rather than measurement model level.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest integration: apply EC-HTE post-hoc correction to CausalForestDML\n    subgroup CATE estimates + leaf-level corrected pseudo-outcomes with variance-adjusted\n    CIs. Compare against naive forest and globally-corrected forest. ELEVATED TO P0:\n    Claim 2 explicitly states CausalForestDML but no experiment validates this — claim-evidence\n    gap is reviewer killshot.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mcmc_rhat_max: 1.024\n    mcmc_ess_min: 129\n    mcmc_divergent: 0\n    runtime_min: 69\n    total_mc_runs: 3600\n    hb_vs_mle_rmse_improvement_k2_n50: 4-9%\n    hb_vs_mle_rmse_improvement_k2_n100: 1-2%\n    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%\n    hb_coverage_min: 0.87\n    hb_coverage_median: 0.93\n    k4_extreme_n50_blowup: false\n    k4_extreme_n50_blowup_note: Fixed by singularity guard + 4-chain MCMC\n    mcmc_fix_4chain:\n      rhat_max_all_configs: 1.0034\n      ess_min_all_configs: 1618\n      ess_improvement: ~4x vs 2-chain\n      k4_extreme_n50_A_rmse_z0: 3.14 → 0.99\n      k4_extreme_n50_B_rmse_z0: 509.93 → 0.27\n      k4_extreme_n100_A_rmse_z0: 11.57 → 0.29\n      singularity_guard_triggers: extreme/n=50 only (2 HB, 3 MLE / 100 runs)\n      results_file: results/exp001_hb_results_v2.csv\n    hyperprior_sensitivity:\n      scale_range: 0.5-2.0\n      k2_rmse_variation: <1%\n      k4_rmse_variation: ~4-5%\n      coverage_invariant: true\n      conclusion: robust\n      results_file: results/exp001_hyperprior_sensitivity.csv\n- exp_id: exp-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r2_k2: 0.9939\n    r2_k4: 0.9738\n    tightness_ratio_k2_median: 1.0027\n    tightness_ratio_k4_median: 1.0234\n    debiasing_hurts_pct: 50\n    debiasing_hurts_pct_note: 260/520 (excluding dc=0 rows where bias=0)\n    debiasing_hurts_threshold_delta_misclass: 0.1235\n    max_bias_ratio_k2: 2.86\n    max_bias_ratio_k4: 2.41\n    coverage_2se_k2: 0.951\n    coverage_2se_k4: 0.94\n- exp_id: exp-007\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_rows: 6912\n    dgps:\n    - A_covariate_only\n    - B_outcome_only\n    - C_both_errors\n    - D_no_error\n    methods: 8\n    mc_runs: 100\n    double_correction_fix_verified: true\n    dgp_a_ec_hte_ppci_equals_ec_hte: true\n    dgp_c_extreme_n250_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.225\n      ec_hte_bias_z0: 0.178\n      ec_hte_rmse_z0: 0.226\n      ppci_bias_z0: 0.004\n      ppci_rmse_z0: 0.261\n      naive_bias_z0: 0.251\n      naive_rmse_z0: 0.269\n    dgp_c_n500_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.142\n      ec_hte_bias_z0: 0.088\n      ec_hte_rmse_z0: 0.134\n    key_finding: ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better\n      than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.\n- exp_id: exp-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase: A_semi_synthetic\n    n_subgroups: 4\n    misclass_rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25\n    subgroup_sizes: S0~38%, S1~38%, S2~12%, S3~12%\n    p_z1_actual: 0.39\n    debiasing_hurts_confirmed: true\n    mc_runs: 100\n    v3_hb_integration:\n      methods:\n      - oracle\n      - naive\n      - global_corrected\n      - stratified_mle\n      - hb_ec_hte\n      hb_vs_mle_summary:\n        S2_n50_rmse_z0_improvement: +21.4%\n        S2_n100_rmse_z0_improvement: +39.5%\n        S3_n50_blowup: RMSE 345-804% worse\n        convergence_at_n250: < 5% difference\n        S0_n50_extreme_rmse_z0_improvement: +88%\n      key_finding: HB partial pooling helps mid-misclass subgroups (S2) at small n_expert\n        but blows up in extreme-misclass tiny subgroups (S3 at n=50). Converges to\n        MLE at n>=250.\n      hypothesis_verdict: partially_validated\n    results_file_v3: results/exp003_phase_a_v3.csv\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subgroup_level_auc: 0.833\n    subgroup_correlation: 0.86\n    setting_level_auc: 0.49\n    low_pi_hurt_pct: 84.6\n    high_pi_hurt_pct: 15.4\n    theory_alignment: consistent with exp-002 formula\n- exp_id: exp-011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    n_configs: 8\n    total_rows: 144\n    runtime_min: 35\n    methods:\n    - naive_forest\n    - global_forest\n    - ec_hte_forest\n    mean_abs_bias:\n      naive_forest: 0.1558\n      global_forest: 0.1073\n      ec_hte_forest: 0.0608\n    mean_rmse:\n      naive_forest: 0.1782\n      global_forest: 0.1659\n      ec_hte_forest: 0.2289\n    debiasing_hurts_cases: 9\n    debiasing_hurts_max_ratio: 5.9\n    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'\n    k2_n500_ec_hte_bias_range: 0.004-0.013 (near zero)\n    k2_n500_global_bias_range: 0.033-0.109 (still biased)\n    pattern_consistent_with_diff_in_means: true\n    claim2_validated: true\n- exp_id: exp-006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    total_rows: 288\n    runtime_min: 110\n    grid: n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]\n    crossover_hb_beats_global:\n      K2_extreme: 250\n      K2_moderate: never\n      K4_extreme: 1000\n      K4_moderate: 2000\n    hb_vs_mle: HB ≥ MLE in 22/24 configs (partial pooling never significantly hurts\n      in symmetric DGP)\n    hb_best_improvement_over_mle:\n      K4_moderate_n50_sgC: +42.4% RMSE\n      K4_extreme_n50_sgC: +23.4% RMSE\n      K4_moderate_n50_sgB: +24.0% RMSE\n    convergence: HB ≈ MLE at n≥1000 (<0.5% difference)\n    key_finding: 'Crossover depends strongly on K and regime. K=2: crossover at n=250\n      (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest\n      improvement over MLE via partial pooling.'\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:31:41.722Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:31:41.722Z",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T03:31:41.759Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Real LLM annotations exhibit substantial misclassification heterogeneity on CSS tasks; semi-synthetic and real-data experiments confirm bias mechanism at practical magnitudes; all three claims validated with explicit boundary conditions
核心假设：['GPT-4.1 misclassification rates vary ≥0.12 (max−min) across text-feature subgroups on TweetEval sentiment', 'Semi-synthetic with real LLM labels replicates bias amplification ≥2x in majority of high-heterogeneity configs', 'EC-HTE RMSE competitive with global at n_expert ≥ 500 for K=4 (ratio ≤ 1.2)', 'Diagnostic criterion, after refinement (max-subgroup product or weighted aggregation), achieves cross-validated setting-level AUC ≥ 0.70', 'UC Berkeley hate speech real-data case study shows ≥1 subgroup with CATE shift > 2 SE between global and EC-HTE', 'ec_hte_ppci composition replicates near-zero bias on semi-synthetic with mixed covariate+outcome error']
关键指标范围：{'semi_synth_llm_delta_pi': [0.12, 0.25], 'semi_synth_llm_bias_amplification_median': [2.0, 4.0], 'ec_hte_bias_reduction_pct_n500': [55, 80], 'ec_hte_rmse_ratio_n500_k4': [1.0, 1.2], 'diagnostic_cv_auc_setting': [0.7, 0.85], 'diagnostic_cv_auc_subgroup': [0.83, 0.95], 'real_data_max_cate_shift_se': [2.0, 5.0], 'coverage_ec_hte_95': [0.9, 0.97], 'ec_hte_ppci_bias_reduction_vs_ec_hte_dgpC': [80, 97]}
叙事方向：Original framing fully intact. Lead with bias identity theorem (exact, R²≥0.97) and 'debiasing can hurt' proposition as problem-level discovery. Headline: 'global correction worsens subgroup CATE bias by 2-3x; EC-HTE reduces to near-zero with 250-500 expert labels.' Three claims at full strength with boundary conditions (n_expert/K ≥ 25, det(Ĉ_k) ≠ 0). Diagnostic criterion positioned as practitioner decision rule. EC-HTE+PPCI complementarity elevated in abstract. Paper structure standard: theory → method → synthetic → semi-synthetic (real LLM) → real data. exp-008/009 in appendix. Four main-text figures as planned.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: ec_hte_llm_annotation
venue: emnlp-2026

## paper_framing.md

# Paper Framing — ec_hte_llm_annotation

## Target Venue
- Primary: EMNLP 2026 Main (via ARR)
- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026
- Format: Long paper, 8 pages + unlimited references

## Core Claims (3 条，可证伪)

1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this "debiasing" can worsen CATE bias by 2-3x (median across configurations), with extreme cases exceeding 20x. Global correction increases subgroup-level bias in ~50% of the parameter space.

2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction in moderate-sized subgroups by borrowing strength across groups (classic James-Stein shrinkage). **Boundary condition**: when expert labels per subgroup < ~25 (e.g., n_expert=50 with 12% minority subgroup → ~6 labels) AND subgroup parameter is far from group mean, shrinkage can be harmful — stratified MLE is preferred. Recommended: n_expert such that smallest subgroup contains ≥25 expert labels. **NOTE**: exact improvement magnitudes pending full 100 MC confirmation (current estimates from n_mc=2 dry-run). Demonstrated with both difference-in-means and CausalForestDML (exp-011: consistent bias reduction pattern, ec_hte_forest |bias|=0.06 vs naive 0.16). CausalForest amplifies the debiasing-hurts effect (up to 5.9x in K=4/extreme) due to nonlinear CATE estimation.

3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.

## Story Spine

- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis across computational social science (CSS) — e.g., sentiment framing moderates message effectiveness, hate speech type moderates intervention impact. LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education; documented across CSS tasks including sentiment, stance, toxicity). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.

- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**

- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as "problem identification + principled solution" not "new estimation technique."

- **Headline result template**: "On semi-synthetic CSS benchmarks (sentiment analysis, hate speech detection), global correction worsens subgroup CATE bias by 2-3x (median), with up to 20x in extreme cases; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels."

- **Oracle framing**: When reporting DGP C results where ec_hte_ppci outperforms oracle, always use "covariate-oracle" (true Z + observed Y), never unqualified "oracle". Frame as "composite correction is necessary and sufficient when both error types coexist" — NOT "beats oracle". The result is by construction (ec_hte_ppci corrects both error types; covariate-oracle only corrects one), not surprising.

## Key Contributions (ordered for paper)

1. **Bias decomposition identity**: Exact population-level identity: bias ∝ misclassification heterogeneity × CATE heterogeneity (Δπ×Δτ product form). NOT a bound — it is an exact identity under A1–A4; finite-sample R² measures MC noise, not bound looseness. Includes "debiasing can hurt" proposition with constructive example. Frame as "bias decomposition" or "bias identity" throughout — never "bias bound." (Theory + Empirical)
2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)
3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)
4. **EC-HTE + PPCI complementarity**: EC-HTE is a structured correction exploiting mixing matrix structure for covariate-side error; PPCI rectifier is a general-purpose residual correction that captures any systematic error (including outcome-side). They are complementary, not orthogonal — PPCI alone can partially correct covariate error but less efficiently than M⁻¹; in composition, EC-HTE handles the structured covariate error precisely, and the residual rectifier handles remaining outcome error. Composition achieves best-of-both when both error types are present. Elevate in abstract and contributions list. (Method + Empirical)
5. **Comprehensive validation**: Synthetic + semi-synthetic + real-data case study (pattern consistency, not ground-truth benchmark) with multiple LLMs. (Empirical)

## Anticipated Reviewer Concerns

1. **"Why not just use expert labels directly for CATE?"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.

2. **"How is this different from PPCI / DSL?"** — PPCI rectifier is a general-purpose correction that captures any systematic error (covariate + outcome); EC-HTE is a structured correction exploiting mixing matrix structure specifically for covariate-side error. They are complementary: EC-HTE alone is more efficient for covariate error (uses M⁻¹ structure), PPCI alone can partially correct covariate error but with higher variance (limited by gold subset). In composition, EC-HTE handles structured covariate error, residual rectifier handles outcome error. DSL applied per-subgroup is a valid baseline but lacks cross-subgroup shrinkage, operates at estimand level rather than measurement model level, and has strictly higher variance under partial pooling. Do NOT say "DSL cannot do subgroup correction" — say it lacks the principled shrinkage mechanism.

3. **"Incremental over Mozer (2026)"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.

4. **"How sensitive to subgroup definition?"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.

5. **"Real-world expert label cost"** — exp-006 provides precise RMSE crossover points: K=2/extreme n_expert=250, K=4/extreme n=1000, K=4/moderate n=2000, K=2/moderate never crosses (global always better on RMSE). Paper needs "Expert Budget Recommendation" subsection with per-K guidelines. Key message: when diagnostic criterion flags high heterogeneity (extreme regime), EC-HTE is worth the investment at moderate budgets; when heterogeneity is low, global correction is the safer choice. This honest framing connects Claim 2 (EC-HTE method) to Claim 3 (diagnostic criterion) — the diagnostic decides the correction strategy.

6. **"How does this differ from Carroll et al. (2006) / classical measurement error?"** — The qualitative insight that misspecified corrections can amplify MSE is classical (Fuller 1987, Sec. 2.3). Our specific contributions beyond this are: (a) the quantitative Δπ×Δτ product form for CATE estimation with effect-modifier misclassification, (b) demonstrating this failure mode occurs *by default* in standard LLM annotation workflows, and (c) providing a computable diagnostic and correction framework. Must explicitly cite and contextualize: Fuller (1987), Carroll et al. (2006 Ch. 4), Gustafson (2003), Hu & Schennach (2008), Imai & Yamamoto (2010). Also cite Bayesian annotation models: Dawid & Skene, Passonneau & Carpenter (2014), Hovy et al. (2013). **Bibliography target: 30-35 references** spanning measurement error, Bayesian estimation, causal inference, LLM-as-annotator (Tornberg 2024, Gilardi et al. 2023, Ziems et al. 2024), HTE methods (Wager & Athey 2018, Kennedy 2023, Chernozhukov et al. 2018).

7. **"Methodological novelty is modest"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. HB partial pooling provides meaningful RMSE reduction for moderate subgroups but is NOT "never worse than global" — it is a James-Stein shrinkage estimator with known boundary conditions. **Recommended condition**: n_expert per subgroup ≥ ~25 (e.g., n_expert ≥ 100 for K=4 with 12% minority). Below this, stratified MLE is preferred. This honest limitation strengthens credibility. State conditions explicitly using per-subgroup formulation, not just total n_expert.

8. **"Why no figures?"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.

## Venue Fit

EMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use cases (sentiment analysis, hate speech detection, refugee interview coding), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track. **NOTE**: Framing broadened from "political-science" to "CSS" (D004b) — TweetEval stance tasks too small (N<1000), sentiment (N=45K) usable but not political science. CSS is more accurate and equally strong for EMNLP.

Risk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.

## Writing Requirements (Dream Round 2 consensus)

1. **"Bias decomposition" NOT "bias bound"** — Theorem 1 is an exact identity at population level. R² < 1.0 in verification reflects finite-sample MC noise, not bound looseness.
2. **Bibliography: 30-35 references minimum** — Must span 5 literatures: classical measurement error, Bayesian estimation, causal inference, LLM-as-annotator, CSS. Critical citations: Fuller 1987, Wager & Athey 2018, Imai & Yamamoto 2010.
3. **3+ figures in main text** — (a) bias mechanism schematic, (b) Δπ×Δτ amplification heatmap, (c) diagnostic ROC curve, (d) budget crossover curves. Move exp-008/exp-009 tables to appendix.
4. **Semi-synthetic DGP fully specified** — outcome generation, treatment assignment, CATE injection mechanism.
5. **Real-data framed as pattern consistency** — NOT ground-truth benchmark. No bias/RMSE against unknown true CATEs.
6. **EC-HTE advantage is conditional, not universal** — ec_hte dominates when misclassification heterogeneity is high (extreme regime) OR n_expert is large (≥500). In moderate regime with small n_expert (~100), global correction can outperform ec_hte because per-subgroup CM estimation noise exceeds the benefit of stratification. This connects to Claim 3: the diagnostic criterion (Δπ×Δτ) predicts when EC-HTE is needed. Unified condition: n_expert/K ≥ ~25-50 experts per subgroup.
11. **RMSE tradeoff must be disclosed** — ec_hte has higher RMSE than global/naive in K=4/n≤100 configs (up to 3.5x in extreme cases) due to noisy per-subgroup CM estimation. Bias is lower but variance is higher. Must report both bias AND RMSE; include bias-RMSE tradeoff analysis. At n_expert≥500, ec_hte RMSE becomes competitive.
12. **K-dependence of debiasing-hurts** — K=2 extreme magnification ~2.7x; K=4 extreme ~5.9x. More subgroups → larger π heterogeneity → more severe global correction damage. Report this scaling.
7. **Confusion matrix invertibility** — State det(Ĉ_k) ≠ 0 assumption explicitly.
8. **Diagnostic AUC cross-validated** — Leave-one-setting-out or held-out evaluation, not in-sample.
9. **Hyperprior values stated + sensitivity analysis** — Gamma(α, β) for Dirichlet concentration; report sensitivity to 2× changes.
10. **PPCI complementarity elevated** — Highlight in abstract and contributions. Frame as "complementary" not "orthogonal": EC-HTE is structured covariate-error correction; PPCI rectifier is general residual correction. Composition = EC-HTE handles structured part + rectifier handles remainder (primarily outcome error).


## experiment_plan (with registry status)

- id: exp-001
  claim: 2
  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior
    confusion matrix estimator with partial pooling, compare against MLE/Laplace on
    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).
    Primary validation of Claim 2. MUST report full MCMC diagnostics: sampler (PyMC
    NUTS), chains (≥4), warmup (≥1000), R̂ (<1.01), ESS (>200), runtime vs MLE. Report
    SEs/CIs for all metrics from MC runs. Monitor coverage calibration — if systematic
    undercoverage, diagnose cause.'
  priority: P0
  gpu_budget_hours: 0
  compute: CPU (PyMC + econml)
  estimated_time: 12-24h (coding + 1000 MC runs)
  deps: []
  status: planned
- id: exp-002
  claim: 1
  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,
    CATE_heterogeneity) analytically, then verify empirically across systematic parameter
    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup
    example. MUST include K>2 extension: verify bias formula empirically for K=4 subgroups;
    add Remark after Proposition 1 discussing general-K case (sum-of-products form).
    Report R² of analytic prediction vs MC, bound tightness ratio, and CIs on all
    bias estimates.'
  priority: P0
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 8-12h
  deps: []
  status: planned
- id: exp-003
  claim: 1,2,3
  description: 'Semi-synthetic benchmark: use real CSS tweet corpus — TweetEval sentiment
    (N=45K, primary) for exp-003. Framing broadened from ''political-science'' to
    ''CSS'' per D004b (stance tasks N<1000 unusable). Inject known CATE heterogeneity
    structure, annotate with GPT-4.1 (API) and optionally Qwen3-235B-A22B (GPU), measure
    subgroup-specific misclassification rates, apply EC-HTE vs baselines. Subgroup
    variables: text features (has_hashtag, text_length) for semi-synthetic; demographic
    subgroups reserved for exp-004. MUST fully specify DGP in paper: (a) outcome generation
    model, (b) treatment assignment mechanism, (c) how true CATEs are injected. MUST
    run LLM annotation pilot (~1000 samples) before committing to verify per-subgroup
    misclassification heterogeneity exists.'
  priority: P0
  gpu_budget_hours: 20
  compute: GPU (LLM inference for annotation)
  estimated_time: 24-36h
  deps:
  - exp-001
  status: planned
- id: exp-004
  claim: 1,2
  description: 'Real-data case study (pattern consistency, NOT ground-truth validation):
    apply EC-HTE to real CSS dataset with subgroup-varying LLM misclassification.
    Show: (a) global vs EC-HTE produce qualitatively different CATE distributions,
    (b) EC-HTE results consistent with domain knowledge (demographic effect direction),
    (c) bootstrap CIs on point estimate differences. Frame as ''illustrative application''
    not ''ground-truth benchmark''. Reviewer confirmed: real data has no ground truth
    CATE, CV-based ground truth is circular. PRIMARY: UC Berkeley Measuring Hate Speech
    corpus (public, rich demographic subgroups). NICE-TO-HAVE: Ashwin et al. (2025)
    if obtainable (requires author email + IRB, not feasible within 5-day DDL).'
  priority: P0
  gpu_budget_hours: 10
  compute: GPU (LLM inference) or API
  estimated_time: 24h
  deps:
  - exp-001
  status: planned
  risk: UC Berkeley dataset causal framework (T,Y,Z,S) mapping needs design
- id: exp-005
  claim: 3
  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×
    CATE_heterogeneity product from pilot data across all experimental settings, show
    it predicts when global correction fails. ROC analysis of threshold. MUST use
    cross-validation or held-out evaluation (NOT in-sample AUC on own experiments).
    Dream Round 2 flagged in-sample AUC as methodological weakness across best and
    median tiers.'
  priority: P0
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 4-8h
  deps:
  - exp-001
  - exp-003
  status: planned
- id: exp-006
  claim: 2
  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,
    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where
    EC-HTE > Global. Validate HB partial pooling value at small n.'
  priority: P1
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 8h
  deps:
  - exp-001
  status: planned
- id: exp-007
  claim: 1,2
  description: 'PPCI + DSL baseline comparison: (a) PPCI kernel-based conditional
    correction vs EC-HTE on covariate-side vs outcome-side error; (b) per-subgroup
    DSL as additional baseline (DSL applied independently per subgroup, no cross-subgroup
    shrinkage — shows EC-HTE''s partial pooling advantage); (c) EC-HTE+PPCI composition
    for simultaneous covariate+outcome error; (d) CRITICAL: include ''pure covariate-error,
    zero outcome-error'' control condition to demonstrate EC-HTE advantage when covariate-side
    error dominates (PPCI should be ineffective here). Paper framing: DSL per-subgroup
    is a valid baseline but lacks cross-subgroup shrinkage and operates at estimand
    level rather than measurement model level.'
  priority: P0
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 16h
  deps:
  - exp-001
  - exp-003
  status: planned
- id: exp-008
  claim: 2
  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude
    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit
    varies by LLM quality.'
  priority: P1
  gpu_budget_hours: 15
  compute: GPU
  estimated_time: 12h
  deps:
  - exp-003
  status: planned
- id: exp-009
  claim: 2
  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted
    allocation targeting high-CATE × high-error subgroups, compare against uniform
    and uncertainty-only allocation.'
  priority: P2
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 16h
  deps:
  - exp-001
  - exp-006
  status: planned
- id: exp-010
  claim: 2
  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups
    are noisy/overlapping or when the true subgroup structure doesn''t align with
    the conditioning variable.'
  priority: P2
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 8h
  deps:
  - exp-001
  status: planned
- id: exp-011
  claim: 2
  description: 'Causal forest integration: apply EC-HTE post-hoc correction to CausalForestDML
    subgroup CATE estimates + leaf-level corrected pseudo-outcomes with variance-adjusted
    CIs. Compare against naive forest and globally-corrected forest. ELEVATED TO P0:
    Claim 2 explicitly states CausalForestDML but no experiment validates this — claim-evidence
    gap is reviewer killshot.'
  priority: P0
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 16h
  deps:
  - exp-001
  status: planned


## registry (completed experiments)

- exp_id: exp-001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mcmc_rhat_max: 1.024
    mcmc_ess_min: 129
    mcmc_divergent: 0
    runtime_min: 69
    total_mc_runs: 3600
    hb_vs_mle_rmse_improvement_k2_n50: 4-9%
    hb_vs_mle_rmse_improvement_k2_n100: 1-2%
    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%
    hb_coverage_min: 0.87
    hb_coverage_median: 0.93
    k4_extreme_n50_blowup: false
    k4_extreme_n50_blowup_note: Fixed by singularity guard + 4-chain MCMC
    mcmc_fix_4chain:
      rhat_max_all_configs: 1.0034
      ess_min_all_configs: 1618
      ess_improvement: ~4x vs 2-chain
      k4_extreme_n50_A_rmse_z0: 3.14 → 0.99
      k4_extreme_n50_B_rmse_z0: 509.93 → 0.27
      k4_extreme_n100_A_rmse_z0: 11.57 → 0.29
      singularity_guard_triggers: extreme/n=50 only (2 HB, 3 MLE / 100 runs)
      results_file: results/exp001_hb_results_v2.csv
    hyperprior_sensitivity:
      scale_range: 0.5-2.0
      k2_rmse_variation: <1%
      k4_rmse_variation: ~4-5%
      coverage_invariant: true
      conclusion: robust
      results_file: results/exp001_hyperprior_sensitivity.csv
- exp_id: exp-002
  name: ''
  status: DONE
  conclusion: success
  metrics:
    r2_k2: 0.9939
    r2_k4: 0.9738
    tightness_ratio_k2_median: 1.0027
    tightness_ratio_k4_median: 1.0234
    debiasing_hurts_pct: 50
    debiasing_hurts_pct_note: 260/520 (excluding dc=0 rows where bias=0)
    debiasing_hurts_threshold_delta_misclass: 0.1235
    max_bias_ratio_k2: 2.86
    max_bias_ratio_k4: 2.41
    coverage_2se_k2: 0.951
    coverage_2se_k4: 0.94
- exp_id: exp-007
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_rows: 6912
    dgps:
    - A_covariate_only
    - B_outcome_only
    - C_both_errors
    - D_no_error
    methods: 8
    mc_runs: 100
    double_correction_fix_verified: true
    dgp_a_ec_hte_ppci_equals_ec_hte: true
    dgp_c_extreme_n250_k2:
      ec_hte_ppci_bias_z0: 0.005
      ec_hte_ppci_rmse_z0: 0.225
      ec_hte_bias_z0: 0.178
      ec_hte_rmse_z0: 0.226
      ppci_bias_z0: 0.004
      ppci_rmse_z0: 0.261
      naive_bias_z0: 0.251
      naive_rmse_z0: 0.269
    dgp_c_n500_k2:
      ec_hte_ppci_bias_z0: 0.005
      ec_hte_ppci_rmse_z0: 0.142
      ec_hte_bias_z0: 0.088
      ec_hte_rmse_z0: 0.134
    key_finding: ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better
      than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.
- exp_id: exp-003
  name: ''
  status: DONE
  conclusion: success
  metrics:
    phase: A_semi_synthetic
    n_subgroups: 4
    misclass_rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25
    subgroup_sizes: S0~38%, S1~38%, S2~12%, S3~12%
    p_z1_actual: 0.39
    debiasing_hurts_confirmed: true
    mc_runs: 100
    v3_hb_integration:
      methods:
      - oracle
      - naive
      - global_corrected
      - stratified_mle
      - hb_ec_hte
      hb_vs_mle_summary:
        S2_n50_rmse_z0_improvement: +21.4%
        S2_n100_rmse_z0_improvement: +39.5%
        S3_n50_blowup: RMSE 345-804% worse
        convergence_at_n250: < 5% difference
        S0_n50_extreme_rmse_z0_improvement: +88%
      key_finding: HB partial pooling helps mid-misclass subgroups (S2) at small n_expert
        but blows up in extreme-misclass tiny subgroups (S3 at n=50). Converges to
        MLE at n>=250.
      hypothesis_verdict: partially_validated
    results_file_v3: results/exp003_phase_a_v3.csv
- exp_id: exp-005
  name: ''
  status: DONE
  conclusion: success
  metrics:
    subgroup_level_auc: 0.833
    subgroup_correlation: 0.86
    setting_level_auc: 0.49
    low_pi_hurt_pct: 84.6
    high_pi_hurt_pct: 15.4
    theory_alignment: consistent with exp-002 formula
- exp_id: exp-011
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_mc: 100
    n_configs: 8
    total_rows: 144
    runtime_min: 35
    methods:
    - naive_forest
    - global_forest
    - ec_hte_forest
    mean_abs_bias:
      naive_forest: 0.1558
      global_forest: 0.1073
      ec_hte_forest: 0.0608
    mean_rmse:
      naive_forest: 0.1782
      global_forest: 0.1659
      ec_hte_forest: 0.2289
    debiasing_hurts_cases: 9
    debiasing_hurts_max_ratio: 5.9
    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'
    k2_n500_ec_hte_bias_range: 0.004-0.013 (near zero)
    k2_n500_global_bias_range: 0.033-0.109 (still biased)
    pattern_consistent_with_diff_in_means: true
    claim2_validated: true
- exp_id: exp-006
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_mc: 100
    total_rows: 288
    runtime_min: 110
    grid: n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]
    crossover_hb_beats_global:
      K2_extreme: 250
      K2_moderate: never
      K4_extreme: 1000
      K4_moderate: 2000
    hb_vs_mle: HB ≥ MLE in 22/24 configs (partial pooling never significantly hurts
      in symmetric DGP)
    hb_best_improvement_over_mle:
      K4_moderate_n50_sgC: +42.4% RMSE
      K4_extreme_n50_sgC: +23.4% RMSE
      K4_moderate_n50_sgB: +24.0% RMSE
    convergence: HB ≈ MLE at n≥1000 (<0.5% difference)
    key_finding: 'Crossover depends strongly on K and regime. K=2: crossover at n=250
      (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest
      improvement over MLE via partial pooling.'

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: best
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b63972de-7f24-4eb2-ac43-6e4748a290fb",
  "type": "user",
  "uuid": "f1c6c443-00e7-4ab9-a6b7-497a2b72e3e4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:31:41.757Z_

```json
{
  "parentUuid": "f1c6c443-00e7-4ab9-a6b7-497a2b72e3e4",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "deae7ac1-4ec3-478f-8c92-54d2fc1f0e76",
  "timestamp": "2026-05-21T03:31:41.757Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:31:41.757Z_

```json
{
  "parentUuid": "deae7ac1-4ec3-478f-8c92-54d2fc1f0e76",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "da8d3e71-f5f5-4943-b4d9-cf54a58c96e3",
  "timestamp": "2026-05-21T03:31:41.757Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Real LLM annotations exhibit substantial misclassification heterogeneity on CSS tasks; semi-synthetic and real-data experiments confirm bias mechanism at p…",
  "leafUuid": "da8d3e71-f5f5-4943-b4d9-cf54a58c96e3",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE validation: bias mechanism, diagnostic criterion, real LLM labels",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4"
}
```

---

### Assistant

_source line 8 · 2026-05-21T03:33:09.061Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment plan, under the "best" tier definition. I need to look at which experiments are still "planned" vs "DONE".

From the registry, the following are DONE:
- exp-001: DONE
- exp-002: DONE
- exp-003: DONE (phase A semi-synthetic)
- exp-005: DONE
- exp-006: DONE
- exp-007: DONE
- exp-011: DONE

From the experiment plan, the following are still "planned":


- exp-003: has a phase B (real LLM annotation with GPT-4.1 and Qwen3) that's still pending, even though phase A is done
- exp-004: planned
- exp-008: planned
- exp-009: planned
- exp-010: planned

Wait, let me check the registry more carefully. Looking at which experiments are marked as DONE versus which are still planned, I see that exp-001, exp-002, exp-005, exp-006, exp-007, and exp-011 are all completed. The ones that are actually still pending are exp-003's second phase, exp-004, exp-008, exp-009, and exp-010 — those are the real-data case study, the multiple LLM annotator comparison, the adaptive expert allocation, and the robustness testing.

The user is asking for predictions on all planned experiments, but there's some ambiguity here since the experiment plan lists everything as "planned" while the registry shows many are already done. I think they're asking for the ones that haven't been executed yet, so I should focus on generating detailed predictions for those five remaining experiments. So the registry shows experiments 001, 002, 003, 005, 006, 007, and 011 are marked as done, while the experiment plan lists everything as planned — there's a mismatch. The ones that haven't appeared in the registry yet are exp-004, exp-008, exp-009, and exp-010, plus potentially a remaining phase of exp-003. I think the user wants predictions for whichever experiments are still pending, so I should focus on those four plus any incomplete phases of exp-003. 我在纠结该如何理解这个请求——是否应该为已完成的实验生成预测结果似乎没有意义。让我重新审视这个问题：experiment_plan 中所有条目的状态都标记为 planned，这可能是原始计划文档，而 registry 才是追踪实际完成情况的地方。我认为最合理的做法是为尚未完成的实验生成最佳情景下的预测，也就是 exp-004、exp-008、exp-009、exp-010，以及 exp-003 的 phase B（如果适用的话）。

不过再想想，用户可能就是想要对整个实验计划中的所有实验进行标准的研究方法论预测——对已完成的实验，我的预测应该与实际结果一致（因为最佳情景本来就是基于可达成的结果定义的），对未完成的实验则预测应该发生的结果。我应该为所有实验生成 YAML 输出，每个实验需要包含名称、计划 ID、描述、预期结果指标、结果依据、表格和图表说明。现在让我逐个考虑每个实验在最佳情景下的预测。 Continuing through the remaining experiments—exp-006 shows expert labeling works well with reasonable sample sizes, exp-007 confirms the debiasing method handles the hardest case effectively, and exp-008 through exp-011 outline what still needs validation around LLM variation, adaptive strategies, robustness properties, and causal forest compatibility.

Now I'm constructing the full YAML specification with comprehensive metrics and narrative guidance. The core story stays intact: the bias identity theorem provides exact characterization, debiasing paradoxically worsens subgroup bias without expert correction, and EC-HTE recovers near-zero bias efficiently with modest expert annotation budgets.

Writing YAML configuration... Now I'm looking at the computational requirements and expected outcomes across the remaining experiments. For exp-002, I'm predicting strong model fit with R² values above 0.97 even at higher complexity, though debiasing actually worsens performance in about half the parameter space with bias ratios reaching up to 5.9x at K=4. For exp-003, I'm expecting GPT-4.1 to show meaningful misclassification rate variation across subgroups with bias amplification in the 2-4x range, which the EC-HTE approach should help mitigate.

Looking ahead at the remaining experiments, exp-004 needs to demonstrate genuine heterogeneity with CATE shifts exceeding two standard errors and qualitatively distinct distributions between methods. Exp-005 should show strong subgroup discrimination with AUCs in the 0.83-0.95 range while maintaining reasonable cross-validated performance. For exp-006, I'm targeting EC-HTE to achieve RMSE ratios under 1.2 at moderate sample sizes with clear inflection points where K=2 and K=4 perform optimally at different scales. Finally, exp-007 should demonstrate that combining EC-HTE with post-prediction calibration intervals yields 80-97% bias reduction compared to EC-HTE alone in the most challenging data generation process. Now I'm compiling the tier metrics for the YAML output, focusing on the performance thresholds across different experimental conditions and diagnostic measures. Writing the YAML configuration...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da8d3e71-f5f5-4943-b4d9-cf54a58c96e3",
  "isSidechain": false,
  "requestId": "req_011CbF1SfHMqCrGzAjioP8Fz",
  "type": "assistant",
  "uuid": "6f55d98b-205d-42e7-af92-9ddf95d485d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jb9Qg6k2DtHfULksv2QA85",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14593,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15804,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14593
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

_source line 9 · 2026-05-21T03:37:19.830Z_

```yaml
tier: best
narrative_guidance: >
  Original framing fully intact. Lead with bias identity theorem (exact, R²≥0.97) and
  'debiasing can hurt' proposition as problem-level discovery. Headline: 'global correction
  worsens subgroup CATE bias by 2-3x; EC-HTE reduces to near-zero with 250-500 expert
  labels.' Three claims at full strength with boundary conditions (n_expert/K ≥ 25,
  det(Ĉ_k) ≠ 0). Diagnostic criterion positioned as practitioner decision rule.
  EC-HTE+PPCI complementarity elevated in abstract. Paper structure: theory → method →
  synthetic → semi-synthetic (real LLM) → real data. exp-008/009 in appendix.
  Four main-text figures: (1) bias mechanism schematic, (2) Δπ×Δτ heatmap,
  (3) diagnostic ROC, (4) budget crossover.

imagined_experiments:
  - name: "HB EC-HTE Synthetic Validation"
    plan_id: "exp-001"
    description: >
      Hierarchical Bayesian Dirichlet-prior confusion matrix estimator with partial pooling,
      full regime sweep (extreme/moderate/homogeneous × n_expert 50-2000 × K=2,4).
      MCMC diagnostics, hyperprior sensitivity, coverage calibration.
    expected_results:
      mcmc_rhat_max: 1.003
      mcmc_ess_min: 1600
      mcmc_divergent: 0
      mcmc_chains: 4
      mcmc_warmup: 1000
      total_mc_runs: 3600
      runtime_min: 70
      hb_vs_mle_rmse_improvement_k2_n50: "5-9%"
      hb_vs_mle_rmse_improvement_k2_n100: "1-2%"
      hb_vs_mle_rmse_improvement_k4_n50_moderate: "6-9%"
      hb_vs_mle_rmse_improvement_k4_n50_extreme_sgC: "23%"
      hb_coverage_min: 0.90
      hb_coverage_median: 0.93
      hyperprior_sensitivity_k2: "<1%"
      hyperprior_sensitivity_k4: "~4-5%"
      singularity_guard_trigger_rate: "2-3% in extreme/n=50 only"
    result_rationale: >
      Best 档要求 MCMC 完全收敛且 HB 在小样本下显著优于 MLE。4-chain NUTS 在 Dirichlet
      后验上收敛性好（共轭结构近似），R̂<1.01 和 ESS>1000 可以可靠达到。HB 的 partial pooling
      在 K=4/n=50 的小子群（~6 个 expert labels）上通过 James-Stein 收缩提供 6-23% RMSE
      改善——这是经典收缩估计量在高维/小样本下的已知优势。K=2/n≥100 时改善收窄至 1-2% 因为
      MLE 本身已有足够样本。Coverage ≥0.90 因为 HB 后验区间自然包含参数不确定性。Hyperprior
      对 K=2 不敏感（仅 2 个子群，先验影响被数据淹没），K=4 时先验在极端子群有 ~5% 影响但
      不改变定性结论。Singularity guard 仅在 extreme/n=50 触发，因为 12% minority subgroup
      在 n=50 下仅有 ~6 labels，混淆矩阵可能出现零行。
    tables:
      - "Table S1: MCMC diagnostics (R̂, ESS, divergences) by config"
      - "Table 1: HB vs MLE vs Laplace RMSE comparison across regime × K × n_expert grid"
      - "Table S2: Hyperprior sensitivity (scale 0.5-2.0×)"
    figures_description:
      - "Figure S1: Posterior trace plots for representative configs (K=4/extreme/n=50)"
    analysis: >
      HB partial pooling 的核心价值在 K=4/n≤100 区间：子群样本量小到 MLE 不稳定，但又不至于
      小到 shrinkage 反而有害。Best 档下 4-chain MCMC 消除了 2-chain 的收敛问题（ESS 提升
      ~4x），singularity guard 处理了极端情况。这为后续所有实验提供了可靠的 CM 估计基础设施。
      Boundary condition 明确：n_expert/K ≥ 25 per subgroup 是 HB 的推荐操作区间。

  - name: "Bias Identity Verification"
    plan_id: "exp-002"
    description: >
      解析推导 bias = f(Δπ, Δτ) identity，在 K=2 和 K=4 上通过 MC 验证。
      构造 'debiasing can hurt' 的两子群反例。
    expected_results:
      r2_k2: 0.994
      r2_k4: 0.974
      tightness_ratio_k2_median: 1.003
      tightness_ratio_k4_median: 1.023
      debiasing_hurts_pct: 50
      debiasing_hurts_pct_detail: "260/520 non-trivial configs"
      debiasing_hurts_threshold_delta_misclass: 0.12
      max_bias_ratio_k2: 2.86
      max_bias_ratio_k4: 5.9
      bias_identity_formula: "bias_k = Σ_j (π_j - π̄)(τ_j - τ̄) × w_j"
      coverage_2se_k2: 0.951
      coverage_2se_k4: 0.940
    result_rationale: >
      Bias identity 是精确的群体级恒等式（不是 bound），R² 衡量的是 MC 有限样本噪声对
      解析预测的偏差。K=2 时 R²≈0.994 因为两子群的 Δπ×Δτ 乘积形式完全精确；K=4 时
      降至 0.974 因为 sum-of-products 形式有更多交叉项，MC 噪声累积更大。Debiasing hurts
      在恰好 50% 的参数空间成立——这是几何必然：当 Δπ 和 Δτ 同号时 global correction
      产生的 bias 方向与 naive bias 相同但幅度更大。Max bias ratio K=2 约 2.9x 受限于
      两子群的自由度；K=4 达 5.9x 因为更多子群 → 更大的 π heterogeneity spread →
      global correction 对低误差子群的 over-correction 更严重。阈值 Δπ≈0.12 是
      debiasing hurts 的临界点，与 LLM annotation 的实际异质性范围 [0.12, 0.25] 吻合——
      说明在实际场景中该问题大概率出现。
    tables:
      - "Table 2: Bias identity verification — R², tightness ratio by K"
      - "Table 3: Debiasing-hurts frequency and max magnification by regime"
    figures_description:
      - "Figure 1 (main): Δπ×Δτ bias amplification heatmap, K=2 and K=4 panels"
      - "Figure S2: Scatter of analytic prediction vs MC bias, colored by regime"
    analysis: >
      R²≥0.97 对 K=4 验证了 sum-of-products 推广在实践中成立。50% debiasing-hurts 率是
      最强叙事点——说明 global correction 在一半参数空间是有害的，且 K scaling (2.9x→5.9x)
      意味着子群越多越危险。Δπ≈0.12 阈值与 exp-003 实测 LLM heterogeneity 直接呼应，
      建立了理论→实证的桥梁。

  - name: "Semi-Synthetic CSS Benchmark with Real LLM Annotations"
    plan_id: "exp-003"
    description: >
      TweetEval sentiment (N=45K) 上注入已知 CATE 结构，GPT-4.1 标注，测量子群特异性
      误分率，EC-HTE vs baselines 全面比较。子群变量：has_hashtag, text_length。
    expected_results:
      dataset: "TweetEval sentiment (N≈45000)"
      llm: "GPT-4.1"
      n_subgroups: 4
      subgroup_vars: ["has_hashtag", "text_length_bin"]
      misclass_rates_by_subgroup:
        S0_short_no_hashtag: 0.06
        S1_short_hashtag: 0.11
        S2_long_no_hashtag: 0.14
        S3_long_hashtag: 0.23
      delta_pi_max_min: 0.17
      bias_amplification_median: 2.8
      bias_amplification_max: 8.5
      ec_hte_bias_reduction_pct_n250: 62
      ec_hte_bias_reduction_pct_n500: 73
      ec_hte_rmse_ratio_n500_k4: 1.12
      coverage_ec_hte_95_n500: 0.94
      coverage_naive: 0.78
      coverage_global: 0.82
      debiasing_hurts_confirmed: true
      debiasing_hurts_subgroups: ["S0_short_no_hashtag"]
      hb_vs_mle_s2_n100_improvement: "+35%"
      hb_blowup_s3_n50: true
      mc_runs: 100
    result_rationale: >
      GPT-4.1 在 sentiment 分类上的整体 accuracy ~85-90%，但误分率跨子群异质性显著：
      短文本无 hashtag（S0）接近模型训练分布，误分率最低（~6%）；长文本含 hashtag（S3）
      因多义性、讽刺、非标准语法，误分率最高（~23%）。Δπ=0.17 落在 best 档 [0.12, 0.25]
      范围内——这不是人为构造，而是 LLM 对不同文本特征的已知 sensitivity 差异。
      Bias amplification median 2.8x 源于：global CM 将 S0 的低误差率"拉高"至 pooled
      水平，对 S0 的 CATE 产生反向偏差；S3 则被"拉低"。中位 2.8x 在 best 档 [2.0, 4.0]
      中部，因为 4 子群的 heterogeneity spread 足够大但非人工极端化。
      EC-HTE 在 n=500 时 bias 减少 73%，因为每子群 ≥125 labels（满足 ≥25 boundary）
      足以估计子群特异 CM。RMSE ratio 1.12 反映了 per-subgroup CM 估计引入的额外方差，
      但已被 bias 减少主导。Coverage 0.94 因为 HB 后验区间正确反映了 CM 估计的不确定性。
      HB 在 S2 (12% minority, n=100 → ~12 labels) 仍有 35% RMSE 改善（partial pooling
      从多数子群借力），但 S3/n=50 (~6 labels) 出现 blowup——与 exp-001 一致，确认
      boundary condition。
    tables:
      - "Table 4: Per-subgroup GPT-4.1 misclassification rates on TweetEval sentiment"
      - "Table 5: Bias amplification — naive vs global vs EC-HTE across n_expert grid"
      - "Table S3: Full method × subgroup × n_expert results matrix"
    figures_description:
      - "Figure 2 (main): Bias mechanism schematic — global over/under-correction by subgroup"
      - "Figure S3: GPT-4.1 confusion matrices per subgroup (heatmap)"
    analysis: >
      此实验是 best 档的核心支柱——用真实 LLM 标注（非模拟）确认了 bias mechanism 在
      practical magnitudes 下存在。Δπ=0.17 > 理论阈值 0.12，说明标准 LLM annotation
      pipeline 默认处于 debiasing-hurts 区域。Semi-synthetic 设计保留了 ground truth
      CATE 可对比，同时 misclassification structure 完全来自真实 LLM，不可被质疑为
      人工构造。这直接回应了 reviewer concern "how realistic is this heterogeneity?"。

  - name: "Real-Data Case Study — UC Berkeley Hate Speech"
    plan_id: "exp-004"
    description: >
      UC Berkeley Measuring Hate Speech corpus 上的 pattern consistency 分析。
      设计 (T,Y,Z,S) 映射，比较 global vs EC-HTE 的 CATE 分布差异，
      bootstrap CI 量化差异显著性。
    expected_results:
      dataset: "UC Berkeley Measuring Hate Speech"
      n_samples: "~39000 annotations, ~27000 unique comments"
      treatment_var: "target_identity_mention (binary)"
      outcome_var: "hate_speech_severity (continuous or binarized)"
      effect_modifier: "LLM-predicted comment_type (e.g., derogatory vs non-derogatory)"
      subgroup_var: "annotator_demographic (race/gender) or target_group"
      n_subgroups: 4
      llm_annotation_model: "GPT-4.1"
      delta_pi_observed: 0.15
      max_cate_shift_se: 3.2
      n_subgroups_with_shift_gt_2se: 2
      global_vs_ec_hte_qualitative_difference: true
      domain_consistency: "EC-HTE CATE directions consistent with known hate speech literature"
      bootstrap_ci_non_overlap: "2 of 4 subgroups show non-overlapping 95% CIs"
      ec_hte_coverage_bootstrap: 0.94
    result_rationale: >
      UC Berkeley 数据集有丰富的 demographic 元数据和连续严重性评分，适合构造因果框架。
      Treatment = identity mention 是自然的二元处理变量；outcome = severity 有足够变异。
      GPT-4.1 对 comment_type 的误分率在不同 target group/语境下必然异质——针对种族
      的仇恨言语通常更显式（低误分），而性别相关或隐含仇恨（讽刺、微攻击）误分率高。
      Δπ=0.15 合理（与 exp-003 量级一致）。Max CATE shift 3.2 SE 落在 best 档
      [2.0, 5.0] 范围内——这意味着至少 1 个子群上 global 和 EC-HTE 给出统计显著不同的
      CATE 估计，差异达 3.2 个标准误，不可归因于抽样波动。两个子群 shift>2SE 是合理的：
      高误差子群（隐含仇恨类型）的 CATE 被 global correction 系统性扭曲；低误差子群
      （显式仇恨）被 over-correct。Domain consistency 成立因为 EC-HTE 的子群特异校正
      消除了 mixing bias，恢复了符合 prior knowledge 的 CATE 方向（如：identity mention
      对 severity 的影响在 derogatory 语境下更大，这是文献一致的）。
    tables:
      - "Table 6: UC Berkeley hate speech — per-subgroup LLM misclassification rates"
      - "Table 7: Global vs EC-HTE CATE estimates with bootstrap 95% CIs by subgroup"
    figures_description:
      - "Figure S4: CATE distributions — global vs EC-HTE kernel density plots per subgroup"
      - "Figure S5: Bootstrap CI comparison forest plot"
    analysis: >
      Real-data case study 不追求 ground-truth benchmark（没有真实 CATE 可比较），而是
      展示 pattern consistency: (1) LLM misclassification heterogeneity 确实存在，
      (2) global vs EC-HTE 产生 qualitatively different 结论，(3) EC-HTE 结论与
      domain knowledge 一致。3.2 SE 的 max shift 足以让 reviewer 相信差异不是噪声。
      这回应了 "theoretical concern without practical consequence" 的潜在质疑。
      Framing: "illustrative application demonstrating the practical relevance of the
      bias mechanism, not a ground-truth validation."

  - name: "Diagnostic Criterion Cross-Validated AUC"
    plan_id: "exp-005"
    description: >
      Δπ×Δτ product 作为 global correction 失败的诊断指标。
      Leave-one-setting-out 交叉验证 ROC 分析。
    expected_results:
      n_settings: "≥20 (from exp-001/002/003 configs)"
      diagnostic_metric: "max_subgroup(Δπ_k × Δτ_k)"
      cv_method: "leave-one-setting-out"
      subgroup_level_auc: 0.88
      setting_level_auc: 0.75
      subgroup_correlation_pi_tau_product_vs_bias: 0.86
      optimal_threshold: 0.015
      sensitivity_at_threshold: 0.82
      specificity_at_threshold: 0.78
      low_pi_hurt_pct: 85
      high_pi_hurt_pct: 15
    result_rationale: >
      Subgroup-level AUC 0.88 落在 best 档 [0.83, 0.95]——Δπ×Δτ product 是 exact identity
      的直接操作化，在子群级别预测 bias 方向（hurt vs help）的能力由理论保证，AUC 的偏离
      来源仅为 MC 有限样本噪声。Setting-level AUC 0.75 落在 [0.7, 0.85]，低于 subgroup
      AUC 因为 setting-level aggregation（"此 setting 中是否有任何子群被 hurt"）是一个
      更粗粒度的二分类任务，存在 threshold-sensitive 的边界 settings（Δπ 接近 0.12 阈值）。
      Cross-validation 而非 in-sample 使 AUC 略低但方法学上无可挑剔——这是 best 档要求的
      key differentiator。Correlation 0.86 与 exp-002 的 R²=0.97 一致（r≈√0.97≈0.985
      在群体级，0.86 在有限样本下合理）。Low-π 子群 85% 被 hurt 确认了 bias mechanism
      的方向性：低误差子群被 global correction over-correct。
    tables:
      - "Table 8: Diagnostic criterion — CV AUC, sensitivity, specificity"
      - "Table S4: Per-setting diagnostic scores and actual hurt/help classification"
    figures_description:
      - "Figure 3 (main): Diagnostic ROC curve with operating point annotated"
      - "Figure S6: Δπ×Δτ product vs observed bias scatter, colored by hurt/help"
    analysis: >
      Setting-level AUC ≥0.70 是 best 档的 critical threshold——低于此则 diagnostic 作为
      practitioner tool 不可用。0.75 意味着 clinician-grade discrimination：给定 pilot
      data 中的 Δπ 和 Δτ 估计，能 75% 准确判断是否需要 stratified correction。
      这直接支撑 Claim 3，且连接到 Claim 2 的 expert budget recommendation：当 diagnostic
      flags high heterogeneity → use EC-HTE → budget per exp-006 crossover points。

  - name: "Expert Label Budget Sensitivity"
    plan_id: "exp-006"
    description: >
      n_expert ∈ {50,100,250,500,1000,2000} × K ∈ {2,4} × regime ∈ {extreme,moderate}
      系统性扫描，确定 EC-HTE vs Global 的 RMSE crossover 点。
    expected_results:
      grid: "n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]"
      mc_runs: 100
      total_configs: 24
      crossover_points:
        K2_extreme: 250
        K2_moderate: "never (global always better on RMSE)"
        K4_extreme: 1000
        K4_moderate: 2000
      ec_hte_rmse_ratio_n500_k4_extreme: 1.08
      ec_hte_rmse_ratio_n500_k4_moderate: 1.35
      ec_hte_rmse_ratio_n1000_k4_extreme: 0.92
      hb_vs_mle_wins: "22/24 configs"
      hb_best_improvement_over_mle: "+42% (K4/moderate/n50/sgC)"
      hb_convergence_to_mle: "n≥1000 (<0.5% difference)"
      bias_at_crossover_K2_extreme: "EC-HTE |bias| < 0.01 vs global |bias| ≈ 0.08"
    result_rationale: >
      Crossover 依赖 K 和 regime 是 bias-variance tradeoff 的直接后果：EC-HTE 每子群 CM
      估计引入 O(K/n_expert) 的额外方差，只有当 bias reduction 超过此方差增量时才值得。
      K=2/extreme crossover 在 n=250（每子群 ~125 labels）因为 extreme regime 有大
      bias（Δπ>0.15）且只需估计 2 个 CM。K=4/extreme 延迟到 n=1000（每子群 ~250 labels）
      因为需估计 4 个 CM，但 extreme 的高 bias 仍使 crossover 可达。K=2/moderate 永不
      crossover 因为 moderate regime 的 Δπ≈0.05-0.08 < 阈值 0.12，bias 太小不足以
      补偿额外方差——这正是 diagnostic criterion 的价值所在：它告诉你何时 NOT to use EC-HTE。
      RMSE ratio 1.08 at n=500/K=4/extreme 落在 best 档 [1.0, 1.2]，表明 EC-HTE 在此
      点已接近 competitive。HB 在 22/24 configs 优于 MLE 因为 partial pooling 的
      shrinkage 几乎总是有益的（James-Stein 现象），唯一例外是子群样本量已足够大使
      MLE 最优的 configs。
    tables:
      - "Table S5: Full RMSE grid — n_expert × K × regime × method"
      - "Table 9: Crossover summary with per-K/regime budget recommendations"
    figures_description:
      - "Figure 4 (main): Budget crossover curves — EC-HTE vs Global RMSE by n_expert, paneled by K×regime"
    analysis: >
      Budget sensitivity 是论文的 practical backbone：它将 Claim 2 从理论可能转化为
      actionable guidance。Key message for practitioners: K=2/extreme 只需 250 labels
      （约 $500 annotation cost），K=4/extreme 需 1000 labels。Moderate regime 下
      global correction 更安全——直接连接 Claim 3 的 diagnostic criterion。
      "Expert Budget Recommendation" subsection 用此数据给出 per-K guidelines。

  - name: "PPCI + DSL Baseline Comparison"
    plan_id: "exp-007"
    description: >
      4 个 DGP（covariate-only/outcome-only/both/none）× 8 methods × n_expert grid。
      验证 EC-HTE+PPCI 互补性，DSL per-subgroup baseline，纯 covariate-error 控制条件。
    expected_results:
      dgps: ["A_covariate_only", "B_outcome_only", "C_both_errors", "D_no_error"]
      methods: 8
      mc_runs: 100
      total_rows: 6912
      dgp_a_covariate_only:
        ec_hte_bias_z0: 0.008
        ppci_bias_z0: 0.19
        ec_hte_ppci_bias_z0: 0.008
        global_bias_z0: 0.15
        naive_bias_z0: 0.22
        dsl_per_subgroup_bias_z0: 0.04
        ec_hte_vs_ppci_ratio: "24x better (PPCI ineffective on pure covariate error)"
      dgp_b_outcome_only:
        ppci_bias_z0: 0.005
        ec_hte_bias_z0: 0.17
        ec_hte_ppci_bias_z0: 0.005
      dgp_c_both_errors_extreme_n250:
        ec_hte_ppci_bias_z0: 0.005
        ec_hte_bias_z0: 0.178
        ppci_bias_z0: 0.004
        naive_bias_z0: 0.251
        ec_hte_ppci_rmse_z0: 0.225
        ec_hte_ppci_vs_ec_hte_bias_reduction_pct: 97
      dgp_c_both_errors_n500:
        ec_hte_ppci_bias_z0: 0.005
        ec_hte_ppci_rmse_z0: 0.142
        ec_hte_bias_z0: 0.088
      dgp_d_no_error:
        all_methods_bias: "< 0.01"
        all_methods_equivalent: true
      dsl_per_subgroup_vs_ec_hte:
        rmse_ratio_n250: 1.3
        rmse_ratio_n500: 1.15
        advantage: "EC-HTE: partial pooling reduces variance; DSL: no cross-subgroup shrinkage"
      coverage_ec_hte_ppci: 1.0
    result_rationale: >
      DGP A（纯 covariate error）是 EC-HTE 的 home turf：误分率异质性完全在 covariate 侧，
      EC-HTE 通过子群特异 M⁻¹ 矩阵精确校正，bias 降至 ~0.008（MC 噪声水平）。PPCI 在
      DGP A 几乎无效（bias 0.19 ≈ naive 0.22）因为 PPCI rectifier 校正的是 outcome-side
      systematic error，对 covariate 侧的 mixing matrix 结构无从利用。这是 best 档的
      关键论证点：EC-HTE 和 PPCI 解决不同类型的误差。
      DGP C（both errors）下 ec_hte_ppci 组合达 97% bias reduction vs ec_hte alone——
      落在 best 档 [80, 97] 上限。原因：EC-HTE 处理了 covariate-side structured error
      （M⁻¹），PPCI rectifier 处理了 residual outcome-side error，组合覆盖了全部误差源。
      97% 而非 100% 因为有限样本下两个校正的噪声不完全独立。
      DSL per-subgroup 在 DGP A 上 bias=0.04 优于 global（0.15）但劣于 EC-HTE（0.008）——
      DSL 在 estimand level 操作缺乏 measurement model level 的结构利用，且无 cross-subgroup
      shrinkage 导致更高方差。RMSE ratio 1.3→1.15 随 n 增加收敛，因为大样本下 shrinkage
      优势消失。
    tables:
      - "Table 10: Method comparison across 4 DGPs — bias, RMSE, coverage"
      - "Table S6: Full 6912-row results summary statistics"
    figures_description:
      - "Figure S7: DGP A pure-covariate-error control — EC-HTE vs PPCI bias comparison"
      - "Figure S8: DGP C composition — bias reduction waterfall (naive → ec_hte → ec_hte_ppci)"
    analysis: >
      4-DGP 设计是论文方法学最强的贡献之一——通过正交化误差源，精确定位了 EC-HTE 和 PPCI
      的 respective domains。DGP A 的 pure-covariate control 消除了 "why not just use PPCI
      for everything" 的 reviewer 质疑。ec_hte_ppci 在 DGP C 的 97% bias reduction
      证明了互补性不是概念上的而是 quantitatively massive。Coverage 1.0 因为 HB 后验 +
      PPCI confidence set 的联合区间足够保守。

  - name: "Multiple LLM Annotator Comparison"
    plan_id: "exp-008"
    description: >
      GPT-4.1 vs Qwen3-235B-A22B vs Claude Sonnet 4.6 在 TweetEval sentiment 上的
      误分率异质性比较，EC-HTE benefit 与 LLM quality 的关系。
    expected_results:
      dataset: "TweetEval sentiment"
      llms: ["GPT-4.1", "Qwen3-235B-A22B", "Claude Sonnet 4.6"]
      overall_accuracy:
        gpt4_1: 0.88
        qwen3_235b: 0.82
        claude_sonnet: 0.86
      delta_pi_max_min:
        gpt4_1: 0.17
        qwen3_235b: 0.22
        claude_sonnet: 0.14
      bias_amplification_median:
        gpt4_1: 2.8
        qwen3_235b: 3.6
        claude_sonnet: 2.3
      ec_hte_bias_reduction_pct_n500:
        gpt4_1: 73
        qwen3_235b: 78
        claude_sonnet: 65
      correlation_delta_pi_vs_ec_hte_benefit: 0.92
      subgroup_error_pattern_consistency: "All 3 LLMs show higher error on long+hashtag texts"
    result_rationale: >
      三个 LLM 有不同的 overall accuracy 但共享相似的 error heterogeneity pattern——
      长文本含 hashtag 对所有 LLM 都更难（多义性、讽刺检测是通用难题，不依赖于特定模型
      架构）。Qwen3-235B Δπ 最大（0.22）因为 overall accuracy 最低（0.82），错误率的
      子群间 spread 与 base error rate 正相关（误差越多，子群间差异有更大绝对空间）。
      Claude Sonnet Δπ 最小（0.14）因为 accuracy 中等偏上且 error pattern 更均匀。
      EC-HTE benefit 与 Δπ 高度相关（r=0.92）——直接验证了 Theorem 1 的 operational
      implication：误分异质性越大，stratified correction 越必要。Qwen3 的 78% bias
      reduction 最高因为 global correction 在高异质性下"做错得最多"。所有 LLM 的 error
      pattern 一致性说明这不是模型特异的 artifact，而是任务固有的 subgroup difficulty
      structure。
    tables:
      - "Table S7: Per-LLM per-subgroup misclassification rates"
      - "Table S8: EC-HTE benefit comparison across LLMs"
    figures_description:
      - "Figure S9: Δπ vs EC-HTE bias reduction scatter across 3 LLMs"
    analysis: >
      此实验在 appendix（P1 priority），但对 generalizability 至关重要：证明 bias mechanism
      不是 GPT-4.1 特异的，而是 LLM-as-annotator paradigm 的 structural property。
      Correlation 0.92 between Δπ and EC-HTE benefit 是 Theorem 1 的 empirical corollary，
      强化了 diagnostic criterion 的 practical value。

  - name: "Adaptive Expert Annotation Allocation"
    plan_id: "exp-009"
    description: >
      CATE-weighted allocation（targeting high-CATE × high-error subgroups）vs uniform
      和 uncertainty-only allocation 的 RMSE 比较。
    expected_results:
      allocation_strategies: ["uniform", "uncertainty_only", "cate_weighted", "oracle_optimal"]
      n_expert_total: [250, 500, 1000]
      n_subgroups: 4
      rmse_improvement_cate_weighted_vs_uniform:
        n250: "18%"
        n500: "12%"
        n1000: "6%"
      rmse_improvement_cate_weighted_vs_uncertainty:
        n250: "8%"
        n500: "5%"
        n1000: "3%"
      oracle_gap_pct:
        n250: "12%"
        n500: "8%"
        n1000: "4%"
      optimal_allocation_pattern: "60% to high-error subgroups, 40% split among rest"
      mc_runs: 100
    result_rationale: >
      CATE-weighted allocation 在 n=250 时改善最大（18% vs uniform）因为稀缺资源下
      allocation efficiency 最重要——将更多 labels 分配到 high-CATE × high-error 子群
      减少了对 total RMSE 贡献最大的 component。随 n 增加改善收窄（12%→6%）因为所有
      子群最终都获得足够 labels。Uncertainty-only allocation 已部分捕获了正确方向（高
      误差子群获得更多 labels），但忽略了 CATE magnitude——一个低 CATE 高误差子群的
      CM 估计精度对 total RMSE 贡献小。Oracle gap 12%→4% 表明 CATE-weighted 在小 n 时
      的 pilot CATE 估计噪声限制了其效率，但大 n 时接近 oracle。60/40 的最优分配比例
      反映了 extreme regime 下子群误差率的不对称性（S3 误差率是 S0 的 ~4 倍）。
    tables:
      - "Table S9: Allocation strategy comparison — RMSE by n_expert and strategy"
    figures_description:
      - "Figure S10: Allocation efficiency curves — RMSE vs n_expert by strategy"
    analysis: >
      此实验在 appendix（P2 priority），为 practitioners 提供进阶 guidance：在 expert
      budget 受限时如何最优分配。18% 的 n=250 改善等价于"同等 RMSE 下节省 ~45 labels"——
      对 annotation 预算有直接的美元价值。但 diminishing returns at n≥1000 说明在充裕
      预算下 uniform 已足够好，降低了 implementation complexity。

  - name: "Robustness to Misspecified Subgroup Structure"
    plan_id: "exp-010"
    description: >
      测试 EC-HTE 在子群定义噪声化（misspecified）时的表现：(a) subgroup labels 有
      随机噪声，(b) 真实子群结构与 conditioning variable 不对齐。
    expected_results:
      conditions:
        - name: "well_specified"
          ec_hte_bias: 0.01
          ec_hte_rmse: 0.15
        - name: "10pct_label_noise"
          ec_hte_bias: 0.025
          ec_hte_rmse: 0.17
          rmse_increase_vs_well_specified: "13%"
        - name: "20pct_label_noise"
          ec_hte_bias: 0.05
          ec_hte_rmse: 0.21
          rmse_increase_vs_well_specified: "40%"
        - name: "orthogonal_subgroup"
          ec_hte_bias: 0.09
          ec_hte_rmse: 0.25
          note: "EC-HTE degrades to near-global performance"
        - name: "partially_aligned_subgroup"
          ec_hte_bias: 0.04
          ec_hte_rmse: 0.19
          rmse_increase_vs_well_specified: "27%"
      hb_shrinkage_behavior: "Noisy subgroups → stronger shrinkage toward global mean"
      global_correction_baseline_rmse: 0.22
      ec_hte_still_beats_global_up_to: "20% label noise"
      mc_runs: 100
    result_rationale: >
      HB partial pooling 的 shrinkage 机制提供了自然的 robustness：当子群定义有噪声时，
      子群内 CM 估计量的似然变得更扁平（less informative），HB 自动增加向 global mean 的
      shrinkage。10% noise 下 RMSE 增加 13% 是 graceful——子群 CM 仍捕获了 90% 的真实
      heterogeneity structure。20% noise 下增加 40% 但仍优于 global（0.21 < 0.22），因为
      即使有噪声的子群特异 CM 也比完全忽视异质性的 pooled CM 更好。Orthogonal subgroup
      （conditioning variable 与真实结构正交）时 EC-HTE 退化到 near-global 而非更差——
      这是 shrinkage estimator 的已知 property：worst case = pooled，不会 blow up。
      Partially aligned（50% 信号）时 RMSE 0.19，位于 well-specified 和 orthogonal 之间，
      符合线性插值预期。这直接回应 reviewer concern 4（"how sensitive to subgroup
      definition?"）：答案是 graceful degradation，worst case 退回 global，不会更差。
    tables:
      - "Table S10: Robustness analysis — RMSE by misspecification level"
    figures_description:
      - "Figure S11: RMSE degradation curve as function of subgroup noise level"
    analysis: >
      此实验（P2, appendix）回答了一个关键 reviewer 担忧。最重要的结论是 EC-HTE 的
      worst-case 是 global correction（orthogonal 条件下），而非比 global 更差。这意味着
      使用 EC-HTE 没有 downside risk——即使子群定义完全错误，也只是"浪费了" expert labels
      用于无用的子群 CM 估计，结果回退到 global 水平。HB shrinkage 是这个 safety net 的
      机制：数据不支持子群差异时，后验自动收缩到 shared mean。

  - name: "Causal Forest Integration"
    plan_id: "exp-011"
    description: >
      CausalForestDML 上 EC-HTE 后校正 vs naive forest vs globally-corrected forest。
      验证 bias reduction pattern 在非参数 CATE 估计器上一致。
    expected_results:
      estimator: "CausalForestDML (econml)"
      n_mc: 100
      n_configs: 8
      mean_abs_bias:
        naive_forest: 0.156
        global_forest: 0.107
        ec_hte_forest: 0.061
      mean_rmse:
        naive_forest: 0.178
        global_forest: 0.166
        ec_hte_forest: 0.229
      ec_hte_bias_reduction_vs_naive: "61%"
      ec_hte_bias_reduction_vs_global: "43%"
      debiasing_hurts_cases: 9
      debiasing_hurts_max_ratio: 5.9
      debiasing_hurts_detail: "K=4/extreme/sg0: global 5.9x worse than naive"
      k2_n500_ec_hte_bias_range: "0.004-0.013"
      k2_n500_global_bias_range: "0.033-0.109"
      rmse_tradeoff_note: "EC-HTE RMSE 28% higher than global mean — bias-variance tradeoff"
      pattern_consistent_with_diff_in_means: true
    result_rationale: >
      CausalForest 的非线性 CATE 估计放大了 bias mechanism：forest 的 adaptive splitting
      将 subgroup-level bias 传播到 leaf-level 估计中，且非线性变换使 global correction
      的 over/under-correction 效应非线性放大。Debiasing hurts max ratio 5.9x（vs
      diff-in-means 的 2.86x）正是因为 forest 在 K=4/extreme 的低误差子群（sg0）上
      将 global correction 的 over-correction 通过 splitting 进一步极化。EC-HTE 在
      K=2/n=500 上 bias 降至 0.004-0.013 因为每子群有足够 labels（≥250）精确估计 CM，
      forest 的 pseudo-outcome 被正确校正。RMSE 28% 更高反映了子群级 CM 估计噪声在
      forest 的 variance-sensitive splitting 中被放大——这是 bias-variance tradeoff 的
      honest disclosure。Pattern consistency with diff-in-means 确认了 bias mechanism
      是 estimator-agnostic：无论用参数还是非参数方法，global correction 在高 Δπ 下
      都会 hurt。这回堵了 "your results only hold for simple estimators" 的 reviewer concern。
    tables:
      - "Table 11: CausalForest — naive vs global vs EC-HTE bias and RMSE"
      - "Table S11: Per-config detailed forest results"
    figures_description:
      - "Figure S12: Forest debiasing-hurts magnification — K=4/extreme detail"
    analysis: >
      CausalForest 实验将 Claim 2 从 diff-in-means toy estimator 扩展到 state-of-the-art
      HTE 方法。5.9x 的 debiasing hurts ratio 是论文最大的单个数字——适合作为 abstract
      中的 "up to" claim。RMSE tradeoff 必须 honest disclose：EC-HTE 用 bias 换
      variance，在 n<500 时不一定 RMSE-optimal。这连接到 exp-006 的 budget guidance
      和 exp-005 的 diagnostic criterion，形成完整的 decision framework。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f55d98b-205d-42e7-af92-9ddf95d485d6",
  "isSidechain": false,
  "requestId": "req_011CbF1SfHMqCrGzAjioP8Fz",
  "type": "assistant",
  "uuid": "5d7a37c4-1ed9-4ba8-9f3d-8c164d029d5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jb9Qg6k2DtHfULksv2QA85",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14593,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15804,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15804,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14593
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Real LLM annotations exhibit substantial misclassification heterogeneity on CSS tasks; semi-synthetic and real-data experiments confirm bias mechanism at p…",
  "leafUuid": "5d7a37c4-1ed9-4ba8-9f3d-8c164d029d5d",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE validation: bias mechanism, diagnostic criterion, real LLM labels",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Real LLM annotations exhibit substantial misclassification heterogeneity on CSS tasks; semi-synthetic and real-data experiments confirm bias mechanism at p…",
  "leafUuid": "5d7a37c4-1ed9-4ba8-9f3d-8c164d029d5d",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE validation: bias mechanism, diagnostic criterion, real LLM labels",
  "sessionId": "8c906e6c-7366-4d44-99bf-450a9e8cb9b4"
}
```

---
