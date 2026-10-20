# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：DIF在真实数据上信号微弱或FPR过高无法实用；RL-robustness优势不显著；核心'psychometric detection'假设在LLM

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/7d0d8a68-fd2a-484b-8e5b-a8af6081aedb.jsonl`
- **Structured JSON:** [`89c63a99bb3cd2d9e760.json`](../../sessions/89/89c63a99bb3cd2d9e760.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:54:34.221Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:54:34.221Z",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：DIF在真实数据上信号微弱或FPR过高无法实用；RL-robustness优势不显著；核心'psychometric detection'假设在LLM场景下不成立——需重新寻找angle\n核心假设：['真实LLM response data严重违反IRT假设——模型间ability维度不一致（architecture差异导致non-unidimensional response patterns），DIF信号被model heterogeneity淹没', 'Real contamination以partial/variant形式为主而非verbatim，导致item-level behavioral shift不足以在ICC上形成detectable DIF', 'RL-robustness差异不显著：DIF在RL下也退化（RL改变了ICC形状而非仅平移），或传统方法在RL下表现尚可', 'MMLU-CF ground truth本身noisy，无法提供有效外部验证', 'Ensemble中多信号共线性高——覆盖盲区的理论不成立，各signal flag同一批items', 'Bifactor model在5000+异构模型上不收敛或factor结构不可解释']\n关键指标范围：{'dif_tpr_real_data_delta_ge_1.4': [0.25, 0.5], 'dif_fpr_real_data': [0.08, 0.15], 'mmlu_cf_correlation_with_dif_flags': [0.0, 0.15], 'rl_power_retention_ratio': [0.5, 0.75], 'traditional_detector_auroc_under_rl': [0.55, 0.72], 'ensemble_tpr_full_spectrum': [0.35, 0.6], 'constat_tpr_non_rl_delta_ge_0.6': [0.2, 0.4], 'dvd_tpr_variant_contamination': [0.15, 0.35], 'equating_spearman_rho': [0.75, 0.88], 'gsm8k_gsm1k_gap_dif_correlation': [0.0, 0.18], 'difficulty_calibration_rho_student_sim': [0.4, 0.58]}\n叙事方向：核心\"DIF是RL-robust contamination signal\"假设不成立，需要reframe。 可行angle 1: \"Negative result + diagnostic framework\"——系统性地展示为什么psychometric DIF 在LLM场景下失效（IRT assumption violations的taxonomy），这本身是对growing IRT-for-LLM文献 （Growing Pains等）的重要warning。转化为\"when do psychometric tools transfer to LLM evaluation?\" 可行angle 2: \"Ensemble as empirical coverage map\"——即使单个signal弱， 通过large-scale empirical analysis（5000+ models × 12K items × 3 signals） 提供第一个contamination detection方法的systematic comparison under controlled conditions， 强调实验infrastructure和benchmark贡献（public detection toolkit + annotated contamination flags）。 可行angle 3: 放弃detection，pivot到Claim 3的regeneration—— bifactor IRT equating for benchmark versioning作为独立贡献， 即使不和contamination detection绑定，\"psychometrically equivalent benchmark updates\" 本身对LiveBench/DynaBench类工作是有价值的改进。 仍冲ICLR但需要完全重写introduction和story spine，timeline紧张但5个月内可行。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning 3 years of releases, DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026).\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: 'Apply DIF analysis to METABENCH MMLU response matrix (5,055 models\n    × 12,508 items). Split models into temporal cohorts by release date (pre-2024\n    vs post-2024, plus finer annual splits). Run ETS C DIF detection on all items.\n    Validate against MMLU-CF (ACL 2025) contamination-free items as partial ground\n    truth: items present in MMLU but significantly modified in MMLU-CF should correlate\n    with DIF flags. Sensitivity analysis across different cohort definitions and contamination\n    thresholds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: 'Empirically validate DIF''s RL-robustness claim. Construct two scenarios:\n    (a) cohort with SFT-only models, (b) cohort including RL-trained reasoning models\n    (DeepSeek-R1, Qwen-2.5-RL, etc. from METABENCH or via inference). Run DIF + traditional\n    detectors (Min-K%, ConStat perturbation, DVD) on both scenarios. Show DIF maintains\n    detection power in scenario (b) while traditional detectors degrade. If METABENCH\n    lacks RL-trained models, run inference on 10-15 open-weight RL models on MMLU.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations Depends on 003a and 003b\n    completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond MMLU-CF.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:54:34.225Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:54:34.225Z",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T19:54:34.248Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：DIF在真实数据上信号微弱或FPR过高无法实用；RL-robustness优势不显著；核心'psychometric detection'假设在LLM场景下不成立——需重新寻找angle
核心假设：['真实LLM response data严重违反IRT假设——模型间ability维度不一致（architecture差异导致non-unidimensional response patterns），DIF信号被model heterogeneity淹没', 'Real contamination以partial/variant形式为主而非verbatim，导致item-level behavioral shift不足以在ICC上形成detectable DIF', 'RL-robustness差异不显著：DIF在RL下也退化（RL改变了ICC形状而非仅平移），或传统方法在RL下表现尚可', 'MMLU-CF ground truth本身noisy，无法提供有效外部验证', 'Ensemble中多信号共线性高——覆盖盲区的理论不成立，各signal flag同一批items', 'Bifactor model在5000+异构模型上不收敛或factor结构不可解释']
关键指标范围：{'dif_tpr_real_data_delta_ge_1.4': [0.25, 0.5], 'dif_fpr_real_data': [0.08, 0.15], 'mmlu_cf_correlation_with_dif_flags': [0.0, 0.15], 'rl_power_retention_ratio': [0.5, 0.75], 'traditional_detector_auroc_under_rl': [0.55, 0.72], 'ensemble_tpr_full_spectrum': [0.35, 0.6], 'constat_tpr_non_rl_delta_ge_0.6': [0.2, 0.4], 'dvd_tpr_variant_contamination': [0.15, 0.35], 'equating_spearman_rho': [0.75, 0.88], 'gsm8k_gsm1k_gap_dif_correlation': [0.0, 0.18], 'difficulty_calibration_rho_student_sim': [0.4, 0.58]}
叙事方向：核心"DIF是RL-robust contamination signal"假设不成立，需要reframe。 可行angle 1: "Negative result + diagnostic framework"——系统性地展示为什么psychometric DIF 在LLM场景下失效（IRT assumption violations的taxonomy），这本身是对growing IRT-for-LLM文献 （Growing Pains等）的重要warning。转化为"when do psychometric tools transfer to LLM evaluation?" 可行angle 2: "Ensemble as empirical coverage map"——即使单个signal弱， 通过large-scale empirical analysis（5000+ models × 12K items × 3 signals） 提供第一个contamination detection方法的systematic comparison under controlled conditions， 强调实验infrastructure和benchmark贡献（public detection toolkit + annotated contamination flags）。 可行angle 3: 放弃detection，pivot到Claim 3的regeneration—— bifactor IRT equating for benchmark versioning作为独立贡献， 即使不和contamination detection绑定，"psychometrically equivalent benchmark updates" 本身对LiveBench/DynaBench类工作是有价值的改进。 仍冲ICLR但需要完全重写introduction和story spine，timeline紧张但5个月内可行。

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
  "promptId": "25fb28cb-c4f2-490e-b63e-5bd1111b4401",
  "type": "user",
  "uuid": "6a5bf5d5-a134-433d-80b2-34309de8ce01",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:54:34.246Z_

```json
{
  "parentUuid": "6a5bf5d5-a134-433d-80b2-34309de8ce01",
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
  "uuid": "c3a84f40-b5b8-44e4-adca-ce5f98247b8a",
  "timestamp": "2026-05-20T19:54:34.246Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:54:34.247Z_

```json
{
  "parentUuid": "c3a84f40-b5b8-44e4-adca-ce5f98247b8a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "719b40bf-34c4-4695-9b93-18e8ccb70d4e",
  "timestamp": "2026-05-20T19:54:34.247Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DIF在真实数据上信号微弱或FPR过高无法实用；RL-robustness优势不显著；核心'psychometric detection'假设在LLM场景下不成立——需重新寻找angle 核心假设：['真实LLM response data严重违反IRT假设——模型间ability维度不一致（archite…",
  "leafUuid": "719b40bf-34c4-4695-9b93-18e8ccb70d4e",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination detection via DIF and psychometric equating",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:54:55.539Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, under the "worst" tier scenario. I need to provide specific metric predictions with rationales explaining why those results would occur under the worst-case assumptions.

Let me go through each planned experiment and generate worst-tier predictions.

Let me carefully review the worst tier definition:

- DIF signal weak on real data or FPR too high
- RL-robustness advantage not significant
- Core 'psychometric detection' hypothesis doesn't hold for LLMs
- Need to find a new angle

Key assumptions for worst tier:


Real LLM response data severely violates IRT assumptions due to model heterogeneity drowning out the DIF signal, real contamination is only partial or variant rather than verbatim so item-level behavioral shifts are insufficient, RL-robustness differences don't materialize as significant, MMLU-CF ground truth is too noisy, ensemble signals end up collinear without covering each other's blind spots, and the bifactor model either fails to converge or produces uninterpretable factor structures on the large heterogeneous dataset. Now I'm setting the metric ranges for worst-case performance, starting with DIF TPR delta predictions in the 0.25 to 0.5 range and examining what FPR thresholds would look like. Now I'm looking at the difficulty calibration metric with student similarity, then moving on to generate predictions across nine planned experiments ranging from real data difficulty analysis to item-focused tree evaluations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "719b40bf-34c4-4695-9b93-18e8ccb70d4e",
  "isSidechain": false,
  "requestId": "req_011CbEQarXS2z2TSrdtfjhyr",
  "type": "assistant",
  "uuid": "ce953908-91ce-47c6-be4f-eaff661cb7bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DtmMuicC1zeFsfWBoRQb3Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10703,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12443,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10703
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

_source line 9 · 2026-05-20T19:58:48.748Z_

```yaml
tier: worst
narrative_guidance: >
  核心"DIF是RL-robust contamination signal"假设不成立。5000+异构模型的response matrix严重违反IRT
  unidimensionality假设，architecture差异（encoder-only vs decoder-only vs MoE）制造了大量
  spurious DIF，FPR膨胀至实用边界之外。真实contamination以partial memorization为主，
  ICC shift不足以在高噪声背景下被检出。RL-robustness优势不显著——传统方法在RL下虽然退化，
  但DIF也退化，差距不足以支撑"orthogonal signal"叙事。需要pivot到negative-result framing
  或剥离Claim 3做独立贡献。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      对METABENCH MMLU response matrix (5,055 models × 12,508 items)执行temporal cohort DIF分析，
      以MMLU-CF为partial ground truth验证。
    expected_results:
      dif_tpr_delta_ge_1.4: 0.38
      dif_tpr_delta_ge_1.0: 0.18
      dif_fpr: 0.12
      mmlu_cf_correlation_with_dif_flags_phi: 0.09
      mmlu_cf_correlation_with_dif_flags_spearman: 0.07
      irt_model_fit_rmsea: 0.11
      irt_model_fit_cfi: 0.78
      n_items_flagged_ets_c: 1840
      n_items_flagged_ets_c_after_fpr_correction: 620
      cohort_size_pre2024: 1850
      cohort_size_post2024: 3205
      unidimensionality_test_p: 0.001
      item_discrimination_variance: 2.8
    result_rationale: >
      5055个模型跨越encoder-only (BERT-family)、decoder-only (GPT/LLaMA family)、MoE等根本不同
      的architecture，对MMLU items的response pattern受architecture驱动而非ability驱动。例如
      decoder-only模型在long-context reasoning items上系统性优于encoder-only模型，这与contamination
      无关但产生大量DIF。RMSEA=0.11远超可接受阈值(0.06)，CFI=0.78低于0.90标准，表明unidimensional
      IRT model严重misfit。在此背景下ETS C的effect-size threshold无法区分architecture-driven DIF
      和contamination-driven DIF，导致FPR膨胀至0.12。1840个items被flagged（15%的item pool），
      其中大部分是false positives。与MMLU-CF的correlation仅phi=0.09，接近random——因为MMLU-CF
      本身的contamination annotation也有噪声（它只标注了"显著修改"的items，但并未验证原始items
      确实被contaminated），加上DIF flags被spurious signal淹没，两个noisy signal之间几乎无相关。
    tables:
      - title: "Table 1: DIF Detection Performance on METABENCH MMLU (Worst Tier)"
        columns: [metric, pre2024_vs_post2024, annual_cohorts, sliding_window_6mo]
        rows:
          - [TPR_delta_ge_1.4, 0.38, 0.31, 0.28]
          - [TPR_delta_ge_1.0, 0.18, 0.14, 0.12]
          - [FPR, 0.12, 0.14, 0.15]
          - [F1_delta_ge_1.4, 0.33, 0.28, 0.25]
          - [N_flagged_items, 1840, 2100, 2350]
          - [MMLU-CF_phi_correlation, 0.09, 0.07, 0.06]
      - title: "Table 2: IRT Model Fit Diagnostics"
        columns: [fit_index, value, acceptable_threshold, verdict]
        rows:
          - [RMSEA, 0.11, "≤0.06", FAIL]
          - [CFI, 0.78, "≥0.90", FAIL]
          - [TLI, 0.74, "≥0.90", FAIL]
          - [SRMR, 0.09, "≤0.08", FAIL]
          - [M2_p_value, "<0.001", ">0.05", FAIL]
    figures_description:
      - "Fig 1: ICC overlay of 20 highest-DIF items — curves show chaotic crossing patterns
        rather than clean uniform/non-uniform DIF, suggesting architecture heterogeneity
        rather than contamination as primary driver"
      - "Fig 2: DIF effect size distribution — bimodal with large peak near zero and long
        right tail, but right tail items do not correlate with MMLU-CF contamination markers"
      - "Fig 3: Heatmap of DIF flags × model architecture family — shows systematic DIF
        patterns aligned with architecture rather than temporal cohort"
    analysis: >
      核心发现：real data上IRT model严重misfit，DIF检测被architecture heterogeneity主导。
      Simulation中（Phase 2, N=100, δ=1.4, TPR=0.76）的performance无法迁移到real data，
      因为simulation假设了unidimensional ability和homogeneous population——这在5055个异构模型上
      完全不成立。FPR=0.12意味着每1000个clean items中有120个被错误flagged，在MMLU的12508个items
      上产生约1500个false positives，淹没了真正的contamination signal。MMLU-CF validation几乎
      为negative（phi=0.09），无法作为DIF有效性的支撑证据。结论：categorical temporal cohort DIF
      在heterogeneous model population上不可直接使用。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      对比DIF与传统检测器在包含/不包含RL-trained模型的cohort上的表现差异。
    expected_results:
      dif_tpr_sft_only_delta_ge_1.4: 0.42
      dif_tpr_with_rl_delta_ge_1.4: 0.29
      dif_power_retention_ratio: 0.69
      traditional_mink_auroc_sft: 0.74
      traditional_mink_auroc_rl: 0.58
      traditional_constat_auroc_sft: 0.71
      traditional_constat_auroc_rl: 0.61
      traditional_dvd_auroc_sft: 0.68
      traditional_dvd_auroc_rl: 0.55
      dif_auroc_sft: 0.67
      dif_auroc_rl: 0.54
      dif_vs_traditional_auroc_gap_under_rl: 0.02
      n_rl_models_available: 12
      rl_model_cohort_size: 12
    result_rationale: >
      RL-robustness假设的理论基础是"DIF操作在group-level ICC上，RL只平移不改变ICC形状"。但worst
      情景下RL不仅平移ICC——GRPO/PPO通过reward shaping改变了模型在不同difficulty levels上的response
      pattern，导致ICC形状本身变化（slope变陡或变平）。这使得RL-trained模型与SFT模型之间的ICC差异
      既来自contamination也来自training method，DIF无法区分二者。DIF在RL cohort下power从0.42降到
      0.29（retention ratio=0.69），传统方法从~0.71降到~0.58。关键是DIF的降幅比例与传统方法相当，
      AUROC差距仅0.02——不足以支撑"DIF是RL-orthogonal signal"的核心论点。此外，可获取的RL模型
      仅12个（METABENCH中标注为RL-trained的开源模型有限），cohort太小导致DIF统计功效本身就低，
      难以将power loss归因于RL vs simply small N。
    tables:
      - title: "Table 3: RL-Robustness Comparison — DIF vs Traditional Detectors"
        columns: [method, auroc_sft_cohort, auroc_rl_cohort, retention_ratio, delta_auroc]
        rows:
          - [DIF_ETS_C, 0.67, 0.54, 0.81, -0.13]
          - [Min-K%, 0.74, 0.58, 0.78, -0.16]
          - [ConStat, 0.71, 0.61, 0.86, -0.10]
          - [DVD, 0.68, 0.55, 0.81, -0.13]
          - [Perplexity, 0.69, 0.56, 0.81, -0.13]
      - title: "Table 4: DIF TPR Under SFT vs RL Cohorts"
        columns: [effect_size, tpr_sft_only, tpr_with_rl, retention]
        rows:
          - ["δ≥1.6", 0.48, 0.35, 0.73]
          - ["δ≥1.4", 0.42, 0.29, 0.69]
          - ["δ≥1.0", 0.20, 0.13, 0.65]
          - ["δ≥0.6", 0.09, 0.06, 0.67]
    figures_description:
      - "Fig 4: ROC curves for all 5 methods under SFT-only vs RL-included cohorts —
        all curves shift left/down under RL, with DIF and traditional methods degrading
        similarly (overlapping confidence intervals)"
      - "Fig 5: ICC comparison for 5 known-contaminated items — RL models show altered
        slope (not just intercept shift), violating the theoretical basis of DIF robustness"
    analysis: >
      DIF的RL-robustness优势不显著。AUROC under RL: DIF 0.54 vs best traditional 0.61 (ConStat)，
      DIF实际上略差于ConStat。Power retention ratio 0.69落在worst tier预测范围[0.5, 0.75]内。
      核心问题：RL改变ICC形状（discrimination parameter a也变化），不仅仅是difficulty shift，
      这意味着DIF的理论robustness argument不成立。加上RL cohort sample size仅12，统计结论的
      可靠性本身存疑。无法支撑paper的headline claim。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      独立评估ConStat-style perturbation testing在MMLU上的contamination检测能力。
    expected_results:
      constat_tpr_non_rl_delta_ge_0.6: 0.32
      constat_tpr_non_rl_delta_ge_1.0: 0.45
      constat_tpr_non_rl_delta_ge_1.4: 0.55
      constat_tpr_rl_delta_ge_0.6: 0.11
      constat_tpr_rl_delta_ge_1.0: 0.18
      constat_fpr: 0.06
      constat_fdr_controlled_power: 0.28
      n_perturbation_items_generated: 220
      perturbation_quality_human_equiv_rate: 0.82
      paraphrase_semantic_similarity: 0.91
    result_rationale: >
      ConStat在non-RL模型上有中等检测力（TPR=0.32 for δ≥0.6），因为SFT模型对verbatim
      memorized items的perturbation确实敏感——答对原题但答错改写题是contamination的合理信号。
      但在worst tier下：(1) 真实contamination多为partial memorization，模型可能只记住了answer
      pattern而非exact wording，对perturbation同样答对，降低sensitivity；(2) LLM paraphrase
      生成的reformulations质量参差——82%被判为semantically equivalent，但18%引入了微妙的
      difficulty变化，增加noise；(3) RL模型对perturbation的sensitivity本身就低（RL鼓励
      generalization），RL场景下TPR骤降至0.11。FDR-controlled power仅0.28，意味着在控制
      false discovery rate后，能检出的contaminated items不到三分之一。作为standalone result
      有一定baseline价值，但不足以独立成章。
    tables:
      - title: "Table 5: ConStat Perturbation Detection by Effect Size and Model Type"
        columns: [effect_size, tpr_sft, tpr_rl, tpr_mixed, fpr]
        rows:
          - ["δ≥1.4", 0.55, 0.18, 0.38, 0.06]
          - ["δ≥1.0", 0.45, 0.14, 0.30, 0.06]
          - ["δ≥0.6", 0.32, 0.11, 0.22, 0.07]
          - ["δ≥0.4", 0.19, 0.08, 0.14, 0.07]
    figures_description:
      - "Fig 6: ConStat detection power as function of perturbation intensity — diminishing
        returns beyond moderate paraphrasing, suggesting contamination is not purely
        surface-form dependent"
    analysis: >
      ConStat在non-RL场景下对large effects有moderate power，但RL场景下急剧退化。作为ensemble
      component对non-RL覆盖有限值，但无法作为RL-robust complement to DIF（两者在RL下都弱）。
      FDR-controlled power 0.28意味着实际可用的detection capacity很有限。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      独立评估DVD generation variance方法在MMLU上检测variant contamination的能力。
    expected_results:
      dvd_tpr_variant_contamination: 0.22
      dvd_tpr_verbatim_contamination: 0.48
      dvd_tpr_partial_contamination: 0.12
      dvd_fpr: 0.09
      dvd_auroc_overall: 0.61
      n_models_evaluated: 13
      n_items_sampled: 500
      responses_per_item: 50
      bimodal_distribution_rate_contaminated: 0.18
      bimodal_distribution_rate_clean: 0.07
      gpu_hours_used: 65
    result_rationale: >
      DVD的理论基础是contaminated items上model generation variance呈bimodal分布（有时recall
      memorized answer，有时不能）。在worst tier下：(1) variant contamination（题目被改写后
      contaminated）信号最弱——模型对variant的memorization不稳定，generation variance与clean
      items差异小，TPR仅0.22；(2) partial contamination（仅记住部分信息）几乎无法检测（TPR=0.12），
      因为partial memory不产生bimodal response pattern，而是持续的uncertainty；(3) 即使verbatim
      contamination，TPR也仅0.48，因为很多模型在temperature sampling下对已知答案也表现stable
      （always correct），generation variance反而很低——与clean but easy items难以区分；(4)
      bimodal rate在contaminated items上仅18% vs clean items 7%，差异有统计显著性但effect size
      太小无法做reliable detection。FPR=0.09偏高。总计消耗65 GPU hours，性价比低。
    tables:
      - title: "Table 6: DVD Detection by Contamination Type"
        columns: [contamination_type, tpr, fpr, auroc, n_items]
        rows:
          - [verbatim, 0.48, 0.09, 0.72, 120]
          - [variant, 0.22, 0.09, 0.58, 180]
          - [partial, 0.12, 0.09, 0.52, 200]
          - [overall, 0.25, 0.09, 0.61, 500]
    figures_description:
      - "Fig 7: Generation variance distributions for contaminated vs clean items —
        overlapping distributions with small separation, bimodal pattern only visible
        in subset of verbatim contamination cases"
    analysis: >
      DVD对variant contamination的检测力远低于预期（TPR=0.22 vs 论文claim需要的高coverage）。
      核心问题是real-world contamination不产生clean bimodal response pattern——partial memorization
      导致diffuse variance而非bimodal variance。GPU开销大但回报低，作为ensemble component
      贡献有限。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      将DIF + ConStat + DVD融合为多信号ensemble，评估覆盖度和precision。
    expected_results:
      ensemble_tpr_full_spectrum: 0.42
      ensemble_tpr_delta_ge_1.4: 0.52
      ensemble_tpr_delta_ge_1.0: 0.30
      ensemble_tpr_delta_ge_0.6: 0.18
      ensemble_fpr: 0.11
      ensemble_f1: 0.35
      majority_voting_tpr: 0.38
      weighted_fusion_tpr: 0.42
      signal_correlation_dif_constat: 0.61
      signal_correlation_dif_dvd: 0.54
      signal_correlation_constat_dvd: 0.58
      unique_items_flagged_by_only_one_signal_pct: 0.15
      items_flagged_by_all_three_pct: 0.42
    result_rationale: >
      Ensemble假设三个signal互补——DIF覆盖large effects+RL场景，ConStat覆盖non-RL medium effects，
      DVD覆盖variant contamination。但worst tier下：(1) 三个signal之间correlation高（r=0.54-0.61），
      表明它们largely flag同一批items而非互补覆盖不同盲区；(2) 仅15%的items被unique地由某一个
      signal单独检出，说明"互补覆盖"理论不成立——各signal的failure modes相关（都在partial/medium
      effect上失败）；(3) 42%的items被三个signal同时flag，说明easy cases三者都能检出但hard cases
      三者都漏检；(4) FPR=0.11，majority voting无法有效压低FPR因为false positives也呈相关模式
      （architecture-driven spurious DIF也往往在perturbation testing中产生false positive）。
      Weighted fusion比majority voting略好（TPR 0.42 vs 0.38）但提升有限。整体full-spectrum
      TPR=0.42落在worst tier [0.35, 0.6]范围内，不足以作为实用detection system。
    tables:
      - title: "Table 7: Ensemble vs Individual Signal Performance"
        columns: [method, tpr_ge_1.4, tpr_ge_1.0, tpr_ge_0.6, fpr, f1]
        rows:
          - [DIF_only, 0.38, 0.18, 0.09, 0.12, 0.25]
          - [ConStat_only, 0.38, 0.30, 0.22, 0.06, 0.32]
          - [DVD_only, 0.25, 0.15, 0.10, 0.09, 0.18]
          - [Majority_2of3, 0.38, 0.19, 0.11, 0.05, 0.30]
          - [Weighted_fusion, 0.52, 0.30, 0.18, 0.11, 0.35]
      - title: "Table 8: Signal Correlation Matrix"
        columns: [signal_pair, pearson_r, overlap_in_flagged_items_pct]
        rows:
          - [DIF-ConStat, 0.61, 0.68]
          - [DIF-DVD, 0.54, 0.59]
          - [ConStat-DVD, 0.58, 0.63]
    figures_description:
      - "Fig 8: Venn diagram of items flagged by each signal — large central overlap,
        small unique regions, contradicting the 'complementary coverage' hypothesis"
      - "Fig 9: Ensemble TPR as function of effect size — flat improvement over best
        individual signal, no 'coverage completion' effect at medium/low effects"
    analysis: >
      Ensemble的"互补覆盖"核心假设不成立。信号间高相关（0.54-0.61）意味着ensemble主要在置信度上
      提升（对已检出items更confident）而非在覆盖度上提升（检出新items）。Weighted fusion的TPR=0.42
      仅比best individual signal (ConStat 0.30 at δ≥1.0) 提升有限，且FPR=0.11偏高。这个ensemble
      不能作为"full-spectrum detection system"呈现——更准确的描述是"three weak signals with
      correlated failure modes"。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      在GSM8K上复制DIF分析，以GSM1K作为contamination ground truth进行交叉验证。
    expected_results:
      gsm8k_gsm1k_gap_dif_correlation_spearman: 0.11
      gsm8k_gsm1k_gap_dif_correlation_pearson: 0.08
      dif_tpr_gsm8k_delta_ge_1.4: 0.30
      dif_fpr_gsm8k: 0.13
      n_models_with_both_gsm8k_gsm1k: 48
      irt_model_fit_rmsea_gsm8k: 0.09
      gsm8k_item_discrimination_mean: 0.85
      gsm1k_gap_mean_across_models: 0.07
      gsm1k_gap_std: 0.11
      n_items_gsm8k_analyzed: 1319
    result_rationale: >
      GSM8K validation在worst tier下面临多重困难：(1) 可获取的同时有GSM8K和GSM1K结果的模型仅
      约48个（远少于MMLU的5055个），DIF统计功效严重不足；(2) GSM8K是math benchmark，item
      discrimination偏低(mean a=0.85)因为数学题的对错更binary、less informative about latent
      ability gradient，这直接降低DIF detection power；(3) GSM8K-GSM1K gap本身noisy（std=0.11
      vs mean=0.07），gap的model-level variance高说明contamination不是uniform的——不同模型
      contamination程度差异大，但DIF是item-level metric，model-level gap与item-level DIF
      flag之间的mapping本就不是直接对应的；(4) GSM1K作为ground truth的assumption是"GSM1K
      uncontaminated"，但GSM1K发布后也可能被contaminated，ground truth本身会退化。
      Spearman rho=0.11几乎无相关，无法支撑cross-benchmark generalizability。
    tables:
      - title: "Table 9: GSM8K Cross-Validation Results"
        columns: [metric, value, worst_tier_range, verdict]
        rows:
          - [DIF_TPR_δ≥1.4, 0.30, "0.25-0.50", IN_RANGE]
          - [DIF_FPR, 0.13, "0.08-0.15", IN_RANGE]
          - [GSM8K-GSM1K_gap_correlation, 0.11, "0.0-0.18", IN_RANGE]
          - [N_models, 48, "≥50 desired", INSUFFICIENT]
          - [IRT_fit_RMSEA, 0.09, "≤0.06", FAIL]
    figures_description:
      - "Fig 10: Scatter plot of per-model GSM8K-GSM1K gap vs number of DIF-flagged items
        in that model's performance — near-zero correlation with wide scatter"
    analysis: >
      Cross-benchmark validation为negative result。GSM8K上DIF表现与MMLU类似（low TPR, high FPR），
      且与GSM1K ground truth的correlation接近零（rho=0.11）。样本量不足（48 models vs desired 50+）
      进一步削弱统计结论的可靠性。这不能作为DIF generalizability的支撑证据。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      在METABENCH MMLU数据上拟合bifactor IRT模型，选取anchor items，执行equating pilot。
    expected_results:
      bifactor_convergence: partial
      bifactor_iterations_to_convergence: 8500
      bifactor_n_items_converged: 9200
      bifactor_n_items_failed: 3308
      general_factor_variance_explained: 0.35
      n_specific_factors: 57
      specific_factor_avg_loading: 0.28
      anchor_item_n_selected: 380
      anchor_item_stability_mean_dif: 0.15
      equating_spearman_rho_before: 0.82
      equating_spearman_rho_after: 0.85
      equating_rank_displacement_mean: 3.2
      equating_rank_displacement_p95: 12
      score_reliability_original: 0.94
      score_reliability_equated: 0.89
    result_rationale: >
      Bifactor model在5055个异构模型上面临严重的estimation challenge：(1) 57个MMLU subjects作为
      specific factors，加上1个general factor，parameter space巨大（~12500 items × 3 parameters
      × 58 factors），在worst tier下3308个items（26%）的参数估计不收敛或产生Heywood cases
      （negative variance estimates）；(2) general factor仅解释35%的variance——这意味着MMLU
      不是primarily measuring一个general LLM ability，而是highly multidimensional的，bifactor
      structure不是good fit；(3) specific factor loadings平均仅0.28，说明subject-level factors
      也很弱，很多items不清晰地load在任何factor上——factor structure不可解释；(4) 尽管如此，
      equating在技术上仍可执行：选出380个stable anchor items（无DIF、参数估计收敛），equating
      后ranking correlation从0.82提升到0.85，但这个提升幅度小（Δ=0.03），且基线rho=0.82
      已低于Claim 3要求的0.95标准。Equating没有失败但也没有convincingly成功——它能small
      improvement ranking stability，但不能达到psychometric equivalence的标准。
    tables:
      - title: "Table 10: Bifactor IRT Model Fit and Equating Results"
        columns: [metric, value, target, verdict]
        rows:
          - [convergence_rate, "73.5%", "≥95%", FAIL]
          - [general_factor_variance, 0.35, "≥0.50", WEAK]
          - [anchor_items_available, 380, "≥500", MARGINAL]
          - [equating_rho, 0.85, "≥0.95", FAIL]
          - [rank_displacement_p95, 12, "≤5", FAIL]
          - [score_reliability_post, 0.89, "≥0.92", MARGINAL]
      - title: "Table 11: Factor Structure Summary"
        columns: [factor_type, n_factors, mean_loading, pct_items_loading_gt_0.3]
        rows:
          - [general, 1, 0.42, "62%"]
          - [specific_STEM, 14, 0.31, "38%"]
          - [specific_humanities, 18, 0.26, "29%"]
          - [specific_social_science, 15, 0.28, "33%"]
          - [specific_other, 10, 0.24, "25%"]
    figures_description:
      - "Fig 11: Scree plot showing eigenvalues — no clear elbow, gradual decline
        suggesting no dominant general factor"
      - "Fig 12: Equated vs original model rankings — scatter with regression line
        showing moderate but not strong agreement (rho=0.85), notable outliers at tails"
    analysis: >
      Bifactor model在异构LLM population上partially converges但factor structure不清晰。
      General factor太弱（35% variance）挑战了"MMLU measures a coherent construct"的前提。
      Equating产生了modest improvement (0.82→0.85) 但远未达到psychometric equivalence标准
      (0.95)。作为独立贡献（Claim 3 standalone），这个result需要被framed为"benchmark
      multidimensionality的empirical characterization"而非"successful equating"。可能可以
      pivot到Growing Pains style的"LLM evaluation需要multidimensional IRT"叙事。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      生成替代items并通过student simulation进行calibration，评估difficulty estimation质量。
    expected_results:
      n_items_generated: 150
      n_items_passing_quality_filter: 112
      difficulty_calibration_rho_student_sim: 0.48
      difficulty_calibration_rho_prompt_based: 0.22
      difficulty_mae_student_sim: 0.85
      difficulty_mae_prompt_based: 1.45
      discrimination_calibration_rho: 0.31
      construct_alignment_rate: 0.72
      holdout_validation_rho: 0.44
      student_sim_correlation_with_real_models: 0.52
      gpu_hours_used: 180
    result_rationale: >
      Item generation在worst tier下的核心问题：(1) Student simulation (arXiv 2601.09953)
      的difficulty estimation在MMLU上表现弱于其在其他benchmarks上的reported results——因为
      MMLU covers 57 diverse subjects，student simulation的"simulated students"是single LLM
      做capability ablation，但不同subject需要不同type的knowledge/reasoning，single-model
      simulation无法capture this diversity，rho=0.48；(2) Prompt-based difficulty targeting
      依然很差（rho=0.22），与文献报告一致；(3) Student simulation比prompt-based好（0.48 vs 0.22）
      但absolute accuracy仍不够——difficulty MAE=0.85 logits意味着平均偏差接近1个标准差，
      生成的items实际difficulty与target可能差1-2个difficulty band；(4) Discrimination calibration
      更差（rho=0.31），因为discrimination是更subtle的item property，依赖于item如何在不同ability
      levels上区分模型，student simulation几乎无法capture；(5) Construct alignment rate 72%
      意味着28%的generated items虽然表面上是同一subject但实际测量的cognitive process不同
      （e.g., 要求recall的item被替换为要求reasoning的item）。这些result不支撑"calibrated
      item regeneration"的claim，但student sim vs prompt-based的comparison本身有文献价值。
    tables:
      - title: "Table 12: Item Calibration Comparison"
        columns: [method, difficulty_rho, difficulty_mae, discrimination_rho, construct_alignment]
        rows:
          - [student_simulation, 0.48, 0.85, 0.31, "72%"]
          - [prompt_based, 0.22, 1.45, 0.18, "65%"]
          - [random_baseline, 0.05, 1.80, 0.08, "45%"]
      - title: "Table 13: Holdout Validation on 30 Models"
        columns: [metric, student_sim, prompt_based]
        rows:
          - [difficulty_rank_correlation, 0.44, 0.19]
          - [score_equivalence_rho, 0.78, 0.68]
          - [ranking_preservation_top10, "70%", "50%"]
    figures_description:
      - "Fig 13: Predicted vs actual item difficulty — student simulation shows moderate
        correlation but with substantial scatter, especially for very hard items"
      - "Fig 14: Distribution of difficulty estimation errors — student simulation
        has tighter but still wide distribution (SD=0.85) compared to prompt-based (SD=1.2)"
    analysis: >
      Student simulation在MMLU上的calibration quality不足以支撑reliable item replacement。
      Difficulty rho=0.48意味着替换后的benchmark与原版在difficulty ordering上只有moderate
      agreement，不够做psychometric equating。但student sim vs prompt-based的comparison
      （0.48 vs 0.22）以及failure mode analysis（which subjects/difficulty ranges失败）
      仍有独立的文献贡献价值。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      实现cumulative Bayesian DIF priors，模拟4次successive benchmark administrations的power积累。
    expected_results:
      single_admin_power_delta_1.0: 0.15
      cumulative_power_2_admins_delta_1.0: 0.22
      cumulative_power_3_admins_delta_1.0: 0.30
      cumulative_power_4_admins_delta_1.0: 0.38
      single_admin_power_delta_1.4: 0.35
      cumulative_power_4_admins_delta_1.4: 0.55
      bayesian_fpr_single: 0.10
      bayesian_fpr_cumulative_4: 0.08
      prior_informativeness_shrinkage: 0.45
    result_rationale: >
      Bayesian cumulative priors在worst tier下受到两个因素制约：(1) 如果baseline single-admin
      power已经很低（0.15 for δ=1.0，因为real data上IRT model misfit），那么cumulative
      evidence accumulation的起点就低——Bayesian updating from a weak prior仍然是weak，
      4次admin后仅到0.38（远低于theoretical prediction of 0.70）；(2) Prior informativeness
      受model population heterogeneity影响——如果每次administration的model cohort composition
      很不同（architecture mix变化），prior从上一admin的posterior transfer不顺畅，shrinkage
      factor高达0.45（理想应<0.2），意味着prior对posterior的influence被data overwhelm但data
      本身noisy。FPR从0.10降至0.08是modest improvement。总体而言，cumulative approach能
      提升power但幅度远不如simulated homogeneous scenarios中的预期。
    tables:
      - title: "Table 14: Cumulative Bayesian DIF Power Accumulation"
        columns: [n_administrations, power_delta_1.0, power_delta_1.4, fpr]
        rows:
          - [1, 0.15, 0.35, 0.10]
          - [2, 0.22, 0.42, 0.09]
          - [3, 0.30, 0.49, 0.09]
          - [4, 0.38, 0.55, 0.08]
    figures_description:
      - "Fig 15: Power accumulation curves — shallow slope compared to theoretical
        prediction (dashed line), gap widens with each administration due to
        population heterogeneity"
    analysis: >
      Cumulative Bayesian approach有边际收益但无法rescue低baseline power。4 admins后power
      仅从0.15升至0.38 (δ=1.0)，远低于theoretical 0.70。Population heterogeneity导致prior
      transfer效率低。作为P2 experiment，结果不改变overall narrative但进一步确认了DIF在
      heterogeneous LLM population上的fundamental limitations。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      分析benchmark在progressive item replacement下的validity degradation。
    expected_results:
      ranking_stability_5pct_replaced: 0.94
      ranking_stability_10pct_replaced: 0.88
      ranking_stability_20pct_replaced: 0.79
      ranking_stability_50pct_replaced: 0.62
      score_reliability_5pct: 0.92
      score_reliability_10pct: 0.88
      score_reliability_20pct: 0.81
      score_reliability_50pct: 0.67
      construct_coverage_5pct: 0.97
      construct_coverage_10pct: 0.93
      construct_coverage_20pct: 0.85
      construct_coverage_50pct: 0.71
      critical_replacement_threshold: 0.12
    result_rationale: >
      Graceful degradation在worst tier下退化快于预期因为：(1) Item calibration quality差
      （difficulty rho=0.48 from plan_006），替换items的psychometric properties与被替换items
      不匹配，每次替换引入的error大于calibration error budget允许的范围；(2) Bifactor equating
      不充分（rho=0.85 from plan_005），equating本身引入systematic bias，累积到20%替换时
      ranking stability降至0.79（如果equating完美，应维持在0.92+）；(3) Construct coverage
      degradation因为28%的generated items construct alignment有问题（from plan_006），
      20%替换时约5-6%的items测量不同construct，coverage降至0.85。Critical threshold（ranking
      rho降至0.90以下的替换比例）仅12%——意味着实际上只能安全替换约1500个items，远少于
      potential contaminated items的数量（如果FPR=0.12则约1800个被flag）。
    tables:
      - title: "Table 15: Validity Degradation Under Progressive Replacement"
        columns: [replacement_pct, ranking_rho, reliability, construct_coverage]
        rows:
          - ["0% (baseline)", 1.00, 0.94, 1.00]
          - ["5%", 0.94, 0.92, 0.97]
          - ["10%", 0.88, 0.88, 0.93]
          - ["20%", 0.79, 0.81, 0.85]
          - ["50%", 0.62, 0.67, 0.71]
      - title: "Table 16: Critical Thresholds"
        columns: [validity_criterion, threshold_value, max_safe_replacement_pct]
        rows:
          - [ranking_rho_≥0.90, 0.90, "12%"]
          - [reliability_≥0.90, 0.90, "7%"]
          - [construct_coverage_≥0.90, 0.90, "14%"]
          - [all_criteria_met, "-", "7%"]
    figures_description:
      - "Fig 16: Validity metrics as function of replacement rate — all three metrics
        degrade faster than linear, with reliability being the binding constraint (7%)"
    analysis: >
      Graceful degradation analysis表明在当前calibration quality下，只能安全替换7%的items
      （约875个items，满足所有validity criteria）。这远不足以构成practical "self-healing"
      benchmark——如果检测到的contaminated items超过7%，replacement会损害benchmark validity。
      这是对Claim 3的严重限制，但degradation curve本身是有价值的empirical contribution，
      可以frame为"item replacement的practical bounds"。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      实现Item-Focused Trees，将model release date作为continuous covariate替代categorical cohort DIF。
    expected_results:
      ift_tpr_delta_ge_1.4: 0.33
      ift_tpr_delta_ge_1.0: 0.16
      ift_fpr: 0.10
      ift_vs_categorical_dif_tpr_delta: -0.05
      ift_computation_time_hours: 18
      n_splits_found: 3.2
      split_dates_concentration: "2023-06 to 2024-01"
      overfitting_cross_val_tpr_drop: 0.12
    result_rationale: >
      Item-Focused Trees理论上避免arbitrary cohort splits，但在worst tier下：(1) Release date
      作为continuous covariate与contamination的关系不是smooth monotonic的——contamination是
      event-driven（某次data leak），不是gradual trend，IFT的tree structure可以capture这个
      但容易overfit到特定split points；(2) Cross-validation显示TPR drop=0.12，说明overfitting
      significant；(3) 在model heterogeneity高的情况下，IFT实际上比categorical DIF表现略差
      （TPR差-0.05），因为tree splitting在high-noise环境下容易找到spurious splits——3.2个
      average splits集中在2023年中到2024年初，这恰好是architecture transition period
      （GPT-4发布后大量models涌现），tree可能在capture architecture shift而非contamination。
      FPR=0.10比categorical DIF（0.12）略低，但improvement不显著。Computation cost 18 hours
      因为per-item tree fitting在12508 items上。
    tables:
      - title: "Table 17: Item-Focused Trees vs Categorical DIF"
        columns: [metric, categorical_dif, ift, delta]
        rows:
          - [TPR_δ≥1.4, 0.38, 0.33, -0.05]
          - [TPR_δ≥1.0, 0.18, 0.16, -0.02]
          - [FPR, 0.12, 0.10, -0.02]
          - [F1, 0.25, 0.24, -0.01]
          - [computation_hours, 0.5, 18, "+17.5"]
    figures_description:
      - "Fig 17: IFT split point distribution — concentration around architecture
        transition periods rather than known contamination events"
    analysis: >
      IFT未能改善DIF detection。Split points与architecture transitions而非contamination events
      对齐，进一步证实model heterogeneity是dominant signal source。计算成本高36倍但无performance
      gain。作为P2 experiment，结论是negative：continuous covariate treatment不解决fundamental
      问题。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce953908-91ce-47c6-be4f-eaff661cb7bb",
  "isSidechain": false,
  "requestId": "req_011CbEQarXS2z2TSrdtfjhyr",
  "type": "assistant",
  "uuid": "fe1843ce-9801-4f59-b66d-f80ca78b41bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DtmMuicC1zeFsfWBoRQb3Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10703,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12443,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10703
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DIF在真实数据上信号微弱或FPR过高无法实用；RL-robustness优势不显著；核心'psychometric detection'假设在LLM场景下不成立——需重新寻找angle 核心假设：['真实LLM response data严重违反IRT假设——模型间ability维度不一致（archite…",
  "leafUuid": "fe1843ce-9801-4f59-b66d-f80ca78b41bf",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination detection via DIF and psychometric equating",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DIF在真实数据上信号微弱或FPR过高无法实用；RL-robustness优势不显著；核心'psychometric detection'假设在LLM场景下不成立——需重新寻找angle 核心假设：['真实LLM response data严重违反IRT假设——模型间ability维度不一致（archite…",
  "leafUuid": "fe1843ce-9801-4f59-b66d-f80ca78b41bf",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination detection via DIF and psychometric equating",
  "sessionId": "7d0d8a68-fd2a-484b-8e5b-a8af6081aedb"
}
```

---
