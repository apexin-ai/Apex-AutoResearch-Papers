# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：三条 Claims 均有强证据支撑；诊断准则经交叉验证后仍有效；real data 重分析显示模式一致性；EMNLP 审稿人接受 'problem di

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/7e054a7a-62e4-42c8-8871-eaebc9435796.jsonl`
- **Structured JSON:** [`c0a1ebadace089059b91.json`](../../sessions/c0/c0a1ebadace089059b91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:27:16.629Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:27:16.629Z",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：三条 Claims 均有强证据支撑；诊断准则经交叉验证后仍有效；real data 重分析显示模式一致性；EMNLP 审稿人接受 'problem discovery + principled solution' 定位\n核心假设：['诊断准则 (Claim 3) 从 setting-level 重构为 subgroup-level 预测任务后，leave-one-setting-out CV AUC ≥ 0.75（当前 subgroup AUC=0.833 可迁移至 CV 设定）', 'exp-004 real data 通过更细粒度 subgroup 定义或补充第二数据集（如 TweetEval sentiment），EC-HTE 至少展示方向性一致的 bias reduction 或 coverage 优势', 'RMSE tradeoff 被审稿人接受：bias reduction 是 primary metric，RMSE 在 n_expert ≥ 500 时已 competitive', 'PPCI 互补性 (35x bias reduction in DGP C) 被视为实质性贡献', '审稿人认可 bias mechanism discovery 的独立价值，不要求 convergence rates 或 minimax bounds']\n关键指标范围：{'bias_amplification_max_dim': [2.4, 2.9], 'bias_amplification_max_cf': [5.0, 6.5], 'ec_hte_bias_reduction_factor_vs_global': [2.0, 4.5], 'ec_hte_ppci_bias_dgp_c': [0.002, 0.01], 'r2_bias_identity_k2': [0.99, 0.995], 'r2_bias_identity_k4': [0.97, 0.98], 'diagnostic_auc_cv': [0.75, 0.85], 'real_data_delta_pi': [0.1, 0.2], 'coverage_ec_hte': [0.92, 0.97], 'hb_crossover_k2_extreme': [200, 300], 'hb_crossover_k4_extreme': [800, 1200], 'multi_llm_delta_pi_min': [0.05, 0.08]}\n叙事方向：原始三 Claim 结构完整保留。Lead with 'debiasing can hurt' 作为 surprising finding（50% parameter space, up to 5.9x amplification），EC-HTE 作为 principled fix with precise budget guidelines，诊断准则作为 practical decision tool。PPCI 互补性升级至 Contribution #4。Real data 作为 consistent illustration。Headline: 'Global correction worsens subgroup CATE bias by 2-3x median; EC-HTE reduces bias to near-zero with 250 expert labels; composition with PPCI achieves 0.005 bias under dual error.' 审稿周期 1R accept 或 minor revision。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ec_hte_llm_annotation\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 2-3x (median across configurations), with amplification up to 5.9x for K=4 subgroups; when naive bias is near zero, global correction creates bias where none existed. For the difference-in-means estimator, the amplification magnitude does NOT monotonically increase with K (K=2 extreme: up to 2.86× vs K=4 extreme: up to 2.41×); however, with nonlinear estimators such as CausalForest, more subgroups amplify the effect substantially (K=4/extreme: up to 5.9×) due to compounding estimation noise in tree-based CATE. Global correction increases subgroup-level bias in ~50% of the parameter space.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias when misclassification heterogeneity is sufficiently high, while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction by borrowing strength across groups (classic James-Stein shrinkage). We provide precise crossover thresholds: EC-HTE outperforms global correction in RMSE with as few as 250 expert labels (K=2, high heterogeneity), scaling to ~1000 for K=4. **Boundary condition**: when expert labels per subgroup < ~25, shrinkage can be harmful — stratified MLE is preferred. **EC-HTE is most valuable precisely when it is most needed — the diagnostic criterion (Claim 3) identifies these scenarios.** **CONFIRMED** by exp-003 full 100 MC (1200 runs, 0 errors). HB crossover at ~11 experts/subgroup; ≥25 recommended for robust performance. Demonstrated with both difference-in-means and CausalForestDML (exp-011: consistent bias reduction pattern, ec_hte_forest |bias|=0.06 vs naive 0.16). CausalForest amplifies the debiasing-hurts effect (up to 5.9x in K=4/extreme) due to nonlinear CATE estimation.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic that simultaneously predicts when global correction is harmful (Claim 1) and when the expert label investment for stratified correction is worthwhile (connecting to the budget guidelines from Claim 2). This criterion has standalone value independent of EC-HTE — even without adopting EC-HTE, knowing when global correction backfires is practically actionable.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis across computational social science (CSS) — e.g., sentiment framing moderates message effectiveness, hate speech type moderates intervention impact. LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education; documented across CSS tasks including sentiment, stance, toxicity). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as \"problem identification + principled solution\" not \"new estimation technique.\"\n\n- **Headline result template**: \"On semi-synthetic CSS benchmarks, global correction worsens subgroup CATE bias by 2-3x (median), with amplification up to 5.9x for K=4 subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels. Combined with PPCI, the composition achieves near-zero bias (0.005) even when both covariate and outcome errors are present.\"\n\n- **Oracle framing**: When reporting DGP C results where ec_hte_ppci outperforms oracle, always use \"covariate-oracle\" (true Z + observed Y), never unqualified \"oracle\". Frame as \"composite correction is necessary and sufficient when both error types coexist\" — NOT \"beats oracle\". The result is by construction (ec_hte_ppci corrects both error types; covariate-oracle only corrects one), not surprising.\n\n## Key Contributions (ordered for paper)\n\n1. **Bias decomposition identity**: Exact population-level identity: bias ∝ misclassification heterogeneity × CATE heterogeneity (Δπ×Δτ product form). NOT a bound — it is an exact identity under A1–A4; finite-sample R² measures MC noise, not bound looseness. Includes \"debiasing can hurt\" proposition with constructive example. Frame as \"bias decomposition\" or \"bias identity\" throughout — never \"bias bound.\" (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **EC-HTE + PPCI composition — empirically necessary and sufficient**: EC-HTE and PPCI are empirically necessary and sufficient in composition: neither alone adequately handles dual-error scenarios (DGP C), but their composition reduces bias to near-zero (0.005, a 35× improvement over EC-HTE alone). EC-HTE exploits mixing matrix structure for covariate-side error; PPCI rectifier captures outcome-side error. PPCI alone can partially correct covariate error but with higher variance (limited by gold subset size). In Methods, retain full discussion of partial overlap; in Abstract, lead with \"necessary and sufficient in composition.\" (Method + Empirical)\n5. **Comprehensive validation**: Synthetic + semi-synthetic + real-data case study (pattern consistency, not ground-truth benchmark) with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI / DSL?\"** — PPCI rectifier is a general-purpose correction that captures any systematic error (covariate + outcome); EC-HTE is a structured correction exploiting mixing matrix structure specifically for covariate-side error. They are complementary: EC-HTE alone is more efficient for covariate error (uses M⁻¹ structure), PPCI alone can partially correct covariate error but with higher variance (limited by gold subset). In composition, EC-HTE handles structured covariate error, residual rectifier handles outcome error. DSL applied per-subgroup is a valid baseline but lacks cross-subgroup shrinkage, operates at estimand level rather than measurement model level, and has strictly higher variance under partial pooling. Do NOT say \"DSL cannot do subgroup correction\" — say it lacks the principled shrinkage mechanism.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — exp-006 provides precise RMSE crossover points: K=2/extreme n_expert=250, K=4/extreme n=1000, K=4/moderate n=2000, K=2/moderate never crosses (global always better on RMSE). Paper needs \"Expert Budget Recommendation\" subsection with per-K guidelines. Key message: when diagnostic criterion flags high heterogeneity (extreme regime), EC-HTE is worth the investment at moderate budgets; when heterogeneity is low, global correction is the safer choice. This honest framing connects Claim 2 (EC-HTE method) to Claim 3 (diagnostic criterion) — the diagnostic decides the correction strategy.\n\n6. **\"How does this differ from Carroll et al. (2006) / classical measurement error?\"** — The qualitative insight that misspecified corrections can amplify MSE is classical (Fuller 1987, Sec. 2.3). Our specific contributions beyond this are: (a) the quantitative Δπ×Δτ product form for CATE estimation with effect-modifier misclassification, (b) demonstrating this failure mode occurs *by default* in standard LLM annotation workflows, and (c) providing a computable diagnostic and correction framework. Must explicitly cite and contextualize: Fuller (1987), Carroll et al. (2006 Ch. 4), Gustafson (2003), Hu & Schennach (2008), Imai & Yamamoto (2010). Also cite Bayesian annotation models: Dawid & Skene, Passonneau & Carpenter (2014), Hovy et al. (2013). **Bibliography target: 30-35 references** spanning measurement error, Bayesian estimation, causal inference, LLM-as-annotator (Tornberg 2024, Gilardi et al. 2023, Ziems et al. 2024), HTE methods (Wager & Athey 2018, Kennedy 2023, Chernozhukov et al. 2018).\n\n7. **\"Methodological novelty is modest\"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. HB partial pooling provides meaningful RMSE reduction for moderate subgroups but is NOT \"never worse than global\" — it is a James-Stein shrinkage estimator with known boundary conditions. **Recommended condition**: n_expert per subgroup ≥ ~25 (e.g., n_expert ≥ 100 for K=4 with 12% minority). Below this, stratified MLE is preferred. This honest limitation strengthens credibility. State conditions explicitly using per-subgroup formulation, not just total n_expert.\n\n8. **\"Why no figures?\"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use cases (sentiment analysis, hate speech detection, refugee interview coding), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track. **NOTE**: Framing broadened from \"political-science\" to \"CSS\" (D004b) — TweetEval stance tasks too small (N<1000), sentiment (N=45K) usable but not political science. CSS is more accurate and equally strong for EMNLP.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n## Writing Requirements (Dream Round 2 consensus)\n\n1. **\"Bias decomposition\" NOT \"bias bound\"** — Theorem 1 is an exact identity at population level. R² < 1.0 in verification reflects finite-sample MC noise, not bound looseness.\n2. **Bibliography: 30-35 references minimum** — Must span 5 literatures: classical measurement error, Bayesian estimation, causal inference, LLM-as-annotator, CSS. Critical citations: Fuller 1987, Wager & Athey 2018, Imai & Yamamoto 2010.\n3. **3+ figures in main text** — (a) bias mechanism schematic, (b) Δπ×Δτ amplification heatmap, (c) diagnostic ROC curve, (d) budget crossover curves. Move exp-008/exp-009 tables to appendix.\n4. **Semi-synthetic DGP fully specified** — outcome generation, treatment assignment, CATE injection mechanism.\n5. **Real-data framed as pattern consistency** — NOT ground-truth benchmark. No bias/RMSE against unknown true CATEs.\n6. **EC-HTE advantage is conditional, not universal** — ec_hte dominates when misclassification heterogeneity is high (extreme regime) OR n_expert is large (≥500). In moderate regime with small n_expert (~100), global correction can outperform ec_hte because per-subgroup CM estimation noise exceeds the benefit of stratification. This connects to Claim 3: the diagnostic criterion (Δπ×Δτ) predicts when EC-HTE is needed. Unified condition: n_expert/K ≥ ~25-50 experts per subgroup.\n11. **RMSE tradeoff must be disclosed** — ec_hte has higher RMSE than global/naive in K=4/n≤100 configs (up to 3.5x in extreme cases) due to noisy per-subgroup CM estimation. Bias is lower but variance is higher. Must report both bias AND RMSE; include bias-RMSE tradeoff analysis. At n_expert≥500, ec_hte RMSE becomes competitive.\n12. **K-dependence of debiasing-hurts** — DIM estimator: K=2 extreme ~2.86×, K=4 extreme ~2.41× (does NOT monotonically increase with K). CausalForest: K=4 extreme up to 5.9× (nonlinear estimator amplifies with more subgroups). Report both patterns; do NOT claim \"more subgroups → always worse\" without qualifying the estimator.\n7. **Confusion matrix invertibility** — State det(Ĉ_k) ≠ 0 assumption explicitly.\n8. **Diagnostic AUC cross-validated** — Leave-one-setting-out or held-out evaluation, not in-sample.\n9. **Hyperprior values stated + sensitivity analysis** — Gamma(α, β) for Dirichlet concentration; report sensitivity to 2× changes.\n10. **PPCI complementarity elevated** — Highlight in abstract and contributions. Frame as \"complementary\" not \"orthogonal\": EC-HTE is structured covariate-error correction; PPCI rectifier is general residual correction. Composition = EC-HTE handles structured part + rectifier handles remainder (primarily outcome error).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2. MUST report full MCMC diagnostics: sampler (PyMC\n    NUTS), chains (≥4), warmup (≥1000), R̂ (<1.01), ESS (>200), runtime vs MLE. Report\n    SEs/CIs for all metrics from MC runs. Monitor coverage calibration — if systematic\n    undercoverage, diagnose cause.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example. MUST include K>2 extension: verify bias formula empirically for K=4 subgroups;\n    add Remark after Proposition 1 discussing general-K case (sum-of-products form).\n    Report R² of analytic prediction vs MC, bound tightness ratio, and CIs on all\n    bias estimates.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim: 1,2,3\n  description: 'Semi-synthetic benchmark: use real CSS tweet corpus — TweetEval sentiment\n    (N=45K, primary) for exp-003. Framing broadened from ''political-science'' to\n    ''CSS'' per D004b (stance tasks N<1000 unusable). Inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 (API) and optionally Qwen3-235B-A22B (GPU), measure\n    subgroup-specific misclassification rates, apply EC-HTE vs baselines. Subgroup\n    variables: text features (has_hashtag, text_length) for semi-synthetic; demographic\n    subgroups reserved for exp-004. MUST fully specify DGP in paper: (a) outcome generation\n    model, (b) treatment assignment mechanism, (c) how true CATEs are injected. MUST\n    run LLM annotation pilot (~1000 samples) before committing to verify per-subgroup\n    misclassification heterogeneity exists.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim: 1,2\n  description: 'Real-data case study (pattern consistency, NOT ground-truth validation):\n    apply EC-HTE to real CSS dataset with subgroup-varying LLM misclassification.\n    Show: (a) global vs EC-HTE produce qualitatively different CATE distributions,\n    (b) EC-HTE results consistent with domain knowledge (demographic effect direction),\n    (c) bootstrap CIs on point estimate differences. Frame as ''illustrative application''\n    not ''ground-truth benchmark''. Reviewer confirmed: real data has no ground truth\n    CATE, CV-based ground truth is circular. PRIMARY: UC Berkeley Measuring Hate Speech\n    corpus (public, rich demographic subgroups). NICE-TO-HAVE: Ashwin et al. (2025)\n    if obtainable (requires author email + IRB, not feasible within 5-day DDL).'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference) or API\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: UC Berkeley dataset causal framework (T,Y,Z,S) mapping needs design\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold. MUST use\n    cross-validation or held-out evaluation (NOT in-sample AUC on own experiments).\n    Dream Round 2 flagged in-sample AUC as methodological weakness across best and\n    median tiers.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1,2\n  description: 'PPCI + DSL baseline comparison: (a) PPCI kernel-based conditional\n    correction vs EC-HTE on covariate-side vs outcome-side error; (b) per-subgroup\n    DSL as additional baseline (DSL applied independently per subgroup, no cross-subgroup\n    shrinkage — shows EC-HTE''s partial pooling advantage); (c) EC-HTE+PPCI composition\n    for simultaneous covariate+outcome error; (d) CRITICAL: include ''pure covariate-error,\n    zero outcome-error'' control condition to demonstrate EC-HTE advantage when covariate-side\n    error dominates (PPCI should be ineffective here). Paper framing: DSL per-subgroup\n    is a valid baseline but lacks cross-subgroup shrinkage and operates at estimand\n    level rather than measurement model level.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest integration: apply EC-HTE post-hoc correction to CausalForestDML\n    subgroup CATE estimates + leaf-level corrected pseudo-outcomes with variance-adjusted\n    CIs. Compare against naive forest and globally-corrected forest. ELEVATED TO P0:\n    Claim 2 explicitly states CausalForestDML but no experiment validates this — claim-evidence\n    gap is reviewer killshot.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mcmc_rhat_max: 1.024\n    mcmc_ess_min: 129\n    mcmc_divergent: 0\n    runtime_min: 69\n    total_mc_runs: 3600\n    hb_vs_mle_rmse_improvement_k2_n50: 4-9%\n    hb_vs_mle_rmse_improvement_k2_n100: 1-2%\n    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%\n    hb_coverage_min: 0.87\n    hb_coverage_median: 0.93\n    k4_extreme_n50_blowup: false\n    k4_extreme_n50_blowup_note: Fixed by singularity guard + 4-chain MCMC\n    mcmc_fix_4chain:\n      rhat_max_all_configs: 1.0034\n      ess_min_all_configs: 1618\n      ess_improvement: ~4x vs 2-chain\n      k4_extreme_n50_A_rmse_z0: 3.14 → 0.99\n      k4_extreme_n50_B_rmse_z0: 509.93 → 0.27\n      k4_extreme_n100_A_rmse_z0: 11.57 → 0.29\n      singularity_guard_triggers: extreme/n=50 only (2 HB, 3 MLE / 100 runs)\n      results_file: results/exp001_hb_results_v2.csv\n    hyperprior_sensitivity:\n      scale_range: 0.5-2.0\n      k2_rmse_variation: <1%\n      k4_rmse_variation: ~4-5%\n      coverage_invariant: true\n      conclusion: robust\n      results_file: results/exp001_hyperprior_sensitivity.csv\n- exp_id: exp-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r2_k2: 0.9939\n    r2_k4: 0.9738\n    tightness_ratio_k2_median: 1.0027\n    tightness_ratio_k4_median: 1.0234\n    debiasing_hurts_pct: 50\n    debiasing_hurts_pct_note: 260/520 (excluding dc=0 rows where bias=0)\n    debiasing_hurts_threshold_delta_misclass: 0.1235\n    max_bias_ratio_k2: 2.86\n    max_bias_ratio_k4: 2.41\n    coverage_2se_k2: 0.951\n    coverage_2se_k4: 0.94\n- exp_id: exp-007\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_rows: 6912\n    dgps:\n    - A_covariate_only\n    - B_outcome_only\n    - C_both_errors\n    - D_no_error\n    methods: 8\n    mc_runs: 100\n    double_correction_fix_verified: true\n    dgp_a_ec_hte_ppci_equals_ec_hte: true\n    dgp_c_extreme_n250_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.225\n      ec_hte_bias_z0: 0.178\n      ec_hte_rmse_z0: 0.226\n      ppci_bias_z0: 0.004\n      ppci_rmse_z0: 0.261\n      naive_bias_z0: 0.251\n      naive_rmse_z0: 0.269\n    dgp_c_n500_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.142\n      ec_hte_bias_z0: 0.088\n      ec_hte_rmse_z0: 0.134\n    key_finding: ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better\n      than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.\n- exp_id: exp-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase: A_semi_synthetic\n    n_subgroups: 4\n    misclass_rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25\n    subgroup_sizes: S0~38%, S1~38%, S2~12%, S3~12%\n    p_z1_actual: 0.39\n    debiasing_hurts_confirmed: true\n    mc_runs: 100\n    v3_hb_integration_100mc:\n      methods:\n      - oracle\n      - naive\n      - global_corrected\n      - stratified_mle\n      - hb_ec_hte\n      hb_vs_mle_summary:\n        n50_S3_extreme: -57% RMSE (HB worse, but not catastrophic)\n        n50_S3_moderate: -54% RMSE z1 (HB worse)\n        n100_S3_extreme: +60% RMSE z1 (HB dramatically better)\n        n100_S3_moderate: +24% RMSE z1 (HB better)\n        n100_S2: +5-8% RMSE (HB better)\n        n250_S3: +5-17% RMSE (HB better)\n        n500_all: +0.2-1.6% (converged)\n      key_finding: '100 MC confirms: S3 blowup at n=50 is real but moderate (not catastrophic\n        as dry-run suggested). At n>=100, HB is better everywhere, especially S3 (+26-60%).\n        Partial pooling sweet spot is n=100-250.'\n      hypothesis_verdict: validated_with_boundary\n      boundary_condition: n_expert>=100 recommended; n=50 with extreme heterogeneity\n        in tiny subgroups shows moderate degradation\n    results_file_v3: results/exp003_phase_a_v3.csv\n    results_file_v3_raw: results/exp003_phase_a_v3_raw.csv\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subgroup_level_auc: 0.833\n    subgroup_correlation: 0.86\n    setting_level_auc: 0.49\n    low_pi_hurt_pct: 84.6\n    high_pi_hurt_pct: 15.4\n    theory_alignment: consistent with exp-002 formula\n- exp_id: exp-011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    n_configs: 8\n    total_rows: 144\n    runtime_min: 35\n    methods:\n    - naive_forest\n    - global_forest\n    - ec_hte_forest\n    mean_abs_bias:\n      naive_forest: 0.1558\n      global_forest: 0.1073\n      ec_hte_forest: 0.0608\n    mean_rmse:\n      naive_forest: 0.1782\n      global_forest: 0.1659\n      ec_hte_forest: 0.2289\n    debiasing_hurts_cases: 9\n    debiasing_hurts_max_ratio: 5.9\n    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'\n    k2_n500_ec_hte_bias_range: 0.004-0.013 (near zero)\n    k2_n500_global_bias_range: 0.033-0.109 (still biased)\n    pattern_consistent_with_diff_in_means: true\n    claim2_validated: true\n- exp_id: exp-006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    total_rows: 288\n    runtime_min: 110\n    grid: n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]\n    crossover_hb_beats_global:\n      K2_extreme: 250\n      K2_moderate: never\n      K4_extreme: 1000\n      K4_moderate: 2000\n    hb_vs_mle: HB ≥ MLE in 21/24 configs (87.5%; partial pooling rarely hurts in symmetric\n      DGP)\n    hb_best_improvement_over_mle:\n      K4_moderate_n50_sgC: +42.4% RMSE\n      K4_extreme_n50_sgC: +23.4% RMSE\n      K4_moderate_n50_sgB: +24.0% RMSE\n    convergence: HB ≈ MLE at n≥1000 (<0.5% difference)\n    key_finding: 'Crossover depends strongly on K and regime. K=2: crossover at n=250\n      (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest\n      improvement over MLE via partial pooling.'\n- exp_id: exp-007b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    kill_reason: 'D012: Director 决定放弃 HB backfill。理由：PPCI 表核心 story 是互补性，HB vs MLE\n      是边际改进；exp-001 已验证 HB。CSV 已重命名为 .broken'\n- exp_id: exp-012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: gpt-4.1-2025-04-14\n    n_samples: 500\n    valid_annotations: 500\n    failed: 0\n    accuracy_3class: 0.672\n    accuracy_binary: 0.858\n    subgroup_misclass_rates:\n      hash_long: 0\n      hash_medium: 0.2\n      hash_short: 0.174\n      nohash_long: 0\n      nohash_medium: 0.102\n      nohash_short: 0.138\n    delta_pi: 0.2\n    heterogeneity_significant: true\n    key_finding: Hashtag presence increases binary misclassification rate (~0.17-0.20\n      vs ~0.10-0.14 for non-hashtag). Delta-pi=0.200 confirms meaningful heterogeneity\n      for EC-HTE correction.\n    analysis_file: results/pilot_gpt41_analysis.md\n- exp_id: exp-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    config: K=4/extreme/n_expert=50\n    n_expert_per_K: 12.5\n    hb_method: EB (Empirical Bayes, not Gibbs — conservative estimate for boundary\n      condition)\n    avg_rmse_naive: 0.109\n    avg_rmse_global: 0.14\n    avg_rmse_mle: 0.28\n    avg_rmse_eb: 0.292\n    worst_subgroup: A(pi=0.30) EB RMSE=0.62\n    amplification_max: 4.4x (A/EB vs global)\n    threshold_confirmed: n_expert/K=12.5 < 25\n    naive_beats_all: true\n    debiasing_hurts_D: Naive bias=0.001, Global bias=0.110 — extreme over-correction\n      in lowest-error subgroup\n- exp_id: exp-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    configs: 3\n    asymmetric_configs:\n    - balanced(FPR=0.15,FNR=0.25)\n    - fpr_dominant(FPR=0.30,FNR=0.10)\n    - fnr_dominant(FPR=0.10,FNR=0.30)\n    delta_tau_grid:\n    - 0\n    - 0.1\n    - 0.2\n    - 0.3\n    - 0.5\n    n_mc: 100\n    N: 5000\n    n_expert: 250\n    r2_analytic_vs_mc: 0.992\n    product_structure_cv: ~1e-16 (exact)\n    product_structure_confirmed: true\n    a2_not_required: true\n    ec_hte_avg_abs_bias: 0.006\n    ec_hte_avg_rmse: 0.033\n    ec_hte_avg_coverage: 0.9\n    global_avg_abs_bias: 0.025\n    global_avg_rmse: 0.04\n    global_avg_coverage: 0.78\n    naive_avg_abs_bias: 0.025\n    naive_avg_rmse: 0.039\n    naive_avg_coverage: 0.87\n    bias_reduction_vs_global: 4.2x\n    coverage_improvement_vs_global: +12pp\n    latex_derivation_included: true\n    key_finding: Product structure bias = Δτ·[B_s]_{z,1} holds exactly under asymmetric\n      misclassification. A2 (symmetric) assumption is NOT required. EC-HTE dominates\n      with 4.2x bias reduction.\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dataset: UC Berkeley Measuring Hate Speech\n    n_comments: 2496\n    valid_annotations: 2496\n    subgroups:\n      plat0_long: 624\n      plat0_short: 624\n      plat23_long: 624\n      plat23_short: 624\n    subgroup_type: text features (platform_group × text_length)\n    delta_pi: 0.117\n    global_FPR: 0.139\n    global_FNR: 0.533\n    misclass_rates:\n      plat0_long: 0.266\n      plat0_short: 0.337\n      plat23_long: 0.303\n      plat23_short: 0.383\n    avg_abs_bias:\n      naive: 0.21\n      global: 0.273\n      ec_hte: 0.313\n    cate_comparison: EC-HTE does not outperform global on avg |bias| — high FNR (~53%)\n      and wide CIs limit correction effectiveness on this dataset\n    key_finding: Δπ=0.117 confirms real-world misclassification heterogeneity across\n      text-feature subgroups. High global FNR (53%) indicates LLM severely under-classifies\n      dehumanization. CATE correction comparison inconclusive due to wide bootstrap\n      CIs.\n- exp_id: exp-008\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    models_completed:\n    - gpt-3.5-turbo\n    - gpt-4.1\n    - gpt-4o\n    - gpt-4o-mini\n    - gpt-4-turbo\n    - gpt-5.4\n    total_models: 6\n    proxy_provider: OpenAI only\n    gpt5x_model_used: gpt-5.4\n    gpt55_failed: reasoning tokens consume max_tokens budget, too slow (~1min/call)\n    filtered_analysis:\n      excluded_subgroups:\n      - False_long (n=6)\n      - True_long (n=4)\n      min_n_threshold: 10\n      retained_subgroups:\n      - False_medium (n=187)\n      - False_short (n=109)\n      - True_medium (n=125)\n      - True_short (n=69)\n    effective_delta_pi:\n      gpt-3.5-turbo: 0.198\n      gpt-4-turbo: 0.149\n      gpt-4.1: 0.098\n      gpt-4o: 0.08\n      gpt-4o-mini: 0.136\n      gpt-5.4: 0.114\n    all_effective_delta_pi_above_005: true\n    worst_subgroup_consensus: True_medium (5/6 models)\n    spearman_significant_pairs:\n    - gpt-4-turbo vs gpt-4o (ρ=1.000)\n    - gpt-4.1 vs gpt-4o-mini (ρ=1.000)\n    - gpt-4.1 vs gpt-5.4 (ρ=1.000)\n    - gpt-4o-mini vs gpt-5.4 (ρ=1.000)\n    spearman_note: Only 4 subgroups after filtering, limited statistical power (most\n      p>0.20)\n    key_finding: All 6 models (GPT-3.5 through GPT-5.4, three generations) show effective\n      Δπ > 0.05 after excluding n<10 subgroups. Heterogeneity is structural, not model-specific.\n- exp_id: exp-010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    configs: 2\n    noise_levels:\n    - 0\n    - 0.1\n    - 0.25\n    - 0.5\n    total_runs: 800\n    runtime_sec: 15\n    k2_coverage_naive:\n    - 0.875\n    - 0.877\n    - 0.89\n    - 0.897\n    k2_coverage_hb:\n    - 0.958\n    - 0.948\n    - 0.95\n    - 0.945\n    k2_coverage_global:\n    - 0.925\n    - 0.935\n    - 0.932\n    - 0.945\n    k4_coverage_naive:\n    - 0.904\n    - 0.916\n    - 0.909\n    - 0.919\n    k4_coverage_hb:\n    - 0.956\n    - 0.958\n    - 0.96\n    - 0.946\n    k4_coverage_global:\n    - 0.93\n    - 0.953\n    - 0.948\n    - 0.944\n    hb_beats_mle_all_configs: true\n    hb_improvement_range: +0.1% to +0.9% RMSE\n    graceful_convergence_at_50pct: true\n    key_finding: 'Coverage is the decisive metric: naive 87-92%, EC-HTE 95-96% across\n      all noise levels. No catastrophic failure. HB shrinkage provides automatic safeguard\n      — converges to global at 50% noise.'\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:27:16.632Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:27:16.632Z",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T12:27:16.652Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：三条 Claims 均有强证据支撑；诊断准则经交叉验证后仍有效；real data 重分析显示模式一致性；EMNLP 审稿人接受 'problem discovery + principled solution' 定位
核心假设：['诊断准则 (Claim 3) 从 setting-level 重构为 subgroup-level 预测任务后，leave-one-setting-out CV AUC ≥ 0.75（当前 subgroup AUC=0.833 可迁移至 CV 设定）', 'exp-004 real data 通过更细粒度 subgroup 定义或补充第二数据集（如 TweetEval sentiment），EC-HTE 至少展示方向性一致的 bias reduction 或 coverage 优势', 'RMSE tradeoff 被审稿人接受：bias reduction 是 primary metric，RMSE 在 n_expert ≥ 500 时已 competitive', 'PPCI 互补性 (35x bias reduction in DGP C) 被视为实质性贡献', '审稿人认可 bias mechanism discovery 的独立价值，不要求 convergence rates 或 minimax bounds']
关键指标范围：{'bias_amplification_max_dim': [2.4, 2.9], 'bias_amplification_max_cf': [5.0, 6.5], 'ec_hte_bias_reduction_factor_vs_global': [2.0, 4.5], 'ec_hte_ppci_bias_dgp_c': [0.002, 0.01], 'r2_bias_identity_k2': [0.99, 0.995], 'r2_bias_identity_k4': [0.97, 0.98], 'diagnostic_auc_cv': [0.75, 0.85], 'real_data_delta_pi': [0.1, 0.2], 'coverage_ec_hte': [0.92, 0.97], 'hb_crossover_k2_extreme': [200, 300], 'hb_crossover_k4_extreme': [800, 1200], 'multi_llm_delta_pi_min': [0.05, 0.08]}
叙事方向：原始三 Claim 结构完整保留。Lead with 'debiasing can hurt' 作为 surprising finding（50% parameter space, up to 5.9x amplification），EC-HTE 作为 principled fix with precise budget guidelines，诊断准则作为 practical decision tool。PPCI 互补性升级至 Contribution #4。Real data 作为 consistent illustration。Headline: 'Global correction worsens subgroup CATE bias by 2-3x median; EC-HTE reduces bias to near-zero with 250 expert labels; composition with PPCI achieves 0.005 bias under dual error.' 审稿周期 1R accept 或 minor revision。

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
  "promptId": "a1828d57-2138-4141-b728-0c6c43e377d0",
  "type": "user",
  "uuid": "0f714d44-2b88-4529-a20a-ac4a4ee5e4f4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:27:16.650Z_

```json
{
  "parentUuid": "0f714d44-2b88-4529-a20a-ac4a4ee5e4f4",
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
  "uuid": "35faf0d1-5339-4736-a768-bdf081cb0ff7",
  "timestamp": "2026-05-21T12:27:16.650Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:27:16.650Z_

```json
{
  "parentUuid": "35faf0d1-5339-4736-a768-bdf081cb0ff7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9c75d5c2-5976-4f09-b68e-0d597e0feec8",
  "timestamp": "2026-05-21T12:27:16.650Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 Claims 均有强证据支撑；诊断准则经交叉验证后仍有效；real data 重分析显示模式一致性；EMNLP 审稿人接受 'problem discovery + principled solution' 定位 核心假设：['诊断准则 (Claim 3) 从 setting-level 重构为 sub…",
  "leafUuid": "9c75d5c2-5976-4f09-b68e-0d597e0feec8",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE bias mechanism discovery and expert label budgeting",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:27:47.199Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment plan, under the "best" tier definition they've provided. I need to look at which experiments are still "planned" vs already "DONE" in the registry.

Let me cross-reference:

Registry (DONE):
- exp-001: DONE
- exp-002: DONE
- exp-003: DONE
- exp-004: DONE
- exp-005: DONE
- exp-006: DONE
- exp-007: DONE
- exp-007b: killed


- exp-008: DONE
- exp-010: DONE
- exp-011: DONE
- exp-012: DONE (pilot)
- exp-013: DONE
- exp-014: DONE

Experiment plan status:
- exp-001 through exp-008: all marked as planned in the plan but already completed in the registry
- exp-009: planned but not yet in the registry as done
- exp-010 through exp-011: planned but already completed

So exp-009 is the only one that's truly still pending. But wait, looking back at what the user actually asked for — they want detailed predictions for every experiment marked as "planned" in the experiment_plan document, which means all of them since they all have that status in the plan itself, regardless of what's in the registry.

The user is asking me to generate forecasted results for each planned experiment under the "best" tier scenario. For experiments already completed, I should use their actual results as the basis for my predictions since those results likely align with the best-case tier. For exp-009, which hasn't been executed yet, I'll need to predict what best-tier results would look like based on the experiment's design and parameters. I'm finishing up the predictions for the remaining experiments—exp-009 on adaptive allocation is the only one left to estimate. Now I'll compile everything into the YAML structure with the predicted best-tier results, expected metrics, and supporting rationale for each experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c75d5c2-5976-4f09-b68e-0d597e0feec8",
  "isSidechain": false,
  "requestId": "req_011CbFiHTPGHW4jCnyacQS3r",
  "type": "assistant",
  "uuid": "cd042168-6517-46c8-8de3-617216cca95b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eo87kd1zJn7uK77Z1eUjj5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17601,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15554,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15554,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17601
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

_source line 9 · 2026-05-21T12:32:21.857Z_

```yaml
tier: best
narrative_guidance: >
  三条 Claims 完整保留，Lead with 'debiasing can hurt' (50% parameter space, up to 5.9x amplification)。
  EC-HTE 作为 principled fix，诊断准则作为 practical decision tool。PPCI 互补性升级至 Contribution #4。
  Real data 作为 consistent illustration (pattern consistency, NOT ground-truth benchmark)。
  Headline: 'Global correction worsens subgroup CATE bias by 2-3x median; EC-HTE reduces bias
  to near-zero with 250 expert labels; composition with PPCI achieves 0.005 bias under dual error.'
  审稿周期目标 1R accept 或 minor revision。

imagined_experiments:
  - name: "Hierarchical Bayesian EC-HTE on Synthetic Data"
    plan_id: "exp-001"
    description: >
      HB Dirichlet-prior confusion matrix estimator with partial pooling，
      full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × K=2,4)，
      与 MLE/Laplace 对比。100 MC runs per config，4-chain NUTS MCMC。
    expected_results:
      mcmc_rhat_max: 1.005
      mcmc_ess_min: 1500
      mcmc_divergent: 0
      runtime_min: 70
      total_mc_runs: 3600
      hb_vs_mle_rmse_improvement_k2_n50: "4-9%"
      hb_vs_mle_rmse_improvement_k4_n50_moderate: "6-9%"
      hb_coverage_median: 0.93
      hb_coverage_min: 0.87
      hyperprior_sensitivity_k2_variation: "<1%"
      hyperprior_sensitivity_k4_variation: "~4-5%"
      singularity_guard_triggers: "extreme/n=50 only (2-3 per 100 runs)"
    result_rationale: >
      best 档下 MCMC 收敛良好 (R̂<1.01, ESS>200) 因为 4-chain NUTS 提供充分探索，
      Dirichlet 先验与 multinomial likelihood 共轭性保证后验几何良好。
      HB 在 n=50 小样本时优势最大 (4-9% RMSE improvement) 因为 partial pooling
      的 James-Stein shrinkage 在信息稀缺时借力最强；n≥500 时 MLE 已有足够数据，
      HB 收敛至 MLE (<0.5% 差异)。coverage median 0.93 而非 0.95 因为 HB 后验
      区间基于 MCMC 样本，有限 MC 引入的 discretization 导致轻微 undercoverage。
      hyperprior sensitivity 在 K=4 时更大 (~4-5%) 因为 4 subgroup 的 Dirichlet
      浓度参数影响更多自由度，但 coverage 不变说明 point estimate 对先验敏感
      但区间宽度自适应补偿。
    tables:
      - title: "HB vs MLE RMSE Comparison (K=2)"
        columns: [regime, n_expert, subgroup, hb_rmse, mle_rmse, improvement_pct]
        rows:
          - [extreme, 50, z0, 0.095, 0.104, 8.7]
          - [extreme, 50, z1, 0.102, 0.108, 5.6]
          - [extreme, 100, z0, 0.065, 0.066, 1.5]
          - [extreme, 100, z1, 0.068, 0.069, 1.4]
          - [extreme, 250, z0, 0.041, 0.042, 2.4]
          - [extreme, 500, z0, 0.029, 0.029, 0.3]
          - [moderate, 50, z0, 0.088, 0.092, 4.3]
          - [moderate, 100, z0, 0.060, 0.061, 1.6]
      - title: "HB vs MLE RMSE Comparison (K=4)"
        columns: [regime, n_expert, subgroup, hb_rmse, mle_rmse, improvement_pct]
        rows:
          - [extreme, 50, sgC, 0.99, 1.30, 23.8]
          - [moderate, 50, sgC, 0.85, 0.93, 8.6]
          - [moderate, 50, sgB, 0.42, 0.52, 19.2]
          - [extreme, 100, sgC, 0.29, 0.46, 37.0]
          - [extreme, 250, sgC, 0.14, 0.15, 6.7]
      - title: "Hyperprior Sensitivity (scale ∈ {0.5, 1.0, 2.0})"
        columns: [K, metric, scale_0.5, scale_1.0, scale_2.0]
        rows:
          - [2, rmse_mean, 0.0632, 0.0635, 0.0638]
          - [4, rmse_mean, 0.182, 0.175, 0.168]
          - [2, coverage, 0.93, 0.93, 0.93]
          - [4, coverage, 0.92, 0.93, 0.93]
    figures_description:
      - "HB vs MLE RMSE ratio across n_expert (x-axis log scale), 分 K=2/K=4 和 extreme/moderate 四面板"
    analysis: >
      HB partial pooling 的核心价值在小样本 (n_expert/K < 50)：shrinkage 将不稳定的
      per-subgroup MLE 拉向 pooled estimate，降低 variance。K=4/extreme/n=50 的
      singularity guard 触发 (2-3/100 runs) 说明此边界条件下 MLE 本身不可靠，
      HB 的正则化是必要的。4-chain MCMC 相比 2-chain 的 ESS 提升 ~4x 确认
      多链策略对 posterior geometry exploration 的价值。

  - name: "Formal Bias Decomposition Verification"
    plan_id: "exp-002"
    description: >
      解析推导 bias = Δπ × Δτ 的 exact identity，系统参数网格上 MC 验证。
      K=2 和 K=4 分别验证。包含 'debiasing can hurt' proposition 的构造性证明。
    expected_results:
      r2_bias_identity_k2: 0.994
      r2_bias_identity_k4: 0.974
      tightness_ratio_k2_median: 1.003
      tightness_ratio_k4_median: 1.023
      debiasing_hurts_pct: 50
      debiasing_hurts_threshold_delta_misclass: 0.12
      max_bias_ratio_k2_extreme: 2.86
      max_bias_ratio_k4_extreme: 2.41
      coverage_2se_k2: 0.951
      coverage_2se_k4: 0.940
    result_rationale: >
      R²=0.994 (K=2) 因为二子群下 bias identity 是 exact (population level)，
      MC 偏差仅来自有限样本噪声 (N=5000, 100 MC runs)。K=4 的 R²=0.974 稍低
      因为 sum-of-products form 中 4 个子群的 MC 噪声累积（4 个交叉项 vs K=2 的 1 个），
      但仍然是 identity 而非 bound。tightness ratio ≈1.0 进一步确认这是 exact identity。
      debiasing hurts 50% (260/520 non-trivial configs) 因为当 naive bias 方向与
      global correction 方向同号时 correction 有效，异号时 amplify——对称参数网格下
      恰好 50%。max_bias_ratio K=2 > K=4 (2.86 vs 2.41) 因为 DIM estimator 下
      K=2 的两个子群 error rate 差异最大化（所有 heterogeneity 集中在一个对比），
      而 K=4 将 heterogeneity 分散到多个对比，单个子群的 worst-case amplification 反而降低。
      这是 DIM estimator 的特性——CausalForest 行为相反 (exp-011)。
    tables:
      - title: "Bias Identity R² Verification"
        columns: [K, n_configs, R2, tightness_median, tightness_95pct]
        rows:
          - [2, 260, 0.994, 1.003, 1.012]
          - [4, 260, 0.974, 1.023, 1.068]
      - title: "Debiasing Hurts Analysis"
        columns: [K, total_configs, hurts_count, hurts_pct, max_ratio, worst_config]
        rows:
          - [2, 260, 130, 50.0, 2.86, "Δπ=0.20, Δτ=0.50"]
          - [4, 260, 130, 50.0, 2.41, "Δπ=0.20, Δτ=0.50"]
      - title: "Bias Amplification by Parameter Region"
        columns: [delta_pi, delta_tau, k2_ratio, k4_ratio, direction]
        rows:
          - [0.05, 0.1, 1.12, 1.08, "global improves"]
          - [0.05, 0.5, 1.45, 1.32, "global improves"]
          - [0.15, 0.1, 1.85, 1.62, "global hurts"]
          - [0.15, 0.5, 2.52, 2.18, "global hurts"]
          - [0.20, 0.5, 2.86, 2.41, "global hurts (maximum)"]
    figures_description:
      - "Δπ × Δτ heatmap showing bias amplification factor，红色=global hurts, 蓝色=global helps"
      - "Analytic prediction vs MC bias scatter plot with R² annotation, K=2 和 K=4 双面板"
    analysis: >
      bias identity 的 exact 性质（R²>0.97 for both K）为 Claim 1 提供了最强支撑。
      50% hurts rate 是对称参数网格的自然结果，但实际应用中 heterogeneity 方向未知，
      因此 50% 是 prior probability of harm——足以证明 global correction 不可盲目应用。
      K-dependence 的 non-monotonicity (K=2 > K=4 for DIM) 是一个需要在论文中
      显式讨论的 subtle point，避免审稿人误读为 "more subgroups → always worse"。

  - name: "Semi-Synthetic CSS Benchmark (TweetEval Sentiment)"
    plan_id: "exp-003"
    description: >
      TweetEval sentiment (N=45K) 上注入已知 CATE heterogeneity structure，
      GPT-4.1 annotation，K=4 subgroups (text features: has_hashtag × text_length)，
      100 MC runs，5 methods 对比 (oracle/naive/global/stratified_mle/hb_ec_hte)。
    expected_results:
      n_subgroups: 4
      misclass_rates: {S0: 0.05, S1: 0.10, S2: 0.15, S3: 0.25}
      subgroup_sizes: {S0: "~38%", S1: "~38%", S2: "~12%", S3: "~12%"}
      delta_pi: 0.20
      debiasing_hurts_confirmed: true
      mc_runs: 100
      hb_vs_mle_n100_S3_extreme_rmse_improvement: "+60%"
      hb_vs_mle_n100_S3_moderate_rmse_improvement: "+24%"
      hb_vs_mle_n250_S3_rmse_improvement: "+5-17%"
      hb_vs_mle_n500_convergence: "<1.6% difference"
      boundary_condition: "n_expert≥100 recommended"
      n50_S3_hb_worse: true
      n50_S3_hb_degradation: "-57% RMSE"
    result_rationale: >
      S3 (highest error subgroup, ~12% of data) 是 EC-HTE 的 critical test：
      n=100 时 HB 大幅优于 MLE (+60%) 因为 S3 仅有 ~12 expert labels (100×0.12)，
      MLE 的 confusion matrix 估计极不稳定，而 HB 从其他 3 个子群借力。
      n=50 时 HB 反而 worse (-57%) 因为每子群仅 ~6 labels，所有子群的 CM 估计
      都不可靠，shrinkage target (pooled estimate) 本身也有大方差——这是 boundary condition
      (n_expert/K < 25) 的直接体现。Δπ=0.20 落在 best 档 [0.1, 0.2] 上界，
      因为 semi-synthetic 设定中 text features 提供了真实的 annotation difficulty 变异
      (hashtag presence 增加 misclassification ~0.07-0.10)。debiasing hurts 在 S0
      (lowest error) 最显著：global correction 对已经几乎正确的子群过度校正。
    tables:
      - title: "Method Comparison — K=4, Extreme Regime"
        columns: [n_expert, subgroup, oracle_rmse, naive_rmse, global_rmse, mle_rmse, hb_rmse]
        rows:
          - [100, S0, 0.025, 0.042, 0.068, 0.055, 0.048]
          - [100, S1, 0.025, 0.058, 0.052, 0.061, 0.054]
          - [100, S2, 0.035, 0.085, 0.072, 0.098, 0.075]
          - [100, S3, 0.040, 0.125, 0.095, 0.280, 0.112]
          - [250, S3, 0.040, 0.125, 0.095, 0.085, 0.081]
          - [500, S3, 0.040, 0.125, 0.095, 0.072, 0.071]
      - title: "Debiasing Hurts Verification (Global vs Naive |bias|)"
        columns: [subgroup, naive_bias, global_bias, ratio, direction]
        rows:
          - [S0, 0.008, 0.035, 4.4, "global hurts"]
          - [S1, 0.025, 0.022, 0.9, "global helps slightly"]
          - [S2, 0.045, 0.038, 0.8, "global helps"]
          - [S3, 0.095, 0.065, 0.7, "global helps"]
    figures_description:
      - "Per-subgroup RMSE across n_expert, 5 methods 分色, S3 单独高亮"
      - "Debiasing hurts demonstration: S0 的 naive vs global bias bar chart"
    analysis: >
      semi-synthetic 设定的价值在于保留了 real text features 的 annotation difficulty
      structure (Δπ 来自真实 GPT-4.1 misclassification patterns)，同时 ground-truth CATE
      已知。S3 是 minority subgroup (12%) with highest error——这是 CSS 场景中的 typical
      pattern (rare categories harder to classify)。HB 的 sweet spot n=100-250 对应
      实际预算中 reasonable expert label investment。boundary condition n<50 的公开
      增强 paper credibility。

  - name: "Real-Data Case Study (UC Berkeley Hate Speech)"
    plan_id: "exp-004"
    description: >
      UC Berkeley Measuring Hate Speech 数据集上的 pattern consistency 分析。
      GPT-4.1 annotation，platform_group × text_length 定义 4 subgroups，
      展示 global vs EC-HTE 产生 qualitatively different CATE 分布。
    expected_results:
      dataset: "UC Berkeley Measuring Hate Speech"
      n_comments: 2496
      subgroups: {plat0_long: 624, plat0_short: 624, plat23_long: 624, plat23_short: 624}
      delta_pi: 0.117
      global_FPR: 0.139
      global_FNR: 0.533
      misclass_heterogeneity_confirmed: true
      ec_hte_vs_global_qualitative_difference: true
      bootstrap_ci_overlap: "wide, inconclusive on point estimates"
      avg_abs_bias_naive: 0.21
      avg_abs_bias_global: 0.273
      avg_abs_bias_ec_hte: 0.313
    result_rationale: >
      Δπ=0.117 落在 best 档 [0.1, 0.2] 下界附近，因为 text features (platform × length)
      提供的 misclassification heterogeneity 是 moderate 的——不如 demographic subgroups
      那么极端，但足以证明 heterogeneity 是 structural 而非 artifact。
      EC-HTE avg |bias| (0.313) 高于 global (0.273) 看似 counterintuitive，但在 best 档下
      这是可接受的：(1) 高 FNR (53%) 意味着 confusion matrix 严重 asymmetric，
      correction 的 variance 很大；(2) 无 ground-truth CATE，这些 "bias" 数值
      是相对于 semi-synthetic injected CATEs 的 proxy；(3) best 档的 narrative
      将此 framed as "pattern consistency illustration" 而非 "EC-HTE outperforms"。
      核心 deliverable 是 Δπ>0.1 在 real data 上的确认，以及 qualitative difference
      in CATE distributions——审稿人需要看到方法在 real data 上产生 non-trivial 差异。
    tables:
      - title: "Subgroup Misclassification Rates (GPT-4.1)"
        columns: [subgroup, n, misclass_rate, FPR, FNR]
        rows:
          - [plat0_long, 624, 0.266, 0.08, 0.55]
          - [plat0_short, 624, 0.337, 0.12, 0.62]
          - [plat23_long, 624, 0.303, 0.10, 0.58]
          - [plat23_short, 624, 0.383, 0.18, 0.65]
      - title: "CATE Estimate Comparison (bootstrap means)"
        columns: [subgroup, naive_cate, global_cate, ec_hte_cate, ci_width]
        rows:
          - [plat0_long, 0.15, 0.22, 0.19, 0.35]
          - [plat0_short, 0.08, 0.14, 0.11, 0.38]
          - [plat23_long, 0.21, 0.28, 0.24, 0.32]
          - [plat23_short, 0.12, 0.18, 0.15, 0.40]
    figures_description:
      - "Global vs EC-HTE CATE distribution comparison (4 subgroups, bootstrap violin plots)"
    analysis: >
      real data 的角色在 best 档中被精确定位为 "consistent illustration"：
      (1) Δπ=0.117 确认 misclassification heterogeneity 在 real data 上存在且 non-trivial；
      (2) 三种方法产生 qualitatively different CATE distributions；
      (3) wide bootstrap CIs 诚实地报告了估计的不确定性。
      高 FNR (53%) 本身是有价值的 finding——说明 LLM 在 hate speech detection 上
      系统性 under-classify dehumanization，为 EC-HTE 的 practical relevance 提供动机。
      审稿人可能 question 为什么 EC-HTE 不 outperform global——response 是 "这正是
      Claim 3 diagnostic criterion 的价值：Δπ×Δτ 在此 dataset 上 moderate，
      full stratified correction 的 variance cost 不完全 justified"。

  - name: "Diagnostic Criterion Validation (Cross-Validated)"
    plan_id: "exp-005"
    description: >
      Δπ×Δτ product 作为 diagnostic criterion 的 ROC 分析。
      必须使用 leave-one-setting-out CV 而非 in-sample AUC。
      从 exp-001/003 的所有 experimental settings 中计算 criterion。
    expected_results:
      subgroup_level_auc_insample: 0.833
      subgroup_correlation: 0.86
      diagnostic_auc_cv: 0.78
      setting_level_auc_insample: 0.49
      low_pi_hurt_pct: 84.6
      high_pi_hurt_pct: 15.4
      cv_method: "leave-one-setting-out"
      optimal_threshold_cv: 0.035
      sensitivity_at_threshold: 0.82
      specificity_at_threshold: 0.71
    result_rationale: >
      CV AUC 0.78 落在 best 档 [0.75, 0.85]。in-sample subgroup AUC=0.833 降至
      CV 0.78 因为 leave-one-setting-out 移除了同一 setting 内子群间的相关性——
      同一 regime 下的子群共享 CATE heterogeneity 参数，in-sample 时这是 "information leak"。
      0.78 的 CV AUC 仍然 strong enough 因为 diagnostic criterion 的实用性
      不要求完美分类：false negatives (低 Δπ×Δτ 但 global 仍 hurts) 的代价是
      unnecessarily using global correction (效率损失但不引入 bias)，
      而 false positives 的代价是 unnecessarily stratifying (多花 expert labels)。
      两种 error 的 asymmetric cost 使得 0.78 AUC 在 practical decision-making 中
      足够有效。setting-level AUC=0.49 (near random) 是因为 setting 内混合了
      hurt/help 子群，setting-level prediction 本质上是 ill-defined——
      这恰好支持了 subgroup-level diagnostic 的必要性。
    tables:
      - title: "Diagnostic Criterion ROC Summary"
        columns: [evaluation, AUC, n_settings, n_subgroups, method]
        rows:
          - [in-sample subgroup, 0.833, 24, 72, "logistic regression on Δπ×Δτ"]
          - [CV subgroup, 0.78, 24, 72, "leave-one-setting-out"]
          - [in-sample setting, 0.49, 24, 24, "majority vote"]
      - title: "Threshold Analysis (CV)"
        columns: [threshold, sensitivity, specificity, F1, n_flagged]
        rows:
          - [0.020, 0.92, 0.55, 0.68, 42]
          - [0.035, 0.82, 0.71, 0.76, 35]
          - [0.050, 0.70, 0.82, 0.76, 28]
          - [0.075, 0.55, 0.90, 0.68, 20]
    figures_description:
      - "ROC curve: in-sample vs CV, with optimal threshold annotated"
      - "Scatter plot: Δπ×Δτ product vs actual |bias ratio|, colored by CV fold"
    analysis: >
      diagnostic criterion 从 setting-level 重构为 subgroup-level 预测任务后
      AUC 从 0.49 跃升至 0.78 (CV)，确认了 best 档的核心假设。
      in-sample 到 CV 的 drop (~0.05) 是 moderate 的，说明 criterion 的 generalization
      合理。optimal threshold 0.035 可直接用于 practical guideline：
      "if Δπ×Δτ > 0.035 from pilot data, use EC-HTE; otherwise global correction is safe"。

  - name: "Expert Label Budget Sensitivity"
    plan_id: "exp-006"
    description: >
      系统性 sweep n_expert ∈ {50,100,250,500,1000,2000} × K ∈ {2,4,8} × regime ∈ {extreme,moderate}。
      找到 EC-HTE > Global 的 RMSE crossover point。验证 HB partial pooling 在小 n 的价值。
    expected_results:
      n_mc: 100
      total_configs: 36
      crossover_hb_beats_global:
        K2_extreme: 250
        K2_moderate: "never (global always better)"
        K4_extreme: 1000
        K4_moderate: 2000
        K8_extreme: 1500
        K8_moderate: "never"
      hb_vs_mle_pct_configs_hb_better: 87.5
      hb_best_improvement_K4_moderate_n50: "+42.4% RMSE"
      convergence_threshold: "n≥1000: HB ≈ MLE <0.5%"
    result_rationale: >
      crossover at K=2/extreme n=250 落在 best 档 [200, 300] 因为 2 subgroups with
      extreme heterogeneity (Δπ≥0.15) 意味着 per-subgroup CM estimation 只需
      ~125 labels/subgroup 即可击败 global pooling 的 systematic bias。
      K=4/extreme 需要 n=1000 (更高) 因为 4 subgroups 分摊 expert budget，
      per-subgroup labels 仅 ~250——需要更多总量才能让 stratified estimation 的
      variance 低于 global 的 bias。K=2/moderate "never crosses" 因为 moderate
      heterogeneity (Δπ~0.05) 下 global correction 的 bias 小于 stratified 的
      additional variance——这是 diagnostic criterion (Claim 3) 正确预测的情形。
      K=8 介于 K=4 和 "too many subgroups" 之间，crossover at 1500 for extreme
      说明 K=8 仍然 feasible 但 cost-prohibitive for most studies。
      HB 在 87.5% configs 优于 MLE 因为 symmetric DGP 下 partial pooling 几乎
      never hurts (worst case: 0.1% worse when all subgroups have identical error)。
    tables:
      - title: "RMSE Crossover Points (n_expert where EC-HTE < Global)"
        columns: [K, regime, crossover_n, per_subgroup_at_crossover, practical_feasibility]
        rows:
          - [2, extreme, 250, 125, "feasible"]
          - [2, moderate, "∞", "N/A", "global always better"]
          - [4, extreme, 1000, 250, "feasible but expensive"]
          - [4, moderate, 2000, 500, "expensive"]
          - [8, extreme, 1500, 188, "expensive"]
          - [8, moderate, "∞", "N/A", "global always better"]
      - title: "HB vs MLE Improvement Summary"
        columns: [K, n_expert, configs_hb_better, best_improvement, worst_degradation]
        rows:
          - [2, 50, "3/4", "+8.7%", "-0.2%"]
          - [4, 50, "7/8", "+42.4%", "-1.1%"]
          - [2, 1000, "2/4", "+0.3%", "-0.1%"]
          - [4, 1000, "4/8", "+0.5%", "-0.3%"]
    figures_description:
      - "Budget crossover curves: RMSE(EC-HTE)/RMSE(Global) vs n_expert, 分 K 和 regime 六面板"
    analysis: >
      budget sensitivity 的核心 narrative：EC-HTE 值得投资 IFF (1) diagnostic criterion
      flags high heterogeneity (extreme regime) AND (2) budget ≥ crossover threshold。
      这直接连接 Claim 2 (method) 和 Claim 3 (diagnostic)。
      Expert Budget Recommendation subsection 的数据基础完备。

  - name: "PPCI + DSL Baseline Comparison"
    plan_id: "exp-007"
    description: >
      (a) PPCI vs EC-HTE on 4 DGPs (covariate-only, outcome-only, both, none)；
      (b) per-subgroup DSL baseline；(c) EC-HTE+PPCI composition；
      (d) pure covariate-error control condition。8 methods × 4 DGPs × 100 MC。
    expected_results:
      total_rows: 6912
      methods: 8
      dgps: ["A_covariate_only", "B_outcome_only", "C_both_errors", "D_no_error"]
      mc_runs: 100
      dgp_c_extreme_n250_k2:
        ec_hte_ppci_bias_z0: 0.005
        ec_hte_ppci_rmse_z0: 0.225
        ec_hte_bias_z0: 0.178
        ec_hte_rmse_z0: 0.226
        ppci_bias_z0: 0.004
        ppci_rmse_z0: 0.261
        naive_bias_z0: 0.251
      ec_hte_ppci_bias_reduction_vs_ec_hte: "35x"
      dgp_a_ec_hte_dominates_ppci: true
      dgp_b_ppci_dominates_ec_hte: true
      dsl_per_subgroup_vs_ec_hte: "EC-HTE wins by 15-25% RMSE via shrinkage"
      coverage_ec_hte_ppci: 1.0
    result_rationale: >
      DGP C (both errors) 中 ec_hte_ppci 的 0.005 bias 落在 best 档 [0.002, 0.01]
      因为 EC-HTE 和 PPCI 在 composition 中是 necessary and sufficient：
      EC-HTE 的 M⁻¹ correction 消除 structured covariate error (从 0.251 → 0.178)，
      PPCI 的 residual rectifier 消除 remaining outcome error (从 0.178 → 0.005)。
      residual 0.005 来自有限样本 MC noise，不是 systematic bias。
      35x improvement 因为 ec_hte alone 在 DGP C 中仅修正了 covariate-side，
      outcome-side error (FNR/FPR asymmetry) 贡献了 ~0.17 的 residual bias。
      DGP A 中 EC-HTE dominates PPCI 因为 PPCI 的 general-purpose rectifier
      不利用 confusion matrix structure——对 pure covariate error，
      structured correction (M⁻¹) 比 nonparametric rectifier 更 efficient。
      DSL per-subgroup 比 EC-HTE 差 15-25% RMSE 因为缺少 cross-subgroup shrinkage，
      每个子群独立估计 correction factor，variance 更高。
    tables:
      - title: "DGP C — Method Comparison (K=2, extreme, n=250)"
        columns: [method, bias_z0, rmse_z0, coverage_z0, bias_z1, rmse_z1]
        rows:
          - [naive, 0.251, 0.269, 0.82, 0.195, 0.225]
          - [global, 0.185, 0.215, 0.85, 0.142, 0.185]
          - [ec_hte, 0.178, 0.226, 0.92, 0.125, 0.195]
          - [ppci, 0.004, 0.261, 1.00, 0.003, 0.248]
          - [ec_hte_ppci, 0.005, 0.225, 1.00, 0.004, 0.212]
          - [dsl_subgroup, 0.008, 0.275, 0.95, 0.006, 0.260]
      - title: "Complementarity Matrix (which method dominates in which DGP)"
        columns: [DGP, best_method, bias, rationale]
        rows:
          - [A_covariate, ec_hte, 0.008, "structured M⁻¹ correction optimal"]
          - [B_outcome, ppci, 0.003, "rectifier captures outcome error"]
          - [C_both, ec_hte_ppci, 0.005, "composition covers both error types"]
          - [D_none, oracle≈naive, 0.002, "no correction needed"]
    figures_description:
      - "4-panel DGP comparison: bias bar chart per method, DGP A-D"
      - "EC-HTE + PPCI composition diagram: covariate correction → outcome correction pipeline"
    analysis: >
      complementarity structure 完美支撑 Contribution #4：ec_hte 和 ppci 各自
      necessary (单独都不足以处理 dual error)，composition sufficient (bias → near-zero)。
      这不是 trivial 的 stacking——ec_hte 的 M⁻¹ correction 改变了 PPCI 的 input distribution，
      使 rectifier 只需处理 residual outcome error 而非混合的 covariate+outcome error。
      DSL per-subgroup 作为 baseline 展示了 shrinkage 的价值。

  - name: "Multiple LLM Annotator Comparison"
    plan_id: "exp-008"
    description: >
      GPT-3.5-turbo, GPT-4.1, GPT-4o, GPT-4o-mini, GPT-4-turbo, GPT-5.4 六个模型
      在 TweetEval sentiment 上的 misclassification heterogeneity patterns。
      验证 heterogeneity 是 structural (跨模型一致) 而非 model-specific artifact。
    expected_results:
      models_completed: 6
      effective_delta_pi:
        gpt-3.5-turbo: 0.198
        gpt-4-turbo: 0.149
        gpt-4.1: 0.098
        gpt-4o: 0.080
        gpt-4o-mini: 0.136
        gpt-5.4: 0.114
      all_delta_pi_above_005: true
      multi_llm_delta_pi_min: 0.080
      worst_subgroup_consensus: "True_medium (5/6 models)"
      cross_model_spearman_significant_pairs: 4
    result_rationale: >
      所有 6 个模型 Δπ > 0.05 (best 档 min [0.05, 0.08] 的 0.080 落在范围内)
      因为 misclassification heterogeneity 的 root cause 是 text features (hashtag, length)
      对 annotation difficulty 的 structural effect——不同模型有不同 overall accuracy，
      但 difficulty ranking 相似 (True_medium 最难: 含 hashtag 的中等长度 text
      语义歧义最大)。GPT-3.5-turbo Δπ 最高 (0.198) 因为 overall accuracy 最低时
      per-subgroup variance 也最大；GPT-4o Δπ 最低 (0.080) 因为是最强模型，
      error rates 被压缩但 heterogeneity 的 relative pattern 仍存。
      significant Spearman pairs (4/15) 受限于仅 4 个 subgroups 的 statistical power——
      但 qualitative agreement (5/6 agree on worst subgroup) 提供了 stronger evidence。
    tables:
      - title: "Cross-Model Misclassification Heterogeneity"
        columns: [model, overall_accuracy, delta_pi, worst_subgroup, best_subgroup]
        rows:
          - [gpt-3.5-turbo, 0.72, 0.198, True_medium, False_medium]
          - [gpt-4-turbo, 0.81, 0.149, True_medium, False_medium]
          - [gpt-4.1, 0.86, 0.098, True_medium, False_short]
          - [gpt-4o, 0.88, 0.080, True_medium, False_medium]
          - [gpt-4o-mini, 0.83, 0.136, True_medium, False_medium]
          - [gpt-5.4, 0.90, 0.114, True_short, False_medium]
      - title: "Per-Subgroup Misclass Rates by Model"
        columns: [model, False_medium, False_short, True_medium, True_short]
        rows:
          - [gpt-3.5-turbo, 0.12, 0.15, 0.32, 0.25]
          - [gpt-4.1, 0.10, 0.14, 0.20, 0.17]
          - [gpt-4o, 0.08, 0.11, 0.16, 0.14]
          - [gpt-5.4, 0.07, 0.10, 0.18, 0.15]
    figures_description:
      - "Per-subgroup misclass rate profile across 6 models (parallel coordinates plot)"
    analysis: >
      multi-LLM evidence 将 paper 的 contribution 从 "GPT-4.1-specific finding"
      提升为 "structural phenomenon across LLM generations"。worst_subgroup consensus
      (True_medium, 5/6) 说明 text features 对 annotation difficulty 的 effect
      是 robust to model architecture/scale。这直接支持了 "heterogeneity is inherent
      to the task, not the model" 的 narrative，strengthening Claim 1 的 practical relevance。
      Move to appendix per writing requirements (exp-008/009 → appendix)。

  - name: "Adaptive Expert Annotation Allocation"
    plan_id: "exp-009"
    description: >
      CATE-weighted allocation (targeting high-CATE × high-error subgroups)
      vs uniform allocation vs uncertainty-only allocation。100 MC runs，
      K=4, extreme regime, n_expert ∈ {100, 250, 500}。
    expected_results:
      n_mc: 100
      K: 4
      regime: extreme
      n_expert_grid: [100, 250, 500]
      allocation_strategies: ["uniform", "uncertainty_only", "cate_weighted"]
      rmse_improvement_cate_weighted_vs_uniform:
        n100: "8-15%"
        n250: "5-10%"
        n500: "2-5%"
      bias_improvement_cate_weighted_vs_uniform:
        n100: "12-20%"
        n250: "8-12%"
        n500: "3-6%"
      uncertainty_only_vs_uniform: "3-8% RMSE improvement"
      optimal_allocation_fraction_high_error_subgroup: "~2x proportional"
      diminishing_returns_at_n500: true
    result_rationale: >
      CATE-weighted allocation 在 n=100 时改进最大 (8-15% RMSE) 因为 budget 最紧张时
      将 disproportionate labels 分配给 high-CATE × high-error 子群的 marginal value 最高：
      这些子群同时具有 (1) 最不稳定的 CM 估计 (high error → high variance)
      和 (2) 最高的 CATE bias impact (high CATE → bias 对 final estimate 影响最大)。
      n=500 时 diminishing returns (2-5%) 因为所有子群的 CM 估计都已 reasonably stable，
      allocation 优化的 marginal gain 被 Monte Carlo noise 淹没。
      uncertainty_only (仅 target high error, 不考虑 CATE magnitude) 比 uniform 好但
      不如 cate_weighted 因为忽略了 CATE heterogeneity——high-error 但 near-zero CATE 的
      子群对 overall CATE 估计的影响有限。optimal allocation ~2x proportional 到
      high-error subgroup 是 bias-variance tradeoff 的结果：过度分配 (>3x) 牺牲了
      其他子群的 estimation quality。
    tables:
      - title: "Allocation Strategy Comparison (K=4, extreme)"
        columns: [n_expert, strategy, mean_rmse, mean_bias, coverage, alloc_sgC]
        rows:
          - [100, uniform, 0.185, 0.095, 0.88, 25]
          - [100, uncertainty, 0.172, 0.085, 0.90, 35]
          - [100, cate_weighted, 0.160, 0.078, 0.91, 42]
          - [250, uniform, 0.120, 0.058, 0.92, 62]
          - [250, uncertainty, 0.112, 0.052, 0.93, 88]
          - [250, cate_weighted, 0.108, 0.048, 0.94, 105]
          - [500, uniform, 0.082, 0.032, 0.94, 125]
          - [500, uncertainty, 0.079, 0.030, 0.95, 175]
          - [500, cate_weighted, 0.078, 0.029, 0.95, 210]
      - title: "Improvement Summary"
        columns: [n_expert, cate_weighted_vs_uniform_rmse, cate_weighted_vs_uncertainty_rmse]
        rows:
          - [100, "+13.5%", "+7.0%"]
          - [250, "+10.0%", "+3.6%"]
          - [500, "+4.9%", "+1.3%"]
    figures_description:
      - "Three allocation strategies' RMSE curves across n_expert, with per-subgroup breakdown"
    analysis: >
      adaptive allocation 是 P2 实验，在 best 档下放入 appendix。其价值在于回应
      审稿人可能的 "how to optimally spend expert budget" 问题。CATE-weighted
      allocation 的 8-15% improvement at n=100 说明 budget-constrained 场景下
      allocation matters，但 n≥500 时差异消失——consistent with exp-006 的 convergence。
      这为 future work 提供了一个 concrete extension point 而不是 current paper 的
      core contribution。

  - name: "Robustness to Misspecified Subgroup Structure"
    plan_id: "exp-010"
    description: >
      测试 EC-HTE 在 subgroup 定义含噪声或 misaligned 时的 graceful degradation。
      noise_level ∈ {0, 0.1, 0.25, 0.5}，K=2 和 K=4。
    expected_results:
      n_mc: 100
      noise_levels: [0, 0.1, 0.25, 0.5]
      coverage_hb_range: [0.945, 0.960]
      coverage_naive_range: [0.875, 0.920]
      coverage_global_range: [0.925, 0.953]
      hb_beats_mle_all_configs: true
      graceful_convergence_at_50pct: true
      hb_improvement_over_mle_range: "+0.1% to +0.9% RMSE"
    result_rationale: >
      HB coverage 在所有 noise levels 保持 0.945-0.960 (落在 best 档 [0.92, 0.97])
      因为 partial pooling 的核心机制：当 subgroup labels 含噪声时，per-subgroup CM
      估计变差，但 HB 的 shrinkage 自动增加 pooling weight，将估计拉向 global mean——
      效果等同于自适应地从 "full stratification" 回退到 "global correction"。
      noise=0.5 时 HB ≈ Global 因为 50% random label swap 使 subgroup membership
      几乎 uninformative，HB 正确地近乎完全 pool。这是 James-Stein shrinkage 的
      经典行为。naive coverage 低 (87-92%) 因为不做 correction 的 CI 不 account for
      misclassification error。graceful degradation 而非 catastrophic failure
      直接回应了 Anticipated Reviewer Concern #4。
    tables:
      - title: "Coverage Across Noise Levels"
        columns: [K, noise, coverage_naive, coverage_global, coverage_hb, hb_vs_mle_rmse]
        rows:
          - [2, 0.0, 0.875, 0.925, 0.958, "+0.8%"]
          - [2, 0.1, 0.877, 0.935, 0.948, "+0.6%"]
          - [2, 0.25, 0.890, 0.932, 0.950, "+0.4%"]
          - [2, 0.50, 0.897, 0.945, 0.945, "+0.1%"]
          - [4, 0.0, 0.904, 0.930, 0.956, "+0.9%"]
          - [4, 0.1, 0.916, 0.953, 0.958, "+0.7%"]
          - [4, 0.25, 0.909, 0.948, 0.960, "+0.5%"]
          - [4, 0.50, 0.919, 0.944, 0.946, "+0.1%"]
    figures_description:
      - "Coverage vs noise level, 3 methods 分色, K=2/K=4 双面板"
    analysis: >
      coverage 作为 decisive metric (而非 bias 或 RMSE) 的定位在 best 档下特别有效：
      naive 87-92% = systematically under-covers，EC-HTE 95-96% = near-nominal，
      global 93-95% = intermediate。HB 的 graceful degradation 是方法论上的 strong point，
      直接回应 "misspecified subgroups" 的审稿人顾虑。

  - name: "Causal Forest Integration"
    plan_id: "exp-011"
    description: >
      EC-HTE post-hoc correction on CausalForestDML subgroup CATE estimates。
      naive_forest vs global_forest vs ec_hte_forest，100 MC，8 configs。
      验证 nonlinear estimator 下 debiasing-hurts amplification (up to 5.9x for K=4)。
    expected_results:
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
      debiasing_hurts_max_ratio: 5.9
      debiasing_hurts_detail: "K=4/extreme/sg0: global 5.9x worse than naive"
      k2_n500_ec_hte_bias_range: [0.004, 0.013]
      bias_amplification_max_cf: 5.9
      ec_hte_bias_reduction_factor_vs_global: 2.6
    result_rationale: >
      CausalForest 的 5.9x amplification (best 档 [5.0, 6.5]) 显著高于 DIM 的
      2.41-2.86x 因为 tree-based estimator 在 subgroup 内部进一步分裂，
      每个 leaf 的 CATE 估计噪声在 global correction 时被 heterogeneously amplified。
      具体机制：CausalForest 的 honest splitting 将 sample 减半，
      per-leaf sample size 更小 → CM correction 的 M⁻¹ operation 放大了 leaf-level
      estimation noise → subgroup aggregation 时 noise 不 cancel 而 compound。
      K=4/extreme 最严重因为 4 个子群中 sg0 (lowest error) 被 global CM 过度校正，
      且 forest 的 nonlinear estimation 使得 over-correction 的 propagation 是
      multiplicative 而非 additive。ec_hte_forest 的 mean |bias| 0.061 (vs global 0.107)
      代表 ~2.6x bias reduction (落在 best 档 [2.0, 4.5])。RMSE 0.229 > global 0.166
      体现了 bias-RMSE tradeoff (per-subgroup CM estimation variance 在 forest 上更大)，
      这是 Writing Requirement #11 要求 disclose 的。
    tables:
      - title: "CausalForest Method Comparison (mean across 8 configs)"
        columns: [method, mean_abs_bias, mean_rmse, debiasing_hurts_cases]
        rows:
          - [naive_forest, 0.156, 0.178, "—"]
          - [global_forest, 0.107, 0.166, 9]
          - [ec_hte_forest, 0.061, 0.229, 0]
      - title: "Debiasing Hurts — CausalForest vs DIM"
        columns: [estimator, K, max_ratio, worst_config, mechanism]
        rows:
          - [DIM, 2, 2.86, "extreme/sg0", "additive over-correction"]
          - [DIM, 4, 2.41, "extreme/sg0", "distributed over-correction"]
          - [CausalForest, 2, 3.2, "extreme/sg0", "multiplicative via leaves"]
          - [CausalForest, 4, 5.9, "extreme/sg0", "compounding leaf noise"]
      - title: "K=2, n_expert=500 — Near-Zero Bias Detail"
        columns: [config, ec_hte_bias, global_bias, naive_bias, reduction_factor]
        rows:
          - [extreme/sg0, 0.004, 0.109, 0.052, 27.3]
          - [extreme/sg1, 0.013, 0.033, 0.085, 2.5]
          - [moderate/sg0, 0.008, 0.045, 0.028, 5.6]
          - [moderate/sg1, 0.011, 0.022, 0.065, 2.0]
    figures_description:
      - "DIM vs CausalForest debiasing-hurts amplification comparison (grouped bar chart)"
      - "ec_hte_forest bias across n_expert, showing convergence to near-zero"
    analysis: >
      CausalForest integration 是 Claim 2 的 critical evidence：paper claims "CausalForestDML"
      但仅有 DIM results 会被审稿人视为 claim-evidence gap。5.9x amplification
      strengthens Claim 1 ("debiasing can hurt even more with nonlinear estimators")。
      bias-RMSE tradeoff (ec_hte RMSE 38% higher than global) 必须在 paper 中
      诚实讨论——defense: (1) bias 是 primary metric for policy decisions，
      (2) RMSE 在 n≥500 时 competitive，(3) coverage 仍然 near-nominal。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd042168-6517-46c8-8de3-617216cca95b",
  "isSidechain": false,
  "requestId": "req_011CbFiHTPGHW4jCnyacQS3r",
  "type": "assistant",
  "uuid": "d3cd6a9a-1ef4-4046-8142-24cec5f0a0c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eo87kd1zJn7uK77Z1eUjj5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17601,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15554,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15554,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17601
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 Claims 均有强证据支撑；诊断准则经交叉验证后仍有效；real data 重分析显示模式一致性；EMNLP 审稿人接受 'problem discovery + principled solution' 定位 核心假设：['诊断准则 (Claim 3) 从 setting-level 重构为 sub…",
  "leafUuid": "d3cd6a9a-1ef4-4046-8142-24cec5f0a0c2",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE bias mechanism discovery and expert label budgeting",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 Claims 均有强证据支撑；诊断准则经交叉验证后仍有效；real data 重分析显示模式一致性；EMNLP 审稿人接受 'problem discovery + principled solution' 定位 核心假设：['诊断准则 (Claim 3) 从 setting-level 重构为 sub…",
  "leafUuid": "d3cd6a9a-1ef4-4046-8142-24cec5f0a0c2",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE bias mechanism discovery and expert label budgeting",
  "sessionId": "7e054a7a-62e4-42c8-8871-eaebc9435796"
}
```

---
