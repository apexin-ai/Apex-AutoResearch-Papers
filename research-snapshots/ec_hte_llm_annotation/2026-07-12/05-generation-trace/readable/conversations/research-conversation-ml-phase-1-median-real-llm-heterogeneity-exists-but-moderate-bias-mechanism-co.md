# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Real LLM heterogeneity exists but moderate; bias mechanism confirmed at sm

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/23ff0975-bed3-4c9c-bd2c-5b8a0f153224.jsonl`
- **Structured JSON:** [`6274847a7ad098c47b3c.json`](../../sessions/62/6274847a7ad098c47b3c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:37:22.924Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:37:22.924Z",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Real LLM heterogeneity exists but moderate; bias mechanism confirmed at smaller magnitudes than synthetic; EC-HTE works but requires larger expert budgets than hoped; diagnostic reframed from setting-level threshold to subgroup-level screening tool\n核心假设：['GPT-4.1 Δπ across subgroups ~ 0.05-0.12 — measurable but not extreme-regime levels', 'Bias amplification 1.3-2x with real LLM labels — visible but below synthetic headline numbers', 'EC-HTE RMSE competitive only at n_expert ≥ 1000 for K=4; bias advantage clear but variance penalty dominates at smaller budgets', 'Diagnostic setting-level AUC stays 0.50-0.65 even after refinement — not a reliable decision rule; subgroup-level AUC robust at ~0.80', 'UC Berkeley real data shows directional CATE differences but most subgroups within overlapping CIs', 'ec_hte_ppci composition works but advantage over ec_hte alone modest due to lower outcome-error in real data']\n关键指标范围：{'semi_synth_llm_delta_pi': [0.05, 0.12], 'semi_synth_llm_bias_amplification_median': [1.3, 2.0], 'ec_hte_bias_reduction_pct_n500': [30, 55], 'ec_hte_rmse_ratio_n500_k4': [1.2, 1.6], 'diagnostic_cv_auc_setting': [0.5, 0.65], 'diagnostic_cv_auc_subgroup': [0.75, 0.85], 'real_data_max_cate_shift_se': [1.0, 2.0], 'coverage_ec_hte_95': [0.85, 0.93], 'ec_hte_ppci_bias_reduction_vs_ec_hte_dgpC': [40, 80]}\n叙事方向：Bias identity (Claim 1) holds exactly — this is mathematical, not empirical. Empirical headline softened: 'up to 2-3x in controlled synthetic; 1.3-2x with current SOTA LLMs on standard CSS tasks, expected to increase on harder annotation tasks.' Claim 2 reframed: EC-HTE provides principled bias reduction but requires honest bias-RMSE tradeoff disclosure — add 'When to Use EC-HTE' subsection with per-K budget recommendations replacing the '250 labels' headline. Claim 3 substantially weakened: drop 'computable diagnostic threshold' from contributions; reframe as 'subgroup-level misclassification audit protocol' — subgroup AUC ~0.80 supports identifying which subgroups are at risk, not whether the overall setting needs correction. Strengthen theoretical framing: lead with the identity and CausalForest amplification (5.9x, already validated) to argue the problem scales with estimator complexity. Add forward-looking argument: as LLMs are applied to harder CSS tasks (cross-lingual, implicit sentiment, complex framing), heterogeneity will increase. Paper needs ~0.5 page more for limitations; move exp-008/009 plus one main-text table to appendix to accommodate.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ec_hte_llm_annotation\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 2-3x (median across configurations), with extreme cases exceeding 20x. Global correction increases subgroup-level bias in ~50% of the parameter space.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction in moderate-sized subgroups by borrowing strength across groups (classic James-Stein shrinkage). **Boundary condition**: when expert labels per subgroup < ~25 (e.g., n_expert=50 with 12% minority subgroup → ~6 labels) AND subgroup parameter is far from group mean, shrinkage can be harmful — stratified MLE is preferred. Recommended: n_expert such that smallest subgroup contains ≥25 expert labels. **NOTE**: exact improvement magnitudes pending full 100 MC confirmation (current estimates from n_mc=2 dry-run). Demonstrated with both difference-in-means and CausalForestDML (exp-011: consistent bias reduction pattern, ec_hte_forest |bias|=0.06 vs naive 0.16). CausalForest amplifies the debiasing-hurts effect (up to 5.9x in K=4/extreme) due to nonlinear CATE estimation.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis across computational social science (CSS) — e.g., sentiment framing moderates message effectiveness, hate speech type moderates intervention impact. LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education; documented across CSS tasks including sentiment, stance, toxicity). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as \"problem identification + principled solution\" not \"new estimation technique.\"\n\n- **Headline result template**: \"On semi-synthetic CSS benchmarks (sentiment analysis, hate speech detection), global correction worsens subgroup CATE bias by 2-3x (median), with up to 20x in extreme cases; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels.\"\n\n- **Oracle framing**: When reporting DGP C results where ec_hte_ppci outperforms oracle, always use \"covariate-oracle\" (true Z + observed Y), never unqualified \"oracle\". Frame as \"composite correction is necessary and sufficient when both error types coexist\" — NOT \"beats oracle\". The result is by construction (ec_hte_ppci corrects both error types; covariate-oracle only corrects one), not surprising.\n\n## Key Contributions (ordered for paper)\n\n1. **Bias decomposition identity**: Exact population-level identity: bias ∝ misclassification heterogeneity × CATE heterogeneity (Δπ×Δτ product form). NOT a bound — it is an exact identity under A1–A4; finite-sample R² measures MC noise, not bound looseness. Includes \"debiasing can hurt\" proposition with constructive example. Frame as \"bias decomposition\" or \"bias identity\" throughout — never \"bias bound.\" (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **EC-HTE + PPCI complementarity**: EC-HTE is a structured correction exploiting mixing matrix structure for covariate-side error; PPCI rectifier is a general-purpose residual correction that captures any systematic error (including outcome-side). They are complementary, not orthogonal — PPCI alone can partially correct covariate error but less efficiently than M⁻¹; in composition, EC-HTE handles the structured covariate error precisely, and the residual rectifier handles remaining outcome error. Composition achieves best-of-both when both error types are present. Elevate in abstract and contributions list. (Method + Empirical)\n5. **Comprehensive validation**: Synthetic + semi-synthetic + real-data case study (pattern consistency, not ground-truth benchmark) with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI / DSL?\"** — PPCI rectifier is a general-purpose correction that captures any systematic error (covariate + outcome); EC-HTE is a structured correction exploiting mixing matrix structure specifically for covariate-side error. They are complementary: EC-HTE alone is more efficient for covariate error (uses M⁻¹ structure), PPCI alone can partially correct covariate error but with higher variance (limited by gold subset). In composition, EC-HTE handles structured covariate error, residual rectifier handles outcome error. DSL applied per-subgroup is a valid baseline but lacks cross-subgroup shrinkage, operates at estimand level rather than measurement model level, and has strictly higher variance under partial pooling. Do NOT say \"DSL cannot do subgroup correction\" — say it lacks the principled shrinkage mechanism.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — exp-006 provides precise RMSE crossover points: K=2/extreme n_expert=250, K=4/extreme n=1000, K=4/moderate n=2000, K=2/moderate never crosses (global always better on RMSE). Paper needs \"Expert Budget Recommendation\" subsection with per-K guidelines. Key message: when diagnostic criterion flags high heterogeneity (extreme regime), EC-HTE is worth the investment at moderate budgets; when heterogeneity is low, global correction is the safer choice. This honest framing connects Claim 2 (EC-HTE method) to Claim 3 (diagnostic criterion) — the diagnostic decides the correction strategy.\n\n6. **\"How does this differ from Carroll et al. (2006) / classical measurement error?\"** — The qualitative insight that misspecified corrections can amplify MSE is classical (Fuller 1987, Sec. 2.3). Our specific contributions beyond this are: (a) the quantitative Δπ×Δτ product form for CATE estimation with effect-modifier misclassification, (b) demonstrating this failure mode occurs *by default* in standard LLM annotation workflows, and (c) providing a computable diagnostic and correction framework. Must explicitly cite and contextualize: Fuller (1987), Carroll et al. (2006 Ch. 4), Gustafson (2003), Hu & Schennach (2008), Imai & Yamamoto (2010). Also cite Bayesian annotation models: Dawid & Skene, Passonneau & Carpenter (2014), Hovy et al. (2013). **Bibliography target: 30-35 references** spanning measurement error, Bayesian estimation, causal inference, LLM-as-annotator (Tornberg 2024, Gilardi et al. 2023, Ziems et al. 2024), HTE methods (Wager & Athey 2018, Kennedy 2023, Chernozhukov et al. 2018).\n\n7. **\"Methodological novelty is modest\"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. HB partial pooling provides meaningful RMSE reduction for moderate subgroups but is NOT \"never worse than global\" — it is a James-Stein shrinkage estimator with known boundary conditions. **Recommended condition**: n_expert per subgroup ≥ ~25 (e.g., n_expert ≥ 100 for K=4 with 12% minority). Below this, stratified MLE is preferred. This honest limitation strengthens credibility. State conditions explicitly using per-subgroup formulation, not just total n_expert.\n\n8. **\"Why no figures?\"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use cases (sentiment analysis, hate speech detection, refugee interview coding), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track. **NOTE**: Framing broadened from \"political-science\" to \"CSS\" (D004b) — TweetEval stance tasks too small (N<1000), sentiment (N=45K) usable but not political science. CSS is more accurate and equally strong for EMNLP.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n## Writing Requirements (Dream Round 2 consensus)\n\n1. **\"Bias decomposition\" NOT \"bias bound\"** — Theorem 1 is an exact identity at population level. R² < 1.0 in verification reflects finite-sample MC noise, not bound looseness.\n2. **Bibliography: 30-35 references minimum** — Must span 5 literatures: classical measurement error, Bayesian estimation, causal inference, LLM-as-annotator, CSS. Critical citations: Fuller 1987, Wager & Athey 2018, Imai & Yamamoto 2010.\n3. **3+ figures in main text** — (a) bias mechanism schematic, (b) Δπ×Δτ amplification heatmap, (c) diagnostic ROC curve, (d) budget crossover curves. Move exp-008/exp-009 tables to appendix.\n4. **Semi-synthetic DGP fully specified** — outcome generation, treatment assignment, CATE injection mechanism.\n5. **Real-data framed as pattern consistency** — NOT ground-truth benchmark. No bias/RMSE against unknown true CATEs.\n6. **EC-HTE advantage is conditional, not universal** — ec_hte dominates when misclassification heterogeneity is high (extreme regime) OR n_expert is large (≥500). In moderate regime with small n_expert (~100), global correction can outperform ec_hte because per-subgroup CM estimation noise exceeds the benefit of stratification. This connects to Claim 3: the diagnostic criterion (Δπ×Δτ) predicts when EC-HTE is needed. Unified condition: n_expert/K ≥ ~25-50 experts per subgroup.\n11. **RMSE tradeoff must be disclosed** — ec_hte has higher RMSE than global/naive in K=4/n≤100 configs (up to 3.5x in extreme cases) due to noisy per-subgroup CM estimation. Bias is lower but variance is higher. Must report both bias AND RMSE; include bias-RMSE tradeoff analysis. At n_expert≥500, ec_hte RMSE becomes competitive.\n12. **K-dependence of debiasing-hurts** — K=2 extreme magnification ~2.7x; K=4 extreme ~5.9x. More subgroups → larger π heterogeneity → more severe global correction damage. Report this scaling.\n7. **Confusion matrix invertibility** — State det(Ĉ_k) ≠ 0 assumption explicitly.\n8. **Diagnostic AUC cross-validated** — Leave-one-setting-out or held-out evaluation, not in-sample.\n9. **Hyperprior values stated + sensitivity analysis** — Gamma(α, β) for Dirichlet concentration; report sensitivity to 2× changes.\n10. **PPCI complementarity elevated** — Highlight in abstract and contributions. Frame as \"complementary\" not \"orthogonal\": EC-HTE is structured covariate-error correction; PPCI rectifier is general residual correction. Composition = EC-HTE handles structured part + rectifier handles remainder (primarily outcome error).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2. MUST report full MCMC diagnostics: sampler (PyMC\n    NUTS), chains (≥4), warmup (≥1000), R̂ (<1.01), ESS (>200), runtime vs MLE. Report\n    SEs/CIs for all metrics from MC runs. Monitor coverage calibration — if systematic\n    undercoverage, diagnose cause.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example. MUST include K>2 extension: verify bias formula empirically for K=4 subgroups;\n    add Remark after Proposition 1 discussing general-K case (sum-of-products form).\n    Report R² of analytic prediction vs MC, bound tightness ratio, and CIs on all\n    bias estimates.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim: 1,2,3\n  description: 'Semi-synthetic benchmark: use real CSS tweet corpus — TweetEval sentiment\n    (N=45K, primary) for exp-003. Framing broadened from ''political-science'' to\n    ''CSS'' per D004b (stance tasks N<1000 unusable). Inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 (API) and optionally Qwen3-235B-A22B (GPU), measure\n    subgroup-specific misclassification rates, apply EC-HTE vs baselines. Subgroup\n    variables: text features (has_hashtag, text_length) for semi-synthetic; demographic\n    subgroups reserved for exp-004. MUST fully specify DGP in paper: (a) outcome generation\n    model, (b) treatment assignment mechanism, (c) how true CATEs are injected. MUST\n    run LLM annotation pilot (~1000 samples) before committing to verify per-subgroup\n    misclassification heterogeneity exists.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim: 1,2\n  description: 'Real-data case study (pattern consistency, NOT ground-truth validation):\n    apply EC-HTE to real CSS dataset with subgroup-varying LLM misclassification.\n    Show: (a) global vs EC-HTE produce qualitatively different CATE distributions,\n    (b) EC-HTE results consistent with domain knowledge (demographic effect direction),\n    (c) bootstrap CIs on point estimate differences. Frame as ''illustrative application''\n    not ''ground-truth benchmark''. Reviewer confirmed: real data has no ground truth\n    CATE, CV-based ground truth is circular. PRIMARY: UC Berkeley Measuring Hate Speech\n    corpus (public, rich demographic subgroups). NICE-TO-HAVE: Ashwin et al. (2025)\n    if obtainable (requires author email + IRB, not feasible within 5-day DDL).'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference) or API\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: UC Berkeley dataset causal framework (T,Y,Z,S) mapping needs design\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold. MUST use\n    cross-validation or held-out evaluation (NOT in-sample AUC on own experiments).\n    Dream Round 2 flagged in-sample AUC as methodological weakness across best and\n    median tiers.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1,2\n  description: 'PPCI + DSL baseline comparison: (a) PPCI kernel-based conditional\n    correction vs EC-HTE on covariate-side vs outcome-side error; (b) per-subgroup\n    DSL as additional baseline (DSL applied independently per subgroup, no cross-subgroup\n    shrinkage — shows EC-HTE''s partial pooling advantage); (c) EC-HTE+PPCI composition\n    for simultaneous covariate+outcome error; (d) CRITICAL: include ''pure covariate-error,\n    zero outcome-error'' control condition to demonstrate EC-HTE advantage when covariate-side\n    error dominates (PPCI should be ineffective here). Paper framing: DSL per-subgroup\n    is a valid baseline but lacks cross-subgroup shrinkage and operates at estimand\n    level rather than measurement model level.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest integration: apply EC-HTE post-hoc correction to CausalForestDML\n    subgroup CATE estimates + leaf-level corrected pseudo-outcomes with variance-adjusted\n    CIs. Compare against naive forest and globally-corrected forest. ELEVATED TO P0:\n    Claim 2 explicitly states CausalForestDML but no experiment validates this — claim-evidence\n    gap is reviewer killshot.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mcmc_rhat_max: 1.024\n    mcmc_ess_min: 129\n    mcmc_divergent: 0\n    runtime_min: 69\n    total_mc_runs: 3600\n    hb_vs_mle_rmse_improvement_k2_n50: 4-9%\n    hb_vs_mle_rmse_improvement_k2_n100: 1-2%\n    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%\n    hb_coverage_min: 0.87\n    hb_coverage_median: 0.93\n    k4_extreme_n50_blowup: false\n    k4_extreme_n50_blowup_note: Fixed by singularity guard + 4-chain MCMC\n    mcmc_fix_4chain:\n      rhat_max_all_configs: 1.0034\n      ess_min_all_configs: 1618\n      ess_improvement: ~4x vs 2-chain\n      k4_extreme_n50_A_rmse_z0: 3.14 → 0.99\n      k4_extreme_n50_B_rmse_z0: 509.93 → 0.27\n      k4_extreme_n100_A_rmse_z0: 11.57 → 0.29\n      singularity_guard_triggers: extreme/n=50 only (2 HB, 3 MLE / 100 runs)\n      results_file: results/exp001_hb_results_v2.csv\n    hyperprior_sensitivity:\n      scale_range: 0.5-2.0\n      k2_rmse_variation: <1%\n      k4_rmse_variation: ~4-5%\n      coverage_invariant: true\n      conclusion: robust\n      results_file: results/exp001_hyperprior_sensitivity.csv\n- exp_id: exp-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r2_k2: 0.9939\n    r2_k4: 0.9738\n    tightness_ratio_k2_median: 1.0027\n    tightness_ratio_k4_median: 1.0234\n    debiasing_hurts_pct: 50\n    debiasing_hurts_pct_note: 260/520 (excluding dc=0 rows where bias=0)\n    debiasing_hurts_threshold_delta_misclass: 0.1235\n    max_bias_ratio_k2: 2.86\n    max_bias_ratio_k4: 2.41\n    coverage_2se_k2: 0.951\n    coverage_2se_k4: 0.94\n- exp_id: exp-007\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_rows: 6912\n    dgps:\n    - A_covariate_only\n    - B_outcome_only\n    - C_both_errors\n    - D_no_error\n    methods: 8\n    mc_runs: 100\n    double_correction_fix_verified: true\n    dgp_a_ec_hte_ppci_equals_ec_hte: true\n    dgp_c_extreme_n250_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.225\n      ec_hte_bias_z0: 0.178\n      ec_hte_rmse_z0: 0.226\n      ppci_bias_z0: 0.004\n      ppci_rmse_z0: 0.261\n      naive_bias_z0: 0.251\n      naive_rmse_z0: 0.269\n    dgp_c_n500_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.142\n      ec_hte_bias_z0: 0.088\n      ec_hte_rmse_z0: 0.134\n    key_finding: ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better\n      than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.\n- exp_id: exp-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase: A_semi_synthetic\n    n_subgroups: 4\n    misclass_rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25\n    subgroup_sizes: S0~38%, S1~38%, S2~12%, S3~12%\n    p_z1_actual: 0.39\n    debiasing_hurts_confirmed: true\n    mc_runs: 100\n    v3_hb_integration:\n      methods:\n      - oracle\n      - naive\n      - global_corrected\n      - stratified_mle\n      - hb_ec_hte\n      hb_vs_mle_summary:\n        S2_n50_rmse_z0_improvement: +21.4%\n        S2_n100_rmse_z0_improvement: +39.5%\n        S3_n50_blowup: RMSE 345-804% worse\n        convergence_at_n250: < 5% difference\n        S0_n50_extreme_rmse_z0_improvement: +88%\n      key_finding: HB partial pooling helps mid-misclass subgroups (S2) at small n_expert\n        but blows up in extreme-misclass tiny subgroups (S3 at n=50). Converges to\n        MLE at n>=250.\n      hypothesis_verdict: partially_validated\n    results_file_v3: results/exp003_phase_a_v3.csv\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subgroup_level_auc: 0.833\n    subgroup_correlation: 0.86\n    setting_level_auc: 0.49\n    low_pi_hurt_pct: 84.6\n    high_pi_hurt_pct: 15.4\n    theory_alignment: consistent with exp-002 formula\n- exp_id: exp-011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    n_configs: 8\n    total_rows: 144\n    runtime_min: 35\n    methods:\n    - naive_forest\n    - global_forest\n    - ec_hte_forest\n    mean_abs_bias:\n      naive_forest: 0.1558\n      global_forest: 0.1073\n      ec_hte_forest: 0.0608\n    mean_rmse:\n      naive_forest: 0.1782\n      global_forest: 0.1659\n      ec_hte_forest: 0.2289\n    debiasing_hurts_cases: 9\n    debiasing_hurts_max_ratio: 5.9\n    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'\n    k2_n500_ec_hte_bias_range: 0.004-0.013 (near zero)\n    k2_n500_global_bias_range: 0.033-0.109 (still biased)\n    pattern_consistent_with_diff_in_means: true\n    claim2_validated: true\n- exp_id: exp-006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    total_rows: 288\n    runtime_min: 110\n    grid: n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]\n    crossover_hb_beats_global:\n      K2_extreme: 250\n      K2_moderate: never\n      K4_extreme: 1000\n      K4_moderate: 2000\n    hb_vs_mle: HB ≥ MLE in 22/24 configs (partial pooling never significantly hurts\n      in symmetric DGP)\n    hb_best_improvement_over_mle:\n      K4_moderate_n50_sgC: +42.4% RMSE\n      K4_extreme_n50_sgC: +23.4% RMSE\n      K4_moderate_n50_sgB: +24.0% RMSE\n    convergence: HB ≈ MLE at n≥1000 (<0.5% difference)\n    key_finding: 'Crossover depends strongly on K and regime. K=2: crossover at n=250\n      (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest\n      improvement over MLE via partial pooling.'\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:37:22.929Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:37:22.929Z",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-21T03:37:22.970Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Real LLM heterogeneity exists but moderate; bias mechanism confirmed at smaller magnitudes than synthetic; EC-HTE works but requires larger expert budgets than hoped; diagnostic reframed from setting-level threshold to subgroup-level screening tool
核心假设：['GPT-4.1 Δπ across subgroups ~ 0.05-0.12 — measurable but not extreme-regime levels', 'Bias amplification 1.3-2x with real LLM labels — visible but below synthetic headline numbers', 'EC-HTE RMSE competitive only at n_expert ≥ 1000 for K=4; bias advantage clear but variance penalty dominates at smaller budgets', 'Diagnostic setting-level AUC stays 0.50-0.65 even after refinement — not a reliable decision rule; subgroup-level AUC robust at ~0.80', 'UC Berkeley real data shows directional CATE differences but most subgroups within overlapping CIs', 'ec_hte_ppci composition works but advantage over ec_hte alone modest due to lower outcome-error in real data']
关键指标范围：{'semi_synth_llm_delta_pi': [0.05, 0.12], 'semi_synth_llm_bias_amplification_median': [1.3, 2.0], 'ec_hte_bias_reduction_pct_n500': [30, 55], 'ec_hte_rmse_ratio_n500_k4': [1.2, 1.6], 'diagnostic_cv_auc_setting': [0.5, 0.65], 'diagnostic_cv_auc_subgroup': [0.75, 0.85], 'real_data_max_cate_shift_se': [1.0, 2.0], 'coverage_ec_hte_95': [0.85, 0.93], 'ec_hte_ppci_bias_reduction_vs_ec_hte_dgpC': [40, 80]}
叙事方向：Bias identity (Claim 1) holds exactly — this is mathematical, not empirical. Empirical headline softened: 'up to 2-3x in controlled synthetic; 1.3-2x with current SOTA LLMs on standard CSS tasks, expected to increase on harder annotation tasks.' Claim 2 reframed: EC-HTE provides principled bias reduction but requires honest bias-RMSE tradeoff disclosure — add 'When to Use EC-HTE' subsection with per-K budget recommendations replacing the '250 labels' headline. Claim 3 substantially weakened: drop 'computable diagnostic threshold' from contributions; reframe as 'subgroup-level misclassification audit protocol' — subgroup AUC ~0.80 supports identifying which subgroups are at risk, not whether the overall setting needs correction. Strengthen theoretical framing: lead with the identity and CausalForest amplification (5.9x, already validated) to argue the problem scales with estimator complexity. Add forward-looking argument: as LLMs are applied to harder CSS tasks (cross-lingual, implicit sentiment, complex framing), heterogeneity will increase. Paper needs ~0.5 page more for limitations; move exp-008/009 plus one main-text table to appendix to accommodate.

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
tier: median
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
  "promptId": "4d95ea83-042a-4fb4-972a-b462ee50aa02",
  "type": "user",
  "uuid": "44d1b245-ce32-4487-999b-46d58f016a28",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:37:22.968Z_

```json
{
  "parentUuid": "44d1b245-ce32-4487-999b-46d58f016a28",
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
  "uuid": "755ae70e-a766-4423-9a9e-8d0c1ff83287",
  "timestamp": "2026-05-21T03:37:22.968Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:37:22.968Z_

```json
{
  "parentUuid": "755ae70e-a766-4423-9a9e-8d0c1ff83287",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "546557bb-fb9a-4b01-8967-85cfdf21f928",
  "timestamp": "2026-05-21T03:37:22.968Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Real LLM heterogeneity exists but moderate; bias mechanism confirmed at smaller magnitudes than synthetic; EC-HTE works but requires larger expert budget…",
  "leafUuid": "546557bb-fb9a-4b01-8967-85cfdf21f928",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE bias mechanism validation across CSS tasks",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224"
}
```

---

### Assistant

_source line 8 · 2026-05-21T03:37:51.577Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, based on the "median" tier definition they've provided. I need to look at which experiments are still "planned" vs "DONE".

From the experiment_plan and registry:
- exp-001: DONE
- exp-002: DONE
- exp-003: DONE


- exp-004: planned
- exp-005: DONE
- exp-006: DONE
- exp-007: DONE
- exp-008: planned
- exp-009: planned
- exp-010: planned
- exp-011: DONE

So the planned experiments are: exp-004, exp-008, exp-009, exp-010. Now I'm working through predictions for each of these under the median tier, using the median tier definition and the completed experiment results as reference points. Starting with exp-004, the UC Berkeley real-data case study on measuring hate speech, where the median tier predicts directional CATE effects.

For exp-008, I'm comparing multiple LLM annotators—GPT-4.1, Qwen3-235B-A22B, and Claude Sonnet 4.6—where I expect GPT-4.1 to show treatment effect variation around 0.05-0.12 across subgroups, with semi-synthetic bias amplification in the 1.3-2x range, and each model exhibiting distinct heterogeneity patterns. For exp-009, I'm looking at adaptive expert annotation allocation weighted by CATE, where the median tier suggests EC-HTE should work but demands a larger expert budget than baseline approaches.

For exp-010, I'm testing EC-HTE's robustness when subgroup structure is misspecified or noisy—the method still performs but requires increased budgets, and partial pooling helps stabilize estimates. Now for exp-004 using the UC Berkeley Measuring Hate Speech corpus, I need to map the observational data onto a causal framework: LLM annotations of hate speech severity and type serve as effect modifiers, demographic attributes define subgroups, and I'm looking for directional CATE differences across these groups, though most confidence intervals will overlap with some variation in standard error units.

For exp-008, I'm comparing three LLMs with different quality profiles—GPT-4.1 has the lowest misclassification and modest bias amplification around 1.3-2x, while Qwen3 likely shows higher error rates and potentially stronger amplification, and Claude Sonnet sits competitively with GPT-4.1. The benefit of EC-HTE scales with how much heterogeneity each model introduces. For exp-009 on adaptive allocation, I'm examining how the EC-HTE approach with partial credible intervals affects the composition of allocated samples.

Adaptive allocation shows promise but the gains are moderate—probably around 10-20% RMSE improvement over uniform allocation given that real data tends to have lower outcome error. For exp-010 with misspecified subgroups, hierarchical Bayes shrinkage provides a buffer against model misspecification, though the degradation is still noticeable at roughly 15-30% RMSE increase compared to correctly specified groups. Now I'm preparing the full YAML output with detailed metrics and supporting rationales.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "546557bb-fb9a-4b01-8967-85cfdf21f928",
  "isSidechain": false,
  "requestId": "req_011CbF1sp2R5WmkAu9mmQMXj",
  "type": "assistant",
  "uuid": "3d54d894-d32e-453c-a8a3-c9d239e21e3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEeFJqzxiSysZbzYCmX4LN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14699,
      "cache_read_input_tokens": 11841,
      "output_tokens": 7291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7291,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14699
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

_source line 9 · 2026-05-21T03:39:55.009Z_

```yaml
tier: median
narrative_guidance: >
  Real LLM heterogeneity exists but moderate; bias mechanism confirmed at smaller magnitudes
  than synthetic; EC-HTE works but requires larger expert budgets than hoped; diagnostic
  reframed from setting-level threshold to subgroup-level screening tool. Paper framing:
  lead with exact identity (mathematical, not empirical), soften empirical headline to
  '1.3-2x with current SOTA LLMs', add 'When to Use EC-HTE' subsection with per-K budget
  recommendations, drop 'computable diagnostic threshold' from contributions and reframe
  as 'subgroup-level misclassification audit protocol'. Strengthen forward-looking argument:
  heterogeneity will increase on harder CSS tasks.

imagined_experiments:
  - name: "Real-data case study — UC Berkeley Measuring Hate Speech"
    plan_id: "exp-004"
    description: >
      Apply EC-HTE to UC Berkeley Measuring Hate Speech corpus. Map corpus structure to
      causal framework: T = comment contains identity-directed language (binary), Y = annotator
      severity rating (binarized at median), Z = LLM-classified hate speech type (e.g.,
      dehumanization vs incivility — effect modifier), S = target demographic subgroups
      (race, gender, sexuality from corpus metadata). Annotate Z with GPT-4.1 API. Compare
      global-corrected vs EC-HTE CATE estimates across demographic subgroups. Report bootstrap
      CIs on CATE shift (global − EC-HTE) in SE units. Frame as pattern consistency, NOT
      ground-truth benchmark.
    expected_results:
      n_samples: ~39000
      n_subgroups_demographic: 4-6
      n_subgroups_hate_type_z: 3-4
      gpt41_overall_accuracy_vs_expert: 0.72-0.78
      gpt41_delta_pi_across_subgroups: 0.06-0.11
      gpt41_misclass_rate_range: [0.15, 0.32]
      gpt41_worst_subgroup_error: 0.28-0.32
      gpt41_best_subgroup_error: 0.15-0.19
      global_vs_ec_hte_cate_shift_max_se: 1.4
      global_vs_ec_hte_cate_shift_median_se: 0.8
      subgroups_with_nonoverlapping_95ci: 1-2 of 4-6
      subgroups_with_overlapping_95ci: 3-4 of 4-6
      ec_hte_cate_direction_consistent_with_domain: true
      bootstrap_iterations: 1000
      qualitative_difference_detected: true
      quantitative_significance: partial
    result_rationale: >
      Under median tier, real LLM heterogeneity is moderate (Δπ ~ 0.06-0.11). The UC Berkeley
      corpus has genuine demographic variation in hate speech perception, but GPT-4.1 is a
      strong annotator — its error heterogeneity across subgroups is measurable but not extreme.
      Most subgroups show directional CATE differences between global and EC-HTE corrections,
      but bootstrap CIs overlap for the majority because (a) the Δπ is moderate so the
      correction difference is small, and (b) per-subgroup sample sizes for smaller demographic
      groups (e.g., LGBTQ+ targets) yield wide CIs. 1-2 subgroups with the largest Δπ × Δτ
      product (likely race-related targets where both misclassification and effect heterogeneity
      concentrate) show non-overlapping CIs at 95% level. This supports the paper's pattern-
      consistency narrative: EC-HTE produces qualitatively different and domain-consistent
      CATE distributions, but the real-data case study alone does not constitute strong
      quantitative evidence — it illustrates the method's applicability and directional
      correctness. The 0.28-0.32 worst-subgroup error rate reflects GPT-4.1's known weakness
      on implicit/coded hate speech targeting specific demographics, while explicit hate speech
      (best subgroup) is classified more reliably at 0.15-0.19 error.
    tables:
      - name: "Table: UC Berkeley Real-Data CATE Estimates by Demographic Subgroup"
        columns: [subgroup, n, misclass_rate_llm, cate_naive, cate_global, cate_ec_hte, shift_se, ci_95_overlap]
        representative_rows:
          - [race_target, 8200, 0.28, 0.142, 0.098, 0.131, 1.6, "no"]
          - [gender_target, 11500, 0.21, 0.105, 0.083, 0.097, 1.1, "yes"]
          - [sexuality_target, 4800, 0.25, 0.118, 0.089, 0.112, 1.3, "marginal"]
          - [religion_target, 3200, 0.19, 0.091, 0.078, 0.086, 0.7, "yes"]
    figures_description:
      - "Forest plot: CATE point estimates with 95% bootstrap CIs for each demographic subgroup under naive, global-corrected, and EC-HTE. Visual emphasis on subgroups where global and EC-HTE diverge beyond CI overlap."
      - "Bar chart: Per-subgroup LLM misclassification rates showing heterogeneity pattern. Annotate with Δπ values."
    analysis: >
      Results support pattern consistency: EC-HTE shifts CATEs toward domain-expected
      directions (hate speech targeting racial minorities shows larger treatment effects
      than global correction suggests, consistent with known annotation difficulty gradient).
      The limited number of non-overlapping CIs (1-2 of 4-6) is expected under median tier —
      real LLM heterogeneity is moderate, not extreme. This motivates the forward-looking
      argument: on harder annotation tasks (cross-lingual hate speech, implicit framing),
      heterogeneity will increase and EC-HTE's advantage will grow. Frame in paper as
      'illustrative application demonstrating practical relevance' with explicit caveat
      that no ground-truth CATEs exist for real data. Move to ~1 page in main text with
      full table in appendix.

  - name: "Multiple LLM annotator comparison"
    plan_id: "exp-008"
    description: >
      Annotate TweetEval sentiment corpus (same as exp-003) with three LLMs: GPT-4.1 (API),
      Qwen3-235B-A22B (GPU), Claude Sonnet 4.6 (API). Measure per-subgroup misclassification
      rates for each LLM. Apply EC-HTE with each LLM's annotations. Compare bias amplification
      patterns and EC-HTE benefit across LLMs. Show that EC-HTE benefit scales with LLM
      misclassification heterogeneity.
    expected_results:
      gpt41_overall_accuracy: 0.82-0.86
      gpt41_delta_pi: 0.07-0.10
      gpt41_bias_amplification_median: 1.4-1.7
      qwen3_overall_accuracy: 0.74-0.80
      qwen3_delta_pi: 0.10-0.18
      qwen3_bias_amplification_median: 1.6-2.2
      claude_sonnet_overall_accuracy: 0.83-0.87
      claude_sonnet_delta_pi: 0.05-0.09
      claude_sonnet_bias_amplification_median: 1.3-1.5
      ec_hte_bias_reduction_pct_gpt41_n500: 35-50
      ec_hte_bias_reduction_pct_qwen3_n500: 45-60
      ec_hte_bias_reduction_pct_claude_n500: 30-45
      rank_order_heterogeneity: "Qwen3 > GPT-4.1 ≥ Claude Sonnet"
      ec_hte_benefit_correlates_with_delta_pi: true
      correlation_delta_pi_vs_bias_reduction: 0.85-0.95
    result_rationale: >
      Under median tier, real LLM heterogeneity is moderate across all models. Qwen3 as an
      open-source model has the highest overall error and the most heterogeneous error pattern
      — it struggles disproportionately on minority subgroups (short texts, hashtag-heavy
      content) compared to majority subgroups, yielding Δπ ~ 0.10-0.18. GPT-4.1 and Claude
      Sonnet are both frontier API models with similar overall accuracy (0.82-0.87), but
      GPT-4.1 shows slightly more heterogeneity (Δπ ~ 0.07-0.10 vs 0.05-0.09) due to
      different calibration patterns across text styles. The key finding is that EC-HTE
      benefit scales monotonically with Δπ: Qwen3 benefits most (45-60% bias reduction),
      GPT-4.1 moderately (35-50%), Claude Sonnet least (30-45%). All bias amplification
      factors are in the 1.3-2.2x range — measurable but below the 2-3x synthetic headline.
      This confirms the median tier narrative: the bias mechanism is real and present in
      current SOTA LLMs, but at moderate magnitudes. The forward-looking argument gains
      support: Qwen3's higher heterogeneity on this relatively easy task (sentiment) suggests
      that harder tasks will push all LLMs toward the higher end of the heterogeneity
      spectrum.
    tables:
      - name: "Table: LLM Annotation Quality and EC-HTE Benefit Comparison"
        columns: [llm, overall_acc, delta_pi, bias_amp_median, ec_hte_bias_red_pct_n500, ec_hte_rmse_ratio_n500]
        representative_rows:
          - [GPT-4.1, 0.84, 0.08, 1.55, 42, 1.35]
          - [Qwen3-235B-A22B, 0.77, 0.14, 1.9, 53, 1.22]
          - [Claude_Sonnet_4.6, 0.85, 0.07, 1.4, 37, 1.42]
      - name: "Table: Per-Subgroup Misclassification Rates by LLM"
        columns: [subgroup, n_pct, gpt41_misclass, qwen3_misclass, claude_misclass]
        representative_rows:
          - [S0_long_no_hashtag, 38%, 0.11, 0.16, 0.10]
          - [S1_long_hashtag, 38%, 0.14, 0.20, 0.13]
          - [S2_short_no_hashtag, 12%, 0.19, 0.28, 0.17]
          - [S3_short_hashtag, 12%, 0.22, 0.34, 0.20]
    figures_description:
      - "Scatter plot: Δπ (x-axis) vs EC-HTE bias reduction % (y-axis) with one point per LLM. Shows monotonic relationship. Annotate with LLM names. Include regression line with R²."
      - "Grouped bar chart: Per-subgroup misclassification rates for each LLM. Shows heterogeneity pattern is qualitatively similar across LLMs but magnitude differs."
    analysis: >
      This experiment is P1 — likely moves to appendix under median tier to free main-text
      space. Key takeaway for main text (1-2 sentences): 'EC-HTE benefit scales with LLM
      misclassification heterogeneity; across three SOTA LLMs, bias amplification ranges
      from 1.3-2.2x, with open-source models showing higher heterogeneity and correspondingly
      greater EC-HTE benefit.' The Qwen3 results provide the forward-looking argument
      anchor: even at moderate overall accuracy, subgroup-level heterogeneity creates
      meaningful bias. Full table in appendix. RMSE ratio > 1.0 for all LLMs at n=500
      confirms the median-tier finding that EC-HTE requires larger expert budgets than
      hoped — bias is reduced but RMSE tradeoff is real.

  - name: "Adaptive expert annotation allocation"
    plan_id: "exp-009"
    description: >
      Implement three allocation strategies for expert annotation budget: (a) uniform
      allocation (baseline), (b) uncertainty-weighted (allocate proportional to posterior
      variance of CM estimates), (c) CATE-weighted (allocate proportional to estimated
      |CATE| × misclassification uncertainty — targeting subgroups where correction matters
      most). Compare on synthetic DGP from exp-001 at n_expert ∈ {250, 500, 1000} × K=4
      (where budget pressure is highest). Primary metric: RMSE of subgroup CATEs.
    expected_results:
      cate_weighted_vs_uniform_rmse_reduction_n250: 8-15%
      cate_weighted_vs_uniform_rmse_reduction_n500: 5-10%
      cate_weighted_vs_uniform_rmse_reduction_n1000: 2-5%
      uncertainty_vs_uniform_rmse_reduction_n250: 5-10%
      uncertainty_vs_uniform_rmse_reduction_n500: 3-7%
      cate_weighted_vs_uncertainty_advantage: "modest, 3-6% at n250"
      worst_subgroup_rmse_improvement_n250: 15-25%
      allocation_shift_from_uniform: "~40-60% of budget to 2 highest-error subgroups (S2,S3) vs 25% each under uniform"
      crossover_improvement: "K4 extreme crossover moves from n=1000 to n=750-800 with CATE-weighted allocation"
      adaptive_overhead_runtime: "<5% additional compute"
    result_rationale: >
      Under median tier, the advantage of adaptive allocation over uniform is modest because
      (a) with moderate LLM heterogeneity (Δπ ~ 0.05-0.12), the per-subgroup CM estimation
      noise differences are not dramatic enough for targeted allocation to yield large gains,
      and (b) at K=4, even with optimal allocation, the smallest subgroups (12%) still have
      limited sample sizes that dominate the variance. The CATE-weighted strategy helps most
      at n=250 (8-15% RMSE reduction) where budget pressure is highest — it effectively
      moves the K=4 crossover point from n=1000 to ~n=750-800, but does not achieve the
      hoped-for halving of required budget. The worst-subgroup improvement (15-25%) is more
      meaningful than the average because allocation concentrates labels on S3 (highest error,
      smallest subgroup) where marginal expert labels have the highest impact on CM estimation
      quality. At n=1000+, all strategies converge because per-subgroup CMs are already
      well-estimated under any allocation. The modest overall gain reflects the median-tier
      reality that the problem is fundamentally about total budget, not allocation efficiency.
    tables:
      - name: "Table: Allocation Strategy Comparison — K=4 Extreme Regime"
        columns: [n_expert, strategy, rmse_mean, rmse_worst_sg, bias_mean, allocation_S0_S1_S2_S3]
        representative_rows:
          - [250, uniform, 0.385, 0.62, 0.08, "25/25/25/25%"]
          - [250, uncertainty, 0.358, 0.54, 0.07, "18/22/28/32%"]
          - [250, cate_weighted, 0.340, 0.48, 0.06, "15/20/27/38%"]
          - [500, uniform, 0.245, 0.38, 0.05, "25/25/25/25%"]
          - [500, cate_weighted, 0.225, 0.31, 0.04, "16/21/26/37%"]
          - [1000, uniform, 0.165, 0.22, 0.03, "25/25/25/25%"]
          - [1000, cate_weighted, 0.158, 0.20, 0.03, "18/22/27/33%"]
    figures_description:
      - "Line plot: RMSE vs n_expert for three allocation strategies at K=4 extreme. Show convergence at large n and divergence at small n. Mark crossover points where EC-HTE beats global."
    analysis: >
      P2 experiment — moves to appendix. The modest gains (8-15% at best) under median tier
      mean this is a 'nice to have' refinement rather than a core contribution. Main text
      should mention adaptive allocation as a practical extension in 1-2 sentences. The
      crossover improvement (n=1000 → n=750-800 for K=4) is useful but does not change the
      headline message that K=4 requires substantial expert budgets. Worth including in
      appendix to show the method is extensible and to provide practical guidance for
      practitioners who want to minimize labeling cost.

  - name: "Robustness to misspecified subgroup structure"
    plan_id: "exp-010"
    description: >
      Test EC-HTE under three misspecification scenarios: (a) noisy subgroup assignment —
      add 10-30% label noise to true subgroup indicators Z, (b) coarsened subgroups —
      collapse K=4 true subgroups into K=2 observed subgroups (merging heterogeneous pairs),
      (c) irrelevant subgroup variable — condition on a variable uncorrelated with
      misclassification heterogeneity. Compare EC-HTE vs global correction under each
      scenario. DGP from exp-001 (K=4 extreme regime, n_expert=500).
    expected_results:
      # Scenario A: noisy subgroup assignment
      noisy_10pct_rmse_increase_vs_correct: 5-10%
      noisy_20pct_rmse_increase_vs_correct: 12-22%
      noisy_30pct_rmse_increase_vs_correct: 25-40%
      noisy_10pct_ec_hte_still_beats_global: true
      noisy_20pct_ec_hte_still_beats_global: true
      noisy_30pct_ec_hte_vs_global: "marginal or global wins on RMSE"
      noisy_crossover_noise_level: "~25-30% noise"
      # Scenario B: coarsened subgroups
      coarsened_k4_to_k2_bias_residual_pct: 30-50%
      coarsened_k4_to_k2_rmse_vs_correct_ec_hte: 1.3-1.6x
      coarsened_k4_to_k2_still_beats_naive: true
      coarsened_k4_to_k2_vs_global: "EC-HTE still better but margin halved"
      # Scenario C: irrelevant subgroup
      irrelevant_ec_hte_rmse_vs_global: 1.05-1.15x
      irrelevant_ec_hte_bias_vs_global: "approximately equal"
      irrelevant_hb_shrinkage_toward_global: ">90% shrinkage weight on global mean"
      irrelevant_harm_vs_global: "minimal — HB partial pooling collapses to near-global"
    result_rationale: >
      Under median tier, EC-HTE shows graceful degradation under misspecification due to HB
      partial pooling, but the degradation is noticeable, not negligible. (A) Noisy subgroup
      assignment: 10% noise is tolerable because HB smooths over small perturbations —
      per-subgroup CM estimates are slightly noisier but still capture the main heterogeneity
      pattern. At 20% noise, the subgroup-specific CMs are substantially contaminated,
      increasing RMSE by 12-22%. At 30%, subgroup structure is so noisy that per-subgroup CM
      estimation adds more noise than signal — EC-HTE becomes marginal vs global. The ~25-30%
      crossover is consistent with James-Stein theory: when the signal-to-noise ratio of
      subgroup differences drops below ~1, pooling dominates stratification. (B) Coarsened
      subgroups: merging K=4 into K=2 by pairing heterogeneous subgroups retains only partial
      heterogeneity structure. EC-HTE still beats naive (it captures between-pair
      heterogeneity) but misses within-pair heterogeneity, leaving 30-50% of the original
      bias uncorrected. The RMSE penalty (1.3-1.6x) reflects estimating a less informative
      but lower-variance correction. (C) Irrelevant subgroup: this is the key robustness
      test — if the subgroup variable has no relationship to misclassification heterogeneity,
      EC-HTE should not hurt. HB partial pooling correctly shrinks subgroup-specific estimates
      toward the global mean (>90% shrinkage weight), making EC-HTE approximately equivalent
      to global correction with only minimal overhead (5-15% RMSE increase from residual
      subgroup noise). This demonstrates that the HB framework is 'safe to apply' even when
      the practitioner is uncertain about subgroup relevance — a key practical selling point.
    tables:
      - name: "Table: Robustness Analysis — RMSE Relative to Correctly-Specified EC-HTE"
        columns: [scenario, parameter, ec_hte_rmse_ratio, ec_hte_bias_ratio, beats_global, beats_naive]
        representative_rows:
          - [noisy_10pct, "10% label noise", 1.08, 1.12, "yes", "yes"]
          - [noisy_20pct, "20% label noise", 1.18, 1.30, "yes (marginal)", "yes"]
          - [noisy_30pct, "30% label noise", 1.35, 1.55, "no", "yes"]
          - [coarsened_k4_to_k2, "K=4→K=2 merge", 1.45, 1.40, "yes", "yes"]
          - [irrelevant_subgroup, "uncorrelated Z", 1.10, 1.02, "no (≈equal)", "yes"]
      - name: "Table: HB Shrinkage Weights Under Misspecification"
        columns: [scenario, mean_shrinkage_toward_global, min_shrinkage, max_shrinkage]
        representative_rows:
          - [correct_specification, 0.35, 0.15, 0.55]
          - [noisy_20pct, 0.55, 0.35, 0.70]
          - [noisy_30pct, 0.68, 0.50, 0.82]
          - [irrelevant_subgroup, 0.92, 0.85, 0.97]
    figures_description:
      - "Line plot: RMSE vs noise level (0-30%) for EC-HTE, global, and naive. Show EC-HTE degradation curve and crossover with global at ~25-30% noise."
      - "Bar chart: Shrinkage weight toward global mean for each misspecification scenario. Shows HB automatic adaptation."
    analysis: >
      P2 experiment — appendix. The key message for main text is a single paragraph in the
      robustness section: 'EC-HTE degrades gracefully under subgroup misspecification due to
      hierarchical Bayesian partial pooling. When subgroup assignments are noisy (up to ~20%
      label error), EC-HTE retains its advantage over global correction. When the subgroup
      variable is irrelevant, HB shrinkage collapses to near-global correction, incurring
      minimal RMSE overhead (5-15%). Practitioners can safely apply EC-HTE without certainty
      that the chosen subgroup variable captures the full misclassification heterogeneity
      structure.' The coarsened-subgroups result also motivates the practical recommendation
      to use fine-grained subgroups when available, since coarsening sacrifices 30-50% of the
      bias reduction. Under median tier, the crossover at ~25-30% noise is a meaningful
      boundary condition — it says EC-HTE is robust to moderate misspecification but not to
      severe misspecification, which is an honest and credible claim.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d54d894-d32e-453c-a8a3-c9d239e21e3b",
  "isSidechain": false,
  "requestId": "req_011CbF1sp2R5WmkAu9mmQMXj",
  "type": "assistant",
  "uuid": "6c6b4862-2ee4-461d-9455-6d2e2a6fafda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEeFJqzxiSysZbzYCmX4LN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14699,
      "cache_read_input_tokens": 11841,
      "output_tokens": 7291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7291,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14699
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Real LLM heterogeneity exists but moderate; bias mechanism confirmed at smaller magnitudes than synthetic; EC-HTE works but requires larger expert budget…",
  "leafUuid": "6c6b4862-2ee4-461d-9455-6d2e2a6fafda",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE bias mechanism validation across CSS tasks",
  "sessionId": "23ff0975-bed3-4c9c-bd2c-5b8a0f153224"
}
```

---
