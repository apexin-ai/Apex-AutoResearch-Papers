# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：IRT假设在LLM群体上严重违反，DIF标记被能力-污染混淆主导，核心检测Claim不成立，需彻底reframe 核心假设：['即使架构分层后IRT拟

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/f643bdc4-2564-483d-b287-4dcc5775353a.jsonl`
- **Structured JSON:** [`e9b906ad57b400985406.json`](../../sessions/e9/e9b906ad57b400985406.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T21:03:29.718Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T21:03:29.718Z",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：IRT假设在LLM群体上严重违反，DIF标记被能力-污染混淆主导，核心检测Claim不成立，需彻底reframe\n核心假设：['即使架构分层后IRT拟合仍不可接受（RMSEA>0.10），LLM群体本质上违反局部独立性', 'Within-family分析显示>60%的DIF标记反映能力增长而非污染——因果归因不可靠', 'Semi-synthetic验证揭示：仅极大效应（δ≥2.0）可检测，因真实response pattern的噪声远超模拟', 'RL鲁棒性实证不可证伪——reasoning-RL模型太少，alignment-RL不是目标机制', 'Bifactor模型不收敛或锚题不足以支撑等值', 'GSM8K交叉验证相关性弱（r<0.25），DIF标记缺乏外部效度']\n关键指标范围：{'semi_synthetic_tpr_delta_ge_1.4': [0.3, 0.5], 'semi_synthetic_fpr': [0.1, 0.2], 'rl_retention_ratio': [0.6, 0.8], 'rmsea_decoder_only': [0.08, 0.15], 'rmsea_full_population': [0.12, 0.2], 'within_family_confound_overlap': [0.15, 0.35], 'gsm8k_dif_gap_correlation_r': [0.05, 0.25], 'bifactor_equating_spearman_rho': [0.8, 0.9], 'ensemble_tpr_delta_ge_0.8': [0.25, 0.45], 'ensemble_fpr': [0.1, 0.2], 'constat_auroc_non_rl': [0.45, 0.6], 'dvd_variant_detection_tpr': [0.15, 0.35]}\n叙事方向：核心检测Claim不成立，但不降级venue——reframe为以下angle之一： (1) \"心理测量诊断\"角度：LLM群体大规模IRT分析本身是贡献——揭示为什么经典心理测量工具 不能直接搬到LLM评估场景（架构异质性→维度违反，训练数据重叠→局部独立性违反）， 并给出\"LLM-adapted psychometrics\"的修正方向（架构分层+条件独立性松弛）。 (2) \"混淆分离框架\"角度：within-family + domain-specificity分析虽未成功分离污染与能力， 但建立了严格的方法论框架来量化这种混淆的程度——首次证明\"污染检测必须控制能力增长\" 这一被社区忽视的问题。DIF作为诊断工具（不是检测工具）仍有价值。 (3) \"Semi-synthetic评估基准\"角度：提出的受控注入验证方法论成为评估任何污染检测器的 ground-truth框架，填补MMLU-CF(κ=0.14)和GSM1K各自局限性留下的空白。 再生部分如bifactor不收敛则砍掉Claim 3，聚焦诊断+评估方法论，仍为ICLR级贡献。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nfocus: Verify that the updated framing (qualified novelty, partial exploitation analysis, contamination-capability confound controls) and new experiments (plan_010 architecture-stratified DIF, plan_011 semi-synthetic validation) address the issues from Dream #1. Pay attention to whether the 9 Anticipated Reviewer Concerns now have adequate experimental coverage.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. A nuance: partial exploitation (model memorizes but answers correctly only p<1 of the time) shrinks DIF effect size proportionally — we formally characterize detection power as a function of exploitation rate. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates a psychometric monitoring and regeneration framework — applying mature, validated psychometric tools to solve an urgent ML evaluation problem.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning a capability range from near-random (46% accuracy) to near-saturation (60%), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026). Leveraging the unprecedented scale of METABENCH (5,219 models), we conduct the largest DIF analysis in LLM evaluation literature.\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n\n7. **\"DIF flags may reflect capability improvement, not contamination\"**\n   - Response: Post-2024 models are both more capable and more contaminated. We control for this via (a) within-family DIF analysis (same architecture at different training stages, e.g., Llama-2→3→3.1), where capability trajectory is known, isolating contamination-specific DIF; (b) domain-specificity analysis of DIF flags vs known capability trajectories; (c) bifactor model's subject-specific factors as covariates to absorb domain-specific capability gains.\n   - Evidence needed: plan_001 (within-family sub-analysis), plan_005 (bifactor covariates)\n\n8. **\"Ground truth is too noisy to validate DIF — MMLU-CF κ=0.14 is near-random\"**\n   - Response: (a) We supplement MMLU-CF with semi-synthetic validation: inject known contamination signals into the real METABENCH response matrix and measure DIF detection power under controlled conditions. (b) GSM8K/GSM1K provides independent cross-benchmark ground truth. (c) We explicitly characterize MMLU-CF's own reliability limitations before using it as validation.\n   - Evidence needed: plan_011 (semi-synthetic validation), plan_004 (GSM8K cross-validation)\n\n9. **\"Partial exploitation defeats DIF — RL models may only exploit p<1 of memorized items\"**\n   - Response: Formal power analysis as function of exploitation rate p shows: at p=1.0 DIF detects with TPR=0.72-0.85; at p=0.6 effect size shrinks ~0.6×, falling to medium range where ensemble's ConStat signal provides coverage. DIF + ensemble jointly cover p≥0.4. Below p=0.4, contamination impact on rankings is minimal.\n   - Evidence needed: plan_002 (partial exploitation analysis)\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Validate against MMLU-CF\\\n    \\ (ACL 2025) contamination-free items as partial ground truth. (d) Within-family\\\n    \\ confound control: run DIF within model families (Llama-2→3→3.1,\\n    Qwen-1.5→2→2.5,\\\n    \\ Mistral→Mixtral) where capability trajectory is known. If DIF flags\\n    items\\\n    \\ that are NOT differentially contaminated within-family, the flag reflects capability\\n\\\n    \\    gain, not contamination. Report: DIF flag overlap between cross-cohort and\\\n    \\ within-family\\n    analyses to disentangle contamination from capability improvement.\\n\\\n    (e) Domain-specificity analysis: correlate DIF flags with MMLU subject categories\\\n    \\ to check\\n    whether flags cluster in domains with known capability jumps vs\\\n    \\ known contamination.\\nReport: DIF flags × cohort definition × item filtering\\\n    \\ — 4-way sensitivity matrix + within-family confound control + domain-specificity\\\n    \\ analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond MMLU-CF.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (MMLU-CF κ=0.14 too weak for validation). Design:\\\n    \\ (a) Select 500 items with known-clean status (no DIF flags, stable across cohorts)\\\n    \\ (b) For a random subset of 100-200 items, inject synthetic contamination:\\n\\\n    \\    flip responses of focal-group models from incorrect→correct with probability\\\n    \\ p\\n    (simulating contamination at varying exploitation rates)\\n(c) Run DIF\\\n    \\ detection; measure TPR/FPR against known-injected ground truth (d) Vary injection\\\n    \\ parameters: contamination prevalence (5%-30%), exploitation rate\\n    (0.4-1.0),\\\n    \\ focal group size (N=40-200)\\nProvides controlled ground truth that MMLU-CF and\\\n    \\ GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T21:03:29.721Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T21:03:29.721Z",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T21:03:29.742Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：IRT假设在LLM群体上严重违反，DIF标记被能力-污染混淆主导，核心检测Claim不成立，需彻底reframe
核心假设：['即使架构分层后IRT拟合仍不可接受（RMSEA>0.10），LLM群体本质上违反局部独立性', 'Within-family分析显示>60%的DIF标记反映能力增长而非污染——因果归因不可靠', 'Semi-synthetic验证揭示：仅极大效应（δ≥2.0）可检测，因真实response pattern的噪声远超模拟', 'RL鲁棒性实证不可证伪——reasoning-RL模型太少，alignment-RL不是目标机制', 'Bifactor模型不收敛或锚题不足以支撑等值', 'GSM8K交叉验证相关性弱（r<0.25），DIF标记缺乏外部效度']
关键指标范围：{'semi_synthetic_tpr_delta_ge_1.4': [0.3, 0.5], 'semi_synthetic_fpr': [0.1, 0.2], 'rl_retention_ratio': [0.6, 0.8], 'rmsea_decoder_only': [0.08, 0.15], 'rmsea_full_population': [0.12, 0.2], 'within_family_confound_overlap': [0.15, 0.35], 'gsm8k_dif_gap_correlation_r': [0.05, 0.25], 'bifactor_equating_spearman_rho': [0.8, 0.9], 'ensemble_tpr_delta_ge_0.8': [0.25, 0.45], 'ensemble_fpr': [0.1, 0.2], 'constat_auroc_non_rl': [0.45, 0.6], 'dvd_variant_detection_tpr': [0.15, 0.35]}
叙事方向：核心检测Claim不成立，但不降级venue——reframe为以下angle之一： (1) "心理测量诊断"角度：LLM群体大规模IRT分析本身是贡献——揭示为什么经典心理测量工具 不能直接搬到LLM评估场景（架构异质性→维度违反，训练数据重叠→局部独立性违反）， 并给出"LLM-adapted psychometrics"的修正方向（架构分层+条件独立性松弛）。 (2) "混淆分离框架"角度：within-family + domain-specificity分析虽未成功分离污染与能力， 但建立了严格的方法论框架来量化这种混淆的程度——首次证明"污染检测必须控制能力增长" 这一被社区忽视的问题。DIF作为诊断工具（不是检测工具）仍有价值。 (3) "Semi-synthetic评估基准"角度：提出的受控注入验证方法论成为评估任何污染检测器的 ground-truth框架，填补MMLU-CF(κ=0.14)和GSM1K各自局限性留下的空白。 再生部分如bifactor不收敛则砍掉Claim 3，聚焦诊断+评估方法论，仍为ICLR级贡献。

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
  "promptId": "aa18f34b-ec1d-4973-ba0b-c5d582fa05ba",
  "type": "user",
  "uuid": "e488d1bd-c27b-401e-baf8-153d40a3214b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T21:03:29.741Z_

```json
{
  "parentUuid": "e488d1bd-c27b-401e-baf8-153d40a3214b",
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
  "uuid": "30764662-ed04-4256-a7b5-5523f191957d",
  "timestamp": "2026-05-20T21:03:29.741Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T21:03:29.741Z_

```json
{
  "parentUuid": "30764662-ed04-4256-a7b5-5523f191957d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "adf000e1-c615-41bc-97f0-52e93c7e1479",
  "timestamp": "2026-05-20T21:03:29.741Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：IRT假设在LLM群体上严重违反，DIF标记被能力-污染混淆主导，核心检测Claim不成立，需彻底reframe 核心假设：['即使架构分层后IRT拟合仍不可接受（RMSEA>0.10），LLM群体本质上违反局部独立性', 'Within-family分析显示>60%的DIF标记反映能力增长而非污染——因果…",
  "leafUuid": "adf000e1-c615-41bc-97f0-52e93c7e1479",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Semi-synthetic and architecture-stratified validation for irt-bench contamination detection",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a"
}
```

---

### Assistant

_source line 8 · 2026-05-20T21:03:43.149Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed worst-tier predicted results for every "planned" experiment in the experiment_plan. I need to produce a single YAML block with the worst-tier framing, giving specific predicted metrics, rationales, tables, figures, and analysis for each experiment.

Let me go through each planned experiment and generate worst-case predictions based on the worst-tier definition provided.

The worst tier means:
- IRT assumptions severely violated on LLM populations
- DIF flags dominated by capability-contamination confounding
- Core detection claim doesn't hold
- Need to completely reframe

Key metric ranges for worst:


- semi_synthetic_tpr_delta_ge_1.4: [0.3, 0.5]
- semi_synthetic_fpr: [0.1, 0.2]
- rl_retention_ratio: [0.6, 0.8]
- rmsea_decoder_only: [0.08, 0.15]
- rmsea_full_population: [0.12, 0.2]
- within_family_confound_overlap: [0.15, 0.35]
- gsm8k_dif_gap_correlation_r: [0.05, 0.25]
- bifactor_equating_spearman_rho: [0.8, 0.95]

Now I'm mapping these metric ranges to each experiment and determining what worst-case values would look like for the specific analyses planned. Now I'm finishing the list of planned experiments, completing items six through thirteen, then moving on to construct the worst-case scenario predictions for each one.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adf000e1-c615-41bc-97f0-52e93c7e1479",
  "isSidechain": false,
  "requestId": "req_011CbEVqhYgaJpPbp4s1ff4S",
  "type": "assistant",
  "uuid": "28e29ba9-3c8f-4542-85e3-302f2e0dcc0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LnFHK67ZdWdJVQaeu8udi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12924,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15545,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15545,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12924
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

_source line 9 · 2026-05-20T21:08:28.471Z_

```yaml
tier: worst
narrative_guidance: >
  核心检测Claim不成立。IRT单维假设在LLM全群体上严重违反（RMSEA>0.12），架构分层后仅部分改善（RMSEA~0.10）。
  DIF标记与能力增长高度混淆——within-family分析显示>60%的标记在已知无差异污染的家族内也出现，
  因果归因不可靠。Semi-synthetic验证揭示检测power远低于simulation预期（TPR~0.40 at δ≥1.4），
  因真实response matrix的噪声结构（缺失模式、ceiling/floor效应、架构聚类）压制了信号。
  Reframe方向：放弃"DIF是污染检测器"的叙事，转向(1)心理测量诊断——首个大规模实证证据说明
  经典IRT为什么不能直接用于LLM评估，(2)混淆分离框架——量化污染与能力混淆程度的方法论贡献，
  (3)semi-synthetic评估基准——为任何污染检测器提供controlled ground truth。
  仍为ICLR级贡献，但claim从"我们能检测污染"变为"我们证明了为什么检测污染比社区认为的更难，并提供了正确的工具链"。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      对METABENCH MMLU全量数据（5,219模型×12,508题）运行DIF分析，
      含时间队列划分、能力五分位划分、负区分度过滤敏感性分析、
      within-family混淆控制、domain-specificity分析。
    expected_results:
      irt_2pl_rmsea_full_population: 0.14
      irt_2pl_cfi_full_population: 0.72
      irt_2pl_rmsea_filtered_no_neg_disc: 0.11
      temporal_cohort_dif_flags_ets_c_count: 1850
      temporal_cohort_dif_flags_ets_c_rate: 0.148
      quintile_cohort_dif_flags_ets_c_count: 2300
      quintile_cohort_dif_flags_ets_c_rate: 0.184
      dif_flag_overlap_temporal_vs_quintile: 0.41
      mmlu_cf_validation_precision: 0.18
      mmlu_cf_validation_recall: 0.34
      mmlu_cf_cohen_kappa_vs_dif: 0.07
      within_family_confound_overlap_llama: 0.68
      within_family_confound_overlap_qwen: 0.61
      within_family_confound_overlap_mistral: 0.55
      within_family_confound_overlap_avg: 0.62
      domain_specificity_chi2_p: 0.23
      negative_disc_item_dif_rate: 0.31
      filtered_vs_unfiltered_flag_jaccard: 0.63
    result_rationale: >
      RMSEA=0.14远超可接受阈值(0.08)，因LLM群体包含encoder-decoder、MoE、dense decoder-only等
      异质架构，violate单维IRT的局部独立性假设。15.4%负区分度项进一步拉高misfit。
      DIF检出率~15%看似合理，但within-family分析揭示致命问题：Llama-2→3→3.1系列中，
      68%的cross-cohort DIF flag在family内也被标记——这些family内不存在差异污染（同一训练pipeline），
      说明DIF捕获的主要是能力增长而非污染。Qwen和Mistral系列类似(61%/55%)。
      MMLU-CF验证极弱(κ=0.07)，因MMLU-CF自身标注一致性仅κ=0.14，无法作为可靠ground truth。
      Domain-specificity分析未发现DIF flag在已知污染域vs已知能力提升域之间的显著聚类差异(p=0.23)，
      混淆不可分离。两种cohort划分的flag overlap仅0.41，说明DIF结果对分组策略高度敏感。
    tables:
      - title: "Table 1: IRT Model Fit Diagnostics (Full Population)"
        columns: [metric, full_population, neg_disc_filtered, decoder_only_ref]
        rows:
          - [RMSEA, 0.14, 0.11, "see plan_010"]
          - [CFI, 0.72, 0.79, "see plan_010"]
          - [TLI, 0.69, 0.76, "see plan_010"]
          - [SRMR, 0.09, 0.07, "see plan_010"]
      - title: "Table 2: DIF Detection Summary by Cohort Definition"
        columns: [cohort_type, n_ref, n_focal, dif_flags, flag_rate, "overlap_w_other"]
        rows:
          - [temporal_2023v2024, 1253, 656, 1850, 0.148, 0.41]
          - [quintile_Q1vQ5, 1044, 1044, 2300, 0.184, 0.41]
      - title: "Table 3: Within-Family Confound Analysis"
        columns: [family, n_models, cross_cohort_flags, within_family_flags, overlap_rate]
        rows:
          - [Llama-2/3/3.1, 47, 312, 213, 0.68]
          - [Qwen-1.5/2/2.5, 38, 289, 176, 0.61]
          - [Mistral/Mixtral, 29, 198, 109, 0.55]
          - [weighted_avg, 114, "—", "—", 0.62]
    figures_description:
      - "Fig 1: RMSEA violin plot across 57 MMLU subjects showing severe heterogeneity (range 0.06-0.22)"
      - "Fig 2: DIF flag overlap heatmap — temporal vs quintile vs within-family，显示三种划分标记高度不一致"
      - "Fig 3: Within-family DIF flag与cross-cohort DIF flag的Venn diagram，62%重叠区域标注为'能力-污染不可分'"
      - "Fig 4: Domain-specificity scatter — DIF flag rate per subject vs known contamination proxy, r=0.11"
    analysis: >
      IRT模型拟合灾难性失败(RMSEA=0.14)是worst档的核心信号。这不是技术问题而是理论问题——
      LLM群体的架构异质性使单维能力假设不成立。Within-family confound overlap 62%是致命发现：
      如果Llama-2→3的DIF flag中2/3在已知无差异污染的升级路径中也出现，
      那么DIF本质上在测量"模型变好了"而非"模型被污染了"。
      MMLU-CF验证完全失败(κ=0.07)，但这可归因于MMLU-CF自身质量而非DIF——
      这为reframe提供了空间：MMLU-CF不适合做ground truth，需要semi-synthetic方法(plan_011)。
      叙事转向：这些结果本身就是重要的负面发现——首次大规模实证证明DIF在LLM场景下的失效模式。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      验证DIF对RL训练的鲁棒性。含SFT基线队列、alignment-RL队列(DPO/ORPO)、
      reasoning-RL队列(GRPO/PPO 10-15模型)的DIF分析，以及partial exploitation power分析。
    expected_results:
      dif_flag_retention_sft_vs_alignrl: 0.82
      dif_flag_retention_sft_vs_reasonrl_mixed: 0.71
      rl_retention_ratio: 0.71
      constat_auroc_sft: 0.73
      constat_auroc_align_rl: 0.61
      constat_auroc_reason_rl: 0.48
      mink_auroc_sft: 0.68
      mink_auroc_reason_rl: 0.44
      dif_auroc_sft_cohort: 0.62
      dif_auroc_alignrl_cohort: 0.58
      dif_auroc_reasonrl_mixed_cohort: 0.55
      delong_dif_vs_constat_p: 0.31
      tost_equivalence_p: 0.18
      partial_exploit_tpr_p1_0: 0.42
      partial_exploit_tpr_p0_8: 0.33
      partial_exploit_tpr_p0_6: 0.24
      partial_exploit_tpr_p0_4: 0.15
      partial_exploit_ensemble_coverage_p0_6: 0.38
      bootstrap_ci_dif_auroc_95: [0.48, 0.62]
      n_reasoning_rl_models_available: 12
    result_rationale: >
      DIF retention ratio 0.71表面上看"还行"，但置于worst语境下：(1)基线DIF AUROC本身就只有0.62
      （因plan_001揭示的IRT misfit和confound问题），所以0.71的retention是在一个已经很弱的基线上，
      实际AUROC≈0.55，接近随机。(2)仅12个reasoning-RL模型可用，统计power极低，
      bootstrap CI宽达[0.48,0.62]，跨过0.5随机线。(3)TOST等价性检验p=0.18>0.05，
      无法声称DIF与ConStat"等效"——也无法声称DIF"更好"。DeLong检验p=0.31说明差异不显著，
      但这是因为两者都很差而非两者都好。(4)Partial exploitation分析是worst档最具破坏性的发现：
      真实response matrix噪声下，即使p=1.0的full exploitation，TPR也只有0.42（远低于simulation的0.72），
      p=0.6时降至0.24。Ensemble在p=0.6时也仅0.38。结论：RL鲁棒性名义上成立（DIF不像ConStat
      那样急剧下降），但在一个本身就不work的检测器上谈鲁棒性毫无意义。
    tables:
      - title: "Table 4: DIF vs Traditional Detectors Across RL Types"
        columns: [detector, sft_auroc, align_rl_auroc, reason_rl_auroc, retention_ratio]
        rows:
          - [DIF_ETS_C, 0.62, 0.58, 0.55, 0.71]
          - [ConStat, 0.73, 0.61, 0.48, 0.66]
          - [Min-K%, 0.68, 0.55, 0.44, 0.65]
          - [Min-K%++, 0.71, 0.59, 0.46, 0.65]
      - title: "Table 5: Partial Exploitation Power Curve"
        columns: [exploitation_rate_p, dif_tpr, dif_fpr, ensemble_tpr, ensemble_fpr]
        rows:
          - [1.0, 0.42, 0.14, 0.48, 0.16]
          - [0.8, 0.33, 0.13, 0.41, 0.15]
          - [0.6, 0.24, 0.12, 0.38, 0.14]
          - [0.4, 0.15, 0.11, 0.28, 0.13]
    figures_description:
      - "Fig 5: AUROC bootstrap distribution (1000 resamples) for DIF on reasoning-RL mixed cohort, 95% CI跨过0.5"
      - "Fig 6: Partial exploitation power curve — TPR vs exploitation rate p, 叠加simulation预测(虚线)与real-data结果(实线)的巨大gap"
      - "Fig 7: DeLong test pairwise比较矩阵——所有detector pair差异均不显著，因为都在chance附近"
    analysis: >
      RL鲁棒性论证在worst档下变成了一个pyrrhic victory：DIF确实比ConStat/Min-K%更稳定，
      但稳定在一个接近随机的水平。根本原因是plan_001的IRT misfit传导——
      如果item parameters估计不准（因为模型异质性违反假设），那么DIF统计量本身就是噪声的。
      Reasoning-RL模型数量(N=12)不足以做统计推断，这一点在worst档下无法弥补。
      Partial exploitation分析的simulation-to-real gap（0.72→0.42 at p=1.0）是关键发现——
      说明real response matrix的噪声结构（非随机缺失、ceiling效应、架构聚类）远比i.i.d. simulation假设的恶劣。
      Reframe价值：这个gap本身就是方法论贡献——量化了simulation与现实的差距，为未来work设定了realistic expectations。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      独立评估ConStat式perturbation testing在MMLU上的检测力，
      含200+题的语义等价改写、原始vs改写性能比较、FDR控制检测。
    expected_results:
      constat_auroc_non_rl: 0.54
      constat_auroc_sft_only: 0.62
      constat_auroc_rl_models: 0.43
      constat_fdr_controlled_tpr_alpha_0_05: 0.28
      constat_fdr_controlled_tpr_alpha_0_10: 0.36
      perturbation_quality_semantic_sim: 0.87
      perturbation_quality_human_eval: 0.79
      n_items_reformulated: 220
      reformulation_difficulty_shift_mean: 0.35
      reformulation_difficulty_shift_std: 0.41
      constat_detection_by_effect_size_small: 0.12
      constat_detection_by_effect_size_medium: 0.31
      constat_detection_by_effect_size_large: 0.52
    result_rationale: >
      ConStat在non-RL模型上AUROC=0.54，远低于原论文报告水平。原因：(1)perturbation本身引入
      非平凡的难度偏移(mean=0.35 logit, std=0.41)——语义等价的改写不是心理测量等价的改写，
      contamination-free的项也会表现出原始vs改写差异。(2)MMLU的multiple-choice格式使
      perturbation空间受限——改写选项措辞几乎不可避免地改变干扰项吸引力。(3)在RL模型上
      AUROC=0.43<0.5，说明RL训练导致的output distribution平滑使perturbation sensitivity
      方向反转——RL模型对改写更稳定（不是因为不污染，而是因为GRPO clipping压制了敏感性变化）。
      FDR控制后TPR仅0.28(α=0.05)，大量真阳性在多重检验校正中被消除。
      Worst档结论：ConStat作为standalone检测器在MMLU场景下不可靠。
    tables:
      - title: "Table 6: ConStat Detection Power by Model Type"
        columns: [model_type, n_models, auroc, fdr_tpr_0_05, fdr_tpr_0_10]
        rows:
          - [SFT-only, 85, 0.62, 0.34, 0.42]
          - [Align-RL(DPO/ORPO), 65, 0.51, 0.22, 0.31]
          - [Reason-RL(GRPO), 12, 0.43, 0.15, 0.24]
          - [All, 162, 0.54, 0.28, 0.36]
      - title: "Table 7: Perturbation Quality Assessment"
        columns: [metric, mean, std, min, max]
        rows:
          - [semantic_similarity, 0.87, 0.06, 0.71, 0.97]
          - [difficulty_shift_logit, 0.35, 0.41, -0.52, 1.83]
          - [distractor_attractiveness_change, 0.22, 0.31, -0.18, 1.12]
    figures_description:
      - "Fig 8: ConStat AUROC by model type的bar chart with error bars，RL模型显著低于SFT"
      - "Fig 9: Perturbation difficulty shift distribution——长尾分布说明'语义等价≠心理测量等价'"
    analysis: >
      ConStat失败的核心原因是perturbation-difficulty confound：改写不可避免地改变题目难度，
      而这与contamination signal混淆。在worst档下这不意外——原ConStat论文在controlled setting
      下work，但MMLU的选择题格式放大了perturbation artifact。RL AUROC<0.5说明信号反转，
      不是ConStat的fault而是RL训练机制的必然结果。
      Reframe价值：这些结果量化了perturbation-based方法的fundamental limitation，
      为"为什么需要新方法"提供了实证论据。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      独立评估DVD generation variance在MMLU上的检测力，
      含10-15个开源模型、每题50次temperature采样、方差分析。
    expected_results:
      dvd_variant_detection_tpr: 0.23
      dvd_verbatim_detection_tpr: 0.31
      dvd_fpr: 0.14
      dvd_auroc_overall: 0.58
      n_models_evaluated: 13
      n_items_evaluated: 500
      generation_variance_contaminated_mean: 0.34
      generation_variance_clean_mean: 0.29
      generation_variance_overlap_coefficient: 0.72
      bimodal_detection_rate_contaminated: 0.18
      bimodal_detection_rate_clean: 0.11
      gpu_hours_used: 62
    result_rationale: >
      DVD在worst档下表现差，原因：(1)MMLU是选择题——模型输出方差本身就很低（输出空间只有A/B/C/D），
      generation variance的区分力受限于这个compressed output space。(2)Contaminated vs clean项
      的方差分布高度重叠(overlap=0.72)——污染项不一定方差低（模型可能memorize了错误答案pattern），
      clean项不一定方差高（能力足够的模型在easy项上也方差低）。(3)Bimodal detection在两类项上
      差异不大(0.18 vs 0.11)，信噪比不足。(4)Multiple-choice格式下temperature采样的多样性
      被logit差异主导而非memorization——高confidence的非污染回答也呈现低方差。
      DVD更适合open-ended generation场景，在MCQ上fundamental limitation明显。
    tables:
      - title: "Table 8: DVD Detection Power"
        columns: [contamination_type, tpr, fpr, auroc, n_items]
        rows:
          - [verbatim, 0.31, 0.14, 0.62, 150]
          - [variant, 0.23, 0.14, 0.56, 150]
          - [overall, 0.27, 0.14, 0.58, 300]
      - title: "Table 9: Generation Variance Distribution"
        columns: [item_status, variance_mean, variance_std, bimodal_rate]
        rows:
          - [contaminated, 0.34, 0.18, 0.18]
          - [clean, 0.29, 0.16, 0.11]
          - [effect_size_d, 0.30, "—", "—"]
    figures_description:
      - "Fig 10: Generation variance kernel density plot — contaminated vs clean distributions几乎完全重叠"
      - "Fig 11: Per-model DVD AUROC scatter, 大多数模型在0.5-0.65之间，无clear separation"
    analysis: >
      DVD在MCQ场景下的failure是structural的——output space太小，variance信号被compressed。
      Effect size d=0.30属于small effect，在N=13模型×500题的规模下不足以支撑检测。
      Reframe价值：这是MCQ format的fundamental limitation的实证证明，
      推动社区思考format-aware的检测方法设计。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      将DIF+ConStat+DVD融合为多信号集成，含阈值校准、投票策略、覆盖分析。
    expected_results:
      ensemble_tpr_delta_ge_0_8: 0.38
      ensemble_tpr_delta_ge_1_4: 0.48
      ensemble_fpr: 0.16
      majority_vote_tpr: 0.32
      majority_vote_fpr: 0.11
      weighted_fusion_tpr: 0.43
      weighted_fusion_fpr: 0.16
      uniform_weight_tpr: 0.39
      uniform_weight_fpr: 0.14
      cross_val_weight_stability_cv: 0.35
      dif_unique_contribution: 0.08
      constat_unique_contribution: 0.11
      dvd_unique_contribution: 0.05
      signal_correlation_dif_constat: 0.22
      signal_correlation_dif_dvd: 0.14
      signal_correlation_constat_dvd: 0.18
    result_rationale: >
      三个弱检测器的ensemble不会产生强检测器——这是worst档的核心推论。
      (1)每个信号AUROC都在0.54-0.62范围，信号间相关性低(0.14-0.22)看似有利于ensemble，
      但低相关性在这里反映的是"各自捕获不同的噪声"而非"各自捕获不同的信号"。
      (2)Weighted fusion优于majority vote(0.43 vs 0.32 TPR)，但FPR也更高(0.16 vs 0.11)。
      Cross-validation显示权重不稳定(CV=0.35)，说明过拟合风险高。
      (3)Ensemble TPR@δ≥1.4仅0.48——即使是大效应也有超过一半漏检。FPR=0.16意味着
      每6个flag中有1个是误报，在12,508题的MMLU上产生~2000个false alarm。
      (4)各信号unique contribution很小(5-11%)，说明重叠区域不是"强化"而是"共同噪声"。
    tables:
      - title: "Table 10: Ensemble Fusion Strategy Comparison"
        columns: [strategy, tpr_delta_ge_0_8, tpr_delta_ge_1_4, fpr, f1]
        rows:
          - [DIF_only, 0.28, 0.42, 0.14, 0.33]
          - [ConStat_only, 0.31, 0.36, 0.12, 0.34]
          - [DVD_only, 0.20, 0.27, 0.14, 0.24]
          - [majority_2of3, 0.32, 0.40, 0.11, 0.37]
          - [weighted_fusion, 0.43, 0.48, 0.16, 0.40]
          - [uniform_weight, 0.39, 0.45, 0.14, 0.39]
      - title: "Table 11: Signal Correlation Matrix"
        columns: [signal_pair, pearson_r, overlap_flags]
        rows:
          - [DIF-ConStat, 0.22, 0.28]
          - [DIF-DVD, 0.14, 0.19]
          - [ConStat-DVD, 0.18, 0.23]
    figures_description:
      - "Fig 12: Ensemble TPR-FPR trade-off curve — 所有operating point的FPR>0.10或TPR<0.40"
      - "Fig 13: Venn diagram of signal coverage — 三信号union比any single signal仅提升~15%"
      - "Fig 14: Cross-validation weight stability — 5 fold间权重波动大，DIF权重从0.25到0.55"
    analysis: >
      Ensemble未能rescue单信号的weakness。"互补覆盖"的叙事在worst档下不成立——
      三个信号各自太弱，合并后仍太弱。但信号独立性分析(低相关)有方法论价值：
      它说明DIF/ConStat/DVD确实capture不同的contamination facets，
      只是每个facet上的power都不足。
      Reframe：ensemble框架作为evaluation protocol有贡献——未来更强的单信号检测器
      可以插入这个框架获得覆盖分析。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      在GSM8K上复制DIF分析，用GSM1K作为独立ground truth。
      收集50+模型的per-item response，做temporal cohort DIF，
      将DIF flag与per-model GSM8K-GSM1K accuracy gap关联。
    expected_results:
      gsm8k_dif_flag_rate: 0.11
      gsm8k_gsm1k_gap_mean: 0.062
      gsm8k_gsm1k_gap_std: 0.078
      gsm8k_dif_gap_correlation_r: 0.14
      gsm8k_dif_gap_correlation_p: 0.32
      gsm8k_irt_rmsea: 0.10
      n_models_collected: 58
      n_gsm8k_items: 1319
      dif_tpr_against_gsm1k_proxy: 0.22
      dif_fpr_against_gsm1k_proxy: 0.09
    result_rationale: >
      GSM8K交叉验证产出极弱相关(r=0.14, p=0.32)，原因：(1)GSM8K→GSM1K accuracy gap
      是model-level指标，DIF flag是item-level指标，两者度量不同granularity的contamination，
      对齐需要强假设（污染是均匀的across items）。(2)GSM8K的math reasoning性质使能力增长
      与contamination更难分离——新模型genuinely更擅长数学，gap可能反映的是eval methodology差异
      而非contamination。(3)GSM8K仅1,319题，N=58模型，统计power不足。(4)IRT fit在GSM8K上
      好于MMLU(RMSEA=0.10)因为数学题更unidimensional，但仍在边界区间。
      DIF在GSM1K proxy ground truth上的TPR=0.22极低，说明DIF flag与已知ground truth不对齐。
    tables:
      - title: "Table 12: GSM8K Cross-Validation Results"
        columns: [metric, value, ci_95_lower, ci_95_upper]
        rows:
          - [dif_gap_correlation_r, 0.14, -0.12, 0.38]
          - [dif_tpr_vs_gsm1k, 0.22, 0.10, 0.36]
          - [dif_fpr_vs_gsm1k, 0.09, 0.04, 0.16]
          - [irt_rmsea, 0.10, 0.08, 0.12]
    figures_description:
      - "Fig 15: Scatter plot — model-level DIF flag count vs GSM8K-GSM1K gap, r=0.14, CI跨零"
      - "Fig 16: GSM8K item-level DIF flags与GSM1K-defined contamination status的confusion matrix"
    analysis: >
      GSM8K验证失败彻底——r=0.14的95% CI包含零，无统计显著性。
      这削弱了DIF作为跨benchmark通用检测器的claim。但分析揭示了一个有用的insight：
      model-level gap与item-level DIF的granularity mismatch是根本问题，
      未来验证需要item-level ground truth（指向plan_011 semi-synthetic方法的必要性）。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      在METABENCH MMLU上拟合bifactor IRT模型（通用因子+学科因子），
      选锚题，做固定参数校准，验证等值分数等效性。
    expected_results:
      bifactor_convergence: false
      bifactor_convergence_subset_n_subjects: 8
      bifactor_rmsea_subset: 0.09
      bifactor_general_factor_variance_explained: 0.38
      bifactor_subject_factor_variance_explained: 0.31
      bifactor_residual_variance: 0.31
      anchor_item_count: 145
      anchor_item_stability_criterion_met_rate: 0.12
      equated_score_spearman_rho: 0.84
      equated_vs_original_rank_displacement_mean: 23
      equated_vs_original_rank_displacement_max: 312
      fixed_param_calibration_convergence_rate: 0.71
    result_rationale: >
      Bifactor模型在完整57学科上不收敛——这是worst档的defining prediction。原因：
      (1)12,508题×5,219模型的response matrix过于稀疏（many models没做完全部MMLU），
      bifactor需要估计的参数量(2×12508 + 57个学科因子loading)远超有效sample size。
      (2)学科因子间不正交——STEM学科高度相关，humanities学科高度相关，违反bifactor的
      近似正交假设。(3)通用因子仅解释38%方差——LLM能力高度multidimensional，
      单一g-factor模型不适用。退而求其次在8个大学科子集上可以收敛(RMSEA=0.09)，
      但这意味着跨学科等值不可行。锚题仅145个（<1.2%的题），稳定性达标率仅12%——
      大多数"稳定"题在不同cohort下参数也在漂移，因为IRT参数估计本身就不稳定。
      Spearman ρ=0.84看似可接受但低于0.95目标，且mean rank displacement=23意味着
      约5%的模型排名变动超过1个百分位——对leaderboard而言不可接受。
    tables:
      - title: "Table 13: Bifactor Model Fit"
        columns: [scope, convergence, rmsea, gen_var, subj_var, resid_var]
        rows:
          - [full_57_subjects, No, "—", "—", "—", "—"]
          - [subset_8_subjects, Yes, 0.09, 0.38, 0.31, 0.31]
          - [subset_4_stem, Yes, 0.07, 0.44, 0.28, 0.28]
      - title: "Table 14: Equating Quality"
        columns: [metric, value, target, met]
        rows:
          - [anchor_items, 145, ">500", No]
          - [anchor_stability_rate, 0.12, ">0.80", No]
          - [spearman_rho, 0.84, ">0.95", No]
          - [rank_displacement_mean, 23, "<5", No]
          - [fixed_param_convergence, 0.71, ">0.90", No]
    figures_description:
      - "Fig 17: Bifactor通用因子loading heatmap across subjects——STEM vs humanities清晰的两个cluster而非单一维度"
      - "Fig 18: 锚题stability across temporal cohorts——仅12%满足strict stability criterion"
      - "Fig 19: Equated vs original ranking scatter plot, ρ=0.84, 多个outlier偏离对角线"
    analysis: >
      Bifactor不收敛直接否定Claim 3。子集上的勉强收敛不足以支撑full-scale regeneration。
      核心问题是LLM能力的multidimensionality——38%通用因子方差说明超过60%的variance是
      domain-specific或residual的，单一等值框架不适用。
      但这个负面结果本身有价值：它是首个大规模实证证据说明bifactor IRT在LLM评估中的失效模式。
      Reframe：砍掉Claim 3，或将其降格为"在homogeneous subdomain内可行的局部等值"。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      为DIF-flagged MMLU题生成替代项，用student simulation校准难度，
      比较prompt-based vs empirical calibration。
    expected_results:
      n_items_generated: 300
      prompt_difficulty_correlation_rho: 0.21
      student_sim_difficulty_correlation_rho: 0.58
      student_sim_discrimination_correlation_rho: 0.41
      construct_validity_factor_loading_mean: 0.52
      construct_validity_factor_loading_target: 0.70
      replacement_item_acceptance_rate: 0.34
      difficulty_rmse_vs_original: 1.12
      discrimination_rmse_vs_original: 0.48
    result_rationale: >
      Prompt-based difficulty targeting一如文献预期地差(ρ=0.21)。Student simulation
      改善显著(ρ=0.58)但仍低于文献报告的0.75-0.82——因为MMLU的多学科异质性使得
      单一student simulation模型难以同时校准STEM和humanities。
      Construct validity是biggest failure：生成项的平均factor loading=0.52 vs 目标0.70，
      说明LLM生成的替代题虽然表面上在同一学科、同一认知水平，但测量的实际construct有偏移。
      仅34%的生成项满足acceptance criteria（难度、区分度、factor loading全部达标），
      意味着要替换100个flagged题需要生成~300个candidate——成本和质量控制问题突出。
    tables:
      - title: "Table 15: Item Generation Calibration Quality"
        columns: [calibration_method, difficulty_rho, discrimination_rho, construct_loading]
        rows:
          - [prompt_based, 0.21, 0.14, 0.48]
          - [student_simulation, 0.58, 0.41, 0.52]
          - [target, ">0.75", ">0.60", ">0.70"]
    figures_description:
      - "Fig 20: Generated vs original item difficulty scatter — student sim ρ=0.58, 大量离散"
      - "Fig 21: Factor loading distribution of generated items vs originals — 左移明显"
    analysis: >
      Item generation在worst档下quality insufficient for regeneration。
      Student simulation的partial success (ρ=0.58)相比prompt-based (ρ=0.21)是有意义的improvement，
      但距离psychometrically equivalent replacement还有大gap。
      Reframe：student simulation方法论贡献仍在，但regeneration pipeline需要更多研发。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      实现累积Bayesian DIF prior (Sinharay et al., 2006)，
      模拟4次连续benchmark administration，展示累积power改善。
    expected_results:
      single_admin_power_medium_delta_1_0: 0.22
      cumulative_2_admin_power: 0.31
      cumulative_3_admin_power: 0.39
      cumulative_4_admin_power: 0.45
      simulation_single_admin_power: 0.40
      power_improvement_factor_4_admin: 2.05
      bayes_factor_threshold_sensitivity: "BF>3 at 4th admin for 45% of truly contaminated items"
    result_rationale: >
      起点power=0.22（非simulation的0.40）——因为base DIF检测power在real data上已经degraded
      （plan_001的发现传导到这里）。累积后达到0.45——2x improvement看似decent，但绝对水平
      仍不足以做可靠检测。原因：Bayesian prior accumulation假设item parameters在administrations
      间是stable的，但LLM evaluation的"administrations"是不同时期的模型群体，
      item parameters本身可能在drift（因为新模型能力profile不同）。Prior可能在accumulate
      过时信息而非strengthen信号。
    tables:
      - title: "Table 16: Cumulative Bayesian DIF Power"
        columns: [n_administrations, power_real, power_simulation, ratio]
        rows:
          - [1, 0.22, 0.40, 0.55]
          - [2, 0.31, 0.54, 0.57]
          - [3, 0.39, 0.64, 0.61]
          - [4, 0.45, 0.70, 0.64]
    figures_description:
      - "Fig 22: Cumulative power curve — real vs simulation, gap不收敛反而expanding"
    analysis: >
      Bayesian accumulation帮助但不足以rescue。Simulation-to-real gap从0.55扩大到0.64
      说明累积过程在amplify real data的systematic bias。方法论仍有价值但需要加入
      item parameter drift correction。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      分析benchmark在不同替换率下的validity退化：排名稳定性、分数信度、construct覆盖。
    expected_results:
      ranking_stability_5pct_replace: 0.96
      ranking_stability_10pct_replace: 0.91
      ranking_stability_20pct_replace: 0.82
      ranking_stability_50pct_replace: 0.63
      score_reliability_5pct: 0.94
      score_reliability_10pct: 0.89
      score_reliability_20pct: 0.78
      score_reliability_50pct: 0.55
      construct_coverage_20pct: 0.85
      construct_coverage_50pct: 0.61
      acceptable_replacement_threshold: "5-10%"
    result_rationale: >
      在worst档下，替换项质量低(plan_006的factor loading=0.52)导致退化速度快于理论预期。
      10%替换时ranking stability=0.91，低于通常acceptable的0.95——因为替换项不仅改变难度
      还改变construct coverage。20%替换时信度降至0.78，50%时本质上是一个不同的test。
      可接受阈值仅5-10%，意味着如果DIF flags 15%的题为contaminated，
      即使全部替换也只有勉强够用。但如果contamination更广泛，regeneration不可行。
    tables:
      - title: "Table 17: Graceful Degradation Curves"
        columns: [replace_rate, rank_stability, score_reliability, construct_coverage]
        rows:
          - [0.05, 0.96, 0.94, 0.97]
          - [0.10, 0.91, 0.89, 0.93]
          - [0.20, 0.82, 0.78, 0.85]
          - [0.50, 0.63, 0.55, 0.61]
    figures_description:
      - "Fig 23: Degradation curves — 三条线（rank/reliability/coverage）在20%处都crossing below acceptable thresholds"
    analysis: >
      Degradation analysis在worst档下更像一个cautionary tale：它量化了low-quality replacement
      的代价，为"为什么item generation需要更好的calibration"提供实证。
      独立贡献是degradation framework本身——可用于任何benchmark regeneration方案的evaluation。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      实现Item-Focused Trees (Tutz & Berger, 2016)作为categorical cohort DIF的替代，
      将模型release date作为连续协变量。
    expected_results:
      ift_auroc: 0.57
      ift_vs_categorical_dif_flag_overlap: 0.48
      ift_tpr_delta_ge_1_4: 0.39
      ift_fpr: 0.12
      ift_rmsea_improvement: 0.01
      ift_tree_depth_mean: 2.3
      ift_overfitting_cv_gap: 0.09
    result_rationale: >
      IFT避免了arbitrary cohort划分，理论上更flexible。但worst档下：
      (1)AUROC=0.57仅marginal improvement over categorical DIF(~0.55)——因为底层IRT misfit
      不是cohort定义的问题，而是模型异质性的问题，IFT不能修复这个。
      (2)与categorical DIF的flag overlap仅0.48——两种方法不同意一半的flag，
      说明DIF结果fundamentally unstable，不取决于"真正的contamination"而取决于方法选择。
      (3)Overfitting gap=0.09说明tree在capture noise而非signal。
    tables:
      - title: "Table 18: IFT vs Categorical DIF Comparison"
        columns: [method, auroc, tpr_delta_ge_1_4, fpr, flag_count]
        rows:
          - [categorical_temporal, 0.55, 0.42, 0.14, 1850]
          - [categorical_quintile, 0.53, 0.38, 0.16, 2300]
          - [item_focused_tree, 0.57, 0.39, 0.12, 1620]
    figures_description:
      - "Fig 24: IFT split points visualization — release date splits不在intuitive boundaries (e.g., GPT-4 release)"
      - "Fig 25: IFT vs categorical flag agreement heatmap — 大面积disagreement"
    analysis: >
      IFT不能rescue DIF——问题在上游(IRT假设违反)，不在cohort定义。
      但IFT vs categorical的disagreement是有用的diagnostic：
      它量化了DIF结果对分析选择的敏感性，支撑"DIF不适合做检测器"的conclusion。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      在decoder-only同质子群体上运行DIF，测试IRT拟合是否改善、spurious DIF是否减少。
    expected_results:
      decoder_only_n_models: 3420
      decoder_only_rmsea: 0.10
      decoder_only_cfi: 0.82
      decoder_only_tli: 0.79
      full_pop_rmsea_ref: 0.14
      rmsea_improvement: 0.04
      dif_flag_rate_decoder_only: 0.12
      dif_flag_rate_full_pop_ref: 0.148
      fpr_decoder_only: 0.11
      fpr_full_pop_ref: 0.14
      tpr_decoder_only_delta_ge_1_4: 0.45
      within_family_confound_overlap_decoder_only: 0.55
      moe_vs_dense_subanalysis_rmsea_dense: 0.08
      moe_vs_dense_subanalysis_rmsea_moe: 0.12
    result_rationale: >
      Architecture stratification帮助但不够——这是worst档的关键特征。
      RMSEA从0.14降到0.10：improvement是real的(Δ=0.04)但0.10仍在borderline-to-poor区间
      (acceptable threshold是0.08)。原因：decoder-only内部仍有substantial heterogeneity——
      MoE vs dense, 不同parameter scales (1B-70B), 不同tokenizer, 不同training data。
      去除architecture heterogeneity是necessary but not sufficient。
      DIF flag rate降低(0.12 vs 0.148)和FPR降低(0.11 vs 0.14)说明部分spurious DIF
      确实来自architecture差异，但幅度有限。Within-family confound overlap从0.62降到0.55——
      仍然>50%的flag是confounded。Dense-only进一步分析(RMSEA=0.08)暗示如果进一步
      subset到完全homogeneous群体，fit会acceptable——但代价是N大幅缩小，power更低。
    tables:
      - title: "Table 19: Architecture Stratification Effect"
        columns: [population, n_models, rmsea, cfi, dif_flag_rate, fpr, within_fam_overlap]
        rows:
          - [full_population, 5219, 0.14, 0.72, 0.148, 0.14, 0.62]
          - [decoder_only, 3420, 0.10, 0.82, 0.120, 0.11, 0.55]
          - [decoder_dense_only, 1850, 0.08, 0.88, 0.098, 0.08, 0.47]
          - [decoder_moe_only, 380, 0.12, 0.78, 0.135, 0.13, 0.58]
      - title: "Table 20: Fit Diagnostic Breakdown"
        columns: [subgroup, rmsea, n, effective_power_at_d_1_4]
        rows:
          - [all_decoder, 0.10, 3420, 0.45]
          - [dense_small_1B_7B, 0.07, 1200, 0.38]
          - [dense_large_13B_70B, 0.09, 650, 0.42]
          - [moe_all, 0.12, 380, 0.30]
    figures_description:
      - "Fig 26: RMSEA by population subset — 递减但需要极细分才能到acceptable"
      - "Fig 27: Within-family confound overlap随population homogeneity的变化——缓慢下降但不消失"
      - "Fig 28: Power-fit tradeoff — 更homogeneous→更好fit但更少model→更低power"
    analysis: >
      Plan_010是worst档最有价值的实验——它精确量化了IRT misfit的来源和修复成本。
      结论："DIF要work需要architecture-homogeneous populations"是一个actionable finding，
      但代价是严重的power loss。这直接支撑reframe angle (1)——
      "为什么经典心理测量不能直接用于LLM"的诊断性贡献。
      Dense-only RMSEA=0.08是一个hope signal，但N=1850+within-family overlap=0.47
      说明即使在最favorable condition下confounding仍是dominant problem。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: >
      在真实METABENCH response matrix中注入已知contamination，
      测量DIF检测power under controlled ground truth。
    expected_results:
      semi_synthetic_tpr_delta_ge_1_4: 0.41
      semi_synthetic_tpr_delta_ge_1_0: 0.28
      semi_synthetic_tpr_delta_ge_0_6: 0.15
      semi_synthetic_fpr: 0.14
      prevalence_5pct_tpr: 0.48
      prevalence_15pct_tpr: 0.39
      prevalence_30pct_tpr: 0.33
      exploit_rate_1_0_tpr: 0.41
      exploit_rate_0_8_tpr: 0.33
      exploit_rate_0_6_tpr: 0.24
      exploit_rate_0_4_tpr: 0.14
      focal_n_40_tpr: 0.29
      focal_n_100_tpr: 0.41
      focal_n_200_tpr: 0.47
      simulation_vs_semi_synthetic_gap_tpr: 0.31
      simulation_tpr_reference_delta_1_4: 0.72
    result_rationale: >
      Semi-synthetic验证是worst档的smoking gun。TPR@δ≥1.4=0.41，远低于pure simulation的0.72。
      Gap=0.31(0.72-0.41)量化了simulation与现实的差距。原因清晰：
      (1)真实response matrix有non-random missing pattern——不是所有模型都做了全部题，
      missingness与model capability相关，biases IRT parameter estimation。
      (2)Ceiling/floor效应——easy题上所有模型都对，hard题上所有模型都错，
      这些题的DIF无法检测（因为没有ability-conditional variation）。
      (3)Architecture clustering——同family模型response pattern高度相关，
      violate DIF的independent observations假设。
      (4)Injection本身可能"太干净"——real contamination不是uniform probability flip，
      而是pattern-dependent（模型倾向于memorize特定类型的题），
      但这个bias direction使semi-synthetic结果成为optimistic estimate。
      Prevalence依赖反直觉(5%>15%>30%)——因为高prevalence时injected signal淹没在
      baseline noise中，DIF的focal-reference contrast被稀释。
      FPR=0.14>>0.05目标，因为real matrix中的existing contamination
      （我们不知道的ground truth）产生false positive contamination。
    tables:
      - title: "Table 21: Semi-Synthetic Detection Power Matrix"
        columns: [delta, prevalence, exploit_rate, tpr, fpr, auroc]
        rows:
          - [1.4, 0.15, 1.0, 0.41, 0.14, 0.68]
          - [1.4, 0.15, 0.6, 0.24, 0.13, 0.59]
          - [1.0, 0.15, 1.0, 0.28, 0.14, 0.60]
          - [1.0, 0.15, 0.6, 0.17, 0.13, 0.54]
          - [0.6, 0.15, 1.0, 0.15, 0.14, 0.52]
      - title: "Table 22: Simulation vs Semi-Synthetic Gap"
        columns: [condition, sim_tpr, semi_syn_tpr, gap, gap_pct]
        rows:
          - [N100_d1.4_p1.0, 0.72, 0.41, 0.31, "43%"]
          - [N100_d1.0_p1.0, 0.52, 0.28, 0.24, "46%"]
          - [N80_d1.4_p1.0, 0.68, 0.38, 0.30, "44%"]
      - title: "Table 23: Focal Group Size Effect"
        columns: [focal_n, tpr_d1_4, fpr, power_gain_per_10_models]
        rows:
          - [40, 0.29, 0.15, "—"]
          - [60, 0.34, 0.14, 0.025]
          - [80, 0.38, 0.14, 0.020]
          - [100, 0.41, 0.14, 0.015]
          - [200, 0.47, 0.13, 0.006]
    figures_description:
      - "Fig 29: TPR heatmap — delta × exploitation rate, 仅右上角(δ≥2.0, p≥0.8)达到TPR>0.50"
      - "Fig 30: Simulation vs semi-synthetic power curve overlay — persistent ~40% gap across all conditions"
      - "Fig 31: FPR decomposition — 0.14中约0.05来自statistical noise, 0.09来自uncontrolled existing contamination"
      - "Fig 32: Prevalence paradox — TPR随prevalence增加而下降的机制图"
    analysis: >
      Plan_011是worst档的cornerstone experiment。它做了三件事：
      (1)Definitively证明simulation结果不能translate to real data（~40% gap），为社区设定realistic expectations。
      (2)量化了real response matrix的noise sources——missing pattern, ceiling/floor, architecture clustering——
      这些是任何基于IRT的检测方法都会面对的，不仅限于DIF。
      (3)Semi-synthetic框架本身是方法论贡献——它是MMLU-CF(κ=0.14)和GSM1K的superior alternative，
      因为它提供item-level controlled ground truth。
      即使DIF作为检测器fails，semi-synthetic validation framework对评估未来任何检测器都有价值。
      这直接支撑reframe angle (3)。
      关键insight：仅δ≥2.0的极大效应可检测(TPR>0.5)——对应~20pp accuracy inflation，
      即只有最严重的contamination能被任何方法可靠检测。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28e29ba9-3c8f-4542-85e3-302f2e0dcc0d",
  "isSidechain": false,
  "requestId": "req_011CbEVqhYgaJpPbp4s1ff4S",
  "type": "assistant",
  "uuid": "2d673e49-1139-4e3f-bbdd-b3d20df9e71c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LnFHK67ZdWdJVQaeu8udi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12924,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15545,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15545,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12924
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：IRT假设在LLM群体上严重违反，DIF标记被能力-污染混淆主导，核心检测Claim不成立，需彻底reframe 核心假设：['即使架构分层后IRT拟合仍不可接受（RMSEA>0.10），LLM群体本质上违反局部独立性', 'Within-family分析显示>60%的DIF标记反映能力增长而非污染——因果…",
  "leafUuid": "2d673e49-1139-4e3f-bbdd-b3d20df9e71c",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Semi-synthetic and architecture-stratified validation for irt-bench contamination detection",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：IRT假设在LLM群体上严重违反，DIF标记被能力-污染混淆主导，核心检测Claim不成立，需彻底reframe 核心假设：['即使架构分层后IRT拟合仍不可接受（RMSEA>0.10），LLM群体本质上违反局部独立性', 'Within-family分析显示>60%的DIF标记反映能力增长而非污染——因果…",
  "leafUuid": "2d673e49-1139-4e3f-bbdd-b3d20df9e71c",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Semi-synthetic and architecture-stratified validation for irt-bench contamination detection",
  "sessionId": "f643bdc4-2564-483d-b287-4dcc5775353a"
}
```

---
