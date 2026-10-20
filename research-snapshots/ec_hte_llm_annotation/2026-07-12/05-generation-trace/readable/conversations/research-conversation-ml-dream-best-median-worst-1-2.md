# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/eb14b2bb-7025-4ead-996a-0fab8e4a37fc.jsonl`
- **Structured JSON:** [`01024ee61005ca320122.json`](../../sessions/01/01024ee61005ca320122.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T19:31:19.765Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T19:31:19.765Z",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: ec_hte_llm_annotation\nvenue: emnlp-2026\nfocus: Reframed paper: title changed to \"When Debiasing Hurts\", core contributions shifted from EC-HTE method to (1) exact bias identity + (2) actionable diagnostic. EC-HTE de-emphasized as \"the correction prescribed by the identity.\" New real-data validation on CivilComments (R²=0.944, 14 LLM-dataset combinations). Evaluate whether this framing shift improves Excitement scores vs previous 3/3.5 baseline.\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 2-3x (median across configurations), with amplification up to 5.9x for K=4 subgroups; when naive bias is near zero, global correction creates bias where none existed. For the difference-in-means estimator, the amplification magnitude does NOT monotonically increase with K (K=2 extreme: up to 2.86× vs K=4 extreme: up to 2.41×); however, with nonlinear estimators such as CausalForest, more subgroups amplify the effect substantially (K=4/extreme: up to 5.9×) due to compounding estimation noise in tree-based CATE. Global correction increases subgroup-level bias in ~50% of the parameter space.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias when misclassification heterogeneity is sufficiently high, while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction by borrowing strength across groups (classic James-Stein shrinkage). We provide precise crossover thresholds: EC-HTE outperforms global correction in RMSE with as few as 250 expert labels (K=2, high heterogeneity), scaling to ~1000 for K=4. **Boundary condition**: when expert labels per subgroup < ~25, shrinkage can be harmful — stratified MLE is preferred. **EC-HTE is most valuable precisely when it is most needed — the diagnostic criterion (Claim 3) identifies these scenarios.** **CONFIRMED** by exp-003 full 100 MC (1200 runs, 0 errors). HB crossover at ~11 experts/subgroup; ≥25 recommended for robust performance. Demonstrated with both difference-in-means and CausalForestDML (exp-011: consistent bias reduction pattern, ec_hte_forest |bias|=0.06 vs naive 0.16). CausalForest amplifies the debiasing-hurts effect (up to 5.9x in K=4/extreme) due to nonlinear CATE estimation.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic that simultaneously predicts when global correction is harmful (Claim 1) and when the expert label investment for stratified correction is worthwhile (connecting to the budget guidelines from Claim 2). This criterion has standalone value independent of EC-HTE — even without adopting EC-HTE, knowing when global correction backfires is practically actionable.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis across computational social science (CSS) — e.g., sentiment framing moderates message effectiveness, hate speech type moderates intervention impact. LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education; documented across CSS tasks including sentiment, stance, toxicity). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as \"problem identification + principled solution\" not \"new estimation technique.\"\n\n- **Headline result template**: \"On semi-synthetic CSS benchmarks, global correction worsens subgroup CATE bias by 2-3x (median), with amplification up to 5.9x for K=4 subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels. Combined with PPCI, the composition achieves near-zero bias (0.005) even when both covariate and outcome errors are present.\"\n\n- **Oracle framing**: When reporting DGP C results where ec_hte_ppci outperforms oracle, always use \"covariate-oracle\" (true Z + observed Y), never unqualified \"oracle\". Frame as \"composite correction is necessary and sufficient when both error types coexist\" — NOT \"beats oracle\". The result is by construction (ec_hte_ppci corrects both error types; covariate-oracle only corrects one), not surprising.\n\n## Key Contributions (ordered for paper)\n\n1. **Bias decomposition identity**: Exact population-level identity: bias ∝ misclassification heterogeneity × CATE heterogeneity (Δπ×Δτ product form). NOT a bound — it is an exact identity under A1–A4; finite-sample R² measures MC noise, not bound looseness. Includes \"debiasing can hurt\" proposition with constructive example. Frame as \"bias decomposition\" or \"bias identity\" throughout — never \"bias bound.\" (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **EC-HTE + PPCI composition — empirically necessary and sufficient**: EC-HTE and PPCI are empirically necessary and sufficient in composition: neither alone adequately handles dual-error scenarios (DGP C), but their composition reduces bias to near-zero (0.005, a 35× improvement over EC-HTE alone). EC-HTE exploits mixing matrix structure for covariate-side error; PPCI rectifier captures outcome-side error. PPCI alone can partially correct covariate error but with higher variance (limited by gold subset size). In Methods, retain full discussion of partial overlap; in Abstract, lead with \"necessary and sufficient in composition.\" (Method + Empirical)\n5. **Comprehensive validation**: Synthetic + semi-synthetic + real-data case study (pattern consistency, not ground-truth benchmark) with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI / DSL?\"** — PPCI rectifier is a general-purpose correction that captures any systematic error (covariate + outcome); EC-HTE is a structured correction exploiting mixing matrix structure specifically for covariate-side error. They are complementary: EC-HTE alone is more efficient for covariate error (uses M⁻¹ structure), PPCI alone can partially correct covariate error but with higher variance (limited by gold subset). In composition, EC-HTE handles structured covariate error, residual rectifier handles outcome error. DSL applied per-subgroup is a valid baseline but lacks cross-subgroup shrinkage, operates at estimand level rather than measurement model level, and has strictly higher variance under partial pooling. Do NOT say \"DSL cannot do subgroup correction\" — say it lacks the principled shrinkage mechanism.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — exp-006 provides precise RMSE crossover points: K=2/extreme n_expert=250, K=4/extreme n=1000, K=4/moderate n=2000, K=2/moderate never crosses (global always better on RMSE). Paper needs \"Expert Budget Recommendation\" subsection with per-K guidelines. Key message: when diagnostic criterion flags high heterogeneity (extreme regime), EC-HTE is worth the investment at moderate budgets; when heterogeneity is low, global correction is the safer choice. This honest framing connects Claim 2 (EC-HTE method) to Claim 3 (diagnostic criterion) — the diagnostic decides the correction strategy.\n\n6. **\"How does this differ from Carroll et al. (2006) / classical measurement error?\"** — The qualitative insight that misspecified corrections can amplify MSE is classical (Fuller 1987, Sec. 2.3). Our specific contributions beyond this are: (a) the quantitative Δπ×Δτ product form for CATE estimation with effect-modifier misclassification, (b) demonstrating this failure mode occurs *by default* in standard LLM annotation workflows, and (c) providing a computable diagnostic and correction framework. Must explicitly cite and contextualize: Fuller (1987), Carroll et al. (2006 Ch. 4), Gustafson (2003), Hu & Schennach (2008), Imai & Yamamoto (2010). Also cite Bayesian annotation models: Dawid & Skene, Passonneau & Carpenter (2014), Hovy et al. (2013). **Bibliography target: 30-35 references** spanning measurement error, Bayesian estimation, causal inference, LLM-as-annotator (Tornberg 2024, Gilardi et al. 2023, Ziems et al. 2024), HTE methods (Wager & Athey 2018, Kennedy 2023, Chernozhukov et al. 2018).\n\n7. **\"Methodological novelty is modest\"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. HB partial pooling provides meaningful RMSE reduction for moderate subgroups but is NOT \"never worse than global\" — it is a James-Stein shrinkage estimator with known boundary conditions. **Recommended condition**: n_expert per subgroup ≥ ~25 (e.g., n_expert ≥ 100 for K=4 with 12% minority). Below this, stratified MLE is preferred. This honest limitation strengthens credibility. State conditions explicitly using per-subgroup formulation, not just total n_expert.\n\n8. **\"Why no figures?\"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use cases (sentiment analysis, hate speech detection, refugee interview coding), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track. **NOTE**: Framing broadened from \"political-science\" to \"CSS\" (D004b) — TweetEval stance tasks too small (N<1000), sentiment (N=45K) usable but not political science. CSS is more accurate and equally strong for EMNLP.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n## Writing Requirements (Dream Round 2 consensus)\n\n1. **\"Bias decomposition\" NOT \"bias bound\"** — Theorem 1 is an exact identity at population level. R² < 1.0 in verification reflects finite-sample MC noise, not bound looseness.\n2. **Bibliography: 30-35 references minimum** — Must span 5 literatures: classical measurement error, Bayesian estimation, causal inference, LLM-as-annotator, CSS. Critical citations: Fuller 1987, Wager & Athey 2018, Imai & Yamamoto 2010.\n3. **3+ figures in main text** — (a) bias mechanism schematic, (b) Δπ×Δτ amplification heatmap, (c) diagnostic ROC curve, (d) budget crossover curves. Move exp-008/exp-009 tables to appendix.\n4. **Semi-synthetic DGP fully specified** — outcome generation, treatment assignment, CATE injection mechanism.\n5. **Real-data framed as pattern consistency** — NOT ground-truth benchmark. No bias/RMSE against unknown true CATEs.\n6. **EC-HTE advantage is conditional, not universal** — ec_hte dominates when misclassification heterogeneity is high (extreme regime) OR n_expert is large (≥500). In moderate regime with small n_expert (~100), global correction can outperform ec_hte because per-subgroup CM estimation noise exceeds the benefit of stratification. This connects to Claim 3: the diagnostic criterion (Δπ×Δτ) predicts when EC-HTE is needed. Unified condition: n_expert/K ≥ ~25-50 experts per subgroup.\n11. **RMSE tradeoff must be disclosed** — ec_hte has higher RMSE than global/naive in K=4/n≤100 configs (up to 3.5x in extreme cases) due to noisy per-subgroup CM estimation. Bias is lower but variance is higher. Must report both bias AND RMSE; include bias-RMSE tradeoff analysis. At n_expert≥500, ec_hte RMSE becomes competitive.\n12. **K-dependence of debiasing-hurts** — DIM estimator: K=2 extreme ~2.86×, K=4 extreme ~2.41× (does NOT monotonically increase with K). CausalForest: K=4 extreme up to 5.9× (nonlinear estimator amplifies with more subgroups). Report both patterns; do NOT claim \"more subgroups → always worse\" without qualifying the estimator.\n7. **Confusion matrix invertibility** — State det(Ĉ_k) ≠ 0 assumption explicitly.\n8. **Diagnostic AUC cross-validated** — Leave-one-setting-out or held-out evaluation, not in-sample.\n9. **Hyperprior values stated + sensitivity analysis** — Gamma(α, β) for Dirichlet concentration; report sensitivity to 2× changes.\n10. **PPCI complementarity elevated** — Highlight in abstract and contributions. Frame as \"complementary\" not \"orthogonal\": EC-HTE is structured covariate-error correction; PPCI rectifier is general residual correction. Composition = EC-HTE handles structured part + rectifier handles remainder (primarily outcome error).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2. MUST report full MCMC diagnostics: sampler (PyMC\n    NUTS), chains (≥4), warmup (≥1000), R̂ (<1.01), ESS (>200), runtime vs MLE. Report\n    SEs/CIs for all metrics from MC runs. Monitor coverage calibration — if systematic\n    undercoverage, diagnose cause.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example. MUST include K>2 extension: verify bias formula empirically for K=4 subgroups;\n    add Remark after Proposition 1 discussing general-K case (sum-of-products form).\n    Report R² of analytic prediction vs MC, bound tightness ratio, and CIs on all\n    bias estimates.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim: 1,2,3\n  description: 'Semi-synthetic benchmark: use real CSS tweet corpus — TweetEval sentiment\n    (N=45K, primary) for exp-003. Framing broadened from ''political-science'' to\n    ''CSS'' per D004b (stance tasks N<1000 unusable). Inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 (API) and optionally Qwen3-235B-A22B (GPU), measure\n    subgroup-specific misclassification rates, apply EC-HTE vs baselines. Subgroup\n    variables: text features (has_hashtag, text_length) for semi-synthetic; demographic\n    subgroups reserved for exp-004. MUST fully specify DGP in paper: (a) outcome generation\n    model, (b) treatment assignment mechanism, (c) how true CATEs are injected. MUST\n    run LLM annotation pilot (~1000 samples) before committing to verify per-subgroup\n    misclassification heterogeneity exists.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim: 1,2\n  description: 'Real-data case study (pattern consistency, NOT ground-truth validation):\n    apply EC-HTE to real CSS dataset with subgroup-varying LLM misclassification.\n    Show: (a) global vs EC-HTE produce qualitatively different CATE distributions,\n    (b) EC-HTE results consistent with domain knowledge (demographic effect direction),\n    (c) bootstrap CIs on point estimate differences. Frame as ''illustrative application''\n    not ''ground-truth benchmark''. Reviewer confirmed: real data has no ground truth\n    CATE, CV-based ground truth is circular. PRIMARY: UC Berkeley Measuring Hate Speech\n    corpus (public, rich demographic subgroups). NICE-TO-HAVE: Ashwin et al. (2025)\n    if obtainable (requires author email + IRB, not feasible within 5-day DDL).'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference) or API\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: UC Berkeley dataset causal framework (T,Y,Z,S) mapping needs design\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold. MUST use\n    cross-validation or held-out evaluation (NOT in-sample AUC on own experiments).\n    Dream Round 2 flagged in-sample AUC as methodological weakness across best and\n    median tiers.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1,2\n  description: 'PPCI + DSL baseline comparison: (a) PPCI kernel-based conditional\n    correction vs EC-HTE on covariate-side vs outcome-side error; (b) per-subgroup\n    DSL as additional baseline (DSL applied independently per subgroup, no cross-subgroup\n    shrinkage — shows EC-HTE''s partial pooling advantage); (c) EC-HTE+PPCI composition\n    for simultaneous covariate+outcome error; (d) CRITICAL: include ''pure covariate-error,\n    zero outcome-error'' control condition to demonstrate EC-HTE advantage when covariate-side\n    error dominates (PPCI should be ineffective here). Paper framing: DSL per-subgroup\n    is a valid baseline but lacks cross-subgroup shrinkage and operates at estimand\n    level rather than measurement model level.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest integration: apply EC-HTE post-hoc correction to CausalForestDML\n    subgroup CATE estimates + leaf-level corrected pseudo-outcomes with variance-adjusted\n    CIs. Compare against naive forest and globally-corrected forest. ELEVATED TO P0:\n    Claim 2 explicitly states CausalForestDML but no experiment validates this — claim-evidence\n    gap is reviewer killshot.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mcmc_rhat_max: 1.024\n    mcmc_ess_min: 129\n    mcmc_divergent: 0\n    runtime_min: 69\n    total_mc_runs: 3600\n    hb_vs_mle_rmse_improvement_k2_n50: 4-9%\n    hb_vs_mle_rmse_improvement_k2_n100: 1-2%\n    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%\n    hb_coverage_min: 0.87\n    hb_coverage_median: 0.93\n    k4_extreme_n50_blowup: false\n    k4_extreme_n50_blowup_note: Fixed by singularity guard + 4-chain MCMC\n    mcmc_fix_4chain:\n      rhat_max_all_configs: 1.0034\n      ess_min_all_configs: 1618\n      ess_improvement: ~4x vs 2-chain\n      k4_extreme_n50_A_rmse_z0: 3.14 → 0.99\n      k4_extreme_n50_B_rmse_z0: 509.93 → 0.27\n      k4_extreme_n100_A_rmse_z0: 11.57 → 0.29\n      singularity_guard_triggers: extreme/n=50 only (2 HB, 3 MLE / 100 runs)\n      results_file: results/exp001_hb_results_v2.csv\n    hyperprior_sensitivity:\n      scale_range: 0.5-2.0\n      k2_rmse_variation: <1%\n      k4_rmse_variation: ~4-5%\n      coverage_invariant: true\n      conclusion: robust\n      results_file: results/exp001_hyperprior_sensitivity.csv\n- exp_id: exp-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r2_k2: 0.9939\n    r2_k4: 0.9738\n    tightness_ratio_k2_median: 1.0027\n    tightness_ratio_k4_median: 1.0234\n    debiasing_hurts_pct: 50\n    debiasing_hurts_pct_note: 260/520 (excluding dc=0 rows where bias=0)\n    debiasing_hurts_threshold_delta_misclass: 0.1235\n    max_bias_ratio_k2: 2.86\n    max_bias_ratio_k4: 2.41\n    coverage_2se_k2: 0.951\n    coverage_2se_k4: 0.94\n- exp_id: exp-007\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_rows: 6912\n    dgps:\n    - A_covariate_only\n    - B_outcome_only\n    - C_both_errors\n    - D_no_error\n    methods: 8\n    mc_runs: 100\n    double_correction_fix_verified: true\n    dgp_a_ec_hte_ppci_equals_ec_hte: true\n    dgp_c_extreme_n250_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.225\n      ec_hte_bias_z0: 0.178\n      ec_hte_rmse_z0: 0.226\n      ppci_bias_z0: 0.004\n      ppci_rmse_z0: 0.261\n      naive_bias_z0: 0.251\n      naive_rmse_z0: 0.269\n    dgp_c_n500_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.142\n      ec_hte_bias_z0: 0.088\n      ec_hte_rmse_z0: 0.134\n    key_finding: ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better\n      than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.\n- exp_id: exp-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase: A_semi_synthetic\n    n_subgroups: 4\n    misclass_rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25\n    subgroup_sizes: S0~38%, S1~38%, S2~12%, S3~12%\n    p_z1_actual: 0.39\n    debiasing_hurts_confirmed: true\n    mc_runs: 100\n    v3_hb_integration_100mc:\n      methods:\n      - oracle\n      - naive\n      - global_corrected\n      - stratified_mle\n      - hb_ec_hte\n      hb_vs_mle_summary:\n        n50_S3_extreme: -57% RMSE (HB worse, but not catastrophic)\n        n50_S3_moderate: -54% RMSE z1 (HB worse)\n        n100_S3_extreme: +60% RMSE z1 (HB dramatically better)\n        n100_S3_moderate: +24% RMSE z1 (HB better)\n        n100_S2: +5-8% RMSE (HB better)\n        n250_S3: +5-17% RMSE (HB better)\n        n500_all: +0.2-1.6% (converged)\n      key_finding: '100 MC confirms: S3 blowup at n=50 is real but moderate (not catastrophic\n        as dry-run suggested). At n>=100, HB is better everywhere, especially S3 (+26-60%).\n        Partial pooling sweet spot is n=100-250.'\n      hypothesis_verdict: validated_with_boundary\n      boundary_condition: n_expert>=100 recommended; n=50 with extreme heterogeneity\n        in tiny subgroups shows moderate degradation\n    results_file_v3: results/exp003_phase_a_v3.csv\n    results_file_v3_raw: results/exp003_phase_a_v3_raw.csv\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subgroup_level_auc: 0.833\n    subgroup_correlation: 0.86\n    setting_level_auc: 0.49\n    low_pi_hurt_pct: 84.6\n    high_pi_hurt_pct: 15.4\n    theory_alignment: consistent with exp-002 formula\n- exp_id: exp-011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    n_configs: 8\n    total_rows: 144\n    runtime_min: 35\n    methods:\n    - naive_forest\n    - global_forest\n    - ec_hte_forest\n    mean_abs_bias:\n      naive_forest: 0.1558\n      global_forest: 0.1073\n      ec_hte_forest: 0.0608\n    mean_rmse:\n      naive_forest: 0.1782\n      global_forest: 0.1659\n      ec_hte_forest: 0.2289\n    debiasing_hurts_cases: 9\n    debiasing_hurts_max_ratio: 5.9\n    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'\n    k2_n500_ec_hte_bias_range: 0.004-0.013 (near zero)\n    k2_n500_global_bias_range: 0.033-0.109 (still biased)\n    pattern_consistent_with_diff_in_means: true\n    claim2_validated: true\n- exp_id: exp-006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    total_rows: 288\n    runtime_min: 110\n    grid: n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]\n    crossover_hb_beats_global:\n      K2_extreme: 250\n      K2_moderate: never\n      K4_extreme: 1000\n      K4_moderate: 2000\n    hb_vs_mle: HB ≥ MLE in 21/24 configs (87.5%; partial pooling rarely hurts in symmetric\n      DGP)\n    hb_best_improvement_over_mle:\n      K4_moderate_n50_sgC: +42.4% RMSE\n      K4_extreme_n50_sgC: +23.4% RMSE\n      K4_moderate_n50_sgB: +24.0% RMSE\n    convergence: HB ≈ MLE at n≥1000 (<0.5% difference)\n    key_finding: 'Crossover depends strongly on K and regime. K=2: crossover at n=250\n      (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest\n      improvement over MLE via partial pooling.'\n- exp_id: exp-007b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    kill_reason: 'D012: Director 决定放弃 HB backfill。理由：PPCI 表核心 story 是互补性，HB vs MLE\n      是边际改进；exp-001 已验证 HB。CSV 已重命名为 .broken'\n- exp_id: exp-012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: gpt-4.1-2025-04-14\n    n_samples: 500\n    valid_annotations: 500\n    failed: 0\n    accuracy_3class: 0.672\n    accuracy_binary: 0.858\n    subgroup_misclass_rates:\n      hash_long: 0\n      hash_medium: 0.2\n      hash_short: 0.174\n      nohash_long: 0\n      nohash_medium: 0.102\n      nohash_short: 0.138\n    delta_pi: 0.2\n    heterogeneity_significant: true\n    key_finding: Hashtag presence increases binary misclassification rate (~0.17-0.20\n      vs ~0.10-0.14 for non-hashtag). Delta-pi=0.200 confirms meaningful heterogeneity\n      for EC-HTE correction.\n    analysis_file: results/pilot_gpt41_analysis.md\n- exp_id: exp-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    config: K=4/extreme/n_expert=50\n    n_expert_per_K: 12.5\n    hb_method: EB (Empirical Bayes, not Gibbs — conservative estimate for boundary\n      condition)\n    avg_rmse_naive: 0.109\n    avg_rmse_global: 0.14\n    avg_rmse_mle: 0.28\n    avg_rmse_eb: 0.292\n    worst_subgroup: A(pi=0.30) EB RMSE=0.62\n    amplification_max: 4.4x (A/EB vs global)\n    threshold_confirmed: n_expert/K=12.5 < 25\n    naive_beats_all: true\n    debiasing_hurts_D: Naive bias=0.001, Global bias=0.110 — extreme over-correction\n      in lowest-error subgroup\n- exp_id: exp-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    configs: 3\n    asymmetric_configs:\n    - balanced(FPR=0.15,FNR=0.25)\n    - fpr_dominant(FPR=0.30,FNR=0.10)\n    - fnr_dominant(FPR=0.10,FNR=0.30)\n    delta_tau_grid:\n    - 0\n    - 0.1\n    - 0.2\n    - 0.3\n    - 0.5\n    n_mc: 100\n    N: 5000\n    n_expert: 250\n    r2_analytic_vs_mc: 0.992\n    product_structure_cv: ~1e-16 (exact)\n    product_structure_confirmed: true\n    a2_not_required: true\n    ec_hte_avg_abs_bias: 0.006\n    ec_hte_avg_rmse: 0.033\n    ec_hte_avg_coverage: 0.9\n    global_avg_abs_bias: 0.025\n    global_avg_rmse: 0.04\n    global_avg_coverage: 0.78\n    naive_avg_abs_bias: 0.025\n    naive_avg_rmse: 0.039\n    naive_avg_coverage: 0.87\n    bias_reduction_vs_global: 4.2x\n    coverage_improvement_vs_global: +12pp\n    latex_derivation_included: true\n    key_finding: Product structure bias = Δτ·[B_s]_{z,1} holds exactly under asymmetric\n      misclassification. A2 (symmetric) assumption is NOT required. EC-HTE dominates\n      with 4.2x bias reduction.\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dataset: UC Berkeley Measuring Hate Speech\n    n_comments: 2496\n    valid_annotations: 2496\n    subgroups:\n      plat0_long: 624\n      plat0_short: 624\n      plat23_long: 624\n      plat23_short: 624\n    subgroup_type: text features (platform_group × text_length)\n    delta_pi: 0.117\n    global_FPR: 0.139\n    global_FNR: 0.533\n    misclass_rates:\n      plat0_long: 0.266\n      plat0_short: 0.337\n      plat23_long: 0.303\n      plat23_short: 0.383\n    avg_abs_bias:\n      naive: 0.21\n      global: 0.273\n      ec_hte: 0.313\n    cate_comparison: EC-HTE does not outperform global on avg |bias| — high FNR (~53%)\n      and wide CIs limit correction effectiveness on this dataset\n    key_finding: Δπ=0.117 confirms real-world misclassification heterogeneity across\n      text-feature subgroups. High global FNR (53%) indicates LLM severely under-classifies\n      dehumanization. CATE correction comparison inconclusive due to wide bootstrap\n      CIs.\n- exp_id: exp-008\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    models_completed:\n    - gpt-3.5-turbo\n    - gpt-4.1\n    - gpt-4o\n    - gpt-4o-mini\n    - gpt-4-turbo\n    - gpt-5.4\n    total_models: 6\n    proxy_provider: OpenAI only\n    gpt5x_model_used: gpt-5.4\n    gpt55_failed: reasoning tokens consume max_tokens budget, too slow (~1min/call)\n    filtered_analysis:\n      excluded_subgroups:\n      - False_long (n=6)\n      - True_long (n=4)\n      min_n_threshold: 10\n      retained_subgroups:\n      - False_medium (n=187)\n      - False_short (n=109)\n      - True_medium (n=125)\n      - True_short (n=69)\n    effective_delta_pi:\n      gpt-3.5-turbo: 0.198\n      gpt-4-turbo: 0.149\n      gpt-4.1: 0.098\n      gpt-4o: 0.08\n      gpt-4o-mini: 0.136\n      gpt-5.4: 0.114\n    all_effective_delta_pi_above_005: true\n    worst_subgroup_consensus: True_medium (5/6 models)\n    spearman_significant_pairs:\n    - gpt-4-turbo vs gpt-4o (ρ=1.000)\n    - gpt-4.1 vs gpt-4o-mini (ρ=1.000)\n    - gpt-4.1 vs gpt-5.4 (ρ=1.000)\n    - gpt-4o-mini vs gpt-5.4 (ρ=1.000)\n    spearman_note: Only 4 subgroups after filtering, limited statistical power (most\n      p>0.20)\n    key_finding: All 6 models (GPT-3.5 through GPT-5.4, three generations) show effective\n      Δπ > 0.05 after excluding n<10 subgroups. Heterogeneity is structural, not model-specific.\n- exp_id: exp-010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    configs: 2\n    noise_levels:\n    - 0\n    - 0.1\n    - 0.25\n    - 0.5\n    total_runs: 800\n    runtime_sec: 15\n    k2_coverage_naive:\n    - 0.875\n    - 0.877\n    - 0.89\n    - 0.897\n    k2_coverage_hb:\n    - 0.958\n    - 0.948\n    - 0.95\n    - 0.945\n    k2_coverage_global:\n    - 0.925\n    - 0.935\n    - 0.932\n    - 0.945\n    k4_coverage_naive:\n    - 0.904\n    - 0.916\n    - 0.909\n    - 0.919\n    k4_coverage_hb:\n    - 0.956\n    - 0.958\n    - 0.96\n    - 0.946\n    k4_coverage_global:\n    - 0.93\n    - 0.953\n    - 0.948\n    - 0.944\n    hb_beats_mle_all_configs: true\n    hb_improvement_range: +0.1% to +0.9% RMSE\n    graceful_convergence_at_50pct: true\n    key_finding: 'Coverage is the decisive metric: naive 87-92%, EC-HTE 95-96% across\n      all noise levels. No catastrophic failure. HB shrinkage provides automatic safeguard\n      — converges to global at 50% noise.'\n- exp_id: exp-015\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_mc: 100\n    n_expert_grid:\n    - 100\n    - 250\n    - 500\n    subgroups: 4\n    real_cm_source: exp-012 GPT-4.1 pilot\n    cm_params:\n      S0_False_medium:\n        FPR: 0.054\n        FNR: 0.526\n        weight: 0.38\n      S1_False_short:\n        FPR: 0.101\n        FNR: 0.3\n        weight: 0.22\n      S2_True_short:\n        FPR: 0.143\n        FNR: 0.308\n        weight: 0.14\n      S3_True_medium:\n        FPR: 0.194\n        FNR: 0.222\n        weight: 0.25\n    delta_pi: 0.098\n    P_Z1: 0.18\n    rmse_n100:\n      naive: 0.123\n      global: 0.263\n      hb: 0.784\n    rmse_n250:\n      naive: 0.123\n      global: 0.232\n      hb: 0.411\n    rmse_n500:\n      naive: 0.123\n      global: 0.196\n      hb: 0.26\n    coverage_n100:\n      naive: 0.868\n      global: 0.922\n      hb: 0.744\n    coverage_n250:\n      naive: 0.868\n      global: 0.908\n      hb: 0.828\n    coverage_n500:\n      naive: 0.873\n      global: 0.885\n      hb: 0.89\n    hb_worse_than_global_all_n: true\n    root_cause: S0 FNR=0.526 makes CM row near-uniform [0.526, 0.474], inversion amplifies\n      noise. Combined with P(Z=1)=0.18, too few Z=1 expert labels per subgroup for\n      reliable per-subgroup CM estimation.\n    key_finding: EC-HTE fails under realistic asymmetric CMs when any subgroup has\n      FNR≈0.5 (near-random for positive class). This is consistent with exp-004 (FNR=53%)\n      and exp-013 (boundary at n_expert/K=12.5). Identifies classifier quality threshold\n      as honest limitation.\n- exp_id: exp-016\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    model_selected: gpt-3.5-turbo\n    worst_subgroup_fnr: 0.211\n    worst_subgroup_fpr: 0.393\n    rmse_n100:\n      naive: 0.127\n      global: 0.265\n      hb: 0.93\n    rmse_n250:\n      naive: 0.127\n      global: 0.221\n      hb: 0.527\n    rmse_n500:\n      naive: 0.127\n      global: 0.199\n      hb: 0.322\n    coverage_n100:\n      naive: 0.784\n      global: 0.893\n      hb: 0.769\n    coverage_n250:\n      naive: 0.784\n      global: 0.922\n      hb: 0.843\n    coverage_n500:\n      naive: 0.784\n      global: 0.939\n      hb: 0.894\n    hb_worse_than_global_all_n: true\n    vs_exp015: exp-016 HB RMSE even worse than exp-015 despite lower FNR, because\n      high FPR variance (0.14-0.39) makes subgroup CM estimation harder\n    bright_spot: 'S0/z=1 at n=500: HB |bias|=0.193 < Global |bias|=0.252 — one case\n      where subgroup-specific correction helps'\n    root_cause: High FPR variance across subgroups (0.143-0.393) + P(Z=1)=0.18 → insufficient\n      Z=1 expert labels per subgroup. Lower FNR alone does not fix the fundamental\n      sample-size constraint.\n    key_finding: Neither low-FNR (gpt-3.5-turbo) nor low-FPR (GPT-4.1) real CMs enable\n      EC-HTE to beat global. The bottleneck is P(Z=1)=0.18 creating too few positive-class\n      expert labels per subgroup for reliable CM estimation.\n- exp_id: exp-017\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 50\n    config: K=2/extreme/n_expert=500\n    rlearner_results:\n      naive:\n        avg_abs_bias: 0.121\n        rmse: 0.139\n        coverage: 0.47\n      global:\n        avg_abs_bias: 0.098\n        rmse: 0.123\n        coverage: 0.71\n      ec_hte:\n        avg_abs_bias: 0.013\n        rmse: 0.08\n        coverage: 0.92\n      oracle:\n        avg_abs_bias: 0.006\n        rmse: 0.056\n        coverage: 0.94\n    causal_forest_comparison:\n      naive:\n        avg_abs_bias: 0.125\n        rmse: 0.143\n        coverage: 0.46\n      global:\n        avg_abs_bias: 0.104\n        rmse: 0.129\n        coverage: 0.65\n      ec_hte:\n        avg_abs_bias: 0.008\n        rmse: 0.082\n        coverage: 0.91\n    ec_hte_bias_reduction_vs_naive: 9.3x (R-learner) vs 15.6x (CausalForest)\n    pattern_consistent: true\n    key_finding: EC-HTE correction generalizes across CATE estimators. R-learner ec_hte\n      achieves |bias|=0.013 (vs naive 0.121), 92% coverage — closely matching CausalForest\n      pattern.\n- exp_id: exp-018\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 50\n    config: K=2/extreme/n_expert=500/multiplicative\n    dgp: Y(1) = Y(0) * exp(tau(Z)), tau(Z=0)=0, tau(Z=1)=0.3\n    results:\n      oracle:\n        avg_abs_bias: 0.031\n        rmse: 0.038\n        coverage: 0.96\n      ec_hte:\n        avg_abs_bias: 0.054\n        rmse: 0.068\n        coverage: 0.955\n      global_corrected:\n        avg_abs_bias: 0.11\n        rmse: 0.124\n        coverage: 0.54\n      naive:\n        avg_abs_bias: 0.135\n        rmse: 0.142\n        coverage: 0.435\n    ec_hte_rmse_reduction_vs_naive: 52%\n    ec_hte_coverage: 0.955\n    vs_exp001_additive: EC-HTE RMSE 0.068 (multiplicative) vs 0.091 (additive, same\n      config) — actually better due to larger true CATEs making relative bias smaller\n    key_finding: EC-HTE robust to non-additive treatment effects. 52% RMSE reduction\n      vs naive, 95.5% coverage (target 95%). Answers Reviewer Q3.\n- exp_id: exp-019\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theorem1_r2:\n      K2:\n        pz0.1: 0.998\n        pz0.2: 0.989\n        pz0.3: 0.994\n        pz0.4: 0.995\n        pz0.5: 0.995\n      K4:\n        pz0.1: 0.984\n        pz0.2: 0.976\n        pz0.3: 0.985\n        pz0.4: 0.984\n        pz0.5: 0.992\n    theorem1_r2_range: 0.976-0.998 (all >0.95)\n    rmse_ratio_hb_over_global:\n      K2:\n        pz0.1: 0.92\n        pz0.2: 0.763\n        pz0.3: 0.78\n        pz0.4: 0.874\n        pz0.5: 0.857\n      K4:\n        pz0.1: 1.542\n        pz0.2: 1.684\n        pz0.3: 1.121\n        pz0.4: 1.082\n        pz0.5: 1.063\n    hb_wins_K2: all 5 P(Z=1) values (ratio 0.76-0.92)\n    hb_wins_K4: none (ratio 1.06-1.68)\n    coverage_hb: 0.92-0.94 across all settings (near-nominal 0.95)\n    coverage_naive: 0.65-0.79\n    coverage_global: 0.79-0.90\n    key_finding: 'Theorem 1 R²>0.976 universally — bias decomposition holds regardless\n      of P(Z=1). EC-HTE RMSE advantage depends on K: K=2 HB wins everywhere, K=4 HB\n      loses at n_expert=250 (insufficient per-subgroup minority data). Coverage: HB\n      0.92-0.94 near-nominal at all settings.'\n- exp_id: exp-020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    max_cond_number: 1.89\n    mean_cond_number: 1.446\n    p99_cond_number: 1.893\n    guard_trigger_rate_all_kappa: 0\n    rmse_hb: 0.0759\n    rmse_global: 0.0765\n    rmse_ratio: 1.048\n    numerical_instability_rate: 0\n    safety_margin_at_kappa100: 53x\n    stress_test_near_random_max_cond: 1125.3\n    stress_test_near_random_triggers_kappa100: true\n- exp_id: exp-021\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_cells_compared: 94\n    median_delta_pct: 3.2\n    max_delta_pct: 25.5\n    cells_under_5pct: 79/94 (84%)\n    cells_under_10pct: 93/94 (99%)\n    outlier: K=4/extreme/n=100/HB base (-25.5%, known numerically unstable)\n    method_note: EB instead of Gibbs (<0.002 CM difference, 10s vs 114min)\n- exp_id: exp-022\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rmse_range_reasonable: 6.0%\n    rmse_range_all: 17.3%\n    gamma31_rmse: 0.0841\n    gamma31_rank: 8/15\n    coverage_range: 0.925-0.938\n    hb_beats_mle: 9/15\n    best_config: Gamma(1,0.5)\n    best_rmse: 0.0825\n- exp_id: exp-023\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dgp: heterogeneous-tau\n    N: 5000\n    P_Z1: 0.652\n    K: 4\n    subgroups:\n    - False_medium\n    - False_short\n    - True_medium\n    - True_short\n    delta_tau:\n      False_medium: 0.1\n      False_short: 0.1\n      True_medium: 0.3\n      True_short: 0.6\n    n_expert_sweep:\n    - 200\n    - 500\n    - 1000\n    mc_seeds: 50\n    hb_method: MAP-EB Gamma(3,1)\n    bias_echte_wins: 3/3 budgets\n    bias_reduction_n500: 68% vs Global (0.0099 vs 0.0314)\n    bias_reduction_n200: 32% vs Global (0.0248 vs 0.0365)\n    bias_reduction_n1000: 55% vs Global (0.0130 vs 0.0286)\n    rmse_echte_wins: 0/3 aggregate\n    rmse_true_short_n1000:\n      global: 0.1693\n      echte: 0.1637\n      improvement: -3.3%\n    rmse_true_short_z0_n1000:\n      global: 0.2577\n      echte: 0.2117\n      improvement: -17.8%\n    key_finding: EC-HTE wins bias at all budgets. High-Δτ subgroup (True_short) RMSE\n      wins at n≥500. Aggregate RMSE loss driven by low-Δτ subgroups where stratified\n      variance cost exceeds small bias gain.\n- exp_id: exp-024\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R2_overall: 0.975\n    data_sources:\n    - exp023_confusion_matrices.json\n    - c1_multi_llm/*_cm_profile.md\n    n_llm_dataset_combos: 11\n    output_files:\n    - results/exp_realcm_bias_identity.csv\n    - results/exp_realcm_summary.csv\n- exp_id: exp-025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    screening: 0/16 combos pass all conditions (κ≤1.25 bottleneck)\n    oracle_screening: HB wins 41/52 comparisons on aggregate RMSE\n    hb_vs_mle: HB beats Strat MLE in 52/52 comparisons\n    best_case: 'Qwen2.5-7B K=4 n=500 Z=0: ΔRMSE=-0.0075'\n    open_source_llms: All 4 (Llama/Qwen/Mistral/Gemma) HB wins 32/32 on TweetEval\n    hb_loses: gpt-3.5-turbo/TweetEval (high FPR asymmetry), gpt-4o/CivilComments (low\n      P(Z=1)=0.3)\n    output_files:\n    - results/exp_screening.csv\n    - results/exp_oracle_screening.csv\n    - results/exp_positive_scenario_summary.md\n- exp_id: exp-026\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K2_n25:\n      mle_rmse: 0.2562\n      hb_rmse: 0.2689\n      delta_pct: +4.9%\n      global_rmse: 0.1013\n    K2_n50:\n      mle_rmse: 0.2748\n      hb_rmse: 0.2306\n      delta_pct: -16.1%\n      global_rmse: 0.0879\n    K2_n75:\n      mle_rmse: 0.0911\n      hb_rmse: 0.0893\n      delta_pct: -1.9%\n    K4_n25:\n      mle_rmse: 0.4011\n      hb_rmse: 0.6116\n      delta_pct: +52.5%\n      global_rmse: 0.1289\n    K4_n50:\n      mle_rmse: 0.3798\n      hb_rmse: 0.4701\n      delta_pct: +23.8%\n      global_rmse: 0.1172\n    K4_n75:\n      mle_rmse: 0.2208\n      hb_rmse: 0.2111\n      delta_pct: -4.4%\n    K4_n100:\n      mle_rmse: 0.2152\n      hb_rmse: 0.2123\n      delta_pct: -1.3%\n    coverage_all: '>=0.88, no catastrophic failures'\n    crossover_K2: n_expert=50 (HB -16.1%)\n    crossover_K4: n_expert=75 (HB -4.4%)\n    key_finding: HB shrinkage advantage emerges at n≥50 (K=2) and n≥75 (K=4). Below\n      these thresholds, global pooling outperforms both HB and MLE — validates budget\n      threshold claim.\n    mc_runs: 100\n    output_file: results/exp_low_budget_hb.csv\n- exp_id: exp-027\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    oracle_true_Z:\n      coverage: 0.945\n      bias: 0.0056\n      rmse: 0.078\n    echte_true_CM:\n      coverage: 0.925\n      bias: 0.0078\n      rmse: 0.114\n    echte_estimated_CM:\n      coverage: 0.931\n      bias: 0.0148\n      rmse: 0.121\n    global_true_CM:\n      coverage: 0.913\n      bias: 0.0371\n      rmse: 0.11\n    global_estimated_CM:\n      coverage: 0.911\n      bias: 0.0379\n      rmse: 0.111\n    naive:\n      coverage: 0.883\n      bias: 0.0447\n      rmse: 0.095\n    key_finding: 'Oracle CF SE well-calibrated (94.5%). EC-HTE true CM (92.5%) ≈ estimated\n      CM (93.1%): CM estimation NOT the coverage gap source. ~2pp drop from Oracle\n      to EC-HTE true CM comes from M^{-1} SE propagation, not CM estimation noise.'\n    dgp: K=4 extreme, N=5000, n_expert=500, 100 MC runs\n    output_file: results/exp_cf_oracle_coverage.csv\n- exp_id: exp-027b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    dgp: K=2 extreme, π=[0.05,0.25], N=5000, n_expert=250, 100 MC runs\n    oracle_true_Z:\n      coverage: 0.94\n      bias: 0.0023\n      rmse: 0.056\n    echte_true_CM:\n      coverage: 0.94\n      bias: 0.0027\n      rmse: 0.073\n    echte_estimated_CM:\n      coverage: 0.925\n      bias: 0.0044\n      rmse: 0.079\n    global_true_CM:\n      coverage: 0.885\n      bias: 0.045\n      rmse: 0.083\n    global_estimated_CM:\n      coverage: 0.883\n      bias: 0.045\n      rmse: 0.085\n    naive:\n      coverage: 0.828\n      bias: 0.046\n      rmse: 0.077\n    key_finding: 'K=2: Oracle 94%, EC-HTE true CM 94%, EC-HTE estimated CM 92.5%.\n      CF SE is well-calibrated. 83-85% coverage in paper comes from Naive (uncorrected\n      misclassification bias), NOT from CF SE under-calibration. EC-HTE restores near-nominal\n      coverage.'\n    output_file: results/exp_cf_oracle_coverage_k2.csv\n- exp_id: exp-027c\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dgp: 'MF2 exact DGP: K=2, π=[0.05,0.25], τ(0)=0.10, τ(1)=0.40, N=5000, n_expert=250,\n      100 MC'\n    oracle_true_Z:\n      coverage: 0.96\n      bias: 0.077\n      rmse: 0.091\n      mean_se: 0.09\n    echte_true_CM:\n      coverage: 0.913\n      bias: 0.103\n      rmse: 0.112\n      mean_se: 0.114\n    echte_estimated_CM:\n      coverage: 0.923\n      bias: 0.1\n      rmse: 0.111\n      mean_se: 0.119\n    global_true_CM:\n      coverage: 0.95\n      bias: 0.107\n      rmse: 0.114\n      mean_se: 0.107\n    global_estimated_CM:\n      coverage: 0.943\n      bias: 0.105\n      rmse: 0.114\n      mean_se: 0.109\n    naive:\n      coverage: 0.773\n      bias: 0.12\n      rmse: 0.125\n      mean_se: 0.087\n    key_finding: 'DGP difference NOT the source of 83% vs 92.5% gap. Per-subgroup\n      EC-HTE coverage ~92.25% in both 027b and 027c. The 83% in MF2 is an aggregate\n      mixing effect: low-misclass subgroup (π=0.05) has 83% coverage while high-misclass\n      subgroup (π=0.25) has 99%. M⁻¹ creates asymmetric SE amplification across subgroups.'\n    comparison_027b:\n      oracle: 94.0% → 96.0%\n      echte_est: 92.5% → 92.25%\n      conclusion: Nearly identical per-subgroup coverage despite different τ values\n    output_file: results/exp_cf_oracle_coverage_mf2dgp.csv\n- exp_id: exp-028\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_symmetric_auc: 0.626\n    overall_asymmetric_auc: 0.611\n    k4_only:\n      symmetric_auc_range: 0.0-1.0\n      asymmetric_auc_range: 0.0-1.0\n      perfect_auc_combos:\n      - Llama/TweetEval\n      - Qwen/TweetEval\n      - Mistral/TweetEval\n      - gpt-4o/TweetEval\n      - gpt-3.5-turbo/TweetEval(asym only)\n      - gpt-4.1/TweetEval(asym only)\n    k2_all_auc_zero: true\n    z0_z1_identical: true\n    theoretical_insight: For DIM, |B_s[0,1]|=|B_s[1,1]| (column-stochastic M). Asymmetric\n      diagnostic degenerates to symmetric because DIM CATE bias depends on δ_s = (FPR_s+FNR_s)/2\n      - π̄, not on FPR/FNR individually.\n    output_files:\n    - results/exp_asymmetric_diagnostic_auc.csv\n    - results/exp_asymmetric_diagnostic_auc_summary.csv\n- exp_id: exp-029\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dgp: K=2, pi=[0.05,0.25], tau(0)=0, tau(1)=0.3, N=5000, n_expert=250, 100 MC\n    gamma_sweep:\n    - 0\n    - 0.05\n    - 0.1\n    - 0.15\n    - 0.2\n    echte_coverage:\n      g0.00: 0.955\n      g0.05: 0.955\n      g0.10: 0.953\n      g0.15: 0.948\n      g0.20: 0.935\n    echte_abs_bias:\n      g0.00: 0.0596\n      g0.05: 0.0593\n      g0.10: 0.063\n      g0.15: 0.0652\n      g0.20: 0.0677\n    global_coverage:\n      g0.00: 0.927\n      g0.05: 0.935\n      g0.10: 0.938\n      g0.15: 0.943\n      g0.20: 0.94\n    naive_coverage:\n      g0.00: 0.877\n      g0.05: 0.838\n      g0.10: 0.835\n      g0.15: 0.792\n      g0.20: 0.795\n    key_finding: 'EC-HTE coverage degrades gracefully: 95.5%→93.5% over gamma 0→0.2\n      (−2.0pp). ALL correction methods maintain ≥90% coverage across all gamma. Naive\n      degrades fastest (87.7%→79.5%, −8.2pp). At moderate violation gamma=0.1, EC-HTE\n      coverage=95.3% (−0.2pp from baseline). EC-HTE |bias| increases 13.7% at gamma=0.2\n      but remains comparable to Global.'\n    coverage_below_90_threshold:\n      Naive: 0\n      Global: never\n      Strat_MLE: never\n      HB_ECHTE: never\n    output_files:\n    - results/exp_a1_sensitivity.csv\n    - results/exp_a1_sensitivity_summary.csv\n    - results/exp_a1_sensitivity_subgroup.csv\n- exp_id: exp-030\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hb_echte_coverage: 0.956\n    hb_echte_rmse: 0.34\n    hb_echte_mean_abs_bias: 0.183\n    oracle_coverage: 0.944\n    oracle_rmse: 0.113\n    oracle_mean_abs_bias: 0.09\n    global_coverage: 0.951\n    global_rmse: 0.168\n    global_mean_abs_bias: 0.135\n    strat_mle_coverage: 0.953\n    strat_mle_rmse: 0.638\n    strat_mle_mean_abs_bias: 0.219\n    naive_coverage: 0.913\n    naive_rmse: 0.133\n    naive_mean_abs_bias: 0.107\n    hb_vs_mle_rmse_improvement_pct: 47\n    per_subgroup_expert_labels: 31\n    source: results/exp_k8_subgroups_summary.csv\n    note: All CM-aware methods coverage ≥95%. HB RMSE 47% better than MLE but worse\n      than Global. K=8 is boundary condition.\n- exp_id: exp-031\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hb_echte_coverage: 0.95\n    hb_echte_rmse: 0.086\n    hb_echte_mean_abs_bias: 0.068\n    oracle_coverage: 0.943\n    oracle_rmse: 0.061\n    oracle_mean_abs_bias: 0.048\n    global_coverage: 0.93\n    global_rmse: 0.087\n    global_mean_abs_bias: 0.071\n    strat_mle_coverage: 0.95\n    strat_mle_rmse: 0.087\n    strat_mle_mean_abs_bias: 0.069\n    naive_coverage: 0.863\n    naive_rmse: 0.083\n    naive_mean_abs_bias: 0.066\n    beta_confound: 0.5\n    propensity_range: 0.38-0.62\n    source: results/exp_confounded_dgp_summary.csv\n    note: EC-HTE + IPW-DIM coverage 95.0% under moderate confounding. Global 93.0%.\n      Naive 86.3%.\n- exp_id: exp-032\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    min_hb_coverage: 0.945\n    max_oracle_vs_est_gap: 0.01\n    hb_cov_b0.25_oracle: 0.9625\n    hb_cov_b0.25_estimated: 0.9725\n    hb_cov_b0.5_oracle: 0.95\n    hb_cov_b0.5_estimated: 0.9575\n    hb_cov_b1.0_oracle: 0.9575\n    hb_cov_b1.0_estimated: 0.96\n    hb_cov_b2.0_oracle: 0.945\n    hb_cov_b2.0_estimated: 0.9475\n    hb_rmse_b2.0_oracle: 0.1258\n    naive_cov_range: 0.845-0.898\n    source: results/exp_confounded_sweep_summary.csv\n    note: All 8 configs HB coverage >=94.5%. Oracle vs estimated gap <=1pp. Hypothesis\n      fully confirmed.\n- exp_id: exp-033\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hb_baseline_rmse: 0.333\n    hb_baseline_coverage: 0.959\n    v1_adaptive_alpha_rmse: 0.216\n    v1_adaptive_alpha_coverage: 0.96\n    v2_kappa_fallback_rmse: 0.25\n    v2_kappa_fallback_coverage: 0.96\n    v3_combined_rmse: 0.216\n    v3_combined_coverage: 0.96\n    global_rmse: 0.166\n    global_coverage: 0.958\n    v1_vs_baseline_improvement_pct: 35\n    v1_still_exceeds_global_pct: 30\n    source: results/exp_k8_adaptive_summary.csv\n    note: V1 (adaptive alpha) reduces RMSE 35% (0.333->0.216) but still exceeds Global\n      (0.166). Gap narrowed from 2x to 1.3x. Confirms boundary is real but mitigable.\n- exp_id: exp-034\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    source: results/exp_fl_comparison_summary.csv\n    fl_scalar_abs_bias: 0.0909\n    fl_scalar_rmse: 0.1161\n    fl_scalar_coverage: 0.85\n    fl_per_subgroup_abs_bias: 0.112\n    fl_per_subgroup_rmse: 0.1582\n    fl_per_subgroup_coverage: 0.838\n    echte_abs_bias: 0.0643\n    echte_rmse: 0.0858\n    echte_coverage: 0.953\n    global_cm_abs_bias: 0.0643\n    global_cm_rmse: 0.0806\n    global_cm_coverage: 0.938\n    naive_abs_bias: 0.0621\n    naive_coverage: 0.858\n    oracle_abs_bias: 0.0454\n    oracle_coverage: 0.943\n    sign_reversal: 'F-L Scalar: s0=+0.073 s1=+0.068, both positive (no sign-reversal).\n      F-L Per-Subgroup: s0=+0.024 s1=+0.160. EC-HTE: s0=+0.006 s1=+0.001 (near-zero\n      bias both subgroups)'\n    key_finding: F-L scalar and F-L per-subgroup both WORSE than naive on aggregate\n      |bias|. F-L scalar over-corrects s0 (bias +0.073 vs naive +0.005). F-L per-subgroup\n      dramatically over-corrects s1 (bias +0.160). EC-HTE achieves near-zero per-subgroup\n      bias with nominal coverage (95.3%). CM inversion fundamentally different from\n      F-L scalar rescaling.\n- exp_id: exp-035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    source: results/exp_asymmetric_cm_summary.csv\n    echte_asym_abs_bias: 0.057\n    echte_asym_rmse: 0.0735\n    echte_asym_coverage: 0.945\n    echte_sym_abs_bias: 0.0618\n    echte_sym_rmse: 0.0831\n    echte_sym_coverage: 0.93\n    global_asym_abs_bias: 0.0609\n    global_asym_coverage: 0.915\n    global_sym_abs_bias: 0.0629\n    global_sym_coverage: 0.915\n    naive_abs_bias: 0.0592\n    naive_coverage: 0.87\n    oracle_abs_bias: 0.0454\n    oracle_coverage: 0.943\n    asym_vs_sym_echte_rmse_delta: -0.0096\n    asym_vs_sym_echte_cov_delta: 0.015\n    s1_echte_asym_cov: 0.93\n    s1_echte_sym_cov: 0.91\n    key_finding: 'EC-HTE asymmetric achieves 94.5% coverage (vs 93.0% symmetric) under\n      7:1 FPR/FNR ratio. RMSE improved 11.5% (0.0831→0.0735). Asymmetric formula essential\n      for high FPR/FNR ratios. s1 (high-error) coverage: 93.0% asymmetric vs 91.0%\n      symmetric.'\n- exp_id: exp-037\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    source: results/exp_calibration_summary.csv\n    calibrated_echte_abs_bias: 0.0554\n    calibrated_echte_coverage: 0.965\n    calibrated_global_abs_bias: 0.055\n    calibrated_global_coverage: 0.963\n    calibrated_naive_abs_bias: 0.051\n    calibrated_naive_coverage: 0.912\n    uncalibrated_echte_abs_bias: 0.0641\n    uncalibrated_echte_coverage: 0.938\n    uncalibrated_global_abs_bias: 0.0695\n    uncalibrated_global_coverage: 0.92\n    uncalibrated_naive_abs_bias: 0.0634\n    uncalibrated_naive_coverage: 0.84\n    oracle_abs_bias: 0.0431\n    oracle_coverage: 0.963\n    delta_pi_uncalibrated: 0.2\n    delta_pi_calibrated: 0.07\n    key_finding: Calibration reduces Δπ from 0.20 to 0.07 and improves naive coverage\n      (84.0%→91.2%) but doesn't reach nominal 95%. Calibrated+EC-HTE achieves best\n      coverage (96.5%) — EC-HTE corrects residual heterogeneity post-calibration.\n      Calibrated+Naive still under-covers by 3.8pp. EC-HTE and calibration are complementary,\n      not substitutes.\n- exp_id: exp-036\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    source: results/exp_bootstrap_se_v2_summary.csv\n    note: v2 with n_estimators=200 (fixes v1 n_estimators=48 artifact)\n    plugin_coverage: 0.9375\n    bootstrap_coverage: 0.95\n    oracle_coverage: 0.9\n    coverage_improvement: 0.0125\n    plugin_se_mean: 0.073\n    bootstrap_se_mean: 0.083\n    se_ratio_boot_over_plugin: 1.154\n    s0_plugin_cov: 0.95\n    s0_bootstrap_cov: 0.925\n    s1_plugin_cov: 0.925\n    s1_bootstrap_cov: 0.975\n    s1_se_ratio: 1.222\n    n_mc: 20\n    n_bootstrap: 100\n    n_estimators: 200\n    runtime_sec: 1716\n    key_finding: With correct n_estimators=200, plugin SE already near-nominal (93.8%).\n      Bootstrap provides modest improvement to exact 95.0%. v1 '81.7% → 94.2%' gap\n      was artifact of n_estimators=48.\n- exp_id: exp-038\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    reversal_pct_tau001: 31\n    reversal_pct_tau003: 14.9\n    reversal_pct_tau005: 6.1\n    reversal_pct_tau010: 0\n    ec_hte_reversal_pct: 0\n    worst_combo: tau=0.01, delta_misclass=0.19 → 42.9%\n- exp_id: exp-039\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K2_echte_bias: 0.008\n    K2_echte_rmse: 0.089\n    K2_echte_cov: 0.938\n    K4_echte_bias: 0.012\n    K4_echte_rmse: 0.12\n    K4_echte_cov: 0.956\n    K8_echte_bias: 0.183\n    K8_echte_rmse: 0.34\n    K8_echte_cov: 0.956\n    K8_global_rmse: 0.168\n- exp_id: exp-040\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma0_cov: 0.945\n    gamma0_rmse: 0.075\n    gamma005_cov: 0.897\n    gamma005_rmse: 0.092\n    gamma010_cov: 0.75\n    gamma010_rmse: 0.133\n    gamma015_cov: 0.525\n    gamma015_rmse: 0.177\n    gamma020_cov: 0.37\n    gamma020_rmse: 0.224\n    breakeven_gamma: 0.1\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-23T19:31:19.772Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T19:31:19.772Z",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-23T19:31:19.796Z_

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
focus: Reframed paper: title changed to "When Debiasing Hurts", core contributions shifted from EC-HTE method to (1) exact bias identity + (2) actionable diagnostic. EC-HTE de-emphasized as "the correction prescribed by the identity." New real-data validation on CivilComments (R²=0.944, 14 LLM-dataset combinations). Evaluate whether this framing shift improves Excitement scores vs previous 3/3.5 baseline.

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
- exp_id: exp-015
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n_mc: 100
    n_expert_grid:
    - 100
    - 250
    - 500
    subgroups: 4
    real_cm_source: exp-012 GPT-4.1 pilot
    cm_params:
      S0_False_medium:
        FPR: 0.054
        FNR: 0.526
        weight: 0.38
      S1_False_short:
        FPR: 0.101
        FNR: 0.3
        weight: 0.22
      S2_True_short:
        FPR: 0.143
        FNR: 0.308
        weight: 0.14
      S3_True_medium:
        FPR: 0.194
        FNR: 0.222
        weight: 0.25
    delta_pi: 0.098
    P_Z1: 0.18
    rmse_n100:
      naive: 0.123
      global: 0.263
      hb: 0.784
    rmse_n250:
      naive: 0.123
      global: 0.232
      hb: 0.411
    rmse_n500:
      naive: 0.123
      global: 0.196
      hb: 0.26
    coverage_n100:
      naive: 0.868
      global: 0.922
      hb: 0.744
    coverage_n250:
      naive: 0.868
      global: 0.908
      hb: 0.828
    coverage_n500:
      naive: 0.873
      global: 0.885
      hb: 0.89
    hb_worse_than_global_all_n: true
    root_cause: S0 FNR=0.526 makes CM row near-uniform [0.526, 0.474], inversion amplifies
      noise. Combined with P(Z=1)=0.18, too few Z=1 expert labels per subgroup for
      reliable per-subgroup CM estimation.
    key_finding: EC-HTE fails under realistic asymmetric CMs when any subgroup has
      FNR≈0.5 (near-random for positive class). This is consistent with exp-004 (FNR=53%)
      and exp-013 (boundary at n_expert/K=12.5). Identifies classifier quality threshold
      as honest limitation.
- exp_id: exp-016
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    model_selected: gpt-3.5-turbo
    worst_subgroup_fnr: 0.211
    worst_subgroup_fpr: 0.393
    rmse_n100:
      naive: 0.127
      global: 0.265
      hb: 0.93
    rmse_n250:
      naive: 0.127
      global: 0.221
      hb: 0.527
    rmse_n500:
      naive: 0.127
      global: 0.199
      hb: 0.322
    coverage_n100:
      naive: 0.784
      global: 0.893
      hb: 0.769
    coverage_n250:
      naive: 0.784
      global: 0.922
      hb: 0.843
    coverage_n500:
      naive: 0.784
      global: 0.939
      hb: 0.894
    hb_worse_than_global_all_n: true
    vs_exp015: exp-016 HB RMSE even worse than exp-015 despite lower FNR, because
      high FPR variance (0.14-0.39) makes subgroup CM estimation harder
    bright_spot: 'S0/z=1 at n=500: HB |bias|=0.193 < Global |bias|=0.252 — one case
      where subgroup-specific correction helps'
    root_cause: High FPR variance across subgroups (0.143-0.393) + P(Z=1)=0.18 → insufficient
      Z=1 expert labels per subgroup. Lower FNR alone does not fix the fundamental
      sample-size constraint.
    key_finding: Neither low-FNR (gpt-3.5-turbo) nor low-FPR (GPT-4.1) real CMs enable
      EC-HTE to beat global. The bottleneck is P(Z=1)=0.18 creating too few positive-class
      expert labels per subgroup for reliable CM estimation.
- exp_id: exp-017
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_mc: 50
    config: K=2/extreme/n_expert=500
    rlearner_results:
      naive:
        avg_abs_bias: 0.121
        rmse: 0.139
        coverage: 0.47
      global:
        avg_abs_bias: 0.098
        rmse: 0.123
        coverage: 0.71
      ec_hte:
        avg_abs_bias: 0.013
        rmse: 0.08
        coverage: 0.92
      oracle:
        avg_abs_bias: 0.006
        rmse: 0.056
        coverage: 0.94
    causal_forest_comparison:
      naive:
        avg_abs_bias: 0.125
        rmse: 0.143
        coverage: 0.46
      global:
        avg_abs_bias: 0.104
        rmse: 0.129
        coverage: 0.65
      ec_hte:
        avg_abs_bias: 0.008
        rmse: 0.082
        coverage: 0.91
    ec_hte_bias_reduction_vs_naive: 9.3x (R-learner) vs 15.6x (CausalForest)
    pattern_consistent: true
    key_finding: EC-HTE correction generalizes across CATE estimators. R-learner ec_hte
      achieves |bias|=0.013 (vs naive 0.121), 92% coverage — closely matching CausalForest
      pattern.
- exp_id: exp-018
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_mc: 50
    config: K=2/extreme/n_expert=500/multiplicative
    dgp: Y(1) = Y(0) * exp(tau(Z)), tau(Z=0)=0, tau(Z=1)=0.3
    results:
      oracle:
        avg_abs_bias: 0.031
        rmse: 0.038
        coverage: 0.96
      ec_hte:
        avg_abs_bias: 0.054
        rmse: 0.068
        coverage: 0.955
      global_corrected:
        avg_abs_bias: 0.11
        rmse: 0.124
        coverage: 0.54
      naive:
        avg_abs_bias: 0.135
        rmse: 0.142
        coverage: 0.435
    ec_hte_rmse_reduction_vs_naive: 52%
    ec_hte_coverage: 0.955
    vs_exp001_additive: EC-HTE RMSE 0.068 (multiplicative) vs 0.091 (additive, same
      config) — actually better due to larger true CATEs making relative bias smaller
    key_finding: EC-HTE robust to non-additive treatment effects. 52% RMSE reduction
      vs naive, 95.5% coverage (target 95%). Answers Reviewer Q3.
- exp_id: exp-019
  name: ''
  status: DONE
  conclusion: success
  metrics:
    theorem1_r2:
      K2:
        pz0.1: 0.998
        pz0.2: 0.989
        pz0.3: 0.994
        pz0.4: 0.995
        pz0.5: 0.995
      K4:
        pz0.1: 0.984
        pz0.2: 0.976
        pz0.3: 0.985
        pz0.4: 0.984
        pz0.5: 0.992
    theorem1_r2_range: 0.976-0.998 (all >0.95)
    rmse_ratio_hb_over_global:
      K2:
        pz0.1: 0.92
        pz0.2: 0.763
        pz0.3: 0.78
        pz0.4: 0.874
        pz0.5: 0.857
      K4:
        pz0.1: 1.542
        pz0.2: 1.684
        pz0.3: 1.121
        pz0.4: 1.082
        pz0.5: 1.063
    hb_wins_K2: all 5 P(Z=1) values (ratio 0.76-0.92)
    hb_wins_K4: none (ratio 1.06-1.68)
    coverage_hb: 0.92-0.94 across all settings (near-nominal 0.95)
    coverage_naive: 0.65-0.79
    coverage_global: 0.79-0.90
    key_finding: 'Theorem 1 R²>0.976 universally — bias decomposition holds regardless
      of P(Z=1). EC-HTE RMSE advantage depends on K: K=2 HB wins everywhere, K=4 HB
      loses at n_expert=250 (insufficient per-subgroup minority data). Coverage: HB
      0.92-0.94 near-nominal at all settings.'
- exp_id: exp-020
  name: ''
  status: DONE
  conclusion: success
  metrics:
    max_cond_number: 1.89
    mean_cond_number: 1.446
    p99_cond_number: 1.893
    guard_trigger_rate_all_kappa: 0
    rmse_hb: 0.0759
    rmse_global: 0.0765
    rmse_ratio: 1.048
    numerical_instability_rate: 0
    safety_margin_at_kappa100: 53x
    stress_test_near_random_max_cond: 1125.3
    stress_test_near_random_triggers_kappa100: true
- exp_id: exp-021
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_cells_compared: 94
    median_delta_pct: 3.2
    max_delta_pct: 25.5
    cells_under_5pct: 79/94 (84%)
    cells_under_10pct: 93/94 (99%)
    outlier: K=4/extreme/n=100/HB base (-25.5%, known numerically unstable)
    method_note: EB instead of Gibbs (<0.002 CM difference, 10s vs 114min)
- exp_id: exp-022
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rmse_range_reasonable: 6.0%
    rmse_range_all: 17.3%
    gamma31_rmse: 0.0841
    gamma31_rank: 8/15
    coverage_range: 0.925-0.938
    hb_beats_mle: 9/15
    best_config: Gamma(1,0.5)
    best_rmse: 0.0825
- exp_id: exp-023
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dgp: heterogeneous-tau
    N: 5000
    P_Z1: 0.652
    K: 4
    subgroups:
    - False_medium
    - False_short
    - True_medium
    - True_short
    delta_tau:
      False_medium: 0.1
      False_short: 0.1
      True_medium: 0.3
      True_short: 0.6
    n_expert_sweep:
    - 200
    - 500
    - 1000
    mc_seeds: 50
    hb_method: MAP-EB Gamma(3,1)
    bias_echte_wins: 3/3 budgets
    bias_reduction_n500: 68% vs Global (0.0099 vs 0.0314)
    bias_reduction_n200: 32% vs Global (0.0248 vs 0.0365)
    bias_reduction_n1000: 55% vs Global (0.0130 vs 0.0286)
    rmse_echte_wins: 0/3 aggregate
    rmse_true_short_n1000:
      global: 0.1693
      echte: 0.1637
      improvement: -3.3%
    rmse_true_short_z0_n1000:
      global: 0.2577
      echte: 0.2117
      improvement: -17.8%
    key_finding: EC-HTE wins bias at all budgets. High-Δτ subgroup (True_short) RMSE
      wins at n≥500. Aggregate RMSE loss driven by low-Δτ subgroups where stratified
      variance cost exceeds small bias gain.
- exp_id: exp-024
  name: ''
  status: DONE
  conclusion: success
  metrics:
    R2_overall: 0.975
    data_sources:
    - exp023_confusion_matrices.json
    - c1_multi_llm/*_cm_profile.md
    n_llm_dataset_combos: 11
    output_files:
    - results/exp_realcm_bias_identity.csv
    - results/exp_realcm_summary.csv
- exp_id: exp-025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    screening: 0/16 combos pass all conditions (κ≤1.25 bottleneck)
    oracle_screening: HB wins 41/52 comparisons on aggregate RMSE
    hb_vs_mle: HB beats Strat MLE in 52/52 comparisons
    best_case: 'Qwen2.5-7B K=4 n=500 Z=0: ΔRMSE=-0.0075'
    open_source_llms: All 4 (Llama/Qwen/Mistral/Gemma) HB wins 32/32 on TweetEval
    hb_loses: gpt-3.5-turbo/TweetEval (high FPR asymmetry), gpt-4o/CivilComments (low
      P(Z=1)=0.3)
    output_files:
    - results/exp_screening.csv
    - results/exp_oracle_screening.csv
    - results/exp_positive_scenario_summary.md
- exp_id: exp-026
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K2_n25:
      mle_rmse: 0.2562
      hb_rmse: 0.2689
      delta_pct: +4.9%
      global_rmse: 0.1013
    K2_n50:
      mle_rmse: 0.2748
      hb_rmse: 0.2306
      delta_pct: -16.1%
      global_rmse: 0.0879
    K2_n75:
      mle_rmse: 0.0911
      hb_rmse: 0.0893
      delta_pct: -1.9%
    K4_n25:
      mle_rmse: 0.4011
      hb_rmse: 0.6116
      delta_pct: +52.5%
      global_rmse: 0.1289
    K4_n50:
      mle_rmse: 0.3798
      hb_rmse: 0.4701
      delta_pct: +23.8%
      global_rmse: 0.1172
    K4_n75:
      mle_rmse: 0.2208
      hb_rmse: 0.2111
      delta_pct: -4.4%
    K4_n100:
      mle_rmse: 0.2152
      hb_rmse: 0.2123
      delta_pct: -1.3%
    coverage_all: '>=0.88, no catastrophic failures'
    crossover_K2: n_expert=50 (HB -16.1%)
    crossover_K4: n_expert=75 (HB -4.4%)
    key_finding: HB shrinkage advantage emerges at n≥50 (K=2) and n≥75 (K=4). Below
      these thresholds, global pooling outperforms both HB and MLE — validates budget
      threshold claim.
    mc_runs: 100
    output_file: results/exp_low_budget_hb.csv
- exp_id: exp-027
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    oracle_true_Z:
      coverage: 0.945
      bias: 0.0056
      rmse: 0.078
    echte_true_CM:
      coverage: 0.925
      bias: 0.0078
      rmse: 0.114
    echte_estimated_CM:
      coverage: 0.931
      bias: 0.0148
      rmse: 0.121
    global_true_CM:
      coverage: 0.913
      bias: 0.0371
      rmse: 0.11
    global_estimated_CM:
      coverage: 0.911
      bias: 0.0379
      rmse: 0.111
    naive:
      coverage: 0.883
      bias: 0.0447
      rmse: 0.095
    key_finding: 'Oracle CF SE well-calibrated (94.5%). EC-HTE true CM (92.5%) ≈ estimated
      CM (93.1%): CM estimation NOT the coverage gap source. ~2pp drop from Oracle
      to EC-HTE true CM comes from M^{-1} SE propagation, not CM estimation noise.'
    dgp: K=4 extreme, N=5000, n_expert=500, 100 MC runs
    output_file: results/exp_cf_oracle_coverage.csv
- exp_id: exp-027b
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    dgp: K=2 extreme, π=[0.05,0.25], N=5000, n_expert=250, 100 MC runs
    oracle_true_Z:
      coverage: 0.94
      bias: 0.0023
      rmse: 0.056
    echte_true_CM:
      coverage: 0.94
      bias: 0.0027
      rmse: 0.073
    echte_estimated_CM:
      coverage: 0.925
      bias: 0.0044
      rmse: 0.079
    global_true_CM:
      coverage: 0.885
      bias: 0.045
      rmse: 0.083
    global_estimated_CM:
      coverage: 0.883
      bias: 0.045
      rmse: 0.085
    naive:
      coverage: 0.828
      bias: 0.046
      rmse: 0.077
    key_finding: 'K=2: Oracle 94%, EC-HTE true CM 94%, EC-HTE estimated CM 92.5%.
      CF SE is well-calibrated. 83-85% coverage in paper comes from Naive (uncorrected
      misclassification bias), NOT from CF SE under-calibration. EC-HTE restores near-nominal
      coverage.'
    output_file: results/exp_cf_oracle_coverage_k2.csv
- exp_id: exp-027c
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dgp: 'MF2 exact DGP: K=2, π=[0.05,0.25], τ(0)=0.10, τ(1)=0.40, N=5000, n_expert=250,
      100 MC'
    oracle_true_Z:
      coverage: 0.96
      bias: 0.077
      rmse: 0.091
      mean_se: 0.09
    echte_true_CM:
      coverage: 0.913
      bias: 0.103
      rmse: 0.112
      mean_se: 0.114
    echte_estimated_CM:
      coverage: 0.923
      bias: 0.1
      rmse: 0.111
      mean_se: 0.119
    global_true_CM:
      coverage: 0.95
      bias: 0.107
      rmse: 0.114
      mean_se: 0.107
    global_estimated_CM:
      coverage: 0.943
      bias: 0.105
      rmse: 0.114
      mean_se: 0.109
    naive:
      coverage: 0.773
      bias: 0.12
      rmse: 0.125
      mean_se: 0.087
    key_finding: 'DGP difference NOT the source of 83% vs 92.5% gap. Per-subgroup
      EC-HTE coverage ~92.25% in both 027b and 027c. The 83% in MF2 is an aggregate
      mixing effect: low-misclass subgroup (π=0.05) has 83% coverage while high-misclass
      subgroup (π=0.25) has 99%. M⁻¹ creates asymmetric SE amplification across subgroups.'
    comparison_027b:
      oracle: 94.0% → 96.0%
      echte_est: 92.5% → 92.25%
      conclusion: Nearly identical per-subgroup coverage despite different τ values
    output_file: results/exp_cf_oracle_coverage_mf2dgp.csv
- exp_id: exp-028
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    overall_symmetric_auc: 0.626
    overall_asymmetric_auc: 0.611
    k4_only:
      symmetric_auc_range: 0.0-1.0
      asymmetric_auc_range: 0.0-1.0
      perfect_auc_combos:
      - Llama/TweetEval
      - Qwen/TweetEval
      - Mistral/TweetEval
      - gpt-4o/TweetEval
      - gpt-3.5-turbo/TweetEval(asym only)
      - gpt-4.1/TweetEval(asym only)
    k2_all_auc_zero: true
    z0_z1_identical: true
    theoretical_insight: For DIM, |B_s[0,1]|=|B_s[1,1]| (column-stochastic M). Asymmetric
      diagnostic degenerates to symmetric because DIM CATE bias depends on δ_s = (FPR_s+FNR_s)/2
      - π̄, not on FPR/FNR individually.
    output_files:
    - results/exp_asymmetric_diagnostic_auc.csv
    - results/exp_asymmetric_diagnostic_auc_summary.csv
- exp_id: exp-029
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dgp: K=2, pi=[0.05,0.25], tau(0)=0, tau(1)=0.3, N=5000, n_expert=250, 100 MC
    gamma_sweep:
    - 0
    - 0.05
    - 0.1
    - 0.15
    - 0.2
    echte_coverage:
      g0.00: 0.955
      g0.05: 0.955
      g0.10: 0.953
      g0.15: 0.948
      g0.20: 0.935
    echte_abs_bias:
      g0.00: 0.0596
      g0.05: 0.0593
      g0.10: 0.063
      g0.15: 0.0652
      g0.20: 0.0677
    global_coverage:
      g0.00: 0.927
      g0.05: 0.935
      g0.10: 0.938
      g0.15: 0.943
      g0.20: 0.94
    naive_coverage:
      g0.00: 0.877
      g0.05: 0.838
      g0.10: 0.835
      g0.15: 0.792
      g0.20: 0.795
    key_finding: 'EC-HTE coverage degrades gracefully: 95.5%→93.5% over gamma 0→0.2
      (−2.0pp). ALL correction methods maintain ≥90% coverage across all gamma. Naive
      degrades fastest (87.7%→79.5%, −8.2pp). At moderate violation gamma=0.1, EC-HTE
      coverage=95.3% (−0.2pp from baseline). EC-HTE |bias| increases 13.7% at gamma=0.2
      but remains comparable to Global.'
    coverage_below_90_threshold:
      Naive: 0
      Global: never
      Strat_MLE: never
      HB_ECHTE: never
    output_files:
    - results/exp_a1_sensitivity.csv
    - results/exp_a1_sensitivity_summary.csv
    - results/exp_a1_sensitivity_subgroup.csv
- exp_id: exp-030
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    hb_echte_coverage: 0.956
    hb_echte_rmse: 0.34
    hb_echte_mean_abs_bias: 0.183
    oracle_coverage: 0.944
    oracle_rmse: 0.113
    oracle_mean_abs_bias: 0.09
    global_coverage: 0.951
    global_rmse: 0.168
    global_mean_abs_bias: 0.135
    strat_mle_coverage: 0.953
    strat_mle_rmse: 0.638
    strat_mle_mean_abs_bias: 0.219
    naive_coverage: 0.913
    naive_rmse: 0.133
    naive_mean_abs_bias: 0.107
    hb_vs_mle_rmse_improvement_pct: 47
    per_subgroup_expert_labels: 31
    source: results/exp_k8_subgroups_summary.csv
    note: All CM-aware methods coverage ≥95%. HB RMSE 47% better than MLE but worse
      than Global. K=8 is boundary condition.
- exp_id: exp-031
  name: ''
  status: DONE
  conclusion: success
  metrics:
    hb_echte_coverage: 0.95
    hb_echte_rmse: 0.086
    hb_echte_mean_abs_bias: 0.068
    oracle_coverage: 0.943
    oracle_rmse: 0.061
    oracle_mean_abs_bias: 0.048
    global_coverage: 0.93
    global_rmse: 0.087
    global_mean_abs_bias: 0.071
    strat_mle_coverage: 0.95
    strat_mle_rmse: 0.087
    strat_mle_mean_abs_bias: 0.069
    naive_coverage: 0.863
    naive_rmse: 0.083
    naive_mean_abs_bias: 0.066
    beta_confound: 0.5
    propensity_range: 0.38-0.62
    source: results/exp_confounded_dgp_summary.csv
    note: EC-HTE + IPW-DIM coverage 95.0% under moderate confounding. Global 93.0%.
      Naive 86.3%.
- exp_id: exp-032
  name: ''
  status: DONE
  conclusion: success
  metrics:
    min_hb_coverage: 0.945
    max_oracle_vs_est_gap: 0.01
    hb_cov_b0.25_oracle: 0.9625
    hb_cov_b0.25_estimated: 0.9725
    hb_cov_b0.5_oracle: 0.95
    hb_cov_b0.5_estimated: 0.9575
    hb_cov_b1.0_oracle: 0.9575
    hb_cov_b1.0_estimated: 0.96
    hb_cov_b2.0_oracle: 0.945
    hb_cov_b2.0_estimated: 0.9475
    hb_rmse_b2.0_oracle: 0.1258
    naive_cov_range: 0.845-0.898
    source: results/exp_confounded_sweep_summary.csv
    note: All 8 configs HB coverage >=94.5%. Oracle vs estimated gap <=1pp. Hypothesis
      fully confirmed.
- exp_id: exp-033
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    hb_baseline_rmse: 0.333
    hb_baseline_coverage: 0.959
    v1_adaptive_alpha_rmse: 0.216
    v1_adaptive_alpha_coverage: 0.96
    v2_kappa_fallback_rmse: 0.25
    v2_kappa_fallback_coverage: 0.96
    v3_combined_rmse: 0.216
    v3_combined_coverage: 0.96
    global_rmse: 0.166
    global_coverage: 0.958
    v1_vs_baseline_improvement_pct: 35
    v1_still_exceeds_global_pct: 30
    source: results/exp_k8_adaptive_summary.csv
    note: V1 (adaptive alpha) reduces RMSE 35% (0.333->0.216) but still exceeds Global
      (0.166). Gap narrowed from 2x to 1.3x. Confirms boundary is real but mitigable.
- exp_id: exp-034
  name: ''
  status: DONE
  conclusion: success
  metrics:
    source: results/exp_fl_comparison_summary.csv
    fl_scalar_abs_bias: 0.0909
    fl_scalar_rmse: 0.1161
    fl_scalar_coverage: 0.85
    fl_per_subgroup_abs_bias: 0.112
    fl_per_subgroup_rmse: 0.1582
    fl_per_subgroup_coverage: 0.838
    echte_abs_bias: 0.0643
    echte_rmse: 0.0858
    echte_coverage: 0.953
    global_cm_abs_bias: 0.0643
    global_cm_rmse: 0.0806
    global_cm_coverage: 0.938
    naive_abs_bias: 0.0621
    naive_coverage: 0.858
    oracle_abs_bias: 0.0454
    oracle_coverage: 0.943
    sign_reversal: 'F-L Scalar: s0=+0.073 s1=+0.068, both positive (no sign-reversal).
      F-L Per-Subgroup: s0=+0.024 s1=+0.160. EC-HTE: s0=+0.006 s1=+0.001 (near-zero
      bias both subgroups)'
    key_finding: F-L scalar and F-L per-subgroup both WORSE than naive on aggregate
      |bias|. F-L scalar over-corrects s0 (bias +0.073 vs naive +0.005). F-L per-subgroup
      dramatically over-corrects s1 (bias +0.160). EC-HTE achieves near-zero per-subgroup
      bias with nominal coverage (95.3%). CM inversion fundamentally different from
      F-L scalar rescaling.
- exp_id: exp-035
  name: ''
  status: DONE
  conclusion: success
  metrics:
    source: results/exp_asymmetric_cm_summary.csv
    echte_asym_abs_bias: 0.057
    echte_asym_rmse: 0.0735
    echte_asym_coverage: 0.945
    echte_sym_abs_bias: 0.0618
    echte_sym_rmse: 0.0831
    echte_sym_coverage: 0.93
    global_asym_abs_bias: 0.0609
    global_asym_coverage: 0.915
    global_sym_abs_bias: 0.0629
    global_sym_coverage: 0.915
    naive_abs_bias: 0.0592
    naive_coverage: 0.87
    oracle_abs_bias: 0.0454
    oracle_coverage: 0.943
    asym_vs_sym_echte_rmse_delta: -0.0096
    asym_vs_sym_echte_cov_delta: 0.015
    s1_echte_asym_cov: 0.93
    s1_echte_sym_cov: 0.91
    key_finding: 'EC-HTE asymmetric achieves 94.5% coverage (vs 93.0% symmetric) under
      7:1 FPR/FNR ratio. RMSE improved 11.5% (0.0831→0.0735). Asymmetric formula essential
      for high FPR/FNR ratios. s1 (high-error) coverage: 93.0% asymmetric vs 91.0%
      symmetric.'
- exp_id: exp-037
  name: ''
  status: DONE
  conclusion: success
  metrics:
    source: results/exp_calibration_summary.csv
    calibrated_echte_abs_bias: 0.0554
    calibrated_echte_coverage: 0.965
    calibrated_global_abs_bias: 0.055
    calibrated_global_coverage: 0.963
    calibrated_naive_abs_bias: 0.051
    calibrated_naive_coverage: 0.912
    uncalibrated_echte_abs_bias: 0.0641
    uncalibrated_echte_coverage: 0.938
    uncalibrated_global_abs_bias: 0.0695
    uncalibrated_global_coverage: 0.92
    uncalibrated_naive_abs_bias: 0.0634
    uncalibrated_naive_coverage: 0.84
    oracle_abs_bias: 0.0431
    oracle_coverage: 0.963
    delta_pi_uncalibrated: 0.2
    delta_pi_calibrated: 0.07
    key_finding: Calibration reduces Δπ from 0.20 to 0.07 and improves naive coverage
      (84.0%→91.2%) but doesn't reach nominal 95%. Calibrated+EC-HTE achieves best
      coverage (96.5%) — EC-HTE corrects residual heterogeneity post-calibration.
      Calibrated+Naive still under-covers by 3.8pp. EC-HTE and calibration are complementary,
      not substitutes.
- exp_id: exp-036
  name: ''
  status: DONE
  conclusion: success
  metrics:
    source: results/exp_bootstrap_se_v2_summary.csv
    note: v2 with n_estimators=200 (fixes v1 n_estimators=48 artifact)
    plugin_coverage: 0.9375
    bootstrap_coverage: 0.95
    oracle_coverage: 0.9
    coverage_improvement: 0.0125
    plugin_se_mean: 0.073
    bootstrap_se_mean: 0.083
    se_ratio_boot_over_plugin: 1.154
    s0_plugin_cov: 0.95
    s0_bootstrap_cov: 0.925
    s1_plugin_cov: 0.925
    s1_bootstrap_cov: 0.975
    s1_se_ratio: 1.222
    n_mc: 20
    n_bootstrap: 100
    n_estimators: 200
    runtime_sec: 1716
    key_finding: With correct n_estimators=200, plugin SE already near-nominal (93.8%).
      Bootstrap provides modest improvement to exact 95.0%. v1 '81.7% → 94.2%' gap
      was artifact of n_estimators=48.
- exp_id: exp-038
  name: ''
  status: DONE
  conclusion: success
  metrics:
    reversal_pct_tau001: 31
    reversal_pct_tau003: 14.9
    reversal_pct_tau005: 6.1
    reversal_pct_tau010: 0
    ec_hte_reversal_pct: 0
    worst_combo: tau=0.01, delta_misclass=0.19 → 42.9%
- exp_id: exp-039
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K2_echte_bias: 0.008
    K2_echte_rmse: 0.089
    K2_echte_cov: 0.938
    K4_echte_bias: 0.012
    K4_echte_rmse: 0.12
    K4_echte_cov: 0.956
    K8_echte_bias: 0.183
    K8_echte_rmse: 0.34
    K8_echte_cov: 0.956
    K8_global_rmse: 0.168
- exp_id: exp-040
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gamma0_cov: 0.945
    gamma0_rmse: 0.075
    gamma005_cov: 0.897
    gamma005_rmse: 0.092
    gamma010_cov: 0.75
    gamma010_rmse: 0.133
    gamma015_cov: 0.525
    gamma015_rmse: 0.177
    gamma020_cov: 0.37
    gamma020_rmse: 0.224
    breakeven_gamma: 0.1

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
  "promptId": "a4ce697f-781e-4400-87cd-6b77f8ec6faa",
  "type": "user",
  "uuid": "889db26e-26b3-4c79-936d-601504427876",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T19:31:19.794Z_

```json
{
  "parentUuid": "889db26e-26b3-4c79-936d-601504427876",
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
  "uuid": "e52d5e7e-25d4-4521-bd35-57888b110cb7",
  "timestamp": "2026-05-23T19:31:19.794Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T19:31:19.794Z_

```json
{
  "parentUuid": "e52d5e7e-25d4-4521-bd35-57888b110cb7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1ecfe3ae-dd01-4021-a56b-9152fb37d418",
  "timestamp": "2026-05-23T19:31:19.794Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc",
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
  "leafUuid": "1ecfe3ae-dd01-4021-a56b-9152fb37d418",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Dream scenario planning for When Debiasing Hurts",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc"
}
```

---

### Assistant

_source line 8 · 2026-05-23T19:32:37.754Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research project thoroughly to define three tiers of Dream simulation scenarios.

The project is about EC-HTE (Error-Corrected Heterogeneous Treatment Effects) for LLM annotation in CSS research, targeting EMNLP 2026. The core idea is that when LLM misclassification rates vary across subgroups, applying a global correction can worsen CATE bias — and EC-HTE (hierarchical Bayesian stratified correction) fixes this.

Let me synthesize the key findings from the completed experiments:

**Strengths (what's working):**
1. Bias decomposition identity: R² = 0.976-0.998 (exp-002, exp-019, exp-024)


2. Debiasing paradox: global correction amplifies bias in roughly half the parameter space, reaching up to 5.9x worse (exp-002, exp-011)
3. EC-HTE effectiveness: delivers meaningful bias reduction when we have enough expert labels, especially in extreme scenarios (exp-001, exp-003, exp-006)
4. PPCI composition: achieves near-zero bias when handling dual-error cases (exp-007)
5. Real-world validation: R²=0.944 on CivilComments across 14 LLM-dataset combinations (exp-024)
6. Robustness: maintains stable performance even when subgroup specifications are misaligned (exp-010)

The method also handles confounding, violations of the positivity assumption, multiplicative effects, and multiple CATE estimators gracefully. All six LLMs show meaningful performance gains above the 0.05 threshold, and calibration complementarity holds up empirically.

But there are real constraints: EC-HTE breaks down with realistic asymmetric confusion matrices where false negative rates hit 0.5, the method degrades when we drop below 8 subgroups, and we're trading off higher RMSE for lower bias in many configurations. The diagnostic AUC at the setting level is only 0.49, which suggests limited predictive power there.

The real-world case study doesn't show clear wins for EC-HTE on average absolute bias, which is concerning. Coverage drops sharply when we violate the assumption at gamma=0.10, and there's a meaningful sample size requirement—we need at least 25-50 experts per subgroup, with crossover points ranging from 250 observations at K=2 up to 1000 at K=4. I should track reviewer excitement, bias decomposition R², the magnitude of bias reduction, diagnostic AUC, consistency on real data, RMSE severity, and calibration coverage as I evaluate different tiers.

In the best scenario, all three claims hold up strongly, the reframed narrative about when debiasing backfires resonates, the bias identity is exact and novel, EC-HTE performs well within its constraints, and the diagnostic is genuinely useful. Real data validates the story compellingly, and reviewers see the problem identification as novel. In the median case, the bias identity is solid but the other claims have limitations—EC-HTE only works under extreme heterogeneity with sufficient budget, the diagnostic AUC is weak at the setting level, and real data is inconclusive. The pitch shifts toward emphasizing problem discovery rather than the method itself, since reviewers may question whether EC-HTE offers enough over simpler alternatives.

For the worst case, reviewers view the bias identity as incremental relative to existing measurement error literature, EC-HTE's failures on real data undermine its practical relevance, and the diagnostic doesn't work. The paper needs to pivot entirely toward being an empirical warning about when debiasing fails, with the identity as secondary theoretical support.

Now I'm mapping out concrete metrics to distinguish these tiers: reviewer excitement, soundness, novelty perception of the bias identity, practical value of EC-HTE, diagnostic utility, and how well real data supports the claims. The key question is whether reviewers accept the problem identification as genuinely novel or see it as incremental.

In the best case, the "When Debiasing Hurts" framing resonates as surprising, the high R² on synthetic data reads as exact rather than approximate, EC-HTE's heterogeneous regime feels practically relevant, and the real-data validation on CivilComments holds up despite the RMSE tradeoff. In the median case, reviewers push back on novelty, question when EC-HTE would actually apply, find the diagnostic AUC too weak, and the inconclusive real-data results become a liability.

At worst, the bias identity work looks incremental relative to classical statistics, the negative results on real content moderation systems dominate the narrative, the method appears fragile around K=8, and the sensitivity to gamma=0.1 feels too restrictive. Now I'm thinking through what concrete number ranges to assign for the excitement scores, building on the baseline of 3/3.5 and how much the reframing actually lifts those.

The metrics reviewers will focus on are the excitement and soundness scores on a 1-5 scale, the magnitude of the bias amplification effect, how much EC-HTE reduces bias in the operating regime, the diagnostic AUC, the R² on real data, and the calibration gap from the nominal 95% coverage. I need to define these carefully across the three tiers, keeping in mind that the experimental results are fixed—what varies is how reviewers interpret them. The real question is whether the reframing changes the panel's perception of the work given those fixed results.

The three reviewer panels will have different orientations: the best case has NLP and causal inference experts who appreciate the problem framing and see the identity as novel, the median case is mixed with some skepticism about novelty relative to classical measurement error literature, and the worst case is stats-heavy reviewers who view this as known territory and find the NLP application too narrow. Now I'll structure the YAML with excitement and soundness scores, overall recommendation, perceived novelty, and acceptance rates for each of the three main claims across the tiers.

Writing YAML structure... specific experimental metric ranges too. But the experiments are done — the results are fixed. The question is about reviewer perception. Let me think about this differently.

The Dream simulation is probably about simulating the paper review process. The "key experimental metrics" would be what reviewers perceive as the strength of evidence, which maps to how they interpret the existing results.

Let me structure this around ARR review criteria:
- Excitement (1-5)
- Soundness (1-5)  
- Overall Assessment (1-5)
- Confidence

And key qualitative assessments:
- Is Claim 1 accepted as novel?
- Is Claim 2 accepted as practically useful?
- Is Claim 3 accepted as actionable?

Let me write this up now.

For the number ranges, I'll include both reviewer score predictions and the key "perceived" metric interpretations.

Let me finalize the three tiers:

**Best (Excitement 4-4.5)**: The framing resonates as genuinely surprising to the NLP community, the bias identity reads as a novel formal contribution in the LLM annotation space, and the EC-HTE regime feels practically actionable for CSS workflows. The R²=0.944 result on real data lands as convincing validation, and acknowledging the RMSE tradeoff and K≥8 boundary actually builds credibility rather than undermining it. The full package—problem identification plus formal identity plus diagnostic tool—comes across as a complete contribution.

**Median (Excitement 3-3.5)**: The framing registers as interesting but not particularly surprising, since reviewers have encountered the "correction can hurt" intuition before. The bias identity gets acknowledged as a formalization of existing principles rather than something fundamentally new. The EC-HTE operating regime feels too narrow—requiring extreme heterogeneity and n≥250 limits how practically useful it seems. The diagnostic setting...

Actually, I need to continue from where the next thinking picks up. The next thinking mentions "diagnostic-level AUC=0.49 is weak" and other specifics. Let me integrate that naturally.

The diagnostic-level AUC of 0.49 reads as weak validation, and the real-data case study (exp-004) comes across as inconclusive. The narrative here shifts toward emphasizing problem discovery for the NLP community while downgrading EC-HTE from a solution to more of a proof of concept, with the diagnostic tool positioned as the independent contribution.

**Worst (Excitement 2.5-3)**: Reviewers with measurement error backgrounds see the bias identity as incremental relative to Carroll and Fuller's work. EC-HTE's failures on real confusion matrices (exp-015/016) signal that the method doesn't translate to practice. The paper doesn't convincingly answer "when would anyone actually use this?" The sensitivity analysis showing breakeven at γ=0.1 feels too restrictive, and the diagnostic doesn't operate at a granularity that's actually actionable. The whole thing gets reframed as a cautionary empirical tale rather than a methodological advance.

But wait—the instructions say the worst case still targets EMNLP main, not a downgrade to Findings. So I need to adjust: the worst-case narrative becomes an empirical warning paper anchored by strong real-data evidence across 14 LLM-dataset combinations with R²=0.944. The identity serves as the theoretical foundation, and EC-HTE becomes a demonstration of how the identity's diagnostic value works in practice. The paper's focus shifts from "here's a solution" to "here's the problem and what we learned."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ecfe3ae-dd01-4021-a56b-9152fb37d418",
  "isSidechain": false,
  "requestId": "req_011CbL4Eoxn5vwzvgbHrEPUi",
  "type": "assistant",
  "uuid": "577a4d4e-c226-4556-9fcc-04bbbd2c41ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSdbVz7QgHpsYcrDu4sz3M",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27134,
      "cache_read_input_tokens": 11841,
      "output_tokens": 5639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 5639,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 27134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27134
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

_source line 9 · 2026-05-23T19:33:35.054Z_

```yaml
tiers:
  best:
    meaning: "Reframed 'When Debiasing Hurts' narrative fully lands：reviewers认为 problem identification 本身是 EMNLP 级贡献，bias identity 的 exact 形式在 LLM annotation 语境下被接受为新颖，EC-HTE 在其 operating regime 内的表现被视为 convincing proof of concept"
    key_assumptions:
      - "NLP/CSS-oriented reviewer panel，对 classical measurement error 文献（Fuller/Carroll）不深度熟悉，因此 bias identity 在 LLM annotation 语境下的 formalization 被视为新颖贡献"
      - "'Debiasing can hurt' 的 framing 对 NLP 社区足够 surprising——多数 NLP 工作假设 correction 单调改善，reviewer 认同这是 under-recognized failure mode"
      - "EC-HTE 的 conditional advantage（extreme heterogeneity + n_expert≥250）被接受为 practical regime——reviewer 认同 CSS 场景中 Δπ>0.10 是常见的（exp-008: 6/6 models Δπ>0.05）"
      - "Real-data R²=0.944（14 LLM-dataset combos）被视为 strong pattern validation，不要求 ground-truth CATE benchmark"
      - "Honest limitations disclosure（RMSE tradeoff、K≥8 boundary、real CM negative results）增强可信度而非减分"
      - "Reviewer 不要求 convergence rates 或 minimax bounds——'problem identification + exact identity + diagnostic' 被接受为完整贡献"
    number_ranges:
      excitement: [4.0, 4.5]
      soundness: [3.5, 4.0]
      overall_recommendation: [3.5, 4.0]
      claim1_bias_identity_accepted_pct: [90, 100]
      claim2_echte_accepted_as_useful_pct: [70, 85]
      claim3_diagnostic_accepted_pct: [65, 80]
      perceived_novelty_score: [3.5, 4.5]
      major_weaknesses_per_review: [0, 1]
      revision_requests: ["minor (figures, writing clarity, bibliography)"]
    narrative_direction: "原始 reframed claims 完全成立。三条贡献层次清晰：(1) bias identity 是 exact 且 constructive，直接揭示 LLM annotation pipeline 中被忽视的 failure mode；(2) EC-HTE 是 identity 自然推导出的修正方案，在 high-heterogeneity regime 效果显著（bias reduction 4-15x，coverage 恢复至 95%）；(3) Δπ×Δτ diagnostic 提供 zero-cost 预检，让 practitioner 不用跑 EC-HTE 也能判断 global correction 是否安全。Abstract 可保留 '2-3x median amplification, up to 5.9x' headline。PPCI 互补性作为 bonus contribution。"

  median:
    meaning: "Problem framing 有吸引力但 novelty perception 分裂：部分 reviewer 认为 'correction can hurt' 是 known intuition 的 formalization，EC-HTE 的 narrow operating regime 削弱 practical impact，diagnostic 在 setting level 不 work"
    key_assumptions:
      - "至少一位 reviewer 有 measurement error / causal inference 背景，认为 bias identity 是 Fuller (1987) / Carroll (2006) 在 LLM 场景的 straightforward application，formal novelty modest"
      - "EC-HTE 仅在 extreme heterogeneity + n_expert≥250 (K=2) 或 n_expert≥1000 (K=4) 时优于 global——reviewer 质疑 'how often does this regime occur in practice?'"
      - "Diagnostic setting-level AUC=0.49（exp-005）被至少一位 reviewer 视为 'no better than random'——subgroup-level AUC=0.833 需要已知 subgroup structure，循环论证"
      - "Real-data case study (exp-004) EC-HTE 未能 outperform global（avg |bias|: naive 0.21, global 0.27, ec_hte 0.31）——reviewer 指出 method 在真实数据上 does not deliver"
      - "RMSE tradeoff（ec_hte RMSE up to 3.5x worse in small-n configs）被视为 significant practical limitation，不仅是 honest disclosure"
      - "Negative results on real CMs (exp-015/016: HB worse than global at all n) 被注意到但接受为 honest boundary condition"
    number_ranges:
      excitement: [3.0, 3.5]
      soundness: [3.5, 4.0]
      overall_recommendation: [3.0, 3.5]
      claim1_bias_identity_accepted_pct: [75, 90]
      claim2_echte_accepted_as_useful_pct: [40, 60]
      claim3_diagnostic_accepted_pct: [30, 50]
      perceived_novelty_score: [2.5, 3.5]
      major_weaknesses_per_review: [1, 2]
      revision_requests: ["major: strengthen novelty positioning vs classical ME, improve diagnostic, add successful real-data demonstration"]
    narrative_direction: "需要调整 claims 强度。Claim 1 降级：从 'previously unrecognized bias mechanism' 改为 'first formal characterization of classical ME amplification in LLM annotation pipelines, with exact product-form identity enabling computable diagnostics'——显式承认 qualitative insight 是 classical，quantitative form 和 application context 是新的。Claim 2 降级：EC-HTE 从 'substantial reduction' 改为 'proof-of-concept correction demonstrating the identity is actionable'——重心从 method superiority 转向 identity 的 prescriptive value。Claim 3 需要补充实验：要么 (a) 在更多 DGP 设置上做 cross-validated diagnostic AUC 提升 setting-level 性能，要么 (b) 承认 diagnostic 仅在 subgroup level 有效并相应缩小 claim scope。补充实验方向：找一个 EC-HTE 在 real data 上 works 的案例（需要 high accuracy LLM + balanced class），或在 exp-023 semi-synthetic-with-real-CM 设置上展示成功场景。"

  worst:
    meaning: "核心 novelty 不被认可：reviewer 认为 bias identity 是 textbook material 的 re-derivation，EC-HTE 在实际场景中 consistently 失败，整体贡献不够 EMNLP main"
    key_assumptions:
      - "Reviewer panel 包含 measurement error 专家——直接指出 Theorem 1 是 Carroll et al. (2006, Ch.4) 的 special case，'exact identity' 在该领域是 standard result，不构成 novelty"
      - "EC-HTE 在所有 real CM 实验中 fail（exp-004: inconclusive, exp-015: negative, exp-016: negative）被视为 fatal：method 在 controlled synthetic DGP 上 work 但 real-world 不 work = overfitting to simulation"
      - "A3 assumption sensitivity（exp-040: coverage breakeven at γ=0.1）被视为过于 restrictive——real LLM misclassification 几乎必然 depend on Y"
      - "K=8 boundary（exp-030: HB RMSE 2x global）和 P(Z=1)=0.18 bottleneck 被视为 method fragility evidence"
      - "Diagnostic criterion AUC=0.49 at setting level 被视为 contribution failure，不是 limitation"
      - "'Problem identification' 贡献模式本身被质疑——reviewer 认为 EMNLP main 需要 working solution 而非 warning"
    number_ranges:
      excitement: [2.0, 3.0]
      soundness: [3.0, 3.5]
      overall_recommendation: [2.5, 3.0]
      claim1_bias_identity_accepted_pct: [40, 65]
      claim2_echte_accepted_as_useful_pct: [15, 35]
      claim3_diagnostic_accepted_pct: [10, 30]
      perceived_novelty_score: [2.0, 3.0]
      major_weaknesses_per_review: [2, 3]
      revision_requests: ["reject or major revision: fundamental novelty concerns, method doesn't work on real data"]
    narrative_direction: "需要完全 reframe，但仍冲 EMNLP main。新 angle：'When Debiasing Hurts: A Large-Scale Empirical Study of Measurement Error Amplification in LLM-Annotated Causal Inference'——转型为 empirical contribution paper。核心卖点变为：(1) 14 LLM-dataset combinations × 6 models (3 generations) 的 systematic empirical evidence 证明 heterogeneous misclassification 是 structural phenomenon（R²=0.944），这是迄今最大规模的 LLM annotation error heterogeneity 实证研究；(2) bias identity 降级为 supporting theory（'consistent with classical ME theory, we verify the product-form identity holds empirically across...'），不 claim formal novelty；(3) EC-HTE 降级为 appendix-level 'one possible correction approach with known limitations'，主文 focus 转向 'what practitioners should check before applying any global correction'；(4) Diagnostic 重新 frame 为 'empirical rule of thumb'（Δπ > threshold → don't use global correction），不 claim AUC-based prediction。贡献变为 empirical discovery + practical guidelines，类似 Ribeiro et al. (2020) 'Beyond Accuracy' 的 empirical-contribution 模式。需要新增的工作：(a) 更多 real-data LLM-dataset combinations 的 Δπ 分析扩展到 20+ combos，(b) practitioner-oriented decision flowchart figure，(c) 与 calibration (exp-037) 的关系作为 practical recommendation 的核心。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "577a4d4e-c226-4556-9fcc-04bbbd2c41ac",
  "isSidechain": false,
  "requestId": "req_011CbL4Eoxn5vwzvgbHrEPUi",
  "type": "assistant",
  "uuid": "88fe1fa6-0dc9-4ead-978d-2be64ce44a2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSdbVz7QgHpsYcrDu4sz3M",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27134,
      "cache_read_input_tokens": 11841,
      "output_tokens": 5639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 5639,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 27134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27134
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
  "leafUuid": "88fe1fa6-0dc9-4ead-978d-2be64ce44a2e",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Dream scenario planning for When Debiasing Hurts",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "88fe1fa6-0dc9-4ead-978d-2be64ce44a2e",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Dream scenario planning for When Debiasing Hurts",
  "sessionId": "eb14b2bb-7025-4ead-996a-0fab8e4a37fc"
}
```

---
