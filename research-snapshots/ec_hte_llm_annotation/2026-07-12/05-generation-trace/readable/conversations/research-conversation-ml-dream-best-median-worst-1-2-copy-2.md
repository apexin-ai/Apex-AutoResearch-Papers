# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/89e58173-a620-4c29-b3fe-1f83e9868dc7.jsonl`
- **Structured JSON:** [`8c975b2900f5560d3242.json`](../../sessions/8c/8c975b2900f5560d3242.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:25:01.750Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:25:01.750Z",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: ec_hte_llm_annotation\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 2-3x (median across configurations), with amplification up to 5.9x for K=4 subgroups; when naive bias is near zero, global correction creates bias where none existed. For the difference-in-means estimator, the amplification magnitude does NOT monotonically increase with K (K=2 extreme: up to 2.86× vs K=4 extreme: up to 2.41×); however, with nonlinear estimators such as CausalForest, more subgroups amplify the effect substantially (K=4/extreme: up to 5.9×) due to compounding estimation noise in tree-based CATE. Global correction increases subgroup-level bias in ~50% of the parameter space.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias when misclassification heterogeneity is sufficiently high, while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction by borrowing strength across groups (classic James-Stein shrinkage). We provide precise crossover thresholds: EC-HTE outperforms global correction in RMSE with as few as 250 expert labels (K=2, high heterogeneity), scaling to ~1000 for K=4. **Boundary condition**: when expert labels per subgroup < ~25, shrinkage can be harmful — stratified MLE is preferred. **EC-HTE is most valuable precisely when it is most needed — the diagnostic criterion (Claim 3) identifies these scenarios.** **CONFIRMED** by exp-003 full 100 MC (1200 runs, 0 errors). HB crossover at ~11 experts/subgroup; ≥25 recommended for robust performance. Demonstrated with both difference-in-means and CausalForestDML (exp-011: consistent bias reduction pattern, ec_hte_forest |bias|=0.06 vs naive 0.16). CausalForest amplifies the debiasing-hurts effect (up to 5.9x in K=4/extreme) due to nonlinear CATE estimation.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic that simultaneously predicts when global correction is harmful (Claim 1) and when the expert label investment for stratified correction is worthwhile (connecting to the budget guidelines from Claim 2). This criterion has standalone value independent of EC-HTE — even without adopting EC-HTE, knowing when global correction backfires is practically actionable.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis across computational social science (CSS) — e.g., sentiment framing moderates message effectiveness, hate speech type moderates intervention impact. LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education; documented across CSS tasks including sentiment, stance, toxicity). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as \"problem identification + principled solution\" not \"new estimation technique.\"\n\n- **Headline result template**: \"On semi-synthetic CSS benchmarks, global correction worsens subgroup CATE bias by 2-3x (median), with amplification up to 5.9x for K=4 subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels. Combined with PPCI, the composition achieves near-zero bias (0.005) even when both covariate and outcome errors are present.\"\n\n- **Oracle framing**: When reporting DGP C results where ec_hte_ppci outperforms oracle, always use \"covariate-oracle\" (true Z + observed Y), never unqualified \"oracle\". Frame as \"composite correction is necessary and sufficient when both error types coexist\" — NOT \"beats oracle\". The result is by construction (ec_hte_ppci corrects both error types; covariate-oracle only corrects one), not surprising.\n\n## Key Contributions (ordered for paper)\n\n1. **Bias decomposition identity**: Exact population-level identity: bias ∝ misclassification heterogeneity × CATE heterogeneity (Δπ×Δτ product form). NOT a bound — it is an exact identity under A1–A4; finite-sample R² measures MC noise, not bound looseness. Includes \"debiasing can hurt\" proposition with constructive example. Frame as \"bias decomposition\" or \"bias identity\" throughout — never \"bias bound.\" (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **EC-HTE + PPCI composition — empirically necessary and sufficient**: EC-HTE and PPCI are empirically necessary and sufficient in composition: neither alone adequately handles dual-error scenarios (DGP C), but their composition reduces bias to near-zero (0.005, a 35× improvement over EC-HTE alone). EC-HTE exploits mixing matrix structure for covariate-side error; PPCI rectifier captures outcome-side error. PPCI alone can partially correct covariate error but with higher variance (limited by gold subset size). In Methods, retain full discussion of partial overlap; in Abstract, lead with \"necessary and sufficient in composition.\" (Method + Empirical)\n5. **Comprehensive validation**: Synthetic + semi-synthetic + real-data case study (pattern consistency, not ground-truth benchmark) with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI / DSL?\"** — PPCI rectifier is a general-purpose correction that captures any systematic error (covariate + outcome); EC-HTE is a structured correction exploiting mixing matrix structure specifically for covariate-side error. They are complementary: EC-HTE alone is more efficient for covariate error (uses M⁻¹ structure), PPCI alone can partially correct covariate error but with higher variance (limited by gold subset). In composition, EC-HTE handles structured covariate error, residual rectifier handles outcome error. DSL applied per-subgroup is a valid baseline but lacks cross-subgroup shrinkage, operates at estimand level rather than measurement model level, and has strictly higher variance under partial pooling. Do NOT say \"DSL cannot do subgroup correction\" — say it lacks the principled shrinkage mechanism.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — exp-006 provides precise RMSE crossover points: K=2/extreme n_expert=250, K=4/extreme n=1000, K=4/moderate n=2000, K=2/moderate never crosses (global always better on RMSE). Paper needs \"Expert Budget Recommendation\" subsection with per-K guidelines. Key message: when diagnostic criterion flags high heterogeneity (extreme regime), EC-HTE is worth the investment at moderate budgets; when heterogeneity is low, global correction is the safer choice. This honest framing connects Claim 2 (EC-HTE method) to Claim 3 (diagnostic criterion) — the diagnostic decides the correction strategy.\n\n6. **\"How does this differ from Carroll et al. (2006) / classical measurement error?\"** — The qualitative insight that misspecified corrections can amplify MSE is classical (Fuller 1987, Sec. 2.3). Our specific contributions beyond this are: (a) the quantitative Δπ×Δτ product form for CATE estimation with effect-modifier misclassification, (b) demonstrating this failure mode occurs *by default* in standard LLM annotation workflows, and (c) providing a computable diagnostic and correction framework. Must explicitly cite and contextualize: Fuller (1987), Carroll et al. (2006 Ch. 4), Gustafson (2003), Hu & Schennach (2008), Imai & Yamamoto (2010). Also cite Bayesian annotation models: Dawid & Skene, Passonneau & Carpenter (2014), Hovy et al. (2013). **Bibliography target: 30-35 references** spanning measurement error, Bayesian estimation, causal inference, LLM-as-annotator (Tornberg 2024, Gilardi et al. 2023, Ziems et al. 2024), HTE methods (Wager & Athey 2018, Kennedy 2023, Chernozhukov et al. 2018).\n\n7. **\"Methodological novelty is modest\"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. HB partial pooling provides meaningful RMSE reduction for moderate subgroups but is NOT \"never worse than global\" — it is a James-Stein shrinkage estimator with known boundary conditions. **Recommended condition**: n_expert per subgroup ≥ ~25 (e.g., n_expert ≥ 100 for K=4 with 12% minority). Below this, stratified MLE is preferred. This honest limitation strengthens credibility. State conditions explicitly using per-subgroup formulation, not just total n_expert.\n\n8. **\"Why no figures?\"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use cases (sentiment analysis, hate speech detection, refugee interview coding), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track. **NOTE**: Framing broadened from \"political-science\" to \"CSS\" (D004b) — TweetEval stance tasks too small (N<1000), sentiment (N=45K) usable but not political science. CSS is more accurate and equally strong for EMNLP.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n## Writing Requirements (Dream Round 2 consensus)\n\n1. **\"Bias decomposition\" NOT \"bias bound\"** — Theorem 1 is an exact identity at population level. R² < 1.0 in verification reflects finite-sample MC noise, not bound looseness.\n2. **Bibliography: 30-35 references minimum** — Must span 5 literatures: classical measurement error, Bayesian estimation, causal inference, LLM-as-annotator, CSS. Critical citations: Fuller 1987, Wager & Athey 2018, Imai & Yamamoto 2010.\n3. **3+ figures in main text** — (a) bias mechanism schematic, (b) Δπ×Δτ amplification heatmap, (c) diagnostic ROC curve, (d) budget crossover curves. Move exp-008/exp-009 tables to appendix.\n4. **Semi-synthetic DGP fully specified** — outcome generation, treatment assignment, CATE injection mechanism.\n5. **Real-data framed as pattern consistency** — NOT ground-truth benchmark. No bias/RMSE against unknown true CATEs.\n6. **EC-HTE advantage is conditional, not universal** — ec_hte dominates when misclassification heterogeneity is high (extreme regime) OR n_expert is large (≥500). In moderate regime with small n_expert (~100), global correction can outperform ec_hte because per-subgroup CM estimation noise exceeds the benefit of stratification. This connects to Claim 3: the diagnostic criterion (Δπ×Δτ) predicts when EC-HTE is needed. Unified condition: n_expert/K ≥ ~25-50 experts per subgroup.\n11. **RMSE tradeoff must be disclosed** — ec_hte has higher RMSE than global/naive in K=4/n≤100 configs (up to 3.5x in extreme cases) due to noisy per-subgroup CM estimation. Bias is lower but variance is higher. Must report both bias AND RMSE; include bias-RMSE tradeoff analysis. At n_expert≥500, ec_hte RMSE becomes competitive.\n12. **K-dependence of debiasing-hurts** — DIM estimator: K=2 extreme ~2.86×, K=4 extreme ~2.41× (does NOT monotonically increase with K). CausalForest: K=4 extreme up to 5.9× (nonlinear estimator amplifies with more subgroups). Report both patterns; do NOT claim \"more subgroups → always worse\" without qualifying the estimator.\n7. **Confusion matrix invertibility** — State det(Ĉ_k) ≠ 0 assumption explicitly.\n8. **Diagnostic AUC cross-validated** — Leave-one-setting-out or held-out evaluation, not in-sample.\n9. **Hyperprior values stated + sensitivity analysis** — Gamma(α, β) for Dirichlet concentration; report sensitivity to 2× changes.\n10. **PPCI complementarity elevated** — Highlight in abstract and contributions. Frame as \"complementary\" not \"orthogonal\": EC-HTE is structured covariate-error correction; PPCI rectifier is general residual correction. Composition = EC-HTE handles structured part + rectifier handles remainder (primarily outcome error).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2. MUST report full MCMC diagnostics: sampler (PyMC\n    NUTS), chains (≥4), warmup (≥1000), R̂ (<1.01), ESS (>200), runtime vs MLE. Report\n    SEs/CIs for all metrics from MC runs. Monitor coverage calibration — if systematic\n    undercoverage, diagnose cause.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example. MUST include K>2 extension: verify bias formula empirically for K=4 subgroups;\n    add Remark after Proposition 1 discussing general-K case (sum-of-products form).\n    Report R² of analytic prediction vs MC, bound tightness ratio, and CIs on all\n    bias estimates.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim: 1,2,3\n  description: 'Semi-synthetic benchmark: use real CSS tweet corpus — TweetEval sentiment\n    (N=45K, primary) for exp-003. Framing broadened from ''political-science'' to\n    ''CSS'' per D004b (stance tasks N<1000 unusable). Inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 (API) and optionally Qwen3-235B-A22B (GPU), measure\n    subgroup-specific misclassification rates, apply EC-HTE vs baselines. Subgroup\n    variables: text features (has_hashtag, text_length) for semi-synthetic; demographic\n    subgroups reserved for exp-004. MUST fully specify DGP in paper: (a) outcome generation\n    model, (b) treatment assignment mechanism, (c) how true CATEs are injected. MUST\n    run LLM annotation pilot (~1000 samples) before committing to verify per-subgroup\n    misclassification heterogeneity exists.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim: 1,2\n  description: 'Real-data case study (pattern consistency, NOT ground-truth validation):\n    apply EC-HTE to real CSS dataset with subgroup-varying LLM misclassification.\n    Show: (a) global vs EC-HTE produce qualitatively different CATE distributions,\n    (b) EC-HTE results consistent with domain knowledge (demographic effect direction),\n    (c) bootstrap CIs on point estimate differences. Frame as ''illustrative application''\n    not ''ground-truth benchmark''. Reviewer confirmed: real data has no ground truth\n    CATE, CV-based ground truth is circular. PRIMARY: UC Berkeley Measuring Hate Speech\n    corpus (public, rich demographic subgroups). NICE-TO-HAVE: Ashwin et al. (2025)\n    if obtainable (requires author email + IRB, not feasible within 5-day DDL).'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference) or API\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: UC Berkeley dataset causal framework (T,Y,Z,S) mapping needs design\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold. MUST use\n    cross-validation or held-out evaluation (NOT in-sample AUC on own experiments).\n    Dream Round 2 flagged in-sample AUC as methodological weakness across best and\n    median tiers.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1,2\n  description: 'PPCI + DSL baseline comparison: (a) PPCI kernel-based conditional\n    correction vs EC-HTE on covariate-side vs outcome-side error; (b) per-subgroup\n    DSL as additional baseline (DSL applied independently per subgroup, no cross-subgroup\n    shrinkage — shows EC-HTE''s partial pooling advantage); (c) EC-HTE+PPCI composition\n    for simultaneous covariate+outcome error; (d) CRITICAL: include ''pure covariate-error,\n    zero outcome-error'' control condition to demonstrate EC-HTE advantage when covariate-side\n    error dominates (PPCI should be ineffective here). Paper framing: DSL per-subgroup\n    is a valid baseline but lacks cross-subgroup shrinkage and operates at estimand\n    level rather than measurement model level.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest integration: apply EC-HTE post-hoc correction to CausalForestDML\n    subgroup CATE estimates + leaf-level corrected pseudo-outcomes with variance-adjusted\n    CIs. Compare against naive forest and globally-corrected forest. ELEVATED TO P0:\n    Claim 2 explicitly states CausalForestDML but no experiment validates this — claim-evidence\n    gap is reviewer killshot.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mcmc_rhat_max: 1.024\n    mcmc_ess_min: 129\n    mcmc_divergent: 0\n    runtime_min: 69\n    total_mc_runs: 3600\n    hb_vs_mle_rmse_improvement_k2_n50: 4-9%\n    hb_vs_mle_rmse_improvement_k2_n100: 1-2%\n    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%\n    hb_coverage_min: 0.87\n    hb_coverage_median: 0.93\n    k4_extreme_n50_blowup: false\n    k4_extreme_n50_blowup_note: Fixed by singularity guard + 4-chain MCMC\n    mcmc_fix_4chain:\n      rhat_max_all_configs: 1.0034\n      ess_min_all_configs: 1618\n      ess_improvement: ~4x vs 2-chain\n      k4_extreme_n50_A_rmse_z0: 3.14 → 0.99\n      k4_extreme_n50_B_rmse_z0: 509.93 → 0.27\n      k4_extreme_n100_A_rmse_z0: 11.57 → 0.29\n      singularity_guard_triggers: extreme/n=50 only (2 HB, 3 MLE / 100 runs)\n      results_file: results/exp001_hb_results_v2.csv\n    hyperprior_sensitivity:\n      scale_range: 0.5-2.0\n      k2_rmse_variation: <1%\n      k4_rmse_variation: ~4-5%\n      coverage_invariant: true\n      conclusion: robust\n      results_file: results/exp001_hyperprior_sensitivity.csv\n- exp_id: exp-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r2_k2: 0.9939\n    r2_k4: 0.9738\n    tightness_ratio_k2_median: 1.0027\n    tightness_ratio_k4_median: 1.0234\n    debiasing_hurts_pct: 50\n    debiasing_hurts_pct_note: 260/520 (excluding dc=0 rows where bias=0)\n    debiasing_hurts_threshold_delta_misclass: 0.1235\n    max_bias_ratio_k2: 2.86\n    max_bias_ratio_k4: 2.41\n    coverage_2se_k2: 0.951\n    coverage_2se_k4: 0.94\n- exp_id: exp-007\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_rows: 6912\n    dgps:\n    - A_covariate_only\n    - B_outcome_only\n    - C_both_errors\n    - D_no_error\n    methods: 8\n    mc_runs: 100\n    double_correction_fix_verified: true\n    dgp_a_ec_hte_ppci_equals_ec_hte: true\n    dgp_c_extreme_n250_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.225\n      ec_hte_bias_z0: 0.178\n      ec_hte_rmse_z0: 0.226\n      ppci_bias_z0: 0.004\n      ppci_rmse_z0: 0.261\n      naive_bias_z0: 0.251\n      naive_rmse_z0: 0.269\n    dgp_c_n500_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.142\n      ec_hte_bias_z0: 0.088\n      ec_hte_rmse_z0: 0.134\n    key_finding: ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better\n      than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.\n- exp_id: exp-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase: A_semi_synthetic\n    n_subgroups: 4\n    misclass_rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25\n    subgroup_sizes: S0~38%, S1~38%, S2~12%, S3~12%\n    p_z1_actual: 0.39\n    debiasing_hurts_confirmed: true\n    mc_runs: 100\n    v3_hb_integration_100mc:\n      methods:\n      - oracle\n      - naive\n      - global_corrected\n      - stratified_mle\n      - hb_ec_hte\n      hb_vs_mle_summary:\n        n50_S3_extreme: -57% RMSE (HB worse, but not catastrophic)\n        n50_S3_moderate: -54% RMSE z1 (HB worse)\n        n100_S3_extreme: +60% RMSE z1 (HB dramatically better)\n        n100_S3_moderate: +24% RMSE z1 (HB better)\n        n100_S2: +5-8% RMSE (HB better)\n        n250_S3: +5-17% RMSE (HB better)\n        n500_all: +0.2-1.6% (converged)\n      key_finding: '100 MC confirms: S3 blowup at n=50 is real but moderate (not catastrophic\n        as dry-run suggested). At n>=100, HB is better everywhere, especially S3 (+26-60%).\n        Partial pooling sweet spot is n=100-250.'\n      hypothesis_verdict: validated_with_boundary\n      boundary_condition: n_expert>=100 recommended; n=50 with extreme heterogeneity\n        in tiny subgroups shows moderate degradation\n    results_file_v3: results/exp003_phase_a_v3.csv\n    results_file_v3_raw: results/exp003_phase_a_v3_raw.csv\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subgroup_level_auc: 0.833\n    subgroup_correlation: 0.86\n    setting_level_auc: 0.49\n    low_pi_hurt_pct: 84.6\n    high_pi_hurt_pct: 15.4\n    theory_alignment: consistent with exp-002 formula\n- exp_id: exp-011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    n_configs: 8\n    total_rows: 144\n    runtime_min: 35\n    methods:\n    - naive_forest\n    - global_forest\n    - ec_hte_forest\n    mean_abs_bias:\n      naive_forest: 0.1558\n      global_forest: 0.1073\n      ec_hte_forest: 0.0608\n    mean_rmse:\n      naive_forest: 0.1782\n      global_forest: 0.1659\n      ec_hte_forest: 0.2289\n    debiasing_hurts_cases: 9\n    debiasing_hurts_max_ratio: 5.9\n    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'\n    k2_n500_ec_hte_bias_range: 0.004-0.013 (near zero)\n    k2_n500_global_bias_range: 0.033-0.109 (still biased)\n    pattern_consistent_with_diff_in_means: true\n    claim2_validated: true\n- exp_id: exp-006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    total_rows: 288\n    runtime_min: 110\n    grid: n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]\n    crossover_hb_beats_global:\n      K2_extreme: 250\n      K2_moderate: never\n      K4_extreme: 1000\n      K4_moderate: 2000\n    hb_vs_mle: HB ≥ MLE in 21/24 configs (87.5%; partial pooling rarely hurts in symmetric\n      DGP)\n    hb_best_improvement_over_mle:\n      K4_moderate_n50_sgC: +42.4% RMSE\n      K4_extreme_n50_sgC: +23.4% RMSE\n      K4_moderate_n50_sgB: +24.0% RMSE\n    convergence: HB ≈ MLE at n≥1000 (<0.5% difference)\n    key_finding: 'Crossover depends strongly on K and regime. K=2: crossover at n=250\n      (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest\n      improvement over MLE via partial pooling.'\n- exp_id: exp-007b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    kill_reason: 'D012: Director 决定放弃 HB backfill。理由：PPCI 表核心 story 是互补性，HB vs MLE\n      是边际改进；exp-001 已验证 HB。CSV 已重命名为 .broken'\n- exp_id: exp-012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: gpt-4.1-2025-04-14\n    n_samples: 500\n    valid_annotations: 500\n    failed: 0\n    accuracy_3class: 0.672\n    accuracy_binary: 0.858\n    subgroup_misclass_rates:\n      hash_long: 0\n      hash_medium: 0.2\n      hash_short: 0.174\n      nohash_long: 0\n      nohash_medium: 0.102\n      nohash_short: 0.138\n    delta_pi: 0.2\n    heterogeneity_significant: true\n    key_finding: Hashtag presence increases binary misclassification rate (~0.17-0.20\n      vs ~0.10-0.14 for non-hashtag). Delta-pi=0.200 confirms meaningful heterogeneity\n      for EC-HTE correction.\n    analysis_file: results/pilot_gpt41_analysis.md\n- exp_id: exp-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    config: K=4/extreme/n_expert=50\n    n_expert_per_K: 12.5\n    hb_method: EB (Empirical Bayes, not Gibbs — conservative estimate for boundary\n      condition)\n    avg_rmse_naive: 0.109\n    avg_rmse_global: 0.14\n    avg_rmse_mle: 0.28\n    avg_rmse_eb: 0.292\n    worst_subgroup: A(pi=0.30) EB RMSE=0.62\n    amplification_max: 4.4x (A/EB vs global)\n    threshold_confirmed: n_expert/K=12.5 < 25\n    naive_beats_all: true\n    debiasing_hurts_D: Naive bias=0.001, Global bias=0.110 — extreme over-correction\n      in lowest-error subgroup\n- exp_id: exp-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    configs: 3\n    asymmetric_configs:\n    - balanced(FPR=0.15,FNR=0.25)\n    - fpr_dominant(FPR=0.30,FNR=0.10)\n    - fnr_dominant(FPR=0.10,FNR=0.30)\n    delta_tau_grid:\n    - 0\n    - 0.1\n    - 0.2\n    - 0.3\n    - 0.5\n    n_mc: 100\n    N: 5000\n    n_expert: 250\n    r2_analytic_vs_mc: 0.992\n    product_structure_cv: ~1e-16 (exact)\n    product_structure_confirmed: true\n    a2_not_required: true\n    ec_hte_avg_abs_bias: 0.006\n    ec_hte_avg_rmse: 0.033\n    ec_hte_avg_coverage: 0.9\n    global_avg_abs_bias: 0.025\n    global_avg_rmse: 0.04\n    global_avg_coverage: 0.78\n    naive_avg_abs_bias: 0.025\n    naive_avg_rmse: 0.039\n    naive_avg_coverage: 0.87\n    bias_reduction_vs_global: 4.2x\n    coverage_improvement_vs_global: +12pp\n    latex_derivation_included: true\n    key_finding: Product structure bias = Δτ·[B_s]_{z,1} holds exactly under asymmetric\n      misclassification. A2 (symmetric) assumption is NOT required. EC-HTE dominates\n      with 4.2x bias reduction.\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dataset: UC Berkeley Measuring Hate Speech\n    n_comments: 2496\n    valid_annotations: 2496\n    subgroups:\n      plat0_long: 624\n      plat0_short: 624\n      plat23_long: 624\n      plat23_short: 624\n    subgroup_type: text features (platform_group × text_length)\n    delta_pi: 0.117\n    global_FPR: 0.139\n    global_FNR: 0.533\n    misclass_rates:\n      plat0_long: 0.266\n      plat0_short: 0.337\n      plat23_long: 0.303\n      plat23_short: 0.383\n    avg_abs_bias:\n      naive: 0.21\n      global: 0.273\n      ec_hte: 0.313\n    cate_comparison: EC-HTE does not outperform global on avg |bias| — high FNR (~53%)\n      and wide CIs limit correction effectiveness on this dataset\n    key_finding: Δπ=0.117 confirms real-world misclassification heterogeneity across\n      text-feature subgroups. High global FNR (53%) indicates LLM severely under-classifies\n      dehumanization. CATE correction comparison inconclusive due to wide bootstrap\n      CIs.\n- exp_id: exp-008\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    models_completed:\n    - gpt-3.5-turbo\n    - gpt-4.1\n    - gpt-4o\n    - gpt-4o-mini\n    - gpt-4-turbo\n    - gpt-5.4\n    total_models: 6\n    proxy_provider: OpenAI only\n    gpt5x_model_used: gpt-5.4\n    gpt55_failed: reasoning tokens consume max_tokens budget, too slow (~1min/call)\n    filtered_analysis:\n      excluded_subgroups:\n      - False_long (n=6)\n      - True_long (n=4)\n      min_n_threshold: 10\n      retained_subgroups:\n      - False_medium (n=187)\n      - False_short (n=109)\n      - True_medium (n=125)\n      - True_short (n=69)\n    effective_delta_pi:\n      gpt-3.5-turbo: 0.198\n      gpt-4-turbo: 0.149\n      gpt-4.1: 0.098\n      gpt-4o: 0.08\n      gpt-4o-mini: 0.136\n      gpt-5.4: 0.114\n    all_effective_delta_pi_above_005: true\n    worst_subgroup_consensus: True_medium (5/6 models)\n    spearman_significant_pairs:\n    - gpt-4-turbo vs gpt-4o (ρ=1.000)\n    - gpt-4.1 vs gpt-4o-mini (ρ=1.000)\n    - gpt-4.1 vs gpt-5.4 (ρ=1.000)\n    - gpt-4o-mini vs gpt-5.4 (ρ=1.000)\n    spearman_note: Only 4 subgroups after filtering, limited statistical power (most\n      p>0.20)\n    key_finding: All 6 models (GPT-3.5 through GPT-5.4, three generations) show effective\n      Δπ > 0.05 after excluding n<10 subgroups. Heterogeneity is structural, not model-specific.\n- exp_id: exp-010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    configs: 2\n    noise_levels:\n    - 0\n    - 0.1\n    - 0.25\n    - 0.5\n    total_runs: 800\n    runtime_sec: 15\n    k2_coverage_naive:\n    - 0.875\n    - 0.877\n    - 0.89\n    - 0.897\n    k2_coverage_hb:\n    - 0.958\n    - 0.948\n    - 0.95\n    - 0.945\n    k2_coverage_global:\n    - 0.925\n    - 0.935\n    - 0.932\n    - 0.945\n    k4_coverage_naive:\n    - 0.904\n    - 0.916\n    - 0.909\n    - 0.919\n    k4_coverage_hb:\n    - 0.956\n    - 0.958\n    - 0.96\n    - 0.946\n    k4_coverage_global:\n    - 0.93\n    - 0.953\n    - 0.948\n    - 0.944\n    hb_beats_mle_all_configs: true\n    hb_improvement_range: +0.1% to +0.9% RMSE\n    graceful_convergence_at_50pct: true\n    key_finding: 'Coverage is the decisive metric: naive 87-92%, EC-HTE 95-96% across\n      all noise levels. No catastrophic failure. HB shrinkage provides automatic safeguard\n      — converges to global at 50% noise.'\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:25:01.754Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:25:01.754Z",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T12:25:01.778Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this "debiasing" can worsen CATE bias by 2-3x (median across configurations), with amplification up to 5.9x for K=4 subgroups; when naive bias is near zero, global correction creates bias where none existed. For the difference-in-means estimator, the amplification magnitude does NOT monotonically increase with K (K=2 extreme: up to 2.86× vs K=4 extreme: up to 2.41×); however, with nonlinear estimators such as CausalForest, more subgroups amplify the effect substantially (K=4/extreme: up to 5.9×) due to compounding estimation noise in tree-based CATE. Global correction increases subgroup-level bias in ~50% of the parameter space.

2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias when misclassification heterogeneity is sufficiently high, while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction by borrowing strength across groups (classic James-Stein shrinkage). We provide precise crossover thresholds: EC-HTE outperforms global correction in RMSE with as few as 250 expert labels (K=2, high heterogeneity), scaling to ~1000 for K=4. **Boundary condition**: when expert labels per subgroup < ~25, shrinkage can be harmful — stratified MLE is preferred. **EC-HTE is most valuable precisely when it is most needed — the diagnostic criterion (Claim 3) identifies these scenarios.** **CONFIRMED** by exp-003 full 100 MC (1200 runs, 0 errors). HB crossover at ~11 experts/subgroup; ≥25 recommended for robust performance. Demonstrated with both difference-in-means and CausalForestDML (exp-011: consistent bias reduction pattern, ec_hte_forest |bias|=0.06 vs naive 0.16). CausalForest amplifies the debiasing-hurts effect (up to 5.9x in K=4/extreme) due to nonlinear CATE estimation.

3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic that simultaneously predicts when global correction is harmful (Claim 1) and when the expert label investment for stratified correction is worthwhile (connecting to the budget guidelines from Claim 2). This criterion has standalone value independent of EC-HTE — even without adopting EC-HTE, knowing when global correction backfires is practically actionable.

## Story Spine

- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis across computational social science (CSS) — e.g., sentiment framing moderates message effectiveness, hate speech type moderates intervention impact. LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education; documented across CSS tasks including sentiment, stance, toxicity). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.

- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**

- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as "problem identification + principled solution" not "new estimation technique."

- **Headline result template**: "On semi-synthetic CSS benchmarks, global correction worsens subgroup CATE bias by 2-3x (median), with amplification up to 5.9x for K=4 subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels. Combined with PPCI, the composition achieves near-zero bias (0.005) even when both covariate and outcome errors are present."

- **Oracle framing**: When reporting DGP C results where ec_hte_ppci outperforms oracle, always use "covariate-oracle" (true Z + observed Y), never unqualified "oracle". Frame as "composite correction is necessary and sufficient when both error types coexist" — NOT "beats oracle". The result is by construction (ec_hte_ppci corrects both error types; covariate-oracle only corrects one), not surprising.

## Key Contributions (ordered for paper)

1. **Bias decomposition identity**: Exact population-level identity: bias ∝ misclassification heterogeneity × CATE heterogeneity (Δπ×Δτ product form). NOT a bound — it is an exact identity under A1–A4; finite-sample R² measures MC noise, not bound looseness. Includes "debiasing can hurt" proposition with constructive example. Frame as "bias decomposition" or "bias identity" throughout — never "bias bound." (Theory + Empirical)
2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)
3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)
4. **EC-HTE + PPCI composition — empirically necessary and sufficient**: EC-HTE and PPCI are empirically necessary and sufficient in composition: neither alone adequately handles dual-error scenarios (DGP C), but their composition reduces bias to near-zero (0.005, a 35× improvement over EC-HTE alone). EC-HTE exploits mixing matrix structure for covariate-side error; PPCI rectifier captures outcome-side error. PPCI alone can partially correct covariate error but with higher variance (limited by gold subset size). In Methods, retain full discussion of partial overlap; in Abstract, lead with "necessary and sufficient in composition." (Method + Empirical)
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
12. **K-dependence of debiasing-hurts** — DIM estimator: K=2 extreme ~2.86×, K=4 extreme ~2.41× (does NOT monotonically increase with K). CausalForest: K=4 extreme up to 5.9× (nonlinear estimator amplifies with more subgroups). Report both patterns; do NOT claim "more subgroups → always worse" without qualifying the estimator.
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
    v3_hb_integration_100mc:
      methods:
      - oracle
      - naive
      - global_corrected
      - stratified_mle
      - hb_ec_hte
      hb_vs_mle_summary:
        n50_S3_extreme: -57% RMSE (HB worse, but not catastrophic)
        n50_S3_moderate: -54% RMSE z1 (HB worse)
        n100_S3_extreme: +60% RMSE z1 (HB dramatically better)
        n100_S3_moderate: +24% RMSE z1 (HB better)
        n100_S2: +5-8% RMSE (HB better)
        n250_S3: +5-17% RMSE (HB better)
        n500_all: +0.2-1.6% (converged)
      key_finding: '100 MC confirms: S3 blowup at n=50 is real but moderate (not catastrophic
        as dry-run suggested). At n>=100, HB is better everywhere, especially S3 (+26-60%).
        Partial pooling sweet spot is n=100-250.'
      hypothesis_verdict: validated_with_boundary
      boundary_condition: n_expert>=100 recommended; n=50 with extreme heterogeneity
        in tiny subgroups shows moderate degradation
    results_file_v3: results/exp003_phase_a_v3.csv
    results_file_v3_raw: results/exp003_phase_a_v3_raw.csv
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
    hb_vs_mle: HB ≥ MLE in 21/24 configs (87.5%; partial pooling rarely hurts in symmetric
      DGP)
    hb_best_improvement_over_mle:
      K4_moderate_n50_sgC: +42.4% RMSE
      K4_extreme_n50_sgC: +23.4% RMSE
      K4_moderate_n50_sgB: +24.0% RMSE
    convergence: HB ≈ MLE at n≥1000 (<0.5% difference)
    key_finding: 'Crossover depends strongly on K and regime. K=2: crossover at n=250
      (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest
      improvement over MLE via partial pooling.'
- exp_id: exp-007b
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    kill_reason: 'D012: Director 决定放弃 HB backfill。理由：PPCI 表核心 story 是互补性，HB vs MLE
      是边际改进；exp-001 已验证 HB。CSV 已重命名为 .broken'
- exp_id: exp-012
  name: ''
  status: DONE
  conclusion: success
  metrics:
    model: gpt-4.1-2025-04-14
    n_samples: 500
    valid_annotations: 500
    failed: 0
    accuracy_3class: 0.672
    accuracy_binary: 0.858
    subgroup_misclass_rates:
      hash_long: 0
      hash_medium: 0.2
      hash_short: 0.174
      nohash_long: 0
      nohash_medium: 0.102
      nohash_short: 0.138
    delta_pi: 0.2
    heterogeneity_significant: true
    key_finding: Hashtag presence increases binary misclassification rate (~0.17-0.20
      vs ~0.10-0.14 for non-hashtag). Delta-pi=0.200 confirms meaningful heterogeneity
      for EC-HTE correction.
    analysis_file: results/pilot_gpt41_analysis.md
- exp_id: exp-013
  name: ''
  status: DONE
  conclusion: success
  metrics:
    config: K=4/extreme/n_expert=50
    n_expert_per_K: 12.5
    hb_method: EB (Empirical Bayes, not Gibbs — conservative estimate for boundary
      condition)
    avg_rmse_naive: 0.109
    avg_rmse_global: 0.14
    avg_rmse_mle: 0.28
    avg_rmse_eb: 0.292
    worst_subgroup: A(pi=0.30) EB RMSE=0.62
    amplification_max: 4.4x (A/EB vs global)
    threshold_confirmed: n_expert/K=12.5 < 25
    naive_beats_all: true
    debiasing_hurts_D: Naive bias=0.001, Global bias=0.110 — extreme over-correction
      in lowest-error subgroup
- exp_id: exp-014
  name: ''
  status: DONE
  conclusion: success
  metrics:
    configs: 3
    asymmetric_configs:
    - balanced(FPR=0.15,FNR=0.25)
    - fpr_dominant(FPR=0.30,FNR=0.10)
    - fnr_dominant(FPR=0.10,FNR=0.30)
    delta_tau_grid:
    - 0
    - 0.1
    - 0.2
    - 0.3
    - 0.5
    n_mc: 100
    N: 5000
    n_expert: 250
    r2_analytic_vs_mc: 0.992
    product_structure_cv: ~1e-16 (exact)
    product_structure_confirmed: true
    a2_not_required: true
    ec_hte_avg_abs_bias: 0.006
    ec_hte_avg_rmse: 0.033
    ec_hte_avg_coverage: 0.9
    global_avg_abs_bias: 0.025
    global_avg_rmse: 0.04
    global_avg_coverage: 0.78
    naive_avg_abs_bias: 0.025
    naive_avg_rmse: 0.039
    naive_avg_coverage: 0.87
    bias_reduction_vs_global: 4.2x
    coverage_improvement_vs_global: +12pp
    latex_derivation_included: true
    key_finding: Product structure bias = Δτ·[B_s]_{z,1} holds exactly under asymmetric
      misclassification. A2 (symmetric) assumption is NOT required. EC-HTE dominates
      with 4.2x bias reduction.
- exp_id: exp-004
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dataset: UC Berkeley Measuring Hate Speech
    n_comments: 2496
    valid_annotations: 2496
    subgroups:
      plat0_long: 624
      plat0_short: 624
      plat23_long: 624
      plat23_short: 624
    subgroup_type: text features (platform_group × text_length)
    delta_pi: 0.117
    global_FPR: 0.139
    global_FNR: 0.533
    misclass_rates:
      plat0_long: 0.266
      plat0_short: 0.337
      plat23_long: 0.303
      plat23_short: 0.383
    avg_abs_bias:
      naive: 0.21
      global: 0.273
      ec_hte: 0.313
    cate_comparison: EC-HTE does not outperform global on avg |bias| — high FNR (~53%)
      and wide CIs limit correction effectiveness on this dataset
    key_finding: Δπ=0.117 confirms real-world misclassification heterogeneity across
      text-feature subgroups. High global FNR (53%) indicates LLM severely under-classifies
      dehumanization. CATE correction comparison inconclusive due to wide bootstrap
      CIs.
- exp_id: exp-008
  name: ''
  status: DONE
  conclusion: success
  metrics:
    models_completed:
    - gpt-3.5-turbo
    - gpt-4.1
    - gpt-4o
    - gpt-4o-mini
    - gpt-4-turbo
    - gpt-5.4
    total_models: 6
    proxy_provider: OpenAI only
    gpt5x_model_used: gpt-5.4
    gpt55_failed: reasoning tokens consume max_tokens budget, too slow (~1min/call)
    filtered_analysis:
      excluded_subgroups:
      - False_long (n=6)
      - True_long (n=4)
      min_n_threshold: 10
      retained_subgroups:
      - False_medium (n=187)
      - False_short (n=109)
      - True_medium (n=125)
      - True_short (n=69)
    effective_delta_pi:
      gpt-3.5-turbo: 0.198
      gpt-4-turbo: 0.149
      gpt-4.1: 0.098
      gpt-4o: 0.08
      gpt-4o-mini: 0.136
      gpt-5.4: 0.114
    all_effective_delta_pi_above_005: true
    worst_subgroup_consensus: True_medium (5/6 models)
    spearman_significant_pairs:
    - gpt-4-turbo vs gpt-4o (ρ=1.000)
    - gpt-4.1 vs gpt-4o-mini (ρ=1.000)
    - gpt-4.1 vs gpt-5.4 (ρ=1.000)
    - gpt-4o-mini vs gpt-5.4 (ρ=1.000)
    spearman_note: Only 4 subgroups after filtering, limited statistical power (most
      p>0.20)
    key_finding: All 6 models (GPT-3.5 through GPT-5.4, three generations) show effective
      Δπ > 0.05 after excluding n<10 subgroups. Heterogeneity is structural, not model-specific.
- exp_id: exp-010
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_mc: 100
    configs: 2
    noise_levels:
    - 0
    - 0.1
    - 0.25
    - 0.5
    total_runs: 800
    runtime_sec: 15
    k2_coverage_naive:
    - 0.875
    - 0.877
    - 0.89
    - 0.897
    k2_coverage_hb:
    - 0.958
    - 0.948
    - 0.95
    - 0.945
    k2_coverage_global:
    - 0.925
    - 0.935
    - 0.932
    - 0.945
    k4_coverage_naive:
    - 0.904
    - 0.916
    - 0.909
    - 0.919
    k4_coverage_hb:
    - 0.956
    - 0.958
    - 0.96
    - 0.946
    k4_coverage_global:
    - 0.93
    - 0.953
    - 0.948
    - 0.944
    hb_beats_mle_all_configs: true
    hb_improvement_range: +0.1% to +0.9% RMSE
    graceful_convergence_at_50pct: true
    key_finding: 'Coverage is the decisive metric: naive 87-92%, EC-HTE 95-96% across
      all noise levels. No catastrophic failure. HB shrinkage provides automatic safeguard
      — converges to global at 50% noise.'

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "aff6e893-9260-4a23-ba5b-61bfd4cbaacc",
  "type": "user",
  "uuid": "cefbef99-f3f6-43a3-b211-c098035ba45a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:25:01.776Z_

```json
{
  "parentUuid": "cefbef99-f3f6-43a3-b211-c098035ba45a",
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
  "uuid": "9bd30a8c-49f6-4800-9ef8-3e5035c5c587",
  "timestamp": "2026-05-21T12:25:01.776Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:25:01.776Z_

```json
{
  "parentUuid": "9bd30a8c-49f6-4800-9ef8-3e5035c5c587",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1ae5f996-2371-46ed-88ac-406f7dacfe88",
  "timestamp": "2026-05-21T12:25:01.776Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "1ae5f996-2371-46ed-88ac-406f7dacfe88",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for ec_hte_llm_annotation",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:26:35.588Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a Dream simulation based on the extensive research context provided. This is about the EC-HTE project targeting EMNLP 2026.

Let me analyze the completed experiments and what's left:

**Completed experiments**: exp-001, exp-002, exp-003, exp-005, exp-006, exp-007, exp-008, exp-010, exp-011, exp-012, exp-013, exp-014, exp-004

**Key results so far**:
- Bias mechanism (Claim 1): Confirmed. R²=0.99 (K=2), 0.97 (K=4). Debiasing hurts in ~50% of parameter space. 
- Amplification effects peak at 2.86x for K=2, 2.41x with K=4 DIM, and reach 5.9x with K=4 CausalForest.
- EC-HTE (Claim 2): Confirmed with boundary conditions. HB crossover at n=250 (K=2/extreme), n=1000 (K=4/extreme). Boundary at n_expert/K < 25.
- Diagnostic (Claim 3): Subgroup-level AUC=0.833, but setting-level AUC=0.49 (poor).
- PPCI composition: Near-zero bias (0.005) in DGP C.
- All 6 LLM models show Δπ > 0.05, while real data results are inconclusive due to high false negative rates. CausalForest confirms the bias reduction pattern, and asymmetric misclassification follows the product structure exactly. Robustness testing shows graceful degradation with 95-96% coverage across noise levels, though exp-009 on adaptive allocation remains pending.

The semi-synthetic results demonstrate HB works under specific boundary conditions, but real data didn't show EC-HTE outperforming the global approach. The diagnostic criterion achieves good subgroup-level AUC at 0.833 but struggles at the setting level with 0.49. The debiasing advantage is real but conditional, and there's a notable RMSE tradeoff where EC-HTE performs worse in small-sample configurations. Beyond the experimental results, I'm also contending with writing quality and framing challenges as I think about what these findings mean for the paper.

Now I'm mapping out what could realistically happen in the final push toward submission. Most experiments are already complete, leaving three main uncertainties: whether the paper narrative can be told compellingly, whether the real data case study can be salvaged from its inconclusive results, and whether the diagnostic criterion's poor setting-level performance becomes a fatal flaw. The reviewer reception is also a wildcard—will they see enough novelty despite the mixed results?

I'm sketching out three outcome scenarios. In the best case, all three core claims hold up strongly, the real data aligns with the theory, the diagnostic works convincingly at the setting level, and the narrative flows cleanly. The median scenario has claims one and two surviving but with substantial caveats—the real data shows patterns consistent with the theory but isn't fully convincing, and the diagnostic only works reliably at the subgroup level, requiring me to dial back the strength of my claims. The worst case is when real data actively contradicts the findings and the diagnostic fails outright.

The real question is what experiments might still shift these outcomes and what metrics matter most for evaluating where we actually stand.

The core problems are stark: the diagnostic criterion fails at the setting level (0.49 AUC) even though it works for subgroups, EC-HTE performs worse than naive approaches on real data, and RMSE tradeoffs are unfavorable at small sample sizes. Reviewers will likely see this as incremental unless we can reframe the contribution or get stronger empirical support.

The best-case scenario hinges on whether the semi-synthetic experiments with better annotations show EC-HTE's advantage holds, and whether redefining subgroups in the real data reveals where the method actually helps. Diagnostic criterion improved with cross-validated approach, AUC ≥ 0.80
- Bias amplification narrative is compelling
- Paper accepted at EMNLP

**Median**:
- Semi-synthetic results hold as-is (strong in extreme regime, weak in moderate)
- Real data remains inconclusive, framed as pattern consistency only
- Diagnostic criterion works at subgroup level only, honest framing
- Need to weaken Claim 3, strengthen Claim 1 (bias mechanism discovery) as main contribution
- Paper competitive but needs revision

**Worst**:
- Additional experiments reveal EC-HTE's advantage is narrower than claimed
- Real data contradicts (already showing signs)
- Diagnostic criterion fails cross-validation
- Reviewers see it as "just Bayesian measurement error correction, classical result"
- Need to reframe entirely around bias mechanism discovery only

Now I'm looking at the specific numbers to ground each claim. The bias amplification story is solid with R² values near 0.99 for K=2 and 0.97 for K=4, plus amplification factors reaching 5.9x in some configurations. For EC-HTE, the mean bias improvements look promising but RMSE tells a different story—the method actually performs worse on that metric. The diagnostic criterion achieves 0.833 AUC at the subgroup level, which is respectable but limited in scope. Now I'm thinking through what success looks like across different scenarios—whether the remaining analysis validates the claims strongly, whether the existing results can be presented compellingly, and how to address the gaps in the diagnostic and real-data findings. I'm sketching out a tiered framework in YAML that maps best/median/worst outcomes to specific thresholds: the diagnostic criterion needs to hit AUC ≥ 0.75 through subgroup-level reformulation, the real-data reanalysis should show consistent directional patterns with refined definitions, and the overall narrative should position this as a bias mechanism discovery suitable for EMNLP.

Writing config YAML... The diagnostic criterion only works reliably at the subgroup level with an AUC around 0.83, but falls apart at the setting level, so I can't use it to predict when EC-HTE should be applied versus a global approach. Real data from the latest experiment doesn't show EC-HTE outperforming the global baseline on bias magnitude—the false negative rate is too high and there aren't enough experts per subgroup to make a difference. The core claims about the bias mechanism and EC-HTE solution still hold under specific boundary conditions, though I need to recalibrate what I'm claiming about the diagnostic's generalizability, and there's a real tradeoff with RMSE to contend with. Now I'm looking at the performance ranges across different diagnostic metrics and real-world scenarios—the subgroup AUC is strong at 0.80-0.85, but the setting-level diagnostic performance is weaker at 0.45-0.65, and the real data results are inconclusive on whether EC-HTE actually beats the global approach. The crossover points where hierarchical Bayes becomes competitive are around 200-350 experts for K=2 and 800-1500 for K=4 in extreme heterogeneity regimes, with EC-HTE showing a penalty of 1.2-3.5x worse RMSE when sample sizes are small. I'm reconsidering whether to downgrade the diagnostic criterion claim to just a heuristic given these mixed results.

The narrative shift I'm planning is to anchor the paper on the novel bias mechanism as the primary contribution, reframe the EC-HTE advantage as conditional and honest about its boundaries, and shorten the real data section to just demonstrate that heterogeneity exists rather than claiming EC-HTE solves it. I should add an explicit section on when not to use EC-HTE and highlight PPCI composition as the practical value proposition. If reviewers push back on novelty or the real data contradicts the method's benefit, I'd need to restructure the entire framing around the bias mechanism alone. Now I'm tracking the specific numerical ranges across these key metrics—bias amplification peaks around 2.4 to 2.9 in the maximum dimension case, while the counterfactual scenario shows even larger effects between 4.5 and 6.0. The EC-HTE method shows only marginal improvement over the global baseline (0.8 to 1.5 range), and on real data it actually performs worse by 0.02 to 0.10 in absolute bias terms. The diagnostic criterion fails cross-validation badly with AUC between 0.40 and 0.55, and there's a consistent RMSE penalty of 1.3 to 2.5 times across configurations—this tradeoff is what reviewers see as fundamentally disqualifying.

I'm reconsidering the entire paper structure. Instead of defending three separate claims, I should collapse everything into a single focused argument: global debiasing corrections can paradoxically amplify subgroup-specific bias when the correction mechanism interacts badly with heterogeneous treatment effects. Claim 1 about the bias mechanism becomes the whole paper, while EC-HTE gets repositioned as just one attempted fix with honest acknowledgment that its practical advantages are quite limited. The diagnostic tool shifts from being a decision rule to a sufficient condition for flagging when global correction is risky. This makes the paper tighter and more defensible—shorter overall, with PPCI composition kept as a practical recommendation but not oversold.

Now I need to recalibrate the experimental tiers since most of the work is actually done. The real uncertainties left are whether the diagnostic's cross-validation performance holds up, whether I can improve the real data results, and how reviewers will react. I should organize the tiers around which metrics are still in flux versus which are locked in, and how I'm interpreting the existing evidence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ae5f996-2371-46ed-88ac-406f7dacfe88",
  "isSidechain": false,
  "requestId": "req_011CbFi7WhRGfxb5rkDZjUYe",
  "type": "assistant",
  "uuid": "a9c56e7f-fd37-42b9-80b6-14850c82c95e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNdQ7oDf63pWjRG4KrcUMA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17025,
      "cache_read_input_tokens": 11841,
      "output_tokens": 6913,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 6913,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17025
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

_source line 9 · 2026-05-21T12:27:13.716Z_

```yaml
tiers:
  best:
    meaning: "三条 Claims 均有强证据支撑；诊断准则经交叉验证后仍有效；real data 重分析显示模式一致性；EMNLP 审稿人接受 'problem discovery + principled solution' 定位"
    key_assumptions:
      - "诊断准则 (Claim 3) 从 setting-level 重构为 subgroup-level 预测任务后，leave-one-setting-out CV AUC ≥ 0.75（当前 subgroup AUC=0.833 可迁移至 CV 设定）"
      - "exp-004 real data 通过更细粒度 subgroup 定义或补充第二数据集（如 TweetEval sentiment），EC-HTE 至少展示方向性一致的 bias reduction 或 coverage 优势"
      - "RMSE tradeoff 被审稿人接受：bias reduction 是 primary metric，RMSE 在 n_expert ≥ 500 时已 competitive"
      - "PPCI 互补性 (35x bias reduction in DGP C) 被视为实质性贡献"
      - "审稿人认可 bias mechanism discovery 的独立价值，不要求 convergence rates 或 minimax bounds"
    number_ranges:
      bias_amplification_max_dim: [2.4, 2.9]
      bias_amplification_max_cf: [5.0, 6.5]
      ec_hte_bias_reduction_factor_vs_global: [2.0, 4.5]
      ec_hte_ppci_bias_dgp_c: [0.002, 0.010]
      r2_bias_identity_k2: [0.99, 0.995]
      r2_bias_identity_k4: [0.97, 0.98]
      diagnostic_auc_cv: [0.75, 0.85]
      real_data_delta_pi: [0.10, 0.20]
      coverage_ec_hte: [0.92, 0.97]
      hb_crossover_k2_extreme: [200, 300]
      hb_crossover_k4_extreme: [800, 1200]
      multi_llm_delta_pi_min: [0.05, 0.08]
    narrative_direction: "原始三 Claim 结构完整保留。Lead with 'debiasing can hurt' 作为 surprising finding（50% parameter space, up to 5.9x amplification），EC-HTE 作为 principled fix with precise budget guidelines，诊断准则作为 practical decision tool。PPCI 互补性升级至 Contribution #4。Real data 作为 consistent illustration。Headline: 'Global correction worsens subgroup CATE bias by 2-3x median; EC-HTE reduces bias to near-zero with 250 expert labels; composition with PPCI achieves 0.005 bias under dual error.' 审稿周期 1R accept 或 minor revision。"

  median:
    meaning: "Claim 1（bias mechanism）完全成立；Claim 2（EC-HTE）成立但 boundary conditions 显著；Claim 3（diagnostic）降级为 heuristic；real data 不 conclusive；论文需调整 claims 强度但仍 EMNLP-competitive"
    key_assumptions:
      - "诊断准则 setting-level CV AUC 停留在 0.45-0.65，无法作为可靠决策工具；subgroup-level AUC ~0.83 仍有价值但不足以支撑独立 Claim"
      - "exp-004 real data 维持现状：EC-HTE |bias|=0.313 vs global 0.273 — EC-HTE 未胜出，因 FNR=53% 和小 n_expert/subgroup"
      - "RMSE tradeoff 实质性存在：K=4/n_expert≤250 时 EC-HTE RMSE 比 global 差 1.2-3.5x"
      - "审稿人对 novelty 有保留（'incremental over classical measurement error'）但 rebuttal 后可接受"
      - "EC-HTE 优势限于 extreme heterogeneity + n_expert ≥ 500 的条件下"
    number_ranges:
      bias_amplification_max_dim: [2.4, 2.9]
      bias_amplification_max_cf: [5.0, 6.0]
      ec_hte_bias_reduction_factor_vs_global: [1.5, 3.0]
      ec_hte_ppci_bias_dgp_c: [0.003, 0.015]
      r2_bias_identity_k2: [0.99, 0.995]
      r2_bias_identity_k4: [0.96, 0.98]
      diagnostic_auc_cv: [0.45, 0.65]
      diagnostic_auc_subgroup: [0.80, 0.85]
      real_data_ec_hte_vs_global_bias_diff: [-0.05, 0.05]
      coverage_ec_hte: [0.90, 0.96]
      ec_hte_rmse_penalty_small_n: [1.2, 3.5]
      hb_crossover_k2_extreme: [200, 350]
      hb_crossover_k4_extreme: [800, 1500]
      hb_crossover_k4_moderate: [1500, 2500]
    narrative_direction: "Claim 3 从 'diagnostic criterion' 降级为 'diagnostic heuristic'——用于标记 subgroup-level risk 但非可靠决策工具。Claim 2 重构为 'conditional improvement with explicit boundary conditions'，增加 'When NOT to use EC-HTE' 小节。Claim 1 升级为 primary contribution（bias identity 完全确认，独立于 EC-HTE 是否被采用均有价值）。Real data 缩短为 illustrative application，着重展示 heterogeneity 存在而非 EC-HTE 优势。PPCI 互补性成为关键卖点弥补 EC-HTE 单独使用的局限。可能需要 revision 阶段补充实验（larger real dataset 或 additional DGP）。预期 1-2R 后 accept。"

  worst:
    meaning: "Claim 1（bias mechanism）仍然成立但 EC-HTE 在实际条件下优势微弱；诊断准则 CV 失败；real data 反向；审稿人以 novelty 不足拒稿。需彻底 reframe 为以 Claim 1 为核心的 'bias mechanism discovery' 单 claim 论文"
    key_assumptions:
      - "诊断准则 CV AUC < 0.55，Δπ×Δτ product 不具泛化预测力"
      - "Real data 持续显示 EC-HTE 比 global 差（当前 |bias| 差距 0.04，可能在更多配置下复现）"
      - "EC-HTE 优势仅存在于 synthetic extreme regime；moderate regime 和 real data 均无 benefit 或 degradation"
      - "审稿人将 RMSE tradeoff 视为 disqualifying：'reduces bias but increases MSE — net negative in practice'"
      - "Novelty 论点（'just Bayesian CM estimation applied to CATE'）未说服审稿人；被要求与 Carroll et al. 2006 做更深对比"
      - "PPCI 互补性被视为 trivial（两个 correction 覆盖两种 error，construction by design）"
    number_ranges:
      bias_amplification_max_dim: [2.4, 2.9]
      bias_amplification_max_cf: [4.5, 6.0]
      ec_hte_bias_reduction_factor_vs_global: [0.8, 1.5]
      diagnostic_auc_cv: [0.40, 0.55]
      real_data_ec_hte_minus_global_abs_bias: [0.02, 0.10]
      ec_hte_rmse_penalty_median_across_configs: [1.3, 2.5]
      coverage_ec_hte_small_n: [0.85, 0.92]
      hb_crossover_k4_moderate: [2000, "never"]
    narrative_direction: "放弃三 Claim 结构。重构为单 claim 论文：'Debiasing Can Hurt — When Global Misclassification Correction Amplifies Subgroup CATE Bias'。Claim 1（bias identity + exact product form + constructive 'debiasing hurts' proposition）成为整篇论文核心。EC-HTE 降级为 'one possible mitigation' 放在较短的 methods section，诚实评估其实际优势条件狭窄。诊断准则重构为 sufficient condition for concern（Δπ×Δτ 大时 global correction 肯定有风险）而非 decision tool。PPCI 保留为实用建议但去主次化。论文变短、更聚焦、理论更强。仍投 EMNLP main——bias mechanism result 本身对 CSS+NLP 社区有新颖性和实用价值，类似 'negative result + formal characterization' 类型的成功论文。预期需要 2R 或 resubmit，但不降级 venue。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9c56e7f-fd37-42b9-80b6-14850c82c95e",
  "isSidechain": false,
  "requestId": "req_011CbFi7WhRGfxb5rkDZjUYe",
  "type": "assistant",
  "uuid": "908cb0d6-c20f-48e0-86d3-a3306f2b5f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNdQ7oDf63pWjRG4KrcUMA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17025,
      "cache_read_input_tokens": 11841,
      "output_tokens": 6913,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 6913,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17025
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "908cb0d6-c20f-48e0-86d3-a3306f2b5f1c",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for ec_hte_llm_annotation",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "908cb0d6-c20f-48e0-86d3-a3306f2b5f1c",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for ec_hte_llm_annotation",
  "sessionId": "89e58173-a620-4c29-b3fe-1f83e9868dc7"
}
```

---
