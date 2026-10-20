# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：SOTA LLMs show near-homogeneous errors on standard CSS tasks; bias amplific

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/e76d227e-7e3a-40a9-a1c3-860cc1fb7bca.jsonl`
- **Structured JSON:** [`4c11db65744988bf3506.json`](../../sessions/4c/4c11db65744988bf3506.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:39:57.978Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:39:57.978Z",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：SOTA LLMs show near-homogeneous errors on standard CSS tasks; bias amplification negligible in practice; empirical relevance of the mechanism unvalidated — pivot to theoretical contribution with forward-looking framing\n核心假设：['GPT-4.1 Δπ < 0.05 across subgroups — SOTA LLMs too accurate and too uniform for heterogeneity to matter on TweetEval', 'Bias amplification <1.3x with real LLM labels — within MC noise, not practically meaningful', 'EC-HTE RMSE strictly worse than global at all realistic n_expert (≤2000) with real-LLM semi-synthetic', 'Diagnostic criterion not actionable at any aggregation level', 'UC Berkeley real data shows no meaningful CATE differences — EC-HTE and global produce essentially same estimates', 'Pilot reveals: misclassification heterogeneity is a property of task difficulty × annotator capability, and current SOTA on standard CSS is in the homogeneous regime']\n关键指标范围：{'semi_synth_llm_delta_pi': [0.01, 0.05], 'semi_synth_llm_bias_amplification_median': [1.0, 1.3], 'ec_hte_bias_reduction_pct_n500': [5, 30], 'ec_hte_rmse_ratio_n500_k4': [1.6, 2.5], 'diagnostic_cv_auc_setting': [0.45, 0.55], 'diagnostic_cv_auc_subgroup': [0.55, 0.75], 'real_data_max_cate_shift_se': [0.2, 1.0], 'coverage_ec_hte_95': [0.8, 0.9], 'ec_hte_ppci_bias_reduction_vs_ec_hte_dgpC': [10, 40]}\n叙事方向：Major reframe required — from 'solving a current practical problem' to 'identifying and formalizing a latent bias mechanism with demonstrated consequences.' Three-move pivot: (1) Lead with the exact bias identity as primary theoretical contribution — it is mathematically proven (R²=0.99/0.97) and holds regardless of current LLM quality. Frame as a structural result about measurement error × causal heterogeneity interaction that is missing from both literatures. (2) Demonstrate the mechanism's severity on controlled benchmarks: synthetic (2-3x diff-in-means, 5.9x CausalForest), injected-rate semi-synthetic (Phase A results intact). Argue magnitude scales with annotator error heterogeneity — cite Ashwin et al. 2025 showing high heterogeneity on refugee coding, cross-lingual tasks. Current SOTA LLMs on easy English CSS tasks represent a floor, not a ceiling. (3) Reframe EC-HTE from 'our method beats baselines' to 'the correct correction framework when the mechanism activates, validated under controlled conditions, available for deployment as annotation tasks grow harder.' Drop diagnostic criterion from main contributions; move to appendix as preliminary tool. Add a 'Characterizing the Homogeneity Boundary' analysis: at what Δπ does the mechanism become practically relevant? This negative-result characterization is itself a contribution. Real-data section becomes 'Audit of Current Practice': show that global and EC-HTE agree when heterogeneity is low, confirming the theory predicts when correction is (un)necessary. EMNLP fit reframed: methodological contribution to LLM-as-annotator reliability literature; the community needs to know this failure mode exists even if it is currently dormant. Target: EMNLP Findings if main conference reviewers want larger empirical effect sizes.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ec_hte_llm_annotation\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 2-3x (median across configurations), with extreme cases exceeding 20x. Global correction increases subgroup-level bias in ~50% of the parameter space.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction in moderate-sized subgroups by borrowing strength across groups (classic James-Stein shrinkage). **Boundary condition**: when expert labels per subgroup < ~25 (e.g., n_expert=50 with 12% minority subgroup → ~6 labels) AND subgroup parameter is far from group mean, shrinkage can be harmful — stratified MLE is preferred. Recommended: n_expert such that smallest subgroup contains ≥25 expert labels. **NOTE**: exact improvement magnitudes pending full 100 MC confirmation (current estimates from n_mc=2 dry-run). Demonstrated with both difference-in-means and CausalForestDML (exp-011: consistent bias reduction pattern, ec_hte_forest |bias|=0.06 vs naive 0.16). CausalForest amplifies the debiasing-hurts effect (up to 5.9x in K=4/extreme) due to nonlinear CATE estimation.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis across computational social science (CSS) — e.g., sentiment framing moderates message effectiveness, hate speech type moderates intervention impact. LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education; documented across CSS tasks including sentiment, stance, toxicity). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as \"problem identification + principled solution\" not \"new estimation technique.\"\n\n- **Headline result template**: \"On semi-synthetic CSS benchmarks (sentiment analysis, hate speech detection), global correction worsens subgroup CATE bias by 2-3x (median), with up to 20x in extreme cases; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels.\"\n\n- **Oracle framing**: When reporting DGP C results where ec_hte_ppci outperforms oracle, always use \"covariate-oracle\" (true Z + observed Y), never unqualified \"oracle\". Frame as \"composite correction is necessary and sufficient when both error types coexist\" — NOT \"beats oracle\". The result is by construction (ec_hte_ppci corrects both error types; covariate-oracle only corrects one), not surprising.\n\n## Key Contributions (ordered for paper)\n\n1. **Bias decomposition identity**: Exact population-level identity: bias ∝ misclassification heterogeneity × CATE heterogeneity (Δπ×Δτ product form). NOT a bound — it is an exact identity under A1–A4; finite-sample R² measures MC noise, not bound looseness. Includes \"debiasing can hurt\" proposition with constructive example. Frame as \"bias decomposition\" or \"bias identity\" throughout — never \"bias bound.\" (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **EC-HTE + PPCI complementarity**: EC-HTE is a structured correction exploiting mixing matrix structure for covariate-side error; PPCI rectifier is a general-purpose residual correction that captures any systematic error (including outcome-side). They are complementary, not orthogonal — PPCI alone can partially correct covariate error but less efficiently than M⁻¹; in composition, EC-HTE handles the structured covariate error precisely, and the residual rectifier handles remaining outcome error. Composition achieves best-of-both when both error types are present. Elevate in abstract and contributions list. (Method + Empirical)\n5. **Comprehensive validation**: Synthetic + semi-synthetic + real-data case study (pattern consistency, not ground-truth benchmark) with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI / DSL?\"** — PPCI rectifier is a general-purpose correction that captures any systematic error (covariate + outcome); EC-HTE is a structured correction exploiting mixing matrix structure specifically for covariate-side error. They are complementary: EC-HTE alone is more efficient for covariate error (uses M⁻¹ structure), PPCI alone can partially correct covariate error but with higher variance (limited by gold subset). In composition, EC-HTE handles structured covariate error, residual rectifier handles outcome error. DSL applied per-subgroup is a valid baseline but lacks cross-subgroup shrinkage, operates at estimand level rather than measurement model level, and has strictly higher variance under partial pooling. Do NOT say \"DSL cannot do subgroup correction\" — say it lacks the principled shrinkage mechanism.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — exp-006 provides precise RMSE crossover points: K=2/extreme n_expert=250, K=4/extreme n=1000, K=4/moderate n=2000, K=2/moderate never crosses (global always better on RMSE). Paper needs \"Expert Budget Recommendation\" subsection with per-K guidelines. Key message: when diagnostic criterion flags high heterogeneity (extreme regime), EC-HTE is worth the investment at moderate budgets; when heterogeneity is low, global correction is the safer choice. This honest framing connects Claim 2 (EC-HTE method) to Claim 3 (diagnostic criterion) — the diagnostic decides the correction strategy.\n\n6. **\"How does this differ from Carroll et al. (2006) / classical measurement error?\"** — The qualitative insight that misspecified corrections can amplify MSE is classical (Fuller 1987, Sec. 2.3). Our specific contributions beyond this are: (a) the quantitative Δπ×Δτ product form for CATE estimation with effect-modifier misclassification, (b) demonstrating this failure mode occurs *by default* in standard LLM annotation workflows, and (c) providing a computable diagnostic and correction framework. Must explicitly cite and contextualize: Fuller (1987), Carroll et al. (2006 Ch. 4), Gustafson (2003), Hu & Schennach (2008), Imai & Yamamoto (2010). Also cite Bayesian annotation models: Dawid & Skene, Passonneau & Carpenter (2014), Hovy et al. (2013). **Bibliography target: 30-35 references** spanning measurement error, Bayesian estimation, causal inference, LLM-as-annotator (Tornberg 2024, Gilardi et al. 2023, Ziems et al. 2024), HTE methods (Wager & Athey 2018, Kennedy 2023, Chernozhukov et al. 2018).\n\n7. **\"Methodological novelty is modest\"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. HB partial pooling provides meaningful RMSE reduction for moderate subgroups but is NOT \"never worse than global\" — it is a James-Stein shrinkage estimator with known boundary conditions. **Recommended condition**: n_expert per subgroup ≥ ~25 (e.g., n_expert ≥ 100 for K=4 with 12% minority). Below this, stratified MLE is preferred. This honest limitation strengthens credibility. State conditions explicitly using per-subgroup formulation, not just total n_expert.\n\n8. **\"Why no figures?\"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use cases (sentiment analysis, hate speech detection, refugee interview coding), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track. **NOTE**: Framing broadened from \"political-science\" to \"CSS\" (D004b) — TweetEval stance tasks too small (N<1000), sentiment (N=45K) usable but not political science. CSS is more accurate and equally strong for EMNLP.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n## Writing Requirements (Dream Round 2 consensus)\n\n1. **\"Bias decomposition\" NOT \"bias bound\"** — Theorem 1 is an exact identity at population level. R² < 1.0 in verification reflects finite-sample MC noise, not bound looseness.\n2. **Bibliography: 30-35 references minimum** — Must span 5 literatures: classical measurement error, Bayesian estimation, causal inference, LLM-as-annotator, CSS. Critical citations: Fuller 1987, Wager & Athey 2018, Imai & Yamamoto 2010.\n3. **3+ figures in main text** — (a) bias mechanism schematic, (b) Δπ×Δτ amplification heatmap, (c) diagnostic ROC curve, (d) budget crossover curves. Move exp-008/exp-009 tables to appendix.\n4. **Semi-synthetic DGP fully specified** — outcome generation, treatment assignment, CATE injection mechanism.\n5. **Real-data framed as pattern consistency** — NOT ground-truth benchmark. No bias/RMSE against unknown true CATEs.\n6. **EC-HTE advantage is conditional, not universal** — ec_hte dominates when misclassification heterogeneity is high (extreme regime) OR n_expert is large (≥500). In moderate regime with small n_expert (~100), global correction can outperform ec_hte because per-subgroup CM estimation noise exceeds the benefit of stratification. This connects to Claim 3: the diagnostic criterion (Δπ×Δτ) predicts when EC-HTE is needed. Unified condition: n_expert/K ≥ ~25-50 experts per subgroup.\n11. **RMSE tradeoff must be disclosed** — ec_hte has higher RMSE than global/naive in K=4/n≤100 configs (up to 3.5x in extreme cases) due to noisy per-subgroup CM estimation. Bias is lower but variance is higher. Must report both bias AND RMSE; include bias-RMSE tradeoff analysis. At n_expert≥500, ec_hte RMSE becomes competitive.\n12. **K-dependence of debiasing-hurts** — K=2 extreme magnification ~2.7x; K=4 extreme ~5.9x. More subgroups → larger π heterogeneity → more severe global correction damage. Report this scaling.\n7. **Confusion matrix invertibility** — State det(Ĉ_k) ≠ 0 assumption explicitly.\n8. **Diagnostic AUC cross-validated** — Leave-one-setting-out or held-out evaluation, not in-sample.\n9. **Hyperprior values stated + sensitivity analysis** — Gamma(α, β) for Dirichlet concentration; report sensitivity to 2× changes.\n10. **PPCI complementarity elevated** — Highlight in abstract and contributions. Frame as \"complementary\" not \"orthogonal\": EC-HTE is structured covariate-error correction; PPCI rectifier is general residual correction. Composition = EC-HTE handles structured part + rectifier handles remainder (primarily outcome error).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2. MUST report full MCMC diagnostics: sampler (PyMC\n    NUTS), chains (≥4), warmup (≥1000), R̂ (<1.01), ESS (>200), runtime vs MLE. Report\n    SEs/CIs for all metrics from MC runs. Monitor coverage calibration — if systematic\n    undercoverage, diagnose cause.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example. MUST include K>2 extension: verify bias formula empirically for K=4 subgroups;\n    add Remark after Proposition 1 discussing general-K case (sum-of-products form).\n    Report R² of analytic prediction vs MC, bound tightness ratio, and CIs on all\n    bias estimates.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim: 1,2,3\n  description: 'Semi-synthetic benchmark: use real CSS tweet corpus — TweetEval sentiment\n    (N=45K, primary) for exp-003. Framing broadened from ''political-science'' to\n    ''CSS'' per D004b (stance tasks N<1000 unusable). Inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 (API) and optionally Qwen3-235B-A22B (GPU), measure\n    subgroup-specific misclassification rates, apply EC-HTE vs baselines. Subgroup\n    variables: text features (has_hashtag, text_length) for semi-synthetic; demographic\n    subgroups reserved for exp-004. MUST fully specify DGP in paper: (a) outcome generation\n    model, (b) treatment assignment mechanism, (c) how true CATEs are injected. MUST\n    run LLM annotation pilot (~1000 samples) before committing to verify per-subgroup\n    misclassification heterogeneity exists.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim: 1,2\n  description: 'Real-data case study (pattern consistency, NOT ground-truth validation):\n    apply EC-HTE to real CSS dataset with subgroup-varying LLM misclassification.\n    Show: (a) global vs EC-HTE produce qualitatively different CATE distributions,\n    (b) EC-HTE results consistent with domain knowledge (demographic effect direction),\n    (c) bootstrap CIs on point estimate differences. Frame as ''illustrative application''\n    not ''ground-truth benchmark''. Reviewer confirmed: real data has no ground truth\n    CATE, CV-based ground truth is circular. PRIMARY: UC Berkeley Measuring Hate Speech\n    corpus (public, rich demographic subgroups). NICE-TO-HAVE: Ashwin et al. (2025)\n    if obtainable (requires author email + IRB, not feasible within 5-day DDL).'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference) or API\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: UC Berkeley dataset causal framework (T,Y,Z,S) mapping needs design\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold. MUST use\n    cross-validation or held-out evaluation (NOT in-sample AUC on own experiments).\n    Dream Round 2 flagged in-sample AUC as methodological weakness across best and\n    median tiers.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1,2\n  description: 'PPCI + DSL baseline comparison: (a) PPCI kernel-based conditional\n    correction vs EC-HTE on covariate-side vs outcome-side error; (b) per-subgroup\n    DSL as additional baseline (DSL applied independently per subgroup, no cross-subgroup\n    shrinkage — shows EC-HTE''s partial pooling advantage); (c) EC-HTE+PPCI composition\n    for simultaneous covariate+outcome error; (d) CRITICAL: include ''pure covariate-error,\n    zero outcome-error'' control condition to demonstrate EC-HTE advantage when covariate-side\n    error dominates (PPCI should be ineffective here). Paper framing: DSL per-subgroup\n    is a valid baseline but lacks cross-subgroup shrinkage and operates at estimand\n    level rather than measurement model level.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest integration: apply EC-HTE post-hoc correction to CausalForestDML\n    subgroup CATE estimates + leaf-level corrected pseudo-outcomes with variance-adjusted\n    CIs. Compare against naive forest and globally-corrected forest. ELEVATED TO P0:\n    Claim 2 explicitly states CausalForestDML but no experiment validates this — claim-evidence\n    gap is reviewer killshot.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mcmc_rhat_max: 1.024\n    mcmc_ess_min: 129\n    mcmc_divergent: 0\n    runtime_min: 69\n    total_mc_runs: 3600\n    hb_vs_mle_rmse_improvement_k2_n50: 4-9%\n    hb_vs_mle_rmse_improvement_k2_n100: 1-2%\n    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%\n    hb_coverage_min: 0.87\n    hb_coverage_median: 0.93\n    k4_extreme_n50_blowup: false\n    k4_extreme_n50_blowup_note: Fixed by singularity guard + 4-chain MCMC\n    mcmc_fix_4chain:\n      rhat_max_all_configs: 1.0034\n      ess_min_all_configs: 1618\n      ess_improvement: ~4x vs 2-chain\n      k4_extreme_n50_A_rmse_z0: 3.14 → 0.99\n      k4_extreme_n50_B_rmse_z0: 509.93 → 0.27\n      k4_extreme_n100_A_rmse_z0: 11.57 → 0.29\n      singularity_guard_triggers: extreme/n=50 only (2 HB, 3 MLE / 100 runs)\n      results_file: results/exp001_hb_results_v2.csv\n    hyperprior_sensitivity:\n      scale_range: 0.5-2.0\n      k2_rmse_variation: <1%\n      k4_rmse_variation: ~4-5%\n      coverage_invariant: true\n      conclusion: robust\n      results_file: results/exp001_hyperprior_sensitivity.csv\n- exp_id: exp-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r2_k2: 0.9939\n    r2_k4: 0.9738\n    tightness_ratio_k2_median: 1.0027\n    tightness_ratio_k4_median: 1.0234\n    debiasing_hurts_pct: 50\n    debiasing_hurts_pct_note: 260/520 (excluding dc=0 rows where bias=0)\n    debiasing_hurts_threshold_delta_misclass: 0.1235\n    max_bias_ratio_k2: 2.86\n    max_bias_ratio_k4: 2.41\n    coverage_2se_k2: 0.951\n    coverage_2se_k4: 0.94\n- exp_id: exp-007\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_rows: 6912\n    dgps:\n    - A_covariate_only\n    - B_outcome_only\n    - C_both_errors\n    - D_no_error\n    methods: 8\n    mc_runs: 100\n    double_correction_fix_verified: true\n    dgp_a_ec_hte_ppci_equals_ec_hte: true\n    dgp_c_extreme_n250_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.225\n      ec_hte_bias_z0: 0.178\n      ec_hte_rmse_z0: 0.226\n      ppci_bias_z0: 0.004\n      ppci_rmse_z0: 0.261\n      naive_bias_z0: 0.251\n      naive_rmse_z0: 0.269\n    dgp_c_n500_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.142\n      ec_hte_bias_z0: 0.088\n      ec_hte_rmse_z0: 0.134\n    key_finding: ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better\n      than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.\n- exp_id: exp-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase: A_semi_synthetic\n    n_subgroups: 4\n    misclass_rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25\n    subgroup_sizes: S0~38%, S1~38%, S2~12%, S3~12%\n    p_z1_actual: 0.39\n    debiasing_hurts_confirmed: true\n    mc_runs: 100\n    v3_hb_integration:\n      methods:\n      - oracle\n      - naive\n      - global_corrected\n      - stratified_mle\n      - hb_ec_hte\n      hb_vs_mle_summary:\n        S2_n50_rmse_z0_improvement: +21.4%\n        S2_n100_rmse_z0_improvement: +39.5%\n        S3_n50_blowup: RMSE 345-804% worse\n        convergence_at_n250: < 5% difference\n        S0_n50_extreme_rmse_z0_improvement: +88%\n      key_finding: HB partial pooling helps mid-misclass subgroups (S2) at small n_expert\n        but blows up in extreme-misclass tiny subgroups (S3 at n=50). Converges to\n        MLE at n>=250.\n      hypothesis_verdict: partially_validated\n    results_file_v3: results/exp003_phase_a_v3.csv\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subgroup_level_auc: 0.833\n    subgroup_correlation: 0.86\n    setting_level_auc: 0.49\n    low_pi_hurt_pct: 84.6\n    high_pi_hurt_pct: 15.4\n    theory_alignment: consistent with exp-002 formula\n- exp_id: exp-011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    n_configs: 8\n    total_rows: 144\n    runtime_min: 35\n    methods:\n    - naive_forest\n    - global_forest\n    - ec_hte_forest\n    mean_abs_bias:\n      naive_forest: 0.1558\n      global_forest: 0.1073\n      ec_hte_forest: 0.0608\n    mean_rmse:\n      naive_forest: 0.1782\n      global_forest: 0.1659\n      ec_hte_forest: 0.2289\n    debiasing_hurts_cases: 9\n    debiasing_hurts_max_ratio: 5.9\n    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'\n    k2_n500_ec_hte_bias_range: 0.004-0.013 (near zero)\n    k2_n500_global_bias_range: 0.033-0.109 (still biased)\n    pattern_consistent_with_diff_in_means: true\n    claim2_validated: true\n- exp_id: exp-006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    total_rows: 288\n    runtime_min: 110\n    grid: n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]\n    crossover_hb_beats_global:\n      K2_extreme: 250\n      K2_moderate: never\n      K4_extreme: 1000\n      K4_moderate: 2000\n    hb_vs_mle: HB ≥ MLE in 22/24 configs (partial pooling never significantly hurts\n      in symmetric DGP)\n    hb_best_improvement_over_mle:\n      K4_moderate_n50_sgC: +42.4% RMSE\n      K4_extreme_n50_sgC: +23.4% RMSE\n      K4_moderate_n50_sgB: +24.0% RMSE\n    convergence: HB ≈ MLE at n≥1000 (<0.5% difference)\n    key_finding: 'Crossover depends strongly on K and regime. K=2: crossover at n=250\n      (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest\n      improvement over MLE via partial pooling.'\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:39:57.985Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:39:57.985Z",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T03:39:58.025Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：SOTA LLMs show near-homogeneous errors on standard CSS tasks; bias amplification negligible in practice; empirical relevance of the mechanism unvalidated — pivot to theoretical contribution with forward-looking framing
核心假设：['GPT-4.1 Δπ < 0.05 across subgroups — SOTA LLMs too accurate and too uniform for heterogeneity to matter on TweetEval', 'Bias amplification <1.3x with real LLM labels — within MC noise, not practically meaningful', 'EC-HTE RMSE strictly worse than global at all realistic n_expert (≤2000) with real-LLM semi-synthetic', 'Diagnostic criterion not actionable at any aggregation level', 'UC Berkeley real data shows no meaningful CATE differences — EC-HTE and global produce essentially same estimates', 'Pilot reveals: misclassification heterogeneity is a property of task difficulty × annotator capability, and current SOTA on standard CSS is in the homogeneous regime']
关键指标范围：{'semi_synth_llm_delta_pi': [0.01, 0.05], 'semi_synth_llm_bias_amplification_median': [1.0, 1.3], 'ec_hte_bias_reduction_pct_n500': [5, 30], 'ec_hte_rmse_ratio_n500_k4': [1.6, 2.5], 'diagnostic_cv_auc_setting': [0.45, 0.55], 'diagnostic_cv_auc_subgroup': [0.55, 0.75], 'real_data_max_cate_shift_se': [0.2, 1.0], 'coverage_ec_hte_95': [0.8, 0.9], 'ec_hte_ppci_bias_reduction_vs_ec_hte_dgpC': [10, 40]}
叙事方向：Major reframe required — from 'solving a current practical problem' to 'identifying and formalizing a latent bias mechanism with demonstrated consequences.' Three-move pivot: (1) Lead with the exact bias identity as primary theoretical contribution — it is mathematically proven (R²=0.99/0.97) and holds regardless of current LLM quality. Frame as a structural result about measurement error × causal heterogeneity interaction that is missing from both literatures. (2) Demonstrate the mechanism's severity on controlled benchmarks: synthetic (2-3x diff-in-means, 5.9x CausalForest), injected-rate semi-synthetic (Phase A results intact). Argue magnitude scales with annotator error heterogeneity — cite Ashwin et al. 2025 showing high heterogeneity on refugee coding, cross-lingual tasks. Current SOTA LLMs on easy English CSS tasks represent a floor, not a ceiling. (3) Reframe EC-HTE from 'our method beats baselines' to 'the correct correction framework when the mechanism activates, validated under controlled conditions, available for deployment as annotation tasks grow harder.' Drop diagnostic criterion from main contributions; move to appendix as preliminary tool. Add a 'Characterizing the Homogeneity Boundary' analysis: at what Δπ does the mechanism become practically relevant? This negative-result characterization is itself a contribution. Real-data section becomes 'Audit of Current Practice': show that global and EC-HTE agree when heterogeneity is low, confirming the theory predicts when correction is (un)necessary. EMNLP fit reframed: methodological contribution to LLM-as-annotator reliability literature; the community needs to know this failure mode exists even if it is currently dormant. Target: EMNLP Findings if main conference reviewers want larger empirical effect sizes.

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
tier: worst
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
  "promptId": "56f4d37e-090c-44ac-83e3-89f606d98ab6",
  "type": "user",
  "uuid": "9a9618d6-6584-43c4-9db4-663df4ee8e87",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:39:58.022Z_

```json
{
  "parentUuid": "9a9618d6-6584-43c4-9db4-663df4ee8e87",
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
  "uuid": "35dd148c-e535-443d-b4bf-cb413a16b098",
  "timestamp": "2026-05-21T03:39:58.022Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:39:58.022Z_

```json
{
  "parentUuid": "35dd148c-e535-443d-b4bf-cb413a16b098",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "89d20ca6-258e-4063-b9b2-4fc9f298d5ff",
  "timestamp": "2026-05-21T03:39:58.022Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SOTA LLMs show near-homogeneous errors on standard CSS tasks; bias amplification negligible in practice; empirical relevance of the mechanism unvalidated…",
  "leafUuid": "89d20ca6-258e-4063-b9b2-4fc9f298d5ff",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "SOTA LLM homogeneity and mechanism validation under worst-case",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca"
}
```

---

### Assistant

_source line 8 · 2026-05-21T03:40:29.572Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for all "planned" experiments in the experiment plan, under the "worst" tier scenario. Let me identify which experiments are still "planned" (not done):

Looking at the registry, completed experiments are: exp-001, exp-002, exp-003, exp-005, exp-006, exp-007, exp-011.

Planned experiments remaining: exp-004, exp-008, exp-009, exp-010.

Wait, let me re-check. The experiment_plan lists statuses:


There's a discrepancy between the experiment plan and the registry — most experiments show as "planned" in the plan but are marked "DONE" in the registry. The truly planned experiments that haven't been executed yet are exp-004, exp-008, exp-009, and exp-010.

The user is asking for detailed data on each planned experiment, but since the experiment_plan lists everything as "planned" while the registry shows most are already complete, I think they want me to generate predicted results specifically for the experiments that are still actually pending: exp-004, exp-008, exp-009, and exp-010.

For the "worst" tier classification, I'm considering what it means when experiments show minimal practical impact — where state-of-the-art models perform similarly across different conditions, bias effects are negligible, and the proposed mechanisms don't produce meaningful real-world differences in performance or heterogeneous treatment effects.

Now I'm looking at the specific metric ranges that define this worst tier across different evaluation dimensions.

For the remaining experiments, I need to map out what failure looks like. In the UC Berkeley hate speech study, the worst case is when EC-HTE can't identify meaningful CATE differences because the LLM errors are too uniform across demographic groups—point estimates barely shift beyond measurement noise. Similarly, when comparing multiple LLMs on sentiment classification, the worst scenario is that all three models perform equally poorly and homogeneously, so EC-HTE offers no advantage over a simpler global approach.

With adaptive expert allocation, homogeneous misclassification means the method can't identify which subgroups actually need more annotation effort, collapsing the theoretical benefit. And for robustness to subgroup misspecification, if EC-HTE is already underperforming in most configurations, adding noise to the subgroup structure just makes the per-subgroup confusion matrix estimates even noisier and less reliable.

Now I'm formatting these worst-case scenarios into YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89d20ca6-258e-4063-b9b2-4fc9f298d5ff",
  "isSidechain": false,
  "requestId": "req_011CbF25Esx3Wk5hH4q67ijn",
  "type": "assistant",
  "uuid": "80fee215-6fb3-4a89-922e-9fc7249bf3f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AabA42oegfkqPQe7vmLn5x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14801,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8763,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14801
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

_source line 9 · 2026-05-21T03:42:42.497Z_

```yaml
tier: worst
narrative_guidance: >
  Major reframe required — from 'solving a current practical problem' to 'identifying and formalizing
  a latent bias mechanism with demonstrated consequences.' Three-move pivot: (1) Lead with bias identity
  as primary theoretical contribution (R²=0.99/0.97, holds regardless of LLM quality). (2) Demonstrate
  mechanism severity on controlled benchmarks (synthetic 2-3x, CausalForest 5.9x); argue magnitude
  scales with annotator error heterogeneity — current SOTA on easy English CSS is a floor, not a ceiling.
  (3) Reframe EC-HTE as 'correct correction framework when mechanism activates.' Drop diagnostic from
  main contributions → appendix. Add 'Characterizing the Homogeneity Boundary' analysis. Real-data
  section becomes 'Audit of Current Practice' confirming theory predicts when correction is unnecessary.
  Target: EMNLP Findings.

imagined_experiments:
  - name: "Real-data case study — UC Berkeley Measuring Hate Speech"
    plan_id: "exp-004"
    description: >
      Apply EC-HTE to UC Berkeley hate speech corpus with demographic subgroups (race, gender, age,
      education). Annotate with GPT-4.1 via API. Compare global-corrected vs EC-HTE CATE estimates.
      Frame as 'Audit of Current Practice' — show that when LLM errors are homogeneous, global and
      EC-HTE converge, confirming theory predicts when correction is (un)necessary.
    expected_results:
      llm_overall_accuracy: 0.82
      llm_delta_pi_max_across_demographic_subgroups: 0.03
      llm_delta_pi_race: 0.02
      llm_delta_pi_gender: 0.01
      llm_delta_pi_age: 0.04
      llm_delta_pi_education: 0.03
      global_vs_ec_hte_max_cate_shift_abs: 0.018
      global_vs_ec_hte_max_cate_shift_se: 0.35
      global_vs_ec_hte_mean_cate_shift_se: 0.18
      num_subgroups_shift_exceeds_1se: 0
      num_subgroups_shift_exceeds_0_5se: 1
      ec_hte_vs_global_qualitative_agreement: true
      bootstrap_ci_overlap_pct: 100
      domain_knowledge_consistency: "both methods agree on direction of demographic effects"
      expert_labels_used: 500
      n_total_llm_annotated: 39565
    result_rationale: >
      GPT-4.1 achieves uniformly high accuracy on English hate speech classification — a well-studied
      CSS task with abundant training data. Demographic subgroups (race, gender, age, education of
      annotator or target) produce Δπ ≤ 0.04, well below the threshold where the bias mechanism
      becomes practically relevant. With near-homogeneous confusion matrices across subgroups, the
      global pooled CM is an adequate approximation of each subgroup CM, so global correction and
      EC-HTE produce statistically indistinguishable CATE estimates. All point estimate shifts fall
      within 0.35 SE — not actionable. This is exactly the prediction of the bias identity: when
      Δπ ≈ 0, bias ∝ Δπ×Δτ ≈ 0 regardless of CATE heterogeneity. The result is a negative finding
      for practical relevance but a positive finding for theory validation — the framework correctly
      identifies the homogeneous regime as safe for global correction.
    tables:
      - name: "Table: Real-Data CATE Estimates by Demographic Subgroup"
        columns: [subgroup, n, pi_hat_global, pi_hat_subgroup, cate_naive, cate_global, cate_ec_hte, shift_se, bootstrap_95ci_overlap]
        rows:
          - [race_white, 18200, 0.17, 0.16, 0.031, 0.028, 0.027, 0.15, yes]
          - [race_nonwhite, 21365, 0.17, 0.18, 0.044, 0.040, 0.041, 0.22, yes]
          - [gender_male, 20100, 0.17, 0.17, 0.039, 0.035, 0.035, 0.05, yes]
          - [gender_female, 19465, 0.17, 0.18, 0.036, 0.033, 0.034, 0.18, yes]
          - [age_under30, 15800, 0.17, 0.16, 0.042, 0.038, 0.037, 0.20, yes]
          - [age_30plus, 23765, 0.17, 0.19, 0.033, 0.030, 0.031, 0.28, yes]
          - [edu_college, 22100, 0.17, 0.17, 0.037, 0.034, 0.034, 0.08, yes]
          - [edu_no_college, 17465, 0.17, 0.20, 0.038, 0.034, 0.036, 0.35, yes]
      - name: "Table: Misclassification Heterogeneity Summary"
        columns: [demographic_dimension, n_subgroups, max_delta_pi, min_pi, max_pi, heterogeneity_regime]
        rows:
          - [race, 2, 0.02, 0.16, 0.18, homogeneous]
          - [gender, 2, 0.01, 0.17, 0.18, homogeneous]
          - [age, 2, 0.04, 0.16, 0.19, homogeneous]
          - [education, 2, 0.03, 0.17, 0.20, homogeneous]
    figures_description:
      - "Scatter plot: global-corrected CATE vs EC-HTE CATE per subgroup, with 45-degree reference line
         and bootstrap CIs. All points cluster tightly around the identity line (max deviation 0.35 SE),
         visually confirming no meaningful divergence. Annotate each point with demographic label."
      - "Bar chart: per-subgroup misclassification rate (pi_hat) with 95% CI error bars, grouped by
         demographic dimension. All bars overlap substantially, visualizing the homogeneous error regime.
         Horizontal dashed line at global pooled rate."
    analysis: >
      The real-data audit confirms the worst-tier prediction: on a well-studied English CSS task,
      SOTA LLMs produce near-homogeneous errors across demographic subgroups (max Δπ = 0.04 for age).
      Consequently, global and EC-HTE CATE estimates are statistically indistinguishable — the largest
      shift is 0.35 SE (education dimension), with 100% bootstrap CI overlap across all subgroups.
      This result has TWO interpretations for the paper: (1) Negative: EC-HTE provides no practical
      benefit on this dataset, undermining claims of immediate applicability. (2) Positive (reframed):
      The theory correctly predicts that correction is unnecessary when Δπ ≈ 0, validating the
      diagnostic framework. Frame as 'the bias identity correctly identifies the homogeneous regime.'
      Causal framework mapping: T = exposure to hate speech content, Y = perceived severity rating,
      Z = hate speech type (LLM-classified), S = demographic subgroup. Note limitation: causal
      interpretation is illustrative, not designed for rigorous causal inference on this observational
      corpus. CRITICAL PIVOT: use this result to motivate the 'Characterizing the Homogeneity Boundary'
      analysis — at what Δπ does the mechanism activate? Back-calculate from the bias identity:
      for bias > 0.05 (practical threshold), need Δπ > ~0.12 given observed Δτ. This characterization
      is itself a contribution — it tells practitioners when to worry.

  - name: "Multiple LLM annotator comparison"
    plan_id: "exp-008"
    description: >
      Annotate TweetEval sentiment with GPT-4.1 (API), Qwen3-235B-A22B (GPU), and Claude Sonnet 4.6
      (API). Measure per-subgroup misclassification rates for each LLM. Compare EC-HTE benefit
      across LLMs of different quality tiers.
    expected_results:
      gpt4_1_overall_accuracy: 0.88
      gpt4_1_delta_pi_max: 0.03
      gpt4_1_bias_amplification_median: 1.08
      qwen3_overall_accuracy: 0.81
      qwen3_delta_pi_max: 0.05
      qwen3_bias_amplification_median: 1.22
      claude_sonnet_overall_accuracy: 0.86
      claude_sonnet_delta_pi_max: 0.04
      claude_sonnet_bias_amplification_median: 1.14
      ec_hte_rmse_ratio_vs_global_gpt4_1_n500_k4: 2.1
      ec_hte_rmse_ratio_vs_global_qwen3_n500_k4: 1.7
      ec_hte_rmse_ratio_vs_global_claude_n500_k4: 1.9
      ec_hte_bias_reduction_pct_gpt4_1: 8
      ec_hte_bias_reduction_pct_qwen3: 22
      ec_hte_bias_reduction_pct_claude: 14
      all_llms_homogeneous_regime: true
      n_samples_annotated_per_llm: 5000
      annotation_cost_gpt4_1_usd: 12
      annotation_cost_claude_usd: 18
      gpu_hours_qwen3: 8
    result_rationale: >
      All three SOTA LLMs achieve high accuracy on TweetEval sentiment (a 3-class task with
      well-defined categories: positive/negative/neutral). English sentiment is among the easiest CSS
      tasks — abundant training data, clear label semantics, minimal cultural ambiguity. GPT-4.1 leads
      (0.88 accuracy) with the smallest Δπ (0.03); Qwen3 is weakest (0.81) with slightly larger
      Δπ (0.05) because its English performance lags frontier models, but 0.05 is still in the
      homogeneous regime per the bias identity. Claude Sonnet falls between. All three LLMs produce
      Δπ < 0.05, confirming the worst-tier assumption that SOTA LLMs on standard English CSS tasks
      are 'too accurate and too uniform for heterogeneity to matter.' Bias amplification ranges
      1.08–1.22x — within MC noise, not practically meaningful. EC-HTE has strictly worse RMSE than
      global for all three LLMs at n_expert ≤ 2000 because the per-subgroup CM estimation variance
      exceeds the (tiny) bias reduction. Even the weakest LLM (Qwen3) only shows 22% bias reduction
      with 1.7x RMSE penalty — a bad tradeoff. This result means the 'LLM quality spectrum' story
      partially collapses: the spectrum exists but is compressed into a narrow band where EC-HTE
      is never the right choice on this task.
    tables:
      - name: "Table: LLM Comparison — Misclassification Heterogeneity"
        columns: [llm, accuracy, delta_pi_max, subgroup_with_max_delta, bias_amp_median, bias_amp_max, regime]
        rows:
          - [GPT-4.1, 0.88, 0.03, has_hashtag, 1.08, 1.15, homogeneous]
          - [Qwen3-235B, 0.81, 0.05, short_text, 1.22, 1.29, homogeneous]
          - [Claude-Sonnet-4.6, 0.86, 0.04, has_hashtag, 1.14, 1.21, homogeneous]
      - name: "Table: EC-HTE vs Global by LLM (n_expert=500, K=4)"
        columns: [llm, method, mean_abs_bias, rmse, coverage_95, bias_reduction_pct, rmse_ratio_vs_global]
        rows:
          - [GPT-4.1, global, 0.012, 0.089, 0.94, "-", 1.0]
          - [GPT-4.1, ec_hte, 0.011, 0.187, 0.86, 8, 2.1]
          - [Qwen3-235B, global, 0.028, 0.095, 0.92, "-", 1.0]
          - [Qwen3-235B, ec_hte, 0.022, 0.162, 0.84, 22, 1.7]
          - [Claude-Sonnet-4.6, global, 0.019, 0.091, 0.93, "-", 1.0]
          - [Claude-Sonnet-4.6, ec_hte, 0.016, 0.173, 0.85, 14, 1.9]
    figures_description:
      - "Grouped bar chart: Δπ_max per LLM with 95% CI. All bars below 0.05 dashed threshold line.
         Shows compressed quality spectrum — even the weakest LLM (Qwen3) has near-homogeneous errors."
      - "Bias-RMSE tradeoff scatter: one point per (LLM × method). EC-HTE points are lower-bias but
         much higher-RMSE than global points. Pareto frontier dominated by global correction for all
         three LLMs. Annotate with LLM name."
    analysis: >
      The multi-LLM comparison reveals a compressed quality spectrum on TweetEval sentiment: even the
      weakest model (Qwen3, 0.81 accuracy) achieves Δπ_max = 0.05, barely above the homogeneity
      floor. This confirms the worst-tier hypothesis that standard English CSS tasks are 'solved enough'
      that misclassification heterogeneity is negligible. EC-HTE never dominates global on RMSE for any
      LLM. The reframing implication: move this table to appendix, use it to support the 'current SOTA
      is in the homogeneous regime' argument. The key forward-looking claim becomes: as researchers
      apply LLMs to harder tasks (cross-lingual, low-resource, domain-specialized coding — per Ashwin
      et al. 2025), Δπ will increase and the mechanism will activate. The multi-LLM comparison shows
      the mechanism is 'dormant' on easy tasks, not 'absent' — Qwen3's slightly higher Δπ hints at the
      direction of the gradient.

  - name: "Adaptive expert annotation allocation"
    plan_id: "exp-009"
    description: >
      Implement CATE-weighted allocation targeting high-CATE × high-error subgroups. Compare against
      uniform and uncertainty-only allocation on synthetic data (where mechanism is active) and
      semi-synthetic with real LLM annotations (where mechanism is dormant).
    expected_results:
      # Synthetic (mechanism active — extreme regime)
      synth_extreme_adaptive_vs_uniform_rmse_reduction_k2: 0.18
      synth_extreme_adaptive_vs_uniform_rmse_reduction_k4: 0.24
      synth_extreme_adaptive_vs_uncertainty_rmse_reduction_k4: 0.09
      synth_extreme_optimal_allocation_ratio_high_error_sg: 2.8
      # Semi-synthetic with real LLM (mechanism dormant)
      semi_synth_llm_adaptive_vs_uniform_rmse_reduction_k4: 0.02
      semi_synth_llm_adaptive_vs_uniform_bias_reduction: 0.003
      semi_synth_llm_allocation_entropy: 0.97
      # Practical metrics
      convergence_iterations: 3
      allocation_stability_across_seeds: 0.91
      n_expert_total: 500
    result_rationale: >
      On synthetic data where Δπ is large (extreme regime), adaptive allocation works as designed:
      directing more expert labels to high-error × high-CATE subgroups reduces RMSE by 18-24%
      over uniform allocation because those subgroups have the most to gain from better CM estimation.
      However, on semi-synthetic with real LLM annotations (worst-tier: Δπ < 0.05), adaptive allocation
      degenerates to near-uniform (allocation entropy 0.97 vs 1.0 for perfect uniform) because all
      subgroups have similarly low error rates and similarly uncertain CATEs. The CATE-weighting signal
      is dominated by estimation noise when true Δπ is small, so the algorithm cannot reliably identify
      which subgroups benefit most. RMSE improvement is 2% — within MC noise. This makes adaptive
      allocation a theoretically valid but practically irrelevant contribution under worst-tier
      conditions. Recommendation: present synthetic results in appendix as proof-of-concept; do not
      feature in main text.
    tables:
      - name: "Table: Allocation Strategy Comparison (K=4, n_expert=500)"
        columns: [data_source, allocation, mean_abs_bias, rmse, bias_vs_uniform_pct, rmse_vs_uniform_pct]
        rows:
          - [synthetic_extreme, uniform, 0.062, 0.198, 0, 0]
          - [synthetic_extreme, uncertainty_only, 0.055, 0.178, -11, -10]
          - [synthetic_extreme, cate_weighted, 0.048, 0.151, -23, -24]
          - [synthetic_moderate, uniform, 0.031, 0.145, 0, 0]
          - [synthetic_moderate, cate_weighted, 0.027, 0.131, -13, -10]
          - [semi_synth_llm, uniform, 0.018, 0.142, 0, 0]
          - [semi_synth_llm, cate_weighted, 0.017, 0.139, -6, -2]
      - name: "Table: Allocation Weights by Subgroup (K=4, n_expert=500)"
        columns: [data_source, subgroup, true_pi, true_cate, uniform_weight, adaptive_weight]
        rows:
          - [synthetic_extreme, S0, 0.05, 0.10, 0.25, 0.12]
          - [synthetic_extreme, S1, 0.10, 0.10, 0.25, 0.18]
          - [synthetic_extreme, S2, 0.20, 0.30, 0.25, 0.28]
          - [synthetic_extreme, S3, 0.30, 0.30, 0.25, 0.42]
          - [semi_synth_llm, S0, 0.12, 0.10, 0.25, 0.24]
          - [semi_synth_llm, S1, 0.13, 0.10, 0.25, 0.25]
          - [semi_synth_llm, S2, 0.14, 0.30, 0.25, 0.26]
          - [semi_synth_llm, S3, 0.15, 0.30, 0.25, 0.25]
    figures_description:
      - "Heatmap: allocation weight matrix (subgroup × strategy) for synthetic extreme vs semi-synthetic
         LLM. Synthetic shows clear concentration toward high-error subgroups; semi-synthetic shows
         near-uniform — visually demonstrates the mechanism's dormancy collapsing the allocation signal."
    analysis: >
      Adaptive allocation is a Stage 3 / P2 experiment that, under worst-tier conditions, provides
      negligible empirical value with real LLM annotations. The fundamental issue: when Δπ is small,
      the signal that should guide allocation (error rate × CATE magnitude) is buried in estimation
      noise. The algorithm converges in 3 iterations but converges to near-uniform because it correctly
      identifies that no subgroup has substantially more to gain. For the paper reframe: mention
      adaptive allocation as a theoretical extension in the Discussion section ('when the mechanism
      activates, practitioners can further optimize expert budget allocation'). Do not include in
      main experimental results. Synthetic proof-of-concept in appendix is sufficient.

  - name: "Robustness to misspecified subgroup structure"
    plan_id: "exp-010"
    description: >
      Test EC-HTE when subgroup definitions are noisy (random 10-30% mislabeling of subgroup
      membership), overlapping (soft subgroup assignment), or when the true DGP has a different
      subgroup structure than the conditioning variable used by EC-HTE.
    expected_results:
      # Subgroup label noise (synthetic extreme, n_expert=500, K=4)
      noise_10pct_ec_hte_rmse_ratio_vs_clean: 1.12
      noise_20pct_ec_hte_rmse_ratio_vs_clean: 1.31
      noise_30pct_ec_hte_rmse_ratio_vs_clean: 1.58
      noise_10pct_ec_hte_still_beats_global_bias: true
      noise_20pct_ec_hte_still_beats_global_bias: true
      noise_30pct_ec_hte_worse_than_global_rmse: true
      # Misspecified structure (true K=4, model uses K=2)
      misspec_k2_for_k4_ec_hte_bias_reduction_vs_naive: 0.35
      misspec_k2_for_k4_ec_hte_bias_reduction_vs_global: 0.10
      misspec_k2_for_k4_rmse_penalty: 1.4
      # Misspecified structure (true K=continuous, model uses K=4)
      misspec_discrete_for_continuous_ec_hte_bias_reduction: 0.45
      misspec_discrete_for_continuous_rmse_penalty: 1.2
      # HB partial pooling under misspecification
      hb_vs_mle_robustness_advantage_noise_20pct: 0.08
      hb_shrinkage_mitigates_noise: true
      # Semi-synthetic with real LLM (worst-tier: mechanism dormant)
      semi_synth_llm_noise_20pct_ec_hte_vs_global_rmse_ratio: 2.8
      semi_synth_llm_misspec_any_condition_ec_hte_benefit: negligible
    result_rationale: >
      On synthetic data (mechanism active), EC-HTE degrades gracefully under moderate subgroup
      mislabeling (10-20%) because HB partial pooling provides natural regularization — noisy subgroup
      boundaries cause the posterior to shrink toward the global mean, partially self-correcting. At
      30% mislabeling, the subgroup signal-to-noise ratio collapses and EC-HTE RMSE becomes 1.58x
      the clean baseline, though bias is still lower than naive. When the true structure has K=4 but
      the model uses K=2, EC-HTE captures only the coarsest heterogeneity — bias reduction drops from
      ~60% (correct K) to ~35% vs naive, with a 1.4x RMSE penalty. Continuous-to-discrete
      misspecification is less harmful (1.2x RMSE) because the discretization still captures the
      dominant variation axis. CRITICAL: under worst-tier semi-synthetic conditions (Δπ < 0.05),
      ALL misspecification conditions make EC-HTE strictly worse than global on RMSE. When the
      mechanism is dormant, adding subgroup structure (correct or misspecified) only adds estimation
      noise with no bias reduction to compensate. The RMSE ratio rises to 2.8x at 20% noise
      (vs ~2.0x with clean subgroups), making EC-HTE even less attractive. This is the expected
      behavior: robustness analysis in the homogeneous regime simply confirms that unnecessary
      stratification hurts, and misspecification makes it hurt more.
    tables:
      - name: "Table: Robustness to Subgroup Label Noise (Synthetic Extreme, K=4, n=500)"
        columns: [noise_pct, method, mean_abs_bias, rmse, coverage_95, rmse_ratio_vs_clean_ec_hte]
        rows:
          - [0, global, 0.105, 0.142, 0.94, "-"]
          - [0, ec_hte, 0.028, 0.189, 0.88, 1.00]
          - [10, global, 0.105, 0.144, 0.94, "-"]
          - [10, ec_hte, 0.038, 0.212, 0.86, 1.12]
          - [20, global, 0.105, 0.147, 0.93, "-"]
          - [20, ec_hte, 0.052, 0.248, 0.83, 1.31]
          - [30, global, 0.105, 0.150, 0.93, "-"]
          - [30, ec_hte, 0.071, 0.299, 0.80, 1.58]
      - name: "Table: Robustness to Misspecified K (Synthetic Extreme, n=500)"
        columns: [true_K, model_K, method, mean_abs_bias, rmse, bias_reduction_vs_naive_pct]
        rows:
          - [4, 4, ec_hte, 0.028, 0.189, 62]
          - [4, 2, ec_hte, 0.048, 0.265, 35]
          - [continuous, 4, ec_hte, 0.041, 0.227, 45]
          - [4, 4, global, 0.105, 0.142, "-"]
          - [4, 2, global, 0.105, 0.142, "-"]
      - name: "Table: Robustness Under Worst-Tier Semi-Synthetic (Δπ<0.05, K=4, n=500)"
        columns: [condition, method, mean_abs_bias, rmse, rmse_ratio_vs_global]
        rows:
          - [clean, global, 0.015, 0.091, 1.0]
          - [clean, ec_hte, 0.012, 0.182, 2.0]
          - [noise_10pct, ec_hte, 0.014, 0.211, 2.3]
          - [noise_20pct, ec_hte, 0.016, 0.255, 2.8]
          - [misspec_k2, ec_hte, 0.014, 0.198, 2.2]
    figures_description:
      - "Line plot: EC-HTE RMSE as function of subgroup label noise (0-30%), with horizontal dashed
         line for global RMSE. Two panels: synthetic extreme (EC-HTE starts below global, crosses at
         ~25% noise) and semi-synthetic LLM (EC-HTE always above global, gap widens with noise).
         Clearly shows mechanism-dependent robustness."
      - "Heatmap: bias reduction (%) under misspecification scenarios (rows: noise level × K mismatch;
         columns: synthetic vs semi-synthetic). Synthetic panel shows graceful degradation; semi-synthetic
         panel shows uniformly negligible values — the 'nothing to correct' regime."
    analysis: >
      Robustness analysis under worst-tier conditions serves a dual purpose: (1) On synthetic (mechanism
      active), EC-HTE degrades gracefully up to ~20% subgroup noise — HB partial pooling provides
      natural robustness by shrinking noisy subgroup estimates toward the global mean. This is a
      genuine positive finding. (2) On semi-synthetic with real LLM (mechanism dormant), misspecification
      compounds the existing EC-HTE disadvantage — RMSE ratio rises from 2.0x (clean) to 2.8x (20%
      noise). This is expected: when there is no bias to correct, adding noisy stratification structure
      only increases variance. For the paper reframe: present synthetic robustness as a positive
      property of the HB framework ('EC-HTE is robust to moderate misspecification when the mechanism
      is active'). The semi-synthetic results support the 'homogeneity boundary' argument — below
      the Δπ threshold, ANY stratification (correct or misspecified) is harmful. Include in appendix
      as robustness analysis, not main text. Key honest disclosure: 'EC-HTE requires both (a) the
      bias mechanism to be active (Δπ > threshold) and (b) reasonably accurate subgroup definitions
      (noise < ~20%) to provide RMSE improvement over global correction.'
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80fee215-6fb3-4a89-922e-9fc7249bf3f3",
  "isSidechain": false,
  "requestId": "req_011CbF25Esx3Wk5hH4q67ijn",
  "type": "assistant",
  "uuid": "6e260f10-201d-4399-bf65-84a4c4405ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AabA42oegfkqPQe7vmLn5x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14801,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8763,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14801
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SOTA LLMs show near-homogeneous errors on standard CSS tasks; bias amplification negligible in practice; empirical relevance of the mechanism unvalidated…",
  "leafUuid": "6e260f10-201d-4399-bf65-84a4c4405ced",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "SOTA LLM homogeneity and mechanism validation under worst-case",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SOTA LLMs show near-homogeneous errors on standard CSS tasks; bias amplification negligible in practice; empirical relevance of the mechanism unvalidated…",
  "leafUuid": "6e260f10-201d-4399-bf65-84a4c4405ced",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "SOTA LLM homogeneity and mechanism validation under worst-case",
  "sessionId": "e76d227e-7e3a-40a9-a1c3-860cc1fb7bca"
}
```

---
