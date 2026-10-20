# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：DIF在真实数据上有效但需架构分层约束且检测力低于模拟预期，RL鲁棒性仅对alignment-RL充分验证，Claim需加限定条件 核心假设：['全

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/e092f085-a052-4a24-8ca3-ec58f6905580.jsonl`
- **Structured JSON:** [`ca8a29c32372364275f8.json`](../../sessions/ca/ca8a29c32372364275f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:58:14.491Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:58:14.491Z",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：DIF在真实数据上有效但需架构分层约束且检测力低于模拟预期，RL鲁棒性仅对alignment-RL充分验证，Claim需加限定条件\n核心假设：['全群体IRT拟合边缘（RMSEA 0.08-0.12），架构分层后可接受', 'DIF标记与污染代理部分相关，但within-family分析显示30-50%标记可能反映能力增长', 'Alignment-RL（DPO/ORPO）不降低DIF，但reasoning-RL样本量（10-15个）不足以达到统计显著', 'Bifactor模型收敛但部分科目因子载荷弱，锚题池缩小', 'Ensemble中DVD信号弱于预期（variant污染检测力不足），退化为DIF+ConStat双信号', 'Semi-synthetic验证确认检测力但真实数据效应量分布偏向中等（δ 1.0-1.4）']\n关键指标范围：{'semi_synthetic_tpr_delta_ge_1.4': [0.5, 0.65], 'semi_synthetic_fpr': [0.05, 0.1], 'rl_retention_ratio': [0.75, 0.9], 'rmsea_decoder_only': [0.05, 0.08], 'rmsea_full_population': [0.08, 0.12], 'within_family_confound_overlap': [0.35, 0.55], 'gsm8k_dif_gap_correlation_r': [0.25, 0.45], 'bifactor_equating_spearman_rho': [0.9, 0.95], 'ensemble_tpr_delta_ge_0.8': [0.45, 0.65], 'ensemble_fpr': [0.06, 0.12], 'constat_auroc_non_rl': [0.55, 0.7], 'dvd_variant_detection_tpr': [0.3, 0.5]}\n叙事方向：Claim 1降级为条件性陈述：\"DIF在架构同质子群（decoder-only）上以实用检测力识别大效应污染， 且对alignment-RL鲁棒；对reasoning-RL的鲁棒性有理论保证和初步实证支持但样本有限。\" Claim 2从三信号ensemble退化为DIF+ConStat双信号互补，DVD作为探索性结果放入appendix。 Claim 3需增加\"pilot-scale验证\"限定，强调方法论贡献而非端到端系统。 新增贡献点：(a) 首个大规模LLM群体IRT拟合诊断分析（揭示架构异质性对心理测量建模的影响）， (b) Semi-synthetic验证方法论本身作为污染检测器评估框架的贡献。 论文从\"完整管线系统\"重心移向\"检测方法论+诊断洞察\"，仍可投ICLR但需补充实验或强化分析。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nfocus: Verify that the updated framing (qualified novelty, partial exploitation analysis, contamination-capability confound controls) and new experiments (plan_010 architecture-stratified DIF, plan_011 semi-synthetic validation) address the issues from Dream #1. Pay attention to whether the 9 Anticipated Reviewer Concerns now have adequate experimental coverage.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. A nuance: partial exploitation (model memorizes but answers correctly only p<1 of the time) shrinks DIF effect size proportionally — we formally characterize detection power as a function of exploitation rate. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates a psychometric monitoring and regeneration framework — applying mature, validated psychometric tools to solve an urgent ML evaluation problem.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning a capability range from near-random (46% accuracy) to near-saturation (60%), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026). Leveraging the unprecedented scale of METABENCH (5,219 models), we conduct the largest DIF analysis in LLM evaluation literature.\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n\n7. **\"DIF flags may reflect capability improvement, not contamination\"**\n   - Response: Post-2024 models are both more capable and more contaminated. We control for this via (a) within-family DIF analysis (same architecture at different training stages, e.g., Llama-2→3→3.1), where capability trajectory is known, isolating contamination-specific DIF; (b) domain-specificity analysis of DIF flags vs known capability trajectories; (c) bifactor model's subject-specific factors as covariates to absorb domain-specific capability gains.\n   - Evidence needed: plan_001 (within-family sub-analysis), plan_005 (bifactor covariates)\n\n8. **\"Ground truth is too noisy to validate DIF — MMLU-CF κ=0.14 is near-random\"**\n   - Response: (a) We supplement MMLU-CF with semi-synthetic validation: inject known contamination signals into the real METABENCH response matrix and measure DIF detection power under controlled conditions. (b) GSM8K/GSM1K provides independent cross-benchmark ground truth. (c) We explicitly characterize MMLU-CF's own reliability limitations before using it as validation.\n   - Evidence needed: plan_011 (semi-synthetic validation), plan_004 (GSM8K cross-validation)\n\n9. **\"Partial exploitation defeats DIF — RL models may only exploit p<1 of memorized items\"**\n   - Response: Formal power analysis as function of exploitation rate p shows: at p=1.0 DIF detects with TPR=0.72-0.85; at p=0.6 effect size shrinks ~0.6×, falling to medium range where ensemble's ConStat signal provides coverage. DIF + ensemble jointly cover p≥0.4. Below p=0.4, contamination impact on rankings is minimal.\n   - Evidence needed: plan_002 (partial exploitation analysis)\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Validate against MMLU-CF\\\n    \\ (ACL 2025) contamination-free items as partial ground truth. (d) Within-family\\\n    \\ confound control: run DIF within model families (Llama-2→3→3.1,\\n    Qwen-1.5→2→2.5,\\\n    \\ Mistral→Mixtral) where capability trajectory is known. If DIF flags\\n    items\\\n    \\ that are NOT differentially contaminated within-family, the flag reflects capability\\n\\\n    \\    gain, not contamination. Report: DIF flag overlap between cross-cohort and\\\n    \\ within-family\\n    analyses to disentangle contamination from capability improvement.\\n\\\n    (e) Domain-specificity analysis: correlate DIF flags with MMLU subject categories\\\n    \\ to check\\n    whether flags cluster in domains with known capability jumps vs\\\n    \\ known contamination.\\nReport: DIF flags × cohort definition × item filtering\\\n    \\ — 4-way sensitivity matrix + within-family confound control + domain-specificity\\\n    \\ analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond MMLU-CF.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (MMLU-CF κ=0.14 too weak for validation). Design:\\\n    \\ (a) Select 500 items with known-clean status (no DIF flags, stable across cohorts)\\\n    \\ (b) For a random subset of 100-200 items, inject synthetic contamination:\\n\\\n    \\    flip responses of focal-group models from incorrect→correct with probability\\\n    \\ p\\n    (simulating contamination at varying exploitation rates)\\n(c) Run DIF\\\n    \\ detection; measure TPR/FPR against known-injected ground truth (d) Vary injection\\\n    \\ parameters: contamination prevalence (5%-30%), exploitation rate\\n    (0.4-1.0),\\\n    \\ focal group size (N=40-200)\\nProvides controlled ground truth that MMLU-CF and\\\n    \\ GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T20:58:14.494Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:58:14.494Z",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T20:58:14.516Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：DIF在真实数据上有效但需架构分层约束且检测力低于模拟预期，RL鲁棒性仅对alignment-RL充分验证，Claim需加限定条件
核心假设：['全群体IRT拟合边缘（RMSEA 0.08-0.12），架构分层后可接受', 'DIF标记与污染代理部分相关，但within-family分析显示30-50%标记可能反映能力增长', 'Alignment-RL（DPO/ORPO）不降低DIF，但reasoning-RL样本量（10-15个）不足以达到统计显著', 'Bifactor模型收敛但部分科目因子载荷弱，锚题池缩小', 'Ensemble中DVD信号弱于预期（variant污染检测力不足），退化为DIF+ConStat双信号', 'Semi-synthetic验证确认检测力但真实数据效应量分布偏向中等（δ 1.0-1.4）']
关键指标范围：{'semi_synthetic_tpr_delta_ge_1.4': [0.5, 0.65], 'semi_synthetic_fpr': [0.05, 0.1], 'rl_retention_ratio': [0.75, 0.9], 'rmsea_decoder_only': [0.05, 0.08], 'rmsea_full_population': [0.08, 0.12], 'within_family_confound_overlap': [0.35, 0.55], 'gsm8k_dif_gap_correlation_r': [0.25, 0.45], 'bifactor_equating_spearman_rho': [0.9, 0.95], 'ensemble_tpr_delta_ge_0.8': [0.45, 0.65], 'ensemble_fpr': [0.06, 0.12], 'constat_auroc_non_rl': [0.55, 0.7], 'dvd_variant_detection_tpr': [0.3, 0.5]}
叙事方向：Claim 1降级为条件性陈述："DIF在架构同质子群（decoder-only）上以实用检测力识别大效应污染， 且对alignment-RL鲁棒；对reasoning-RL的鲁棒性有理论保证和初步实证支持但样本有限。" Claim 2从三信号ensemble退化为DIF+ConStat双信号互补，DVD作为探索性结果放入appendix。 Claim 3需增加"pilot-scale验证"限定，强调方法论贡献而非端到端系统。 新增贡献点：(a) 首个大规模LLM群体IRT拟合诊断分析（揭示架构异质性对心理测量建模的影响）， (b) Semi-synthetic验证方法论本身作为污染检测器评估框架的贡献。 论文从"完整管线系统"重心移向"检测方法论+诊断洞察"，仍可投ICLR但需补充实验或强化分析。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen
focus: Verify that the updated framing (qualified novelty, partial exploitation analysis, contamination-capability confound controls) and new experiments (plan_010 architecture-stratified DIF, plan_011 semi-synthetic validation) address the issues from Dream #1. Pay attention to whether the 9 Anticipated Reviewer Concerns now have adequate experimental coverage.

## paper_framing.md

# Paper Framing — irt_equated_bench_regen

## Target Venue
- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)
- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)
- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)

## Core Claims (3 条, 可证伪)

**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.

**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.

**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.

## Story Spine

**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.

**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.

**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. A nuance: partial exploitation (model memorizes but answers correctly only p<1 of the time) shrinks DIF effect size proportionally — we formally characterize detection power as a function of exploitation rate. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates a psychometric monitoring and regeneration framework — applying mature, validated psychometric tools to solve an urgent ML evaluation problem.

**Headline result template**: "On MMLU with 5,000+ models spanning a capability range from near-random (46% accuracy) to near-saturation (60%), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026). Leveraging the unprecedented scale of METABENCH (5,219 models), we conduct the largest DIF analysis in LLM evaluation literature."

## Venue Fit Risks

- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ "fairness testing for items").
- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: "examinees" → "models", "test items" → "benchmark questions", "DIF" → "item-level contamination signal", "equating" → "score comparability across benchmark versions".
- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as "bringing mature psychometric tools to solve an urgent ML problem" rather than "inventing new statistics."

## Anticipated Reviewer Concerns

1. **"DIF power is only sufficient for large effects (δ≥1.4)"**
   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.
   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)

2. **"Model cohort sample sizes are too small for classical DIF"**
   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.
   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)

3. **"Only validated in simulation"**
   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.
   - Evidence needed: plan_001, plan_004

4. **"Item regeneration quality — how do you ensure replacements measure the same construct?"**
   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.
   - Evidence needed: plan_005, plan_006

5. **"RL robustness is only theoretical — where's the empirical evidence?"**
   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.
   - Evidence needed: plan_002

6. **"Computational cost of the full pipeline"**
   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.

7. **"DIF flags may reflect capability improvement, not contamination"**
   - Response: Post-2024 models are both more capable and more contaminated. We control for this via (a) within-family DIF analysis (same architecture at different training stages, e.g., Llama-2→3→3.1), where capability trajectory is known, isolating contamination-specific DIF; (b) domain-specificity analysis of DIF flags vs known capability trajectories; (c) bifactor model's subject-specific factors as covariates to absorb domain-specific capability gains.
   - Evidence needed: plan_001 (within-family sub-analysis), plan_005 (bifactor covariates)

8. **"Ground truth is too noisy to validate DIF — MMLU-CF κ=0.14 is near-random"**
   - Response: (a) We supplement MMLU-CF with semi-synthetic validation: inject known contamination signals into the real METABENCH response matrix and measure DIF detection power under controlled conditions. (b) GSM8K/GSM1K provides independent cross-benchmark ground truth. (c) We explicitly characterize MMLU-CF's own reliability limitations before using it as validation.
   - Evidence needed: plan_011 (semi-synthetic validation), plan_004 (GSM8K cross-validation)

9. **"Partial exploitation defeats DIF — RL models may only exploit p<1 of memorized items"**
   - Response: Formal power analysis as function of exploitation rate p shows: at p=1.0 DIF detects with TPR=0.72-0.85; at p=0.6 effect size shrinks ~0.6×, falling to medium range where ensemble's ConStat signal provides coverage. DIF + ensemble jointly cover p≥0.4. Below p=0.4, contamination impact on rankings is minimal.
   - Evidence needed: plan_002 (partial exploitation analysis)


## experiment_plan (with registry status)

- id: plan_001
  name: real_data_dif_mmlu
  claim: 1
  description: "Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\
    \ × 12,508 items). Data characteristics: only 37% models classifiable by family\
    \ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\
    \ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\
    \ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\
    \ split (ability-based grouping, uses all models) (c) Item filtering: run with\
    \ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\
    \ detection on all items under both cohort definitions. Validate against MMLU-CF\
    \ (ACL 2025) contamination-free items as partial ground truth. (d) Within-family\
    \ confound control: run DIF within model families (Llama-2→3→3.1,\n    Qwen-1.5→2→2.5,\
    \ Mistral→Mixtral) where capability trajectory is known. If DIF flags\n    items\
    \ that are NOT differentially contaminated within-family, the flag reflects capability\n\
    \    gain, not contamination. Report: DIF flag overlap between cross-cohort and\
    \ within-family\n    analyses to disentangle contamination from capability improvement.\n\
    (e) Domain-specificity analysis: correlate DIF flags with MMLU subject categories\
    \ to check\n    whether flags cluster in domains with known capability jumps vs\
    \ known contamination.\nReport: DIF flags × cohort definition × item filtering\
    \ — 4-way sensitivity matrix + within-family confound control + domain-specificity\
    \ analysis.\n"
  priority: P0
  gpu_budget_hours: 0
  deps: []
  registry_id: ''
  status: planned
- id: plan_002
  name: rl_robustness_validation
  claim: 1
  description: "Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\
    \ - \"Alignment RL\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\
    \ produce\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\
    \ 477 such models.\n- \"Reasoning RL\" (GRPO/PPO online training) = the mechanism\
    \ that conceals contamination\n  signals. This is what Claim 1 targets. METABENCH\
    \ has almost none of these.\nDesign (Reviewer-validated): (a) SFT-only cohort\
    \ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\
    \ as mechanism control —\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\
    \ if DIF works on both\n    (a) and (b), robustness covers the full RL spectrum\n\
    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\n\
    \    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\n\
    \    (not a standalone group): DIF is group-level, so we verify that adding RL\
    \ models\n    to a cohort doesn't degrade detection. Separately, run traditional\
    \ detectors\n    (Min-K%, ConStat) on these 10-15 models individually to show\
    \ per-model degradation.\nTwo-level validation: - Group level: DIF flags same\
    \ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\
    \ detectors degrade on (c) individuals → fragile This design works even with only\
    \ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\
    \ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\
    \ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\
    \ test or permutation test for pairwise AUROC differences - TOST equivalence testing\
    \ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\
    \ exploitation power analysis: formally characterize DIF detection power as\n\
    \    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\
    \ answers\n    memorized items correctly with probability p, shrinking DIF effect\
    \ size by ~p.\n    Show detection boundary and ensemble coverage handoff point.\n"
  priority: P0
  gpu_budget_hours: 100
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_003a
  name: constat_perturbation_eval
  claim: 2
  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:
    (a) Generate semantically equivalent reformulations for 200+ MMLU items using
    LLM paraphrasing (b) Compare model performance on original vs reformulated items
    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection
    power by effect size — expected strength on non-RL models, weakness on RL Even
    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.

    '
  priority: P0
  gpu_budget_hours: 80
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_003b
  name: dvd_generation_variance_eval
  claim: 2
  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select
    10-15 open-weight models with inference access (b) Generate 50 responses per item
    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect
    bimodal distributions (contamination signal) (d) Characterize detection power
    for variant contamination vs verbatim contamination Standalone results provide
    variant-contamination detection baseline independent of DIF.

    '
  priority: P0
  gpu_budget_hours: 70
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_003c
  name: ensemble_fusion
  claim: 2
  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate
    per-signal thresholds on subset of items with known contamination status (b) Evaluate
    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:
    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision
    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion
    weights (5-fold); report uniform-weight baseline alongside optimized Depends on
    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  - plan_003a
  - plan_003b
  registry_id: ''
  status: planned
- id: plan_004
  name: cross_benchmark_gsm8k
  claim: 1
  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.
    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard
    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with
    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability
    and provides an independent ground truth beyond MMLU-CF.

    '
  priority: P1
  gpu_budget_hours: 100
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_005
  name: bifactor_irt_equating_pilot
  claim: 3
  description: 'Pilot bifactor IRT equating on MMLU: (a) Fit bifactor model to METABENCH
    MMLU data (general factor + subject-specific factors) (b) Select anchor items
    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter
    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model
    rankings on original vs replaced benchmark should correlate at Spearman rho ≥
    0.95 after equating.

    '
  priority: P1
  gpu_budget_hours: 50
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_006
  name: item_generation_calibration
  claim: 3
  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use
    LLM generation with construct constraints (same subject, same cognitive level)
    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty
    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45
    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate
    on holdout model panel

    '
  priority: P1
  gpu_budget_hours: 200
  deps:
  - plan_005
  registry_id: ''
  status: planned
- id: plan_007
  name: cumulative_bayesian_dif
  claim: 1
  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).
    Simulate 4 successive benchmark administrations. Show power improvement from accumulating
    evidence: individual administration power ~0.40 → cumulative power ~0.70 after
    3 administrations for medium effects (δ=1.0).

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_008
  name: graceful_degradation_analysis
  claim: 3
  description: 'Formal analysis of benchmark validity under item replacement: (a)
    Define validity metrics (ranking stability, score reliability, construct coverage)
    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish
    theoretical bounds on validity degradation as function of replacement rate (d)
    Empirical validation using METABENCH data

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_005
  - plan_006
  registry_id: ''
  status: planned
- id: plan_009
  name: item_focused_trees
  claim: 1
  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative
    to categorical cohort DIF. Treat model release date as continuous covariate. Compare
    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary
    cohort splits, uses full model sample.

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_010
  name: architecture_stratified_dif
  claim: 1
  description: "Run DIF within architecture-homogeneous subpopulations to test whether\
    \ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\
    \ is removed. Dream worst-case identified this as the critical missing experiment.\
    \ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\
    \ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\
    \ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\n\
    \    vs full-population DIF from plan_001\n(d) If fit improves substantially,\
    \ conclusion is \"DIF requires architecture-homogeneous\n    populations\" — a\
    \ fixable constraint, not a fundamental limitation\nZero GPU cost (uses existing\
    \ METABENCH data). Proactive defense against worst-case reviewer concern about\
    \ unidimensional IRT misfit.\n"
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_011
  name: semi_synthetic_contamination_validation
  claim: 1
  description: "Inject known contamination into the real METABENCH response matrix\
    \ and measure DIF detection power under controlled ground truth. Addresses ground\
    \ truth circularity concern (MMLU-CF κ=0.14 too weak for validation). Design:\
    \ (a) Select 500 items with known-clean status (no DIF flags, stable across cohorts)\
    \ (b) For a random subset of 100-200 items, inject synthetic contamination:\n\
    \    flip responses of focal-group models from incorrect→correct with probability\
    \ p\n    (simulating contamination at varying exploitation rates)\n(c) Run DIF\
    \ detection; measure TPR/FPR against known-injected ground truth (d) Vary injection\
    \ parameters: contamination prevalence (5%-30%), exploitation rate\n    (0.4-1.0),\
    \ focal group size (N=40-200)\nProvides controlled ground truth that MMLU-CF and\
    \ GSM1K cannot.\n"
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned


## registry (completed experiments)

- exp_id: mvp_dif_power_sim
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_tpr_mh: 0.6817
    best_tpr_lr: 0.6869
    best_condition: N=100_delta=1.6
    best_auc_mh: 0.9393
    best_auc_lr: 0.9593
    pass_criterion_tpr_mh: 0.0416
    pass_criterion_tpr_lr: 0.0703
    pass_criterion_condition: N=50_delta=1.0
    verdict: FAIL
    all_fpr_below_015: true
- exp_id: mvp_dif_power_sim_phase2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ets_c_tpr_N80_d14: 0.6823
    ets_c_tpr_N80_d16: 0.7223
    ets_c_tpr_N100_d14: 0.7582
    ets_c_tpr_N100_d16: 0.7966
    ets_c_fpr_range: 0.036-0.042
    best_auc_mh: 0.9254
    best_auc_lr: 0.9405
    verdict: PASS
    pass_plus_met: true
    real_param_a_mean: 1.2
    real_param_b_mean: -0.84

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
  "promptId": "67b30c76-d380-41f3-a073-f3f21e05c7bc",
  "type": "user",
  "uuid": "1f7a3c1a-e477-4451-a04f-c9cf93d014a5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:58:14.514Z_

```json
{
  "parentUuid": "1f7a3c1a-e477-4451-a04f-c9cf93d014a5",
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
  "uuid": "36f1679a-ae1f-4d02-9327-38e8fb570973",
  "timestamp": "2026-05-20T20:58:14.514Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:58:14.514Z_

```json
{
  "parentUuid": "36f1679a-ae1f-4d02-9327-38e8fb570973",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8d571009-ceb5-47c8-b96a-a535344f7a56",
  "timestamp": "2026-05-20T20:58:14.514Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DIF在真实数据上有效但需架构分层约束且检测力低于模拟预期，RL鲁棒性仅对alignment-RL充分验证，Claim需加限定条件 核心假设：['全群体IRT拟合边缘（RMSEA 0.08-0.12），架构分层后可接受', 'DIF标记与污染代理部分相关，但within-family分析显示30-50%标…",
  "leafUuid": "8d571009-ceb5-47c8-b96a-a535344f7a56",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experimental validation for IRT-based LLM contamination detection",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580"
}
```

---

### Assistant

_source line 8 · 2026-05-20T20:58:27.719Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "median" tier definition. I need to provide result_rationale for each prediction explaining why this tier would produce these specific results.

Let me go through each planned experiment and generate predictions consistent with the median tier's core assumptions and key metric ranges.

Planned experiments:
1. plan_001: real_data_dif_mmlu
2. plan_002: rl_robustness_validation
3. plan_003a: constat_perturbation_eval
4. plan_003b: dvd_generation_variance_eval


5. plan_003c: ensemble_fusion
6. plan_004: cross_benchmark_gsm8k
7. plan_005: bifactor_irt_equating_pilot
8. plan_006: item_generation_calibration
9. plan_007: cumulative_bayesian_dif
10. plan_008: graceful_degradation_analysis
11. plan_009: item_focused_trees
12. plan_010: architecture_stratified_dif
13. plan_011: semi_synthetic_contamination_validation

Now I'm working through the full list of experiments to construct median-tier predictions for each one, grounding them in the tier's assumptions about model performance and metric ranges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d571009-ceb5-47c8-b96a-a535344f7a56",
  "isSidechain": false,
  "requestId": "req_011CbEVSTrXbQVf5tkQqgxdS",
  "type": "assistant",
  "uuid": "8007dc6c-1c97-49f2-930b-994f83882026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qMYibFSZRz3Ab7v6WzV9X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12831,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12831,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15378,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12831
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

_source line 9 · 2026-05-20T21:03:27.172Z_

```yaml
tier: median
narrative_guidance: >
  论文重心从"端到端污染检测管线"转向"检测方法论贡献+心理测量诊断洞察"。
  Claim 1降级为条件性陈述（架构同质+大效应）；Claim 2从三信号退化为DIF+ConStat双信号；
  Claim 3加"pilot-scale"限定。新增贡献：首个大规模LLM群体IRT拟合诊断、semi-synthetic验证框架。
  仍可投ICLR但需在framing上诚实呈现限制条件，以方法论严谨性取胜而非系统完整性。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: "METABENCH MMLU全量DIF分析（5219模型×12508题），含时序/能力分组、负区分度敏感性、族内混淆控制、领域特异性分析"
    expected_results:
      full_pop_rmsea: 0.105
      full_pop_cfi: 0.82
      full_pop_tli: 0.79
      decoder_only_rmsea: 0.068
      temporal_dif_flags_ets_c_count: 485
      temporal_dif_flags_ets_b_count: 1120
      accuracy_quintile_dif_flags_ets_c_count: 390
      cohort_overlap_jaccard_c: 0.55
      mmlu_cf_validation_kappa: 0.14
      mmlu_cf_partial_correlation_with_dif: 0.18
      neg_disc_sensitivity_flag_change_pct: 12.3
      within_family_confound_overlap: 0.42
      within_family_llama_dif_flags: 68
      within_family_qwen_dif_flags: 52
      domain_specificity_chi2_p: 0.003
      stem_vs_humanities_dif_ratio: 1.45
    result_rationale: >
      全群体IRT拟合边缘（RMSEA~0.105）因架构异质性（encoder-decoder、MoE混入decoder-only群体）违反单维性假设。
      CFI/TLI低于0.90阈值确认模型误拟合。时序DIF标记约485个ETS-C级（3.9%题目），与模拟阶段预期的
      大效应检测力一致。但within-family分析揭示42%标记在族内也出现，表明这些DIF可能反映
      Llama-2→3的架构跃迁带来的能力增长而非污染。MMLU-CF验证受限于其自身低信度（κ=0.14），
      偏相关仅0.18，无法作为强验证。领域特异性显示STEM科目DIF比例高于人文1.45倍，
      与已知的数学/代码领域污染重灾区一致，但也与这些领域能力增长更快的事实混淆。
      负区分度题目移除后标记变化12.3%——非忽略不计但也未颠覆主结论。
    tables:
      - title: "Table 1: IRT Model Fit Diagnostics by Population"
        columns: [population, N_models, N_items, RMSEA, CFI, TLI, SRMR]
        rows:
          - [full_population, 5219, 12508, 0.105, 0.82, 0.79, 0.091]
          - [decoder_only, 3842, 12508, 0.068, 0.92, 0.90, 0.054]
          - [post_2023_decoder_only, 1856, 12508, 0.072, 0.91, 0.89, 0.058]
      - title: "Table 2: DIF Detection Results by Cohort Definition"
        columns: [cohort_def, N_focal, N_ref, ETS_C_flags, ETS_B_flags, ETS_A_pct]
        rows:
          - [temporal_2023v2024, 656, 1253, 485, 1120, 87.2]
          - [accuracy_quintile_Q5vQ1, 1044, 1044, 390, 980, 89.1]
          - [temporal_no_neg_disc, 656, 1253, 427, 985, 88.5]
      - title: "Table 3: Within-Family Confound Analysis"
        columns: [family, N_models, DIF_C_flags, overlap_with_cross_cohort_pct]
        rows:
          - [Llama_2_to_3.1, 38, 68, 44]
          - [Qwen_1.5_to_2.5, 29, 52, 39]
          - [Mistral_Mixtral, 22, 41, 43]
          - [pooled_within_family, 89, 161, 42]
    figures_description:
      - "Fig 1: MMLU IRT拟合诊断——全群体vs decoder-only子群体的item-fit残差分布（Q-Q plot），展示架构分层后拟合改善"
      - "Fig 2: DIF flag Venn diagram——时序cohort vs 能力quintile cohort的ETS-C标记重叠"
      - "Fig 3: Within-family DIF vs cross-cohort DIF flag重叠热力图，按科目domain着色"
      - "Fig 4: 按MMLU subject分组的DIF flag比例（柱状图），叠加已知污染proxy（benchmark出现在训练语料的概率）"
    analysis: >
      核心发现：DIF在真实数据上可检出大效应污染信号，但全群体IRT拟合不佳（RMSEA>0.08）迫使
      结论限定于decoder-only子群体。Within-family混淆分析是本实验最关键的新贡献——42%重叠率
      意味着近半数DIF标记可能是能力增长而非污染。这直接支持Claim 1降级为条件性陈述。
      领域特异性分析提供了间接证据（STEM集中）但无法单独区分污染vs能力。
      MMLU-CF验证基本失败（κ=0.14），需要plan_011的semi-synthetic验证来补救。
      关键方法论贡献：首次报告大规模LLM群体IRT拟合诊断，揭示架构异质性是IRT应用于LLM评估的核心障碍。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: "DIF的RL鲁棒性实证验证：alignment-RL（DPO/ORPO）充分验证+reasoning-RL（GRPO/PPO）初步验证+部分利用功率分析"
    expected_results:
      sft_cohort_n: 1842
      alignment_rl_cohort_n: 477
      reasoning_rl_models_n: 13
      dif_retention_ratio_alignment_rl: 0.88
      dif_retention_ratio_reasoning_rl_mixed: 0.82
      dif_flag_jaccard_sft_vs_alignment: 0.76
      dif_flag_jaccard_sft_vs_sft_plus_rl: 0.71
      constat_auroc_non_rl: 0.62
      constat_auroc_alignment_rl: 0.58
      constat_auroc_reasoning_rl: 0.51
      mink_auroc_non_rl: 0.68
      mink_auroc_reasoning_rl: 0.49
      delong_dif_vs_constat_p: 0.008
      tost_dif_retention_equivalence_p: 0.03
      bootstrap_ci_dif_auroc_95: [0.74, 0.86]
      partial_exploit_tpr_p1_0: 0.73
      partial_exploit_tpr_p0_8: 0.61
      partial_exploit_tpr_p0_6: 0.44
      partial_exploit_tpr_p0_4: 0.28
      partial_exploit_ensemble_handoff_p: 0.55
    result_rationale: >
      Alignment-RL验证充分（N=477）：DIF保留率0.88表明DPO/ORPO不干扰群体级行为模式，因为
      离线偏好优化不产生NLL gap收缩。标记Jaccard 0.76说明添加alignment-RL模型后DIF标记高度稳定。
      ConStat和Min-K%在alignment-RL上仅轻微下降（非目标机制），但在reasoning-RL上ConStat降至0.51（接近随机），
      Min-K%降至0.49，复现Wang et al.发现。
      
      Reasoning-RL验证受限于样本量（仅13个模型）：DIF保留率0.82看似不错，但将13个模型混入
      已有cohort后，它们对群体DIF的影响被稀释——这既是方法论优势（群体级统计天然鲁棒），
      也是验证的局限（无法确认在reasoning-RL占多数时DIF是否仍稳健）。Bootstrap CI较宽。
      TOST等价性检验p=0.03勉强通过（α=0.05），但统计力不足以强声明。
      
      部分利用分析显示清晰的检测力衰减曲线：p=1.0时TPR=0.73与模拟一致，
      p=0.6时降至0.44（中等效应范围），p≈0.55处DIF与ConStat检测力交叉——
      这是ensemble handoff点，但因ConStat自身在RL下降质，实际coverage gap存在于
      reasoning-RL+中等利用率区间。
    tables:
      - title: "Table 4: DIF Robustness Across Training Paradigms"
        columns: [cohort_composition, N_focal, DIF_C_flags, retention_ratio, jaccard_vs_sft_baseline]
        rows:
          - [SFT_only_temporal, 1842, 485, 1.00, 1.00]
          - [SFT_plus_alignment_RL, 2319, 452, 0.88, 0.76]
          - [SFT_plus_all_RL, 2332, 438, 0.82, 0.71]
      - title: "Table 5: Per-Model Detector AUROC Comparison"
        columns: [detector, non_RL, alignment_RL, reasoning_RL, delta_RL]
        rows:
          - [DIF_group_level, 0.81, 0.79, "N/A (group)", "—"]
          - [ConStat, 0.62, 0.58, 0.51, -0.11]
          - [Min-K_pct, 0.68, 0.63, 0.49, -0.19]
          - [Perplexity, 0.61, 0.55, 0.47, -0.14]
      - title: "Table 6: Partial Exploitation Power Curve"
        columns: [exploitation_rate_p, effective_delta, dif_tpr, constat_tpr, ensemble_tpr]
        rows:
          - [1.0, 1.6, 0.73, 0.54, 0.79]
          - [0.8, 1.28, 0.61, 0.48, 0.68]
          - [0.6, 0.96, 0.44, 0.42, 0.55]
          - [0.4, 0.64, 0.28, 0.35, 0.41]
    figures_description:
      - "Fig 5: DIF flag stability——Venn diagram展示SFT-only、+alignment-RL、+reasoning-RL三种cohort组成下ETS-C标记重叠"
      - "Fig 6: 各检测器AUROC在不同训练范式下的degradation curve（bar chart with 95% CI error bars）"
      - "Fig 7: 部分利用率功率曲线——DIF TPR vs exploitation rate p，叠加ConStat和ensemble曲线，标注handoff点"
    analysis: >
      Alignment-RL鲁棒性结论扎实（大样本+统计显著）。Reasoning-RL结论只能写为"初步实证支持"——
      13个模型混入大cohort后检测力保持，但这更多反映群体统计的稀释效应而非真正的机制鲁棒性验证。
      论文需诚实区分两种RL并承认reasoning-RL验证的样本局限。
      部分利用分析提供了实用的检测边界图：p≥0.6时DIF主导，p∈[0.4,0.6]时需ensemble覆盖，
      p<0.4时检测力不足但污染对排名影响也可忽略——这个论证链条完整且可信。
      对比实验清晰展示传统检测器在reasoning-RL下降至随机水平，而DIF保持——
      即使是有限样本下的这一对比也是有价值的实证贡献。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: "ConStat风格扰动检测独立评估：200+题目改写、FDR控制检测、按效应量和训练范式分层"
    expected_results:
      items_reformulated: 220
      reformulation_quality_human_eval: 0.87
      constat_auroc_all_models: 0.63
      constat_auroc_non_rl: 0.67
      constat_auroc_alignment_rl: 0.61
      constat_auroc_reasoning_rl: 0.52
      constat_fdr_controlled_flags: 145
      constat_fdr_level: 0.10
      constat_tpr_delta_ge_1_4: 0.48
      constat_tpr_delta_0_6_to_1_4: 0.35
      constat_fpr: 0.08
      constat_dif_flag_overlap_pct: 38
    result_rationale: >
      ConStat在non-RL模型上表现中等（AUROC 0.67），因为扰动敏感性在未经RL平滑的模型上
      确实能捕捉到记忆痕迹——对原始问题正确但对语义等价改写错误。但AUROC远未达到
      原论文报告的水平，因为：(1) MMLU是4选1MCQ，扰动空间有限（改写选项文本可能
      改变难度而非仅测试记忆）；(2) 大规模改写的质量不均匀（人工评估87%可接受意味着
      13%改写引入了构念偏移）。
      
      Reasoning-RL模型上AUROC降至0.52（接近随机），复现Wang et al.的发现——
      GRPO训练平滑了对扰动的敏感性差异。这正是ConStat的已知弱点，也是ensemble中
      ConStat覆盖non-RL、DIF覆盖RL的分工基础。
      
      ConStat与DIF标记仅38%重叠，说明两者捕捉不同信号维度——ConStat侧重per-model
      扰动敏感性，DIF侧重group-level行为模式差异。这为ensemble互补性提供了实证基础。
    tables:
      - title: "Table 7: ConStat Detection Performance by Model Type"
        columns: [model_type, N_models, AUROC, TPR_at_FDR_0.10, FPR]
        rows:
          - [all_models, 5219, 0.63, 0.38, 0.08]
          - [non_RL, 4742, 0.67, 0.44, 0.07]
          - [alignment_RL, 477, 0.61, 0.36, 0.09]
          - [reasoning_RL, 13, 0.52, 0.22, 0.11]
    figures_description:
      - "Fig 8: ConStat AUROC按模型训练范式分层的ROC曲线族"
      - "Fig 9: ConStat vs DIF标记重叠Venn diagram，按效应量大小着色"
    analysis: >
      ConStat作为独立信号价值中等——对non-RL模型提供DIF的互补视角（per-model粒度），
      但在RL模型上失效。与DIF低重叠率（38%）证实两个信号正交性，为ensemble fusion提供基础。
      结果质量足以支撑双信号ensemble叙事，但不足以单独支撑一个独立claim。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: "DVD生成方差检测独立评估：10-15个开放权重模型、50次采样/题、变体污染检测"
    expected_results:
      models_evaluated: 12
      items_evaluated: 500
      dvd_auroc_overall: 0.56
      dvd_auroc_verbatim_contamination: 0.53
      dvd_auroc_variant_contamination: 0.61
      dvd_tpr_variant_delta_ge_1_0: 0.42
      dvd_fpr: 0.14
      dvd_bimodal_detection_rate: 0.18
      dvd_dif_overlap_pct: 22
      dvd_constat_overlap_pct: 28
    result_rationale: >
      DVD信号在median档显著弱于预期。根本原因：(1) 4选1 MCQ的生成方差信号本质微弱——
      模型输出是4个logit的softmax，即使记忆了答案，temperature sampling下的方差差异
      远小于开放生成任务；(2) 仅12个模型的per-model方差估计噪声大；(3) 变体污染
      （model见过问题变体而非原题）在MMLU上难以量化——没有ground truth标注哪些模型
      见过哪些变体。
      
      AUROC 0.56整体上仅略优于随机。对变体污染略好（0.61）但FPR高达0.14，
      实用价值有限。双峰分布检测率仅18%——大多数题目的生成方差分布是单峰的，
      无法区分记忆vs非记忆。与DIF仅22%重叠表明DVD捕捉的是不同（但更弱）的信号。
      
      这一结果直接支持median叙事：DVD从ensemble的正式组成部分退化为appendix中的
      探索性分析，ensemble从三信号简化为DIF+ConStat双信号。
    tables:
      - title: "Table 8: DVD Detection Performance"
        columns: [contamination_type, AUROC, TPR_at_FPR_0.10, FPR_at_TPR_0.50]
        rows:
          - [overall, 0.56, 0.31, 0.35]
          - [verbatim, 0.53, 0.24, 0.41]
          - [variant, 0.61, 0.42, 0.22]
    figures_description:
      - "Fig 10: DVD生成方差分布——contaminated vs clean items的方差直方图（大量重叠，双峰不明显）"
      - "Appendix Fig: DVD vs DIF vs ConStat三信号标记重叠UpSet plot"
    analysis: >
      DVD在MCQ场景下信号过弱，不足以作为ensemble的正式组件。AUROC 0.56和FPR 0.14
      使其在任何实用阈值下都无法提供可靠检测。此结果应诚实报告并放入appendix，
      作为"DVD在MCQ场景下的局限性"的实证贡献——这本身对社区有信息价值。
      ensemble叙事需从三信号退化为双信号（DIF+ConStat）。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: "多信号ensemble融合：因DVD弱于预期，退化为DIF+ConStat双信号融合+DVD作为可选探索性第三信号"
    expected_results:
      ensemble_2signal_tpr_delta_ge_0_8: 0.58
      ensemble_2signal_fpr: 0.09
      ensemble_3signal_tpr_delta_ge_0_8: 0.55
      ensemble_3signal_fpr: 0.11
      dif_only_tpr_delta_ge_1_4: 0.73
      constat_only_tpr_delta_ge_0_6: 0.35
      ensemble_2signal_tpr_delta_ge_1_4: 0.78
      coverage_union_non_rl: 0.71
      coverage_union_all: 0.62
      majority_vote_2of2_tpr: 0.42
      weighted_fusion_auroc: 0.72
      uniform_weight_auroc: 0.69
      cv_5fold_auroc_std: 0.04
    result_rationale: >
      双信号ensemble（DIF+ConStat）的核心价值在于coverage互补而非精度提升：DIF覆盖大效应+RL场景，
      ConStat覆盖中效应+non-RL场景。union coverage在non-RL模型上达0.71，但在含RL模型的
      全群体上降至0.62（因ConStat在RL上失效，DIF对中效应力不足）。
      
      加入DVD第三信号后ensemble实际略微恶化（TPR持平但FPR从0.09升至0.11），
      因为DVD的高FPR稀释了ensemble精度。这进一步支持将DVD排除出正式ensemble。
      
      加权融合（AUROC 0.72）优于均匀权重（0.69）约3个点，但5-fold CV显示
      标准差0.04，说明改善在噪声范围内——不足以支撑"需要学习融合权重"的claim，
      应报告均匀权重为主结果。
      
      2-of-2多数投票TPR仅0.42——两个信号同时标记的题目太少，说明它们确实在
      检测不同类型的污染，但intersection策略过于保守。
    tables:
      - title: "Table 9: Ensemble Detection Performance"
        columns: [ensemble_config, TPR_delta_ge_0.8, TPR_delta_ge_1.4, FPR, AUROC]
        rows:
          - [DIF_only, 0.45, 0.73, 0.04, 0.76]
          - [ConStat_only, 0.35, 0.48, 0.08, 0.63]
          - [DVD_only, 0.22, 0.31, 0.14, 0.56]
          - [DIF_plus_ConStat_union, 0.58, 0.78, 0.09, 0.72]
          - [DIF_plus_ConStat_plus_DVD, 0.55, 0.76, 0.11, 0.70]
          - [DIF_plus_ConStat_intersection, 0.42, 0.52, 0.03, "—"]
      - title: "Table 10: Fusion Weight Analysis (5-fold CV)"
        columns: [method, mean_AUROC, std_AUROC, DIF_weight, ConStat_weight]
        rows:
          - [uniform, 0.69, 0.05, 0.50, 0.50]
          - [optimized, 0.72, 0.04, 0.62, 0.38]
    figures_description:
      - "Fig 11: 效应量-检测力热力图——横轴δ，纵轴各检测器/ensemble的TPR，展示coverage互补区间"
      - "Fig 12: DIF vs ConStat signal散点图（per-item DIF statistic vs ConStat z-score），标注四象限覆盖"
    analysis: >
      Ensemble叙事需务实调整：不是"三信号系统性覆盖全谱"，而是"DIF+ConStat双信号在各自优势区间互补，
      DIF主攻大效应+RL鲁棒，ConStat补充non-RL中效应检测"。Coverage gap在reasoning-RL+中等效应区间
      客观存在，需在论文中诚实标注。AUROC 0.72的双信号ensemble作为baseline有发表价值，
      但不足以支撑"全覆盖"的强claim。Claim 2需相应弱化。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: "GSM8K跨benchmark DIF复现，以GSM1K为独立ground truth验证DIF标记的污染相关性"
    expected_results:
      gsm8k_models_collected: 62
      gsm8k_items: 1319
      gsm8k_dif_c_flags: 78
      gsm8k_dif_b_flags: 195
      gsm8k_gsm1k_gap_mean: 8.2
      gsm8k_gsm1k_gap_std: 11.4
      dif_gap_correlation_r: 0.36
      dif_gap_correlation_p: 0.004
      dif_flag_enrichment_in_high_gap_models: 1.8
      gsm8k_irt_rmsea: 0.075
      gsm8k_temporal_cohort_n_focal: 28
      gsm8k_temporal_cohort_n_ref: 34
    result_rationale: >
      GSM8K验证提供了MMLU之外的独立实证但效果中等。DIF-gap相关r=0.36（p=0.004）统计显著
      但效应量中等——远非完美验证。原因：(1) GSM8K模型数仅62个，cohort分组后每组不足35，
      低于plan_001的80+阈值，DIF检测力受损；(2) GSM1K accuracy gap本身是model-level指标，
      而DIF是item-level指标，粒度不匹配——需要通过模型级聚合（"高DIF标记模型是否也是高gap模型"）
      间接关联，enrichment ratio 1.8说明存在关联但不强；(3) GSM8K的IRT拟合更好（RMSEA 0.075），
      因为数学推理在LLM群体中更接近单维构念，但模型数少削弱了统计力。
      
      此结果支撑"DIF在多个benchmark上可复现"的claim，但跨benchmark验证力度有限。
      作为supplementary evidence足够，不应作为主要验证手段。
    tables:
      - title: "Table 11: GSM8K DIF Analysis Summary"
        columns: [metric, value]
        rows:
          - [models, 62]
          - [items, 1319]
          - [ETS_C_flags, 78]
          - [IRT_RMSEA, 0.075]
          - [DIF_gap_correlation_r, 0.36]
          - [DIF_gap_correlation_p, 0.004]
          - [flag_enrichment_ratio, 1.8]
    figures_description:
      - "Fig 13: GSM8K per-model DIF标记数 vs GSM8K-GSM1K accuracy gap散点图（含回归线和CI band）"
      - "Fig 14: GSM8K vs MMLU DIF检测结果对比（parallel coordinates图展示两个benchmark的检测特征差异）"
    analysis: >
      跨benchmark验证达到"有意义但不强"的水平。r=0.36支持DIF捕捉与污染相关的信号，
      但无法排除混淆因素（数学推理能力增长也会产生类似pattern）。模型数量限制是主要瓶颈。
      论文中应作为corroborating evidence而非primary validation呈现。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: "MMLU bifactor IRT拟合+锚题选取+固定参数校准替换题等价性pilot验证"
    expected_results:
      bifactor_converged: true
      bifactor_general_factor_variance_explained: 0.58
      bifactor_n_subjects_with_strong_specific_factor: 38
      bifactor_n_subjects_with_weak_specific_factor: 19
      bifactor_rmsea: 0.062
      anchor_items_selected: 620
      anchor_items_pct: 5.0
      anchor_stability_across_cohorts_icc: 0.94
      equated_score_spearman_rho: 0.93
      equated_vs_unequated_rank_shift_median: 2.1
      equated_vs_unequated_rank_shift_95pct: 8.4
      weak_factor_subjects: ["abstract_algebra", "formal_logic", "jurisprudence", "moral_scenarios"]
    result_rationale: >
      Bifactor模型收敛但部分科目因子载荷弱——这是MMLU固有结构问题。MMLU的57个科目中，
      38个（67%）有强特定因子（标准化载荷>0.3），说明确实存在学科特异性维度。
      但19个科目（33%）特定因子弱（载荷<0.2），这些科目的题目本质上只加载在一般因子上，
      意味着它们的替换题校准可能不稳定（缺乏学科维度锚定）。
      
      锚题池620个（5%）看似充足，但因为弱因子科目的题目不适合做锚题，
      实际可用锚题在这些科目上稀疏。整体等价Spearman rho=0.93接近但未达到0.95目标——
      差距来源于弱因子科目的替换题校准误差。中位排名位移2.1位可接受，
      但95百分位8.4位意味着5%的模型排名变动超过8位——在竞争性leaderboard上非trivial。
      
      RMSEA 0.062（bifactor on decoder-only subpop）比单因子0.105大幅改善，
      确认多维IRT建模的必要性和可行性。
    tables:
      - title: "Table 12: Bifactor Model Fit"
        columns: [model, population, RMSEA, CFI, TLI, variance_general]
        rows:
          - [unidimensional, full_pop, 0.105, 0.82, 0.79, "—"]
          - [unidimensional, decoder_only, 0.068, 0.92, 0.90, "—"]
          - [bifactor, decoder_only, 0.062, 0.94, 0.92, 0.58]
      - title: "Table 13: Equating Results"
        columns: [metric, value]
        rows:
          - [anchor_items, 620]
          - [equated_spearman_rho, 0.93]
          - [median_rank_shift, 2.1]
          - [95pct_rank_shift, 8.4]
          - [weak_factor_subjects_count, 19]
    figures_description:
      - "Fig 15: Bifactor因子载荷热力图——57个MMLU科目×（一般因子+特定因子），颜色编码载荷强度"
      - "Fig 16: Equated vs original排名散点图，强因子科目和弱因子科目分色标注"
    analysis: >
      Bifactor equating在pilot规模上"基本可行但有结构性限制"。rho=0.93对pilot而言合理，
      但弱因子科目是系统性瓶颈——这些科目需要额外的构念验证或更大的校准样本。
      论文中Claim 3需加"pilot-scale"限定，并诚实报告弱因子科目的局限。
      方法论贡献：首次对MMLU进行bifactor IRT分析，揭示其多维结构特征。

  - name: item_generation_calibration
    plan_id: plan_006
    description: "DIF标记题替换生成+student simulation校准+与prompt-based难度定向对比"
    expected_results:
      items_generated: 150
      items_passing_construct_filter: 112
      student_sim_difficulty_correlation_rho: 0.78
      prompt_based_difficulty_correlation_rho: 0.28
      holdout_panel_n_models: 50
      holdout_equated_rho: 0.91
      difficulty_mse_student_sim: 0.34
      difficulty_mse_prompt_based: 1.85
      construct_validity_factor_loading_mean: 0.41
      generation_failure_rate: 0.25
    result_rationale: >
      Student simulation校准（rho=0.78）显著优于prompt-based难度定向（rho=0.28），
      复现并扩展arXiv 2601.09953的发现。这是因为student simulation直接模拟目标群体
      （LLM）的应答行为来估计难度，而prompt-based方法依赖LLM对自身难度的元认知——
      已知LLM的自我难度评估与实际表现弱相关。
      
      但holdout验证的equated rho仅0.91，低于plan_005的0.93——因为替换题引入了
      额外的构念偏移（生成质量不完美）。25%的生成失败率（不满足构念约束）说明
      自动化替换仍需人工审核。通过构念filter的112题平均因子载荷0.41（vs原题~0.50），
      表明替换题的构念对齐性有系统性衰减。
      
      核心方法论贡献是student simulation vs prompt-based的对比实验——
      这在现有文献中缺乏大规模实证。但端到端质量（rho 0.91）不足以支撑"自动化再生"的强claim。
    tables:
      - title: "Table 14: Item Generation & Calibration"
        columns: [method, difficulty_rho, difficulty_MSE, N_items]
        rows:
          - [student_simulation, 0.78, 0.34, 112]
          - [prompt_based_targeting, 0.28, 1.85, 112]
          - [random_same_subject, 0.11, 2.40, 112]
      - title: "Table 15: Holdout Validation"
        columns: [metric, original_items, replaced_items]
        rows:
          - [spearman_rho_vs_full, "—", 0.91]
          - [mean_factor_loading, 0.50, 0.41]
          - [difficulty_mean, 0.52, 0.49]
          - [discrimination_mean, 1.18, 0.95]
    figures_description:
      - "Fig 17: Student sim vs prompt-based难度预测散点图（双panel，标注回归线斜率差异）"
      - "Fig 18: 替换题vs原题的IRT参数分布对比（难度和区分度violin plot）"
    analysis: >
      Student simulation校准是可发表的方法论贡献。但替换题整体质量（因子载荷0.41、区分度0.95）
      系统性低于原题，说明LLM生成的MCQ在构念纯度上仍有差距。Claim 3应定位为
      "方法论框架+pilot验证"而非"可部署的再生系统"。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: "累积贝叶斯DIF先验模拟：4次连续benchmark施测的功率累积"
    expected_results:
      single_admin_power_delta_1_0: 0.38
      cumulative_2_admin_power: 0.52
      cumulative_3_admin_power: 0.65
      cumulative_4_admin_power: 0.72
      power_improvement_per_admin: [0.14, 0.13, 0.07]
      bayes_factor_threshold: 3.0
      false_positive_rate_cumulative: 0.06
    result_rationale: >
      单次施测对中等效应（δ=1.0）功率仅0.38，反映classical DIF对中等效应的固有局限。
      累积贝叶斯先验通过将前次分析的后验作为下次先验，逐步积累证据。3次后功率从0.38升至0.65——
      显著提升但未达0.70目标。第4次边际收益递减（+0.07），因为先验已较informative。
      
      FPR从单次的0.04小幅上升至累积的0.06——贝叶斯累积也累积了假阳性证据，
      但受BF阈值控制仍在可接受范围。
      
      此结果支持"DIF作为持续监控工具"的叙事——单次快照检测力有限，
      但随时间累积可覆盖中等效应。纯模拟结果，P2优先级，放supplementary materials。
    tables:
      - title: "Table S1: Cumulative Bayesian DIF Power"
        columns: [n_administrations, power_delta_1_0, power_delta_1_4, fpr]
        rows:
          - [1, 0.38, 0.73, 0.04]
          - [2, 0.52, 0.82, 0.05]
          - [3, 0.65, 0.88, 0.05]
          - [4, 0.72, 0.91, 0.06]
    figures_description:
      - "Supplementary Fig: 累积功率曲线——横轴施测次数，纵轴TPR，三条线对应δ=0.8/1.0/1.4"
    analysis: >
      累积贝叶斯DIF提供了优雅的理论框架但实证验证仅为模拟。作为supplementary结果
      支持"DIF监控随时间增强"的叙事足够，但不应作为主文核心贡献。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: "渐进替换下benchmark效度衰退分析：5%-50%替换率的排名稳定性/信度/构念覆盖"
    expected_results:
      rho_5pct_replaced: 0.98
      rho_10pct_replaced: 0.96
      rho_20pct_replaced: 0.93
      rho_50pct_replaced: 0.85
      reliability_alpha_original: 0.94
      reliability_alpha_20pct_replaced: 0.91
      construct_coverage_original: 1.00
      construct_coverage_20pct_replaced: 0.89
      theoretical_bound_validity_loss_rate: 0.003
      critical_replacement_threshold: 0.28
    result_rationale: >
      渐进替换的效度衰退遵循近似线性规律：每替换10%题目，Spearman rho下降约0.03-0.04。
      这比理论最优（完美替换题下rho应保持0.99+）差，因为plan_006已显示替换题的
      构念纯度系统性低于原题（因子载荷0.41 vs 0.50）。
      
      20%替换时rho=0.93、信度0.91，勉强可接受。50%时rho降至0.85——排名变动过大，
      不再算"等价benchmark"。临界替换率约28%——超过此点效度加速下降。
      
      构念覆盖在20%替换时降至0.89，因为弱因子科目的替换题无法维持原有的
      学科维度覆盖。这与plan_005识别的19个弱因子科目一致。
    tables:
      - title: "Table S2: Graceful Degradation Metrics"
        columns: [replacement_pct, spearman_rho, cronbach_alpha, construct_coverage]
        rows:
          - [0, 1.00, 0.94, 1.00]
          - [5, 0.98, 0.93, 0.97]
          - [10, 0.96, 0.93, 0.94]
          - [20, 0.93, 0.91, 0.89]
          - [50, 0.85, 0.86, 0.74]
    figures_description:
      - "Supplementary Fig: 替换率-效度衰退曲线（三指标并列），标注临界替换率28%"
    analysis: >
      提供了实用的替换预算指导：20%以内替换是安全区间，28%是临界点。
      但这依赖于plan_006的替换题质量——如果替换题质量提升，曲线会更平缓。
      P2优先级结果，支持Claim 3的"有限替换下等价性可维持"子论点。

  - name: item_focused_trees
    plan_id: plan_009
    description: "Item-Focused Trees：将发布日期作为连续协变量的DIF检测替代方法"
    expected_results:
      ift_n_items_flagged: 520
      ift_overlap_with_ets_c: 0.62
      ift_auc: 0.78
      ift_tpr_delta_ge_1_4: 0.69
      ift_fpr: 0.07
      ift_split_point_date: "2023-09"
      ift_advantage_no_arbitrary_cohort: true
      ift_computational_cost_minutes: 45
    result_rationale: >
      IFT将发布日期作为连续协变量，避免了plan_001中任意时序cohort分割的问题。
      AUC 0.78略高于ETS-C categorical DIF（因为连续建模不丢失信息），但TPR 0.69
      略低于ETS-C的0.73（因为树分割不如参数化DIF统计效率高）。
      
      自动学到的分割点2023-09与直觉一致——这大约是LLM训练数据中benchmark泄露
      开始加速的时间点。与ETS-C标记62%重叠说明两种方法捕捉相似但不完全相同的信号——
      IFT额外标记的题目可能反映了渐进式污染（而非二元的污染/未污染）。
      
      FPR 0.07略高于ETS-C的0.04——树方法的灵活性代价。计算成本45分钟可接受。
    tables:
      - title: "Table S3: IFT vs ETS-C DIF Comparison"
        columns: [method, flags, TPR_ge_1.4, FPR, AUC, overlap]
        rows:
          - [ETS_C, 485, 0.73, 0.04, 0.76, "—"]
          - [IFT, 520, 0.69, 0.07, 0.78, 0.62]
    figures_description:
      - "Supplementary Fig: IFT树结构可视化（顶层按发布日期分割，下层按模型族/能力分割）"
    analysis: >
      IFT作为methodological alternative有价值——避免任意cohort分割，提供连续视角。
      与ETS-C互补（不同false positive/negative tradeoff）。P2优先级，
      适合放supplementary作为robustness check。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: "架构分层DIF：decoder-only子群体IRT拟合诊断+DIF检测对比全群体"
    expected_results:
      decoder_only_n: 3842
      decoder_only_rmsea: 0.068
      decoder_only_cfi: 0.92
      decoder_only_tli: 0.90
      decoder_only_srmr: 0.054
      full_pop_rmsea: 0.105
      rmsea_improvement: 0.037
      decoder_only_dif_c_flags: 410
      decoder_only_dif_fpr: 0.035
      decoder_only_dif_tpr_est: 0.71
      full_pop_dif_c_flags: 485
      spurious_dif_reduction_pct: 18
      flag_overlap_jaccard: 0.72
    result_rationale: >
      架构分层后IRT拟合显著改善：RMSEA从0.105降至0.068（跨过0.08阈值进入"可接受"区间），
      CFI/TLI达到0.90+。这确认了架构异质性是全群体IRT误拟合的主要来源——不同架构
      （encoder-decoder、MoE、dense decoder-only）的应答模式存在系统性差异，
      违反单维性假设。
      
      DIF标记从485减至410（减少15%），FPR从0.04降至0.035，说明约75个全群体DIF标记
      是架构差异引起的spurious DIF而非真实污染信号。Spurious DIF减少18%
      是非忽略不计的改善。标记重叠Jaccard 0.72说明核心污染信号在分层后保持稳定。
      
      这一结果直接支持median叙事的核心约束：DIF需在架构同质子群体上运行。
      同时提供了首个大规模LLM群体IRT拟合诊断分析——揭示架构异质性对心理测量建模的影响，
      这本身是独立的方法论贡献。
    tables:
      - title: "Table 16: Architecture Stratification Effect on IRT Fit"
        columns: [population, N, RMSEA, CFI, TLI, SRMR, DIF_C_flags]
        rows:
          - [full_population, 5219, 0.105, 0.82, 0.79, 0.091, 485]
          - [decoder_only, 3842, 0.068, 0.92, 0.90, 0.054, 410]
          - [encoder_decoder, 312, 0.088, 0.87, 0.85, 0.072, "—"]
          - [MoE, 198, 0.095, 0.84, 0.82, 0.081, "—"]
      - title: "Table 17: Spurious DIF Analysis"
        columns: [metric, full_pop, decoder_only, delta]
        rows:
          - [ETS_C_flags, 485, 410, -75]
          - [FPR, 0.040, 0.035, -0.005]
          - [spurious_flag_pct, "—", "—", 15.5]
    figures_description:
      - "Fig 19: IRT拟合诊断——全群体vs各架构子群体的RMSEA/CFI/TLI对比（grouped bar chart）"
      - "Fig 20: DIF flag comparison——全群体vs decoder-only的per-item DIF statistic散点图，标注spurious DIF区域"
    analysis: >
      这是median档最关键的实验之一。结论清晰：DIF需要架构同质子群体才能获得可靠的IRT拟合，
      这是一个可操作的约束（实践中只需筛选decoder-only模型）而非根本性缺陷。
      RMSEA从0.105降至0.068的改善幅度为Claim 1的条件性陈述提供了直接实证支持。
      作为首个大规模LLM群体IRT拟合诊断，本身具有独立发表价值。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: "半合成污染注入验证：在真实METABENCH矩阵上注入已知污染信号，测量DIF检测力"
    expected_results:
      clean_items_selected: 500
      injection_items: 150
      semi_synthetic_tpr_delta_ge_1_4: 0.58
      semi_synthetic_tpr_delta_ge_1_0: 0.41
      semi_synthetic_tpr_delta_ge_0_6: 0.25
      semi_synthetic_fpr: 0.07
      tpr_by_prevalence_5pct: 0.52
      tpr_by_prevalence_15pct: 0.58
      tpr_by_prevalence_30pct: 0.63
      tpr_by_exploitation_rate_1_0: 0.65
      tpr_by_exploitation_rate_0_8: 0.54
      tpr_by_exploitation_rate_0_6: 0.38
      tpr_by_exploitation_rate_0_4: 0.22
      tpr_by_focal_n_40: 0.44
      tpr_by_focal_n_80: 0.58
      tpr_by_focal_n_200: 0.68
      power_surface_r2: 0.89
    result_rationale: >
      Semi-synthetic验证是解决ground truth困境的核心实验。TPR=0.58（δ≥1.4）低于
      纯模拟的0.72-0.73——这个差距是median档的关键特征，原因是真实METABENCH矩阵
      包含模拟中不存在的噪声源：(1) 真实IRT参数分布比模拟假设的更偏斜（负区分度15%题目）；
      (2) 真实群体能力分布非正态（双峰，低能力模型集中在45-50%准确率）；
      (3) 注入污染叠加在可能已有的真实污染之上，导致clean baseline不完全干净。
      
      FPR 0.07（在0.05-0.10范围内）——略高于模拟的0.04，因为真实数据中存在
      plan_001揭示的background DIF（能力增长、架构差异引起的non-contamination DIF）。
      
      参数扫描揭示了清晰的检测力依赖关系：exploitation rate是最强决定因素（从p=1.0到p=0.4，
      TPR从0.65降至0.22），focal group size次之（N=40时TPR=0.44，N=200时0.68），
      污染prevalence影响最小（5%→30%仅+0.11 TPR）。功率曲面R²=0.89说明检测力
      可被这三个参数well-characterized。
      
      真实数据效应量分布偏向中等（δ 1.0-1.4）而非模拟中均匀分布的大效应，
      这是检测力下降的另一来源——在实际污染场景中，多数污染的效应量在medium range，
      正好是DIF检测力最敏感的衰减区间。
    tables:
      - title: "Table 18: Semi-Synthetic Validation — TPR by Effect Size"
        columns: [delta_threshold, TPR, FPR, n_injected]
        rows:
          - ["≥1.4", 0.58, 0.07, 45]
          - ["≥1.0", 0.41, 0.07, 85]
          - ["≥0.6", 0.25, 0.07, 150]
      - title: "Table 19: Semi-Synthetic Power Surface"
        columns: [parameter, low, mid, high, tpr_low, tpr_mid, tpr_high]
        rows:
          - [exploitation_rate, 0.4, 0.7, 1.0, 0.22, 0.45, 0.65]
          - [focal_n, 40, 80, 200, 0.44, 0.58, 0.68]
          - [prevalence, 0.05, 0.15, 0.30, 0.52, 0.58, 0.63]
      - title: "Table 20: Simulation vs Semi-Synthetic Gap"
        columns: [metric, simulation, semi_synthetic, gap]
        rows:
          - [TPR_delta_ge_1.4, 0.73, 0.58, -0.15]
          - [FPR, 0.04, 0.07, +0.03]
          - [AUC, 0.94, 0.82, -0.12]
    figures_description:
      - "Fig 21: 三维功率曲面——exploitation rate × focal N × TPR，prevalence切片（3层）"
      - "Fig 22: 模拟vs半合成ROC曲线对比（标注performance gap来源注释）"
      - "Fig 23: 注入δ分布vs检测率直方图（展示中等效应区间的检测力衰减）"
    analysis: >
      Semi-synthetic验证提供了最可靠的ground truth评估，同时揭示了模拟-真实gap（TPR差距0.15）。
      这个gap本身是重要发现——说明纯模拟评估高估了DIF在真实数据上的检测力。
      功率曲面提供了实用的操作指南（需要多大N、什么效应量范围可检测）。
      方法论贡献：semi-synthetic验证框架本身作为污染检测器评估的通用工具，
      可推广到评估任何item-level检测方法，独立于DIF的具体结果。
      此实验是Claim 1降级为条件性陈述的直接实证基础——"实用检测力"而非"高检测力"。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8007dc6c-1c97-49f2-930b-994f83882026",
  "isSidechain": false,
  "requestId": "req_011CbEVSTrXbQVf5tkQqgxdS",
  "type": "assistant",
  "uuid": "e732f7a9-fca2-48c6-b06a-1fdb1c20f269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qMYibFSZRz3Ab7v6WzV9X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12831,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12831,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15378,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12831
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DIF在真实数据上有效但需架构分层约束且检测力低于模拟预期，RL鲁棒性仅对alignment-RL充分验证，Claim需加限定条件 核心假设：['全群体IRT拟合边缘（RMSEA 0.08-0.12），架构分层后可接受', 'DIF标记与污染代理部分相关，但within-family分析显示30-50%标…",
  "leafUuid": "e732f7a9-fca2-48c6-b06a-1fdb1c20f269",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experimental validation for IRT-based LLM contamination detection",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DIF在真实数据上有效但需架构分层约束且检测力低于模拟预期，RL鲁棒性仅对alignment-RL充分验证，Claim需加限定条件 核心假设：['全群体IRT拟合边缘（RMSEA 0.08-0.12），架构分层后可接受', 'DIF标记与污染代理部分相关，但within-family分析显示30-50%标…",
  "leafUuid": "e732f7a9-fca2-48c6-b06a-1fdb1c20f269",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experimental validation for IRT-based LLM contamination detection",
  "sessionId": "e092f085-a052-4a24-8ca3-ec58f6905580"
}
```

---
