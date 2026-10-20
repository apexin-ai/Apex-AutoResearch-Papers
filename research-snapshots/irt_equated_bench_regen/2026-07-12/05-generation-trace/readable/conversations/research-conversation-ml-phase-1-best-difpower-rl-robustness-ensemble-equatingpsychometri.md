# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：DIF在真实数据上复现模拟power，RL-robustness经验验证成功，ensemble三信号互补清晰，equating达到psychometri

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/25adcdbb-09aa-42cd-bd7a-e053270e6068.jsonl`
- **Structured JSON:** [`7831fb8a8d3ecdc7fe60.json`](../../sessions/78/7831fb8a8d3ecdc7fe60.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:43:57.963Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:43:57.963Z",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：DIF在真实数据上复现模拟power，RL-robustness经验验证成功，ensemble三信号互补清晰，equating达到psychometric标准——原始framing完整成立\n核心假设：['METABENCH真实cohort size达N≥80且contamination effect sizes在δ≥1.4区间有足够flagged items', 'DIF在real response matrix上的power与模拟一致（非simulation artifact）', 'RL-trained模型cohort的DIF power无显著衰减，而传统detector明确退化至near-random', 'MMLU-CF partial ground truth与DIF flags正相关，提供外部验证', 'ConStat和DVD各自在其target effect-size/model-type区间有效，ensemble互补成立', 'Bifactor IRT equating后replacement items保持rank ordering']\n关键指标范围：{'dif_tpr_real_data_delta_ge_1.4': [0.7, 0.85], 'dif_fpr_real_data': [0.02, 0.05], 'mmlu_cf_correlation_with_dif_flags': [0.3, 0.5], 'rl_power_retention_ratio': [0.9, 1.0], 'traditional_detector_auroc_under_rl': [0.48, 0.56], 'ensemble_tpr_full_spectrum': [0.8, 0.92], 'constat_tpr_non_rl_delta_ge_0.6': [0.55, 0.75], 'dvd_tpr_variant_contamination': [0.5, 0.7], 'equating_spearman_rho': [0.95, 0.99], 'gsm8k_gsm1k_gap_dif_correlation': [0.3, 0.5], 'difficulty_calibration_rho_student_sim': [0.7, 0.82]}\n叙事方向：\"Self-healing benchmark\" story完整成立。DIF是唯一经RL训练不退化的contamination信号， 理论论证（group-level ICC vs within-model distribution）获得经验支持。 Ensemble覆盖全effect-size谱，bifactor equating实现psychometrically等价的benchmark再生。 Headline: \"DIF maintains 70-85% TPR where 10 existing methods degrade to random under RL.\" 三条claims均以full strength呈现，ICLR投稿无需调整framing。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026).\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: 'Apply DIF analysis to METABENCH MMLU response matrix (5,055 models\n    × 12,508 items). Split models into temporal cohorts by release date (pre-2024\n    vs post-2024, plus finer annual splits). Run ETS C DIF detection on all items.\n    Validate against MMLU-CF (ACL 2025) contamination-free items as partial ground\n    truth: items present in MMLU but significantly modified in MMLU-CF should correlate\n    with DIF flags. Sensitivity analysis across different cohort definitions and contamination\n    thresholds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: 'Empirically validate DIF''s RL-robustness claim. Construct two scenarios:\n    (a) cohort with SFT-only models, (b) cohort including RL-trained reasoning models\n    (DeepSeek-R1, Qwen-2.5-RL, etc. from METABENCH or via inference). Run DIF + traditional\n    detectors (Min-K%, ConStat perturbation, DVD) on both scenarios. Show DIF maintains\n    detection power in scenario (b) while traditional detectors degrade. If METABENCH\n    lacks RL-trained models, run inference on 10-15 open-weight RL models on MMLU.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations Depends on 003a and 003b\n    completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond MMLU-CF.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:43:57.967Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:43:57.967Z",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T19:43:57.992Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：DIF在真实数据上复现模拟power，RL-robustness经验验证成功，ensemble三信号互补清晰，equating达到psychometric标准——原始framing完整成立
核心假设：['METABENCH真实cohort size达N≥80且contamination effect sizes在δ≥1.4区间有足够flagged items', 'DIF在real response matrix上的power与模拟一致（非simulation artifact）', 'RL-trained模型cohort的DIF power无显著衰减，而传统detector明确退化至near-random', 'MMLU-CF partial ground truth与DIF flags正相关，提供外部验证', 'ConStat和DVD各自在其target effect-size/model-type区间有效，ensemble互补成立', 'Bifactor IRT equating后replacement items保持rank ordering']
关键指标范围：{'dif_tpr_real_data_delta_ge_1.4': [0.7, 0.85], 'dif_fpr_real_data': [0.02, 0.05], 'mmlu_cf_correlation_with_dif_flags': [0.3, 0.5], 'rl_power_retention_ratio': [0.9, 1.0], 'traditional_detector_auroc_under_rl': [0.48, 0.56], 'ensemble_tpr_full_spectrum': [0.8, 0.92], 'constat_tpr_non_rl_delta_ge_0.6': [0.55, 0.75], 'dvd_tpr_variant_contamination': [0.5, 0.7], 'equating_spearman_rho': [0.95, 0.99], 'gsm8k_gsm1k_gap_dif_correlation': [0.3, 0.5], 'difficulty_calibration_rho_student_sim': [0.7, 0.82]}
叙事方向："Self-healing benchmark" story完整成立。DIF是唯一经RL训练不退化的contamination信号， 理论论证（group-level ICC vs within-model distribution）获得经验支持。 Ensemble覆盖全effect-size谱，bifactor equating实现psychometrically等价的benchmark再生。 Headline: "DIF maintains 70-85% TPR where 10 existing methods degrade to random under RL." 三条claims均以full strength呈现，ICLR投稿无需调整framing。


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
  "promptId": "03b7a80b-afdd-4049-a585-321749630f79",
  "type": "user",
  "uuid": "6ae8829a-e171-435d-9b7d-cd6c2b0a679c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:43:57.991Z_

```json
{
  "parentUuid": "6ae8829a-e171-435d-9b7d-cd6c2b0a679c",
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
  "uuid": "92ccbc09-5027-459d-8333-ff1121d6b6ee",
  "timestamp": "2026-05-20T19:43:57.991Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:43:57.991Z_

```json
{
  "parentUuid": "92ccbc09-5027-459d-8333-ff1121d6b6ee",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "466bd22e-0f7f-418e-bf1c-379dfcac343e",
  "timestamp": "2026-05-20T19:43:57.991Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：DIF在真实数据上复现模拟power，RL-robustness经验验证成功，ensemble三信号互补清晰，equating达到psychometric标准——原始framing完整成立 核心假设：['METABENCH真实cohort size达N≥80且contamination effect size…",
  "leafUuid": "466bd22e-0f7f-418e-bf1c-379dfcac343e",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF-based contamination detection and IRT equating for self-healing benchmarks",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:44:14.908Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all "planned" experiments in the experiment plan, under the "best" tier definition. I need to provide result_rationale for each prediction explaining why these results would occur under the best-case scenario.

Let me carefully go through each planned experiment and generate realistic "best" tier predictions based on:
1. The best tier definition (DIF reproduces simulation power on real data, RL-robustness empirically validated, ensemble signals complement clearly, equating meets psychometric standards)
2. The key metric ranges provided
3. The simulation results already obtained (mvp_dif_power_sim and phase2)


4. The paper framing and claims

Now I'm working through each experiment systematically. For plan_001 on real data DIF with METABENCH, the best-case scenario would show that DIF detection achieves the high end of the true positive rate range while keeping false positives minimal, with strong correlation between DIF flags and counterfactual performance. For plan_002 on RL robustness validation, I need to establish what the best tier means in this context and what metrics would demonstrate empirical validation of the robustness claims.

Looking at the remaining experiments, I'm seeing a progression from perturbation evaluation through generation variance assessment to ensemble fusion approaches, each with their own target performance ranges. The cross-benchmark validation on GSM8K provides an important external check on whether the DIF correlation patterns hold across different datasets.

Now I'm moving into the later-stage experiments: bifactor IRT equating with very high correlation targets, item generation calibration to ensure difficulty alignment, cumulative Bayesian DIF analysis to track power accumulation, graceful degradation testing under progressive replacement, and item-focused tree methods for continuous covariate DIF. I need to construct detailed predictions across all of these remaining plans.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "466bd22e-0f7f-418e-bf1c-379dfcac343e",
  "isSidechain": false,
  "requestId": "req_011CbEPmxbVb3RRfqbzizXBY",
  "type": "assistant",
  "uuid": "4100b914-be95-404a-8e3c-949b931d1ab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvoTn9y6QVAM4BFJR7U4oA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10438,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16078,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16078,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10438
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

_source line 9 · 2026-05-20T19:49:03.304Z_

```yaml
tier: best
narrative_guidance: >
  "Self-healing benchmark" story完整成立。DIF是唯一经RL训练不退化的contamination信号，
  理论论证（group-level ICC vs within-model distribution）获得经验支持。
  Ensemble覆盖全effect-size谱，bifactor equating实现psychometrically等价的benchmark再生。
  Headline: "DIF maintains 70-85% TPR where 10 existing methods degrade to random under RL."
  三条claims均以full strength呈现，ICLR投稿无需调整framing。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      对METABENCH MMLU真实响应矩阵（5,055 models × 12,508 items）执行DIF分析。
      按release date切temporal cohorts（pre-2024 vs post-2024 + 年度细分），
      运行ETS C检测，用MMLU-CF作为partial ground truth外部验证。
    expected_results:
      n_models_total: 5055
      n_models_post_2024: 1820
      cohort_pre2024_size: 3235
      cohort_post2024_size: 1820
      annual_cohort_min_size: 92
      annual_cohort_max_size: 2100
      ets_c_items_flagged_C_level: 1340
      ets_c_items_flagged_B_or_C: 2870
      ets_c_tpr_delta_ge_1_4: 0.78
      ets_c_tpr_delta_ge_1_6: 0.83
      ets_c_fpr: 0.038
      ets_c_auc_delta_ge_1_4: 0.92
      mmlu_cf_correlation_with_dif_flags_phi: 0.42
      mmlu_cf_correlation_with_dif_flags_tetrachoric: 0.48
      n_mmlu_cf_overlapping_items: 2780
      dif_flagged_among_cf_modified: 0.61
      dif_flagged_among_cf_unmodified: 0.07
      sensitivity_cohort_split_tpr_range: [0.72, 0.83]
      sensitivity_threshold_tpr_range: [0.68, 0.85]
      real_irt_param_a_mean: 1.18
      real_irt_param_b_mean: -0.79
      real_irt_param_a_std: 0.42
    result_rationale: >
      Phase 2模拟已在N=100/δ=1.6条件下达到TPR=0.7966，真实参数（a_mean=1.2, b_mean=-0.84）
      与模拟设定高度一致。Best档下真实数据复现模拟power的核心条件是：(1) METABENCH post-2024
      cohort达到N≈1820，远超模拟的N=100下限，提供充足统计功效；(2) 真实contamination
      effect sizes在高频benchmark如MMLU上确实存在δ≥1.4的大效应——GSM1K研究已证实10-13pp
      的accuracy gap，对应IRT尺度上δ≈1.5-2.0；(3) ETS C基于effect-size阈值而非p-value，
      大样本下不会出现inflation问题，反而因estimation precision提高而TPR略优于模拟。
      MMLU-CF验证的phi=0.42反映了partial ground truth的本质局限——CF修改的items与真正
      contaminated items有交集但不完全重叠，CF修改了部分未被contaminate的items（降低相关），
      同时未修改一些实际被contaminate的items。但0.42的phi系数在psychometric validation中
      已属中等偏强，足以作为convergent validity evidence。FPR=0.038与模拟的0.036-0.042
      区间一致，因为false positive rate主要由ETS C的Δ_MH阈值决定，不依赖sample size。
    tables:
      - title: "Table 1: DIF Detection Power on METABENCH MMLU Real Data"
        columns: [cohort_split, N_focal, N_ref, delta_range, TPR, FPR, AUC]
        rows:
          - [pre2024_vs_post2024, 1820, 3235, "≥1.4", 0.78, 0.038, 0.92]
          - [pre2024_vs_post2024, 1820, 3235, "≥1.6", 0.83, 0.038, 0.94]
          - [pre2024_vs_post2024, 1820, 3235, "≥1.0", 0.51, 0.041, 0.83]
          - [2022_vs_2024, 920, 2100, "≥1.4", 0.76, 0.036, 0.91]
          - [2023_vs_2025, 680, 1340, "≥1.4", 0.74, 0.039, 0.90]
          - [annual_finest, 92, 2100, "≥1.4", 0.72, 0.042, 0.88]
      - title: "Table 2: MMLU-CF External Validation"
        columns: [category, n_items, dif_flagged_rate, description]
        rows:
          - [CF_modified_items, 2780, 0.61, "Items significantly changed in MMLU-CF"]
          - [CF_unmodified_items, 9728, 0.07, "Items unchanged in MMLU-CF"]
          - [phi_coefficient, null, 0.42, "Association between DIF flag and CF modification"]
          - [tetrachoric_r, null, 0.48, "Latent correlation estimate"]
    figures_description:
      - "Figure 1: Heatmap of ETS C Δ_MH values across 12,508 MMLU items, ordered by subject. Clear clustering of large-DIF items in STEM subjects (math, CS, physics) that are more likely contaminated through code training data."
      - "Figure 2: ROC curves comparing DIF detection at different cohort splits. Curves are tightly clustered (AUC range 0.88-0.94), demonstrating robustness to arbitrary cohort boundary choice."
      - "Figure 3: Scatter plot of DIF Δ_MH magnitude vs MMLU-CF modification indicator. Violin plots showing clear separation between CF-modified (higher DIF) and CF-unmodified items."
    analysis: >
      真实数据DIF检测power与Phase 2模拟高度一致，验证了模拟参数设定的生态效度。
      关键发现：(1) MMLU上约10.7%的items呈现ETS C级DIF，集中在STEM领域，与contamination
      through pretraining code data的预期一致；(2) MMLU-CF外部验证提供convergent evidence，
      phi=0.42虽非完美但在partial ground truth条件下合理——完美相关本身不可信，因为CF的
      modification策略与contamination并非一一对应；(3) 敏感性分析显示TPR在不同cohort
      定义下稳定在0.72-0.83区间，最弱的annual finest split（N_focal=92）仍达0.72，
      正好符合Phase 2模拟在N=80条件下的预测。这一结果直接支持Claim 1的real-data validation。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      经验验证DIF的RL-robustness。构建SFT-only cohort和含RL-trained模型的cohort，
      同时运行DIF与传统检测器（Min-K%、ConStat perturbation、DVD），对比RL条件下的退化。
    expected_results:
      n_rl_models_evaluated: 14
      n_sft_models_evaluated: 40
      rl_models_list: >
        DeepSeek-R1, DeepSeek-R1-Distill-{7B,14B,32B,70B}, Qwen2.5-RL-{7B,72B},
        Llama-3.1-Nemotron-Ultra-253B, QwQ-32B, Skywork-OR1-{8B,32B}, K1.5-Chat,
        Eurus-2-7B-PRIME, OpenThinker-7B
      dif_tpr_sft_cohort_delta_ge_1_4: 0.79
      dif_tpr_rl_cohort_delta_ge_1_4: 0.76
      dif_power_retention_ratio: 0.96
      dif_fpr_sft_cohort: 0.037
      dif_fpr_rl_cohort: 0.041
      mink_auroc_sft: 0.72
      mink_auroc_rl: 0.51
      mink_degradation_pp: 21
      constat_auroc_sft: 0.68
      constat_auroc_rl: 0.53
      constat_degradation_pp: 15
      dvd_auroc_sft: 0.65
      dvd_auroc_rl: 0.54
      dvd_degradation_pp: 11
      perplexity_auroc_sft: 0.61
      perplexity_auroc_rl: 0.50
      lowercase_auroc_sft: 0.58
      lowercase_auroc_rl: 0.49
      traditional_mean_auroc_sft: 0.65
      traditional_mean_auroc_rl: 0.51
      p_value_dif_retention_paired_t: 0.62
      p_value_traditional_degradation_paired_t: 0.0003
    result_rationale: >
      DIF的RL-robustness源于其检测机制的根本差异。传统检测器（Min-K%、perplexity-based）
      依赖within-model output distributions——GRPO/PPO通过policy smoothing将memorized items
      的output distribution调整到与clean items相似，消除可检测的distributional anomaly。
      Wang et al. (ICLR 2026)已实证证明这种退化：~156 GRPO steps即可将多数检测器降至
      near-random。DIF则完全不同：它比较的是group-level Item Characteristic Curves——
      "给定相同latent ability θ，focal group（post-training cohort）在item j上的correct
      probability是否高于reference group"。RL训练可以smooth output token distributions，
      但无法消除behavioral fact："这个模型答对了这道它memorized的题"。除非RL训练能让模型
      在memorized items上故意答错（这会negate contamination的目的），否则group-level
      behavioral pattern必然保留。Power retention ratio=0.96（而非1.0）的微小衰减来自
      RL模型通常具有更高的general ability θ，这略微压缩了DIF effect size的估计——但这是
      统计层面的minor attenuation，不是mechanistic failure。传统检测器的AUROC从0.65降至
      0.51（mean across methods），与Wang et al.报告的14-20pp退化一致。
    tables:
      - title: "Table 3: DIF vs Traditional Detectors Under RL Training"
        columns: [method, auroc_sft_cohort, auroc_rl_cohort, degradation_pp, p_value]
        rows:
          - [DIF_ETS_C, 0.91, 0.90, 1, 0.62]
          - [Min-K%, 0.72, 0.51, 21, 0.0002]
          - [ConStat_perturbation, 0.68, 0.53, 15, 0.001]
          - [DVD_generation_var, 0.65, 0.54, 11, 0.004]
          - [Perplexity, 0.61, 0.50, 11, 0.003]
          - [Lowercase, 0.58, 0.49, 9, 0.008]
          - [zlib_ratio, 0.60, 0.50, 10, 0.005]
          - [Top-K_prob, 0.63, 0.52, 11, 0.003]
          - [Ref_model_loss, 0.67, 0.53, 14, 0.002]
          - [Neighbor_text, 0.59, 0.50, 9, 0.007]
          - [DetectGPT, 0.55, 0.49, 6, 0.04]
      - title: "Table 4: DIF Power Retention by RL Training Intensity"
        columns: [model_group, n_models, dif_tpr_delta_ge_1_4, dif_fpr, retention_vs_sft]
        rows:
          - [SFT_only, 40, 0.79, 0.037, 1.00]
          - [Light_RL_under_500_steps, 6, 0.78, 0.039, 0.99]
          - [Heavy_RL_over_500_steps, 8, 0.75, 0.041, 0.95]
          - [All_RL, 14, 0.76, 0.041, 0.96]
    figures_description:
      - "Figure 4: Bar chart comparing AUROC of 11 detection methods on SFT vs RL cohorts. DIF bar is near-identical height; all others show clear drops. Error bars from bootstrap."
      - "Figure 5: Scatter plot of DIF Δ_MH estimated on SFT cohort vs RL cohort for same items. Points cluster tightly along the diagonal (r=0.94), demonstrating effect size stability."
      - "Figure 6: Conceptual diagram contrasting DIF's group-level ICC mechanism vs within-model distribution-based detectors, illustrating why RL smoothing affects the latter but not the former."
    analysis: >
      RL-robustness经验验证是论文最核心的卖点。DIF power retention ratio=0.96意味着
      RL训练对DIF检测力几乎无影响（paired t-test p=0.62，无统计显著差异），而10种传统
      检测器平均退化14pp至near-random（mean AUROC=0.51）。这直接验证了理论预测：
      DIF操作在group-level behavioral space，RL无法在不放弃contamination benefit的
      情况下消除这一信号。Heavy RL（>500 steps）组的轻微衰减（retention=0.95）可归因于
      更高general ability导致的effect size estimation compression，而非mechanism failure。
      这一结果使headline claim成立："DIF maintains 76% TPR where 10 existing methods
      degrade to random under RL training."

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      独立评估ConStat-style perturbation testing在MMLU上的检测力，
      生成200+ items的语义等价改写，比较原始vs改写表现，刻画effect size谱上的检测力。
    expected_results:
      n_items_reformulated: 240
      n_models_tested: 35
      n_reformulations_per_item: 5
      constat_tpr_non_rl_delta_ge_0_6: 0.68
      constat_tpr_non_rl_delta_ge_1_0: 0.74
      constat_tpr_non_rl_delta_ge_1_4: 0.62
      constat_tpr_rl_delta_ge_0_6: 0.31
      constat_tpr_rl_delta_ge_1_0: 0.38
      constat_fpr_non_rl: 0.06
      constat_fpr_rl: 0.08
      constat_fdr_controlled_alpha_0_05: 0.048
      mean_accuracy_drop_contaminated_items: 0.18
      mean_accuracy_drop_clean_items: 0.03
      reformulation_semantic_similarity: 0.91
    result_rationale: >
      ConStat的检测逻辑是：contaminated models在original items上表现异常好，但在
      semantically equivalent reformulations上表现回落——因为memorization是surface-form
      specific的。在non-RL models上，这一逻辑有效：SFT训练的memorization直接绑定到
      token sequences，reformulation打破了这种绑定，导致contaminated items上出现显著
      accuracy drop（mean=0.18 vs clean items的0.03）。TPR在δ≥0.6时达0.68，因为即使
      中等效应的contamination也会在perturbation下暴露。但在δ≥1.4时TPR反而降到0.62，
      因为极大effect size的items通常是extremely easy items（即使不contaminate也正确率高），
      reformulation后的drop较小。ConStat在RL模型上急剧退化（TPR从0.68降至0.31），因为
      GRPO/PPO的policy optimization使模型学会了更general的answer patterns而非
      surface-form memorization——RL模型在reformulated items上的accuracy drop较小，
      使perturbation signal模糊化。这正是ConStat在ensemble中的定位：覆盖non-RL models的
      medium effect sizes（DIF在δ<1.0时power不足），但在RL场景下需要DIF补位。
    tables:
      - title: "Table 5: ConStat Detection Power by Effect Size and Model Type"
        columns: [model_type, delta_range, n_items, TPR, FPR, FDR]
        rows:
          - [non_RL, "≥0.6", 142, 0.68, 0.06, 0.048]
          - [non_RL, "≥1.0", 87, 0.74, 0.06, 0.041]
          - [non_RL, "≥1.4", 48, 0.62, 0.06, 0.052]
          - [RL, "≥0.6", 142, 0.31, 0.08, 0.12]
          - [RL, "≥1.0", 87, 0.38, 0.08, 0.10]
          - [all_models, "≥0.6", 142, 0.52, 0.07, 0.07]
    figures_description:
      - "Figure 7: Paired accuracy comparison (original vs reformulated) for contaminated vs clean items, split by model type (SFT vs RL). Clear separation for SFT, collapsed for RL."
      - "Figure 8: ConStat detection power curve across effect size spectrum, overlaid with DIF power curve. Crossover around δ≈1.0 shows complementary regions."
    analysis: >
      ConStat在non-RL模型上的medium-effect-size检测力（δ≥0.6: TPR=0.68）验证了其在
      ensemble中的角色——填补DIF在small-to-medium effects上的盲区。RL条件下的急剧退化
      （TPR从0.68→0.31）与Wang et al.的发现一致，因为perturbation sensitivity本质上仍
      依赖于surface-form specific memorization pattern，RL训练将其平滑化。FDR控制在
      non-RL条件下有效（0.048 < 0.05），但RL条件下FDR升至0.12，需在ensemble中对RL模型
      降低ConStat权重。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      独立评估DVD generation variance在MMLU上的检测力，对10-15个open-weight模型
      每item生成50次response，计算generation variance分数，检测bimodal distributions。
    expected_results:
      n_models_evaluated: 12
      n_items_evaluated: 2000
      responses_per_item: 50
      temperature_range: [0.7, 1.0]
      dvd_tpr_variant_contamination: 0.65
      dvd_tpr_verbatim_contamination: 0.38
      dvd_tpr_all_contamination: 0.52
      dvd_fpr: 0.07
      dvd_auroc_variant: 0.78
      dvd_auroc_verbatim: 0.62
      dvd_auroc_overall: 0.71
      bimodal_detection_rate_contaminated: 0.58
      bimodal_detection_rate_clean: 0.04
      dvd_tpr_rl_variant: 0.47
      dvd_tpr_rl_verbatim: 0.29
      generation_variance_contaminated_mean: 0.31
      generation_variance_clean_mean: 0.12
    result_rationale: >
      DVD的检测逻辑基于generation variance：contaminated models在memorized items上的
      generation distribution呈现bimodal pattern——当temperature sampling触发"recall"
      mode时high confidence输出memorized answer，否则回到general reasoning mode。
      Variant contamination（模型见过item的变体而非原始形式）下DVD最有效（TPR=0.65），
      因为variant exposure创造了partial memorization——模型"几乎记得"答案，导致生成
      在confident recall和uncertain reasoning之间振荡，产生高variance和清晰的bimodality。
      Verbatim contamination下DVD效果较差（TPR=0.38），因为完全memorized items的生成
      variance反而很低（模型每次都确信地输出相同答案），bimodal signal消失。这使DVD与DIF
      形成互补：DIF在verbatim large effects上最强，DVD在variant contamination上最强。
      RL条件下DVD退化到TPR=0.47（variant），因为GRPO smoothing降低了generation variance
      的discriminability，但退化幅度小于ConStat（因为DVD利用的是sampling-level variance
      而非perturbation sensitivity，RL对sampling variance的影响弱于对perturbation
      response的影响）。
    tables:
      - title: "Table 6: DVD Detection Power by Contamination Type"
        columns: [contamination_type, model_type, n_items, TPR, FPR, AUROC]
        rows:
          - [variant, non_RL, 320, 0.65, 0.07, 0.78]
          - [verbatim, non_RL, 480, 0.38, 0.07, 0.62]
          - [all, non_RL, 800, 0.52, 0.07, 0.71]
          - [variant, RL, 320, 0.47, 0.09, 0.68]
          - [verbatim, RL, 480, 0.29, 0.09, 0.57]
          - [all, RL, 800, 0.38, 0.09, 0.63]
    figures_description:
      - "Figure 9: Distribution of generation variance scores for contaminated (variant vs verbatim) and clean items. Variant contamination shows clear right shift; verbatim shows compressed distribution."
      - "Figure 10: Bimodality coefficient heatmap across items and models, with contamination status overlay. Clear bimodal clusters for variant-contaminated items."
    analysis: >
      DVD填补了ensemble中的variant contamination盲区。DIF主要检测verbatim large effects
      （模型在original item上的behavioral anomaly），ConStat检测non-RL medium effects，
      DVD则捕获variant contamination——模型见过类似但不完全相同的items，产生partial
      memorization的generation variance signal。三者的complementary coverage pattern
      在best档下清晰呈现，为ensemble fusion提供了solid foundation。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      融合DIF + ConStat + DVD为multi-signal ensemble。校准per-signal阈值，
      评估majority voting和weighted fusion，展示ensemble coverage覆盖全effect-size谱。
    expected_results:
      ensemble_tpr_full_spectrum: 0.87
      ensemble_tpr_delta_ge_1_4: 0.91
      ensemble_tpr_delta_ge_1_0: 0.85
      ensemble_tpr_delta_ge_0_6: 0.78
      ensemble_fpr: 0.08
      ensemble_auroc: 0.93
      majority_2of3_tpr: 0.72
      majority_2of3_fpr: 0.04
      weighted_fusion_tpr: 0.87
      weighted_fusion_fpr: 0.08
      dif_unique_detections_pct: 0.28
      constat_unique_detections_pct: 0.15
      dvd_unique_detections_pct: 0.12
      all_three_overlap_pct: 0.31
      two_signal_overlap_pct: 0.14
      ensemble_tpr_rl_models: 0.82
      ensemble_tpr_non_rl_models: 0.90
      optimal_weights_dif: 0.45
      optimal_weights_constat: 0.30
      optimal_weights_dvd: 0.25
    result_rationale: >
      Ensemble的power来源于三信号的systematic complementarity。在best档下，每个信号
      覆盖不同的effect-size × model-type区间：DIF覆盖large effects（δ≥1.4）且RL-robust，
      ConStat覆盖non-RL medium effects（δ≥0.6），DVD覆盖variant contamination。
      Weighted fusion（DIF=0.45, ConStat=0.30, DVD=0.25）优于majority voting
      （TPR 0.87 vs 0.72），因为majority voting要求至少2/3信号agree，而在信号覆盖不
      重叠的区间（如RL+large effect只有DIF有效），single-signal detection被majority
      voting过滤掉。Weighted fusion允许high-confidence single signal触发detection。
      Full-spectrum TPR=0.87的构成：δ≥1.4区间DIF主导（TPR=0.91），δ=0.6-1.4区间ConStat
      补位（将DIF单独的~0.40 TPR提升到ensemble的0.78），variant contamination区间DVD
      补位（unique detections 12%）。FPR=0.08略高于single-signal的0.04-0.07，这是
      multi-signal fusion的inherent trade-off——更多信号意味着更多false positive
      opportunities，但0.08仍在可接受范围内。RL模型上ensemble TPR=0.82（vs non-RL的0.90），
      差距来自ConStat在RL条件下的退化被DIF的RL-robustness部分补偿。
    tables:
      - title: "Table 7: Ensemble vs Individual Signal Detection Power"
        columns: [method, tpr_full, tpr_ge_1_4, tpr_ge_0_6, fpr, auroc]
        rows:
          - [DIF_only, 0.58, 0.78, 0.35, 0.038, 0.84]
          - [ConStat_only, 0.44, 0.62, 0.68, 0.06, 0.76]
          - [DVD_only, 0.38, 0.38, 0.45, 0.07, 0.71]
          - [Majority_2of3, 0.72, 0.81, 0.64, 0.04, 0.89]
          - [Weighted_fusion, 0.87, 0.91, 0.78, 0.08, 0.93]
      - title: "Table 8: Signal Complementarity Analysis"
        columns: [detection_source, pct_of_total_detections, example_regime]
        rows:
          - [DIF_unique, 0.28, "Large effect + RL models"]
          - [ConStat_unique, 0.15, "Medium effect + non-RL models"]
          - [DVD_unique, 0.12, "Variant contamination"]
          - [DIF_and_ConStat, 0.08, "Large effect + non-RL"]
          - [DIF_and_DVD, 0.04, "Large variant + RL"]
          - [ConStat_and_DVD, 0.02, "Medium variant + non-RL"]
          - [All_three, 0.31, "Large effect + non-RL + verbatim"]
    figures_description:
      - "Figure 11: Venn diagram of detections by three signals, showing complementary coverage with ~45% items detected by only one or two signals."
      - "Figure 12: Detection power heatmap across effect-size (δ) × model-type (SFT/RL) × contamination-type (verbatim/variant) grid. Each cell colored by which signal(s) contribute most."
      - "Figure 13: Precision-recall curves for individual signals vs ensemble. Ensemble dominates at all recall levels."
    analysis: >
      Ensemble coverage分析是Claim 2的核心evidence。三信号互补的清晰pattern——
      DIF覆盖RL+large effects，ConStat覆盖non-RL+medium effects，DVD覆盖variant
      contamination——使full-spectrum TPR从任何单信号的最高0.58提升到0.87。
      关键是unique detections分析：每个信号贡献12-28%的独占检测，证明任何单信号都不可替代。
      Weighted fusion优于majority voting 15pp，反映了信号互补性超过信号冗余性——
      在most detection regimes下只有1-2个信号active，majority voting的"2-of-3 agreement"
      要求过于保守。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      在GSM8K上复制DIF分析，用GSM1K作为contamination ground truth。
      收集50+模型的per-item binary responses，运行temporal cohort DIF，
      将DIF flags与per-model GSM8K-GSM1K accuracy gap关联。
    expected_results:
      n_models_gsm8k: 62
      n_items_gsm8k: 1319
      n_items_gsm1k: 1250
      cohort_pre2024_n: 28
      cohort_post2024_n: 34
      dif_flagged_items_gsm8k: 178
      dif_flagged_rate: 0.135
      dif_tpr_gsm8k_delta_ge_1_4: 0.74
      dif_fpr_gsm8k: 0.042
      gsm8k_gsm1k_gap_mean_all_models: 0.068
      gsm8k_gsm1k_gap_mean_contaminated_models: 0.112
      gsm8k_gsm1k_gap_mean_clean_models: 0.024
      gsm8k_gsm1k_gap_dif_correlation_spearman: 0.43
      gsm8k_gsm1k_gap_dif_correlation_pearson: 0.38
      per_item_dif_vs_gap_correlation: 0.41
      gsm8k_dif_auc: 0.88
    result_rationale: >
      GSM8K是ideal validation target因为GSM1K提供了independent contamination ground truth——
      GSM1K是GSM8K的分布匹配但全新的test set，GSM8K-GSM1K accuracy gap直接反映
      contamination benefit。DIF在GSM8K上的TPR=0.74（vs MMLU的0.78）略低，因为：
      (1) 样本量较小（62 models vs MMLU的5055），cohort sizes（28 vs 34）接近power
      下限；(2) GSM8K是math reasoning benchmark，item discrimination更依赖reasoning
      ability而非factual recall，DIF effect sizes分布略低于MMLU。Spearman rho=0.43
      between per-model DIF flag count和GSM8K-GSM1K gap是中等相关，因为DIF flags是
      binary item-level indicators而GSM8K-GSM1K gap是continuous model-level metric，
      二者在aggregation level上不同——item-level DIF flag到model-level gap的mapping
      需要通过contamination load（模型见过的flagged items数量）mediating。直接的
      per-item correlation（item的DIF flag vs 该item的across-model gap）达到0.41，
      提供convergent evidence。这一跨benchmark验证支持DIF检测的generalizability，
      不仅限于MMLU。
    tables:
      - title: "Table 9: DIF Detection on GSM8K with GSM1K Ground Truth"
        columns: [metric, value]
        rows:
          - [n_models, 62]
          - [n_items, 1319]
          - [DIF_flagged_items, 178]
          - [DIF_flagged_rate, 0.135]
          - [TPR_delta_ge_1_4, 0.74]
          - [FPR, 0.042]
          - [AUC, 0.88]
          - [GSM8K-GSM1K_gap_DIF_corr_spearman, 0.43]
      - title: "Table 10: GSM8K-GSM1K Gap by Model Contamination Status"
        columns: [model_group, n_models, mean_gap, std_gap, median_gap]
        rows:
          - [DIF_high_contamination, 18, 0.112, 0.034, 0.105]
          - [DIF_low_contamination, 22, 0.051, 0.028, 0.047]
          - [DIF_clean, 22, 0.024, 0.019, 0.020]
    figures_description:
      - "Figure 14: Scatter plot of per-model DIF contamination load (count of flagged items answered correctly) vs GSM8K-GSM1K accuracy gap. Positive trend with Spearman ρ=0.43."
      - "Figure 15: Item-level DIF magnitude (Δ_MH) distribution on GSM8K, overlaid with GSM1K-based ground truth labels."
    analysis: >
      跨benchmark验证成功，DIF在GSM8K上的检测力（TPR=0.74）与MMLU结果一致（考虑到
      较小样本量下的预期衰减）。GSM8K-GSM1K gap与DIF flags的spearman rho=0.43提供了
      独立于MMLU-CF的external validation，使用完全不同的ground truth来源。
      13.5%的GSM8K items被flagged，与Mirzadeh et al. (NeurIPS 2024)报告的GSM8K
      contamination prevalence一致。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      在METABENCH MMLU数据上pilot bifactor IRT equating。拟合bifactor model
      （general factor + subject-specific factors），选择anchor items，
      通过fixed-parameter calibration校准replacement items，验证equated score等价性。
    expected_results:
      bifactor_model_converged: true
      n_general_factor_loadings_gt_0_3: 11200
      n_subject_factors: 57
      subject_factor_loading_mean: 0.42
      general_factor_loading_mean: 0.58
      general_factor_variance_explained: 0.48
      total_variance_explained: 0.72
      n_anchor_items_selected: 3100
      anchor_item_criteria: "No DIF (ETS A), discrimination a>0.8, low missingness"
      anchor_item_stability_rho: 0.98
      n_replacement_items_calibrated: 500
      equating_spearman_rho: 0.97
      equating_pearson_r: 0.96
      equating_rank_displacement_mean: 1.8
      equating_rank_displacement_max: 12
      equating_score_rmse: 0.021
      equating_classification_agreement: 0.94
      chi_square_equating_test_p: 0.34
      anchor_item_dif_free_rate: 0.92
      replacement_item_factor_loading_corr: 0.88
    result_rationale: >
      Bifactor model在MMLU上的良好拟合源于MMLU的psychometric structure：它是multi-subject
      benchmark，每个subject（57个）构成一个specific factor，同时存在general cognitive
      ability factor（因为performance across subjects是正相关的——general intelligence
      drives cross-domain performance）。General factor解释48%方差，与educational
      testing中的typical bifactor results一致。Anchor items（3100个，~25%）是高稳定性、
      无DIF的items——在temporal cohorts间parameter estimates一致，表明未被contaminate。
      25%的anchor rate在psychometric equating中是standard practice（Kolen & Brennan
      推荐20-30%）。Equating后的Spearman rho=0.97表明模型rankings在original vs
      replaced benchmark间高度保持——rank displacement mean=1.8意味着平均每个模型只
      移动1-2个排名位置。这一精度来自fixed-parameter calibration的mechanics：
      replacement items的parameters在anchor item scale上calibrate，数学上保证了
      score comparability（up to estimation error）。Score RMSE=0.021（在0-1 scale上）
      反映estimation uncertainty而非systematic bias。Chi-square equating test p=0.34
      表明无法拒绝"equated scores等价于original scores"的null hypothesis，即equating
      在统计上成功。
    tables:
      - title: "Table 11: Bifactor Model Fit Statistics"
        columns: [metric, value]
        rows:
          - [RMSEA, 0.028]
          - [CFI, 0.96]
          - [TLI, 0.95]
          - [General_factor_variance_pct, 0.48]
          - [Subject_factors_variance_pct, 0.24]
          - [Total_variance_explained, 0.72]
          - [N_subjects_factors, 57]
      - title: "Table 12: Equating Results — Original vs Replaced Benchmark"
        columns: [metric, value, interpretation]
        rows:
          - [Spearman_rho, 0.97, "Rankings nearly identical"]
          - [Pearson_r, 0.96, "Scores linearly related"]
          - [RMSE, 0.021, "Minimal score displacement"]
          - [Mean_rank_displacement, 1.8, "Average 1-2 rank positions"]
          - [Max_rank_displacement, 12, "Worst case still within noise"]
          - [Classification_agreement, 0.94, "94% same performance tier"]
          - [Chi_sq_test_p, 0.34, "Cannot reject equivalence"]
    figures_description:
      - "Figure 16: Scatter plot of model scores on original vs equated benchmark (500 items replaced). Points tightly clustered along diagonal with Pearson r=0.96."
      - "Figure 17: Bifactor model path diagram for top-5 MMLU subjects showing general and subject-specific factor loadings."
      - "Figure 18: Rank displacement distribution — right-skewed with most models displaced by 0-3 positions."
    analysis: >
      Bifactor IRT equating在MMLU上达到psychometric standard（rho=0.97, RMSE=0.021），
      证明了Claim 3的可行性——contaminated items可以被replaced而preserving benchmark
      comparability。关键支撑是25% anchor items提供了stable calibration bridge，
      bifactor structure正确捕获了MMLU的multi-subject + general ability structure。
      Classification agreement=0.94意味着在实际的model evaluation场景中，equated
      benchmark与original benchmark在94%的模型对比决策上给出相同结论。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      生成replacement items并通过student simulation校准。对比prompt-based difficulty
      targeting与empirical calibration的精度。在holdout model panel上验证。
    expected_results:
      n_items_generated: 500
      n_items_passing_quality_filter: 420
      quality_filter_pass_rate: 0.84
      n_student_sim_models: 8
      student_sim_responses_per_item: 200
      difficulty_rho_student_sim: 0.78
      difficulty_rho_prompt_targeting: 0.28
      difficulty_rmse_student_sim: 0.14
      difficulty_rmse_prompt_targeting: 0.38
      discrimination_rho_student_sim: 0.62
      discrimination_rho_prompt_targeting: 0.15
      holdout_panel_equating_rho: 0.95
      construct_validity_factor_loading_corr: 0.85
      subject_match_accuracy: 0.92
      cognitive_level_match_accuracy: 0.78
      item_format_compliance: 0.97
    result_rationale: >
      Student simulation校准（基于arXiv 2601.09953方法）的核心优势是empirical——
      它通过让diverse student models实际回答generated items来estimate difficulty，
      而非依赖LLM的self-report。rho=0.78与原论文报告的r=0.75-0.82一致，因为MMLU
      的MCQ format与student simulation的optimal use case对齐（forced-choice items
      比open-ended items更适合binary response modeling）。Prompt-based targeting
      的rho=0.28与arXiv 2602.06631报告的rho=0.10-0.45一致——LLMs在内省difficulty
      时系统性地低估hard items、高估easy items，因为difficulty perception与generation
      capability不同。Student simulation的优势在于它bypasses这种miscalibration，
      直接从behavioral responses estimate difficulty。Discrimination的rho=0.62较低
      于difficulty的0.78，因为discrimination是IRT的second-order parameter（item
      sensitivity to ability differences），inherently harder to control through
      generation——它依赖item的specific cognitive demands，而这些难以通过prompt
      engineering精确控制。Construct validity factor loading correlation=0.85表明
      generated items load on相同的subject-specific factors，preserving MMLU的
      bifactor structure。
    tables:
      - title: "Table 13: Calibration Method Comparison"
        columns: [method, difficulty_rho, difficulty_rmse, discrimination_rho, n_items]
        rows:
          - [Student_simulation, 0.78, 0.14, 0.62, 420]
          - [Prompt_targeting, 0.28, 0.38, 0.15, 420]
          - [Random_baseline, 0.05, 0.52, 0.03, 420]
      - title: "Table 14: Generated Item Quality Metrics"
        columns: [metric, value]
        rows:
          - [Quality_filter_pass_rate, 0.84]
          - [Subject_match_accuracy, 0.92]
          - [Cognitive_level_match, 0.78]
          - [Format_compliance, 0.97]
          - [Factor_loading_corr, 0.85]
          - [Holdout_equating_rho, 0.95]
    figures_description:
      - "Figure 19: Scatter plot of estimated vs true difficulty for student simulation (rho=0.78) and prompt targeting (rho=0.28). Student simulation points cluster near diagonal; prompt targeting shows systematic bias."
      - "Figure 20: Factor loading comparison between original and generated items on same MMLU subjects. High correspondence (r=0.85) confirms construct preservation."
    analysis: >
      Student simulation校准是item regeneration pipeline的关键enabler，将difficulty
      estimation精度从prompt-based的rho=0.28提升到0.78——接近3x improvement。
      这一结果支持Claim 3的"empirically calibrated alternatives"承诺。Holdout panel
      equating rho=0.95达到psychometric standard，证明end-to-end pipeline（generation →
      simulation calibration → equating）可以produce functionally equivalent benchmark items。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      实现Bayesian累积DIF先验。模拟4次连续benchmark administration，
      展示evidence accumulation带来的power提升。
    expected_results:
      n_administrations_simulated: 4
      n_models_per_administration: 40
      admin_1_power_medium_delta_1_0: 0.38
      admin_2_cumulative_power: 0.55
      admin_3_cumulative_power: 0.70
      admin_4_cumulative_power: 0.78
      power_gain_per_administration: [0.38, 0.17, 0.15, 0.08]
      bayesian_bf_threshold: 3.0
      false_discovery_rate: 0.04
      convergence_rate: 0.98
      prior_posterior_shrinkage: 0.42
      credible_interval_width_admin1: 0.68
      credible_interval_width_admin4: 0.31
    result_rationale: >
      Bayesian累积先验的power gain来自evidence accumulation的数学性质——每次新的
      administration提供independent observations，posterior distribution随data收窄。
      从single administration的0.38到4次累积的0.78，power nearly doubles。Gain是
      diminishing的（0.17→0.15→0.08），因为posterior precision的improvement是
      sub-linear in sample size（~√n scaling）。对medium effects（δ=1.0）这尤其重要，
      因为classical DIF在single administration with N=40 per cohort时power不足
      （Phase 2模拟显示N=50/δ=1.0时TPR仅0.04-0.07）。Bayesian approach通过
      accumulating evidence across time解决了这个sample-size limitation——每次
      administration贡献40个models，4次累积相当于effective sample of ~160，
      但通过informative priors获得比simple pooling更高的statistical efficiency。
      BF threshold=3.0（moderate evidence）对应psychometric practice中的standard
      decision criterion。FDR=0.04 < 0.05表明error control有效。
    tables:
      - title: "Table 15: Cumulative Bayesian DIF Power Over Administrations"
        columns: [administration, cumulative_n, power_delta_1_0, power_delta_1_4, CI_width]
        rows:
          - [1, 40, 0.38, 0.62, 0.68]
          - [2, 80, 0.55, 0.76, 0.48]
          - [3, 120, 0.70, 0.84, 0.37]
          - [4, 160, 0.78, 0.88, 0.31]
    figures_description:
      - "Figure 21: Power accumulation curves across 4 administrations for δ=0.6, 1.0, 1.4. All show diminishing returns but substantial gains."
      - "Figure 22: Posterior distribution evolution for a representative DIF-flagged item across 4 administrations, showing progressive shrinkage toward true effect."
    analysis: >
      Bayesian累积DIF直接回应reviewer concern #2（sample sizes too small）。
      4次累积后medium-effect power从0.38→0.78，使DIF对medium effects也实用化。
      这一结果支持论文的"living benchmark"叙事——不需要一次性获得大样本，
      可以通过temporal accumulation逐步建立detection confidence。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      分析benchmark在progressive item replacement下的validity degradation。
      定义validity metrics，模拟5%-50% replacement，建立理论bounds。
    expected_results:
      replacement_rates: [0.05, 0.10, 0.20, 0.50]
      ranking_stability_rho_5pct: 0.99
      ranking_stability_rho_10pct: 0.97
      ranking_stability_rho_20pct: 0.95
      ranking_stability_rho_50pct: 0.89
      score_reliability_alpha_original: 0.94
      score_reliability_alpha_5pct: 0.93
      score_reliability_alpha_10pct: 0.93
      score_reliability_alpha_20pct: 0.91
      score_reliability_alpha_50pct: 0.87
      construct_coverage_jaccard_5pct: 0.98
      construct_coverage_jaccard_10pct: 0.96
      construct_coverage_jaccard_20pct: 0.92
      construct_coverage_jaccard_50pct: 0.83
      theoretical_rho_lower_bound_formula: "rho >= 1 - k*replacement_rate*(1-r_replacement)"
      theoretical_rho_lower_bound_20pct: 0.93
      empirical_rho_20pct: 0.95
      validity_threshold_replacement_rate: 0.35
    result_rationale: >
      Graceful degradation的数学基础是：如果replacement items与original items测量相同
      construct（通过bifactor equating保证），且parameter estimation是unbiased的，
      那么benchmark score的perturbation仅来自estimation error。Ranking stability
      (Spearman rho)随replacement rate的下降是approximately linear的：5%→0.99,
      10%→0.97, 20%→0.95, 50%→0.89。0.95 threshold（psychometric standard for
      "essentially equivalent"）在~20% replacement rate时hit——这意味着可以替换
      最多20%的items（~2500 items on MMLU）while maintaining psychometrically equivalent
      rankings。50% replacement导致rho=0.89，仍然usable但not equivalent。
      Score reliability (Cronbach's alpha)从0.94降至0.91 at 20%，因为replacement
      items的discrimination estimates有更大variance（calibration uncertainty），
      but alpha>0.90在psychometric standards中仍属excellent。Construct coverage
      (Jaccard similarity of subject factor coverage)在20%时为0.92，因为replacement
      item generation已constrained to same subject，但minor gaps in specific
      cognitive sub-skills可能出现。Theoretical lower bound formula provides
      conservative estimate，empirical results consistently exceed it（0.95 > 0.93
      at 20%），validating the bound's correctness。
    tables:
      - title: "Table 16: Validity Metrics Under Progressive Replacement"
        columns: [replacement_rate, ranking_rho, reliability_alpha, construct_jaccard, score_rmse]
        rows:
          - [0.00, 1.00, 0.94, 1.00, 0.000]
          - [0.05, 0.99, 0.93, 0.98, 0.008]
          - [0.10, 0.97, 0.93, 0.96, 0.015]
          - [0.20, 0.95, 0.91, 0.92, 0.025]
          - [0.35, 0.92, 0.89, 0.87, 0.038]
          - [0.50, 0.89, 0.87, 0.83, 0.052]
      - title: "Table 17: Theoretical vs Empirical Bounds"
        columns: [replacement_rate, theoretical_rho_lb, empirical_rho, bound_tight]
        rows:
          - [0.05, 0.97, 0.99, false]
          - [0.10, 0.95, 0.97, false]
          - [0.20, 0.93, 0.95, false]
          - [0.50, 0.84, 0.89, false]
    figures_description:
      - "Figure 23: Validity degradation curves (rho, alpha, Jaccard) vs replacement rate, with 0.95 threshold line marking 'psychometrically equivalent' zone."
      - "Figure 24: Theoretical lower bound vs empirical results, showing bound is conservative but informative."
    analysis: >
      Graceful degradation分析为benchmark regeneration建立了formal safety guarantees。
      20% replacement threshold（rho≥0.95）为实际操作提供了clear guideline——
      given MMLU上约10.7% items被DIF flagged（plan_001），单轮replacement在安全范围内。
      理论bound的conservativeness（empirical consistently exceeds theoretical by 2-5pp）
      提供额外safety margin。这一结果完成了Claim 3从detection → generation → equating →
      validity guarantee的完整pipeline。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      实现Item-Focused Trees作为categorical cohort DIF的替代方案。
      将model release date作为continuous covariate，比较检测力和灵活性。
    expected_results:
      ift_tpr_delta_ge_1_4: 0.81
      ift_tpr_delta_ge_1_0: 0.58
      ift_fpr: 0.044
      ift_auc: 0.90
      ift_vs_ets_c_tpr_improvement: 0.03
      ift_vs_ets_c_auc_improvement: -0.02
      ift_detected_gradual_contamination: true
      n_items_with_changepoint: 890
      median_changepoint_date: "2023-06"
      changepoint_clustering_by_subject: true
      ift_computation_time_seconds: 340
      ets_c_computation_time_seconds: 28
    result_rationale: >
      Item-Focused Trees的优势在于不需要arbitrary cohort splits——它自动发现每个item
      的contamination onset point（changepoint）作为tree split。TPR=0.81略优于
      ETS C的0.78（+3pp），因为IFT可以为每个item找到optimal focal/reference split
      而非使用统一的pre/post cutoff。但AUC=0.90略低于ETS C的0.92，因为IFT在small
      effects区间的precision较低（tree splitting在low-signal regime容易overfit）。
      Changepoint clustering by subject是重要的secondary finding——STEM subjects的
      median changepoint早于humanities（2023-03 vs 2023-09），反映code-heavy training
      data对STEM contamination的earlier onset。890个items有detectable changepoints，
      与plan_001的1340 flagged items部分重叠（IFT的threshold更conservative因为tree
      pruning）。计算成本是ETS C的12x，因为recursive partitioning需要对每个item
      搜索所有可能splits，但仍在minutes级别（CPU only），实际可用。IFT的主要paper value
      是methodological：它证明contamination timing是item-specific而非cohort-uniform，
      支持"contamination as gradual process"的narrative。
    tables:
      - title: "Table 18: Item-Focused Trees vs ETS C Comparison"
        columns: [method, tpr_ge_1_4, tpr_ge_1_0, fpr, auc, time_sec]
        rows:
          - [ETS_C, 0.78, 0.45, 0.038, 0.92, 28]
          - [Item_Focused_Trees, 0.81, 0.58, 0.044, 0.90, 340]
          - [Combined, 0.84, 0.60, 0.048, 0.93, 368]
      - title: "Table 19: Contamination Changepoint Analysis"
        columns: [subject_group, n_items_with_changepoint, median_changepoint, range]
        rows:
          - [STEM, 520, "2023-03", "2022-06 to 2024-01"]
          - [Humanities, 210, "2023-09", "2023-01 to 2024-06"]
          - [Social_Sciences, 160, "2023-06", "2022-09 to 2024-03"]
    figures_description:
      - "Figure 25: Item-level changepoint distribution across calendar time, colored by subject. STEM items show earlier contamination onset."
      - "Figure 26: Example Item-Focused Tree for a specific MMLU item, showing splits on release date and model family."
    analysis: >
      IFT作为P2实验提供了methodological depth——contamination timing的item-specific
      和subject-specific patterns是novel finding，支持论文的temporal dynamics narrative。
      Detection power的marginal improvement（+3pp TPR）不足以替代ETS C作为primary
      method，但combined approach（union of flags）将TPR推到0.84。更重要的是IFT的
      changepoint analysis为understanding contamination dynamics提供了unique evidence，
      可作为analysis section的secondary contribution。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4100b914-be95-404a-8e3c-949b931d1ab2",
  "isSidechain": false,
  "requestId": "req_011CbEPmxbVb3RRfqbzizXBY",
  "type": "assistant",
  "uuid": "27560bd1-27d9-4247-8f53-4626a8ef256c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvoTn9y6QVAM4BFJR7U4oA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10438,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16078,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16078,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10438
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：DIF在真实数据上复现模拟power，RL-robustness经验验证成功，ensemble三信号互补清晰，equating达到psychometric标准——原始framing完整成立 核心假设：['METABENCH真实cohort size达N≥80且contamination effect size…",
  "leafUuid": "27560bd1-27d9-4247-8f53-4626a8ef256c",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF-based contamination detection and IRT equating for self-healing benchmarks",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：DIF在真实数据上复现模拟power，RL-robustness经验验证成功，ensemble三信号互补清晰，equating达到psychometric标准——原始framing完整成立 核心假设：['METABENCH真实cohort size达N≥80且contamination effect size…",
  "leafUuid": "27560bd1-27d9-4247-8f53-4626a8ef256c",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF-based contamination detection and IRT equating for self-healing benchmarks",
  "sessionId": "25adcdbb-09aa-42cd-bd7a-e053270e6068"
}
```

---
