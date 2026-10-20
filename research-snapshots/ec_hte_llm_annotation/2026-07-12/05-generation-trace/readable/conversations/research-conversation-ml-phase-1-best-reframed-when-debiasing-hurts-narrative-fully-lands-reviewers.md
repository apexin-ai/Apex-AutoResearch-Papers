# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Reframed 'When Debiasing Hurts' narrative fully lands：reviewers认为 problem id

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/d268f21e-aa46-498b-a290-5def6c522697.jsonl`
- **Structured JSON:** [`62d1ddad544c7e0b5b05.json`](../../sessions/62/62d1ddad544c7e0b5b05.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T19:33:37.783Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T19:33:37.783Z",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Reframed 'When Debiasing Hurts' narrative fully lands：reviewers认为 problem identification 本身是 EMNLP 级贡献，bias identity 的 exact 形式在 LLM annotation 语境下被接受为新颖，EC-HTE 在其 operating regime 内的表现被视为 convincing proof of concept\n核心假设：['NLP/CSS-oriented reviewer panel，对 classical measurement error 文献（Fuller/Carroll）不深度熟悉，因此 bias identity 在 LLM annotation 语境下的 formalization 被视为新颖贡献', \"'Debiasing can hurt' 的 framing 对 NLP 社区足够 surprising——多数 NLP 工作假设 correction 单调改善，reviewer 认同这是 under-recognized failure mode\", 'EC-HTE 的 conditional advantage（extreme heterogeneity + n_expert≥250）被接受为 practical regime——reviewer 认同 CSS 场景中 Δπ>0.10 是常见的（exp-008: 6/6 models Δπ>0.05）', 'Real-data R²=0.944（14 LLM-dataset combos）被视为 strong pattern validation，不要求 ground-truth CATE benchmark', 'Honest limitations disclosure（RMSE tradeoff、K≥8 boundary、real CM negative results）增强可信度而非减分', \"Reviewer 不要求 convergence rates 或 minimax bounds——'problem identification + exact identity + diagnostic' 被接受为完整贡献\"]\n关键指标范围：{'excitement': [4.0, 4.5], 'soundness': [3.5, 4.0], 'overall_recommendation': [3.5, 4.0], 'claim1_bias_identity_accepted_pct': [90, 100], 'claim2_echte_accepted_as_useful_pct': [70, 85], 'claim3_diagnostic_accepted_pct': [65, 80], 'perceived_novelty_score': [3.5, 4.5], 'major_weaknesses_per_review': [0, 1], 'revision_requests': ['minor (figures, writing clarity, bibliography)']}\n叙事方向：原始 reframed claims 完全成立。三条贡献层次清晰：(1) bias identity 是 exact 且 constructive，直接揭示 LLM annotation pipeline 中被忽视的 failure mode；(2) EC-HTE 是 identity 自然推导出的修正方案，在 high-heterogeneity regime 效果显著（bias reduction 4-15x，coverage 恢复至 95%）；(3) Δπ×Δτ diagnostic 提供 zero-cost 预检，让 practitioner 不用跑 EC-HTE 也能判断 global correction 是否安全。Abstract 可保留 '2-3x median amplification, up to 5.9x' headline。PPCI 互补性作为 bonus contribution。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ec_hte_llm_annotation\nvenue: emnlp-2026\nfocus: Reframed paper: title changed to \"When Debiasing Hurts\", core contributions shifted from EC-HTE method to (1) exact bias identity + (2) actionable diagnostic. EC-HTE de-emphasized as \"the correction prescribed by the identity.\" New real-data validation on CivilComments (R²=0.944, 14 LLM-dataset combinations). Evaluate whether this framing shift improves Excitement scores vs previous 3/3.5 baseline.\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 2-3x (median across configurations), with amplification up to 5.9x for K=4 subgroups; when naive bias is near zero, global correction creates bias where none existed. For the difference-in-means estimator, the amplification magnitude does NOT monotonically increase with K (K=2 extreme: up to 2.86× vs K=4 extreme: up to 2.41×); however, with nonlinear estimators such as CausalForest, more subgroups amplify the effect substantially (K=4/extreme: up to 5.9×) due to compounding estimation noise in tree-based CATE. Global correction increases subgroup-level bias in ~50% of the parameter space.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) substantially reduces subgroup-level bias when misclassification heterogeneity is sufficiently high, while controlling estimation variance through partial pooling. HB provides meaningful RMSE reduction by borrowing strength across groups (classic James-Stein shrinkage). We provide precise crossover thresholds: EC-HTE outperforms global correction in RMSE with as few as 250 expert labels (K=2, high heterogeneity), scaling to ~1000 for K=4. **Boundary condition**: when expert labels per subgroup < ~25, shrinkage can be harmful — stratified MLE is preferred. **EC-HTE is most valuable precisely when it is most needed — the diagnostic criterion (Claim 3) identifies these scenarios.** **CONFIRMED** by exp-003 full 100 MC (1200 runs, 0 errors). HB crossover at ~11 experts/subgroup; ≥25 recommended for robust performance. Demonstrated with both difference-in-means and CausalForestDML (exp-011: consistent bias reduction pattern, ec_hte_forest |bias|=0.06 vs naive 0.16). CausalForest amplifies the debiasing-hurts effect (up to 5.9x in K=4/extreme) due to nonlinear CATE estimation.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic that simultaneously predicts when global correction is harmful (Claim 1) and when the expert label investment for stratified correction is worthwhile (connecting to the budget guidelines from Claim 2). This criterion has standalone value independent of EC-HTE — even without adopting EC-HTE, knowing when global correction backfires is practically actionable.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis across computational social science (CSS) — e.g., sentiment framing moderates message effectiveness, hate speech type moderates intervention impact. LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education; documented across CSS tasks including sentiment, stance, toxicity). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as \"problem identification + principled solution\" not \"new estimation technique.\"\n\n- **Headline result template**: \"On semi-synthetic CSS benchmarks, global correction worsens subgroup CATE bias by 2-3x (median), with amplification up to 5.9x for K=4 subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels. Combined with PPCI, the composition achieves near-zero bias (0.005) even when both covariate and outcome errors are present.\"\n\n- **Oracle framing**: When reporting DGP C results where ec_hte_ppci outperforms oracle, always use \"covariate-oracle\" (true Z + observed Y), never unqualified \"oracle\". Frame as \"composite correction is necessary and sufficient when both error types coexist\" — NOT \"beats oracle\". The result is by construction (ec_hte_ppci corrects both error types; covariate-oracle only corrects one), not surprising.\n\n## Key Contributions (ordered for paper)\n\n1. **Bias decomposition identity**: Exact population-level identity: bias ∝ misclassification heterogeneity × CATE heterogeneity (Δπ×Δτ product form). NOT a bound — it is an exact identity under A1–A4; finite-sample R² measures MC noise, not bound looseness. Includes \"debiasing can hurt\" proposition with constructive example. Frame as \"bias decomposition\" or \"bias identity\" throughout — never \"bias bound.\" (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **EC-HTE + PPCI composition — empirically necessary and sufficient**: EC-HTE and PPCI are empirically necessary and sufficient in composition: neither alone adequately handles dual-error scenarios (DGP C), but their composition reduces bias to near-zero (0.005, a 35× improvement over EC-HTE alone). EC-HTE exploits mixing matrix structure for covariate-side error; PPCI rectifier captures outcome-side error. PPCI alone can partially correct covariate error but with higher variance (limited by gold subset size). In Methods, retain full discussion of partial overlap; in Abstract, lead with \"necessary and sufficient in composition.\" (Method + Empirical)\n5. **Comprehensive validation**: Synthetic + semi-synthetic + real-data case study (pattern consistency, not ground-truth benchmark) with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI / DSL?\"** — PPCI rectifier is a general-purpose correction that captures any systematic error (covariate + outcome); EC-HTE is a structured correction exploiting mixing matrix structure specifically for covariate-side error. They are complementary: EC-HTE alone is more efficient for covariate error (uses M⁻¹ structure), PPCI alone can partially correct covariate error but with higher variance (limited by gold subset). In composition, EC-HTE handles structured covariate error, residual rectifier handles outcome error. DSL applied per-subgroup is a valid baseline but lacks cross-subgroup shrinkage, operates at estimand level rather than measurement model level, and has strictly higher variance under partial pooling. Do NOT say \"DSL cannot do subgroup correction\" — say it lacks the principled shrinkage mechanism.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — exp-006 provides precise RMSE crossover points: K=2/extreme n_expert=250, K=4/extreme n=1000, K=4/moderate n=2000, K=2/moderate never crosses (global always better on RMSE). Paper needs \"Expert Budget Recommendation\" subsection with per-K guidelines. Key message: when diagnostic criterion flags high heterogeneity (extreme regime), EC-HTE is worth the investment at moderate budgets; when heterogeneity is low, global correction is the safer choice. This honest framing connects Claim 2 (EC-HTE method) to Claim 3 (diagnostic criterion) — the diagnostic decides the correction strategy.\n\n6. **\"How does this differ from Carroll et al. (2006) / classical measurement error?\"** — The qualitative insight that misspecified corrections can amplify MSE is classical (Fuller 1987, Sec. 2.3). Our specific contributions beyond this are: (a) the quantitative Δπ×Δτ product form for CATE estimation with effect-modifier misclassification, (b) demonstrating this failure mode occurs *by default* in standard LLM annotation workflows, and (c) providing a computable diagnostic and correction framework. Must explicitly cite and contextualize: Fuller (1987), Carroll et al. (2006 Ch. 4), Gustafson (2003), Hu & Schennach (2008), Imai & Yamamoto (2010). Also cite Bayesian annotation models: Dawid & Skene, Passonneau & Carpenter (2014), Hovy et al. (2013). **Bibliography target: 30-35 references** spanning measurement error, Bayesian estimation, causal inference, LLM-as-annotator (Tornberg 2024, Gilardi et al. 2023, Ziems et al. 2024), HTE methods (Wager & Athey 2018, Kennedy 2023, Chernozhukov et al. 2018).\n\n7. **\"Methodological novelty is modest\"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. HB partial pooling provides meaningful RMSE reduction for moderate subgroups but is NOT \"never worse than global\" — it is a James-Stein shrinkage estimator with known boundary conditions. **Recommended condition**: n_expert per subgroup ≥ ~25 (e.g., n_expert ≥ 100 for K=4 with 12% minority). Below this, stratified MLE is preferred. This honest limitation strengthens credibility. State conditions explicitly using per-subgroup formulation, not just total n_expert.\n\n8. **\"Why no figures?\"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use cases (sentiment analysis, hate speech detection, refugee interview coding), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track. **NOTE**: Framing broadened from \"political-science\" to \"CSS\" (D004b) — TweetEval stance tasks too small (N<1000), sentiment (N=45K) usable but not political science. CSS is more accurate and equally strong for EMNLP.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n## Writing Requirements (Dream Round 2 consensus)\n\n1. **\"Bias decomposition\" NOT \"bias bound\"** — Theorem 1 is an exact identity at population level. R² < 1.0 in verification reflects finite-sample MC noise, not bound looseness.\n2. **Bibliography: 30-35 references minimum** — Must span 5 literatures: classical measurement error, Bayesian estimation, causal inference, LLM-as-annotator, CSS. Critical citations: Fuller 1987, Wager & Athey 2018, Imai & Yamamoto 2010.\n3. **3+ figures in main text** — (a) bias mechanism schematic, (b) Δπ×Δτ amplification heatmap, (c) diagnostic ROC curve, (d) budget crossover curves. Move exp-008/exp-009 tables to appendix.\n4. **Semi-synthetic DGP fully specified** — outcome generation, treatment assignment, CATE injection mechanism.\n5. **Real-data framed as pattern consistency** — NOT ground-truth benchmark. No bias/RMSE against unknown true CATEs.\n6. **EC-HTE advantage is conditional, not universal** — ec_hte dominates when misclassification heterogeneity is high (extreme regime) OR n_expert is large (≥500). In moderate regime with small n_expert (~100), global correction can outperform ec_hte because per-subgroup CM estimation noise exceeds the benefit of stratification. This connects to Claim 3: the diagnostic criterion (Δπ×Δτ) predicts when EC-HTE is needed. Unified condition: n_expert/K ≥ ~25-50 experts per subgroup.\n11. **RMSE tradeoff must be disclosed** — ec_hte has higher RMSE than global/naive in K=4/n≤100 configs (up to 3.5x in extreme cases) due to noisy per-subgroup CM estimation. Bias is lower but variance is higher. Must report both bias AND RMSE; include bias-RMSE tradeoff analysis. At n_expert≥500, ec_hte RMSE becomes competitive.\n12. **K-dependence of debiasing-hurts** — DIM estimator: K=2 extreme ~2.86×, K=4 extreme ~2.41× (does NOT monotonically increase with K). CausalForest: K=4 extreme up to 5.9× (nonlinear estimator amplifies with more subgroups). Report both patterns; do NOT claim \"more subgroups → always worse\" without qualifying the estimator.\n7. **Confusion matrix invertibility** — State det(Ĉ_k) ≠ 0 assumption explicitly.\n8. **Diagnostic AUC cross-validated** — Leave-one-setting-out or held-out evaluation, not in-sample.\n9. **Hyperprior values stated + sensitivity analysis** — Gamma(α, β) for Dirichlet concentration; report sensitivity to 2× changes.\n10. **PPCI complementarity elevated** — Highlight in abstract and contributions. Frame as \"complementary\" not \"orthogonal\": EC-HTE is structured covariate-error correction; PPCI rectifier is general residual correction. Composition = EC-HTE handles structured part + rectifier handles remainder (primarily outcome error).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2. MUST report full MCMC diagnostics: sampler (PyMC\n    NUTS), chains (≥4), warmup (≥1000), R̂ (<1.01), ESS (>200), runtime vs MLE. Report\n    SEs/CIs for all metrics from MC runs. Monitor coverage calibration — if systematic\n    undercoverage, diagnose cause.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example. MUST include K>2 extension: verify bias formula empirically for K=4 subgroups;\n    add Remark after Proposition 1 discussing general-K case (sum-of-products form).\n    Report R² of analytic prediction vs MC, bound tightness ratio, and CIs on all\n    bias estimates.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim: 1,2,3\n  description: 'Semi-synthetic benchmark: use real CSS tweet corpus — TweetEval sentiment\n    (N=45K, primary) for exp-003. Framing broadened from ''political-science'' to\n    ''CSS'' per D004b (stance tasks N<1000 unusable). Inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 (API) and optionally Qwen3-235B-A22B (GPU), measure\n    subgroup-specific misclassification rates, apply EC-HTE vs baselines. Subgroup\n    variables: text features (has_hashtag, text_length) for semi-synthetic; demographic\n    subgroups reserved for exp-004. MUST fully specify DGP in paper: (a) outcome generation\n    model, (b) treatment assignment mechanism, (c) how true CATEs are injected. MUST\n    run LLM annotation pilot (~1000 samples) before committing to verify per-subgroup\n    misclassification heterogeneity exists.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim: 1,2\n  description: 'Real-data case study (pattern consistency, NOT ground-truth validation):\n    apply EC-HTE to real CSS dataset with subgroup-varying LLM misclassification.\n    Show: (a) global vs EC-HTE produce qualitatively different CATE distributions,\n    (b) EC-HTE results consistent with domain knowledge (demographic effect direction),\n    (c) bootstrap CIs on point estimate differences. Frame as ''illustrative application''\n    not ''ground-truth benchmark''. Reviewer confirmed: real data has no ground truth\n    CATE, CV-based ground truth is circular. PRIMARY: UC Berkeley Measuring Hate Speech\n    corpus (public, rich demographic subgroups). NICE-TO-HAVE: Ashwin et al. (2025)\n    if obtainable (requires author email + IRB, not feasible within 5-day DDL).'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference) or API\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: UC Berkeley dataset causal framework (T,Y,Z,S) mapping needs design\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold. MUST use\n    cross-validation or held-out evaluation (NOT in-sample AUC on own experiments).\n    Dream Round 2 flagged in-sample AUC as methodological weakness across best and\n    median tiers.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1,2\n  description: 'PPCI + DSL baseline comparison: (a) PPCI kernel-based conditional\n    correction vs EC-HTE on covariate-side vs outcome-side error; (b) per-subgroup\n    DSL as additional baseline (DSL applied independently per subgroup, no cross-subgroup\n    shrinkage — shows EC-HTE''s partial pooling advantage); (c) EC-HTE+PPCI composition\n    for simultaneous covariate+outcome error; (d) CRITICAL: include ''pure covariate-error,\n    zero outcome-error'' control condition to demonstrate EC-HTE advantage when covariate-side\n    error dominates (PPCI should be ineffective here). Paper framing: DSL per-subgroup\n    is a valid baseline but lacks cross-subgroup shrinkage and operates at estimand\n    level rather than measurement model level.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest integration: apply EC-HTE post-hoc correction to CausalForestDML\n    subgroup CATE estimates + leaf-level corrected pseudo-outcomes with variance-adjusted\n    CIs. Compare against naive forest and globally-corrected forest. ELEVATED TO P0:\n    Claim 2 explicitly states CausalForestDML but no experiment validates this — claim-evidence\n    gap is reviewer killshot.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mcmc_rhat_max: 1.024\n    mcmc_ess_min: 129\n    mcmc_divergent: 0\n    runtime_min: 69\n    total_mc_runs: 3600\n    hb_vs_mle_rmse_improvement_k2_n50: 4-9%\n    hb_vs_mle_rmse_improvement_k2_n100: 1-2%\n    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%\n    hb_coverage_min: 0.87\n    hb_coverage_median: 0.93\n    k4_extreme_n50_blowup: false\n    k4_extreme_n50_blowup_note: Fixed by singularity guard + 4-chain MCMC\n    mcmc_fix_4chain:\n      rhat_max_all_configs: 1.0034\n      ess_min_all_configs: 1618\n      ess_improvement: ~4x vs 2-chain\n      k4_extreme_n50_A_rmse_z0: 3.14 → 0.99\n      k4_extreme_n50_B_rmse_z0: 509.93 → 0.27\n      k4_extreme_n100_A_rmse_z0: 11.57 → 0.29\n      singularity_guard_triggers: extreme/n=50 only (2 HB, 3 MLE / 100 runs)\n      results_file: results/exp001_hb_results_v2.csv\n    hyperprior_sensitivity:\n      scale_range: 0.5-2.0\n      k2_rmse_variation: <1%\n      k4_rmse_variation: ~4-5%\n      coverage_invariant: true\n      conclusion: robust\n      results_file: results/exp001_hyperprior_sensitivity.csv\n- exp_id: exp-002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r2_k2: 0.9939\n    r2_k4: 0.9738\n    tightness_ratio_k2_median: 1.0027\n    tightness_ratio_k4_median: 1.0234\n    debiasing_hurts_pct: 50\n    debiasing_hurts_pct_note: 260/520 (excluding dc=0 rows where bias=0)\n    debiasing_hurts_threshold_delta_misclass: 0.1235\n    max_bias_ratio_k2: 2.86\n    max_bias_ratio_k4: 2.41\n    coverage_2se_k2: 0.951\n    coverage_2se_k4: 0.94\n- exp_id: exp-007\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_rows: 6912\n    dgps:\n    - A_covariate_only\n    - B_outcome_only\n    - C_both_errors\n    - D_no_error\n    methods: 8\n    mc_runs: 100\n    double_correction_fix_verified: true\n    dgp_a_ec_hte_ppci_equals_ec_hte: true\n    dgp_c_extreme_n250_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.225\n      ec_hte_bias_z0: 0.178\n      ec_hte_rmse_z0: 0.226\n      ppci_bias_z0: 0.004\n      ppci_rmse_z0: 0.261\n      naive_bias_z0: 0.251\n      naive_rmse_z0: 0.269\n    dgp_c_n500_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.142\n      ec_hte_bias_z0: 0.088\n      ec_hte_rmse_z0: 0.134\n    key_finding: ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better\n      than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.\n- exp_id: exp-003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase: A_semi_synthetic\n    n_subgroups: 4\n    misclass_rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25\n    subgroup_sizes: S0~38%, S1~38%, S2~12%, S3~12%\n    p_z1_actual: 0.39\n    debiasing_hurts_confirmed: true\n    mc_runs: 100\n    v3_hb_integration_100mc:\n      methods:\n      - oracle\n      - naive\n      - global_corrected\n      - stratified_mle\n      - hb_ec_hte\n      hb_vs_mle_summary:\n        n50_S3_extreme: -57% RMSE (HB worse, but not catastrophic)\n        n50_S3_moderate: -54% RMSE z1 (HB worse)\n        n100_S3_extreme: +60% RMSE z1 (HB dramatically better)\n        n100_S3_moderate: +24% RMSE z1 (HB better)\n        n100_S2: +5-8% RMSE (HB better)\n        n250_S3: +5-17% RMSE (HB better)\n        n500_all: +0.2-1.6% (converged)\n      key_finding: '100 MC confirms: S3 blowup at n=50 is real but moderate (not catastrophic\n        as dry-run suggested). At n>=100, HB is better everywhere, especially S3 (+26-60%).\n        Partial pooling sweet spot is n=100-250.'\n      hypothesis_verdict: validated_with_boundary\n      boundary_condition: n_expert>=100 recommended; n=50 with extreme heterogeneity\n        in tiny subgroups shows moderate degradation\n    results_file_v3: results/exp003_phase_a_v3.csv\n    results_file_v3_raw: results/exp003_phase_a_v3_raw.csv\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subgroup_level_auc: 0.833\n    subgroup_correlation: 0.86\n    setting_level_auc: 0.49\n    low_pi_hurt_pct: 84.6\n    high_pi_hurt_pct: 15.4\n    theory_alignment: consistent with exp-002 formula\n- exp_id: exp-011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    n_configs: 8\n    total_rows: 144\n    runtime_min: 35\n    methods:\n    - naive_forest\n    - global_forest\n    - ec_hte_forest\n    mean_abs_bias:\n      naive_forest: 0.1558\n      global_forest: 0.1073\n      ec_hte_forest: 0.0608\n    mean_rmse:\n      naive_forest: 0.1782\n      global_forest: 0.1659\n      ec_hte_forest: 0.2289\n    debiasing_hurts_cases: 9\n    debiasing_hurts_max_ratio: 5.9\n    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'\n    k2_n500_ec_hte_bias_range: 0.004-0.013 (near zero)\n    k2_n500_global_bias_range: 0.033-0.109 (still biased)\n    pattern_consistent_with_diff_in_means: true\n    claim2_validated: true\n- exp_id: exp-006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    total_rows: 288\n    runtime_min: 110\n    grid: n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]\n    crossover_hb_beats_global:\n      K2_extreme: 250\n      K2_moderate: never\n      K4_extreme: 1000\n      K4_moderate: 2000\n    hb_vs_mle: HB ≥ MLE in 21/24 configs (87.5%; partial pooling rarely hurts in symmetric\n      DGP)\n    hb_best_improvement_over_mle:\n      K4_moderate_n50_sgC: +42.4% RMSE\n      K4_extreme_n50_sgC: +23.4% RMSE\n      K4_moderate_n50_sgB: +24.0% RMSE\n    convergence: HB ≈ MLE at n≥1000 (<0.5% difference)\n    key_finding: 'Crossover depends strongly on K and regime. K=2: crossover at n=250\n      (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest\n      improvement over MLE via partial pooling.'\n- exp_id: exp-007b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    kill_reason: 'D012: Director 决定放弃 HB backfill。理由：PPCI 表核心 story 是互补性，HB vs MLE\n      是边际改进；exp-001 已验证 HB。CSV 已重命名为 .broken'\n- exp_id: exp-012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: gpt-4.1-2025-04-14\n    n_samples: 500\n    valid_annotations: 500\n    failed: 0\n    accuracy_3class: 0.672\n    accuracy_binary: 0.858\n    subgroup_misclass_rates:\n      hash_long: 0\n      hash_medium: 0.2\n      hash_short: 0.174\n      nohash_long: 0\n      nohash_medium: 0.102\n      nohash_short: 0.138\n    delta_pi: 0.2\n    heterogeneity_significant: true\n    key_finding: Hashtag presence increases binary misclassification rate (~0.17-0.20\n      vs ~0.10-0.14 for non-hashtag). Delta-pi=0.200 confirms meaningful heterogeneity\n      for EC-HTE correction.\n    analysis_file: results/pilot_gpt41_analysis.md\n- exp_id: exp-013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    config: K=4/extreme/n_expert=50\n    n_expert_per_K: 12.5\n    hb_method: EB (Empirical Bayes, not Gibbs — conservative estimate for boundary\n      condition)\n    avg_rmse_naive: 0.109\n    avg_rmse_global: 0.14\n    avg_rmse_mle: 0.28\n    avg_rmse_eb: 0.292\n    worst_subgroup: A(pi=0.30) EB RMSE=0.62\n    amplification_max: 4.4x (A/EB vs global)\n    threshold_confirmed: n_expert/K=12.5 < 25\n    naive_beats_all: true\n    debiasing_hurts_D: Naive bias=0.001, Global bias=0.110 — extreme over-correction\n      in lowest-error subgroup\n- exp_id: exp-014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    configs: 3\n    asymmetric_configs:\n    - balanced(FPR=0.15,FNR=0.25)\n    - fpr_dominant(FPR=0.30,FNR=0.10)\n    - fnr_dominant(FPR=0.10,FNR=0.30)\n    delta_tau_grid:\n    - 0\n    - 0.1\n    - 0.2\n    - 0.3\n    - 0.5\n    n_mc: 100\n    N: 5000\n    n_expert: 250\n    r2_analytic_vs_mc: 0.992\n    product_structure_cv: ~1e-16 (exact)\n    product_structure_confirmed: true\n    a2_not_required: true\n    ec_hte_avg_abs_bias: 0.006\n    ec_hte_avg_rmse: 0.033\n    ec_hte_avg_coverage: 0.9\n    global_avg_abs_bias: 0.025\n    global_avg_rmse: 0.04\n    global_avg_coverage: 0.78\n    naive_avg_abs_bias: 0.025\n    naive_avg_rmse: 0.039\n    naive_avg_coverage: 0.87\n    bias_reduction_vs_global: 4.2x\n    coverage_improvement_vs_global: +12pp\n    latex_derivation_included: true\n    key_finding: Product structure bias = Δτ·[B_s]_{z,1} holds exactly under asymmetric\n      misclassification. A2 (symmetric) assumption is NOT required. EC-HTE dominates\n      with 4.2x bias reduction.\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dataset: UC Berkeley Measuring Hate Speech\n    n_comments: 2496\n    valid_annotations: 2496\n    subgroups:\n      plat0_long: 624\n      plat0_short: 624\n      plat23_long: 624\n      plat23_short: 624\n    subgroup_type: text features (platform_group × text_length)\n    delta_pi: 0.117\n    global_FPR: 0.139\n    global_FNR: 0.533\n    misclass_rates:\n      plat0_long: 0.266\n      plat0_short: 0.337\n      plat23_long: 0.303\n      plat23_short: 0.383\n    avg_abs_bias:\n      naive: 0.21\n      global: 0.273\n      ec_hte: 0.313\n    cate_comparison: EC-HTE does not outperform global on avg |bias| — high FNR (~53%)\n      and wide CIs limit correction effectiveness on this dataset\n    key_finding: Δπ=0.117 confirms real-world misclassification heterogeneity across\n      text-feature subgroups. High global FNR (53%) indicates LLM severely under-classifies\n      dehumanization. CATE correction comparison inconclusive due to wide bootstrap\n      CIs.\n- exp_id: exp-008\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    models_completed:\n    - gpt-3.5-turbo\n    - gpt-4.1\n    - gpt-4o\n    - gpt-4o-mini\n    - gpt-4-turbo\n    - gpt-5.4\n    total_models: 6\n    proxy_provider: OpenAI only\n    gpt5x_model_used: gpt-5.4\n    gpt55_failed: reasoning tokens consume max_tokens budget, too slow (~1min/call)\n    filtered_analysis:\n      excluded_subgroups:\n      - False_long (n=6)\n      - True_long (n=4)\n      min_n_threshold: 10\n      retained_subgroups:\n      - False_medium (n=187)\n      - False_short (n=109)\n      - True_medium (n=125)\n      - True_short (n=69)\n    effective_delta_pi:\n      gpt-3.5-turbo: 0.198\n      gpt-4-turbo: 0.149\n      gpt-4.1: 0.098\n      gpt-4o: 0.08\n      gpt-4o-mini: 0.136\n      gpt-5.4: 0.114\n    all_effective_delta_pi_above_005: true\n    worst_subgroup_consensus: True_medium (5/6 models)\n    spearman_significant_pairs:\n    - gpt-4-turbo vs gpt-4o (ρ=1.000)\n    - gpt-4.1 vs gpt-4o-mini (ρ=1.000)\n    - gpt-4.1 vs gpt-5.4 (ρ=1.000)\n    - gpt-4o-mini vs gpt-5.4 (ρ=1.000)\n    spearman_note: Only 4 subgroups after filtering, limited statistical power (most\n      p>0.20)\n    key_finding: All 6 models (GPT-3.5 through GPT-5.4, three generations) show effective\n      Δπ > 0.05 after excluding n<10 subgroups. Heterogeneity is structural, not model-specific.\n- exp_id: exp-010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 100\n    configs: 2\n    noise_levels:\n    - 0\n    - 0.1\n    - 0.25\n    - 0.5\n    total_runs: 800\n    runtime_sec: 15\n    k2_coverage_naive:\n    - 0.875\n    - 0.877\n    - 0.89\n    - 0.897\n    k2_coverage_hb:\n    - 0.958\n    - 0.948\n    - 0.95\n    - 0.945\n    k2_coverage_global:\n    - 0.925\n    - 0.935\n    - 0.932\n    - 0.945\n    k4_coverage_naive:\n    - 0.904\n    - 0.916\n    - 0.909\n    - 0.919\n    k4_coverage_hb:\n    - 0.956\n    - 0.958\n    - 0.96\n    - 0.946\n    k4_coverage_global:\n    - 0.93\n    - 0.953\n    - 0.948\n    - 0.944\n    hb_beats_mle_all_configs: true\n    hb_improvement_range: +0.1% to +0.9% RMSE\n    graceful_convergence_at_50pct: true\n    key_finding: 'Coverage is the decisive metric: naive 87-92%, EC-HTE 95-96% across\n      all noise levels. No catastrophic failure. HB shrinkage provides automatic safeguard\n      — converges to global at 50% noise.'\n- exp_id: exp-015\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_mc: 100\n    n_expert_grid:\n    - 100\n    - 250\n    - 500\n    subgroups: 4\n    real_cm_source: exp-012 GPT-4.1 pilot\n    cm_params:\n      S0_False_medium:\n        FPR: 0.054\n        FNR: 0.526\n        weight: 0.38\n      S1_False_short:\n        FPR: 0.101\n        FNR: 0.3\n        weight: 0.22\n      S2_True_short:\n        FPR: 0.143\n        FNR: 0.308\n        weight: 0.14\n      S3_True_medium:\n        FPR: 0.194\n        FNR: 0.222\n        weight: 0.25\n    delta_pi: 0.098\n    P_Z1: 0.18\n    rmse_n100:\n      naive: 0.123\n      global: 0.263\n      hb: 0.784\n    rmse_n250:\n      naive: 0.123\n      global: 0.232\n      hb: 0.411\n    rmse_n500:\n      naive: 0.123\n      global: 0.196\n      hb: 0.26\n    coverage_n100:\n      naive: 0.868\n      global: 0.922\n      hb: 0.744\n    coverage_n250:\n      naive: 0.868\n      global: 0.908\n      hb: 0.828\n    coverage_n500:\n      naive: 0.873\n      global: 0.885\n      hb: 0.89\n    hb_worse_than_global_all_n: true\n    root_cause: S0 FNR=0.526 makes CM row near-uniform [0.526, 0.474], inversion amplifies\n      noise. Combined with P(Z=1)=0.18, too few Z=1 expert labels per subgroup for\n      reliable per-subgroup CM estimation.\n    key_finding: EC-HTE fails under realistic asymmetric CMs when any subgroup has\n      FNR≈0.5 (near-random for positive class). This is consistent with exp-004 (FNR=53%)\n      and exp-013 (boundary at n_expert/K=12.5). Identifies classifier quality threshold\n      as honest limitation.\n- exp_id: exp-016\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    model_selected: gpt-3.5-turbo\n    worst_subgroup_fnr: 0.211\n    worst_subgroup_fpr: 0.393\n    rmse_n100:\n      naive: 0.127\n      global: 0.265\n      hb: 0.93\n    rmse_n250:\n      naive: 0.127\n      global: 0.221\n      hb: 0.527\n    rmse_n500:\n      naive: 0.127\n      global: 0.199\n      hb: 0.322\n    coverage_n100:\n      naive: 0.784\n      global: 0.893\n      hb: 0.769\n    coverage_n250:\n      naive: 0.784\n      global: 0.922\n      hb: 0.843\n    coverage_n500:\n      naive: 0.784\n      global: 0.939\n      hb: 0.894\n    hb_worse_than_global_all_n: true\n    vs_exp015: exp-016 HB RMSE even worse than exp-015 despite lower FNR, because\n      high FPR variance (0.14-0.39) makes subgroup CM estimation harder\n    bright_spot: 'S0/z=1 at n=500: HB |bias|=0.193 < Global |bias|=0.252 — one case\n      where subgroup-specific correction helps'\n    root_cause: High FPR variance across subgroups (0.143-0.393) + P(Z=1)=0.18 → insufficient\n      Z=1 expert labels per subgroup. Lower FNR alone does not fix the fundamental\n      sample-size constraint.\n    key_finding: Neither low-FNR (gpt-3.5-turbo) nor low-FPR (GPT-4.1) real CMs enable\n      EC-HTE to beat global. The bottleneck is P(Z=1)=0.18 creating too few positive-class\n      expert labels per subgroup for reliable CM estimation.\n- exp_id: exp-017\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 50\n    config: K=2/extreme/n_expert=500\n    rlearner_results:\n      naive:\n        avg_abs_bias: 0.121\n        rmse: 0.139\n        coverage: 0.47\n      global:\n        avg_abs_bias: 0.098\n        rmse: 0.123\n        coverage: 0.71\n      ec_hte:\n        avg_abs_bias: 0.013\n        rmse: 0.08\n        coverage: 0.92\n      oracle:\n        avg_abs_bias: 0.006\n        rmse: 0.056\n        coverage: 0.94\n    causal_forest_comparison:\n      naive:\n        avg_abs_bias: 0.125\n        rmse: 0.143\n        coverage: 0.46\n      global:\n        avg_abs_bias: 0.104\n        rmse: 0.129\n        coverage: 0.65\n      ec_hte:\n        avg_abs_bias: 0.008\n        rmse: 0.082\n        coverage: 0.91\n    ec_hte_bias_reduction_vs_naive: 9.3x (R-learner) vs 15.6x (CausalForest)\n    pattern_consistent: true\n    key_finding: EC-HTE correction generalizes across CATE estimators. R-learner ec_hte\n      achieves |bias|=0.013 (vs naive 0.121), 92% coverage — closely matching CausalForest\n      pattern.\n- exp_id: exp-018\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_mc: 50\n    config: K=2/extreme/n_expert=500/multiplicative\n    dgp: Y(1) = Y(0) * exp(tau(Z)), tau(Z=0)=0, tau(Z=1)=0.3\n    results:\n      oracle:\n        avg_abs_bias: 0.031\n        rmse: 0.038\n        coverage: 0.96\n      ec_hte:\n        avg_abs_bias: 0.054\n        rmse: 0.068\n        coverage: 0.955\n      global_corrected:\n        avg_abs_bias: 0.11\n        rmse: 0.124\n        coverage: 0.54\n      naive:\n        avg_abs_bias: 0.135\n        rmse: 0.142\n        coverage: 0.435\n    ec_hte_rmse_reduction_vs_naive: 52%\n    ec_hte_coverage: 0.955\n    vs_exp001_additive: EC-HTE RMSE 0.068 (multiplicative) vs 0.091 (additive, same\n      config) — actually better due to larger true CATEs making relative bias smaller\n    key_finding: EC-HTE robust to non-additive treatment effects. 52% RMSE reduction\n      vs naive, 95.5% coverage (target 95%). Answers Reviewer Q3.\n- exp_id: exp-019\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    theorem1_r2:\n      K2:\n        pz0.1: 0.998\n        pz0.2: 0.989\n        pz0.3: 0.994\n        pz0.4: 0.995\n        pz0.5: 0.995\n      K4:\n        pz0.1: 0.984\n        pz0.2: 0.976\n        pz0.3: 0.985\n        pz0.4: 0.984\n        pz0.5: 0.992\n    theorem1_r2_range: 0.976-0.998 (all >0.95)\n    rmse_ratio_hb_over_global:\n      K2:\n        pz0.1: 0.92\n        pz0.2: 0.763\n        pz0.3: 0.78\n        pz0.4: 0.874\n        pz0.5: 0.857\n      K4:\n        pz0.1: 1.542\n        pz0.2: 1.684\n        pz0.3: 1.121\n        pz0.4: 1.082\n        pz0.5: 1.063\n    hb_wins_K2: all 5 P(Z=1) values (ratio 0.76-0.92)\n    hb_wins_K4: none (ratio 1.06-1.68)\n    coverage_hb: 0.92-0.94 across all settings (near-nominal 0.95)\n    coverage_naive: 0.65-0.79\n    coverage_global: 0.79-0.90\n    key_finding: 'Theorem 1 R²>0.976 universally — bias decomposition holds regardless\n      of P(Z=1). EC-HTE RMSE advantage depends on K: K=2 HB wins everywhere, K=4 HB\n      loses at n_expert=250 (insufficient per-subgroup minority data). Coverage: HB\n      0.92-0.94 near-nominal at all settings.'\n- exp_id: exp-020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    max_cond_number: 1.89\n    mean_cond_number: 1.446\n    p99_cond_number: 1.893\n    guard_trigger_rate_all_kappa: 0\n    rmse_hb: 0.0759\n    rmse_global: 0.0765\n    rmse_ratio: 1.048\n    numerical_instability_rate: 0\n    safety_margin_at_kappa100: 53x\n    stress_test_near_random_max_cond: 1125.3\n    stress_test_near_random_triggers_kappa100: true\n- exp_id: exp-021\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_cells_compared: 94\n    median_delta_pct: 3.2\n    max_delta_pct: 25.5\n    cells_under_5pct: 79/94 (84%)\n    cells_under_10pct: 93/94 (99%)\n    outlier: K=4/extreme/n=100/HB base (-25.5%, known numerically unstable)\n    method_note: EB instead of Gibbs (<0.002 CM difference, 10s vs 114min)\n- exp_id: exp-022\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rmse_range_reasonable: 6.0%\n    rmse_range_all: 17.3%\n    gamma31_rmse: 0.0841\n    gamma31_rank: 8/15\n    coverage_range: 0.925-0.938\n    hb_beats_mle: 9/15\n    best_config: Gamma(1,0.5)\n    best_rmse: 0.0825\n- exp_id: exp-023\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dgp: heterogeneous-tau\n    N: 5000\n    P_Z1: 0.652\n    K: 4\n    subgroups:\n    - False_medium\n    - False_short\n    - True_medium\n    - True_short\n    delta_tau:\n      False_medium: 0.1\n      False_short: 0.1\n      True_medium: 0.3\n      True_short: 0.6\n    n_expert_sweep:\n    - 200\n    - 500\n    - 1000\n    mc_seeds: 50\n    hb_method: MAP-EB Gamma(3,1)\n    bias_echte_wins: 3/3 budgets\n    bias_reduction_n500: 68% vs Global (0.0099 vs 0.0314)\n    bias_reduction_n200: 32% vs Global (0.0248 vs 0.0365)\n    bias_reduction_n1000: 55% vs Global (0.0130 vs 0.0286)\n    rmse_echte_wins: 0/3 aggregate\n    rmse_true_short_n1000:\n      global: 0.1693\n      echte: 0.1637\n      improvement: -3.3%\n    rmse_true_short_z0_n1000:\n      global: 0.2577\n      echte: 0.2117\n      improvement: -17.8%\n    key_finding: EC-HTE wins bias at all budgets. High-Δτ subgroup (True_short) RMSE\n      wins at n≥500. Aggregate RMSE loss driven by low-Δτ subgroups where stratified\n      variance cost exceeds small bias gain.\n- exp_id: exp-024\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R2_overall: 0.975\n    data_sources:\n    - exp023_confusion_matrices.json\n    - c1_multi_llm/*_cm_profile.md\n    n_llm_dataset_combos: 11\n    output_files:\n    - results/exp_realcm_bias_identity.csv\n    - results/exp_realcm_summary.csv\n- exp_id: exp-025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    screening: 0/16 combos pass all conditions (κ≤1.25 bottleneck)\n    oracle_screening: HB wins 41/52 comparisons on aggregate RMSE\n    hb_vs_mle: HB beats Strat MLE in 52/52 comparisons\n    best_case: 'Qwen2.5-7B K=4 n=500 Z=0: ΔRMSE=-0.0075'\n    open_source_llms: All 4 (Llama/Qwen/Mistral/Gemma) HB wins 32/32 on TweetEval\n    hb_loses: gpt-3.5-turbo/TweetEval (high FPR asymmetry), gpt-4o/CivilComments (low\n      P(Z=1)=0.3)\n    output_files:\n    - results/exp_screening.csv\n    - results/exp_oracle_screening.csv\n    - results/exp_positive_scenario_summary.md\n- exp_id: exp-026\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K2_n25:\n      mle_rmse: 0.2562\n      hb_rmse: 0.2689\n      delta_pct: +4.9%\n      global_rmse: 0.1013\n    K2_n50:\n      mle_rmse: 0.2748\n      hb_rmse: 0.2306\n      delta_pct: -16.1%\n      global_rmse: 0.0879\n    K2_n75:\n      mle_rmse: 0.0911\n      hb_rmse: 0.0893\n      delta_pct: -1.9%\n    K4_n25:\n      mle_rmse: 0.4011\n      hb_rmse: 0.6116\n      delta_pct: +52.5%\n      global_rmse: 0.1289\n    K4_n50:\n      mle_rmse: 0.3798\n      hb_rmse: 0.4701\n      delta_pct: +23.8%\n      global_rmse: 0.1172\n    K4_n75:\n      mle_rmse: 0.2208\n      hb_rmse: 0.2111\n      delta_pct: -4.4%\n    K4_n100:\n      mle_rmse: 0.2152\n      hb_rmse: 0.2123\n      delta_pct: -1.3%\n    coverage_all: '>=0.88, no catastrophic failures'\n    crossover_K2: n_expert=50 (HB -16.1%)\n    crossover_K4: n_expert=75 (HB -4.4%)\n    key_finding: HB shrinkage advantage emerges at n≥50 (K=2) and n≥75 (K=4). Below\n      these thresholds, global pooling outperforms both HB and MLE — validates budget\n      threshold claim.\n    mc_runs: 100\n    output_file: results/exp_low_budget_hb.csv\n- exp_id: exp-027\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    oracle_true_Z:\n      coverage: 0.945\n      bias: 0.0056\n      rmse: 0.078\n    echte_true_CM:\n      coverage: 0.925\n      bias: 0.0078\n      rmse: 0.114\n    echte_estimated_CM:\n      coverage: 0.931\n      bias: 0.0148\n      rmse: 0.121\n    global_true_CM:\n      coverage: 0.913\n      bias: 0.0371\n      rmse: 0.11\n    global_estimated_CM:\n      coverage: 0.911\n      bias: 0.0379\n      rmse: 0.111\n    naive:\n      coverage: 0.883\n      bias: 0.0447\n      rmse: 0.095\n    key_finding: 'Oracle CF SE well-calibrated (94.5%). EC-HTE true CM (92.5%) ≈ estimated\n      CM (93.1%): CM estimation NOT the coverage gap source. ~2pp drop from Oracle\n      to EC-HTE true CM comes from M^{-1} SE propagation, not CM estimation noise.'\n    dgp: K=4 extreme, N=5000, n_expert=500, 100 MC runs\n    output_file: results/exp_cf_oracle_coverage.csv\n- exp_id: exp-027b\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    dgp: K=2 extreme, π=[0.05,0.25], N=5000, n_expert=250, 100 MC runs\n    oracle_true_Z:\n      coverage: 0.94\n      bias: 0.0023\n      rmse: 0.056\n    echte_true_CM:\n      coverage: 0.94\n      bias: 0.0027\n      rmse: 0.073\n    echte_estimated_CM:\n      coverage: 0.925\n      bias: 0.0044\n      rmse: 0.079\n    global_true_CM:\n      coverage: 0.885\n      bias: 0.045\n      rmse: 0.083\n    global_estimated_CM:\n      coverage: 0.883\n      bias: 0.045\n      rmse: 0.085\n    naive:\n      coverage: 0.828\n      bias: 0.046\n      rmse: 0.077\n    key_finding: 'K=2: Oracle 94%, EC-HTE true CM 94%, EC-HTE estimated CM 92.5%.\n      CF SE is well-calibrated. 83-85% coverage in paper comes from Naive (uncorrected\n      misclassification bias), NOT from CF SE under-calibration. EC-HTE restores near-nominal\n      coverage.'\n    output_file: results/exp_cf_oracle_coverage_k2.csv\n- exp_id: exp-027c\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dgp: 'MF2 exact DGP: K=2, π=[0.05,0.25], τ(0)=0.10, τ(1)=0.40, N=5000, n_expert=250,\n      100 MC'\n    oracle_true_Z:\n      coverage: 0.96\n      bias: 0.077\n      rmse: 0.091\n      mean_se: 0.09\n    echte_true_CM:\n      coverage: 0.913\n      bias: 0.103\n      rmse: 0.112\n      mean_se: 0.114\n    echte_estimated_CM:\n      coverage: 0.923\n      bias: 0.1\n      rmse: 0.111\n      mean_se: 0.119\n    global_true_CM:\n      coverage: 0.95\n      bias: 0.107\n      rmse: 0.114\n      mean_se: 0.107\n    global_estimated_CM:\n      coverage: 0.943\n      bias: 0.105\n      rmse: 0.114\n      mean_se: 0.109\n    naive:\n      coverage: 0.773\n      bias: 0.12\n      rmse: 0.125\n      mean_se: 0.087\n    key_finding: 'DGP difference NOT the source of 83% vs 92.5% gap. Per-subgroup\n      EC-HTE coverage ~92.25% in both 027b and 027c. The 83% in MF2 is an aggregate\n      mixing effect: low-misclass subgroup (π=0.05) has 83% coverage while high-misclass\n      subgroup (π=0.25) has 99%. M⁻¹ creates asymmetric SE amplification across subgroups.'\n    comparison_027b:\n      oracle: 94.0% → 96.0%\n      echte_est: 92.5% → 92.25%\n      conclusion: Nearly identical per-subgroup coverage despite different τ values\n    output_file: results/exp_cf_oracle_coverage_mf2dgp.csv\n- exp_id: exp-028\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_symmetric_auc: 0.626\n    overall_asymmetric_auc: 0.611\n    k4_only:\n      symmetric_auc_range: 0.0-1.0\n      asymmetric_auc_range: 0.0-1.0\n      perfect_auc_combos:\n      - Llama/TweetEval\n      - Qwen/TweetEval\n      - Mistral/TweetEval\n      - gpt-4o/TweetEval\n      - gpt-3.5-turbo/TweetEval(asym only)\n      - gpt-4.1/TweetEval(asym only)\n    k2_all_auc_zero: true\n    z0_z1_identical: true\n    theoretical_insight: For DIM, |B_s[0,1]|=|B_s[1,1]| (column-stochastic M). Asymmetric\n      diagnostic degenerates to symmetric because DIM CATE bias depends on δ_s = (FPR_s+FNR_s)/2\n      - π̄, not on FPR/FNR individually.\n    output_files:\n    - results/exp_asymmetric_diagnostic_auc.csv\n    - results/exp_asymmetric_diagnostic_auc_summary.csv\n- exp_id: exp-029\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dgp: K=2, pi=[0.05,0.25], tau(0)=0, tau(1)=0.3, N=5000, n_expert=250, 100 MC\n    gamma_sweep:\n    - 0\n    - 0.05\n    - 0.1\n    - 0.15\n    - 0.2\n    echte_coverage:\n      g0.00: 0.955\n      g0.05: 0.955\n      g0.10: 0.953\n      g0.15: 0.948\n      g0.20: 0.935\n    echte_abs_bias:\n      g0.00: 0.0596\n      g0.05: 0.0593\n      g0.10: 0.063\n      g0.15: 0.0652\n      g0.20: 0.0677\n    global_coverage:\n      g0.00: 0.927\n      g0.05: 0.935\n      g0.10: 0.938\n      g0.15: 0.943\n      g0.20: 0.94\n    naive_coverage:\n      g0.00: 0.877\n      g0.05: 0.838\n      g0.10: 0.835\n      g0.15: 0.792\n      g0.20: 0.795\n    key_finding: 'EC-HTE coverage degrades gracefully: 95.5%→93.5% over gamma 0→0.2\n      (−2.0pp). ALL correction methods maintain ≥90% coverage across all gamma. Naive\n      degrades fastest (87.7%→79.5%, −8.2pp). At moderate violation gamma=0.1, EC-HTE\n      coverage=95.3% (−0.2pp from baseline). EC-HTE |bias| increases 13.7% at gamma=0.2\n      but remains comparable to Global.'\n    coverage_below_90_threshold:\n      Naive: 0\n      Global: never\n      Strat_MLE: never\n      HB_ECHTE: never\n    output_files:\n    - results/exp_a1_sensitivity.csv\n    - results/exp_a1_sensitivity_summary.csv\n    - results/exp_a1_sensitivity_subgroup.csv\n- exp_id: exp-030\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hb_echte_coverage: 0.956\n    hb_echte_rmse: 0.34\n    hb_echte_mean_abs_bias: 0.183\n    oracle_coverage: 0.944\n    oracle_rmse: 0.113\n    oracle_mean_abs_bias: 0.09\n    global_coverage: 0.951\n    global_rmse: 0.168\n    global_mean_abs_bias: 0.135\n    strat_mle_coverage: 0.953\n    strat_mle_rmse: 0.638\n    strat_mle_mean_abs_bias: 0.219\n    naive_coverage: 0.913\n    naive_rmse: 0.133\n    naive_mean_abs_bias: 0.107\n    hb_vs_mle_rmse_improvement_pct: 47\n    per_subgroup_expert_labels: 31\n    source: results/exp_k8_subgroups_summary.csv\n    note: All CM-aware methods coverage ≥95%. HB RMSE 47% better than MLE but worse\n      than Global. K=8 is boundary condition.\n- exp_id: exp-031\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hb_echte_coverage: 0.95\n    hb_echte_rmse: 0.086\n    hb_echte_mean_abs_bias: 0.068\n    oracle_coverage: 0.943\n    oracle_rmse: 0.061\n    oracle_mean_abs_bias: 0.048\n    global_coverage: 0.93\n    global_rmse: 0.087\n    global_mean_abs_bias: 0.071\n    strat_mle_coverage: 0.95\n    strat_mle_rmse: 0.087\n    strat_mle_mean_abs_bias: 0.069\n    naive_coverage: 0.863\n    naive_rmse: 0.083\n    naive_mean_abs_bias: 0.066\n    beta_confound: 0.5\n    propensity_range: 0.38-0.62\n    source: results/exp_confounded_dgp_summary.csv\n    note: EC-HTE + IPW-DIM coverage 95.0% under moderate confounding. Global 93.0%.\n      Naive 86.3%.\n- exp_id: exp-032\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    min_hb_coverage: 0.945\n    max_oracle_vs_est_gap: 0.01\n    hb_cov_b0.25_oracle: 0.9625\n    hb_cov_b0.25_estimated: 0.9725\n    hb_cov_b0.5_oracle: 0.95\n    hb_cov_b0.5_estimated: 0.9575\n    hb_cov_b1.0_oracle: 0.9575\n    hb_cov_b1.0_estimated: 0.96\n    hb_cov_b2.0_oracle: 0.945\n    hb_cov_b2.0_estimated: 0.9475\n    hb_rmse_b2.0_oracle: 0.1258\n    naive_cov_range: 0.845-0.898\n    source: results/exp_confounded_sweep_summary.csv\n    note: All 8 configs HB coverage >=94.5%. Oracle vs estimated gap <=1pp. Hypothesis\n      fully confirmed.\n- exp_id: exp-033\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hb_baseline_rmse: 0.333\n    hb_baseline_coverage: 0.959\n    v1_adaptive_alpha_rmse: 0.216\n    v1_adaptive_alpha_coverage: 0.96\n    v2_kappa_fallback_rmse: 0.25\n    v2_kappa_fallback_coverage: 0.96\n    v3_combined_rmse: 0.216\n    v3_combined_coverage: 0.96\n    global_rmse: 0.166\n    global_coverage: 0.958\n    v1_vs_baseline_improvement_pct: 35\n    v1_still_exceeds_global_pct: 30\n    source: results/exp_k8_adaptive_summary.csv\n    note: V1 (adaptive alpha) reduces RMSE 35% (0.333->0.216) but still exceeds Global\n      (0.166). Gap narrowed from 2x to 1.3x. Confirms boundary is real but mitigable.\n- exp_id: exp-034\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    source: results/exp_fl_comparison_summary.csv\n    fl_scalar_abs_bias: 0.0909\n    fl_scalar_rmse: 0.1161\n    fl_scalar_coverage: 0.85\n    fl_per_subgroup_abs_bias: 0.112\n    fl_per_subgroup_rmse: 0.1582\n    fl_per_subgroup_coverage: 0.838\n    echte_abs_bias: 0.0643\n    echte_rmse: 0.0858\n    echte_coverage: 0.953\n    global_cm_abs_bias: 0.0643\n    global_cm_rmse: 0.0806\n    global_cm_coverage: 0.938\n    naive_abs_bias: 0.0621\n    naive_coverage: 0.858\n    oracle_abs_bias: 0.0454\n    oracle_coverage: 0.943\n    sign_reversal: 'F-L Scalar: s0=+0.073 s1=+0.068, both positive (no sign-reversal).\n      F-L Per-Subgroup: s0=+0.024 s1=+0.160. EC-HTE: s0=+0.006 s1=+0.001 (near-zero\n      bias both subgroups)'\n    key_finding: F-L scalar and F-L per-subgroup both WORSE than naive on aggregate\n      |bias|. F-L scalar over-corrects s0 (bias +0.073 vs naive +0.005). F-L per-subgroup\n      dramatically over-corrects s1 (bias +0.160). EC-HTE achieves near-zero per-subgroup\n      bias with nominal coverage (95.3%). CM inversion fundamentally different from\n      F-L scalar rescaling.\n- exp_id: exp-035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    source: results/exp_asymmetric_cm_summary.csv\n    echte_asym_abs_bias: 0.057\n    echte_asym_rmse: 0.0735\n    echte_asym_coverage: 0.945\n    echte_sym_abs_bias: 0.0618\n    echte_sym_rmse: 0.0831\n    echte_sym_coverage: 0.93\n    global_asym_abs_bias: 0.0609\n    global_asym_coverage: 0.915\n    global_sym_abs_bias: 0.0629\n    global_sym_coverage: 0.915\n    naive_abs_bias: 0.0592\n    naive_coverage: 0.87\n    oracle_abs_bias: 0.0454\n    oracle_coverage: 0.943\n    asym_vs_sym_echte_rmse_delta: -0.0096\n    asym_vs_sym_echte_cov_delta: 0.015\n    s1_echte_asym_cov: 0.93\n    s1_echte_sym_cov: 0.91\n    key_finding: 'EC-HTE asymmetric achieves 94.5% coverage (vs 93.0% symmetric) under\n      7:1 FPR/FNR ratio. RMSE improved 11.5% (0.0831→0.0735). Asymmetric formula essential\n      for high FPR/FNR ratios. s1 (high-error) coverage: 93.0% asymmetric vs 91.0%\n      symmetric.'\n- exp_id: exp-037\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    source: results/exp_calibration_summary.csv\n    calibrated_echte_abs_bias: 0.0554\n    calibrated_echte_coverage: 0.965\n    calibrated_global_abs_bias: 0.055\n    calibrated_global_coverage: 0.963\n    calibrated_naive_abs_bias: 0.051\n    calibrated_naive_coverage: 0.912\n    uncalibrated_echte_abs_bias: 0.0641\n    uncalibrated_echte_coverage: 0.938\n    uncalibrated_global_abs_bias: 0.0695\n    uncalibrated_global_coverage: 0.92\n    uncalibrated_naive_abs_bias: 0.0634\n    uncalibrated_naive_coverage: 0.84\n    oracle_abs_bias: 0.0431\n    oracle_coverage: 0.963\n    delta_pi_uncalibrated: 0.2\n    delta_pi_calibrated: 0.07\n    key_finding: Calibration reduces Δπ from 0.20 to 0.07 and improves naive coverage\n      (84.0%→91.2%) but doesn't reach nominal 95%. Calibrated+EC-HTE achieves best\n      coverage (96.5%) — EC-HTE corrects residual heterogeneity post-calibration.\n      Calibrated+Naive still under-covers by 3.8pp. EC-HTE and calibration are complementary,\n      not substitutes.\n- exp_id: exp-036\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    source: results/exp_bootstrap_se_v2_summary.csv\n    note: v2 with n_estimators=200 (fixes v1 n_estimators=48 artifact)\n    plugin_coverage: 0.9375\n    bootstrap_coverage: 0.95\n    oracle_coverage: 0.9\n    coverage_improvement: 0.0125\n    plugin_se_mean: 0.073\n    bootstrap_se_mean: 0.083\n    se_ratio_boot_over_plugin: 1.154\n    s0_plugin_cov: 0.95\n    s0_bootstrap_cov: 0.925\n    s1_plugin_cov: 0.925\n    s1_bootstrap_cov: 0.975\n    s1_se_ratio: 1.222\n    n_mc: 20\n    n_bootstrap: 100\n    n_estimators: 200\n    runtime_sec: 1716\n    key_finding: With correct n_estimators=200, plugin SE already near-nominal (93.8%).\n      Bootstrap provides modest improvement to exact 95.0%. v1 '81.7% → 94.2%' gap\n      was artifact of n_estimators=48.\n- exp_id: exp-038\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    reversal_pct_tau001: 31\n    reversal_pct_tau003: 14.9\n    reversal_pct_tau005: 6.1\n    reversal_pct_tau010: 0\n    ec_hte_reversal_pct: 0\n    worst_combo: tau=0.01, delta_misclass=0.19 → 42.9%\n- exp_id: exp-039\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K2_echte_bias: 0.008\n    K2_echte_rmse: 0.089\n    K2_echte_cov: 0.938\n    K4_echte_bias: 0.012\n    K4_echte_rmse: 0.12\n    K4_echte_cov: 0.956\n    K8_echte_bias: 0.183\n    K8_echte_rmse: 0.34\n    K8_echte_cov: 0.956\n    K8_global_rmse: 0.168\n- exp_id: exp-040\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma0_cov: 0.945\n    gamma0_rmse: 0.075\n    gamma005_cov: 0.897\n    gamma005_rmse: 0.092\n    gamma010_cov: 0.75\n    gamma010_rmse: 0.133\n    gamma015_cov: 0.525\n    gamma015_rmse: 0.177\n    gamma020_cov: 0.37\n    gamma020_rmse: 0.224\n    breakeven_gamma: 0.1\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-23T19:33:37.787Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T19:33:37.787Z",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-23T19:33:37.806Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Reframed 'When Debiasing Hurts' narrative fully lands：reviewers认为 problem identification 本身是 EMNLP 级贡献，bias identity 的 exact 形式在 LLM annotation 语境下被接受为新颖，EC-HTE 在其 operating regime 内的表现被视为 convincing proof of concept
核心假设：['NLP/CSS-oriented reviewer panel，对 classical measurement error 文献（Fuller/Carroll）不深度熟悉，因此 bias identity 在 LLM annotation 语境下的 formalization 被视为新颖贡献', "'Debiasing can hurt' 的 framing 对 NLP 社区足够 surprising——多数 NLP 工作假设 correction 单调改善，reviewer 认同这是 under-recognized failure mode", 'EC-HTE 的 conditional advantage（extreme heterogeneity + n_expert≥250）被接受为 practical regime——reviewer 认同 CSS 场景中 Δπ>0.10 是常见的（exp-008: 6/6 models Δπ>0.05）', 'Real-data R²=0.944（14 LLM-dataset combos）被视为 strong pattern validation，不要求 ground-truth CATE benchmark', 'Honest limitations disclosure（RMSE tradeoff、K≥8 boundary、real CM negative results）增强可信度而非减分', "Reviewer 不要求 convergence rates 或 minimax bounds——'problem identification + exact identity + diagnostic' 被接受为完整贡献"]
关键指标范围：{'excitement': [4.0, 4.5], 'soundness': [3.5, 4.0], 'overall_recommendation': [3.5, 4.0], 'claim1_bias_identity_accepted_pct': [90, 100], 'claim2_echte_accepted_as_useful_pct': [70, 85], 'claim3_diagnostic_accepted_pct': [65, 80], 'perceived_novelty_score': [3.5, 4.5], 'major_weaknesses_per_review': [0, 1], 'revision_requests': ['minor (figures, writing clarity, bibliography)']}
叙事方向：原始 reframed claims 完全成立。三条贡献层次清晰：(1) bias identity 是 exact 且 constructive，直接揭示 LLM annotation pipeline 中被忽视的 failure mode；(2) EC-HTE 是 identity 自然推导出的修正方案，在 high-heterogeneity regime 效果显著（bias reduction 4-15x，coverage 恢复至 95%）；(3) Δπ×Δτ diagnostic 提供 zero-cost 预检，让 practitioner 不用跑 EC-HTE 也能判断 global correction 是否安全。Abstract 可保留 '2-3x median amplification, up to 5.9x' headline。PPCI 互补性作为 bonus contribution。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f7571620-0051-4fc8-8cd6-f409bae6bab3",
  "type": "user",
  "uuid": "2bc7ed2e-1f49-48cd-ae09-870d8b5cfd2c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T19:33:37.804Z_

```json
{
  "parentUuid": "2bc7ed2e-1f49-48cd-ae09-870d8b5cfd2c",
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
  "uuid": "d83c46ea-2188-436f-860b-0cdb3fbc0288",
  "timestamp": "2026-05-23T19:33:37.804Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T19:33:37.804Z_

```json
{
  "parentUuid": "d83c46ea-2188-436f-860b-0cdb3fbc0288",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "989b0967-c3d0-434f-ba2b-3ede65eb8d9d",
  "timestamp": "2026-05-23T19:33:37.804Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reframed 'When Debiasing Hurts' narrative fully lands：reviewers认为 problem identification 本身是 EMNLP 级贡献，bias identity 的 exact 形式在 LLM annotation 语境下被接受为新颖，E…",
  "leafUuid": "989b0967-c3d0-434f-ba2b-3ede65eb8d9d",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Best-tier prediction: EC-HTE diagnostic at EMNLP",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697"
}
```

---

### Assistant

_source line 8 · 2026-05-23T19:34:16.719Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for each planned experiment in the experiment_plan, based on the "best" tier definition they've provided. Many experiments are already completed (in the registry), so I need to focus on the planned ones that haven't been done yet, or provide predictions for all of them as if imagining the results.

Wait, let me re-read. The user says "对 experiment_plan 中每个 planned 实验展开详细数据" - so for each experiment in the plan, I need to provide detailed predicted data. But many are already done. Let me check which ones are still "planned" in the experiment_plan...


Looking at the statuses, most experiments show as planned in the plan but are already marked done in the registry. Only exp-009 appears to be genuinely unfinished, though the list seems to cut off mid-thought.

Actually, I'm realizing this is a simulation task—the user wants me to imagine what the full experimental results would look like under a "best tier" scenario, generating predicted data for each planned experiment as they'd appear in the paper with supporting rationales. The actual registry results exist, but I need to create the idealized predicted versions that would demonstrate the strongest possible outcomes.

Now I'm structuring the YAML output for all experiments from exp-001 through exp-011, using the best tier thresholds as targets: excitement and perceived novelty around 4.0-4.5, soundness and overall recommendation at 3.5-4.0, and acceptance rates for the three main claims ranging from 65-100% depending on the claim. I'll pull from actual registry data where it exists and frame everything through the lens of what would constitute the strongest possible narrative. Generating YAML output... Writing comprehensive YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "989b0967-c3d0-434f-ba2b-3ede65eb8d9d",
  "isSidechain": false,
  "requestId": "req_011CbL4QyzZRiyKH3Df91HwA",
  "type": "assistant",
  "uuid": "9fbd4735-82c6-415d-bb85-060c5b9b441a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FN8nzkEGw5KTYKNoBaAwrS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27792,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1648,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 27792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27792
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

_source line 9 · 2026-05-23T19:34:17.162Z_

<details open><summary>🔧 Tool call — Read · `toolu_017KbEVqfFb9XSPAoaBvGJs8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fbd4735-82c6-415d-bb85-060c5b9b441a",
  "isSidechain": false,
  "requestId": "req_011CbL4QyzZRiyKH3Df91HwA",
  "type": "assistant",
  "uuid": "a09cd4b9-3182-458e-8d6b-a989e90acf94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FN8nzkEGw5KTYKNoBaAwrS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27792,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1648,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 27792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27792
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

_source line 10 · 2026-05-23T19:34:17.180Z_

<details><summary>↩ Tool result · `toolu_017KbEVqfFb9XSPAoaBvGJs8`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
5	- 不要复述用户的问题
6	- 不要给未被要求的建议或补充说明
7	- 推理要彻底，但输出只保留结论和必要信息
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a09cd4b9-3182-458e-8d6b-a989e90acf94",
  "isSidechain": false,
  "promptId": "f7571620-0051-4fc8-8cd6-f409bae6bab3",
  "type": "user",
  "uuid": "ba3196fa-66a7-4896-9773-7a99fd0a93d5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "a09cd4b9-3182-458e-8d6b-a989e90acf94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:34:23.204Z_

<details open><summary>🔧 Tool call — Read · `toolu_015RuEwFMsURXNkWmHkwK56J`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520/memory/MEMORY.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba3196fa-66a7-4896-9773-7a99fd0a93d5",
  "isSidechain": false,
  "requestId": "req_011CbL4TtHqwu8HarTBanL5A",
  "type": "assistant",
  "uuid": "1fbc0c3d-a30a-45bd-95a6-a0b4d943ea22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pe48rTzipheFAGuUm5GMNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1816,
      "cache_read_input_tokens": 39633,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 39633,
          "cache_creation_input_tokens": 1816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1816
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

_source line 12 · 2026-05-23T19:34:23.210Z_

<details><summary>↩ Tool result · reported error · `toolu_015RuEwFMsURXNkWmHkwK56J`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fbc0c3d-a30a-45bd-95a6-a0b4d943ea22",
  "isSidechain": false,
  "promptId": "f7571620-0051-4fc8-8cd6-f409bae6bab3",
  "type": "user",
  "uuid": "12f024e3-30f9-463c-9ad4-10b34fb0a2c7",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520.",
  "sourceToolAssistantUUID": "1fbc0c3d-a30a-45bd-95a6-a0b4d943ea22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:34:25.071Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DQVpAiMXMhrYwW4nmwMFdG`</summary>

```json
{
  "pattern": "results/*.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12f024e3-30f9-463c-9ad4-10b34fb0a2c7",
  "isSidechain": false,
  "requestId": "req_011CbL4UL87EtdKcJQbQb1iw",
  "type": "assistant",
  "uuid": "8cfb1c73-4a6c-4847-a120-a8fe5d003a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbjQabUNpR4i5ep47gr3w2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 137,
      "cache_read_input_tokens": 41449,
      "output_tokens": 54,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 54,
          "cache_read_input_tokens": 41449,
          "cache_creation_input_tokens": 137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 137
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

_source line 14 · 2026-05-23T19:34:25.096Z_

<details><summary>↩ Tool result · `toolu_01DQVpAiMXMhrYwW4nmwMFdG`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cfb1c73-4a6c-4847-a120-a8fe5d003a7a",
  "isSidechain": false,
  "promptId": "f7571620-0051-4fc8-8cd6-f409bae6bab3",
  "type": "user",
  "uuid": "185885f4-9d63-463f-8a2e-43af77066165",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 21,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "8cfb1c73-4a6c-4847-a120-a8fe5d003a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T19:34:27.115Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Rexp7LrRvq4fW2h9fu6dyw`</summary>

```json
{
  "pattern": "results/**/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "185885f4-9d63-463f-8a2e-43af77066165",
  "isSidechain": false,
  "requestId": "req_011CbL4UUAnwFeuP1NpK3DWT",
  "type": "assistant",
  "uuid": "9bcb19d3-9ca3-4d26-923f-6d4aab315fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YqyHcR8pAW7LK8c4bjc3L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 69,
      "cache_read_input_tokens": 41586,
      "output_tokens": 54,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 69,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 54,
          "cache_read_input_tokens": 41586,
          "cache_creation_input_tokens": 69,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 69
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

_source line 16 · 2026-05-23T19:34:27.132Z_

<details><summary>↩ Tool result · `toolu_01Rexp7LrRvq4fW2h9fu6dyw`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bcb19d3-9ca3-4d26-923f-6d4aab315fd0",
  "isSidechain": false,
  "promptId": "f7571620-0051-4fc8-8cd6-f409bae6bab3",
  "type": "user",
  "uuid": "ef0fbf34-ba35-44f5-a774-87b99cab6da5",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 14,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "9bcb19d3-9ca3-4d26-923f-6d4aab315fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T19:38:50.577Z_

Based on the registry data and best-tier definition, here are the detailed predictions for all 11 planned experiments:

```yaml
tier: best
narrative_guidance: >
  Reframed 'When Debiasing Hurts' narrative fully lands. Reviewers (NLP/CSS-oriented, not deep
  measurement-error specialists) accept the bias identity as novel formalization in the LLM annotation
  context. Three-layer contribution structure — (1) exact bias identity, (2) EC-HTE as identity-prescribed
  correction, (3) Δπ×Δτ diagnostic — reads as coherent and complete. Honest disclosure of RMSE tradeoffs,
  K≥8 boundary, and real-CM negative results (exp-015/016) is perceived as mature scholarship, not weakness.
  Excitement 4.0-4.5 driven by 'debiasing can hurt' surprise factor for NLP audience. Soundness 3.5-4.0
  reflects minor concern about lack of convergence rates but acceptance of empirical thoroughness.
  No reviewer demands minimax bounds; 'problem identification + exact identity + diagnostic' accepted
  as complete contribution package.

imagined_experiments:
  - name: "HB EC-HTE Synthetic Validation"
    plan_id: "exp-001"
    description: >
      Hierarchical Bayesian Dirichlet-prior confusion matrix estimator with partial pooling.
      Full regime sweep: extreme/moderate/homogeneous × n_expert={100,250,500,1000,2000} × K={2,4}.
      3600 MC runs total. MCMC diagnostics: PyMC NUTS, 4 chains, 1000 warmup.
    expected_results:
      mcmc_rhat_max: 1.004
      mcmc_ess_min: 1618
      mcmc_divergent: 0
      total_mc_runs: 3600
      runtime_min: 69
      hb_vs_mle_rmse_improvement_k2_n50: "4-9%"
      hb_vs_mle_rmse_improvement_k4_n50_moderate: "6-9%"
      hb_coverage_median: 0.93
      hb_coverage_min: 0.87
      hyperprior_sensitivity_k2_variation: "<1%"
      hyperprior_sensitivity_k4_variation: "~4-5%"
      singularity_guard_triggers: "extreme/n=50 only"
    result_rationale: >
      Best tier assumes reviewers accept HB partial pooling as well-motivated James-Stein shrinkage.
      R̂<1.01 and ESS>200 (actual: ESS>1618 with 4-chain fix) satisfy standard MCMC convergence criteria —
      NLP reviewers without deep Bayesian background will see these as reassuring checkboxes. 4-9% RMSE
      improvement over MLE at small n is modest but directionally correct; reviewers accept this as
      'partial pooling helps when data is scarce' (classical result, applied to new setting). Coverage
      median 0.93 (below nominal 0.95) is disclosed honestly — reviewer sees this as boundary condition
      acknowledgment, not flaw. Hyperprior sensitivity <5% for K=4 confirms robustness without requiring
      exhaustive sensitivity analysis — one table in appendix suffices.
    tables:
      - name: "Table A1: MCMC Diagnostics Summary"
        columns: ["Config", "R-hat (max)", "ESS (min)", "Divergences", "Runtime (s)"]
        rows:
          - ["K=2/extreme/n=100", "1.003", "1842", "0", "68"]
          - ["K=2/moderate/n=100", "1.002", "2105", "0", "65"]
          - ["K=4/extreme/n=100", "1.004", "1618", "0", "82"]
          - ["K=4/moderate/n=100", "1.003", "1790", "0", "79"]
          - ["K=4/extreme/n=50 (guard)", "1.003", "1650", "0", "85"]
      - name: "Table A2: HB vs MLE RMSE Comparison"
        columns: ["Config", "HB RMSE", "MLE RMSE", "Improvement (%)", "HB Coverage"]
        rows:
          - ["K=2/extreme/n=50", "0.228", "0.248", "+8.1%", "0.91"]
          - ["K=2/extreme/n=100", "0.142", "0.145", "+2.1%", "0.93"]
          - ["K=2/extreme/n=250", "0.091", "0.093", "+2.2%", "0.94"]
          - ["K=4/moderate/n=50", "0.195", "0.213", "+8.5%", "0.89"]
          - ["K=4/extreme/n=50", "0.310", "0.382", "+18.8%", "0.87"]
          - ["K=4/extreme/n=100", "0.210", "0.225", "+6.7%", "0.92"]
      - name: "Table A3: Hyperprior Sensitivity (Gamma scale)"
        columns: ["Scale", "K=2 RMSE", "K=4 RMSE", "Coverage"]
        rows:
          - ["0.5x", "0.091", "0.208", "0.93"]
          - ["1.0x (base)", "0.091", "0.210", "0.93"]
          - ["2.0x", "0.091", "0.219", "0.93"]
    figures_description:
      - "Appendix figure: HB vs MLE RMSE ratio across n_expert, colored by regime. Shows convergence at n≥500."
    analysis: >
      Reviewers in best tier see this as thorough validation infrastructure. The 4-chain MCMC fix
      (resolving initial K=4/extreme/n=50 blowup) is disclosed as methodological due diligence.
      Key narrative: HB provides meaningful but modest improvement over MLE — the contribution is NOT
      'HB is dramatically better' but rather 'stratified correction with principled shrinkage enables
      reliable per-subgroup CM estimation.' This framing aligns with the paper's positioning as
      problem-identification rather than method-innovation. Reviewer concern about computational cost
      (69 min for full sweep) is preempted by noting this is a one-time calibration, not per-prediction cost.

  - name: "Bias Identity Verification"
    plan_id: "exp-002"
    description: >
      Formal derivation and empirical verification of bias = f(Δπ, Δτ) identity.
      Systematic parameter grid: Δπ ∈ {0, 0.05, ..., 0.25} × Δτ ∈ {0, 0.1, ..., 0.5} × K ∈ {2,4}.
      'Debiasing can hurt' proposition with constructive two-subgroup example. 520 non-trivial configs.
    expected_results:
      r2_k2: 0.994
      r2_k4: 0.974
      tightness_ratio_k2_median: 1.003
      tightness_ratio_k4_median: 1.023
      debiasing_hurts_pct: 50
      debiasing_hurts_pct_detail: "260/520 configs (excluding Δτ=0)"
      max_bias_ratio_k2: 2.86
      max_bias_ratio_k4: 2.41
      coverage_2se_k2: 0.951
      coverage_2se_k4: 0.940
      headline_median_amplification: "2-3x"
      headline_max_amplification: "5.9x (K=4, CausalForest, from exp-011)"
    result_rationale: >
      This is THE core contribution for best tier. R²=0.994 (K=2) and 0.974 (K=4) confirm the
      identity is exact at population level — finite-sample noise explains remaining variance, NOT
      bound looseness. Best-tier reviewers accept this framing because: (1) 'bias decomposition identity'
      language (not 'bound') is technically precise, (2) tightness ratio ~1.0 means MC estimate matches
      analytic prediction almost exactly, (3) the 50% 'debiasing hurts' rate is striking — it means
      global correction is a coin flip in terms of whether it helps or hurts across the parameter space.
      The '2-3x median, up to 5.9x' headline is calibrated: median is robust (not cherry-picked extreme),
      5.9x is from CausalForest (exp-011) which amplifies via nonlinear estimation. NLP reviewers
      unfamiliar with Fuller/Carroll see the Δπ×Δτ product form as novel; the explicit 'this is classical
      in spirit but new in this specific context' framing preempts the one reviewer who might know
      measurement error literature. K=2 max 2.86× vs K=4 max 2.41× (DIM) is counter-intuitive and
      strengthens novelty — NOT monotonic in K, demonstrating the identity captures non-trivial structure.
    tables:
      - name: "Table 1: Bias Amplification Under Global Correction (Main Paper)"
        columns: ["K", "Δπ", "Δτ", "Analytic Bias", "MC Bias (SE)", "Ratio MC/Analytic", "Global Hurts?"]
        rows:
          - ["2", "0.05", "0.1", "0.005", "0.005 (0.001)", "1.00", "No"]
          - ["2", "0.10", "0.2", "0.020", "0.020 (0.002)", "1.00", "Yes"]
          - ["2", "0.15", "0.3", "0.045", "0.046 (0.003)", "1.02", "Yes"]
          - ["2", "0.20", "0.5", "0.100", "0.101 (0.005)", "1.01", "Yes"]
          - ["2", "0.25", "0.5", "0.125", "0.127 (0.006)", "1.02", "Yes"]
          - ["4", "0.10", "0.2", "0.020", "0.021 (0.003)", "1.05", "Yes"]
          - ["4", "0.20", "0.5", "0.100", "0.103 (0.008)", "1.03", "Yes"]
      - name: "Table 2: Debiasing-Hurts Summary Statistics"
        columns: ["Estimator", "K", "Max Amplification", "Median Amplification", "Hurts Rate (%)"]
        rows:
          - ["DIM", "2", "2.86x", "2.1x", "50%"]
          - ["DIM", "4", "2.41x", "1.8x", "50%"]
          - ["CausalForest", "2", "3.2x", "2.3x", "50%"]
          - ["CausalForest", "4", "5.9x", "3.1x", "50%"]
    figures_description:
      - "Figure 1 (Main): Bias amplification heatmap — Δπ (x-axis) vs Δτ (y-axis), color = amplification ratio. Clear product-structure gradient. White diagonal = amplification = 1.0 boundary."
      - "Figure 2 (Main): Constructive 'debiasing hurts' example — two-subgroup case showing over-correction in low-error subgroup, under-correction in high-error subgroup. Schematic + MC verification overlay."
    analysis: >
      Best tier reviewers rate this 4.0-4.5 excitement because the 'debiasing can hurt' framing
      is genuinely surprising to NLP audience. Most NLP papers assume correction monotonically improves
      estimates; showing 50% failure rate across parameter space is a 'stop and think' result.
      The exact identity (not a bound) is clean enough to be stated as Theorem 1 in under 5 lines.
      R² > 0.97 across all K values makes the empirical verification convincing without requiring
      formal convergence rate proofs. One reviewer may note the classical measurement error parallel
      (Fuller 1987 Sec 2.3) — the explicit citation and 'new in LLM context' framing deflects this
      to a minor comment rather than a novelty objection.

  - name: "Semi-Synthetic CSS Benchmark"
    plan_id: "exp-003"
    description: >
      TweetEval sentiment (N=45K). Inject known CATE heterogeneity, annotate with GPT-4.1.
      K=4 subgroups (text features: has_hashtag × text_length). 100 MC runs with HB integration.
      Methods: oracle, naive, global_corrected, stratified_mle, hb_ec_hte.
    expected_results:
      n_subgroups: 4
      misclass_rates: "S0=0.05, S1=0.10, S2=0.15, S3=0.25"
      delta_pi: 0.20
      debiasing_hurts_confirmed: true
      mc_runs: 100
      hb_vs_mle_n100_S3_extreme: "+60% RMSE improvement (HB dramatically better)"
      hb_vs_mle_n100_S2: "+5-8% RMSE improvement"
      hb_vs_mle_n250_S3: "+5-17% RMSE improvement"
      hb_vs_mle_n500: "converged (<1.6% difference)"
      boundary_condition: "n=50 with extreme heterogeneity in tiny subgroups (S3=12%) shows moderate degradation"
      hb_n50_S3_degradation: "-57% RMSE (HB worse but not catastrophic)"
    result_rationale: >
      Semi-synthetic design validates the bias identity in a realistic annotation pipeline: GPT-4.1
      on TweetEval sentiment produces genuine subgroup-varying misclassification (Δπ=0.20), not
      synthetic noise injection. Best-tier reviewers accept this because: (1) the DGP is fully
      specified (outcome generation + treatment assignment + CATE injection), satisfying the
      'semi-synthetic transparency' requirement, (2) Δπ=0.20 matches the exp-012 pilot finding
      (Δπ=0.200 from GPT-4.1), confirming the heterogeneity is real, not assumed, (3) the +60%
      RMSE improvement at n=100/S3 demonstrates HB's value precisely where it matters most — the
      high-error minority subgroup. The n=50 degradation is disclosed honestly and positioned as a
      boundary condition, not a failure. NLP reviewers see 'real LLM + real corpus' as strong
      validation even though CATEs are injected. The 12% minority subgroup size (S2, S3) maps to
      realistic CSS scenarios (e.g., minority demographic groups in survey data).
    tables:
      - name: "Table 3: Semi-Synthetic Benchmark Results (Main Paper)"
        columns: ["Method", "Subgroup", "n_expert", "|Bias|", "RMSE", "Coverage"]
        rows:
          - ["Oracle", "All", "-", "0.003", "0.045", "0.96"]
          - ["Naive", "S3 (high-error)", "-", "0.089", "0.109", "0.82"]
          - ["Global Corrected", "S3 (high-error)", "-", "0.142", "0.165", "0.78"]
          - ["Stratified MLE", "S3 (high-error)", "100", "0.038", "0.195", "0.91"]
          - ["HB EC-HTE", "S3 (high-error)", "100", "0.015", "0.078", "0.93"]
          - ["HB EC-HTE", "S3 (high-error)", "250", "0.008", "0.062", "0.94"]
          - ["HB EC-HTE", "S3 (high-error)", "500", "0.004", "0.051", "0.95"]
          - ["Global Corrected", "S0 (low-error)", "-", "0.067", "0.082", "0.85"]
          - ["HB EC-HTE", "S0 (low-error)", "100", "0.005", "0.048", "0.94"]
      - name: "Table A4: Debiasing Hurts in Semi-Synthetic Setting"
        columns: ["Subgroup", "Naive |Bias|", "Global |Bias|", "Amplification", "Direction"]
        rows:
          - ["S0 (π=0.05)", "0.012", "0.067", "5.6x", "Over-corrected"]
          - ["S1 (π=0.10)", "0.035", "0.048", "1.4x", "Over-corrected"]
          - ["S2 (π=0.15)", "0.058", "0.052", "0.9x", "Slight improvement"]
          - ["S3 (π=0.25)", "0.089", "0.142", "1.6x", "Under-corrected"]
    figures_description:
      - "Figure 3 (Main): Per-subgroup bias comparison — grouped bar chart, naive vs global vs EC-HTE, showing over/under-correction pattern in global, near-zero in EC-HTE."
    analysis: >
      The semi-synthetic benchmark is the paper's empirical centerpiece. Best-tier reviewers see the
      'global hurts S0 by 5.6×' result as the most compelling instantiation of the bias identity —
      a low-error subgroup gets WORSE after correction, which is exactly the failure mode the paper
      identifies. The progression from n=50 (HB struggles) to n=100 (HB wins) to n=500 (converged)
      maps cleanly to the budget guidance in exp-006. Honest disclosure of n=50 boundary makes the
      n≥100 recommendation credible.

  - name: "Real-Data Case Study (Pattern Consistency)"
    plan_id: "exp-004"
    description: >
      UC Berkeley Measuring Hate Speech corpus. N=2496 comments. GPT-4.1 annotation.
      Subgroups: platform_group × text_length (K=4). Pattern consistency analysis,
      NOT ground-truth CATE benchmark. Bootstrap CIs on point estimate differences.
    expected_results:
      dataset: "UC Berkeley Measuring Hate Speech"
      n_comments: 2496
      delta_pi: 0.117
      global_FPR: 0.139
      global_FNR: 0.533
      misclass_range: "0.266 - 0.383"
      echte_vs_global_avg_bias: "EC-HTE does not outperform global (high FNR limits correction)"
      key_pattern: "Δπ=0.117 confirms real-world heterogeneity exists"
      honest_limitation: "High FNR (53%) makes CM near-singular for positive class"
    result_rationale: >
      This is a negative/mixed result that STRENGTHENS the best-tier narrative. The real-data case
      shows: (1) misclassification heterogeneity exists in real LLM annotation (Δπ=0.117, statistically
      significant), validating the premise that global correction is mis-specified in practice,
      (2) EC-HTE does NOT outperform when FNR≈53% (near-random for positive class) — this connects
      to the honest boundary condition from exp-015/016 and the 'classifier quality threshold'
      limitation. Best-tier reviewers see this as mature scholarship: the authors don't cherry-pick
      favorable datasets, they show where the method works AND where it doesn't, and explain WHY
      (near-singular CM). The 'pattern consistency, not ground-truth benchmark' framing is accepted
      because reviewers agree no ground-truth CATE exists for observational data.
    tables:
      - name: "Table 4: Real-Data Misclassification Heterogeneity (Main Paper)"
        columns: ["Subgroup", "n", "FPR", "FNR", "Overall Misclass Rate"]
        rows:
          - ["plat0_long", "624", "0.08", "0.58", "0.266"]
          - ["plat0_short", "624", "0.12", "0.62", "0.337"]
          - ["plat23_long", "624", "0.10", "0.55", "0.303"]
          - ["plat23_short", "624", "0.15", "0.59", "0.383"]
          - ["Global (pooled)", "2496", "0.139", "0.533", "0.322"]
      - name: "Table A5: Real-Data CATE Comparison"
        columns: ["Method", "Avg |Bias|", "Bootstrap 95% CI Width", "Note"]
        rows:
          - ["Naive", "0.210", "0.18", "Baseline"]
          - ["Global Corrected", "0.273", "0.22", "FNR=53% amplifies noise"]
          - ["EC-HTE", "0.313", "0.31", "Wide CIs due to near-singular CM"]
          - ["Note", "-", "-", "No ground-truth CATE; pattern comparison only"]
    figures_description:
      - "Appendix figure: Per-subgroup misclassification rate bar chart with 95% bootstrap CIs, showing statistically significant heterogeneity."
    analysis: >
      Best-tier reviewers (70-85% accept EC-HTE as useful) interpret this correctly: the negative
      real-data result is a feature, not a bug. It demonstrates the diagnostic criterion's value —
      a practitioner would compute Δπ=0.117 and FNR=0.533, conclude the classifier quality is
      insufficient for stratified correction, and stick with global correction or improve the
      classifier. This directly validates Claim 3 (diagnostic) by showing a real scenario where
      the diagnostic would correctly advise AGAINST EC-HTE. Reviewers note the honest framing
      approvingly: 'the authors show both success and failure cases.' Revision request: one
      reviewer asks for a second real dataset with lower FNR to show EC-HTE working — this is
      classified as minor revision.

  - name: "Diagnostic Criterion Validation"
    plan_id: "exp-005"
    description: >
      Compute Δπ × Δτ product from pilot data across all experimental settings.
      ROC analysis of threshold for predicting when global correction fails.
      Cross-validated (NOT in-sample) AUC.
    expected_results:
      subgroup_level_auc: 0.833
      subgroup_correlation: 0.86
      setting_level_auc: 0.49
      low_pi_hurt_pct: 84.6
      high_pi_hurt_pct: 15.4
      theory_alignment: "consistent with exp-002 formula"
    result_rationale: >
      Subgroup-level AUC=0.833 is strong for a zero-cost diagnostic. Best-tier reviewers accept this
      as 'useful practical tool' (65-80% acceptance range). The setting-level AUC=0.49 (near random)
      is an honest disclosure — the diagnostic works at the subgroup level (predicting WHICH subgroups
      get hurt) but not at the setting level (predicting WHETHER any subgroup gets hurt). This is
      theoretically consistent: the bias identity is a per-subgroup statement (each subgroup has its
      own Δπ_k × Δτ_k), not a global statement. Reviewers see this distinction as demonstrating
      understanding of the theory's scope. The 84.6% hurt rate for low-Δπ subgroups vs 15.4% for
      high-Δπ subgroups confirms the asymmetry predicted by the identity: low-error subgroups are
      over-corrected by global pooling. This is the 'debiasing hurts' mechanism in action.
    tables:
      - name: "Table 5: Diagnostic Criterion Performance (Main Paper)"
        columns: ["Level", "AUC", "Correlation", "Precision@80%Recall", "Note"]
        rows:
          - ["Subgroup-level", "0.833", "0.86", "0.79", "Primary diagnostic"]
          - ["Setting-level", "0.49", "0.12", "0.51", "Near random (expected)"]
      - name: "Table A6: Diagnostic by Subgroup Δπ Quartile"
        columns: ["Δπ Quartile", "Hurt Rate (%)", "Mean Amplification", "Diagnostic Recommendation"]
        rows:
          - ["Q1 (lowest Δπ)", "84.6%", "2.8x", "Flag: likely over-corrected"]
          - ["Q2", "62.3%", "1.6x", "Caution: mixed"]
          - ["Q3", "38.1%", "0.9x", "OK: near breakeven"]
          - ["Q4 (highest Δπ)", "15.4%", "0.5x", "Safe: under-corrected, global helps"]
    figures_description:
      - "Figure 4 (Main): Diagnostic ROC curve at subgroup level with AUC=0.833. Annotated operating point at 80% recall."
      - "Appendix figure: Scatter plot of Δπ×Δτ product vs actual bias amplification, showing strong subgroup-level correlation (r=0.86)."
    analysis: >
      Best-tier reviewers (65-80% acceptance for diagnostic) see AUC=0.833 as 'good enough for
      practical use.' The key selling point is zero cost — the diagnostic requires only a pilot
      confusion matrix, which practitioners already compute. Even without adopting EC-HTE, knowing
      when global correction backfires has standalone value. The setting-level AUC=0.49 is a
      limitation that reviewers note but don't penalize heavily, because the subgroup-level diagnostic
      is what matters for the 'which subgroups to worry about' decision. One reviewer may request
      cross-validation details — this is a minor revision request.

  - name: "Expert Label Budget Sensitivity"
    plan_id: "exp-006"
    description: >
      Systematic sweep: n_expert ∈ {50,100,250,500,1000,2000} × K ∈ {2,4} × regime ∈ {extreme,moderate}.
      Find RMSE crossover where EC-HTE beats global. 288 total configs, 100 MC runs each.
    expected_results:
      total_configs: 288
      runtime_min: 110
      crossover_K2_extreme: 250
      crossover_K2_moderate: "never (global always better on RMSE)"
      crossover_K4_extreme: 1000
      crossover_K4_moderate: 2000
      hb_beats_mle_pct: "87.5% (21/24 configs)"
      convergence_threshold: "n≥1000: HB ≈ MLE (<0.5%)"
      best_hb_improvement: "K=4/moderate/n=50/sgC: +42.4% RMSE over MLE"
    result_rationale: >
      Budget sensitivity is critical for Claim 2 acceptance (70-85% in best tier). The crossover
      points provide actionable guidance: K=2/extreme at n=250 is practical (typical CSS study can
      afford 250 expert labels), K=4/extreme at n=1000 is feasible but expensive. The 'K=2/moderate
      never crosses' result is an honest limitation that HELPS the narrative — it connects directly
      to Claim 3 (diagnostic): when heterogeneity is moderate, the diagnostic correctly advises
      against EC-HTE. Best-tier reviewers see this as 'the method knows when to use itself.'
      The 87.5% HB≥MLE rate confirms partial pooling rarely hurts (James-Stein guarantee in
      symmetric DGP). Convergence at n≥1000 shows HB advantage is most valuable in the
      data-scarce regime where it matters most.
    tables:
      - name: "Table 6: Expert Budget Crossover Points (Main Paper)"
        columns: ["K", "Regime", "Crossover n_expert", "HB RMSE at Crossover", "Global RMSE at Crossover"]
        rows:
          - ["2", "Extreme", "250", "0.091", "0.095"]
          - ["2", "Moderate", "Never", "-", "-"]
          - ["4", "Extreme", "1000", "0.068", "0.072"]
          - ["4", "Moderate", "2000", "0.055", "0.058"]
      - name: "Table A7: Full Budget Sweep"
        columns: ["n_expert", "K", "Regime", "HB RMSE", "MLE RMSE", "Global RMSE", "HB Wins?"]
        rows:
          - ["50", "2", "extreme", "0.228", "0.248", "0.105", "vs MLE yes, vs Global no"]
          - ["100", "2", "extreme", "0.142", "0.145", "0.098", "vs MLE yes, vs Global no"]
          - ["250", "2", "extreme", "0.091", "0.093", "0.095", "Both"]
          - ["500", "2", "extreme", "0.072", "0.073", "0.092", "Both"]
          - ["50", "4", "extreme", "0.310", "0.382", "0.128", "vs MLE yes"]
          - ["250", "4", "extreme", "0.135", "0.140", "0.110", "vs MLE yes"]
          - ["1000", "4", "extreme", "0.068", "0.069", "0.072", "Both"]
    figures_description:
      - "Figure 5 (Main): Budget crossover curves — RMSE (y-axis) vs n_expert (x-axis), separate lines for HB/MLE/Global, faceted by K×regime. Crossover points annotated."
    analysis: >
      Best-tier reviewers want actionable budget guidance. The 'Expert Budget Recommendation'
      subsection distills this: 'For K=2 with high heterogeneity, 250 expert labels suffice.
      For K=4, budget 1000. When diagnostic indicates moderate heterogeneity, global correction
      is the safer choice.' This connects Claims 2 and 3 into a coherent decision framework.
      The HB vs MLE comparison (87.5% HB wins) is a secondary but reassuring result — it justifies
      the Bayesian machinery over simpler alternatives.

  - name: "PPCI + DSL Baseline Comparison"
    plan_id: "exp-007"
    description: >
      Four DGPs: A (covariate-only error), B (outcome-only error), C (both errors), D (no error).
      8 methods including EC-HTE, PPCI, EC-HTE+PPCI composition, DSL per-subgroup.
      6912 total rows, 100 MC runs per config.
    expected_results:
      total_rows: 6912
      dgps: ["A_covariate_only", "B_outcome_only", "C_both_errors", "D_no_error"]
      methods: 8
      dgp_c_extreme_n250_k2_ec_hte_ppci_bias: 0.005
      dgp_c_extreme_n250_k2_ec_hte_bias: 0.178
      dgp_c_extreme_n250_k2_ppci_bias: 0.004
      dgp_c_extreme_n250_k2_naive_bias: 0.251
      bias_reduction_composition_vs_echte: "35x"
      coverage_ec_hte_ppci: 1.0
      dgp_a_ec_hte_ppci_equals_ec_hte: true
    result_rationale: >
      The PPCI composition result is the paper's strongest empirical finding for best tier.
      EC-HTE+PPCI achieves near-zero bias (0.005) in DGP C — a 35× improvement over EC-HTE alone.
      This proves 'necessary and sufficient in composition': EC-HTE handles structured covariate
      error, PPCI rectifier handles outcome error, composition handles both. Best-tier reviewers
      (NLP-oriented) see this as a complete pipeline solution: LLM annotation introduces BOTH
      error types, and the composition addresses both. The DGP A control (EC-HTE+PPCI = EC-HTE)
      confirms no double-correction — PPCI correctly contributes nothing when there's no outcome error.
      DGP D (no error) confirms all methods reduce to oracle. The 'pure covariate-error' control
      (DGP A) demonstrates EC-HTE's structural advantage: PPCI alone has higher variance because
      it treats covariate error as a generic black-box correction, while EC-HTE exploits the
      mixing matrix structure.
    tables:
      - name: "Table 7: Method Comparison Across Error Types (Main Paper)"
        columns: ["DGP", "Method", "|Bias| (z0)", "RMSE (z0)", "Coverage"]
        rows:
          - ["A (cov only)", "EC-HTE", "0.008", "0.089", "0.94"]
          - ["A (cov only)", "PPCI", "0.045", "0.132", "0.88"]
          - ["A (cov only)", "EC-HTE+PPCI", "0.008", "0.089", "0.94"]
          - ["B (out only)", "EC-HTE", "0.085", "0.112", "0.87"]
          - ["B (out only)", "PPCI", "0.006", "0.098", "0.95"]
          - ["B (out only)", "EC-HTE+PPCI", "0.005", "0.095", "0.96"]
          - ["C (both)", "Naive", "0.251", "0.269", "0.72"]
          - ["C (both)", "EC-HTE", "0.178", "0.226", "0.83"]
          - ["C (both)", "PPCI", "0.004", "0.261", "0.91"]
          - ["C (both)", "EC-HTE+PPCI", "0.005", "0.225", "1.00"]
          - ["D (none)", "All methods", "~0.002", "~0.045", "~0.95"]
      - name: "Table A8: DSL Per-Subgroup Baseline"
        columns: ["Config", "DSL |Bias|", "EC-HTE |Bias|", "DSL RMSE", "EC-HTE RMSE"]
        rows:
          - ["K=2/extreme/n=250", "0.015", "0.008", "0.115", "0.089"]
          - ["K=2/extreme/n=500", "0.010", "0.005", "0.085", "0.072"]
          - ["K=4/extreme/n=500", "0.022", "0.012", "0.142", "0.120"]
    figures_description:
      - "Appendix figure: 2×2 grid of DGP panels showing method performance. Highlights EC-HTE+PPCI dominance in DGP C."
    analysis: >
      Best-tier reviewers see the composition result as elevating the contribution from 'yet another
      correction method' to 'principled framework for LLM annotation pipelines.' The EC-HTE+PPCI
      composition addresses the realistic scenario where both covariate and outcome errors coexist —
      which is the default in LLM annotation. The DSL comparison shows EC-HTE's structural advantage
      (mixing matrix exploitation + shrinkage) over generic per-subgroup correction. Reviewer concern
      about 'just use PPCI' is preempted by DGP A results: PPCI alone has higher variance when
      error is purely covariate-side.

  - name: "Multiple LLM Annotator Comparison"
    plan_id: "exp-008"
    description: >
      Six OpenAI models: GPT-3.5-turbo, GPT-4-turbo, GPT-4o, GPT-4o-mini, GPT-4.1, GPT-5.4.
      TweetEval sentiment. Measure per-subgroup misclassification heterogeneity across models.
      Test structural persistence of heterogeneity.
    expected_results:
      models_completed: 6
      all_delta_pi_above_005: true
      effective_delta_pi_range: "0.080 - 0.198"
      worst_subgroup_consensus: "True_medium (5/6 models)"
      spearman_significant_pairs: 4
      gpt35_delta_pi: 0.198
      gpt41_delta_pi: 0.098
      gpt4o_delta_pi: 0.080
      gpt5x_delta_pi: 0.114
    result_rationale: >
      This experiment validates the paper's core premise: misclassification heterogeneity is
      STRUCTURAL, not model-specific. All 6 models across 3 generations (GPT-3.5 through GPT-5.4)
      show Δπ > 0.05 — the threshold where the bias identity predicts meaningful amplification.
      Best-tier reviewers see this as strong evidence that the problem won't 'go away with better
      models.' The worst-subgroup consensus (True_medium, 5/6 models) suggests text features
      driving misclassification are stable across architectures. The Spearman correlations (4 significant
      pairs) show error patterns are correlated across models — the same subgroups are hard for all
      LLMs. This is a P1 experiment that moves to appendix but provides crucial evidence for the
      'this matters in practice' argument. Best-tier reviewers cite this as supporting evidence when
      rating practical significance.
    tables:
      - name: "Table A9: Cross-Model Misclassification Heterogeneity (Appendix)"
        columns: ["Model", "Overall Accuracy", "Effective Δπ", "Worst Subgroup", "Best Subgroup"]
        rows:
          - ["GPT-3.5-turbo", "0.78", "0.198", "True_medium (0.39)", "False_medium (0.10)"]
          - ["GPT-4-turbo", "0.83", "0.149", "True_medium (0.28)", "False_medium (0.08)"]
          - ["GPT-4o", "0.85", "0.080", "True_medium (0.22)", "False_medium (0.07)"]
          - ["GPT-4o-mini", "0.82", "0.136", "True_medium (0.30)", "False_medium (0.09)"]
          - ["GPT-4.1", "0.86", "0.098", "True_medium (0.24)", "False_short (0.07)"]
          - ["GPT-5.4", "0.84", "0.114", "True_medium (0.26)", "False_medium (0.08)"]
    figures_description:
      - "Appendix figure: Grouped bar chart of Δπ across 6 models, with horizontal line at Δπ=0.05 threshold. All bars above threshold."
    analysis: >
      Moved to appendix per paper framing guidelines. But best-tier reviewers reference it in
      reviews: 'The multi-model analysis convincingly demonstrates that heterogeneity is structural.'
      The fact that even GPT-5.4 shows Δπ=0.114 preempts the 'future models will fix this' objection.

  - name: "Adaptive Expert Annotation Allocation"
    plan_id: "exp-009"
    description: >
      CATE-weighted allocation targeting high-CATE × high-error subgroups.
      Compare against uniform and uncertainty-only allocation.
      Stage 3 experiment — builds on exp-001 infrastructure and exp-006 budget analysis.
    expected_results:
      allocation_strategies: ["uniform", "uncertainty_only", "cate_weighted"]
      uniform_rmse_k4_n500: 0.120
      uncertainty_rmse_k4_n500: 0.105
      cate_weighted_rmse_k4_n500: 0.095
      cate_weighted_improvement_vs_uniform: "~21%"
      cate_weighted_improvement_vs_uncertainty: "~10%"
      effective_crossover_reduction: "Reduces K=4 crossover from n=1000 to ~700"
      coverage_all_strategies: "0.92-0.95"
    result_rationale: >
      P2 experiment — appendix material. Under best tier, reviewers see adaptive allocation as
      a nice-to-have extension that demonstrates the framework's practical flexibility. The 21%
      RMSE improvement over uniform allocation is meaningful but not dramatic — it confirms that
      allocation matters but doesn't change the paper's main conclusions. The 'reduces crossover
      from n=1000 to ~700' result tightens the budget guidance from exp-006 but is incremental.
      Best-tier reviewers mention this favorably in 'additional contributions' but don't weight it
      heavily in their overall assessment. The CATE-weighted strategy's advantage comes from
      concentrating expert labels where both error and effect heterogeneity are highest — this is
      a direct application of the Δπ×Δτ diagnostic (Claim 3) to allocation, creating a nice
      conceptual link.
    tables:
      - name: "Table A10: Allocation Strategy Comparison (Appendix)"
        columns: ["Strategy", "K", "n_expert", "RMSE", "Coverage", "Crossover n"]
        rows:
          - ["Uniform", "4", "500", "0.120", "0.93", "1000"]
          - ["Uncertainty-only", "4", "500", "0.105", "0.93", "850"]
          - ["CATE-weighted", "4", "500", "0.095", "0.94", "700"]
          - ["Uniform", "2", "250", "0.091", "0.94", "250"]
          - ["CATE-weighted", "2", "250", "0.082", "0.94", "180"]
    figures_description:
      - "Appendix figure: Budget crossover curves under different allocation strategies, showing leftward shift with CATE-weighted allocation."
    analysis: >
      P2 experiment positioned as 'practical extension.' Best-tier reviewers note it approvingly
      but don't consider it a core contribution. One reviewer may suggest this as future work
      rather than appendix material — minor framing decision, not a weakness.

  - name: "Robustness to Misspecified Subgroup Structure"
    plan_id: "exp-010"
    description: >
      Test EC-HTE when subgroups are noisy/overlapping. Noise levels: 0%, 10%, 25%, 50% subgroup
      misassignment. K={2,4}. Coverage as decisive metric.
    expected_results:
      noise_levels: [0, 0.1, 0.25, 0.5]
      total_runs: 800
      k2_coverage_hb_range: "0.945 - 0.958"
      k4_coverage_hb_range: "0.946 - 0.960"
      k2_coverage_naive_range: "0.875 - 0.897"
      hb_beats_mle_all_configs: true
      graceful_convergence_at_50pct: true
      coverage_drop_0_to_50_noise: "-1.3pp (K=2), -1.0pp (K=4)"
    result_rationale: >
      Robustness is essential for reviewer acceptance of Claim 2 (70-85% range). The key result is
      graceful degradation: EC-HTE coverage drops only ~1pp from 0% to 50% noise, while maintaining
      nominal coverage (>94.5%) at all noise levels. This directly addresses reviewer concern #4
      ('how sensitive to subgroup definition?') with a quantitative answer: 'not very.' The mechanism
      is HB partial pooling — at 50% noise, subgroups are essentially random, and HB automatically
      shrinks toward global (its prior), recovering global correction's behavior. This is the
      James-Stein guarantee in action: 'never much worse than the shrinkage target.' Naive coverage
      (87-90%) is consistently below nominal, confirming that misclassification bias — not subgroup
      misspecification — is the dominant source of coverage failure. Best-tier reviewers see this
      robustness analysis as demonstrating methodological maturity.
    tables:
      - name: "Table A11: Robustness to Subgroup Noise (Appendix)"
        columns: ["Noise (%)", "K", "HB Coverage", "Global Coverage", "Naive Coverage", "HB RMSE"]
        rows:
          - ["0%", "2", "0.958", "0.925", "0.875", "0.089"]
          - ["10%", "2", "0.948", "0.935", "0.877", "0.092"]
          - ["25%", "2", "0.950", "0.932", "0.890", "0.094"]
          - ["50%", "2", "0.945", "0.945", "0.897", "0.096"]
          - ["0%", "4", "0.956", "0.930", "0.904", "0.120"]
          - ["10%", "4", "0.958", "0.953", "0.916", "0.122"]
          - ["25%", "4", "0.960", "0.948", "0.909", "0.125"]
          - ["50%", "4", "0.946", "0.944", "0.919", "0.128"]
    figures_description:
      - "Appendix figure: Coverage vs noise level, showing EC-HTE flat near 95% while naive degrades. HB converges to global at 50% noise."
    analysis: >
      Best-tier reviewers use this to rebut their own concern about subgroup sensitivity. The
      'automatic shrinkage to global at high noise' property is intellectually satisfying — it means
      EC-HTE is a strict generalization of global correction, not a fragile alternative. Coverage
      as the decisive metric (not RMSE) is the right framing: practitioners care about interval
      validity more than point estimate precision.

  - name: "Causal Forest Integration"
    plan_id: "exp-011"
    description: >
      EC-HTE correction applied to CausalForestDML subgroup estimates. Compare naive_forest,
      global_forest, ec_hte_forest. K={2,4} × regime × n_expert. 144 total rows, 100 MC runs.
    expected_results:
      n_mc: 100
      n_configs: 8
      total_rows: 144
      mean_abs_bias_naive_forest: 0.156
      mean_abs_bias_global_forest: 0.107
      mean_abs_bias_ec_hte_forest: 0.061
      mean_rmse_naive_forest: 0.178
      mean_rmse_global_forest: 0.166
      mean_rmse_ec_hte_forest: 0.229
      debiasing_hurts_max_ratio: "5.9x (K=4/extreme/sg0)"
      debiasing_hurts_cases: 9
      k2_n500_ec_hte_bias_range: "0.004-0.013 (near zero)"
      pattern_consistent_with_dim: true
    result_rationale: >
      CausalForest integration is P0 because Claim 2 explicitly mentions CausalForestDML — without
      this experiment, there's a claim-evidence gap that reviewers would flag as a killshot.
      The results show two key patterns: (1) EC-HTE achieves 61% bias reduction vs naive and 43%
      vs global, confirming the correction generalizes beyond DIM to nonlinear CATE estimators,
      (2) the 'debiasing hurts' effect is AMPLIFIED with CausalForest (5.9× for K=4/extreme vs
      2.41× for DIM) — nonlinear estimation compounds the misclassification-induced bias. This
      amplification is the headline '5.9×' number in the abstract. Best-tier reviewers accept
      the RMSE tradeoff (EC-HTE RMSE 0.229 > global 0.166) because it's disclosed honestly and
      explained: variance-bias tradeoff from per-subgroup CM estimation. At n=500/K=2, EC-HTE
      bias is near-zero (0.004-0.013) with competitive RMSE, showing the tradeoff resolves with
      sufficient expert labels. The '5.9× amplification with CausalForest' result is particularly
      impactful for NLP audience — many CSS researchers use causal forests, so this directly
      threatens their existing workflows.
    tables:
      - name: "Table 8: CausalForest Integration Results (Main Paper)"
        columns: ["Method", "Mean |Bias|", "Mean RMSE", "Max Amplification", "K=2/n=500 |Bias|"]
        rows:
          - ["Naive Forest", "0.156", "0.178", "-", "0.125"]
          - ["Global Forest", "0.107", "0.166", "5.9x (K=4/extreme/sg0)", "0.033-0.109"]
          - ["EC-HTE Forest", "0.061", "0.229", "-", "0.004-0.013"]
      - name: "Table 9: Debiasing-Hurts Cases in CausalForest (Main Paper)"
        columns: ["Config", "Subgroup", "Naive |Bias|", "Global |Bias|", "Amplification"]
        rows:
          - ["K=4/extreme", "sg0 (lowest π)", "0.018", "0.106", "5.9x"]
          - ["K=4/extreme", "sg1", "0.045", "0.078", "1.7x"]
          - ["K=2/extreme", "sg0 (lowest π)", "0.022", "0.063", "2.9x"]
          - ["K=2/moderate", "sg0", "0.015", "0.031", "2.1x"]
      - name: "Table A12: Bias-RMSE Tradeoff by Budget"
        columns: ["n_expert", "K", "EC-HTE |Bias|", "EC-HTE RMSE", "Global |Bias|", "Global RMSE"]
        rows:
          - ["100", "2", "0.025", "0.185", "0.071", "0.112"]
          - ["250", "2", "0.012", "0.128", "0.065", "0.108"]
          - ["500", "2", "0.006", "0.095", "0.059", "0.105"]
          - ["250", "4", "0.032", "0.265", "0.095", "0.145"]
          - ["500", "4", "0.018", "0.195", "0.088", "0.140"]
    figures_description:
      - "Figure 6 (Main): Side-by-side comparison of DIM vs CausalForest debiasing-hurts effect. Shows amplification increases with nonlinear estimator, especially at K=4."
    analysis: >
      Best-tier reviewers see CausalForest results as the strongest evidence for practical relevance.
      The 5.9× amplification headline number comes from this experiment and is the paper's most
      eye-catching finding. The RMSE tradeoff is disclosed in a dedicated 'Bias-RMSE Tradeoff'
      subsection — reviewers appreciate the transparency and note that at n≥500, the tradeoff
      largely resolves. The pattern consistency between DIM and CausalForest ('same direction,
      amplified magnitude') strengthens the theoretical claim that the bias identity captures a
      fundamental mechanism, not an estimator-specific artifact. Combined with exp-017 (R-learner
      replication), this establishes estimator-agnosticism as a validated property.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef0fbf34-ba35-44f5-a774-87b99cab6da5",
  "isSidechain": false,
  "requestId": "req_011CbL4Ucvu6FwMjYF5hVK8U",
  "type": "assistant",
  "uuid": "aabf7394-677f-4ca3-a4a4-1d7de036d3ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UvvJqkB61ggC9z2MAVYS7a",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 69,
      "cache_read_input_tokens": 41655,
      "output_tokens": 13362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 69,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13362,
          "cache_read_input_tokens": 41655,
          "cache_creation_input_tokens": 69,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 69
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reframed 'When Debiasing Hurts' narrative fully lands：reviewers认为 problem identification 本身是 EMNLP 级贡献，bias identity 的 exact 形式在 LLM annotation 语境下被接受为新颖，E…",
  "leafUuid": "aabf7394-677f-4ca3-a4a4-1d7de036d3ba",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Best-tier prediction: EC-HTE diagnostic at EMNLP",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reframed 'When Debiasing Hurts' narrative fully lands：reviewers认为 problem identification 本身是 EMNLP 级贡献，bias identity 的 exact 形式在 LLM annotation 语境下被接受为新颖，E…",
  "leafUuid": "aabf7394-677f-4ca3-a4a4-1d7de036d3ba",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Best-tier prediction: EC-HTE diagnostic at EMNLP",
  "sessionId": "d268f21e-aa46-498b-a290-5def6c522697"
}
```

---
