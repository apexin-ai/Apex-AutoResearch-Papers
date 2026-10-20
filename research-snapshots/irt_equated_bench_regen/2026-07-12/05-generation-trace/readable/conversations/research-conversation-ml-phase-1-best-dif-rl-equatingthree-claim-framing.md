# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：DIF在真实数据上复现仿真预测，RL鲁棒性实证确认，equating达到心理测量标准——原始three-claim framing完整成立 核心假设：[

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/21234657-3e54-488f-a743-b1a19a8c893b.jsonl`
- **Structured JSON:** [`7d649efb2823177eb6a0.json`](../../sessions/7d/7d649efb2823177eb6a0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:36:19.752Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:36:19.752Z",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：DIF在真实数据上复现仿真预测，RL鲁棒性实证确认，equating达到心理测量标准——原始three-claim framing完整成立\n核心假设：['METABENCH MMLU响应矩阵中temporal cohort间存在可检测的DIF模式，且与MMLU-CF污染标注显著相关', 'RL训练模型cohort中DIF检测力几乎无衰减，因为群体水平ICC异常无法被模型内分布平滑消除', '双因子IRT锚题选择充分，替换题经验标定后能保持排名一致性', 'GSM8K跨基准验证独立复现DIF检测效果']\n关键指标范围：{'real_data_dif_tpr_large_effect': [0.7, 0.85], 'real_data_dif_fpr': [0.02, 0.05], 'dif_mmlu_cf_correlation': [0.3, 0.5], 'rl_robustness_tpr_retention': [0.9, 1.0], 'competitor_auroc_post_rl': [0.48, 0.58], 'ensemble_coverage_all_effects': [0.85, 0.95], 'ensemble_fpr': [0.03, 0.08], 'equating_spearman_rho': [0.95, 0.99], 'difficulty_calibration_r': [0.7, 0.85], 'gsm8k_dif_gap_correlation': [0.35, 0.55]}\n叙事方向：原始framing完全成立：DIF是唯一RL-robust的污染检测信号（Claim 1实证验证）， ensemble覆盖全效应量谱（Claim 2），bifactor equating实现心理测量等价的基准再生（Claim 3）。 标题可用\"self-healing benchmark\"。Headline result直接套用模板，数字落在承诺范围内。 ICLR投稿无需调整claim强度。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026).\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: 'Apply DIF analysis to METABENCH MMLU response matrix (5,055 models\n    × 12,508 items). Split models into temporal cohorts by release date (pre-2024\n    vs post-2024, plus finer annual splits). Run ETS C DIF detection on all items.\n    Validate against MMLU-CF (ACL 2025) contamination-free items as partial ground\n    truth: items present in MMLU but significantly modified in MMLU-CF should correlate\n    with DIF flags. Sensitivity analysis across different cohort definitions and contamination\n    thresholds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: 'Empirically validate DIF''s RL-robustness claim. Construct two scenarios:\n    (a) cohort with SFT-only models, (b) cohort including RL-trained reasoning models\n    (DeepSeek-R1, Qwen-2.5-RL, etc. from METABENCH or via inference). Run DIF + traditional\n    detectors (Min-K%, ConStat perturbation, DVD) on both scenarios. Show DIF maintains\n    detection power in scenario (b) while traditional detectors degrade. If METABENCH\n    lacks RL-trained models, run inference on 10-15 open-weight RL models on MMLU.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003\n  name: multi_signal_ensemble\n  claim: 2\n  description: 'Implement 3-signal contamination sentinel ensemble: Signal 1 — DIF\n    ETS C (large effects, RL-robust) Signal 2 — ConStat-style perturbation testing\n    (semantically equivalent reformulations, FDR control) Signal 3 — DVD generation\n    variance (50 responses/item via temperature sampling, bimodal detection) Evaluate\n    ensemble with 2-of-3 voting on MMLU using METABENCH data. Show: (a) ensemble coverage\n    across effect sizes (DIF covers δ≥1.4, others cover δ<1.0), (b) ensemble maintains\n    precision (FPR<0.10), (c) ensemble is robust to model mix.\n\n    '\n  priority: P0\n  gpu_budget_hours: 150\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond MMLU-CF.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:36:19.755Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:36:19.755Z",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T19:36:19.777Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：DIF在真实数据上复现仿真预测，RL鲁棒性实证确认，equating达到心理测量标准——原始three-claim framing完整成立
核心假设：['METABENCH MMLU响应矩阵中temporal cohort间存在可检测的DIF模式，且与MMLU-CF污染标注显著相关', 'RL训练模型cohort中DIF检测力几乎无衰减，因为群体水平ICC异常无法被模型内分布平滑消除', '双因子IRT锚题选择充分，替换题经验标定后能保持排名一致性', 'GSM8K跨基准验证独立复现DIF检测效果']
关键指标范围：{'real_data_dif_tpr_large_effect': [0.7, 0.85], 'real_data_dif_fpr': [0.02, 0.05], 'dif_mmlu_cf_correlation': [0.3, 0.5], 'rl_robustness_tpr_retention': [0.9, 1.0], 'competitor_auroc_post_rl': [0.48, 0.58], 'ensemble_coverage_all_effects': [0.85, 0.95], 'ensemble_fpr': [0.03, 0.08], 'equating_spearman_rho': [0.95, 0.99], 'difficulty_calibration_r': [0.7, 0.85], 'gsm8k_dif_gap_correlation': [0.35, 0.55]}
叙事方向：原始framing完全成立：DIF是唯一RL-robust的污染检测信号（Claim 1实证验证）， ensemble覆盖全效应量谱（Claim 2），bifactor equating实现心理测量等价的基准再生（Claim 3）。 标题可用"self-healing benchmark"。Headline result直接套用模板，数字落在承诺范围内。 ICLR投稿无需调整claim强度。


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
- id: plan_003
  name: multi_signal_ensemble
  claim: 2
  description: 'Implement 3-signal contamination sentinel ensemble: Signal 1 — DIF
    ETS C (large effects, RL-robust) Signal 2 — ConStat-style perturbation testing
    (semantically equivalent reformulations, FDR control) Signal 3 — DVD generation
    variance (50 responses/item via temperature sampling, bimodal detection) Evaluate
    ensemble with 2-of-3 voting on MMLU using METABENCH data. Show: (a) ensemble coverage
    across effect sizes (DIF covers δ≥1.4, others cover δ<1.0), (b) ensemble maintains
    precision (FPR<0.10), (c) ensemble is robust to model mix.

    '
  priority: P0
  gpu_budget_hours: 150
  deps:
  - plan_001
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
  "promptId": "2f56fb05-58bb-4ba8-9fd6-4c9957d75ee4",
  "type": "user",
  "uuid": "7c53a6d4-7370-4310-b308-8cde3c056958",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:36:19.776Z_

```json
{
  "parentUuid": "7c53a6d4-7370-4310-b308-8cde3c056958",
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
  "uuid": "ecdd37f7-3b9d-495e-ace9-6b6e2c096182",
  "timestamp": "2026-05-20T19:36:19.776Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:36:19.776Z_

```json
{
  "parentUuid": "ecdd37f7-3b9d-495e-ace9-6b6e2c096182",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "30682c03-c987-407e-8bc0-4c5d0757c5ac",
  "timestamp": "2026-05-20T19:36:19.776Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：DIF在真实数据上复现仿真预测，RL鲁棒性实证确认，equating达到心理测量标准——原始three-claim framing完整成立 核心假设：['METABENCH MMLU响应矩阵中temporal cohort间存在可检测的DIF模式，且与MMLU-CF污染标注显著相关', 'RL训练模型coho…",
  "leafUuid": "30682c03-c987-407e-8bc0-4c5d0757c5ac",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF-based contamination detection for self-healing benchmarks",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:36:34.636Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment plan, under the "best" tier scenario. I need to provide specific metric predictions with rationales for why those results would occur under the best-case narrative.

Let me carefully go through each experiment and generate predictions consistent with the best tier definition and the key metric ranges provided.

Key metric ranges for best tier:
- real_data_dif_tpr_large_effect: [0.7, 0.85]
- real_data_dif_fpr: [0.02, 0.05]


- dif_mmlu_cf_correlation: [0.3, 0.5]
- rl_robustness_tpr_retention: [0.9, 1.0]
- competitor_auroc_post_rl: [0.48, 0.58]
- ensemble_coverage_all_effects: [0.85, 0.95]
- ensemble_fpr: [0.03, 0.08]
- equating_spearman_rho: [0.95, 0.99]
- difficulty_calibration_r: [0.7, 0.85]
- gsm8k_dif_gap_correlation: [0.35, 0.55]

Now I'm pulling in the Phase 2 simulation results showing ETS C TPR performance across different sample sizes and effect sizes, with FPR staying in the 0.036-0.042 range. With these benchmarks in place, I'm ready to map out detailed predictions for each of the nine planned experiments, starting with real data DIF validation on MMLU and moving through robustness checks, ensemble methods, cross-benchmark testing, IRT equating, item generation, Bayesian DIF analysis, and graceful degradation scenarios.

Writing experiment predictions as YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30682c03-c987-407e-8bc0-4c5d0757c5ac",
  "isSidechain": false,
  "requestId": "req_011CbEPCBVBsuhya86PLb4Es",
  "type": "assistant",
  "uuid": "234d489d-f51c-4705-a1ce-298c321ba075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DgfruVfzLNLzwLQueKAa4V",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9974,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12025,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9974
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

_source line 9 · 2026-05-20T19:40:10.452Z_

```yaml
tier: best
narrative_guidance: >
  原始three-claim framing完整成立。DIF在METABENCH真实数据上复现仿真预测的检测力，
  MMLU-CF交叉验证提供外部效度，RL-trained模型cohort中DIF信号几乎无衰减而竞争方法
  降至随机水平，ensemble覆盖全效应量谱，bifactor equating达到心理测量等价标准。
  标题使用"self-healing benchmark"，headline数字直接落在承诺范围内，ICLR投稿无需
  降调任何claim。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      在METABENCH MMLU响应矩阵(5055模型×12508题)上运行ETS C DIF检测。
      按release date划分temporal cohort (pre-2024 reference vs post-2024 focal,
      加年度细分)。以MMLU-CF污染标注为部分ground truth进行外部验证。
    expected_results:
      n_models_total: 5055
      n_items_total: 12508
      cohort_pre2024_n: 2180
      cohort_post2024_n: 2875
      ets_c_tpr_large_effect_d14: 0.78
      ets_c_tpr_large_effect_d16: 0.83
      ets_c_fpr: 0.035
      n_items_flagged_c_category: 1840
      pct_items_flagged: 0.147
      dif_mmlu_cf_correlation_phi: 0.42
      dif_mmlu_cf_correlation_p: 1.2e-38
      sensitivity_annual_split_tpr_range: [0.71, 0.85]
      sensitivity_threshold_sweep_auc: 0.91
      irt_param_a_mean_flagged: 0.68
      irt_param_a_mean_clean: 1.14
      irt_param_b_shift_flagged: -1.32
    result_rationale: >
      仿真Phase 2已确认ETS C在N=100/δ=1.4条件下TPR=0.758，真实数据cohort规模
      远超仿真设定(N>2000 per cohort)，统计功效大幅提升。但真实数据中contamination
      effect size并非均匀分布——部分题目仅有中等DIF，拉低整体TPR。综合效应：
      大效应题目TPR达0.78，略高于仿真N=100预测值但未达理论上限，因为真实DIF
      模式含噪声(模型能力异质性、partial memorization)。FPR=0.035与仿真一致，
      因为ETS C基于效应量阈值而非p值，对样本量不敏感。MMLU-CF相关φ=0.42：
      MMLU-CF通过语义改写消除memorization优势，DIF flags的题目正是那些在改写后
      难度显著变化的题目，两者测量同一latent construct(memorization-induced
      easiness)，但操作化方式不同(behavioral DIF vs perturbation)，故相关为
      中等偏强而非接近1。flagged题目的IRT区分度(a=0.68)显著低于clean题目
      (a=1.14)，因为contaminated题目对高低能力模型的区分力被memorization效应
      压平。
    tables:
      - name: "Table 1: DIF Detection on METABENCH MMLU"
        columns: [cohort_split, n_reference, n_focal, tpr_large, tpr_medium, fpr, n_flagged, auc]
        rows:
          - [pre2024_vs_post2024, 2180, 2875, 0.78, 0.31, 0.035, 1840, 0.91]
          - [annual_2022_vs_2024, 680, 1450, 0.82, 0.35, 0.032, 1920, 0.93]
          - [annual_2023_vs_2025, 1200, 1380, 0.75, 0.28, 0.038, 1710, 0.89]
      - name: "Table 2: MMLU-CF Cross-Validation"
        columns: [metric, value, ci_95_lower, ci_95_upper]
        rows:
          - [phi_coefficient, 0.42, 0.38, 0.46]
          - [odds_ratio, 4.8, 4.1, 5.6]
          - [precision_at_mmlu_cf, 0.61, 0.57, 0.65]
          - [recall_at_mmlu_cf, 0.74, 0.69, 0.79]
    figures_description:
      - "Fig 1a: Item DIF magnitude (Δ_MH) histogram，双峰分布，clean items聚集在|Δ|<0.4, contaminated items在|Δ|>1.0处形成第二峰"
      - "Fig 1b: ROC curve across ETS C threshold sweep，AUC=0.91，标注operating point (TPR=0.78, FPR=0.035)"
      - "Fig 1c: DIF flag vs MMLU-CF label confusion matrix heatmap，φ=0.42"
      - "Fig 1d: Flagged vs clean items的IRT ICC曲线对比，flagged items的focal group ICC向左偏移(contamination-induced easiness)"
    analysis: >
      真实数据结果与仿真预测高度一致，确认DIF在operational条件下具备实用检测力。
      MMLU-CF交叉验证(φ=0.42)提供独立于方法论的外部效度——DIF检测到的异常题目
      确实与已知污染源高度重叠。14.7%的MMLU题目被flagged，与GSM1K报告的10-13%
      accuracy gap数量级一致。年度细分显示DIF在2022-vs-2024对比中最强(φ=0.82 TPR)，
      因为时间跨度最大、contamination累积效应最显著。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      构建SFT-only cohort和RL-inclusive cohort，在两种场景下对比DIF与传统检测器
      (Min-K%, ConStat perturbation, DVD)的检测力变化。
    expected_results:
      n_sft_models: 85
      n_rl_models: 18
      dif_tpr_sft_cohort: 0.79
      dif_tpr_rl_inclusive_cohort: 0.76
      dif_tpr_retention_ratio: 0.962
      dif_fpr_rl_cohort: 0.038
      mink_auroc_sft: 0.73
      mink_auroc_rl: 0.52
      mink_degradation_pp: 21
      constat_auroc_sft: 0.81
      constat_auroc_rl: 0.54
      constat_degradation_pp: 27
      dvd_auroc_sft: 0.69
      dvd_auroc_rl: 0.51
      dvd_degradation_pp: 18
      dif_auroc_sft: 0.91
      dif_auroc_rl: 0.89
      dif_degradation_pp: 2
      wilcoxon_dif_vs_best_competitor_p: 3.4e-7
    result_rationale: >
      DIF的RL鲁棒性源于其操作层级：DIF测量的是群体水平的Item Characteristic Curve
      异常(conditional on θ，contaminated cohort在特定题目上的正确率异常偏高)。
      RL训练(GRPO/PPO)优化的是policy-level output distribution——它平滑token
      概率、降低perplexity离群值、改变generation diversity——但无法消除一个
      已memorize题目的behavioral事实：模型答对了它"不该"答对的题目(given其θ)。
      要消除DIF信号，RL需要让模型在memorized题目上故意答错，这与contamination
      带来的reward signal矛盾。因此DIF TPR仅从0.79降至0.76(3.8%衰减)，完全
      在统计噪声范围内。相比之下，Min-K%依赖token-level perplexity异常，
      GRPO直接优化这一分布使其平滑(21pp AUROC降幅)；ConStat依赖perturbation
      sensitivity差异，RL models学会了对paraphrase的robust responding(27pp降幅)；
      DVD依赖generation variance bimodality，RL的KL-constrained optimization
      直接压缩output variance(18pp降幅)。这三种方法均操作在model-internal
      distribution层级，恰好是RL训练的直接优化目标。
    tables:
      - name: "Table 3: Detection Power — SFT-only vs RL-inclusive Cohorts"
        columns: [method, auroc_sft, auroc_rl, delta_pp, tpr_at_fpr05_sft, tpr_at_fpr05_rl]
        rows:
          - [DIF_ETS_C, 0.91, 0.89, -2, 0.79, 0.76]
          - [Min-K_Percent, 0.73, 0.52, -21, 0.48, 0.19]
          - [ConStat_Perturb, 0.81, 0.54, -27, 0.58, 0.22]
          - [DVD_GenVar, 0.69, 0.51, -18, 0.39, 0.15]
          - [Perplexity_Ratio, 0.71, 0.49, -22, 0.44, 0.16]
      - name: "Table 4: RL Model Breakdown"
        columns: [model_family, training_type, n_models, dif_tpr_on_known_contaminated]
        rows:
          - [DeepSeek-R1-variants, GRPO, 5, 0.77]
          - [Qwen2.5-RL-variants, PPO+GRPO, 4, 0.74]
          - [LLaMA3-RL-finetunes, DPO+PPO, 6, 0.75]
          - [Other-RL, mixed, 3, 0.78]
    figures_description:
      - "Fig 2a: Paired AUROC bar chart (SFT vs RL cohort)，5种方法，DIF几乎无变化而其他方法大幅下降"
      - "Fig 2b: DIF effect size (Δ_MH) scatter plot，SFT-cohort vs RL-cohort per item，Pearson r=0.94"
      - "Fig 2c: 各方法在RL cohort上的ROC曲线叠加，DIF曲线远离对角线而其他方法贴近"
    analysis: >
      这是论文的核心differentiating result。DIF的96.2% TPR retention率直接验证了
      理论预测：群体水平ICC异常不可被模型内分布优化消除。竞争方法AUROC降至
      0.49-0.54(实质随机)，与Wang et al. (ICLR 2026)报告的14-20pp degradation
      一致(我们观测到18-27pp，更大是因为我们的RL模型更多样)。这建立了DIF作为
      唯一RL-robust contamination signal的empirical case。

  - name: multi_signal_ensemble
    plan_id: plan_003
    description: >
      实现三信号ensemble (DIF + ConStat perturbation + DVD generation variance)，
      评估在全效应量谱和模型类型景观上的覆盖率。
    expected_results:
      ensemble_coverage_large_effects: 0.92
      ensemble_coverage_medium_effects: 0.68
      ensemble_coverage_small_effects: 0.41
      ensemble_coverage_all_effects_weighted: 0.89
      ensemble_fpr: 0.055
      ensemble_f1_large: 0.88
      ensemble_f1_medium: 0.62
      dif_solo_coverage_large: 0.78
      dif_solo_coverage_medium: 0.31
      dif_solo_coverage_small: 0.08
      constat_solo_coverage_large: 0.71
      constat_solo_coverage_medium: 0.55
      constat_solo_coverage_small: 0.32
      dvd_solo_coverage_large: 0.52
      dvd_solo_coverage_medium: 0.48
      dvd_solo_coverage_small: 0.35
      overlap_dif_constat: 0.43
      overlap_dif_dvd: 0.22
      overlap_constat_dvd: 0.51
      ensemble_voting_2of3_precision: 0.87
      ensemble_voting_2of3_recall: 0.89
      ensemble_any_signal_recall: 0.94
      ensemble_any_signal_precision: 0.72
    result_rationale: >
      三信号ensemble的设计逻辑是互补覆盖：DIF擅长大效应且RL-robust，ConStat擅长
      中小效应(perturbation sensitivity对subtle memorization敏感)，DVD擅长variant
      contamination(generation variance bimodality)。在best档：(1) 大效应覆盖0.92，
      因为DIF(0.78)和ConStat(0.71)在大效应上高度有效，union后覆盖接近1-
      (1-0.78)(1-0.71)=0.936(略低于独立假设因为存在正相关overlap=0.43)。
      (2) 中效应覆盖0.68，主要由ConStat(0.55)和DVD(0.48)贡献，DIF此区间较弱(0.31)。
      (3) 小效应覆盖0.41，三个信号均较弱但union仍有增益。加权overall coverage 0.89
      (权重偏向大中效应，因为这些才是影响排名的效应)。FPR=0.055因为2-of-3 voting
      要求多信号一致，有效控制了单信号false positive的传播——只有两个独立信号
      同时误报才会触发ensemble flag，概率约为单信号FPR的平方量级。
    tables:
      - name: "Table 5: Ensemble Coverage by Effect Size"
        columns: [effect_size_bin, dif_only, constat_only, dvd_only, ensemble_2of3, ensemble_any]
        rows:
          - ["large (δ≥1.4)", 0.78, 0.71, 0.52, 0.92, 0.96]
          - ["medium (0.6≤δ<1.4)", 0.31, 0.55, 0.48, 0.68, 0.81]
          - ["small (δ<0.6)", 0.08, 0.32, 0.35, 0.41, 0.58]
          - ["weighted_overall", 0.54, 0.56, 0.46, 0.89, 0.94]
      - name: "Table 6: Ensemble Precision-Recall by Voting Threshold"
        columns: [threshold, precision, recall, f1, fpr]
        rows:
          - [any_signal, 0.72, 0.94, 0.82, 0.098]
          - [2_of_3, 0.87, 0.89, 0.88, 0.055]
          - [all_3, 0.95, 0.41, 0.57, 0.012]
      - name: "Table 7: Signal Complementarity Matrix (Jaccard overlap on flagged items)"
        columns: [pair, jaccard_overlap, unique_to_first, unique_to_second]
        rows:
          - [DIF_vs_ConStat, 0.43, 0.28, 0.31]
          - [DIF_vs_DVD, 0.22, 0.51, 0.39]
          - [ConStat_vs_DVD, 0.51, 0.19, 0.22]
    figures_description:
      - "Fig 3a: Venn diagram三信号flagged items overlap，数字标注各区域item count"
      - "Fig 3b: Effect size spectrum coverage curve，x轴δ从0到2.5，y轴coverage，三条单信号线+ensemble线"
      - "Fig 3c: Precision-Recall curve for ensemble voting thresholds"
    analysis: >
      2-of-3 voting是最优operating point (F1=0.88)。DIF和ConStat的overlap(0.43)
      确认它们测量的是同一现象的不同manifestation，但各有独占区域。DVD与DIF的
      低overlap(0.22)说明DVD捕捉了DIF遗漏的variant contamination模式。
      ensemble weighted coverage 0.89满足best档[0.85, 0.95]要求，FPR=0.055落在
      [0.03, 0.08]范围内。Claim 2成立。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      在GSM8K上复制DIF分析，利用GSM1K作为独立ground truth验证跨基准泛化性。
    expected_results:
      n_models_gsm8k: 62
      n_items_gsm8k: 1319
      cohort_early_n: 28
      cohort_late_n: 34
      dif_flagged_items: 195
      pct_flagged: 0.148
      dif_flag_vs_gsm1k_gap_correlation_spearman: 0.46
      dif_flag_vs_gsm1k_gap_correlation_p: 2.1e-4
      mean_gap_dif_flagged_items: 0.142
      mean_gap_clean_items: 0.031
      gap_ratio: 4.58
      tpr_against_gsm1k_top_quartile: 0.74
      fpr_against_gsm1k_bottom_quartile: 0.041
      ets_c_large_effect_count: 112
      ets_c_medium_effect_count: 83
    result_rationale: >
      GSM8K是数学推理benchmark，contamination模式与MMLU(知识recall)不同。
      GSM1K提供了独立ground truth：per-model GSM8K-GSM1K accuracy gap直接量化
      contamination程度。在best档，DIF flagged items与per-model gap的Spearman
      ρ=0.46(落在[0.35, 0.55]范围)。相关未达MMLU-CF的0.42(φ)但仍高度显著，
      原因是：(1) GSM8K模型样本量较小(N=62 vs MMLU的5055)，统计功效受限；
      (2) GSM1K是whole-benchmark ground truth(per-model gap)而非per-item label，
      与DIF的per-item检测存在粒度不匹配——但DIF flagged items上的gap(0.142)是
      clean items(0.031)的4.58倍，confirming DIF flags确实集中在contamination
      最严重的题目上。14.8%的flagged率与MMLU(14.7%)惊人一致，暗示contamination
      影响的题目比例跨benchmark相对稳定。cohort size较小(28/34)导致medium effect
      检测力较低，但large effect TPR仍达0.74，确认DIF方法的跨benchmark泛化性。
    tables:
      - name: "Table 8: GSM8K DIF Results"
        columns: [metric, value]
        rows:
          - [n_models, 62]
          - [n_items, 1319]
          - [items_flagged_ets_c, 195]
          - [pct_flagged, 0.148]
          - [mean_gap_flagged, 0.142]
          - [mean_gap_clean, 0.031]
          - [spearman_rho_gap_correlation, 0.46]
          - [p_value, 2.1e-4]
      - name: "Table 9: GSM8K vs MMLU DIF Comparison"
        columns: [benchmark, n_models, pct_flagged, tpr_large, fpr, external_validity_corr]
        rows:
          - [MMLU, 5055, 0.147, 0.78, 0.035, "φ=0.42 (MMLU-CF)"]
          - [GSM8K, 62, 0.148, 0.74, 0.041, "ρ=0.46 (GSM1K gap)"]
    figures_description:
      - "Fig 4a: Per-model GSM8K-GSM1K gap vs DIF-flagged item accuracy advantage scatter plot，ρ=0.46"
      - "Fig 4b: DIF flagged vs clean items的gap distribution violin plot，clear separation"
    analysis: >
      GSM8K独立复现确认DIF方法不依赖特定benchmark特性。与MMLU结果的一致性
      (flagged比例、检测力量级)支持DIF作为通用contamination detection框架的定位。
      GSM1K ground truth提供了比MMLU-CF更直接的contamination量化，ρ=0.46的相关
      在考虑粒度不匹配后是强结果。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      在METABENCH MMLU数据上拟合bifactor IRT模型，选择anchor items，
      通过fixed-parameter calibration标定替换题，验证equated score等价性。
    expected_results:
      bifactor_general_factor_variance_explained: 0.52
      n_specific_factors: 14
      specific_factor_variance_range: [0.08, 0.22]
      rmsea: 0.032
      cfi: 0.967
      n_anchor_items_selected: 1875
      anchor_selection_criteria_met_pct: 0.85
      anchor_dif_max: 0.3
      anchor_stability_icc: 0.94
      n_flagged_items_replaced: 1840
      equating_spearman_rho: 0.973
      equating_kendall_tau: 0.951
      equating_rmse_theta: 0.089
      equating_max_rank_change: 12
      equating_mean_rank_change: 2.3
      score_reliability_original: 0.924
      score_reliability_equated: 0.918
      construct_coverage_cosine: 0.97
    result_rationale: >
      Bifactor模型在MMLU上fit良好(RMSEA=0.032, CFI=0.967)因为MMLU本身就是
      多维度结构(57个subject领域)，bifactor的general+specific因子结构天然匹配。
      General factor解释52%方差，反映cross-domain reasoning ability；14个specific
      factors对应聚合后的subject clusters。Anchor items选择1875题(15%，占clean
      items的约17%)——这些题目在所有temporal cohorts上ICC高度稳定(ICC=0.94)且
      无DIF(max Δ<0.3)，确保equating链的psychometric锚点可靠。Spearman ρ=0.973
      (落在[0.95, 0.99])表明equated benchmark上的模型排名与原始benchmark高度
      一致。未达0.99是因为：(1) 替换题虽经calibration但与原题并非完全等价，
      引入少量measurement error；(2) 少数边界模型(排名接近的模型对)可能因
      equating噪声交换位置(max rank change=12, mean=2.3)。Score reliability
      仅从0.924降至0.918，降幅0.006在心理测量标准内完全可接受(<0.02 threshold)。
    tables:
      - name: "Table 10: Bifactor IRT Model Fit"
        columns: [metric, value, acceptable_threshold]
        rows:
          - [RMSEA, 0.032, "<0.06"]
          - [CFI, 0.967, ">0.95"]
          - [TLI, 0.961, ">0.95"]
          - [general_factor_variance, 0.52, ">0.40"]
          - [n_specific_factors, 14, "-"]
      - name: "Table 11: Equating Results"
        columns: [metric, value, target]
        rows:
          - [spearman_rho, 0.973, "≥0.95"]
          - [kendall_tau, 0.951, "≥0.93"]
          - [rmse_theta, 0.089, "<0.15"]
          - [max_rank_change, 12, "<20"]
          - [mean_rank_change, 2.3, "<5"]
          - [reliability_delta, -0.006, ">-0.02"]
      - name: "Table 12: Anchor Item Quality"
        columns: [criterion, value]
        rows:
          - [n_anchor_items, 1875]
          - [max_dif_delta, 0.3]
          - [stability_icc, 0.94]
          - [difficulty_range_coverage, "[-2.8, 2.4]"]
          - [discrimination_mean, 1.21]
    figures_description:
      - "Fig 5a: Original vs equated model rankings scatter plot，ρ=0.973，对角线附近密集分布"
      - "Fig 5b: Bifactor模型path diagram，general factor + 14 specific factors"
      - "Fig 5c: Rank change distribution histogram，heavy tail在±5以内"
      - "Fig 5d: Score reliability (Cronbach's α) across progressive replacement rates"
    analysis: >
      Bifactor equating成功实现心理测量等价。ρ=0.973意味着基准再生后的排名几乎
      不变，少数rank change集中在能力接近的模型对之间(这些rank差异本身在原始
      benchmark的measurement error范围内)。1875个anchor items提供了足够的equating
      链强度。Claim 3的核心——polluted items可以被替换且不损失benchmark validity——
      得到实证验证。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      为DIF-flagged MMLU题目生成替换题，通过student simulation进行empirical
      difficulty calibration，对比prompt-based difficulty targeting。
    expected_results:
      n_items_generated: 2760
      n_items_after_quality_filter: 2210
      quality_filter_pass_rate: 0.80
      difficulty_correlation_student_sim: 0.79
      difficulty_correlation_prompt_based: 0.28
      difficulty_correlation_improvement_ratio: 2.82
      discrimination_correlation_student_sim: 0.71
      construct_match_rate: 0.92
      cognitive_level_match_rate: 0.88
      holdout_panel_difficulty_rmse: 0.34
      holdout_panel_difficulty_correlation: 0.76
      generation_cost_per_item_usd: 0.42
      calibration_cost_per_item_usd: 1.85
    result_rationale: >
      Student simulation (arXiv 2601.09953)通过让多个LLM "学生"回答生成题目来
      empirically估计难度，绕过了直接prompt-based difficulty targeting的根本缺陷
      (LLM对自身/同类的difficulty perception与actual difficulty poorly calibrated，
      故rho=0.28仅略好于random)。r=0.79(落在[0.7, 0.85])因为student simulation
      有效模拟了真实模型panel的response pattern，但存在系统偏差：simulation中
      使用的student models有限(~20)，无法完全覆盖真实5000+模型的ability分布。
      80%的质量过滤通过率因为LLM generation在construct constraints下仍有约20%
      的题目存在ambiguity、incorrect answers或off-construct内容。Construct match
      rate 0.92表明约8%的生成题虽然通过了难度calibration但偏离了原始construct
      (如MMLU abstract_algebra题被替换为linear_algebra变体)。
    tables:
      - name: "Table 13: Difficulty Calibration Comparison"
        columns: [method, difficulty_r, discrimination_r, construct_match, cost_per_item]
        rows:
          - [prompt_based_targeting, 0.28, 0.15, 0.85, "$0.12"]
          - [student_simulation_20_students, 0.79, 0.71, 0.92, "$2.27"]
          - [student_simulation_10_students, 0.72, 0.63, 0.91, "$1.35"]
          - [student_simulation_5_students, 0.61, 0.52, 0.90, "$0.82"]
      - name: "Table 14: Holdout Validation"
        columns: [metric, in_sample, holdout, delta]
        rows:
          - [difficulty_r, 0.79, 0.76, -0.03]
          - [discrimination_r, 0.71, 0.65, -0.06]
          - [difficulty_rmse, 0.29, 0.34, +0.05]
    figures_description:
      - "Fig 6a: Student-sim predicted vs actual difficulty scatter，r=0.79，对比prompt-based (r=0.28)灰色散点"
      - "Fig 6b: Calibration cost vs accuracy Pareto frontier，n_students从5到50"
      - "Fig 6c: 生成题 vs 原题 difficulty distribution对比 (matched histograms)"
    analysis: >
      Student simulation将difficulty calibration accuracy从0.28提升至0.79(2.82x)，
      验证了empirical calibration相对于prompt-based方法的根本优势。20个student
      models是cost-accuracy tradeoff的sweet spot。Combined with plan_005的equating
      框架，这建立了complete item regeneration pipeline：detect → generate →
      calibrate → equate。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      实现cumulative Bayesian DIF priors，模拟4次连续benchmark administration，
      展示累积证据带来的power提升。
    expected_results:
      admin_1_power_medium_effect: 0.38
      admin_2_power_medium_effect: 0.54
      admin_3_power_medium_effect: 0.68
      admin_4_power_medium_effect: 0.76
      admin_1_power_large_effect: 0.72
      admin_4_power_large_effect: 0.94
      bayes_factor_threshold: 10
      cumulative_fpr_admin4: 0.042
      power_improvement_factor_medium: 2.0
      power_improvement_factor_large: 1.31
      convergence_rate_medium: "~3 administrations to 0.70"
    result_rationale: >
      Bayesian累积机制将前一轮的posterior作为下一轮的prior，对持续存在的DIF
      效应形成"证据放大器"。Medium effect(δ=1.0)在单次administration中power仅
      0.38(因cohort sample size有限)，但经3轮累积达0.68、4轮达0.76——每轮新增
      模型cohort为DIF估计提供incremental evidence，prior逐渐从uninformative
      收敛到informative。Large effect改善较小(0.72→0.94)因为起始power已较高，
      ceiling effect。FPR维持在0.042因为Bayesian framework在无真实DIF时posterior
      不会单向漂移——clean items的evidence在零附近random walk，不积累。
      这直接回应了Reviewer Concern #2(样本量不足)：即使单次cohort较小，
      累积3-4轮即可达到实用power。
    tables:
      - name: "Table 15: Cumulative Bayesian DIF Power by Administration"
        columns: [administration, n_new_models, cumulative_n, power_medium, power_large, fpr]
        rows:
          - [1, 80, 80, 0.38, 0.72, 0.040]
          - [2, 85, 165, 0.54, 0.85, 0.041]
          - [3, 90, 255, 0.68, 0.91, 0.043]
          - [4, 95, 350, 0.76, 0.94, 0.042]
    figures_description:
      - "Fig 7a: Power accumulation curve across administrations，medium和large effect两条线"
      - "Fig 7b: Bayesian posterior distribution evolution (4 panels)，showing prior→posterior convergence for a contaminated item"
      - "Fig 7c: FPR stability across administrations (flat line around 0.04)"
    analysis: >
      Cumulative Bayesian DIF是temporal monitoring的关键enabler。3轮累积后medium
      effect power从0.38升至0.68(1.79x)，使DIF方法的覆盖范围从仅large effects
      扩展至medium effects，与ensemble的其他信号互补。这将作为paper的"monitoring
      over time"叙事的核心证据。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      分析benchmark在progressive item replacement下的validity降解，
      建立理论bounds并empirically验证。
    expected_results:
      replacement_5pct_rho: 0.994
      replacement_10pct_rho: 0.985
      replacement_20pct_rho: 0.973
      replacement_50pct_rho: 0.941
      replacement_5pct_reliability: 0.922
      replacement_10pct_reliability: 0.919
      replacement_20pct_reliability: 0.918
      replacement_50pct_reliability: 0.908
      construct_coverage_5pct: 0.998
      construct_coverage_20pct: 0.982
      construct_coverage_50pct: 0.954
      theoretical_bound_slope: -0.0012
      empirical_slope: -0.0011
      theory_empirical_agreement_r: 0.98
      critical_replacement_threshold: 0.62
    result_rationale: >
      Graceful degradation的理论基础是：当替换题经过proper calibration后，每个
      替换引入的measurement error是独立的且bounded(由calibration accuracy控制)。
      因此validity降解近似线性(slope≈-0.0012 per percent replaced)而非catastrophic。
      5%替换几乎无影响(ρ=0.994)因为12508题中替换625题，大量anchor items吸收了
      噪声。20%替换(ρ=0.973)与plan_005的equating结果一致(那里替换了约14.7%的
      flagged items得到ρ=0.973)。50%替换仍保持ρ=0.941(超过0.95需要更精确的
      calibration)，说明framework具有高容量。理论bound(基于test information
      function分析)与empirical结果高度一致(r=0.98)，确认降解过程是可预测的。
      Critical threshold=62%(ρ降至0.93以下)为实践提供了safety margin。
    tables:
      - name: "Table 16: Graceful Degradation Under Progressive Replacement"
        columns: [replacement_pct, spearman_rho, reliability, construct_coverage, max_rank_change]
        rows:
          - [0, 1.000, 0.924, 1.000, 0]
          - [5, 0.994, 0.922, 0.998, 4]
          - [10, 0.985, 0.919, 0.993, 8]
          - [20, 0.973, 0.918, 0.982, 12]
          - [30, 0.961, 0.914, 0.972, 18]
          - [50, 0.941, 0.908, 0.954, 28]
      - name: "Table 17: Theoretical vs Empirical Degradation"
        columns: [metric, theoretical_slope, empirical_slope, agreement_r]
        rows:
          - [spearman_rho, -0.00120, -0.00114, 0.98]
          - [reliability, -0.00032, -0.00035, 0.97]
          - [construct_coverage, -0.00092, -0.00088, 0.99]
    figures_description:
      - "Fig 8a: Degradation curves (ρ, reliability, construct coverage) vs replacement %，theoretical bounds as shaded bands"
      - "Fig 8b: Rank stability heatmap across replacement rates，模型按ability排序"
      - "Fig 8c: Test Information Function comparison at 0%, 20%, 50% replacement"
    analysis: >
      Graceful degradation分析确立了self-healing benchmark的practical viability：
      即使替换50%的题目，benchmark仍保持ρ>0.94的排名一致性。线性降解模型
      的准确预测(r=0.98)使benchmark maintainer可以事先评估任何replacement plan
      的validity impact。这是Claim 3的robustness extension，回应了"替换多少题
      benchmark就失效了"的自然质疑。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      实现Item-Focused Trees，将model release date作为continuous covariate
      进行DIF检测，对比categorical cohort方法。
    expected_results:
      ift_tpr_large_effect: 0.82
      ift_tpr_medium_effect: 0.44
      ift_fpr: 0.039
      ift_vs_categorical_tpr_delta_large: +0.04
      ift_vs_categorical_tpr_delta_medium: +0.13
      ift_auc: 0.93
      categorical_auc: 0.91
      ift_split_points_detected: 3
      primary_split_date: "2023-07"
      secondary_split_date: "2024-03"
      tertiary_split_date: "2024-11"
      ift_computation_time_minutes: 45
      n_items_with_temporal_dif_trend: 2150
    result_rationale: >
      Item-Focused Trees将release date作为continuous covariate，避免了arbitrary
      cohort split的信息损失。IFT自动发现optimal split points，在best档检测到
      3个显著split：2023-07(GPT-4/LLaMA2时代开始，training data大规模扩张)、
      2024-03(post-training RL普及)、2024-11(reasoning model爆发)。
      Large effect TPR提升+0.04(0.82 vs 0.78)较modest，因为large effects在任何
      reasonable split下都能检测到。Medium effect提升+0.13(0.44 vs 0.31)更显著，
      因为IFT利用了full sample而非discarding cohort boundary附近的信息——
      categorical方法在2023年底release的模型被强制归入pre-2024或post-2024，
      引入misclassification noise；IFT将其作为连续梯度处理。AUC从0.91提升至0.93。
      IFT自动发现的split points提供了额外的scientific insight——contamination不是
      均匀增长而是在特定时间节点(对应training paradigm shifts)出现阶梯式跳跃。
    tables:
      - name: "Table 18: IFT vs Categorical DIF Comparison"
        columns: [method, tpr_large, tpr_medium, fpr, auc, requires_cohort_definition]
        rows:
          - [ETS_C_categorical, 0.78, 0.31, 0.035, 0.91, "yes"]
          - [Item_Focused_Trees, 0.82, 0.44, 0.039, 0.93, "no"]
          - [IFT_improvement, +0.04, +0.13, +0.004, +0.02, "-"]
      - name: "Table 19: IFT Detected Split Points"
        columns: [split_rank, date, interpretation, n_items_affected, mean_dif_magnitude]
        rows:
          - [1, "2023-07", "GPT-4 era / large-scale data expansion", 1420, 1.62]
          - [2, "2024-03", "Post-training RL adoption", 580, 1.28]
          - [3, "2024-11", "Reasoning model proliferation", 320, 1.45]
    figures_description:
      - "Fig 9a: IFT detected split points on timeline，与major model release events对齐"
      - "Fig 9b: Per-item DIF magnitude heatmap over continuous release date axis"
      - "Fig 9c: ROC comparison IFT vs categorical DIF"
    analysis: >
      IFT作为categorical DIF的complementary方法，在medium effects上提供显著增益
      且消除了cohort definition的主观性。自动发现的temporal split points为
      contamination dynamics提供了interpretable narrative。作为P2实验，这丰富了
      methodology toolkit但不改变core claims。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "234d489d-f51c-4705-a1ce-298c321ba075",
  "isSidechain": false,
  "requestId": "req_011CbEPCBVBsuhya86PLb4Es",
  "type": "assistant",
  "uuid": "bc8661a0-7b2a-4f7f-8fbc-f24d54ee5b3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DgfruVfzLNLzwLQueKAa4V",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9974,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12025,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9974
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：DIF在真实数据上复现仿真预测，RL鲁棒性实证确认，equating达到心理测量标准——原始three-claim framing完整成立 核心假设：['METABENCH MMLU响应矩阵中temporal cohort间存在可检测的DIF模式，且与MMLU-CF污染标注显著相关', 'RL训练模型coho…",
  "leafUuid": "bc8661a0-7b2a-4f7f-8fbc-f24d54ee5b3c",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF-based contamination detection for self-healing benchmarks",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：DIF在真实数据上复现仿真预测，RL鲁棒性实证确认，equating达到心理测量标准——原始three-claim framing完整成立 核心假设：['METABENCH MMLU响应矩阵中temporal cohort间存在可检测的DIF模式，且与MMLU-CF污染标注显著相关', 'RL训练模型coho…",
  "leafUuid": "bc8661a0-7b2a-4f7f-8fbc-f24d54ee5b3c",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF-based contamination detection for self-healing benchmarks",
  "sessionId": "21234657-3e54-488f-a743-b1a19a8c893b"
}
```

---
