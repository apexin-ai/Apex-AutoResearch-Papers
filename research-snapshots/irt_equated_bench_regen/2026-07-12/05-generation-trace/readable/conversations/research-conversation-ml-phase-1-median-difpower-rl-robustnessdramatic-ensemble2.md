# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：DIF在真实数据上有信号但power低于模拟预期；RL-robustness优势存在但不dramatic；ensemble中某一信号较弱需降级为2-

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/2187a866-46a1-47af-aa52-e4473c9ed41c.jsonl`
- **Structured JSON:** [`f719f7d0d95cf93e5c7b.json`](../../sessions/f7/f719f7d0d95cf93e5c7b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:49:05.869Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:49:05.869Z",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：DIF在真实数据上有信号但power低于模拟预期；RL-robustness优势存在但不dramatic；ensemble中某一信号较弱需降级为2-signal；equating可行但需caveats\n核心假设：['真实contamination effect sizes分布中δ≥1.4的items占比低于预期，多数flagged items在δ=1.0-1.4中等区间', 'DIF在real data上仍能检测但TPR比simulation低10-15pp（real data noise、model heterogeneity、non-uniform contamination patterns）', 'RL-robustness存在但传统detector在RL下未完全退化至random（AUROC 0.58-0.68），缩小DIF的comparative advantage', 'ConStat或DVD其中一个在目标场景下效果不佳（如DVD对non-variant contamination无效、ConStat对RL退化严重），ensemble降级为2-signal', 'Bifactor equating在单subject内可行但跨subject factor结构不稳定，需限制claims scope', 'MMLU-CF correlation弱但正向；GSM8K验证提供补充但非决定性证据']\n关键指标范围：{'dif_tpr_real_data_delta_ge_1.4': [0.5, 0.7], 'dif_fpr_real_data': [0.04, 0.08], 'mmlu_cf_correlation_with_dif_flags': [0.12, 0.3], 'rl_power_retention_ratio': [0.72, 0.9], 'traditional_detector_auroc_under_rl': [0.56, 0.68], 'ensemble_tpr_full_spectrum': [0.6, 0.8], 'constat_tpr_non_rl_delta_ge_0.6': [0.35, 0.55], 'dvd_tpr_variant_contamination': [0.3, 0.5], 'equating_spearman_rho': [0.88, 0.95], 'gsm8k_gsm1k_gap_dif_correlation': [0.15, 0.3], 'difficulty_calibration_rho_student_sim': [0.55, 0.7]}\n叙事方向：Claim 1调整为\"DIF provides a complementary contamination signal with unique RL-robustness properties\" 而非\"唯一在RL下存活的方法\"——comparative advantage是程度差异而非binary。 Claim 2从\"三信号ensemble\"降级为\"双信号+理论分析third signal failure mode\"， 补充ablation study说明为何某信号失效及其对coverage的影响。 Claim 3限定scope至within-subject equating或pilot-scale demonstration， Spearman rho在0.88-0.95间需讨论acceptable degradation bounds。 核心叙事从\"self-healing benchmark\"调整为\"psychometric monitoring framework with contamination-aware recalibration\"， 强调方法论贡献（将DIF引入LLM evaluation）而非end-to-end pipeline的完整性。 需补充ablation/analysis实验约2-3个来填补reviewers会攻击的gap。 仍投ICLR，但需更强的related work对比和honest limitation section。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026).\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: 'Apply DIF analysis to METABENCH MMLU response matrix (5,055 models\n    × 12,508 items). Split models into temporal cohorts by release date (pre-2024\n    vs post-2024, plus finer annual splits). Run ETS C DIF detection on all items.\n    Validate against MMLU-CF (ACL 2025) contamination-free items as partial ground\n    truth: items present in MMLU but significantly modified in MMLU-CF should correlate\n    with DIF flags. Sensitivity analysis across different cohort definitions and contamination\n    thresholds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: 'Empirically validate DIF''s RL-robustness claim. Construct two scenarios:\n    (a) cohort with SFT-only models, (b) cohort including RL-trained reasoning models\n    (DeepSeek-R1, Qwen-2.5-RL, etc. from METABENCH or via inference). Run DIF + traditional\n    detectors (Min-K%, ConStat perturbation, DVD) on both scenarios. Show DIF maintains\n    detection power in scenario (b) while traditional detectors degrade. If METABENCH\n    lacks RL-trained models, run inference on 10-15 open-weight RL models on MMLU.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations Depends on 003a and 003b\n    completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond MMLU-CF.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:49:05.873Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:49:05.873Z",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-20T19:49:05.897Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：DIF在真实数据上有信号但power低于模拟预期；RL-robustness优势存在但不dramatic；ensemble中某一信号较弱需降级为2-signal；equating可行但需caveats
核心假设：['真实contamination effect sizes分布中δ≥1.4的items占比低于预期，多数flagged items在δ=1.0-1.4中等区间', 'DIF在real data上仍能检测但TPR比simulation低10-15pp（real data noise、model heterogeneity、non-uniform contamination patterns）', 'RL-robustness存在但传统detector在RL下未完全退化至random（AUROC 0.58-0.68），缩小DIF的comparative advantage', 'ConStat或DVD其中一个在目标场景下效果不佳（如DVD对non-variant contamination无效、ConStat对RL退化严重），ensemble降级为2-signal', 'Bifactor equating在单subject内可行但跨subject factor结构不稳定，需限制claims scope', 'MMLU-CF correlation弱但正向；GSM8K验证提供补充但非决定性证据']
关键指标范围：{'dif_tpr_real_data_delta_ge_1.4': [0.5, 0.7], 'dif_fpr_real_data': [0.04, 0.08], 'mmlu_cf_correlation_with_dif_flags': [0.12, 0.3], 'rl_power_retention_ratio': [0.72, 0.9], 'traditional_detector_auroc_under_rl': [0.56, 0.68], 'ensemble_tpr_full_spectrum': [0.6, 0.8], 'constat_tpr_non_rl_delta_ge_0.6': [0.35, 0.55], 'dvd_tpr_variant_contamination': [0.3, 0.5], 'equating_spearman_rho': [0.88, 0.95], 'gsm8k_gsm1k_gap_dif_correlation': [0.15, 0.3], 'difficulty_calibration_rho_student_sim': [0.55, 0.7]}
叙事方向：Claim 1调整为"DIF provides a complementary contamination signal with unique RL-robustness properties" 而非"唯一在RL下存活的方法"——comparative advantage是程度差异而非binary。 Claim 2从"三信号ensemble"降级为"双信号+理论分析third signal failure mode"， 补充ablation study说明为何某信号失效及其对coverage的影响。 Claim 3限定scope至within-subject equating或pilot-scale demonstration， Spearman rho在0.88-0.95间需讨论acceptable degradation bounds。 核心叙事从"self-healing benchmark"调整为"psychometric monitoring framework with contamination-aware recalibration"， 强调方法论贡献（将DIF引入LLM evaluation）而非end-to-end pipeline的完整性。 需补充ablation/analysis实验约2-3个来填补reviewers会攻击的gap。 仍投ICLR，但需更强的related work对比和honest limitation section。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen

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

**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.

**Headline result template**: "On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026)."

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


## experiment_plan (with registry status)

- id: plan_001
  name: real_data_dif_mmlu
  claim: 1
  description: 'Apply DIF analysis to METABENCH MMLU response matrix (5,055 models
    × 12,508 items). Split models into temporal cohorts by release date (pre-2024
    vs post-2024, plus finer annual splits). Run ETS C DIF detection on all items.
    Validate against MMLU-CF (ACL 2025) contamination-free items as partial ground
    truth: items present in MMLU but significantly modified in MMLU-CF should correlate
    with DIF flags. Sensitivity analysis across different cohort definitions and contamination
    thresholds.

    '
  priority: P0
  gpu_budget_hours: 0
  deps: []
  registry_id: ''
  status: planned
- id: plan_002
  name: rl_robustness_validation
  claim: 1
  description: 'Empirically validate DIF''s RL-robustness claim. Construct two scenarios:
    (a) cohort with SFT-only models, (b) cohort including RL-trained reasoning models
    (DeepSeek-R1, Qwen-2.5-RL, etc. from METABENCH or via inference). Run DIF + traditional
    detectors (Min-K%, ConStat perturbation, DVD) on both scenarios. Show DIF maintains
    detection power in scenario (b) while traditional detectors degrade. If METABENCH
    lacks RL-trained models, run inference on 10-15 open-weight RL models on MMLU.

    '
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
    analysis: ensemble FPR<0.10 across all configurations Depends on 003a and 003b
    completing; if one signal fails, degrade to 2-signal ensemble.

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
  "promptId": "f16844c1-7cc1-4aea-853f-8c8da22d0fe3",
  "type": "user",
  "uuid": "713282e9-0d36-48a0-9ede-f7c9f1954365",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:49:05.896Z_

```json
{
  "parentUuid": "713282e9-0d36-48a0-9ede-f7c9f1954365",
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
  "uuid": "e14da796-2c39-453b-bd4b-39eb0117d42e",
  "timestamp": "2026-05-20T19:49:05.896Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:49:05.896Z_

```json
{
  "parentUuid": "e14da796-2c39-453b-bd4b-39eb0117d42e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8e4110dd-d20c-4111-a73d-5210ee846b53",
  "timestamp": "2026-05-20T19:49:05.896Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DIF在真实数据上有信号但power低于模拟预期；RL-robustness优势存在但不dramatic；ensemble中某一信号较弱需降级为2-signal；equating可行但需caveats 核心假设：['真实contamination effect sizes分布中δ≥1.4的items占比低…",
  "leafUuid": "8e4110dd-d20c-4111-a73d-5210ee846b53",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination detection in LLM benchmarks via DIF and psychometric equating",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:49:08.817Z_

I'll analyze each planned experiment under the median tier assumptions and generate detailed predicted results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e4110dd-d20c-4111-a73d-5210ee846b53",
  "isSidechain": false,
  "requestId": "req_011CbEQAegNNqJMkNu5Gkt5H",
  "type": "assistant",
  "uuid": "374a3172-fedd-4273-913f-ee1cb325b742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BMyDUHvomrHB45dftFN7D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10658,
      "cache_read_input_tokens": 11841,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 97,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10658
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

_source line 9 · 2026-05-20T19:49:09.765Z_

<details open><summary>🔧 Tool call — Read · `toolu_012hUHZNuvb7rGgZuQEuPzKr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "374a3172-fedd-4273-913f-ee1cb325b742",
  "isSidechain": false,
  "requestId": "req_011CbEQAegNNqJMkNu5Gkt5H",
  "type": "assistant",
  "uuid": "68bb6f33-f7a9-4305-a112-9ae02dbaf74b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BMyDUHvomrHB45dftFN7D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10658,
      "cache_read_input_tokens": 11841,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 97,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10658
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

_source line 10 · 2026-05-20T19:49:09.783Z_

<details><summary>↩ Tool result · `toolu_012hUHZNuvb7rGgZuQEuPzKr`</summary>

```text
1	
2	## 输出风格
3	
4	- 回复简洁直接，不说废话
5	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
6	- 不要复述用户的问题
7	- 不要给未被要求的建议或补充说明
8	- 推理要彻底，但输出只保留结论和必要信息
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68bb6f33-f7a9-4305-a112-9ae02dbaf74b",
  "isSidechain": false,
  "promptId": "f16844c1-7cc1-4aea-853f-8c8da22d0fe3",
  "type": "user",
  "uuid": "e5fb56f4-ad4e-4651-8b58-54ed5f91514c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "68bb6f33-f7a9-4305-a112-9ae02dbaf74b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T19:49:33.577Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze each planned experiment under the median tier assumptions and generate detailed predicted results. I need to consider:

1. The median tier definition and its core assumptions
2. The key metric ranges defined for median tier
3. Each experiment's goals and dependencies
4. The narrative direction adjustments for median tier

Let me go through each experiment systematically and generate realistic predicted data.

For the median tier:
- DIF has signal on real data but power is lower than simulation
- RL-robustness advantage exists but isn't dramatic
- One ensemble signal is weak, degrading to 2-signal
- Equating works but needs caveats


- Now I'm looking at the performance metrics across these experiments, establishing the expected ranges for each key indicator like DIF's true positive rate on real data, false positive rates, correlation patterns with MMLU, and how well traditional detectors hold up under RL attacks.

For the first experiment with real data and MMLU, I'm expecting the signal to be present but weaker than what the simulations showed—the ETS C true positive rate around 0.68-0.80 for the higher difficulty range should drop by roughly 10-15 percentage points when accounting for real-world noise, model variation, and uneven contamination patterns.

Under reinforcement learning, DIF should hold up better than traditional detectors, though the advantage won't be as pronounced as the simulation suggested. For ConStat, it performs well on non-RL models but degrades significantly under RL training. DVD might be the weaker signal in the median tier—it struggles with non-variant contamination specifically—so I'm leaning toward DVD as the one that fails in the ensemble rather than ConStat.

When I combine these signals, the ensemble drops to just DIF and ConStat with analysis of why DVD breaks down, pushing the TPR into the 0.6-0.8 range. Looking at cross-benchmark validation with GSM8K, I'm seeing weak but positive correlation around 0.15-0.3 for the DIF gap. The bifactor IRT equating works within subjects with Spearman correlations between 0.88-0.95, but cross-subject stability is shaky. Item generation calibration using student simulation performs better than prompt-based approaches but still modest at 0.55-0.7 correlation. The cumulative Bayesian DIF approach shows promise but the gains are incremental.

Now I'm moving into graceful degradation analysis to see how validity holds as replacement rates increase, and examining item-focused trees which give modest improvements over categorical DIF. Let me work through detailed predictions with specific numbers and rationales.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5fb56f4-ad4e-4651-8b58-54ed5f91514c",
  "isSidechain": false,
  "requestId": "req_011CbEQAwC3tUbEQJR8obJgj",
  "type": "assistant",
  "uuid": "6ebd3e78-3676-4956-ad3c-6ebd56c2d044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYyLVDy8dbokeQsHT1p6g5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 22499,
      "output_tokens": 17213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17213,
          "cache_read_input_tokens": 22499,
          "cache_creation_input_tokens": 269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 269
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

_source line 12 · 2026-05-20T19:54:31.522Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1 调整为 "DIF provides a complementary contamination signal with unique RL-robustness properties"，
  强调程度差异而非 binary 生存。Claim 2 从三信号降级为双信号 + DVD failure mode analysis。
  Claim 3 限定为 within-subject equating pilot，讨论 acceptable degradation bounds。
  核心叙事从 "self-healing benchmark" 转向 "psychometric monitoring framework with contamination-aware recalibration"。
  需补充 2-3 个 ablation 实验填补 reviewer 攻击面。仍投 ICLR，但 related work 和 limitation 需加厚。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      在 METABENCH MMLU 响应矩阵（5,055 models × 12,508 items）上执行 DIF 分析。
      按 release date 划分 temporal cohorts（pre-2024 vs post-2024，以及更细的年度分割）。
      对所有 items 运行 ETS C DIF 检测，以 MMLU-CF 为部分 ground truth 做交叉验证。
    expected_results:
      n_models_after_quality_filter: 4312
      n_items_analyzable: 11847
      cohort_pre2024_size: 2876
      cohort_post2024_size: 1436
      n_items_flagged_ets_c: 743
      pct_items_flagged: 0.0627
      dif_tpr_delta_ge_1.4_vs_mmlu_cf: 0.58
      dif_tpr_delta_ge_1.0: 0.41
      dif_fpr_clean_items: 0.062
      mmlu_cf_correlation_spearman: 0.21
      mmlu_cf_correlation_p_value: 0.003
      n_items_delta_ge_1.4_estimated: 187
      n_items_delta_1.0_to_1.4_estimated: 412
      n_items_delta_lt_1.0_estimated: 144
      ets_c_auc_vs_mmlu_cf_binary: 0.71
      sensitivity_cohort_split_annual_tpr_range: "0.52-0.63"
      sensitivity_threshold_sweep_tpr_range: "0.44-0.67"
    result_rationale: >
      Simulation 在 N=100, δ=1.4 下得到 TPR=0.758，但真实数据有三个系统性降级因素：
      (1) 真实 contamination effect sizes 不是均匀的 δ=1.4，多数 flagged items 落在 δ=1.0-1.4 的中间地带，
      拉低了 aggregate TPR；(2) METABENCH 数据的 model heterogeneity（不同架构、不同 training recipe）
      引入 DIF 分析假设之外的 noise，使得 IRT ability estimation 精度下降；
      (3) contamination 不是 binary uniform 的——部分 models 只接触了 partial benchmark subsets，
      创造了 fuzzy group boundaries 而非 simulation 中的 clean reference/focal split。
      MMLU-CF correlation 为正但弱（ρ=0.21），因为 MMLU-CF 的 modification 并非针对 DIF 设计——
      它改变了 item 内容以消除记忆优势，但有些 modification 也改变了 difficulty，
      引入了 false negatives（item 有 DIF 但 CF 版本 too different to count as same construct）。
      FPR 从 simulation 的 0.036-0.042 升至 0.062，因为 real data 中存在
      non-contamination 来源的 DIF（如 certain model families 对特定 domain 有 architecture-driven advantages）。
      δ≥1.4 的 items 仅占 flagged items 的约 25%，大部分 contamination signal 在 medium effect 区间。
    tables:
      - name: "Table 1: DIF Detection Performance on MMLU by Effect Size Band"
        columns: ["effect_size_band", "n_items_estimated", "ets_c_tpr", "ets_c_fpr", "mh_tpr", "lr_tpr"]
        rows:
          - ["δ ≥ 1.6", 68, 0.69, 0.058, 0.54, 0.61]
          - ["δ ∈ [1.4, 1.6)", 119, 0.52, 0.065, 0.38, 0.44]
          - ["δ ∈ [1.0, 1.4)", 412, 0.41, 0.063, 0.27, 0.33]
          - ["δ ∈ [0.6, 1.0)", 144, 0.18, 0.061, 0.11, 0.14]
          - ["Clean (no contamination evidence)", "~10400", "—", 0.062, "—", "—"]
      - name: "Table 2: Sensitivity to Cohort Definition"
        columns: ["cohort_split", "focal_n", "reference_n", "tpr_delta_ge_1.4", "fpr", "n_flagged"]
        rows:
          - ["pre-2024 vs post-2024", 1436, 2876, 0.58, 0.062, 743]
          - ["pre-2023 vs post-2023", 1891, 2421, 0.54, 0.071, 812]
          - ["Annual (2022 vs 2024+)", 987, 1436, 0.63, 0.057, 691]
          - ["Quarterly (Q1-Q2 2023 vs Q3-Q4 2024)", 623, 718, 0.52, 0.084, 658]
      - name: "Table 3: MMLU-CF Cross-Validation"
        columns: ["metric", "value", "95% CI"]
        rows:
          - ["Spearman ρ (DIF effect size vs CF accuracy gap)", 0.21, "[0.09, 0.33]"]
          - ["Items flagged by both DIF and CF", 47, "—"]
          - ["Items flagged by DIF only", 696, "—"]
          - ["Items flagged by CF only", 83, "—"]
          - ["Cohen's κ (binary agreement)", 0.14, "[0.06, 0.22]"]
    figures_description:
      - "Figure 1: Scatter plot — DIF effect size (Δ_MH) vs MMLU-CF accuracy gap per item. 
        Weak positive trend (ρ=0.21) with substantial scatter. Color-coded by MMLU subject.
        STEM items cluster slightly tighter; humanities items show more dispersion.
        Annotation: items with high DIF but low CF gap likely reflect contamination patterns
        CF modification did not capture (e.g., partial memorization of distractor patterns)."
      - "Figure 2: Histogram of estimated DIF effect sizes across all 12,508 items.
        Distribution is right-skewed with long tail. Vertical lines at δ=0.6, 1.0, 1.4 thresholds.
        Bulk of items (89%) below δ=0.6. Of flagged items, majority in δ=1.0-1.4 band,
        not the δ≥1.4 band where DIF has strongest power."
      - "Figure 3: ROC curves for DIF detection using MMLU-CF as noisy ground truth.
        ETS C achieves AUC=0.71, MH AUC=0.64, LR AUC=0.68.
        Note: AUC is suppressed by ground truth noise (CF ≠ perfect contamination label)."
    analysis: >
      核心发现：DIF 在真实数据上有统计显著的 contamination 信号，但 power 比 simulation 低约 12-18pp。
      主要瓶颈是 real contamination effect sizes 分布——δ≥1.4 的 items 仅占约 25%，
      而 DIF 在 δ<1.0 区间的 power 不足以独立检测。
      MMLU-CF 交叉验证提供了 directional support（p=0.003）但 agreement 较低（κ=0.14），
      这既反映 DIF 的 imperfect power，也反映 CF 本身作为 ground truth 的局限性。
      Cohort split sensitivity 分析显示：focal group 越小，FPR 升高（quarterly split 达 0.084），
      建议使用年度或更粗的 cohort 划分。
      对 Claim 1 的影响：TPR=0.58 低于 paper framing 中承诺的 0.72-0.85 range，
      需要将 claim 调整为 "practical detection of large effects" 并明确 medium effect 的 coverage gap。
      这个 gap 恰好为 ensemble（Claim 2）提供了动机。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      实证验证 DIF 的 RL-robustness。构建 SFT-only 和 SFT+RL 两种 cohort，
      在两种场景下运行 DIF 和传统 detectors，量化 RL 对各方法的影响。
    expected_results:
      n_rl_models_identified_in_metabench: 23
      n_rl_models_added_via_inference: 12
      total_rl_models: 35
      total_sft_only_models: 187
      dif_tpr_sft_cohort_delta_ge_1.4: 0.61
      dif_tpr_rl_cohort_delta_ge_1.4: 0.54
      dif_power_retention_ratio: 0.885
      mink_auroc_sft: 0.74
      mink_auroc_rl: 0.51
      mink_power_retention: 0.689
      constat_auroc_sft: 0.69
      constat_auroc_rl: 0.58
      constat_power_retention: 0.841
      dvd_auroc_sft: 0.62
      dvd_auroc_rl: 0.56
      dvd_power_retention: 0.903
      dif_vs_best_traditional_gap_under_rl: 0.08
      gpu_hours_used: 87
    result_rationale: >
      DIF 的 power retention ratio (0.885) 高于传统方法平均值，但 gap 不如理论预期那么 dramatic。
      原因：(1) RL 训练确实平滑了 output distribution（Min-K% AUROC 从 0.74 降至 0.51，
      与 Wang et al. 的 14-20pp degradation 一致），但 DIF 也受到了轻微影响——
      RL 不仅平滑 output，还改变了 response 的 confidence calibration，
      这通过 ability estimation 间接影响 DIF（IRT θ estimates 在 RL models 上 less stable）。
      (2) 传统方法在 RL 下并未完全退化到 random：ConStat AUROC=0.58（不是 0.50），
      因为 perturbation sensitivity 虽然降低但未完全消失——RL 训练通常在 original format 上做 PPO，
      paraphrased items 仍能 trip up 部分 RL models。
      DVD 在 RL 下 AUROC=0.56，看似 retention 高（0.903），但 baseline 本身就低（0.62），
      说明 DVD 对这个 scenario 本身就不敏感而非 RL-robust。
      最终 DIF vs best traditional 的 gap（在 RL 下 DIF TPR=0.54 vs ConStat AUROC=0.58）
      不是 "DIF 独活" 的故事，而是 "DIF 保持了 reasonable power 且是 RL-robustness 最好的之一"。
      这要求将 narrative 从 "only survivor" 调整为 "most robust complement"。
    tables:
      - name: "Table 4: Detection Power Under SFT vs RL Training"
        columns: ["method", "auroc_sft", "auroc_rl", "retention_ratio", "Δ_auroc"]
        rows:
          - ["DIF (ETS C)", 0.73, 0.68, 0.885, -0.05]
          - ["Min-K%", 0.74, 0.51, 0.689, -0.23]
          - ["Min-K%++", 0.71, 0.53, 0.746, -0.18]
          - ["ConStat (perturbation)", 0.69, 0.58, 0.841, -0.11]
          - ["DVD (generation variance)", 0.62, 0.56, 0.903, -0.06]
          - ["Perplexity ratio", 0.67, 0.49, 0.731, -0.18]
          - ["Zlib ratio", 0.59, 0.52, 0.881, -0.07]
      - name: "Table 5: DIF TPR Breakdown by RL Intensity"
        columns: ["rl_category", "n_models", "dif_tpr_delta_ge_1.4", "mink_auroc"]
        rows:
          - ["SFT only", 187, 0.61, 0.74]
          - ["Light RL (< 200 steps)", 14, 0.57, 0.59]
          - ["Heavy RL (≥ 200 steps)", 21, 0.51, 0.47]
    figures_description:
      - "Figure 4: Grouped bar chart — AUROC by detection method, SFT vs RL cohorts.
        DIF shows smallest absolute drop. Min-K% shows largest. Error bars from bootstrap.
        Key visual: DIF bar heights nearly equal across groups; Min-K% and perplexity bars
        drop sharply in RL group."
      - "Figure 5: Power retention ratio plot — methods ranked by (AUROC_RL / AUROC_SFT).
        DIF ranks 2nd (0.885) after DVD (0.903), but DVD's baseline is too low to be useful.
        Annotation: 'high retention on low baseline ≠ useful detection'."
      - "Figure 6: Scatter — DIF effect size vs Min-K% score per item, colored by model training type.
        SFT models show positive correlation; RL models show DIF signal persisting
        while Min-K% collapses toward uniform."
    analysis: >
      RL-robustness 存在但不 dramatic。DIF 的 retention ratio (0.885) 在所有方法中排名靠前，
      但 ConStat (0.841) 也保持了 reasonable power，DVD retention 高但 baseline 低。
      Median tier 下的故事不是 "DIF 是唯一幸存者"，
      而是 "DIF 提供了 RL-robust 且 complementary 的信号"。
      传统方法中 Min-K% 退化最严重（AUROC 0.51，接近 random），
      这与 Wang et al. 一致——output-distribution-based 方法对 RL 最脆弱。
      但 performance-based 方法（ConStat）退化幅度小于预期。
      Reviewer 可能攻击：(1) RL models 样本量小（n=35），统计 power 有限；
      (2) "RL intensity" 是 proxy 而非精确度量。
      需在 paper 中 acknowledge 这些 limitations 并建议 future work 用 controlled RL fine-tuning 验证。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      独立评估 ConStat-style perturbation testing 在 MMLU 上的 contamination 检测能力。
    expected_results:
      n_items_reformulated: 248
      n_models_tested: 42
      reformulation_semantic_similarity_mean: 0.91
      constat_tpr_non_rl_delta_ge_0.6: 0.47
      constat_tpr_non_rl_delta_ge_1.0: 0.58
      constat_tpr_non_rl_delta_ge_1.4: 0.64
      constat_tpr_rl_models_delta_ge_0.6: 0.23
      constat_tpr_rl_models_delta_ge_1.0: 0.31
      constat_fdr_controlled_alpha_0.05: 0.048
      constat_fdr_controlled_alpha_0.10: 0.087
      n_items_detected_fdr_0.10: 89
      overlap_with_dif_flags: 0.34
      gpu_hours_used: 72
    result_rationale: >
      ConStat 在 non-RL models 上表现 reasonable（TPR=0.47 at δ≥0.6），
      因为 perturbation sensitivity 是 memorization 的 direct signal——
      memorized items 的 reformulated 版本会导致 accuracy drop，
      而 genuinely understood items 不会。这在 SFT models 上工作良好。
      但 TPR 未达到 ConStat 原论文 claimed 的水平，原因是：
      (1) MMLU 是 multiple-choice，perturbation space 受限——
      改变 stem wording 可能改变 difficulty 而非仅测 memorization；
      (2) LLM reformulation 质量不均匀，部分 paraphrases 引入了 subtle meaning shifts，
      增加了 noise。在 RL models 上 TPR 下降到 0.23（δ≥0.6），
      因为 RL 训练增强了 models 对 input perturbation 的 robustness（PPO reward hacking 的副效应），
      使得 perturbation sensitivity 信号被 masked。
      与 DIF flags 的 overlap 为 0.34——两种方法检测不同的 contamination facets，
      DIF 捕捉 group-level behavioral shift，ConStat 捕捉 item-level perturbation sensitivity，
      这正好支持 ensemble 的 complementarity 论点。
    tables:
      - name: "Table 6: ConStat Detection Power by Effect Size and Model Type"
        columns: ["effect_size_band", "tpr_non_rl", "tpr_rl", "tpr_all_models"]
        rows:
          - ["δ ≥ 1.4", 0.64, 0.31, 0.53]
          - ["δ ∈ [1.0, 1.4)", 0.58, 0.28, 0.48]
          - ["δ ∈ [0.6, 1.0)", 0.47, 0.23, 0.39]
          - ["δ < 0.6", 0.12, 0.08, 0.10]
      - name: "Table 7: ConStat vs DIF Signal Overlap Analysis"
        columns: ["category", "n_items", "pct_of_flagged"]
        rows:
          - ["Flagged by both DIF and ConStat", 31, "34%"]
          - ["Flagged by DIF only", 58, "64%"]
          - ["Flagged by ConStat only", 52, "57%"]
          - ["Union (either method)", 141, "—"]
    figures_description:
      - "Figure 7: Venn diagram of DIF vs ConStat flagged items.
        Modest overlap (34%) demonstrates complementarity rather than redundancy.
        Annotated with examples: DIF-only items tend to be large-effect, RL-model-driven;
        ConStat-only items tend to be medium-effect, SFT-model-driven."
      - "Figure 8: ConStat detection power curve (TPR vs FDR threshold) for non-RL vs RL model subsets.
        Non-RL curve substantially above RL curve, visualizing the RL degradation.
        DIF power (horizontal reference line) shown for comparison."
    analysis: >
      ConStat 是 ensemble 中可用的第二个信号。它在 non-RL 场景下提供了 DIF 的 complementary coverage，
      尤其在 medium effect sizes（δ=0.6-1.4）——这恰好是 DIF 的 weak spot。
      但 ConStat 在 RL 下 degradation 明显（TPR 从 0.47 降至 0.23），
      形成了与 DIF 的互补关系：DIF RL-robust 但需大 effect sizes，ConStat 覆盖 medium effects 但 RL-fragile。
      两者 overlap 仅 34%，支持 ensemble 而非 redundancy。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      独立评估 DVD generation variance 在 MMLU contamination detection 上的表现。
    expected_results:
      n_models_with_inference_access: 14
      n_items_tested: 248
      responses_per_item: 50
      dvd_tpr_variant_contamination: 0.38
      dvd_tpr_verbatim_contamination: 0.16
      dvd_tpr_non_variant_all: 0.19
      dvd_fpr: 0.094
      dvd_auroc_overall: 0.57
      bimodal_distribution_pct_items: 0.078
      generation_variance_mean_clean: 0.42
      generation_variance_mean_contaminated: 0.31
      generation_variance_separation_cohens_d: 0.38
      gpu_hours_used: 64
    result_rationale: >
      DVD 在 median tier 下是表现最弱的信号，降级 ensemble 从 3-signal 到 2-signal 的主要原因。
      核心问题：MMLU 是 multiple-choice format，generation variance 的 signal 天然被压缩——
      即使 model 记忆了答案，其 generation 仍然只是 output 一个 letter (A/B/C/D)，
      variance 空间极为有限。DVD 原设计针对 open-ended generation tasks，
      在那里 memorized 内容会导致 deterministic long-form output（低 variance），
      但 MMLU 的 forced-choice format 使得这个信号几乎消失。
      Variant contamination（model 见过 rephrased version）确实产生了 slightly higher detection（TPR=0.38），
      因为 model 在 seen variants 上的 confidence distribution 有异常——
      但这个 TPR 仍然不足以作为 reliable signal。
      Verbatim contamination 的 TPR 仅 0.16，因为 correct 答案的 generation variance
      在 clean 和 contaminated items 之间差异太小（Cohen's d=0.38）。
      FPR=0.094 偏高，接近 actionable threshold。
      这些结果表明 DVD 在 MMLU-like benchmarks 上不适用，
      但需在 paper 中分析 failure mode 并讨论其在 open-ended benchmarks 上的 potential。
    tables:
      - name: "Table 8: DVD Detection Performance on MMLU"
        columns: ["contamination_type", "n_items", "tpr", "auroc", "cohen_d"]
        rows:
          - ["Variant contamination", 34, 0.38, 0.62, 0.51]
          - ["Verbatim contamination", 89, 0.16, 0.54, 0.29]
          - ["Mixed/unknown", 125, 0.19, 0.57, 0.38]
          - ["Clean items", "~11600", "—(FPR=0.094)", "—", "—"]
      - name: "Table 9: Generation Variance Statistics"
        columns: ["item_category", "mean_variance", "std", "median"]
        rows:
          - ["Clean items", 0.42, 0.18, 0.39]
          - ["Contaminated (verbatim)", 0.31, 0.21, 0.28]
          - ["Contaminated (variant)", 0.27, 0.19, 0.24]
    figures_description:
      - "Figure 9: Distribution of generation variance scores for clean vs contaminated items.
        Substantial overlap between distributions. Cohen's d=0.38 indicates weak separation.
        Contrast with DIF effect size distribution (Figure 2) to motivate why DVD
        fails on multiple-choice format."
      - "Figure 10: Per-model variance heatmap (14 models × 248 items).
        No clear bimodal structure visible for most contaminated items.
        Bimodal pattern appears in only 7.8% of items — insufficient for reliable detection."
    analysis: >
      DVD 是 ensemble 中 failed signal。Multiple-choice format 从根本上限制了 generation variance 的信息量。
      这不是 DVD method 本身的缺陷，而是 application domain mismatch。
      Paper 中需要：(1) 清楚报告 DVD 的 failure 及 root cause analysis；
      (2) 讨论 DVD 可能在 open-ended benchmarks（如 HumanEval、MATH with free-form answers）上有效；
      (3) 作为 ablation study 之一，分析 format dependence 对 detection signal 的影响。
      这个 negative result 反而增强 paper 的 intellectual honesty，reviewer 会 appreciate 
      对 failure mode 的 transparent analysis 而非 cherry-picking。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      将 DIF + ConStat 融合为双信号 ensemble（DVD 降级为 ablation analysis）。
    expected_results:
      ensemble_type: "2-signal (DIF + ConStat)"
      ensemble_tpr_delta_ge_1.4_all: 0.73
      ensemble_tpr_delta_ge_1.0_all: 0.61
      ensemble_tpr_delta_ge_0.6_all: 0.48
      ensemble_tpr_full_spectrum: 0.68
      ensemble_fpr: 0.082
      ensemble_tpr_rl_only_delta_ge_1.4: 0.59
      ensemble_tpr_non_rl_delta_ge_0.6: 0.55
      majority_voting_2of2_tpr: 0.34
      majority_voting_1of2_tpr: 0.79
      majority_voting_1of2_fpr: 0.11
      weighted_fusion_optimal_tpr: 0.73
      weighted_fusion_optimal_fpr: 0.082
      dif_weight_in_fusion: 0.58
      constat_weight_in_fusion: 0.42
      ablation_dif_only_tpr: 0.58
      ablation_constat_only_tpr: 0.47
      ablation_add_dvd_tpr_gain: 0.02
      coverage_analysis_dif_unique: 0.21
      coverage_analysis_constat_unique: 0.18
      coverage_analysis_overlap: 0.29
    result_rationale: >
      2-signal ensemble 通过 complementarity 实现了比任一单信号更好的 coverage：
      DIF 覆盖 large effects + RL-robust，ConStat 覆盖 medium effects + non-RL，
      union coverage 高于单独使用任一方法。
      Weighted fusion（DIF 0.58, ConStat 0.42）优于 simple voting，
      因为 DIF 的 RL-robustness 使其在 mixed model population 中更 reliable。
      2-of-2 voting 过于保守（TPR=0.34），因为两种方法检测的 contamination facet 不同——
      要求两者同时 flag 等于取 intersection 而非 union。
      1-of-2 voting FPR 偏高（0.11），因为 ConStat 的 FPR contribution。
      Weighted fusion 在 TPR=0.73 / FPR=0.082 处取得最佳平衡。
      加入 DVD 仅带来 +0.02 TPR gain，不值得增加 pipeline 复杂度，
      证实了 2-signal 降级的合理性。
      Ensemble TPR=0.68（full spectrum）落在 median tier 指标范围 [0.6, 0.8] 内。
    tables:
      - name: "Table 10: Ensemble Fusion Strategy Comparison"
        columns: ["strategy", "tpr_δ≥1.4", "tpr_δ≥0.6", "fpr", "f1"]
        rows:
          - ["DIF only", 0.58, 0.38, 0.062, 0.47]
          - ["ConStat only", 0.64, 0.47, 0.087, 0.51]
          - ["1-of-2 (union)", 0.79, 0.61, 0.110, 0.54]
          - ["2-of-2 (intersection)", 0.34, 0.24, 0.031, 0.37]
          - ["Weighted fusion (optimal)", 0.73, 0.48, 0.082, 0.56]
      - name: "Table 11: Coverage Analysis — What Each Signal Uniquely Detects"
        columns: ["scenario", "dif_alone_detects", "constat_alone_detects", "both_detect", "neither_detects"]
        rows:
          - ["Large effect + RL model", "✓", "✗", "—", "—"]
          - ["Medium effect + SFT model", "✗", "✓", "—", "—"]
          - ["Large effect + SFT model", "—", "—", "✓", "—"]
          - ["Small effect (δ<0.6)", "—", "—", "—", "✓"]
      - name: "Table 12: Ablation — Value of Each Signal in Ensemble"
        columns: ["configuration", "tpr_full_spectrum", "Δ_vs_full_ensemble"]
        rows:
          - ["DIF + ConStat (full)", 0.68, "baseline"]
          - ["DIF only", 0.58, -0.10]
          - ["ConStat only", 0.47, -0.21]
          - ["DIF + ConStat + DVD", 0.70, +0.02]
    figures_description:
      - "Figure 11: Coverage heatmap — rows are (effect size band × model type) cells,
        columns are detection methods. Color intensity = TPR in that cell.
        Shows DIF strong in upper-right (large effect, RL), ConStat strong in middle-left
        (medium effect, SFT), both weak in lower region (small effects).
        Ensemble union covers more cells than either alone."
      - "Figure 12: Precision-Recall curves for single-signal vs ensemble approaches.
        Ensemble curve dominates both individual curves, especially in the 0.4-0.7 recall range
        where complementarity adds most value."
      - "Figure 13: Ablation bar chart — TPR contribution of adding each signal.
        DIF→DIF+ConStat: +0.10. DIF+ConStat→+DVD: +0.02.
        Diminishing returns visualized; motivates 2-signal design choice."
    analysis: >
      2-signal ensemble 在 median tier 下是 pragmatic best result：
      full spectrum TPR=0.68 说明 coverage 有显著 gaps（尤其 small effects + RL），
      但比任一单信号提升 10-21pp。
      Paper narrative 需强调 complementarity mechanism 而非 absolute performance，
      并 honestly 报告 coverage holes。
      DVD ablation 提供了 principled argument for 2-signal design，
      同时 DVD failure analysis 作为 Section 5.3 的 content。
      Reviewer concern：FPR=0.082 接近 0.10 boundary，需讨论 false alarm cost 和 threshold tuning。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      在 GSM8K 上复制 DIF 分析，使用 GSM1K 作为 contamination ground truth。
    expected_results:
      n_models_gsm8k: 68
      n_items_gsm8k: 1319
      n_items_gsm1k: 1250
      cohort_split: "pre-2024 vs post-2024"
      focal_n: 31
      reference_n: 37
      n_items_dif_flagged_gsm8k: 127
      pct_items_flagged_gsm8k: 0.096
      gsm8k_gsm1k_gap_mean_all_models: 0.073
      gsm8k_gsm1k_gap_mean_flagged_models: 0.118
      gsm8k_gsm1k_gap_dif_correlation: 0.22
      gsm8k_gsm1k_gap_correlation_p_value: 0.014
      dif_tpr_vs_gsm1k_proxy: 0.49
      dif_fpr_vs_gsm1k_proxy: 0.071
      per_model_dif_flag_count_vs_gap_r: 0.31
      gpu_hours_used: 83
    result_rationale: >
      GSM8K 上的 DIF 分析面临更大挑战：(1) model sample size 更小（N=68 vs MMLU 的 4312），
      直接降低 statistical power；(2) GSM8K 是 math reasoning 而非 factual recall，
      contamination pattern 不同——models 可能记忆了 solution patterns 而非 specific items，
      DIF 对 pattern-level contamination 不如 item-level 敏感。
      GSM8K-GSM1K gap correlation (ρ=0.22, p=0.014) 提供了独立验证 DIF 有 contamination 信号的证据，
      但 correlation 弱于 MMLU-CF（ρ=0.21 对 ρ=0.22 看似接近，但 GSM1K 是更 clean 的 ground truth），
      反映了 math reasoning benchmark 上 contamination 形态的不同。
      Per-model analysis（每个 model 被 flag 的 item count vs 其 GSM8K-GSM1K gap，r=0.31）
      比 item-level correlation 更强，说明 DIF 在 model-level 上更有 discriminative power。
      TPR=0.49 低于 MMLU 的 0.58，主要因为 sample size 和 effect size distribution 差异。
    tables:
      - name: "Table 13: GSM8K DIF Results Summary"
        columns: ["metric", "value", "95% CI"]
        rows:
          - ["Items flagged by DIF", 127, "—"]
          - ["Mean GSM8K-GSM1K gap (all models)", "7.3%", "[5.1%, 9.5%]"]
          - ["Mean gap (high DIF-flag-count models)", "11.8%", "[8.2%, 15.4%]"]
          - ["Item-level DIF-gap correlation (ρ)", 0.22, "[0.06, 0.37]"]
          - ["Model-level flag-count-gap correlation (r)", 0.31, "[0.14, 0.47]"]
      - name: "Table 14: Cross-Benchmark Comparison"
        columns: ["benchmark", "n_models", "n_items", "dif_tpr", "ground_truth_correlation", "fpr"]
        rows:
          - ["MMLU", 4312, 11847, 0.58, "ρ=0.21 (MMLU-CF)", 0.062]
          - ["GSM8K", 68, 1319, 0.49, "ρ=0.22 (GSM1K)", 0.071]
    figures_description:
      - "Figure 14: Scatter — per-model DIF flag count vs GSM8K-GSM1K accuracy gap.
        Positive trend (r=0.31) with high variance. Models with >15 flagged items
        tend to have larger gaps. Outliers annotated: some models with large gaps
        but few DIF flags (pattern-level contamination DIF misses)."
      - "Figure 15: Side-by-side DIF effect size distributions for MMLU and GSM8K.
        GSM8K distribution shifted left (smaller effects on average), consistent with
        math reasoning contamination being subtler than factual knowledge contamination."
    analysis: >
      GSM8K 结果提供了 complementary 但非 decisive 的验证。
      ρ=0.22 是 statistically significant 但 practically weak 的 correlation。
      主要价值是证明 DIF 在不同 benchmark domain（factual vs reasoning）上都有 signal，
      但 power 更低。Paper 中需讨论 math reasoning benchmarks 上 contamination 形态不同
      （pattern memorization vs item memorization）作为 DIF power 下降的 explanation。
      这个实验作为 supporting evidence 而非 standalone result。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      在 MMLU 上 pilot bifactor IRT equating：拟合 bifactor model，选择 anchor items，
      通过 fixed-parameter calibration 校准 replacement items。
    expected_results:
      bifactor_model_converged: true
      n_general_factor_loadings_gt_0.3: 9847
      n_subject_factors: 57
      subject_factor_variance_explained_range: "0.04-0.18"
      general_factor_variance_explained: 0.41
      n_anchor_items_selected: 2340
      anchor_item_dif_stability: 0.96
      within_subject_equating_spearman_rho_mean: 0.93
      within_subject_equating_rho_range: "0.89-0.97"
      cross_subject_equating_spearman_rho: 0.87
      cross_subject_factor_instability_pct: 0.23
      score_reliability_original: 0.89
      score_reliability_equated_5pct_replaced: 0.87
      score_reliability_equated_20pct_replaced: 0.82
      equating_bias_mean: 0.003
      equating_rmse: 0.047
    result_rationale: >
      Bifactor model 在 MMLU 上 converges 但 reveals structural heterogeneity：
      general factor 仅解释 41% variance（低于典型 educational test 的 50-60%），
      因为 MMLU 覆盖 57 个 diverse subjects，跨 subject variance 大。
      Within-subject equating 表现良好（mean ρ=0.93），因为 same-subject items 共享 factor structure，
      anchor items 稳定性高（stability=0.96）。
      但 cross-subject equating（ρ=0.87）低于 within-subject，因为 23% 的 subjects
      的 factor structure 在不同 model cohorts 间不稳定——
      即 model evolution 不仅改变了 ability level，也改变了 ability structure
      （某些 model families 在 STEM 上进步远快于 humanities），
      violating bifactor model 的 factorial invariance 假设。
      ρ=0.93 在 within-subject 内可行但 ρ=0.87 cross-subject 不足以支持 "全 benchmark 等值" 的 claim。
      这迫使 Claim 3 限定 scope 为 within-subject equating pilot。
      Progressive replacement 分析显示 5% 替换下 reliability 可接受（0.87），
      但 20% 替换时 reliability 降至 0.82，接近 practical minimum。
    tables:
      - name: "Table 15: Bifactor Model Fit Statistics"
        columns: ["metric", "value"]
        rows:
          - ["General factor variance explained", 0.41]
          - ["Mean subject-factor variance", 0.09]
          - ["RMSEA", 0.038]
          - ["CFI", 0.94]
          - ["TLI", 0.92]
          - ["Subjects with stable factor structure", "44/57 (77%)"]
      - name: "Table 16: Equating Performance by Scope"
        columns: ["scope", "spearman_rho", "equating_bias", "rmse", "n_items_replaced"]
        rows:
          - ["Within-subject (STEM avg)", 0.95, 0.002, 0.038, 47]
          - ["Within-subject (Humanities avg)", 0.91, 0.004, 0.052, 39]
          - ["Within-subject (overall)", 0.93, 0.003, 0.047, 86]
          - ["Cross-subject (full MMLU)", 0.87, 0.011, 0.073, 86]
      - name: "Table 17: Score Reliability Under Progressive Replacement"
        columns: ["pct_items_replaced", "reliability_α", "ranking_τ", "rho"]
        rows:
          - ["0% (baseline)", 0.89, 1.00, 1.00]
          - ["5%", 0.87, 0.98, 0.97]
          - ["10%", 0.85, 0.96, 0.95]
          - ["20%", 0.82, 0.93, 0.91]
          - ["50%", 0.74, 0.84, 0.82]
    figures_description:
      - "Figure 16: Within-subject equating scatter plots for 4 representative subjects.
        Original vs equated model rankings. STEM subjects (physics, CS) show tighter fit;
        humanities subjects (philosophy, history) show more scatter."
      - "Figure 17: Reliability degradation curve — score reliability (Cronbach's α equivalent)
        vs percentage of items replaced. Horizontal dashed line at α=0.80 (acceptable threshold).
        Crosses threshold between 20-30% replacement, suggesting practical upper bound."
      - "Figure 18: Subject-level factor stability analysis.
        Heatmap of factor loading correlations across cohorts per subject.
        23% of subjects show loading correlation < 0.85, indicating structural instability."
    analysis: >
      Within-subject equating 是 viable（ρ=0.93），但 cross-subject 不稳定（ρ=0.87）
      限制了 full-benchmark equating 的 claim。
      Paper 中需要：(1) 明确 scope 限制——Claim 3 rewrite 为 "within-subject equating pilot"；
      (2) 讨论 factor instability 的 root cause（model capability evolution 非 uniform across domains）；
      (3) 提出 subject-specific equating 作为 practical deployment strategy。
      Progressive replacement 结果提供了 practical guideline：5-10% 替换安全，20% 是 borderline，
      50% 不可接受。这是有用的 contribution 即使 full equating 不完美。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      为 DIF-flagged 的 MMLU items 生成替换 items，通过 student simulation 校准 difficulty。
    expected_results:
      n_items_generated: 150
      n_items_passing_quality_filter: 118
      quality_filter_pass_rate: 0.787
      difficulty_rho_prompt_based: 0.32
      difficulty_rho_student_sim: 0.63
      difficulty_rho_student_sim_within_subject: 0.68
      discrimination_correlation: 0.41
      construct_validity_factor_loading_mean: 0.38
      construct_validity_factor_loading_original_mean: 0.47
      difficulty_mae_prompt_based: 0.34
      difficulty_mae_student_sim: 0.19
      n_items_within_0.5_logit_of_target: 74
      pct_items_within_0.5_logit: 0.627
      gpu_hours_used: 178
    result_rationale: >
      Student simulation calibration（ρ=0.63）显著优于 prompt-based targeting（ρ=0.32），
      因为 student simulation 通过实际 "model population" 响应来 estimate difficulty，
      绕过了 LLM self-assessment 的 calibration 问题。
      但 ρ=0.63 低于 arXiv 2601.09953 reported 的 r=0.75-0.82，原因有二：
      (1) 那篇论文的 evaluation 是 within-domain（同类型题目），
      而这里的 generated items 跨越了 57 subjects，domain diversity 降低了 aggregate correlation；
      (2) MMLU items 的 difficulty 部分来自 distractor quality，
      LLM generation 的 distractors 往往不如 human-crafted 的 effective，
      导致 generated items systematically easier（difficulty MAE=0.19 with slight easy-bias）。
      Within-subject ρ=0.68 高于 overall 的 0.63，说明 domain-specific generation 更 reliable。
      Construct validity 是 soft spot：generated items 的 factor loadings（mean=0.38）
      低于 original items（0.47），表明 generated items 与 underlying construct 的 alignment 较弱。
      这 limits claim 强度——replacement items 在 difficulty 上校准 acceptable，
      但 construct validity 有 degradation。
    tables:
      - name: "Table 18: Difficulty Calibration Comparison"
        columns: ["method", "ρ_overall", "ρ_within_subject", "mae", "n_within_0.5_logit"]
        rows:
          - ["Prompt-based targeting", 0.32, 0.39, 0.34, "41/118 (35%)"]
          - ["Student simulation", 0.63, 0.68, 0.19, "74/118 (63%)"]
          - ["Student sim + iterative refinement", 0.66, 0.71, 0.17, "79/118 (67%)"]
      - name: "Table 19: Generated Item Quality Metrics"
        columns: ["metric", "generated_items", "original_items", "gap"]
        rows:
          - ["Mean difficulty (IRT b)", -0.62, -0.84, "+0.22 (easier)"]
          - ["Mean discrimination (IRT a)", 0.93, 1.20, "-0.27"]
          - ["Factor loading (general)", 0.38, 0.47, "-0.09"]
          - ["Distractor effectiveness", 0.61, 0.78, "-0.17"]
    figures_description:
      - "Figure 19: Scatter — target difficulty (from DIF-flagged original item) vs achieved difficulty
        (student simulation estimate). Prompt-based (left panel, ρ=0.32) vs student sim (right panel, ρ=0.63).
        Student sim shows tighter fit with systematic easy-bias visible as regression line below identity."
      - "Figure 20: Histogram of difficulty calibration errors (|b_target - b_achieved|).
        Student sim distribution shifted left relative to prompt-based.
        63% of student sim items within 0.5 logit of target (vs 35% for prompt-based)."
    analysis: >
      Student simulation calibration 是 viable 但 imperfect 的 difficulty estimation method。
      ρ=0.63 的 practical implication：about 2/3 of items 在 acceptable difficulty range 内，
      足够 support "empirical calibration dramatically outperforms prompt-based" 的 claim，
      但不足以 claim "precise psychometric replacement"。
      Construct validity gap（factor loading 0.38 vs 0.47）是 paper 需要 honestly address 的 limitation——
      generated items 测量了 approximately same construct 但不 identical。
      Combined with equating results (plan_005)，Claim 3 的叙事应为
      "pilot demonstration of calibrated regeneration with known quality bounds"。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      实现 cumulative Bayesian DIF priors，模拟 4 次连续 benchmark administrations，
      展示 evidence accumulation 带来的 power improvement。
    expected_results:
      n_administrations_simulated: 4
      n_models_per_administration: 80
      power_admin_1_medium_delta_1.0: 0.33
      power_admin_2_cumulative: 0.48
      power_admin_3_cumulative: 0.59
      power_admin_4_cumulative: 0.66
      power_admin_1_large_delta_1.4: 0.55
      power_admin_4_large_delta_1.4_cumulative: 0.78
      false_positive_rate_cumulative: 0.053
      bayes_factor_threshold: 3.0
      pct_items_reaching_bf_threshold_by_admin_4: 0.71
    result_rationale: >
      Bayesian accumulation 从 real-data 的 lower baseline 开始（而非 simulation 的 higher baseline），
      所以 single administration power 为 0.33（medium effect），低于 simulation 的 ~0.40。
      但 accumulation dynamic 仍然 works：每次 administration 增加约 0.10-0.15 power，
      到第 4 次达到 0.66——接近但未达到 simulation 预期的 0.70。
      Gap 来自 real data 的 prior mis-specification：Bayesian prior 假设 DIF effects 
      follow specific distribution，但真实 contamination 的 temporal dynamics 不 stationary
      （某些 items 的 contamination 随时间变化，violating prior assumptions）。
      FPR 保持在 0.053，说明 Bayesian framework 的 false alarm control 合理。
      For large effects（δ=1.4），cumulative power 达到 0.78（4 administrations），
      这是 paper 中值得 highlight 的 positive result——说明 "patience pays off"。
    tables:
      - name: "Table 20: Cumulative Bayesian DIF Power Over Successive Administrations"
        columns: ["administration", "n_models_cumulative", "power_δ=1.0", "power_δ=1.4", "fpr"]
        rows:
          - ["1", 80, 0.33, 0.55, 0.048]
          - ["2", 160, 0.48, 0.67, 0.051]
          - ["3", 240, 0.59, 0.74, 0.052]
          - ["4", 320, 0.66, 0.78, 0.053]
    figures_description:
      - "Figure 21: Power accumulation curves — TPR vs number of administrations for δ=1.0 and δ=1.4.
        Both curves show diminishing-returns concave shape. δ=1.4 curve crosses 0.70 threshold
        by administration 3; δ=1.0 curve approaches but doesn't reach 0.70 by administration 4.
        Extrapolation (dashed) suggests ~6 administrations needed for δ=1.0 to reach 0.70."
    analysis: >
      Bayesian accumulation 是 DIF power 不足问题的 temporal solution。
      核心 message：单次检测 power 有限（0.33-0.55），但 monitoring framework 
      通过时间积累达到 useful power（0.66-0.78 at 4 administrations）。
      这 directly supports "psychometric monitoring framework" 的 narrative reframing——
      不是 one-shot detection 而是 continuous monitoring。
      但需要注意 practical caveat：4 administrations 可能需要 1-2 年，
      在此期间 contamination 已经对 benchmark validity 造成了 damage。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      分析 benchmark validity 在 progressive item replacement 下的 graceful degradation。
    expected_results:
      replacement_rates_tested: [0.05, 0.10, 0.15, 0.20, 0.30, 0.50]
      ranking_stability_kendall_tau_5pct: 0.97
      ranking_stability_kendall_tau_10pct: 0.95
      ranking_stability_kendall_tau_20pct: 0.91
      ranking_stability_kendall_tau_50pct: 0.81
      score_reliability_cronbach_5pct: 0.87
      score_reliability_cronbach_10pct: 0.85
      score_reliability_cronbach_20pct: 0.82
      score_reliability_cronbach_50pct: 0.74
      construct_coverage_jaccard_5pct: 0.97
      construct_coverage_jaccard_20pct: 0.89
      construct_coverage_jaccard_50pct: 0.76
      theoretical_upper_bound_replacement_rate: 0.25
      practical_recommended_max: 0.15
      equating_error_propagation_rmse_10pct: 0.041
      equating_error_propagation_rmse_20pct: 0.068
    result_rationale: >
      Graceful degradation 分析显示 benchmark validity 在 low replacement rates 下 well-preserved，
      但在 >20% 时快速衰退。这符合 psychometric theory：test reliability 近似为 Spearman-Brown 函数，
      each replaced item 引入 calibration error（plan_006 显示 difficulty ρ=0.63），
      error 随 replacement rate 线性累积但 validity impact 呈 nonlinear degradation。
      15% replacement 是 practical sweet spot：ranking stability (τ=0.93) 和 reliability (α=0.84) 
      都在 acceptable range，且涵盖了 plan_001 中约 80% 的 δ≥1.0 flagged items。
      50% replacement 的 reliability 降至 0.74，低于 psychometric 标准的 0.80 threshold——
      这是 "benchmark 不再可比" 的 hard boundary。
      Theoretical analysis 给出 upper bound 25%（在 perfect calibration 假设下），
      但 plan_006 的 imperfect calibration 将实际 limit 压到 15%。
    tables:
      - name: "Table 21: Validity Metrics Under Progressive Replacement"
        columns: ["replacement_rate", "kendall_τ", "cronbach_α", "construct_jaccard", "equating_rmse"]
        rows:
          - ["0% (baseline)", 1.00, 0.89, 1.00, 0.000]
          - ["5%", 0.97, 0.87, 0.97, 0.029]
          - ["10%", 0.95, 0.85, 0.94, 0.041]
          - ["15%", 0.93, 0.84, 0.91, 0.054]
          - ["20%", 0.91, 0.82, 0.89, 0.068]
          - ["30%", 0.87, 0.78, 0.83, 0.091]
          - ["50%", 0.81, 0.74, 0.76, 0.132]
    figures_description:
      - "Figure 22: Multi-panel degradation curves — kendall τ, cronbach α, construct coverage
        vs replacement rate. All three metrics show concave degradation pattern.
        Shaded regions indicate 'safe' (<15%), 'caution' (15-25%), and 'unacceptable' (>25%) zones.
        Vertical dashed lines at 15% (practical) and 25% (theoretical) bounds."
      - "Figure 23: Equating error propagation — RMSE of equated scores vs replacement rate.
        Near-linear growth up to 20%, then acceleration. Error bars from bootstrap (100 resamples)."
    analysis: >
      This experiment 提供了 Claim 3 最重要的 practical guideline：
      up to 15% item replacement 维持 acceptable validity，这足以处理大部分 contamination。
      Paper 应将此 frame 为 "known operating envelope" 而非 limitation——
      psychometric maturity 在于知道方法的 validity bounds，而非声称无限 scalability。
      Theoretical vs practical bound gap（25% vs 15%）由 item generation quality 驱动，
      指向 future work：improve generation quality → expand operating envelope。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      实现 Item-Focused Trees 作为 categorical cohort DIF 的替代方案，
      将 model release date 作为连续 covariate。
    expected_results:
      n_items_analyzed: 11847
      n_items_significant_ift: 891
      ift_tpr_delta_ge_1.4: 0.62
      ift_tpr_delta_ge_1.0: 0.46
      ift_fpr: 0.058
      ift_vs_ets_c_tpr_gain: 0.04
      ift_vs_ets_c_fpr_reduction: 0.004
      ift_detected_gradual_contamination_items: 134
      ift_split_point_mode_month: "2023-09"
      ift_computational_time_minutes: 47
    result_rationale: >
      Item-Focused Trees 提供了 modest improvement over categorical DIF（TPR +0.04, FPR -0.004），
      因为它避免了 arbitrary cohort splits 导致的 information loss——
      连续 covariate 保留了 release date 的 full ordering information。
      但 improvement 幅度有限，因为 contamination 在时间上确实是 roughly step-function-like
      （一旦 benchmark 被 widely available，contamination 快速 saturates），
      使得 continuous treatment 的 marginal benefit 小。
      IFT 的独特贡献是发现了 134 个 "gradual contamination" items——
      这些 items 的 DIF effect size 随时间平滑增长而非 suddenly appear，
      对应 incremental leakage pattern。这在 categorical DIF 中不可见。
      Split point mode 在 2023-09，大致对应 MMLU 进入 mainstream LLM training data 的时间点。
    tables:
      - name: "Table 22: IFT vs Categorical DIF Comparison"
        columns: ["method", "tpr_δ≥1.4", "tpr_δ≥1.0", "fpr", "unique_detections"]
        rows:
          - ["ETS C (categorical)", 0.58, 0.41, 0.062, 47]
          - ["IFT (continuous)", 0.62, 0.46, 0.058, 134]
          - ["Overlap (both detect)", "—", "—", "—", 612]
    figures_description:
      - "Figure 24: Item-level contamination onset timeline.
        X-axis: model release date. Y-axis: IFT-estimated DIF effect size.
        Each line represents one item. Most items show step-function pattern (sudden onset);
        134 items show gradual ramp (linear increase). Vertical dashed line at 2023-09."
    analysis: >
      IFT 是 useful methodological extension 但非 game-changer。
      Paper 中作为 robustness check 和 methodological contribution（Section 4.x）。
      Gradual contamination finding 是 interesting insight，
      可作为 discussion point 关于 contamination dynamics。
      Reviewer 可能认为 +0.04 TPR 不值得 additional complexity；
      response 是 IFT 的价值在 qualitative insight（gradual contamination）而非 quantitative gain。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ebd3e78-3676-4956-ad3c-6ebd56c2d044",
  "isSidechain": false,
  "requestId": "req_011CbEQAwC3tUbEQJR8obJgj",
  "type": "assistant",
  "uuid": "732fae6a-c577-44be-80a3-c8f09bd7213a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYyLVDy8dbokeQsHT1p6g5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 22499,
      "output_tokens": 17213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17213,
          "cache_read_input_tokens": 22499,
          "cache_creation_input_tokens": 269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 269
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DIF在真实数据上有信号但power低于模拟预期；RL-robustness优势存在但不dramatic；ensemble中某一信号较弱需降级为2-signal；equating可行但需caveats 核心假设：['真实contamination effect sizes分布中δ≥1.4的items占比低…",
  "leafUuid": "732fae6a-c577-44be-80a3-c8f09bd7213a",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination detection in LLM benchmarks via DIF and psychometric equating",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：DIF在真实数据上有信号但power低于模拟预期；RL-robustness优势存在但不dramatic；ensemble中某一信号较弱需降级为2-signal；equating可行但需caveats 核心假设：['真实contamination effect sizes分布中δ≥1.4的items占比低…",
  "leafUuid": "732fae6a-c577-44be-80a3-c8f09bd7213a",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination detection in LLM benchmarks via DIF and psychometric equating",
  "sessionId": "2187a866-46a1-47af-aa52-e4473c9ed41c"
}
```

---
