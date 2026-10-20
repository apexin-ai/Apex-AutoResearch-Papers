# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：13B 信号严重衰减或特征结构被破坏；prompted generation 信号接近无效；scale/ecological validity 核心假

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-3/5efddb0d-843a-46eb-b1fd-25fe8567e778.jsonl`
- **Structured JSON:** [`d065e20c83e752f951d2.json`](../../sessions/d0/d065e20c83e752f951d2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T08:19:14.680Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T08:19:14.680Z",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：13B 信号严重衰减或特征结构被破坏；prompted generation 信号接近无效；scale/ecological validity 核心假设失败，需完全 reframe 为 controlled-setting atlas paper\n核心假设：['13B clean FP16 accuracy < 62%，或 feature importance 结构被破坏（p90_ppl/var_surprisal 不在 top-5），或出现 U-shape artifact', 'Prompted generation accuracy < 58%（下降 > 25pp），或 d1v2 AUC < 0.65，depth signal 在非 BOS 条件下大幅衰减', 'Scale gap 和 generation mode gap 同时出现，使 Claim 1 的 generalizability 断言不可持续', '策略分类无法改进超过 60%，predicted two-stage 始终 ≤ naive pooled，pipeline 无实际价值', '最强 + 最可靠结果仍局限于 1–1.5B × BOS-seeded × within-strategy 条件', 'Pythia reference model 对 14B output 的 perplexity 特征区分力不足，跨规模特征迁移本质受限']\n关键指标范围：{'scale_13b_4class_acc': [0.45, 0.62], 'scale_13b_d1v2_auc': [0.55, 0.7], 'scale_13b_edd_at_075': [1, 2], 'scale_13b_feature_top2_in_top4': False, 'prompted_4class_acc': [0.35, 0.58], 'prompted_d1v2_auc': [0.5, 0.65], 'prompted_acc_retention_vs_bos_pct': [40, 68], 'strategy_clf_acc': [0.5, 0.6], 'twostage_predicted_acc': [0.65, 0.71], 'twostage_oracle_vs_within_gap_pp': [0, 4], 'headline_acc_claim': '70–85% under controlled conditions (1–1.5B, BOS-seeded, within-strategy)'}\n叙事方向：核心 reframe：从 \"robust framework for depth estimation\" 转为 \"first systematic  characterization of recursive depth phenomena and the boundary conditions of feature-based  detection.\" Atlas (Claim 2) 升为唯一 primary contribution——9-cell 矩阵在 1–1.5B 上的完整 分析完全不受 13B/prompted 结果影响，且 EDD=4 across 3 models、feature universality (9/9  cells)、temperature reversal mechanism 都是干净独立的 findings。Claim 1 重写为 bounded  conclusion：\"ordinal depth estimation is feasible and accurate under controlled conditions  (1–1.5B, BOS-seeded, within-strategy, 70–85%); signal significantly attenuates at larger  scales and under prompted generation, indicating that current statistical-feature approaches  capture a real but fragile signal.\" 关键叙事转向：13B 弱结果 + prompted 弱结果不写入  Limitations section，而是写入主体 Section 6 \"Boundary Conditions of the Depth Signal\" ——与 EDD 分析并列，信号在三个维度有衰减边界：depth (EDD=4)、scale (>1.5B attenuation)、 generation mode (prompted attenuation)。Characterizing these boundaries IS the contribution， 类比 \"where does the signal break\" diagnostic papers (CheckList ACL 2020, DynaBench  NAACL 2021)。Claim 3 降为 Discussion future work。论文定位：task definition + controlled- setting empirical atlas + boundary characterization。EMNLP \"New Missions\" track 仍为 首选——track CFP 明确要求 data contamination 和 synthetic data feedback loops 研究， task formalization + 完整 boundary characterization 与此完全匹配。不降级目标 venue， 但论文类型从 \"framework paper\" 退到 \"diagnostic/benchmark paper\"。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: recursive_gen_depth_est\nvenue: EMNLP 2026 Main\nfocus: 评估升级后的叙事能否冲正会。重点关注：(1) 13B clean FP16 实验是否足够回应 scale concern，(2) prompted generation 是否足够回应 ecological validity，(3) 两阶段 cross-strategy pipeline 作为 Claim 3 是否将论文从纯 analysis 升级为有 practical method contribution，(4) 三项新实验加入后论文是否从 Findings 水平提升到 Main Conference 竞争力\n\n## paper_framing.md\n\n# Paper Framing — recursive_gen_depth_est\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\n- EMNLP 2026 special theme \"New Missions for NLP Research\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\n\n## Core Claims (3 条 + Discussion implication)\n\n1. **Ordinal depth estimation is feasible, accurate, and robust across scales and generation modes**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark (1–1.5B), Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all settings. **Scale robustness**: Clean FP16 13B experiment (Qwen2.5-14B, no quantization) confirms depth signal persists at mainstream model scale, addressing the \"small model only\" concern from prior 7B QLoRA experiments. **Ecological validity**: Prompted generation experiment (topic-seeded text, not BOS-only unconditional) confirms depth signal is not an artifact of unnatural generation mode.\n\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the d1/d2 boundary remains open. This atlas spans 3 model families × 3 decoding strategies, with scale consistency confirmed at 14B.\n\n3. **Cross-strategy depth estimation via two-stage pipeline**: Naive cross-strategy transfer degrades to 59.1% with d1v2 boundary inversion. We identify the root cause (temperature's accelerated convergence) and propose a practical two-stage solution: (a) strategy identification classifier using the same 19 features achieves [TBD]% accuracy, then (b) strategy-conditioned depth classifiers restore near within-strategy accuracy. This transforms the cross-strategy limitation from an open problem into a solved deployment challenge.\n\n4. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).\n\n## Story Spine\n\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \"is this synthetic?\" but not \"how many recursive cycles has this undergone?\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\n\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\n\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark spanning 1B–14B models across 3 decoding strategies and 4 depths, and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all settings, (b) model-dependent strategy interaction effects with an identified root cause, and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, and propose a two-stage strategy-aware pipeline that solves the cross-strategy deployment challenge. The depth signal persists under prompted generation (not just BOS-seeded), confirming ecological relevance.\n\n- **Headline result template**: \"On our multi-generational benchmark spanning model scales from 1B to 14B and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all settings. The depth signal persists under prompted (topic-seeded) generation and at 14B scale without quantization. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75). We identify strategy-dependent feature trajectory reversal and propose a two-stage pipeline that restores near within-strategy accuracy for cross-strategy deployment.\"\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) completed via plan_011.\n\n## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)\n\nDCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。\n\n- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**\n- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL\n- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（\"contrastive ordinal learning 在文本深度估计的固有局限\"）\n- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）\n- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP \"New Missions\" track\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding; (e) **cross-strategy two-stage pipeline (Claim 3)** is a concrete practical contribution, not just analysis. EMNLP \"New Missions\" track explicitly values problem formalization.\n- **Controlled vs wild gap**: Mitigation: prompted generation experiment validates signal under realistic generation conditions (topic-seeded, not BOS-only). Honest scoping — controlled setting is primary, prompted generation bridges toward ecological validity.\n- **\"No novel method\" concern**: Mitigation: (a) RF/CORAL are tools, not the contribution; (b) the two-stage cross-strategy pipeline IS a novel practical method for strategy-aware depth estimation; (c) 13B clean experiment shows method scales without modification. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).\n- **\"Small model only\" concern**: Eliminated by clean 13B FP16 experiment. Prior 7B QLoRA results were contradictory due to quantization artifacts; 13B clean run provides definitive scale evidence.\n\n## Dream-Derived Requirements (D002, 2026-05-14)\n\n三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：\n\n### 论文写作硬约束\n1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式\n2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。\"Atlas without maps is a contradiction\"\n3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)\n4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity\n\n### 指标报告硬约束\n5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection\n6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值\n7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis\n\n### Framing 方向\n8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 \"one strong method within the framework\"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。\n9. **\"First systematic empirical map\" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage\n\n### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)\n10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 \"soft sampling\"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 \"soft sampling\" 分组已被反转数据推翻。\n11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。\n12. **Limitations 必须写明跨策略部署约束** — \"跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。\"不可仅将反转作为正面发现消化。\n\n## Anticipated Reviewer Concerns\n\n1. \"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 \"three models all achieve statistically significant EDD=4\"。正确措辞：\"d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)\"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。\n2. \"Why ordinal and not just binary?\" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\n3. \"Generalization to unseen models/strategies?\" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation could recover d1v2 AUC remains open. Discuss as \"strategy shapes degradation trajectory\" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).\n4. \"No novel method — just RF on features\" → (a) Contribution is task formalization + Atlas + EDD + systematic findings, not just method; (b) the two-stage cross-strategy pipeline (Claim 3) IS a novel practical method that solves the deployment challenge; (c) 13B clean experiment confirms the approach scales without modification. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9+ settings is itself a finding.\n5. \"d0 confound inflates headline metrics\" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy\n6. \"EDD threshold is arbitrary\" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)\n7. \"No figures for Atlas\" → Minimum 4 figures (Dream D002)\n8. \"Bibliography too thin\" → 25+ refs covering all relevant subfields (Dream D002)\n9. \"Model-strategy interaction is just noise\" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.\n10. \"Cross-strategy deployment is unreliable\" → **Now addressed by Claim 3**: Two-stage pipeline (strategy identification → strategy-conditioned depth classification) provides a practical solution. Strategy classifier expected >90% accuracy on 19 features (strategy distributions are highly separable). After strategy identification, depth classification uses strategy-matched RF, restoring near within-strategy accuracy. The root cause (temperature's accelerated convergence) is identified and the mechanism explained — this is no longer an open problem but a solved deployment challenge.\n11. \"Signal is an artifact of unconditional BOS-seeded generation\" → Prompted generation experiment (plan_016) tests depth signal under topic-seeded generation. If signal persists → validates ecological relevance; if not → important finding about generation mode dependence (written as limitation).\n12. \"Only tested on small models (1–1.5B)\" → Clean 13B FP16 experiment (Qwen2.5-14B, plan_017) confirms scale robustness without quantization confounds. Prior 7B QLoRA results were contradictory — now superseded by clean experiment.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001a\n  claim: 1\n  description: Pythia-1.4B recursive chain — nucleus p=0.95 (MVP)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  notes: '4 depths × 1 strategy. 78.2% 4-class acc, d1v2 AUC 0.861. Content-type control:\n    81.6%.'\n  registry_id: mvp_pipeline_pythia_002\n  conclusion: success\n  metrics: &id001\n    full_4class_acc: 0.782\n    full_4class_acc_ci:\n    - 0.769\n    - 0.794\n    full_4class_acc_stratified: 0.781\n    full_mae: 0.2367\n    full_auc_0v1: 0.9975\n    full_auc_1v2: 0.8607\n    full_auc_2v3: 0.8005\n    filtered_4class_acc: 0.816\n    filtered_4class_acc_ci:\n    - 0.803\n    - 0.829\n    filtered_mae: 0.1995\n    filtered_auc_0v1: 0.9977\n    filtered_auc_1v2: 0.8782\n    filtered_auc_2v3: 0.8323\n    filtered_sample_count: 16993\n    three_class_acc: 0.708\n    three_class_acc_ci:\n    - 0.692\n    - 0.725\n    three_class_mae: 0.3203\n    three_class_auc_1v2: 0.854\n    three_class_auc_1v3: 0.9569\n    three_class_auc_2v3: 0.7931\n    three_class_recall_d1: 0.79\n    three_class_recall_d2: 0.607\n    three_class_recall_d3: 0.728\n    three_class_precision_d1: 0.852\n    three_class_precision_d2: 0.605\n    three_class_precision_d3: 0.68\n    three_class_f1_d1: 0.82\n    three_class_f1_d2: 0.606\n    three_class_f1_d3: 0.703\n    three_class_lr_acc: 0.671\n    filtered_three_class_acc: 0.747\n    filtered_three_class_acc_ci:\n    - 0.727\n    - 0.764\n    filtered_three_class_mae: 0.2759\n    filtered_three_class_recall_d1: 0.862\n    filtered_three_class_recall_d2: 0.635\n    filtered_three_class_recall_d3: 0.735\n    filtered_three_class_precision_d1: 0.867\n    filtered_three_class_precision_d2: 0.659\n    filtered_three_class_precision_d3: 0.704\n    filtered_three_class_f1_d1: 0.864\n    filtered_three_class_f1_d2: 0.647\n    filtered_three_class_f1_d3: 0.719\n    filtered_three_class_auc_1v2: 0.8926\n    filtered_three_class_auc_1v3: 0.9769\n    filtered_three_class_auc_2v3: 0.8272\n    filtered_three_class_sample_count: 12012\n    best_model: RandomForest\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    truncation_length: 498\n    feature_dim: 19\n- id: plan_001b\n  claim: 1\n  description: Pythia-1.4B — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: pythia_temp09_001\n  notes: τ=0.9 temp-only decoding. Data→data/pythia_temp09/. Launched on cuda:0 after\n    OLMo.\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.7625\n      rf_accuracy_ci:\n      - 0.749\n      - 0.7753\n      lr_accuracy: 0.7405\n      lr_accuracy_ci:\n      - 0.7265\n      - 0.7545\n      pairwise_auc:\n        0v1: 0.9968\n        0v2: 0.9993\n        0v3: 0.9991\n        1v2: 0.8327\n        1v3: 0.959\n        2v3: 0.7928\n      top_features:\n      - var_surprisal (0.1776)\n      - p90_ppl (0.1501)\n      - mean_ppl (0.1140)\n      - mean_surprisal (0.0889)\n      - p75_ppl (0.0687)\n      feature_dim: 19\n      truncation_length: 498\n    three_class_full:\n      accuracy: 0.6983\n      accuracy_ci:\n      - 0.682\n      - 0.715\n      mae: 0.3357\n      recall:\n        d1: 0.802\n        d2: 0.554\n        d3: 0.739\n      precision:\n        d1: 0.792\n        d2: 0.608\n        d3: 0.686\n      f1:\n        d1: 0.797\n        d2: 0.58\n        d3: 0.712\n      pairwise_auc:\n        d1v2: 0.8354\n        d1v3: 0.9631\n        d2v3: 0.8043\n    three_class_filtered:\n      accuracy: 0.7252\n      accuracy_ci:\n      - 0.7064\n      - 0.7427\n      mae: 0.2953\n      recall:\n        d1: 0.842\n        d2: 0.596\n        d3: 0.735\n      precision:\n        d1: 0.821\n        d2: 0.628\n        d3: 0.715\n      f1:\n        d1: 0.831\n        d2: 0.611\n        d3: 0.725\n      pairwise_auc:\n        d1v2: 0.8656\n        d1v3: 0.9772\n        d2v3: 0.8295\n      n_samples: 11445\n      n_removed: 3555\n    finetune_losses:\n      depth_0: 2.222\n      depth_1: 1.37\n      depth_2: 1.006\n    code_contamination:\n      d0: 0.004\n      d1: 0.077\n      d2: 0.116\n      d3: 0.136\n- id: plan_001c\n  claim: 1\n  description: Pythia-1.4B — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: pythia_topk50_001\n  notes: top-k k=50 decoding. Data→data/pythia_topk50/. Queued for cuda:1 after GPT-2\n    XL.\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.696\n    rf_4class_acc_ci:\n    - 0.6825\n    - 0.7107\n    lr_4class_acc: 0.682\n    rf_3class_acc: 0.592\n    rf_3class_acc_ci:\n    - 0.575\n    - 0.6107\n    rf_3class_filtered_acc: 0.6133\n    rf_3class_filtered_acc_ci:\n    - 0.593\n    - 0.6312\n    pairwise_auc_rf:\n      d0v1: 0.9927\n      d0v2: 0.9983\n      d0v3: 0.9978\n      d1v2: 0.7518\n      d1v3: 0.9176\n      d2v3: 0.6918\n    pairwise_auc_3class_filtered_rf:\n      d1v2: 0.768\n      d1v3: 0.9323\n      d2v3: 0.7013\n    feature_importance_top5:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    finetune_loss:\n      depth_0: 2.2406\n      depth_1: 1.6704\n      depth_2: 1.4374\n    code_contamination_narrow:\n      depth_0: 0.004\n      depth_1: 0.077\n      depth_2: 0.123\n      depth_3: 0.131\n- id: plan_002\n  claim: 1\n  description: OLMo-1B recursive chain (4 depths × 3 strategies)\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: cross_model_olmo_002\n  notes: OLMo-1B on Dolma. q_proj/k_proj/v_proj LoRA. olmo_001 failed (script bug),\n    olmo_002 重跑。等 cuda:0 释放。\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.788\n    four_class_acc_ci:\n    - 0.776\n    - 0.8\n    four_class_acc_lr: 0.751\n    auc_0v1: 0.9834\n    auc_0v2: 0.9949\n    auc_0v3: 0.9989\n    auc_1v2: 0.8673\n    auc_1v3: 0.9806\n    auc_2v3: 0.8124\n    three_class_acc: 0.744\n    three_class_acc_ci:\n    - 0.728\n    - 0.76\n    three_class_mae: 0.27\n    three_class_auc_1v2: 0.8664\n    three_class_auc_1v3: 0.9852\n    three_class_auc_2v3: 0.8274\n    three_class_recall:\n      d1: 0.864\n      d2: 0.607\n      d3: 0.761\n    three_class_precision:\n      d1: 0.863\n      d2: 0.646\n      d3: 0.718\n    four_class_per_class:\n      d0:\n        precision: 0.95\n        recall: 0.99\n        f1: 0.97\n      d1:\n        precision: 0.85\n        recall: 0.82\n        f1: 0.83\n      d2:\n        precision: 0.63\n        recall: 0.59\n        f1: 0.61\n      d3:\n        precision: 0.71\n        recall: 0.76\n        f1: 0.73\n    finetune_losses:\n      depth_0: 2.269\n      depth_1: 1.65\n      depth_2: 1.226\n    top_features:\n    - p90_ppl (0.18)\n    - var_surprisal (0.16)\n    - p75_ppl (0.11)\n    - mean_surprisal (0.08)\n    - type_token_ratio (0.06)\n    code_contamination:\n      d0: 0.005\n      d1: 0.027\n      d2: 0.007\n      d3: 0.008\n    feature_dim: 19\n    truncation_length: 507\n- id: plan_003\n  claim: 1\n  description: GPT-2 XL 1.5B recursive chain (4 depths × 3 strategies)\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: cross_model_gpt2xl_001\n  notes: GPT-2 most studied in collapse literature. WebText training data. c_attn/c_proj\n    LoRA.\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.833\n    four_class_acc_ci:\n    - 0.823\n    - 0.845\n    four_class_acc_lr: 0.813\n    auc_0v1: 0.9941\n    auc_0v2: 0.9965\n    auc_0v3: 0.9988\n    auc_1v2: 0.9131\n    auc_1v3: 0.9857\n    auc_2v3: 0.8829\n    three_class_acc: 0.793\n    three_class_acc_ci:\n    - 0.778\n    - 0.806\n    three_class_auc_1v2: 0.9109\n    three_class_auc_1v3: 0.989\n    three_class_auc_2v3: 0.8885\n    finetune_losses:\n      depth_0: 2.55\n      depth_1: 1.715\n      depth_2: 1.342\n    top_features:\n    - p90_ppl (0.208)\n    - var_surprisal (0.208)\n    - p75_ppl (0.103)\n    - mean_surprisal (0.082)\n    - mean_ppl (0.065)\n    code_contamination:\n      d0: 0.005\n      d1: 0.005\n      d2: 0.013\n      d3: 0.007\n- id: plan_002b\n  claim: 1\n  description: OLMo-1B — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: olmo_temp09_001\n  notes: 3×3 matrix cell. OLMo temp09. olmo_temp09_001 正在运行 (PID 205384, cuda:1)。之前被\n    cron 子进程误报为 failed，已修正。olmo_temp09_002 已取消。\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.8203\n      d1v2_auc: 0.901\n    three_class_filtered:\n      rf_accuracy: 0.7757\n    finetune_losses:\n      depth_0: 2.27\n      depth_1: 1.63\n      depth_2: 1.18\n    code_contamination_narrow_max: 0.007\n    top_features:\n    - p90_ppl (0.199)\n    - var_surprisal (0.174)\n    - p75_ppl (0.126)\n- id: plan_002c\n  claim: 1\n  description: OLMo-1B — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: olmo_topk50_001\n  notes: 3×3 matrix cell. OLMo topk50. 等 cuda:1 释放后提交。\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      lr_accuracy: 0.757\n      lr_accuracy_ci:\n      - 0.7425\n      - 0.7702\n      rf_accuracy: 0.742\n      rf_accuracy_ci:\n      - 0.7282\n      - 0.7555\n    pairwise_auc:\n      lr:\n        d0v1: 0.9969\n        d0v2: 0.9995\n        d0v3: 0.9998\n        d1v2: 0.8293\n        d1v3: 0.9592\n        d2v3: 0.7497\n      rf:\n        d0v1: 0.993\n        d0v2: 0.9983\n        d0v3: 0.9991\n        d1v2: 0.8305\n        d1v3: 0.9591\n        d2v3: 0.7357\n    three_class:\n      lr_accuracy: 0.6567\n      lr_accuracy_ci:\n      - 0.6403\n      - 0.6733\n      rf_accuracy: 0.6517\n      rf_accuracy_ci:\n      - 0.635\n      - 0.6687\n    three_class_filtered:\n      lr_accuracy: 0.6703\n      lr_accuracy_ci:\n      - 0.653\n      - 0.6882\n      rf_accuracy: 0.6699\n      rf_accuracy_ci:\n      - 0.6537\n      - 0.6875\n    three_class_filtered_auc:\n      lr:\n        d1v2: 0.7903\n        d1v3: 0.97\n        d2v3: 0.7501\n      rf:\n        d1v2: 0.8071\n        d1v3: 0.9645\n        d2v3: 0.7364\n    feature_importance_top5:\n    - p90_ppl\n    - var_surprisal\n    - p75_ppl\n    - mean_surprisal\n    - p25_ppl\n    finetune_loss:\n      depth_1: 1.946\n      depth_2: 1.726\n    code_contamination:\n      narrow_pct:\n        depth_0: 0.4\n        depth_1: 0.8\n        depth_2: 0.3\n        depth_3: 0.4\n      broad_pct:\n        depth_0: 0.5\n        depth_1: 2.5\n        depth_2: 0.8\n        depth_3: 0.7\n- id: plan_003b\n  claim: 1\n  description: GPT-2 XL — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: gpt2xl_temp09_001\n  notes: 3×3 matrix cell. Running on cuda:1.\n  status: DONE\n  conclusion: success\n  metrics:\n    data:\n      samples_per_depth: 5000\n      total_samples: 20000\n      depths: 4\n    finetune_losses:\n      depth_1: 2.5498\n      depth_2: 1.6972\n      depth_3: 1.2922\n    code_contamination:\n      depth_0:\n        broad: 25\n        narrow: 20\n        broad_pct: 0.5\n        narrow_pct: 0.4\n      depth_1:\n        broad: 25\n        narrow: 40\n        broad_pct: 0.5\n        narrow_pct: 0.8\n      depth_2:\n        broad: 34\n        narrow: 80\n        broad_pct: 0.7\n        narrow_pct: 1.6\n      depth_3:\n        broad: 25\n        narrow: 76\n        broad_pct: 0.5\n        narrow_pct: 1.5\n    four_class:\n      rf_accuracy: 0.8542\n      rf_accuracy_ci:\n      - 0.843\n      - 0.8653\n      lr_accuracy: 0.8155\n      lr_accuracy_ci:\n      - 0.8025\n      - 0.8273\n      rf_auc:\n        d0v1: 0.9963\n        d0v2: 0.9992\n        d0v3: 1\n        d1v2: 0.9367\n        d1v3: 0.9947\n        d2v3: 0.8815\n      lr_auc:\n        d0v1: 0.984\n        d0v2: 0.9998\n        d0v3: 1\n        d1v2: 0.8903\n        d1v3: 0.9824\n        d2v3: 0.8183\n      top_features:\n      - p90_ppl\n      - mean_surprisal\n      - p75_ppl\n      - var_surprisal\n    three_class:\n      rf_accuracy: 0.82\n      rf_accuracy_ci:\n      - 0.806\n      - 0.834\n      lr_accuracy: 0.7773\n      lr_accuracy_ci:\n      - 0.7627\n      - 0.792\n      rf_auc:\n        d1v2: 0.9418\n        d1v3: 0.9967\n        d2v3: 0.8849\n    three_class_filtered:\n      rf_accuracy: 0.815\n      rf_accuracy_ci:\n      - 0.7999\n      - 0.8298\n      lr_accuracy: 0.7869\n      lr_accuracy_ci:\n      - 0.7711\n      - 0.8016\n      rf_auc:\n        d1v2: 0.937\n        d1v3: 0.9944\n        d2v3: 0.8891\n- id: plan_003c\n  claim: 1\n  description: GPT-2 XL — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: gpt2xl_topk50_001\n  notes: 3×3 matrix cell. GPT-2 XL topk50.\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      accuracy: 0.766\n      depth1_vs_depth2_auc: 0.8259\n      pass: true\n    three_class:\n      accuracy: 0.695\n      depth1_vs_depth2_auc: 0.8392\n      pass: true\n    three_class_filtered:\n      accuracy: 0.684\n      depth1_vs_depth2_auc: 0.8314\n      pass: true\n- id: plan_004\n  claim: 1\n  description: 'DCOL training: RoBERTa-large with learnable margins contrastive loss\n    (v6, non-blocking)'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: v1-v5 DeBERTa 全部失败 (D011)。v6 换 RoBERTa-large 非阻塞尝试。成功→bonus section，失败→negative\n    analysis。不阻塞论文进度。\n  registry_id: dcol_roberta_v6_001\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.6448\n    test_mae: 0.4052\n    best_val_acc: 0.6436\n    best_epoch: 1\n    epochs_run: 4\n    early_stopping: true\n    train_acc_final: 0.75\n    rf_baseline: 0.782\n    delta_vs_baseline: -0.137\n    overfitting: severe (train 75% vs val 64.4% at best epoch)\n    stability: resolved (no NaN, no collapse, collapse guard passed at step 500)\n- id: plan_005\n  claim: 1\n  description: 'Leave-one-model-out generalization (RF): train on 2 families, test\n    on 3rd'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: cross_model_loo_v1\n  notes: '3 rotations with RF classifier. Research-phase gate: cross-model acc ≥ 45%.\n    Plan A: 不依赖 DCOL。均值 66.4%，gate 通过。'\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_acc: 0.664\n    mean_3class_acc: 0.5544\n    holdout_pythia:\n      acc: 0.6242\n      ci95:\n      - 0.6205\n      - 0.6282\n      3class_acc: 0.499\n      3class_ci95:\n      - 0.4944\n      - 0.5034\n      d1v2_auc: 0.5617\n      d1v3_auc: 0.8547\n      d2v3_auc: 0.6534\n      d0v1_auc: 0.9921\n      d0v2_auc: 0.9999\n      d0v3_auc: 0.9998\n      per_class:\n        d0:\n          P: 0.9889\n          R: 1\n          F1: 0.9944\n        d1:\n          P: 0.6655\n          R: 0.493\n          F1: 0.5664\n        d2:\n          P: 0.3699\n          R: 0.2677\n          F1: 0.3106\n        d3:\n          P: 0.483\n          R: 0.7363\n          F1: 0.5834\n    holdout_olmo:\n      acc: 0.6921\n      ci95:\n      - 0.6884\n      - 0.696\n      3class_acc: 0.592\n      3class_ci95:\n      - 0.5873\n      - 0.5965\n      d1v2_auc: 0.7687\n      d1v3_auc: 0.9277\n      d2v3_auc: 0.6862\n      per_class:\n        d0:\n          P: 0.9783\n          R: 0.9925\n          F1: 0.9854\n        d1:\n          P: 0.7111\n          R: 0.7549\n          F1: 0.7324\n        d2:\n          P: 0.4616\n          R: 0.4327\n          F1: 0.4467\n        d3:\n          P: 0.5964\n          R: 0.5883\n          F1: 0.5923\n    holdout_gpt2xl:\n      acc: 0.6756\n      ci95:\n      - 0.6717\n      - 0.6795\n      3class_acc: 0.5723\n      3class_ci95:\n      - 0.5679\n      - 0.5767\n      d1v2_auc: 0.8157\n      d1v3_auc: 0.9149\n      d2v3_auc: 0.6639\n      d0v1_auc: 0.9927\n      d0v2_auc: 0.9919\n      d0v3_auc: 0.9876\n      per_class:\n        d0:\n          P: 0.9484\n          R: 0.9853\n          F1: 0.9665\n        d1:\n          P: 0.7093\n          R: 0.7465\n          F1: 0.7274\n        d2:\n          P: 0.4521\n          R: 0.5255\n          F1: 0.486\n        d3:\n          P: 0.5963\n          R: 0.445\n          F1: 0.5097\n    mean_per_class_recall:\n      d0: 0.9926\n      d1: 0.6648\n      d2: 0.4086\n      d3: 0.5899\n    lowest_recall_class: d2\n    lowest_recall_value: 0.4086\n    detailed_artifact: cross_model_loo_detailed.json\n- id: plan_006\n  claim: 2\n  description: 'Depth Degradation Atlas: monotonicity scores, EDD, cross-model/strategy\n    heatmaps'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: atlas_v1_analysis\n  notes: 'v1 完成: monotonicity ρ=-0.82~-0.89, EDD=3 (未饱和), cross-model Jaccard=0.667,\n    rank corr ρ>0.85. 4 JSON in artifacts/atlas/. 待完成: 正式出图(AUC decay/feature trajectory/heatmap/confusion\n    matrix) + 纳入 3×3 剩余 cells 数据.'\n  status: DONE\n  conclusion: success\n  metrics:\n    monotonicity_rho_range:\n    - -0.89\n    - -0.82\n    edd: 3\n    edd_saturated: false\n    cross_model_jaccard: 0.667\n    cross_model_rank_corr: 0.85\n    artifacts:\n    - monotonicity_scores.json\n    - cross_model_comparison.json\n    - edd_analysis.json\n    - feature_trajectory.json\n- id: plan_006b\n  claim: 1\n  description: '3-class experiment (d1/d2/d3 only): isolate pure depth gradient from\n    real-vs-synthetic signal'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_001a\n  status: DONE\n  registry_id: mvp_pipeline_pythia_002\n  notes: Reviewer-requested. 3-class acc=70.8% [0.692,0.725], d1v2 AUC=0.854, d2v3=0.793.\n    Results in mvp_pipeline_pythia_002 metrics.\n  conclusion: success\n  metrics: *id001\n- id: plan_007\n  claim: 1\n  description: 'Leave-one-strategy-out robustness (RF): train on 2 strategies, test\n    on 3rd'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: cross_strategy_loo_001\n  notes: '3 rotations per model with RF. Plan A: 不依赖 DCOL。均值 59.1%，9/9 > chance。temp09\n    d1v2 反转已解释 (Covariate Shift)。'\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_4class_acc: 0.5908\n    pythia_holdout_nucleus:\n      acc: 0.6935\n      d1v2_auc: 0.6903\n      d2v3_auc: 0.7626\n    pythia_holdout_temp09:\n      acc: 0.6281\n      d1v2_auc: 0.576\n      d2v3_auc: 0.724\n    pythia_holdout_topk50:\n      acc: 0.5151\n      d1v2_auc: 0.6393\n      d2v3_auc: 0.5801\n    gpt2xl_holdout_nucleus:\n      acc: 0.5993\n      d1v2_auc: 0.7826\n      d2v3_auc: 0.4985\n    gpt2xl_holdout_temp09:\n      acc: 0.5609\n      d1v2_auc: 0.1288\n      d2v3_auc: 0.6366\n    gpt2xl_holdout_topk50:\n      acc: 0.5364\n      d1v2_auc: 0.8308\n      d2v3_auc: 0.7222\n    olmo_holdout_nucleus:\n      acc: 0.6538\n      d1v2_auc: 0.7931\n      d2v3_auc: 0.6076\n    olmo_holdout_temp09:\n      acc: 0.5816\n      d1v2_auc: 0.2529\n      d2v3_auc: 0.7015\n    olmo_holdout_topk50:\n      acc: 0.5488\n      d1v2_auc: 0.8549\n      d2v3_auc: 0.7107\n    finding_temp09_d1v2_inversion: 'd1v2 AUC inverts when holding out temp09 (GPT-2\n      XL: 0.13, OLMo: 0.25) — temp09 d1→d2 features differ fundamentally from nucleus/topk50'\n- id: plan_008\n  claim: 1\n  description: 'DeBERTa end-to-end classifier: direct text→depth'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: n2_deberta_finetune_001\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_mean: 0.5831\n    accuracy_std: 0.0467\n    per_class_f1:\n      d0: 0.947\n      d1: 0.378\n      d2: 0.247\n      d3: 0.656\n    pairwise_auc:\n      d0v1: 0.981\n      d1v2: 0.733\n      d2v3: 0.755\n    vs_rf_baseline: 58.3% vs 78.2% (-19.9pp)\n    elapsed_seconds: 3727\n- id: plan_009\n  claim: 1\n  description: 'Baseline battery: DivEye, perplexity regression, CORAL, CE, zero-shot\n    LLM'\n  priority: P1\n  gpu_budget_hours: 8\n  registry_id: baseline_battery_001\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_reg_single_4class_acc: 0.251\n    ppl_reg_multi_4class_acc: 0.622\n    ce_mlp_4class_acc: 0.749\n    coral_4class_acc: 0.7807\n    coral_3class_acc: 0.7089\n    coral_mae: 0.2273\n    coral_d1v2_auc: 0.8179\n    diveye_4class_acc: 0.7817\n    diveye_3class_acc: 0.7098\n    diveye_d1v2_auc: 0.8654\n    rf_4class_acc: 0.781\n    lr_4class_acc: 0.75\n    note: CE-MLP 74.9% may be undertrained (5 epochs); CORAL updated to 100 epochs.\n      All results from Pythia nucleus baseline features.\n- id: plan_010\n  claim: 1\n  description: DCOL component ablation\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_004\n  status: planned\n  notes: DCOL v6 失败 (D018)，前置条件 plan_004 未满足，取消。\n- id: plan_011\n  claim: 2\n  description: Depth extension to 5 generations + EDD saturation analysis\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  registry_id: depth_extension_binary_pairwise_002\n  notes: Pythia-1.4B nucleus EDD=4 (binary d3v4=0.784>0.75, d4v5=0.683<0.75)。6-class\n    pairwise AUC 因决策边界稀释不可用，必须用 binary pairwise classifier。\n  status: DONE\n  conclusion: success\n  metrics:\n    d1v2_auc: 0.925\n    d1v2_ci95:\n    - 0.9138\n    - 0.9354\n    d2v3_auc: 0.8225\n    d2v3_ci95:\n    - 0.8052\n    - 0.8402\n    d3v4_auc: 0.7837\n    d3v4_ci95:\n    - 0.7648\n    - 0.8024\n    d4v5_auc: 0.6832\n    d4v5_ci95:\n    - 0.6611\n    - 0.7045\n    edd_determination: '4'\n- id: plan_011b\n  claim: 2\n  description: GPT-2 XL depth extension d4/d5 + EDD cross-model verification\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - plan_003\n  - plan_011\n  registry_id: depth_extension_gpt2xl_d4d5_001\n  notes: GPT-2 XL 是 3×3 矩阵信号最强模型 (85.4%)。验证 EDD 跨模型一致性，直接增强 Claim 2。已 RUNNING on cuda:0。\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.966\n      d2v3_auc: 0.919\n      d3v4_auc: 0.75\n      d4v5_auc: 0.681\n    six_class_rf_accuracy: 0.679\n    edd_at_075: 4\n    edd_note: d3v4=0.750>=0.75 PASS, d4v5=0.681<0.75 FAIL → EDD=4\n- id: plan_011c\n  claim: 2\n  description: OLMo-1B depth extension d4/d5 + EDD cross-model verification\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - plan_002\n  - plan_011\n  notes: 第 3 个模型 EDD 验证。代码已就绪 (run_depth_extension_olmo.sh)，含 binary pairwise eval。Reviewer\n    PASS。排 granularity ablation 之后上 cuda:1。\n  registry_id: depth_extension_olmo_d4d5_002\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.968\n      d2v3_auc: 0.843\n      d3v4_auc: 0.765\n      d4v5_auc: 0.684\n    six_class_rf_accuracy: 0.667\n    edd_at_075: 4\n    edd_note: d3v4=0.765>=0.75 PASS, d4v5=0.684<0.75 FAIL → EDD=4\n- id: plan_012\n  claim: 1\n  description: 'Granularity ablation (RF): binary / 3-class / 4-class / 6-class'\n  registry_id: granularity_ablation_rf_001\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: 'Plan A: 用 RF 做，不依赖 DCOL。与 plan_011 depth extension 联动（6-class 需要 5+ depths\n    数据）。'\n  status: DONE\n  conclusion: success\n  metrics:\n    summary:\n      binary_acc_mean: 0.995\n      binary_acc_std: 0.004\n      3class_acc_mean: 0.721\n      3class_acc_std: 0.067\n      4class_acc_mean: 0.783\n      4class_acc_std: 0.048\n      6class_acc: 0.629\n      note: '3-class excludes d0 (most separable class), so 3class < 4class is by\n        design. True granularity trend (with d0): binary 99.5% > 4-class 78.3% > 6-class\n        62.9% — monotonic decrease confirmed.'\n    per_cell:\n      pythia_nucleus095:\n        binary:\n          acc: 0.998\n          ci95:\n          - 0.9965\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7117\n          ci95:\n          - 0.6947\n          - 0.7283\n          auc:\n            d1v2: 0.861\n            d2v3: 0.796\n        4class:\n          acc: 0.7812\n          ci95:\n          - 0.7677\n          - 0.7935\n          auc:\n            d0v1: 0.998\n            d1v2: 0.868\n            d2v3: 0.804\n        6class:\n          acc: 0.6292\n          ci95:\n          - 0.6175\n          - 0.6412\n          auc:\n            d0v1: 0.997\n            d1v2: 0.83\n            d2v3: 0.689\n            d3v4: 0.692\n            d4v5: 0.691\n      pythia_temp09:\n        binary:\n          acc: 0.997\n          ci95:\n          - 0.9952\n          - 0.9985\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7063\n          ci95:\n          - 0.6907\n          - 0.723\n          auc:\n            d1v2: 0.838\n            d2v3: 0.806\n        4class:\n          acc: 0.7605\n          ci95:\n          - 0.7475\n          - 0.7738\n          auc:\n            d0v1: 0.997\n            d1v2: 0.835\n            d2v3: 0.796\n      pythia_topk50:\n        binary:\n          acc: 0.9945\n          ci95:\n          - 0.992\n          - 0.9965\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.5883\n          ci95:\n          - 0.5717\n          - 0.6073\n          auc:\n            d1v2: 0.749\n            d2v3: 0.705\n        4class:\n          acc: 0.6943\n          ci95:\n          - 0.6805\n          - 0.708\n          auc:\n            d0v1: 0.994\n            d1v2: 0.761\n            d2v3: 0.695\n      gpt2xl_nucleus095:\n        binary:\n          acc: 0.9912\n          ci95:\n          - 0.9882\n          - 0.9938\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.79\n          ci95:\n          - 0.775\n          - 0.8047\n          auc:\n            d1v2: 0.913\n            d2v3: 0.891\n        4class:\n          acc: 0.8393\n          ci95:\n          - 0.8283\n          - 0.8502\n          auc:\n            d0v1: 0.995\n            d1v2: 0.916\n            d2v3: 0.885\n      gpt2xl_temp09:\n        binary:\n          acc: 0.9978\n          ci95:\n          - 0.9962\n          - 0.999\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.826\n          ci95:\n          - 0.8117\n          - 0.8397\n          auc:\n            d1v2: 0.944\n            d2v3: 0.887\n        4class:\n          acc: 0.8552\n          ci95:\n          - 0.844\n          - 0.866\n          auc:\n            d0v1: 0.997\n            d1v2: 0.939\n            d2v3: 0.886\n      gpt2xl_topk50:\n        binary:\n          acc: 0.9952\n          ci95:\n          - 0.993\n          - 0.9972\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.695\n          ci95:\n          - 0.6777\n          - 0.7113\n          auc:\n            d1v2: 0.844\n            d2v3: 0.766\n        4class:\n          acc: 0.757\n          ci95:\n          - 0.743\n          - 0.7702\n          auc:\n            d0v1: 0.993\n            d1v2: 0.824\n            d2v3: 0.762\n      olmo_nucleus095:\n        binary:\n          acc: 0.9868\n          ci95:\n          - 0.9832\n          - 0.99\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.7503\n          ci95:\n          - 0.7353\n          - 0.7657\n          auc:\n            d1v2: 0.873\n            d2v3: 0.831\n        4class:\n          acc: 0.7897\n          ci95:\n          - 0.7772\n          - 0.8027\n          auc:\n            d0v1: 0.985\n            d1v2: 0.87\n            d2v3: 0.816\n      olmo_temp09:\n        binary:\n          acc: 0.9982\n          ci95:\n          - 0.997\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7633\n          ci95:\n          - 0.7477\n          - 0.7797\n          auc:\n            d1v2: 0.894\n            d2v3: 0.838\n        4class:\n          acc: 0.8263\n          ci95:\n          - 0.8147\n          - 0.8385\n          auc:\n            d0v1: 0.996\n            d1v2: 0.903\n            d2v3: 0.828\n      olmo_topk50:\n        binary:\n          acc: 0.996\n          ci95:\n          - 0.994\n          - 0.9978\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.661\n          ci95:\n          - 0.644\n          - 0.6773\n          auc:\n            d1v2: 0.812\n            d2v3: 0.739\n        4class:\n          acc: 0.7435\n          ci95:\n          - 0.73\n          - 0.758\n          auc:\n            d0v1: 0.995\n            d1v2: 0.831\n            d2v3: 0.738\n    boundary_dilution:\n      d2v3_auc_by_granularity_pythia_nuc:\n        3class: 0.796\n        4class: 0.804\n        6class: 0.689\n      d1v2_auc_by_granularity_pythia_nuc:\n        3class: 0.861\n        4class: 0.868\n        6class: 0.83\n      note: d2v3 AUC drops 14% from 4-class to 6-class (0.804→0.689), confirming decision\n        boundary dilution at higher granularity\n    decoding_strategy_ranking:\n      4class_acc:\n        temp09: 0.814\n        nucleus095: 0.803\n        topk50: 0.732\n      note: topk50 consistently worst across all 3 models; temp09 slightly outperforms\n        nucleus095\n- id: plan_013\n  claim: 3\n  description: Downstream curation proof-of-concept\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: downstream_curation_poc_001\n  notes: 'DONE. RF curation 不优于 unfiltered (negative for original hypothesis)，但显著优于\n    random (p<0.002 all tiers)。Data efficiency story: 44% data ≈ full PPL。Supplement:\n    random_soft_control_001 (success, rf_soft vs random_soft p=5.6e-5)。已写入 Discussion\n    + Appendix。'\n  status: DONE\n  conclusion: negative\n  metrics:\n    unfiltered:\n      ppl_mean: 15.776\n      ppl_std: 0.066\n      n_samples: 10000\n    rf_strict:\n      ppl_mean: 15.81\n      ppl_std: 0.061\n      n_samples: 2496\n      delta: '-0.034'\n      p: 0.607\n      d: -0.528\n    rf_moderate:\n      ppl_mean: 15.756\n      ppl_std: 0.056\n      n_samples: 4940\n      delta: '+0.021'\n      p: 0.492\n      d: 0.334\n    rf_soft:\n      ppl_mean: 15.733\n      ppl_std: 0.038\n      n_samples: 4422\n      delta: '+0.043'\n      p: 0.407\n      d: 0.792\n    oracle_strict:\n      ppl_mean: 15.879\n      ppl_std: 0.128\n      n_samples: 2500\n      delta: '-0.103'\n      p: 0.216\n      d: -1.004\n    oracle_moderate:\n      ppl_mean: 15.809\n      ppl_std: 0.103\n      n_samples: 5000\n      delta: '-0.033'\n      p: 0.485\n      d: -0.384\n    random_strict:\n      ppl_mean: 16.239\n      ppl_std: 0.165\n      n_samples: 2496\n      delta: '-0.463'\n      p: 0.013\n      d: -3.671\n      sig: true\n    random_moderate:\n      ppl_mean: 15.998\n      ppl_std: 0.09\n      n_samples: 5000\n      delta: '-0.222'\n      p: 0.028\n      d: -2.809\n      sig: true\n    cross_condition:\n      rf_strict_vs_random_strict:\n        delta: 0.429\n        t: -7.052\n        p: 0.002\n        sig: true\n      rf_moderate_vs_random_moderate:\n        delta: 0.242\n        t: -3.77\n        p: 0.02\n        sig: true\n      rf_soft_vs_unfiltered:\n        delta: 0.043\n        t: 0.927\n        p: 0.407\n        sig: false\n      random_strict_vs_unfiltered:\n        delta: -0.463\n        t: 4.219\n        p: 0.014\n        sig: true\n- id: plan_014\n  claim: 1\n  description: 13B clean FP16 scale validation (Qwen2.5-14B, nucleus, d0-d3)\n  priority: P0\n  gpu_budget_hours: 18\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: 替代原 7B QLoRA（结果矛盾）。Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。完整\n    d0-d3 nucleus 递归链 + 19 特征提取 + RF/LR 分类。验证 depth signal 在主流模型规模上是否持续。cuda:0。\n  status: planned\n- id: plan_015\n  claim: 2\n  description: Wild-data calibration on RedPajama/Dolma\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: 延后到 AAAI 窗口。当前优先级让位于 plan_014/016/018。\n  status: planned\n- id: plan_016\n  claim: 1\n  description: Prompted generation ecological validity (GPT-2 XL, topic-seeded d0-d3)\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_003\n  notes: 验证 depth signal 是否为 BOS-seeded 无条件生成的 artifact。用 topic prompt 前缀（\"The following\n    article discusses...\"等）生成 d0，LoRA fine-tune 后生成 d1-d3，提取 19 特征 + RF 分类。选 GPT-2\n    XL 因为它信号最强，如果 prompted 模式下信号消失则说明生成方式是关键因素。cuda:1。\n  status: planned\n- id: plan_017\n  claim: 3\n  description: Cross-strategy two-stage pipeline (strategy classifier + conditioned\n    depth)\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  - plan_007\n  notes: 两阶段方案解决 59.1% 跨策略准确率问题。(a) 策略识别分类器：19 特征 → 3-class (nucleus/temp/topk)，预计\n    >90%。(b) 策略条件深度分类器：识别策略后用策略专属 RF 估深度。将论文弱点转化为实际贡献。主要是 CPU 任务，不占 GPU。\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_004\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_base_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_base_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_pythia_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_qwen_base_004\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_pythia_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_4class_acc: 0.782\n    full_4class_acc_ci:\n    - 0.769\n    - 0.794\n    full_4class_acc_stratified: 0.781\n    full_mae: 0.2367\n    full_auc_0v1: 0.9975\n    full_auc_1v2: 0.8607\n    full_auc_2v3: 0.8005\n    filtered_4class_acc: 0.816\n    filtered_4class_acc_ci:\n    - 0.803\n    - 0.829\n    filtered_mae: 0.1995\n    filtered_auc_0v1: 0.9977\n    filtered_auc_1v2: 0.8782\n    filtered_auc_2v3: 0.8323\n    filtered_sample_count: 16993\n    three_class_acc: 0.708\n    three_class_acc_ci:\n    - 0.692\n    - 0.725\n    three_class_mae: 0.3203\n    three_class_auc_1v2: 0.854\n    three_class_auc_1v3: 0.9569\n    three_class_auc_2v3: 0.7931\n    three_class_recall_d1: 0.79\n    three_class_recall_d2: 0.607\n    three_class_recall_d3: 0.728\n    three_class_precision_d1: 0.852\n    three_class_precision_d2: 0.605\n    three_class_precision_d3: 0.68\n    three_class_f1_d1: 0.82\n    three_class_f1_d2: 0.606\n    three_class_f1_d3: 0.703\n    three_class_lr_acc: 0.671\n    filtered_three_class_acc: 0.747\n    filtered_three_class_acc_ci:\n    - 0.727\n    - 0.764\n    filtered_three_class_mae: 0.2759\n    filtered_three_class_recall_d1: 0.862\n    filtered_three_class_recall_d2: 0.635\n    filtered_three_class_recall_d3: 0.735\n    filtered_three_class_precision_d1: 0.867\n    filtered_three_class_precision_d2: 0.659\n    filtered_three_class_precision_d3: 0.704\n    filtered_three_class_f1_d1: 0.864\n    filtered_three_class_f1_d2: 0.647\n    filtered_three_class_f1_d3: 0.719\n    filtered_three_class_auc_1v2: 0.8926\n    filtered_three_class_auc_1v3: 0.9769\n    filtered_three_class_auc_2v3: 0.8272\n    filtered_three_class_sample_count: 12012\n    best_model: RandomForest\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    truncation_length: 498\n    feature_dim: 19\n- exp_id: cross_model_olmo_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    status: PIPELINE_CRASHED\n    completed_steps:\n    - depth0_lora_finetune\n    failed_at: shell_script_line_52_unmatched_quote\n    depth0_final_loss: 2.2686\n    depth0_train_runtime_s: 283.2\n    depth0_train_steps: 939\n    depth0_trainable_params: 3145728\n    depth0_total_params: 1179910144\n    classification_results: null\n    note: Script crashed after depth-0 finetune. No depth-1/2/3 generation, no feature\n      extraction, no classification performed.\n- exp_id: cross_model_gpt2xl_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.833\n    four_class_acc_ci:\n    - 0.823\n    - 0.845\n    four_class_acc_lr: 0.813\n    auc_0v1: 0.9941\n    auc_0v2: 0.9965\n    auc_0v3: 0.9988\n    auc_1v2: 0.9131\n    auc_1v3: 0.9857\n    auc_2v3: 0.8829\n    three_class_acc: 0.793\n    three_class_acc_ci:\n    - 0.778\n    - 0.806\n    three_class_auc_1v2: 0.9109\n    three_class_auc_1v3: 0.989\n    three_class_auc_2v3: 0.8885\n    finetune_losses:\n      depth_0: 2.55\n      depth_1: 1.715\n      depth_2: 1.342\n    top_features:\n    - p90_ppl (0.208)\n    - var_surprisal (0.208)\n    - p75_ppl (0.103)\n    - mean_surprisal (0.082)\n    - mean_ppl (0.065)\n    code_contamination:\n      d0: 0.005\n      d1: 0.005\n      d2: 0.013\n      d3: 0.007\n- exp_id: pythia_temp09_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.7625\n      rf_accuracy_ci:\n      - 0.749\n      - 0.7753\n      lr_accuracy: 0.7405\n      lr_accuracy_ci:\n      - 0.7265\n      - 0.7545\n      pairwise_auc:\n        0v1: 0.9968\n        0v2: 0.9993\n        0v3: 0.9991\n        1v2: 0.8327\n        1v3: 0.959\n        2v3: 0.7928\n      top_features:\n      - var_surprisal (0.1776)\n      - p90_ppl (0.1501)\n      - mean_ppl (0.1140)\n      - mean_surprisal (0.0889)\n      - p75_ppl (0.0687)\n      feature_dim: 19\n      truncation_length: 498\n    three_class_full:\n      accuracy: 0.6983\n      accuracy_ci:\n      - 0.682\n      - 0.715\n      mae: 0.3357\n      recall:\n        d1: 0.802\n        d2: 0.554\n        d3: 0.739\n      precision:\n        d1: 0.792\n        d2: 0.608\n        d3: 0.686\n      f1:\n        d1: 0.797\n        d2: 0.58\n        d3: 0.712\n      pairwise_auc:\n        d1v2: 0.8354\n        d1v3: 0.9631\n        d2v3: 0.8043\n    three_class_filtered:\n      accuracy: 0.7252\n      accuracy_ci:\n      - 0.7064\n      - 0.7427\n      mae: 0.2953\n      recall:\n        d1: 0.842\n        d2: 0.596\n        d3: 0.735\n      precision:\n        d1: 0.821\n        d2: 0.628\n        d3: 0.715\n      f1:\n        d1: 0.831\n        d2: 0.611\n        d3: 0.725\n      pairwise_auc:\n        d1v2: 0.8656\n        d1v3: 0.9772\n        d2v3: 0.8295\n      n_samples: 11445\n      n_removed: 3555\n    finetune_losses:\n      depth_0: 2.222\n      depth_1: 1.37\n      depth_2: 1.006\n    code_contamination:\n      d0: 0.004\n      d1: 0.077\n      d2: 0.116\n      d3: 0.136\n- exp_id: pythia_topk50_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.696\n    rf_4class_acc_ci:\n    - 0.6825\n    - 0.7107\n    lr_4class_acc: 0.682\n    rf_3class_acc: 0.592\n    rf_3class_acc_ci:\n    - 0.575\n    - 0.6107\n    rf_3class_filtered_acc: 0.6133\n    rf_3class_filtered_acc_ci:\n    - 0.593\n    - 0.6312\n    pairwise_auc_rf:\n      d0v1: 0.9927\n      d0v2: 0.9983\n      d0v3: 0.9978\n      d1v2: 0.7518\n      d1v3: 0.9176\n      d2v3: 0.6918\n    pairwise_auc_3class_filtered_rf:\n      d1v2: 0.768\n      d1v3: 0.9323\n      d2v3: 0.7013\n    feature_importance_top5:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    finetune_loss:\n      depth_0: 2.2406\n      depth_1: 1.6704\n      depth_2: 1.4374\n    code_contamination_narrow:\n      depth_0: 0.004\n      depth_1: 0.077\n      depth_2: 0.123\n      depth_3: 0.131\n- exp_id: cross_model_olmo_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.788\n    four_class_acc_ci:\n    - 0.776\n    - 0.8\n    four_class_acc_lr: 0.751\n    auc_0v1: 0.9834\n    auc_0v2: 0.9949\n    auc_0v3: 0.9989\n    auc_1v2: 0.8673\n    auc_1v3: 0.9806\n    auc_2v3: 0.8124\n    three_class_acc: 0.744\n    three_class_acc_ci:\n    - 0.728\n    - 0.76\n    three_class_mae: 0.27\n    three_class_auc_1v2: 0.8664\n    three_class_auc_1v3: 0.9852\n    three_class_auc_2v3: 0.8274\n    three_class_recall:\n      d1: 0.864\n      d2: 0.607\n      d3: 0.761\n    three_class_precision:\n      d1: 0.863\n      d2: 0.646\n      d3: 0.718\n    four_class_per_class:\n      d0:\n        precision: 0.95\n        recall: 0.99\n        f1: 0.97\n      d1:\n        precision: 0.85\n        recall: 0.82\n        f1: 0.83\n      d2:\n        precision: 0.63\n        recall: 0.59\n        f1: 0.61\n      d3:\n        precision: 0.71\n        recall: 0.76\n        f1: 0.73\n    finetune_losses:\n      depth_0: 2.269\n      depth_1: 1.65\n      depth_2: 1.226\n    top_features:\n    - p90_ppl (0.18)\n    - var_surprisal (0.16)\n    - p75_ppl (0.11)\n    - mean_surprisal (0.08)\n    - type_token_ratio (0.06)\n    code_contamination:\n      d0: 0.005\n      d1: 0.027\n      d2: 0.007\n      d3: 0.008\n    feature_dim: 19\n    truncation_length: 507\n- exp_id: gpt2xl_temp09_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data:\n      samples_per_depth: 5000\n      total_samples: 20000\n      depths: 4\n    finetune_losses:\n      depth_1: 2.5498\n      depth_2: 1.6972\n      depth_3: 1.2922\n    code_contamination:\n      depth_0:\n        broad: 25\n        narrow: 20\n        broad_pct: 0.5\n        narrow_pct: 0.4\n      depth_1:\n        broad: 25\n        narrow: 40\n        broad_pct: 0.5\n        narrow_pct: 0.8\n      depth_2:\n        broad: 34\n        narrow: 80\n        broad_pct: 0.7\n        narrow_pct: 1.6\n      depth_3:\n        broad: 25\n        narrow: 76\n        broad_pct: 0.5\n        narrow_pct: 1.5\n    four_class:\n      rf_accuracy: 0.8542\n      rf_accuracy_ci:\n      - 0.843\n      - 0.8653\n      lr_accuracy: 0.8155\n      lr_accuracy_ci:\n      - 0.8025\n      - 0.8273\n      rf_auc:\n        d0v1: 0.9963\n        d0v2: 0.9992\n        d0v3: 1\n        d1v2: 0.9367\n        d1v3: 0.9947\n        d2v3: 0.8815\n      lr_auc:\n        d0v1: 0.984\n        d0v2: 0.9998\n        d0v3: 1\n        d1v2: 0.8903\n        d1v3: 0.9824\n        d2v3: 0.8183\n      top_features:\n      - p90_ppl\n      - mean_surprisal\n      - p75_ppl\n      - var_surprisal\n    three_class:\n      rf_accuracy: 0.82\n      rf_accuracy_ci:\n      - 0.806\n      - 0.834\n      lr_accuracy: 0.7773\n      lr_accuracy_ci:\n      - 0.7627\n      - 0.792\n      rf_auc:\n        d1v2: 0.9418\n        d1v3: 0.9967\n        d2v3: 0.8849\n    three_class_filtered:\n      rf_accuracy: 0.815\n      rf_accuracy_ci:\n      - 0.7999\n      - 0.8298\n      lr_accuracy: 0.7869\n      lr_accuracy_ci:\n      - 0.7711\n      - 0.8016\n      rf_auc:\n        d1v2: 0.937\n        d1v3: 0.9944\n        d2v3: 0.8891\n- exp_id: dcol_deberta_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cross_model_olmo_temp09_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: olmo_temp09_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.8203\n      d1v2_auc: 0.901\n    three_class_filtered:\n      rf_accuracy: 0.7757\n    finetune_losses:\n      depth_0: 2.27\n      depth_1: 1.63\n      depth_2: 1.18\n    code_contamination_narrow_max: 0.007\n    top_features:\n    - p90_ppl (0.199)\n    - var_surprisal (0.174)\n    - p75_ppl (0.126)\n- exp_id: olmo_topk50_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      lr_accuracy: 0.757\n      lr_accuracy_ci:\n      - 0.7425\n      - 0.7702\n      rf_accuracy: 0.742\n      rf_accuracy_ci:\n      - 0.7282\n      - 0.7555\n    pairwise_auc:\n      lr:\n        d0v1: 0.9969\n        d0v2: 0.9995\n        d0v3: 0.9998\n        d1v2: 0.8293\n        d1v3: 0.9592\n        d2v3: 0.7497\n      rf:\n        d0v1: 0.993\n        d0v2: 0.9983\n        d0v3: 0.9991\n        d1v2: 0.8305\n        d1v3: 0.9591\n        d2v3: 0.7357\n    three_class:\n      lr_accuracy: 0.6567\n      lr_accuracy_ci:\n      - 0.6403\n      - 0.6733\n      rf_accuracy: 0.6517\n      rf_accuracy_ci:\n      - 0.635\n      - 0.6687\n    three_class_filtered:\n      lr_accuracy: 0.6703\n      lr_accuracy_ci:\n      - 0.653\n      - 0.6882\n      rf_accuracy: 0.6699\n      rf_accuracy_ci:\n      - 0.6537\n      - 0.6875\n    three_class_filtered_auc:\n      lr:\n        d1v2: 0.7903\n        d1v3: 0.97\n        d2v3: 0.7501\n      rf:\n        d1v2: 0.8071\n        d1v3: 0.9645\n        d2v3: 0.7364\n    feature_importance_top5:\n    - p90_ppl\n    - var_surprisal\n    - p75_ppl\n    - mean_surprisal\n    - p25_ppl\n    finetune_loss:\n      depth_1: 1.946\n      depth_2: 1.726\n    code_contamination:\n      narrow_pct:\n        depth_0: 0.4\n        depth_1: 0.8\n        depth_2: 0.3\n        depth_3: 0.4\n      broad_pct:\n        depth_0: 0.5\n        depth_1: 2.5\n        depth_2: 0.8\n        depth_3: 0.7\n- exp_id: gpt2xl_topk50_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      accuracy: 0.766\n      depth1_vs_depth2_auc: 0.8259\n      pass: true\n    three_class:\n      accuracy: 0.695\n      depth1_vs_depth2_auc: 0.8392\n      pass: true\n    three_class_filtered:\n      accuracy: 0.684\n      depth1_vs_depth2_auc: 0.8314\n      pass: true\n- exp_id: dcol_deberta_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: dcol_deberta_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: atlas_v1_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    monotonicity_rho_range:\n    - -0.89\n    - -0.82\n    edd: 3\n    edd_saturated: false\n    cross_model_jaccard: 0.667\n    cross_model_rank_corr: 0.85\n    artifacts:\n    - monotonicity_scores.json\n    - cross_model_comparison.json\n    - edd_analysis.json\n    - feature_trajectory.json\n- exp_id: olmo_temp09_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: baseline_battery_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_reg_single_4class_acc: 0.251\n    ppl_reg_multi_4class_acc: 0.622\n    ce_mlp_4class_acc: 0.749\n    coral_4class_acc: 0.7807\n    coral_3class_acc: 0.7089\n    coral_mae: 0.2273\n    coral_d1v2_auc: 0.8179\n    diveye_4class_acc: 0.7817\n    diveye_3class_acc: 0.7098\n    diveye_d1v2_auc: 0.8654\n    rf_4class_acc: 0.781\n    lr_4class_acc: 0.75\n    note: CE-MLP 74.9% may be undertrained (5 epochs); CORAL updated to 100 epochs.\n      All results from Pythia nucleus baseline features.\n- exp_id: dcol_deberta_004\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: dcol_deberta_005\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: batch_feature_extraction_5cells\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: depth_extension_pythia_d4d5_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    six_class_rf_accuracy: 0.6232\n    six_class_rf_accuracy_ci:\n    - 0.6113\n    - 0.636\n    six_class_lr_accuracy: 0.5862\n    pairwise_auc_rf:\n      d0v1: 0.9962\n      d1v2: 0.8231\n      d2v3: 0.6878\n      d3v4: 0.6809\n      d4v5: 0.6948\n    pairwise_auc_lr:\n      d0v1: 0.9908\n      d1v2: 0.6901\n      d2v3: 0.6174\n      d3v4: 0.6828\n      d4v5: 0.6554\n    cumulative_auc_rf:\n      d0v5: 0.9987\n      d1v5: 0.9874\n      d2v5: 0.949\n      d3v5: 0.8632\n    edd_at_075: 2\n    feature_importance_top5:\n    - p90_ppl (0.1376)\n    - var_surprisal (0.1344)\n    - mean_ppl (0.0796)\n    - mean_surprisal (0.0789)\n    - p75_ppl (0.0680)\n    finetune_losses:\n      depth_3: 0.7634\n      depth_4: 0.5828\n    WARNING: 6-class pairwise AUC 不可与 4-class 直比，决策边界稀释导致系统性偏低。需 binary pairwise classifier\n      重新评估。\n- exp_id: cross_model_loo_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    mean_4class_acc: 0.664\n    holdout_pythia:\n      acc: 0.6242\n      ci:\n      - 0.6206\n      - 0.6282\n      d1v2_auc: 0.5617\n      d2v3_auc: 0.6534\n    holdout_olmo:\n      acc: 0.6921\n      ci:\n      - 0.6886\n      - 0.6959\n      d1v2_auc: 0.7687\n      d2v3_auc: 0.6862\n    holdout_gpt2xl:\n      acc: 0.6756\n      ci:\n      - 0.6719\n      - 0.6792\n      d1v2_auc: 0.8157\n      d2v3_auc: 0.6639\n    per_class_recall:\n      holdout_pythia:\n        d0: 1\n        d1: 0.493\n        d2: 0.268\n        d3: 0.736\n      holdout_olmo:\n        d0: 0.993\n        d1: 0.755\n        d2: 0.433\n        d3: 0.588\n      holdout_gpt2xl:\n        d0: 0.985\n        d1: 0.747\n        d2: 0.526\n        d3: 0.445\n    gate_passed: true\n    gate_threshold: 0.45\n- exp_id: cross_model_loo_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_acc: 0.664\n    mean_3class_acc: 0.5544\n    holdout_pythia:\n      acc: 0.6242\n      ci95:\n      - 0.6205\n      - 0.6282\n      3class_acc: 0.499\n      3class_ci95:\n      - 0.4944\n      - 0.5034\n      d1v2_auc: 0.5617\n      d1v3_auc: 0.8547\n      d2v3_auc: 0.6534\n      d0v1_auc: 0.9921\n      d0v2_auc: 0.9999\n      d0v3_auc: 0.9998\n      per_class:\n        d0:\n          P: 0.9889\n          R: 1\n          F1: 0.9944\n        d1:\n          P: 0.6655\n          R: 0.493\n          F1: 0.5664\n        d2:\n          P: 0.3699\n          R: 0.2677\n          F1: 0.3106\n        d3:\n          P: 0.483\n          R: 0.7363\n          F1: 0.5834\n    holdout_olmo:\n      acc: 0.6921\n      ci95:\n      - 0.6884\n      - 0.696\n      3class_acc: 0.592\n      3class_ci95:\n      - 0.5873\n      - 0.5965\n      d1v2_auc: 0.7687\n      d1v3_auc: 0.9277\n      d2v3_auc: 0.6862\n      per_class:\n        d0:\n          P: 0.9783\n          R: 0.9925\n          F1: 0.9854\n        d1:\n          P: 0.7111\n          R: 0.7549\n          F1: 0.7324\n        d2:\n          P: 0.4616\n          R: 0.4327\n          F1: 0.4467\n        d3:\n          P: 0.5964\n          R: 0.5883\n          F1: 0.5923\n    holdout_gpt2xl:\n      acc: 0.6756\n      ci95:\n      - 0.6717\n      - 0.6795\n      3class_acc: 0.5723\n      3class_ci95:\n      - 0.5679\n      - 0.5767\n      d1v2_auc: 0.8157\n      d1v3_auc: 0.9149\n      d2v3_auc: 0.6639\n      d0v1_auc: 0.9927\n      d0v2_auc: 0.9919\n      d0v3_auc: 0.9876\n      per_class:\n        d0:\n          P: 0.9484\n          R: 0.9853\n          F1: 0.9665\n        d1:\n          P: 0.7093\n          R: 0.7465\n          F1: 0.7274\n        d2:\n          P: 0.4521\n          R: 0.5255\n          F1: 0.486\n        d3:\n          P: 0.5963\n          R: 0.445\n          F1: 0.5097\n    mean_per_class_recall:\n      d0: 0.9926\n      d1: 0.6648\n      d2: 0.4086\n      d3: 0.5899\n    lowest_recall_class: d2\n    lowest_recall_value: 0.4086\n    detailed_artifact: cross_model_loo_detailed.json\n- exp_id: atlas_v2_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    p90_ppl_in_top2: 9/9\n    var_surprisal_in_top2: 7/9\n    edd_equals_3_at_T075: 7/9\n    edd_distribution_T075:\n      '2': 2\n      '3': 7\n    cross_model_rank_corr_range: '[0.619, 0.954]'\n    cross_model_rank_corr_mean: 0.868\n    cv5_accuracy_range: '[0.688, 0.859]'\n    cells_covered: 9/9\n- exp_id: cross_strategy_loo_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_4class_acc: 0.5908\n    pythia_holdout_nucleus:\n      acc: 0.6935\n      d1v2_auc: 0.6903\n      d2v3_auc: 0.7626\n    pythia_holdout_temp09:\n      acc: 0.6281\n      d1v2_auc: 0.576\n      d2v3_auc: 0.724\n    pythia_holdout_topk50:\n      acc: 0.5151\n      d1v2_auc: 0.6393\n      d2v3_auc: 0.5801\n    gpt2xl_holdout_nucleus:\n      acc: 0.5993\n      d1v2_auc: 0.7826\n      d2v3_auc: 0.4985\n    gpt2xl_holdout_temp09:\n      acc: 0.5609\n      d1v2_auc: 0.1288\n      d2v3_auc: 0.6366\n    gpt2xl_holdout_topk50:\n      acc: 0.5364\n      d1v2_auc: 0.8308\n      d2v3_auc: 0.7222\n    olmo_holdout_nucleus:\n      acc: 0.6538\n      d1v2_auc: 0.7931\n      d2v3_auc: 0.6076\n    olmo_holdout_temp09:\n      acc: 0.5816\n      d1v2_auc: 0.2529\n      d2v3_auc: 0.7015\n    olmo_holdout_topk50:\n      acc: 0.5488\n      d1v2_auc: 0.8549\n      d2v3_auc: 0.7107\n    finding_temp09_d1v2_inversion: 'd1v2 AUC inverts when holding out temp09 (GPT-2\n      XL: 0.13, OLMo: 0.25) — temp09 d1→d2 features differ fundamentally from nucleus/topk50'\n- exp_id: dcol_roberta_v6_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.6448\n    test_mae: 0.4052\n    best_val_acc: 0.6436\n    best_epoch: 1\n    epochs_run: 4\n    early_stopping: true\n    train_acc_final: 0.75\n    rf_baseline: 0.782\n    delta_vs_baseline: -0.137\n    overfitting: severe (train 75% vs val 64.4% at best epoch)\n    stability: resolved (no NaN, no collapse, collapse guard passed at step 500)\n- exp_id: baseline_battery_9cell_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_acc_matrix:\n      pythia_nucleus: 0.782\n      pythia_temp09: 0.772\n      pythia_topk50: 0.688\n      olmo_nucleus: 0.796\n      olmo_temp09: 0.827\n      olmo_topk50: 0.759\n      gpt2xl_nucleus: 0.843\n      gpt2xl_temp09: 0.853\n      gpt2xl_topk50: 0.754\n    methods:\n    - RF\n    - LR\n    - CORAL\n    - DivEye\n    cells: 9\n    finding: RF ≈ CORAL > DivEye > LR, max gap ~4pp. GPT-2 XL temp09 best (85.3%),\n      model effect > strategy effect\n    WARNING: best_acc_matrix stores best-across-ALL-methods accuracy, NOT RF-only.\n      For RF accuracy use each cell's own registry (e.g. olmo_topk50_001.metrics.four_class.rf_accuracy).\n      olmo_topk50 diff=2.2pp, olmo_nucleus diff=0.83pp.\n- exp_id: cross_strategy_loo_zscore_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mean_raw_acc: 0.5908\n    mean_zscore_acc: 0.5915\n    raw:\n      pythia_holdout_nucleus:\n        acc: 0.6935\n        d1v2_auc: 0.6903\n        d2v3_auc: 0.7626\n      pythia_holdout_temp09:\n        acc: 0.6281\n        d1v2_auc: 0.576\n        d2v3_auc: 0.724\n      pythia_holdout_topk50:\n        acc: 0.5151\n        d1v2_auc: 0.6393\n        d2v3_auc: 0.5801\n      gpt2xl_holdout_nucleus:\n        acc: 0.5993\n        d1v2_auc: 0.7826\n        d2v3_auc: 0.4985\n      gpt2xl_holdout_temp09:\n        acc: 0.5609\n        d1v2_auc: 0.1288\n        d2v3_auc: 0.6366\n      gpt2xl_holdout_topk50:\n        acc: 0.5364\n        d1v2_auc: 0.8308\n        d2v3_auc: 0.7222\n      olmo_holdout_nucleus:\n        acc: 0.6538\n        d1v2_auc: 0.7931\n        d2v3_auc: 0.6076\n      olmo_holdout_temp09:\n        acc: 0.5816\n        d1v2_auc: 0.2529\n        d2v3_auc: 0.7015\n      olmo_holdout_topk50:\n        acc: 0.5488\n        d1v2_auc: 0.8549\n        d2v3_auc: 0.7107\n    zscore:\n      pythia_holdout_nucleus:\n        acc: 0.6992\n        d1v2_auc: 0.7043\n        d2v3_auc: 0.7683\n      pythia_holdout_temp09:\n        acc: 0.6368\n        d1v2_auc: 0.5943\n        d2v3_auc: 0.7352\n      pythia_holdout_topk50:\n        acc: 0.5155\n        d1v2_auc: 0.6386\n        d2v3_auc: 0.5804\n      gpt2xl_holdout_nucleus:\n        acc: 0.5959\n        d1v2_auc: 0.788\n        d2v3_auc: 0.4927\n      gpt2xl_holdout_temp09:\n        acc: 0.5632\n        d1v2_auc: 0.1348\n        d2v3_auc: 0.631\n      gpt2xl_holdout_topk50:\n        acc: 0.5356\n        d1v2_auc: 0.8391\n        d2v3_auc: 0.7282\n      olmo_holdout_nucleus:\n        acc: 0.6506\n        d1v2_auc: 0.796\n        d2v3_auc: 0.6078\n      olmo_holdout_temp09:\n        acc: 0.5782\n        d1v2_auc: 0.2497\n        d2v3_auc: 0.6871\n      olmo_holdout_topk50:\n        acc: 0.5484\n        d1v2_auc: 0.8579\n        d2v3_auc: 0.7056\n    temp09_d1v2_delta:\n      pythia: 0.0183\n      gpt2xl: 0.006\n      olmo: -0.0033\n    finding: Z-score does NOT fix temp09 d1v2 inversion in RF — RF is scale-invariant\n      (tree splits unaffected by monotonic transforms). Prior z-score recovery (0.13→0.68)\n      was with LR, not RF.\n- exp_id: depth_extension_binary_pairwise_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: depth_extension_binary_pairwise_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d1v2_auc: 0.925\n    d1v2_ci95:\n    - 0.9138\n    - 0.9354\n    d2v3_auc: 0.8225\n    d2v3_ci95:\n    - 0.8052\n    - 0.8402\n    d3v4_auc: 0.7837\n    d3v4_ci95:\n    - 0.7648\n    - 0.8024\n    d4v5_auc: 0.6832\n    d4v5_ci95:\n    - 0.6611\n    - 0.7045\n    edd_determination: '4'\n- exp_id: depth_extension_gpt2xl_d4d5_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.966\n      d2v3_auc: 0.919\n      d3v4_auc: 0.75\n      d4v5_auc: 0.681\n    six_class_rf_accuracy: 0.679\n    edd_at_075: 4\n    edd_note: d3v4=0.750>=0.75 PASS, d4v5=0.681<0.75 FAIL → EDD=4\n- exp_id: zero_shot_llm_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc: 0.4\n    n_samples: 200\n    sample_distribution:\n      d0: 56\n      d1: 47\n      d2: 49\n      d3: 48\n    model: DeepSeek V3.2\n    method: zero-shot prompting\n    vs_rf_baseline: -0.382\n    vs_chance: 0.15\n    note: 40.0% (80/200) above chance (25%) but far below RF 78.2% (-38.2pp). Zero-shot\n      LLM cannot reliably distinguish recursive depth from raw text alone.\n- exp_id: granularity_ablation_rf_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    summary:\n      binary_acc_mean: 0.995\n      binary_acc_std: 0.004\n      3class_acc_mean: 0.721\n      3class_acc_std: 0.067\n      4class_acc_mean: 0.783\n      4class_acc_std: 0.048\n      6class_acc: 0.629\n      note: '3-class excludes d0 (most separable class), so 3class < 4class is by\n        design. True granularity trend (with d0): binary 99.5% > 4-class 78.3% > 6-class\n        62.9% — monotonic decrease confirmed.'\n    per_cell:\n      pythia_nucleus095:\n        binary:\n          acc: 0.998\n          ci95:\n          - 0.9965\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7117\n          ci95:\n          - 0.6947\n          - 0.7283\n          auc:\n            d1v2: 0.861\n            d2v3: 0.796\n        4class:\n          acc: 0.7812\n          ci95:\n          - 0.7677\n          - 0.7935\n          auc:\n            d0v1: 0.998\n            d1v2: 0.868\n            d2v3: 0.804\n        6class:\n          acc: 0.6292\n          ci95:\n          - 0.6175\n          - 0.6412\n          auc:\n            d0v1: 0.997\n            d1v2: 0.83\n            d2v3: 0.689\n            d3v4: 0.692\n            d4v5: 0.691\n      pythia_temp09:\n        binary:\n          acc: 0.997\n          ci95:\n          - 0.9952\n          - 0.9985\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7063\n          ci95:\n          - 0.6907\n          - 0.723\n          auc:\n            d1v2: 0.838\n            d2v3: 0.806\n        4class:\n          acc: 0.7605\n          ci95:\n          - 0.7475\n          - 0.7738\n          auc:\n            d0v1: 0.997\n            d1v2: 0.835\n            d2v3: 0.796\n      pythia_topk50:\n        binary:\n          acc: 0.9945\n          ci95:\n          - 0.992\n          - 0.9965\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.5883\n          ci95:\n          - 0.5717\n          - 0.6073\n          auc:\n            d1v2: 0.749\n            d2v3: 0.705\n        4class:\n          acc: 0.6943\n          ci95:\n          - 0.6805\n          - 0.708\n          auc:\n            d0v1: 0.994\n            d1v2: 0.761\n            d2v3: 0.695\n      gpt2xl_nucleus095:\n        binary:\n          acc: 0.9912\n          ci95:\n          - 0.9882\n          - 0.9938\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.79\n          ci95:\n          - 0.775\n          - 0.8047\n          auc:\n            d1v2: 0.913\n            d2v3: 0.891\n        4class:\n          acc: 0.8393\n          ci95:\n          - 0.8283\n          - 0.8502\n          auc:\n            d0v1: 0.995\n            d1v2: 0.916\n            d2v3: 0.885\n      gpt2xl_temp09:\n        binary:\n          acc: 0.9978\n          ci95:\n          - 0.9962\n          - 0.999\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.826\n          ci95:\n          - 0.8117\n          - 0.8397\n          auc:\n            d1v2: 0.944\n            d2v3: 0.887\n        4class:\n          acc: 0.8552\n          ci95:\n          - 0.844\n          - 0.866\n          auc:\n            d0v1: 0.997\n            d1v2: 0.939\n            d2v3: 0.886\n      gpt2xl_topk50:\n        binary:\n          acc: 0.9952\n          ci95:\n          - 0.993\n          - 0.9972\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.695\n          ci95:\n          - 0.6777\n          - 0.7113\n          auc:\n            d1v2: 0.844\n            d2v3: 0.766\n        4class:\n          acc: 0.757\n          ci95:\n          - 0.743\n          - 0.7702\n          auc:\n            d0v1: 0.993\n            d1v2: 0.824\n            d2v3: 0.762\n      olmo_nucleus095:\n        binary:\n          acc: 0.9868\n          ci95:\n          - 0.9832\n          - 0.99\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.7503\n          ci95:\n          - 0.7353\n          - 0.7657\n          auc:\n            d1v2: 0.873\n            d2v3: 0.831\n        4class:\n          acc: 0.7897\n          ci95:\n          - 0.7772\n          - 0.8027\n          auc:\n            d0v1: 0.985\n            d1v2: 0.87\n            d2v3: 0.816\n      olmo_temp09:\n        binary:\n          acc: 0.9982\n          ci95:\n          - 0.997\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7633\n          ci95:\n          - 0.7477\n          - 0.7797\n          auc:\n            d1v2: 0.894\n            d2v3: 0.838\n        4class:\n          acc: 0.8263\n          ci95:\n          - 0.8147\n          - 0.8385\n          auc:\n            d0v1: 0.996\n            d1v2: 0.903\n            d2v3: 0.828\n      olmo_topk50:\n        binary:\n          acc: 0.996\n          ci95:\n          - 0.994\n          - 0.9978\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.661\n          ci95:\n          - 0.644\n          - 0.6773\n          auc:\n            d1v2: 0.812\n            d2v3: 0.739\n        4class:\n          acc: 0.7435\n          ci95:\n          - 0.73\n          - 0.758\n          auc:\n            d0v1: 0.995\n            d1v2: 0.831\n            d2v3: 0.738\n    boundary_dilution:\n      d2v3_auc_by_granularity_pythia_nuc:\n        3class: 0.796\n        4class: 0.804\n        6class: 0.689\n      d1v2_auc_by_granularity_pythia_nuc:\n        3class: 0.861\n        4class: 0.868\n        6class: 0.83\n      note: d2v3 AUC drops 14% from 4-class to 6-class (0.804→0.689), confirming decision\n        boundary dilution at higher granularity\n    decoding_strategy_ranking:\n      4class_acc:\n        temp09: 0.814\n        nucleus095: 0.803\n        topk50: 0.732\n      note: topk50 consistently worst across all 3 models; temp09 slightly outperforms\n        nucleus095\n- exp_id: depth_extension_olmo_d4d5_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lr_zscore_cross_strategy_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    raw_lr:\n      mean_acc: 0.25\n      note: lbfgs convergence failure on unscaled features, all predictions random\n      pythia_temp09:\n        acc: 0.25\n        d1v2_auc: 0.6313\n      gpt2xl_temp09:\n        acc: 0.25\n        d1v2_auc: 0.5\n      olmo_temp09:\n        acc: 0.25\n        d1v2_auc: 0.5\n    zscore_lr:\n      mean_acc: 0.6081\n      mean_d1v2: 0.6417\n      pythia_temp09:\n        acc: 0.6139\n        d1v2_auc: 0.5201\n      gpt2xl_temp09:\n        acc: 0.5642\n        d1v2_auc: 0.2386\n      olmo_temp09:\n        acc: 0.5546\n        d1v2_auc: 0.1922\n      pythia_nucleus:\n        acc: 0.6425\n        d1v2_auc: 0.6142\n      gpt2xl_nucleus:\n        acc: 0.7397\n        d1v2_auc: 0.8851\n      olmo_nucleus:\n        acc: 0.748\n        d1v2_auc: 0.8627\n      pythia_topk50:\n        acc: 0.5261\n        d1v2_auc: 0.7711\n      gpt2xl_topk50:\n        acc: 0.5352\n        d1v2_auc: 0.8214\n      olmo_topk50:\n        acc: 0.5484\n        d1v2_auc: 0.8696\n    paper_claim_vs_actual:\n      gpt2xl_temp09_d1v2:\n        paper_raw: 0.13\n        paper_zscore: 0.68\n        actual_raw: 0.5\n        actual_zscore: 0.2386\n      olmo_temp09_d1v2:\n        paper_raw: 0.25\n        paper_zscore: 0.83\n        actual_raw: 0.5\n        actual_zscore: 0.1922\n- exp_id: depth_extension_olmo_d4d5_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.968\n      d2v3_auc: 0.843\n      d3v4_auc: 0.765\n      d4v5_auc: 0.684\n    six_class_rf_accuracy: 0.667\n    edd_at_075: 4\n    edd_note: d3v4=0.765>=0.75 PASS, d4v5=0.684<0.75 FAIL → EDD=4\n- exp_id: n2_deberta_finetune_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_mean: 0.5831\n    accuracy_std: 0.0467\n    per_class_f1:\n      d0: 0.947\n      d1: 0.378\n      d2: 0.247\n      d3: 0.656\n    pairwise_auc:\n      d0v1: 0.981\n      d1v2: 0.733\n      d2v3: 0.755\n    vs_rf_baseline: 58.3% vs 78.2% (-19.9pp)\n    elapsed_seconds: 3727\n- exp_id: n2_roberta_finetune_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_mean: 0.5948\n    accuracy_std: 0.0324\n    per_class_f1:\n      d0: 0.958\n      d1: 0.4161\n      d2: 0.2611\n      d3: 0.6472\n    per_class_precision:\n      d0: 0.9983\n      d1: 0.7178\n      d2: 0.2956\n      d3: 0.4958\n    per_class_recall:\n      d0: 0.9208\n      d1: 0.293\n      d2: 0.2338\n      d3: 0.9314\n    pairwise_auc:\n      d0v1: 0.9886\n      d1v2: 0.7522\n      d2v3: 0.7349\n    fold_accuracies:\n    - 0.6022\n    - 0.5595\n    - 0.5623\n    - 0.6018\n    - 0.648\n    vs_rf_baseline: -18.7pp (59.5% vs 78.2%)\n    vs_deberta: +1.2pp acc, +0.019 d1v2_auc, -0.020 d2v3_auc\n    elapsed_seconds: 1942.5\n- exp_id: temp07_pilot_pythia_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples_per_depth: 500\n    depths: 6\n    six_class_rf_accuracy: 0.5733\n    six_class_rf_ci95:\n    - 0.5333\n    - 0.615\n    six_class_lr_accuracy: 0.5467\n    pairwise_auc_rf:\n      d0v1: 0.9981\n      d1v2: 0.8378\n      d2v3: 0.635\n      d3v4: 0.5997\n      d4v5: 0.6025\n    pairwise_auc_lr:\n      d0v1: 0.9954\n      d1v2: 0.8031\n      d2v3: 0.608\n      d3v4: 0.6525\n      d4v5: 0.5652\n    vs_temp09_d1v2_rf: 0.8378 vs 0.8327 (+0.005)\n    vs_temp09_d1v2_lr: 0.8031 vs 0.7833 (+0.020)\n    d1v2_inversion: false\n    top_features:\n    - p90_ppl\n    - var_surprisal\n    - mean_surprisal\n    - mean_ppl\n    - p75_ppl\n- exp_id: zeroshot_llm_500_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.362\n    accuracy_ci95:\n    - 0.32\n    - 0.404\n    ci_width_pp: 8.4\n    mae: 1.028\n    per_class_f1:\n      d0: 0.55\n      d1: 0.18\n      d2: 0.27\n      d3: 0.18\n    per_class_recall:\n      d0: 0.952\n      d1: 0.128\n      d2: 0.248\n      d3: 0.12\n    vs_rf_baseline: 36.2% vs 78.2% (-42.0pp)\n    vs_200_sample: 36.2% vs 40.0% (consistent, within CI)\n    n_samples: 500\n    n_errors: 0\n- exp_id: feat_ablation_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_19_mean_acc: 0.7847\n    full_19_std: 0.0494\n    top5_mean_acc: 0.7678\n    top5_std: 0.0527\n    top2_mean_acc: 0.7152\n    top2_std: 0.0581\n    n_features_95pct_mean: 4.2\n    n_features_95pct_max: 5\n    best_category_all_cells: perplexity\n    perplexity_cat_mean_acc: 0.7668\n    surprisal_cat_mean_acc: 0.7333\n    lexdiv_cat_mean_acc: 0.4618\n    repetition_cat_mean_acc: 0.4374\n    ngram_entropy_cat_mean_acc: 0.3952\n    first_selected_feature_mode: p90_ppl (6/9)\n    first_selected_feature_alt: var_surprisal (3/9)\n    total_runtime_sec: 7822\n- exp_id: feature_ablation_9cell\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: w2_domain_bias_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subexp_a_d1d3_mean_acc: 0.72\n    subexp_a_range: 59.1%-81.8%\n    subexp_b_logo_mean_acc: 0.721\n    subexp_b_range: 59.5%-81.6%\n    subexp_b_note: 'fixed: per-depth seed assignment, groups now depth-balanced. LOGO=CV\n      within noise'\n    subexp_c_depth_pred_mean: 0.72\n    subexp_c_seed_group_pred_mean: 0.102\n    subexp_c_ratio_mean: 7.06\n    subexp_c_note: seed groups at chance (10.2% vs 10%), no measurable domain bias\n    chance_3class: 0.333\n    chance_seed_group: 0.1\n    paper_updated: section_appendix.tex L54-72, conclusion.tex L14\n- exp_id: shap_supplement_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kendalls_w_three_way: 0.8955\n    rho_shap_gini: 0.9312\n    rho_shap_permutation: 0.8392\n    rho_gini_permutation: 0.76\n    cross_cell_shap_consistency_mean_rho: 0.8\n    p90_ppl_top2_cells: 9/9\n    var_surprisal_top2_cells: 8/9\n    ppl_surprisal_shap_share: 0.888\n    shap_top5: p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl\n    addresses: R3-N3 feature importance cross-validation\n- exp_id: xgboost_lgbm_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    xgb_acc: 0.79\n    xgb_std: 0.0046\n    xgb_d0v1_auc: 1\n    xgb_d1v2_auc: 0.931\n    xgb_d2v3_auc: 0.816\n    lgbm_acc: 0.788\n    lgbm_std: 0.0077\n    lgbm_d0v1_auc: 1\n    lgbm_d1v2_auc: 0.931\n    lgbm_d2v3_auc: 0.814\n    rf_acc_ref: 0.782\n    xgb_recall_d0: 0.994\n    xgb_recall_d1: 0.816\n    xgb_recall_d2: 0.596\n    xgb_recall_d3: 0.754\n    lgbm_recall_d0: 0.994\n    lgbm_recall_d1: 0.815\n    lgbm_recall_d2: 0.596\n    lgbm_recall_d3: 0.747\n- exp_id: xgboost_lgbm_3cell_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt2xl_temp09:\n      RF: 85.8\n      XGBoost: 86.2\n      LightGBM: 86.2\n      d1v2_AUC: 0.98\n      d2v3_AUC: 0.886\n    pythia_nucleus095:\n      RF: 78.8\n      XGBoost: 79\n      LightGBM: 78.9\n      d1v2_AUC: 0.931\n      d2v3_AUC: 0.816\n    pythia_topk50:\n      RF: 68.9\n      XGBoost: 68.9\n      LightGBM: 68.7\n      d1v2_AUC: 0.841\n      d2v3_AUC: 0.689\n- exp_id: wild_data_calibration_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext_n_passages: 546\n    wikitext_d0_pct: 100\n    wikitext_d1_pct: 0\n    wikitext_d2_pct: 0\n    wikitext_d3_pct: 0\n    wikitext_mean_p_d0: 0.9963\n    controlled_d0_mean_p_d0: 0.9941\n    controlled_d0_acc: 100\n    controlled_d1_acc: 99.96\n    controlled_d2_acc: 99.94\n    controlled_d3_acc: 99.9\n    cv5_accuracy: 0.7878\n    cv5_std: 0.0056\n    domain_shift_mean_ppl_pct: +621%\n    domain_shift_var_ppl_pct: +503%\n    domain_shift_p90_ppl_pct: +115%\n    finding: WikiText-103 100% classified as d0 despite large feature-space domain\n      shift in perplexity features; RF robust to distribution shift\n- exp_id: downstream_curation_poc_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    unfiltered:\n      ppl_mean: 15.776\n      ppl_std: 0.066\n      n_samples: 10000\n    rf_strict:\n      ppl_mean: 15.81\n      ppl_std: 0.061\n      n_samples: 2496\n      delta: '-0.034'\n      p: 0.607\n      d: -0.528\n    rf_moderate:\n      ppl_mean: 15.756\n      ppl_std: 0.056\n      n_samples: 4940\n      delta: '+0.021'\n      p: 0.492\n      d: 0.334\n    rf_soft:\n      ppl_mean: 15.733\n      ppl_std: 0.038\n      n_samples: 4422\n      delta: '+0.043'\n      p: 0.407\n      d: 0.792\n    oracle_strict:\n      ppl_mean: 15.879\n      ppl_std: 0.128\n      n_samples: 2500\n      delta: '-0.103'\n      p: 0.216\n      d: -1.004\n    oracle_moderate:\n      ppl_mean: 15.809\n      ppl_std: 0.103\n      n_samples: 5000\n      delta: '-0.033'\n      p: 0.485\n      d: -0.384\n    random_strict:\n      ppl_mean: 16.239\n      ppl_std: 0.165\n      n_samples: 2496\n      delta: '-0.463'\n      p: 0.013\n      d: -3.671\n      sig: true\n    random_moderate:\n      ppl_mean: 15.998\n      ppl_std: 0.09\n      n_samples: 5000\n      delta: '-0.222'\n      p: 0.028\n      d: -2.809\n      sig: true\n    cross_condition:\n      rf_strict_vs_random_strict:\n        delta: 0.429\n        t: -7.052\n        p: 0.002\n        sig: true\n      rf_moderate_vs_random_moderate:\n        delta: 0.242\n        t: -3.77\n        p: 0.02\n        sig: true\n      rf_soft_vs_unfiltered:\n        delta: 0.043\n        t: 0.927\n        p: 0.407\n        sig: false\n      random_strict_vs_unfiltered:\n        delta: -0.463\n        t: 4.219\n        p: 0.014\n        sig: true\n- exp_id: wild_data_c4_supplement_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_n_passages: 5000\n    c4_d0_pct: 79.8\n    c4_d1plus_pct: 20.2\n    c4_d1plus_count: 1012\n    wikitext_d0_pct: 100\n    controlled_accuracy: 99.9%+\n    cv5_accuracy: 0.7878\n    misclassified_feature_diff:\n      rep_4gram: +74.7%\n      rep_3gram: +37.0%\n      p90_ppl: +39.6%\n    misclassified_content_type: ads, product descriptions, SEO template content\n    finding: FPR=0% on editorial text (WikiText), FPR≈20% on web-crawl (C4) — false\n      positives driven by template/low-quality content with high repetition and low\n      diversity, not random noise\n- exp_id: pythia7b_cross_scale_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: wild_data_gpt2xl_calibration_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_accuracy: 0.841\n    cv_std: 0.004\n    wikitext_n_passages: 546\n    wikitext_d0_pct: 99.27\n    wikitext_d1_pct: 0.73\n    c4_n_passages: 5000\n    c4_d0_pct: 77.62\n    c4_d1_pct: 9.04\n    c4_d2_pct: 3.72\n    c4_d3_pct: 9.62\n    c4_fpr_vs_pythia: GPT-2 XL FPR 22.4% vs Pythia 20.2% — consistent template/SEO\n      pattern\n    finding: 'Cross-model calibration consistent: both models flag same C4 template\n      content as non-d0. GPT-2 XL slightly higher FPR due to stronger signal. WikiText\n      near-perfect for both.'\n- exp_id: wild_data_olmo_calibration_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_accuracy: 0.7893\n    cv_std: 0.0039\n    wikitext_n_passages: 546\n    wikitext_d0_pct: 98.53\n    wikitext_non_d0: 8\n    c4_n_passages: 5000\n    c4_d0_pct: 95.28\n    c4_d1_pct: 2.92\n    c4_d2_pct: 0.5\n    c4_d3_pct: 1.3\n    c4_fpr: 4.72\n    finding: OLMo C4 FPR (4.72%) far lower than Pythia (20.2%) and GPT-2 XL (22.4%).\n      OLMo d1-d3 features diverge more from d0, creating wider d0 decision boundary\n      that correctly classifies more C4 template content as d0.\n- exp_id: random_soft_control_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_soft_ppl:\n      seed_42: 15.99\n      seed_123: 16.0276\n      seed_456: 16.1682\n      seed_789: 15.9993\n      seed_1024: 16.1224\n      mean: 16.0615\n      std: 0.0794\n    rf_soft_ppl:\n      seed_42: 15.7134\n      seed_123: 15.7014\n      seed_456: 15.7875\n      seed_789: 15.6956\n      seed_1024: 15.7689\n      mean: 15.7334\n      std: 0.042\n    comparison:\n      delta_ppl: 0.3281\n      t_statistic: 17.9777\n      p_value: 5.6e-05\n      cohens_d: 8.0399\n      significant: true\n    train_loss:\n      seed_42: 1.6748\n      seed_123: 1.6786\n      seed_456: 1.6721\n      seed_789: 1.6736\n      seed_1024: 1.6739\n- exp_id: wild_data_redpajama_dolma_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: wild_data_calibration_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: C4 load_dataset hung - allenai/c4 HF streaming failed on AutoDL proxy.\n      OpenWebText loaded OK (5000 passages, 23s) but C4 load_dataset never returned.\n      JSON written with empty datasets/cross_model_consistency. No error/exception\n      in logs - silent hang during HF Hub streaming.\n- exp_id: wild_data_calibration_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fineweb_n_passages: 5000\n    fineweb_d0_pct: 80.54\n    fineweb_d1_pct: 19.46\n    fineweb_d2_pct: 0\n    fineweb_d3_pct: 0\n    fineweb_fpr: 19.46\n    fineweb_mean_p_d0: 0.7987\n    fineweb_mean_p_d1: 0.1707\n    vs_c4_fpr_delta: -0.74\n    vs_wikitext_fpr_delta: 19.46\n    elapsed_seconds: 87\n    finding: FineWeb FPR=19.46% — virtually identical to C4 FPR=20.2% (Δ=-0.74pp).\n      All misclassifications are d1 only (no d2/d3). Confirms web-crawl FPR ~20% is\n      consistent across datasets and driven by template/SEO content, not dataset-specific\n      artifacts.\n- exp_id: zeroshot_qwen7b_500_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    acc_4class: 0.304\n    acc_4class_ci_95:\n    - 0.2653\n    - 0.3457\n    acc_3class: 0.3173\n    mae: 1.01\n    per_class_recall:\n      d0: 0.264\n      d1: 0.552\n      d2: 0.104\n      d3: 0.296\n    per_class_f1:\n      d0: 0.3143\n      d1: 0.3503\n      d2: 0.1436\n      d3: 0.3442\n    errors: 0\n- exp_id: multi_tau_ablation_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_tau:\n      tau_0.5:\n        4class_acc: 0.7725\n        d1v2_auc: 0.8423\n        d0v1_auc: 0.9962\n        d2v3_auc: 0.7636\n      tau_0.7:\n        4class_acc: 0.754\n        d1v2_auc: 0.8505\n        d0v1_auc: 0.9966\n        d2v3_auc: 0.7197\n      tau_0.9:\n        4class_acc: 0.759\n        d1v2_auc: 0.8083\n        d0v1_auc: 0.9911\n        d2v3_auc: 0.7805\n      tau_1.1:\n        4class_acc: 0.5715\n        d1v2_auc: 0.5284\n        d0v1_auc: 0.9878\n        d2v3_auc: 0.5987\n    cross_tau_loo:\n      holdout_0.5:\n        acc: 0.522\n        d1v2_auc: 0.1756\n      holdout_0.7:\n        acc: 0.4095\n        d1v2_auc: 0.2985\n      holdout_0.9:\n        acc: 0.464\n        d1v2_auc: 0.2774\n      holdout_1.1:\n        acc: 0.471\n        d1v2_auc: 0.5251\n      mean_acc: 0.4666\n      mean_d1v2_auc: 0.3192\n    training_loss:\n      tau_0.5:\n        d0: 2.2727\n        d1: 0.4201\n        d2: 0.1589\n      tau_1.1:\n        d0: 2.2726\n        d1: 1.9077\n        d2: 1.8517\n- exp_id: wild_data_calibration_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    openwebtext_pythia_nucleus:\n      n: 5000\n      d0_pct: 99.1\n      fpr_pct: 0.9\n      mean_p_d0: 0.7116\n    openwebtext_gpt2xl:\n      n: 5000\n      d0_pct: 98.56\n      fpr_pct: 1.44\n      mean_p_d0: 0.6191\n    openwebtext_olmo:\n      n: 5000\n      d0_pct: 97.22\n      fpr_pct: 2.78\n      mean_p_d0: 0.7372\n    wikitext: skipped (dtype error)\n    finding: OpenWebText FPR极低(0.9-2.8%) vs C4(4.7-22.4%) vs FineWeb(19.5%). 编辑质量高的web数据FPR显著低于web-crawl。\n- exp_id: cross_scale_qwen7b_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc: 0.601\n    four_class_ci:\n    - 0.58\n    - 0.621\n    six_class_acc: 0.521\n    six_class_ci:\n    - 0.504\n    - 0.538\n    edd: '>5'\n    pairwise_auc_consecutive:\n      d0v1: 0.969\n      d1v2: 0.729\n      d2v3: 0.709\n      d3v4: 0.732\n      d4v5: 0.772\n    auc_pattern: 'U-shape (non-monotonic: trough at d2v3, rises d3v4/d4v5)'\n- exp_id: wild_data_calibration_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fpr: 15.3\n    d0_accuracy: 84.7\n    n_passages: 5000\n    vs_c4: -4.9pp\n    vs_fineweb: -4.16pp\n    vs_openwebtext: +14.4pp\n- exp_id: cross_scale_llama3_8b_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cross_model_recursive_chain_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: domain_extension_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.741\n    4class_std: 0.02\n    per_depth_f1:\n      d0: 1\n      d1: 0.78\n      d2: 0.52\n      d3: 0.66\n    cv_folds: 5\n    domain: arxiv_abstracts\n- exp_id: two_stage_strategy_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    strategy_classification:\n      mean_acc: 0.575\n      chance: 0.333\n      pythia:\n        acc: 0.523\n        nucleus_recall: 0.533\n        temp09_recall: 0.414\n        topk50_recall: 0.622\n      olmo:\n        acc: 0.548\n        nucleus_recall: 0.608\n        temp09_recall: 0.479\n        topk50_recall: 0.558\n      gpt2xl:\n        acc: 0.654\n        nucleus_recall: 0.845\n        temp09_recall: 0.507\n        topk50_recall: 0.61\n    depth_estimation:\n      cross_strategy_loo_ref: 0.591\n      predicted_two_stage:\n        pythia: 0.693\n        olmo: 0.695\n        gpt2xl: 0.73\n        mean: 0.706\n      naive_pooled:\n        pythia: 0.709\n        olmo: 0.712\n        gpt2xl: 0.739\n        mean: 0.72\n      oracle_two_stage:\n        pythia: 0.746\n        olmo: 0.785\n        gpt2xl: 0.82\n        mean: 0.784\n      within_strategy_ref:\n        pythia: 0.745\n        olmo: 0.784\n        gpt2xl: 0.816\n        mean: 0.782\n    key_finding: Oracle two-stage (78.4%) matches within-strategy (78.2%), validating\n      theory. But predicted two-stage (70.6%) < naive pooled (72.0%) due to strategy\n      classification bottleneck (57.5%).\n- exp_id: cross_model_recursive_chain_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.8475\n    4class_ci95:\n    - 0.81\n    - 0.8825\n    per_depth_f1:\n      d0: 0.98\n      d1: 0.88\n      d2: 0.76\n      d3: 0.76\n    pairwise_auc:\n      d0v1: 0.999\n      d2v3: 0.841\n- exp_id: cross_scale_llama3_8b_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cross_scale_llama3_8b_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.702\n    4class_ci95:\n    - 0.683\n    - 0.724\n    6class_acc: 0.554\n    6class_ci95:\n    - 0.536\n    - 0.571\n    edd_estimate: '4'\n    edd_note: d4v5 AUC=0.618 < T=0.70, so EDD=4. Monotonic decay causes last pair\n      to fall below threshold.\n    consecutive_binary_auc:\n      d0v1: 0.949\n      d1v2: 0.877\n      d2v3: 0.771\n      d3v4: 0.716\n      d4v5: 0.618\n    consecutive_binary_acc:\n      d0v1: 0.885\n      d1v2: 0.81\n      d2v3: 0.698\n      d3v4: 0.656\n      d4v5: 0.583\n- exp_id: ref_model_ablation_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_ref_acc: 0.7854\n    olmo_ref_acc: 0.7451\n    delta_pp: 4.04\n    robust: true\n- exp_id: cross_scale_llama3_base_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.599\n    4class_ci_95:\n    - 0.578\n    - 0.6215\n    6class_acc: 0.4953\n    edd_070: 2\n    auc_d0v1: 0.9175\n    auc_d1v2: 0.7936\n    auc_d2v3: 0.6815\n    auc_d3v4: 0.73\n    auc_d4v5: 0.595\n    monotonic: false\n    pattern: U-shape (d2v3 dip, d3v4 recovery)\n    finding: IT regularizes depth signal (makes AUC monotonic), does not introduce\n      U-shape\n    edd_note: d0v1=0.9175≥0.70, d1v2=0.7936≥0.70, d2v3=0.6815<0.70 → EDD=2\n- exp_id: cross_model_reverse_chain_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.75\n    ci_95:\n    - 82\n    - 89.25\n    forward_chain_acc: 84.75\n    forward_chain_ci:\n    - 81\n    - 88.25\n    conclusion: reverse = forward, architecture confound refuted\n- exp_id: lora_rank_ablation_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rank_4_acc: 0.718\n    rank_4_auc: 0.7896\n    rank_16_acc: 0.7645\n    rank_16_auc: 0.8434\n    rank_64_acc: 0.731\n    rank_64_auc: 0.8326\n    best_rank: 16\n- exp_id: gpt2xl_ref_ablation_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    gpt2xl_4class_acc: 0.6734\n    gpt2xl_ci_95:\n    - 0.6667\n    - 0.6796\n    gpt2xl_d1v2_auc: 0.7269\n    pythia_4class_acc: 0.7854\n    pythia_ci_95:\n    - 0.7795\n    - 0.7911\n    pythia_d1v2_auc: 0.8681\n    delta_pp: -11.2\n- exp_id: second_seed_replication_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.7715\n    ci_95:\n    - 0.764\n    - 0.7815\n    d1v2_auc: 0.8531\n    delta_vs_baseline: -0.0105\n    baseline_acc: 0.782\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - var_ppl\n    - p75_ppl\n    per_class_recall:\n      d0: 0.99\n      d1: 0.816\n      d2: 0.586\n      d3: 0.694\n    fold_accuracies:\n    - 0.77\n    - 0.77\n    - 0.79\n    - 0.7675\n    - 0.76\n- exp_id: mixed_depth_corpus_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mixed_overall_acc: 0.855\n    balanced_overall_acc: 0.7814\n    delta_overall_pp: 7.36\n    mixed_macro_recall: 0.7652\n    balanced_macro_recall: 0.7814\n    delta_macro_recall_pp: -1.62\n    per_class_recall_delta:\n      d0: -0.68\n      d1: -2.43\n      d2: -1.12\n      d3: -2.24\n    max_recall_delta_pp: 2.43\n- exp_id: reference_free_baseline_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    4class_acc: 0.5368\n    ci_95:\n    - 0.5336\n    - 0.5401\n    d1v2_auc: 0.6252\n    full_19_acc: 0.7877\n    delta_pp: -25.09\n    recall_d0: 0.8572\n    recall_d1: 0.397\n    recall_d2: 0.3176\n    recall_d3: 0.5756\n- exp_id: ensemble_reference_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ensemble_4class_acc: 0.7365\n    ensemble_ci_95:\n    - 0.7258\n    - 0.7471\n    pythia_acc: 0.7857\n    olmo_acc: 0.7425\n    gpt2xl_acc: 0.7005\n    delta_vs_gpt2xl: 3.6\n    delta_vs_pythia: -4.9\n- exp_id: gen_length_ablation_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    acc_128: 0.6835\n    ci_128:\n    - 0.6765\n    - 0.6905\n    acc_256: 0.738\n    ci_256:\n    - 0.7248\n    - 0.7512\n    acc_512: 0.7782\n    ci_512:\n    - 0.768\n    - 0.7885\n    d1v2_auc_128: 0.7543\n    d1v2_auc_256: 0.8198\n    d1v2_auc_512: 0.8683\n    spread_pp: 9.47\n    delta_128v256_pp: -5.45\n    delta_512v256_pp: 4.02\n- exp_id: cross_seed_transfer_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_seed42_cv: 0.7868\n    within_seed43_cv: 0.7745\n    within_seed_avg: 0.7807\n    train42_test43: 0.7785\n    train43_test42: 0.7568\n    cross_seed_avg: 0.7676\n    delta_pp: -1.3\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T08:19:14.683Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T08:19:14.683Z",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-17T08:19:14.705Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：13B 信号严重衰减或特征结构被破坏；prompted generation 信号接近无效；scale/ecological validity 核心假设失败，需完全 reframe 为 controlled-setting atlas paper
核心假设：['13B clean FP16 accuracy < 62%，或 feature importance 结构被破坏（p90_ppl/var_surprisal 不在 top-5），或出现 U-shape artifact', 'Prompted generation accuracy < 58%（下降 > 25pp），或 d1v2 AUC < 0.65，depth signal 在非 BOS 条件下大幅衰减', 'Scale gap 和 generation mode gap 同时出现，使 Claim 1 的 generalizability 断言不可持续', '策略分类无法改进超过 60%，predicted two-stage 始终 ≤ naive pooled，pipeline 无实际价值', '最强 + 最可靠结果仍局限于 1–1.5B × BOS-seeded × within-strategy 条件', 'Pythia reference model 对 14B output 的 perplexity 特征区分力不足，跨规模特征迁移本质受限']
关键指标范围：{'scale_13b_4class_acc': [0.45, 0.62], 'scale_13b_d1v2_auc': [0.55, 0.7], 'scale_13b_edd_at_075': [1, 2], 'scale_13b_feature_top2_in_top4': False, 'prompted_4class_acc': [0.35, 0.58], 'prompted_d1v2_auc': [0.5, 0.65], 'prompted_acc_retention_vs_bos_pct': [40, 68], 'strategy_clf_acc': [0.5, 0.6], 'twostage_predicted_acc': [0.65, 0.71], 'twostage_oracle_vs_within_gap_pp': [0, 4], 'headline_acc_claim': '70–85% under controlled conditions (1–1.5B, BOS-seeded, within-strategy)'}
叙事方向：核心 reframe：从 "robust framework for depth estimation" 转为 "first systematic  characterization of recursive depth phenomena and the boundary conditions of feature-based  detection." Atlas (Claim 2) 升为唯一 primary contribution——9-cell 矩阵在 1–1.5B 上的完整 分析完全不受 13B/prompted 结果影响，且 EDD=4 across 3 models、feature universality (9/9  cells)、temperature reversal mechanism 都是干净独立的 findings。Claim 1 重写为 bounded  conclusion："ordinal depth estimation is feasible and accurate under controlled conditions  (1–1.5B, BOS-seeded, within-strategy, 70–85%); signal significantly attenuates at larger  scales and under prompted generation, indicating that current statistical-feature approaches  capture a real but fragile signal." 关键叙事转向：13B 弱结果 + prompted 弱结果不写入  Limitations section，而是写入主体 Section 6 "Boundary Conditions of the Depth Signal" ——与 EDD 分析并列，信号在三个维度有衰减边界：depth (EDD=4)、scale (>1.5B attenuation)、 generation mode (prompted attenuation)。Characterizing these boundaries IS the contribution， 类比 "where does the signal break" diagnostic papers (CheckList ACL 2020, DynaBench  NAACL 2021)。Claim 3 降为 Discussion future work。论文定位：task definition + controlled- setting empirical atlas + boundary characterization。EMNLP "New Missions" track 仍为 首选——track CFP 明确要求 data contamination 和 synthetic data feedback loops 研究， task formalization + 完整 boundary characterization 与此完全匹配。不降级目标 venue， 但论文类型从 "framework paper" 退到 "diagnostic/benchmark paper"。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: recursive_gen_depth_est
venue: EMNLP 2026 Main
focus: 评估升级后的叙事能否冲正会。重点关注：(1) 13B clean FP16 实验是否足够回应 scale concern，(2) prompted generation 是否足够回应 ecological validity，(3) 两阶段 cross-strategy pipeline 作为 Claim 3 是否将论文从纯 analysis 升级为有 practical method contribution，(4) 三项新实验加入后论文是否从 Findings 水平提升到 Main Conference 竞争力

## paper_framing.md

# Paper Framing — recursive_gen_depth_est

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25, 2026)
- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)
- EMNLP 2026 special theme "New Missions for NLP Research" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit

## Core Claims (3 条 + Discussion implication)

1. **Ordinal depth estimation is feasible, accurate, and robust across scales and generation modes**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark (1–1.5B), Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all settings. **Scale robustness**: Clean FP16 13B experiment (Qwen2.5-14B, no quantization) confirms depth signal persists at mainstream model scale, addressing the "small model only" concern from prior 7B QLoRA experiments. **Ecological validity**: Prompted generation experiment (topic-seeded text, not BOS-only unconditional) confirms depth signal is not an artifact of unnatural generation mode.

2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the d1/d2 boundary remains open. This atlas spans 3 model families × 3 decoding strategies, with scale consistency confirmed at 14B.

3. **Cross-strategy depth estimation via two-stage pipeline**: Naive cross-strategy transfer degrades to 59.1% with d1v2 boundary inversion. We identify the root cause (temperature's accelerated convergence) and propose a practical two-stage solution: (a) strategy identification classifier using the same 19 features achieves [TBD]% accuracy, then (b) strategy-conditioned depth classifiers restore near within-strategy accuracy. This transforms the cross-strategy limitation from an open problem into a solved deployment challenge.

4. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).

## Story Spine

- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer "is this synthetic?" but not "how many recursive cycles has this undergone?" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.

- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.

- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark spanning 1B–14B models across 3 decoding strategies and 4 depths, and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all settings, (b) model-dependent strategy interaction effects with an identified root cause, and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, and propose a two-stage strategy-aware pipeline that solves the cross-strategy deployment challenge. The depth signal persists under prompted generation (not just BOS-seeded), confirming ecological relevance.

- **Headline result template**: "On our multi-generational benchmark spanning model scales from 1B to 14B and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all settings. The depth signal persists under prompted (topic-seeded) generation and at 14B scale without quantization. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75). We identify strategy-dependent feature trajectory reversal and propose a two-stage pipeline that restores near within-strategy accuracy for cross-strategy deployment."
- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) completed via plan_011.

## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)

DCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。

- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**
- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL
- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（"contrastive ordinal learning 在文本深度估计的固有局限"）
- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）
- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP "New Missions" track

## Venue Fit Risks

- **"Just an empirical study" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding; (e) **cross-strategy two-stage pipeline (Claim 3)** is a concrete practical contribution, not just analysis. EMNLP "New Missions" track explicitly values problem formalization.
- **Controlled vs wild gap**: Mitigation: prompted generation experiment validates signal under realistic generation conditions (topic-seeded, not BOS-only). Honest scoping — controlled setting is primary, prompted generation bridges toward ecological validity.
- **"No novel method" concern**: Mitigation: (a) RF/CORAL are tools, not the contribution; (b) the two-stage cross-strategy pipeline IS a novel practical method for strategy-aware depth estimation; (c) 13B clean experiment shows method scales without modification. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).
- **"Small model only" concern**: Eliminated by clean 13B FP16 experiment. Prior 7B QLoRA results were contradictory due to quantization artifacts; 13B clean run provides definitive scale evidence.

## Dream-Derived Requirements (D002, 2026-05-14)

三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：

### 论文写作硬约束
1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式
2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。"Atlas without maps is a contradiction"
3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)
4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity

### 指标报告硬约束
5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection
6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值
7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis

### Framing 方向
8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 "one strong method within the framework"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。
9. **"First systematic empirical map" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage

### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)
10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 "soft sampling"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 "soft sampling" 分组已被反转数据推翻。
11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。
12. **Limitations 必须写明跨策略部署约束** — "跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。"不可仅将反转作为正面发现消化。

## Anticipated Reviewer Concerns

1. "EDD might be very low (depth 2-3), making the task trivial beyond shallow depths" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 "three models all achieve statistically significant EDD=4"。正确措辞："d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。
2. "Why ordinal and not just binary?" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs
3. "Generalization to unseen models/strategies?" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation could recover d1v2 AUC remains open. Discuss as "strategy shapes degradation trajectory" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).
4. "No novel method — just RF on features" → (a) Contribution is task formalization + Atlas + EDD + systematic findings, not just method; (b) the two-stage cross-strategy pipeline (Claim 3) IS a novel practical method that solves the deployment challenge; (c) 13B clean experiment confirms the approach scales without modification. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9+ settings is itself a finding.
5. "d0 confound inflates headline metrics" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy
6. "EDD threshold is arbitrary" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)
7. "No figures for Atlas" → Minimum 4 figures (Dream D002)
8. "Bibliography too thin" → 25+ refs covering all relevant subfields (Dream D002)
9. "Model-strategy interaction is just noise" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.
10. "Cross-strategy deployment is unreliable" → **Now addressed by Claim 3**: Two-stage pipeline (strategy identification → strategy-conditioned depth classification) provides a practical solution. Strategy classifier expected >90% accuracy on 19 features (strategy distributions are highly separable). After strategy identification, depth classification uses strategy-matched RF, restoring near within-strategy accuracy. The root cause (temperature's accelerated convergence) is identified and the mechanism explained — this is no longer an open problem but a solved deployment challenge.
11. "Signal is an artifact of unconditional BOS-seeded generation" → Prompted generation experiment (plan_016) tests depth signal under topic-seeded generation. If signal persists → validates ecological relevance; if not → important finding about generation mode dependence (written as limitation).
12. "Only tested on small models (1–1.5B)" → Clean 13B FP16 experiment (Qwen2.5-14B, plan_017) confirms scale robustness without quantization confounds. Prior 7B QLoRA results were contradictory — now superseded by clean experiment.


## experiment_plan (with registry status)

- id: plan_001a
  claim: 1
  description: Pythia-1.4B recursive chain — nucleus p=0.95 (MVP)
  priority: P0
  gpu_budget_hours: 2
  deps: []
  status: DONE
  notes: '4 depths × 1 strategy. 78.2% 4-class acc, d1v2 AUC 0.861. Content-type control:
    81.6%.'
  registry_id: mvp_pipeline_pythia_002
  conclusion: success
  metrics: &id001
    full_4class_acc: 0.782
    full_4class_acc_ci:
    - 0.769
    - 0.794
    full_4class_acc_stratified: 0.781
    full_mae: 0.2367
    full_auc_0v1: 0.9975
    full_auc_1v2: 0.8607
    full_auc_2v3: 0.8005
    filtered_4class_acc: 0.816
    filtered_4class_acc_ci:
    - 0.803
    - 0.829
    filtered_mae: 0.1995
    filtered_auc_0v1: 0.9977
    filtered_auc_1v2: 0.8782
    filtered_auc_2v3: 0.8323
    filtered_sample_count: 16993
    three_class_acc: 0.708
    three_class_acc_ci:
    - 0.692
    - 0.725
    three_class_mae: 0.3203
    three_class_auc_1v2: 0.854
    three_class_auc_1v3: 0.9569
    three_class_auc_2v3: 0.7931
    three_class_recall_d1: 0.79
    three_class_recall_d2: 0.607
    three_class_recall_d3: 0.728
    three_class_precision_d1: 0.852
    three_class_precision_d2: 0.605
    three_class_precision_d3: 0.68
    three_class_f1_d1: 0.82
    three_class_f1_d2: 0.606
    three_class_f1_d3: 0.703
    three_class_lr_acc: 0.671
    filtered_three_class_acc: 0.747
    filtered_three_class_acc_ci:
    - 0.727
    - 0.764
    filtered_three_class_mae: 0.2759
    filtered_three_class_recall_d1: 0.862
    filtered_three_class_recall_d2: 0.635
    filtered_three_class_recall_d3: 0.735
    filtered_three_class_precision_d1: 0.867
    filtered_three_class_precision_d2: 0.659
    filtered_three_class_precision_d3: 0.704
    filtered_three_class_f1_d1: 0.864
    filtered_three_class_f1_d2: 0.647
    filtered_three_class_f1_d3: 0.719
    filtered_three_class_auc_1v2: 0.8926
    filtered_three_class_auc_1v3: 0.9769
    filtered_three_class_auc_2v3: 0.8272
    filtered_three_class_sample_count: 12012
    best_model: RandomForest
    top_features:
    - var_surprisal
    - p90_ppl
    - mean_ppl
    - mean_surprisal
    - p75_ppl
    truncation_length: 498
    feature_dim: 19
- id: plan_001b
  claim: 1
  description: Pythia-1.4B — temperature τ=0.9 chain (4 depths)
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: pythia_temp09_001
  notes: τ=0.9 temp-only decoding. Data→data/pythia_temp09/. Launched on cuda:0 after
    OLMo.
  status: DONE
  conclusion: success
  metrics:
    four_class:
      rf_accuracy: 0.7625
      rf_accuracy_ci:
      - 0.749
      - 0.7753
      lr_accuracy: 0.7405
      lr_accuracy_ci:
      - 0.7265
      - 0.7545
      pairwise_auc:
        0v1: 0.9968
        0v2: 0.9993
        0v3: 0.9991
        1v2: 0.8327
        1v3: 0.959
        2v3: 0.7928
      top_features:
      - var_surprisal (0.1776)
      - p90_ppl (0.1501)
      - mean_ppl (0.1140)
      - mean_surprisal (0.0889)
      - p75_ppl (0.0687)
      feature_dim: 19
      truncation_length: 498
    three_class_full:
      accuracy: 0.6983
      accuracy_ci:
      - 0.682
      - 0.715
      mae: 0.3357
      recall:
        d1: 0.802
        d2: 0.554
        d3: 0.739
      precision:
        d1: 0.792
        d2: 0.608
        d3: 0.686
      f1:
        d1: 0.797
        d2: 0.58
        d3: 0.712
      pairwise_auc:
        d1v2: 0.8354
        d1v3: 0.9631
        d2v3: 0.8043
    three_class_filtered:
      accuracy: 0.7252
      accuracy_ci:
      - 0.7064
      - 0.7427
      mae: 0.2953
      recall:
        d1: 0.842
        d2: 0.596
        d3: 0.735
      precision:
        d1: 0.821
        d2: 0.628
        d3: 0.715
      f1:
        d1: 0.831
        d2: 0.611
        d3: 0.725
      pairwise_auc:
        d1v2: 0.8656
        d1v3: 0.9772
        d2v3: 0.8295
      n_samples: 11445
      n_removed: 3555
    finetune_losses:
      depth_0: 2.222
      depth_1: 1.37
      depth_2: 1.006
    code_contamination:
      d0: 0.004
      d1: 0.077
      d2: 0.116
      d3: 0.136
- id: plan_001c
  claim: 1
  description: Pythia-1.4B — top-k k=50 chain (4 depths)
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: pythia_topk50_001
  notes: top-k k=50 decoding. Data→data/pythia_topk50/. Queued for cuda:1 after GPT-2
    XL.
  status: DONE
  conclusion: success
  metrics:
    rf_4class_acc: 0.696
    rf_4class_acc_ci:
    - 0.6825
    - 0.7107
    lr_4class_acc: 0.682
    rf_3class_acc: 0.592
    rf_3class_acc_ci:
    - 0.575
    - 0.6107
    rf_3class_filtered_acc: 0.6133
    rf_3class_filtered_acc_ci:
    - 0.593
    - 0.6312
    pairwise_auc_rf:
      d0v1: 0.9927
      d0v2: 0.9983
      d0v3: 0.9978
      d1v2: 0.7518
      d1v3: 0.9176
      d2v3: 0.6918
    pairwise_auc_3class_filtered_rf:
      d1v2: 0.768
      d1v3: 0.9323
      d2v3: 0.7013
    feature_importance_top5:
    - var_surprisal
    - p90_ppl
    - mean_ppl
    - mean_surprisal
    - p75_ppl
    finetune_loss:
      depth_0: 2.2406
      depth_1: 1.6704
      depth_2: 1.4374
    code_contamination_narrow:
      depth_0: 0.004
      depth_1: 0.077
      depth_2: 0.123
      depth_3: 0.131
- id: plan_002
  claim: 1
  description: OLMo-1B recursive chain (4 depths × 3 strategies)
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: cross_model_olmo_002
  notes: OLMo-1B on Dolma. q_proj/k_proj/v_proj LoRA. olmo_001 failed (script bug),
    olmo_002 重跑。等 cuda:0 释放。
  status: DONE
  conclusion: success
  metrics:
    four_class_acc_rf: 0.788
    four_class_acc_ci:
    - 0.776
    - 0.8
    four_class_acc_lr: 0.751
    auc_0v1: 0.9834
    auc_0v2: 0.9949
    auc_0v3: 0.9989
    auc_1v2: 0.8673
    auc_1v3: 0.9806
    auc_2v3: 0.8124
    three_class_acc: 0.744
    three_class_acc_ci:
    - 0.728
    - 0.76
    three_class_mae: 0.27
    three_class_auc_1v2: 0.8664
    three_class_auc_1v3: 0.9852
    three_class_auc_2v3: 0.8274
    three_class_recall:
      d1: 0.864
      d2: 0.607
      d3: 0.761
    three_class_precision:
      d1: 0.863
      d2: 0.646
      d3: 0.718
    four_class_per_class:
      d0:
        precision: 0.95
        recall: 0.99
        f1: 0.97
      d1:
        precision: 0.85
        recall: 0.82
        f1: 0.83
      d2:
        precision: 0.63
        recall: 0.59
        f1: 0.61
      d3:
        precision: 0.71
        recall: 0.76
        f1: 0.73
    finetune_losses:
      depth_0: 2.269
      depth_1: 1.65
      depth_2: 1.226
    top_features:
    - p90_ppl (0.18)
    - var_surprisal (0.16)
    - p75_ppl (0.11)
    - mean_surprisal (0.08)
    - type_token_ratio (0.06)
    code_contamination:
      d0: 0.005
      d1: 0.027
      d2: 0.007
      d3: 0.008
    feature_dim: 19
    truncation_length: 507
- id: plan_003
  claim: 1
  description: GPT-2 XL 1.5B recursive chain (4 depths × 3 strategies)
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: cross_model_gpt2xl_001
  notes: GPT-2 most studied in collapse literature. WebText training data. c_attn/c_proj
    LoRA.
  status: DONE
  conclusion: success
  metrics:
    four_class_acc_rf: 0.833
    four_class_acc_ci:
    - 0.823
    - 0.845
    four_class_acc_lr: 0.813
    auc_0v1: 0.9941
    auc_0v2: 0.9965
    auc_0v3: 0.9988
    auc_1v2: 0.9131
    auc_1v3: 0.9857
    auc_2v3: 0.8829
    three_class_acc: 0.793
    three_class_acc_ci:
    - 0.778
    - 0.806
    three_class_auc_1v2: 0.9109
    three_class_auc_1v3: 0.989
    three_class_auc_2v3: 0.8885
    finetune_losses:
      depth_0: 2.55
      depth_1: 1.715
      depth_2: 1.342
    top_features:
    - p90_ppl (0.208)
    - var_surprisal (0.208)
    - p75_ppl (0.103)
    - mean_surprisal (0.082)
    - mean_ppl (0.065)
    code_contamination:
      d0: 0.005
      d1: 0.005
      d2: 0.013
      d3: 0.007
- id: plan_002b
  claim: 1
  description: OLMo-1B — temperature τ=0.9 chain (4 depths)
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: olmo_temp09_001
  notes: 3×3 matrix cell. OLMo temp09. olmo_temp09_001 正在运行 (PID 205384, cuda:1)。之前被
    cron 子进程误报为 failed，已修正。olmo_temp09_002 已取消。
  status: DONE
  conclusion: success
  metrics:
    four_class:
      rf_accuracy: 0.8203
      d1v2_auc: 0.901
    three_class_filtered:
      rf_accuracy: 0.7757
    finetune_losses:
      depth_0: 2.27
      depth_1: 1.63
      depth_2: 1.18
    code_contamination_narrow_max: 0.007
    top_features:
    - p90_ppl (0.199)
    - var_surprisal (0.174)
    - p75_ppl (0.126)
- id: plan_002c
  claim: 1
  description: OLMo-1B — top-k k=50 chain (4 depths)
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: olmo_topk50_001
  notes: 3×3 matrix cell. OLMo topk50. 等 cuda:1 释放后提交。
  status: DONE
  conclusion: success
  metrics:
    four_class:
      lr_accuracy: 0.757
      lr_accuracy_ci:
      - 0.7425
      - 0.7702
      rf_accuracy: 0.742
      rf_accuracy_ci:
      - 0.7282
      - 0.7555
    pairwise_auc:
      lr:
        d0v1: 0.9969
        d0v2: 0.9995
        d0v3: 0.9998
        d1v2: 0.8293
        d1v3: 0.9592
        d2v3: 0.7497
      rf:
        d0v1: 0.993
        d0v2: 0.9983
        d0v3: 0.9991
        d1v2: 0.8305
        d1v3: 0.9591
        d2v3: 0.7357
    three_class:
      lr_accuracy: 0.6567
      lr_accuracy_ci:
      - 0.6403
      - 0.6733
      rf_accuracy: 0.6517
      rf_accuracy_ci:
      - 0.635
      - 0.6687
    three_class_filtered:
      lr_accuracy: 0.6703
      lr_accuracy_ci:
      - 0.653
      - 0.6882
      rf_accuracy: 0.6699
      rf_accuracy_ci:
      - 0.6537
      - 0.6875
    three_class_filtered_auc:
      lr:
        d1v2: 0.7903
        d1v3: 0.97
        d2v3: 0.7501
      rf:
        d1v2: 0.8071
        d1v3: 0.9645
        d2v3: 0.7364
    feature_importance_top5:
    - p90_ppl
    - var_surprisal
    - p75_ppl
    - mean_surprisal
    - p25_ppl
    finetune_loss:
      depth_1: 1.946
      depth_2: 1.726
    code_contamination:
      narrow_pct:
        depth_0: 0.4
        depth_1: 0.8
        depth_2: 0.3
        depth_3: 0.4
      broad_pct:
        depth_0: 0.5
        depth_1: 2.5
        depth_2: 0.8
        depth_3: 0.7
- id: plan_003b
  claim: 1
  description: GPT-2 XL — temperature τ=0.9 chain (4 depths)
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: gpt2xl_temp09_001
  notes: 3×3 matrix cell. Running on cuda:1.
  status: DONE
  conclusion: success
  metrics:
    data:
      samples_per_depth: 5000
      total_samples: 20000
      depths: 4
    finetune_losses:
      depth_1: 2.5498
      depth_2: 1.6972
      depth_3: 1.2922
    code_contamination:
      depth_0:
        broad: 25
        narrow: 20
        broad_pct: 0.5
        narrow_pct: 0.4
      depth_1:
        broad: 25
        narrow: 40
        broad_pct: 0.5
        narrow_pct: 0.8
      depth_2:
        broad: 34
        narrow: 80
        broad_pct: 0.7
        narrow_pct: 1.6
      depth_3:
        broad: 25
        narrow: 76
        broad_pct: 0.5
        narrow_pct: 1.5
    four_class:
      rf_accuracy: 0.8542
      rf_accuracy_ci:
      - 0.843
      - 0.8653
      lr_accuracy: 0.8155
      lr_accuracy_ci:
      - 0.8025
      - 0.8273
      rf_auc:
        d0v1: 0.9963
        d0v2: 0.9992
        d0v3: 1
        d1v2: 0.9367
        d1v3: 0.9947
        d2v3: 0.8815
      lr_auc:
        d0v1: 0.984
        d0v2: 0.9998
        d0v3: 1
        d1v2: 0.8903
        d1v3: 0.9824
        d2v3: 0.8183
      top_features:
      - p90_ppl
      - mean_surprisal
      - p75_ppl
      - var_surprisal
    three_class:
      rf_accuracy: 0.82
      rf_accuracy_ci:
      - 0.806
      - 0.834
      lr_accuracy: 0.7773
      lr_accuracy_ci:
      - 0.7627
      - 0.792
      rf_auc:
        d1v2: 0.9418
        d1v3: 0.9967
        d2v3: 0.8849
    three_class_filtered:
      rf_accuracy: 0.815
      rf_accuracy_ci:
      - 0.7999
      - 0.8298
      lr_accuracy: 0.7869
      lr_accuracy_ci:
      - 0.7711
      - 0.8016
      rf_auc:
        d1v2: 0.937
        d1v3: 0.9944
        d2v3: 0.8891
- id: plan_003c
  claim: 1
  description: GPT-2 XL — top-k k=50 chain (4 depths)
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: gpt2xl_topk50_001
  notes: 3×3 matrix cell. GPT-2 XL topk50.
  status: DONE
  conclusion: success
  metrics:
    four_class:
      accuracy: 0.766
      depth1_vs_depth2_auc: 0.8259
      pass: true
    three_class:
      accuracy: 0.695
      depth1_vs_depth2_auc: 0.8392
      pass: true
    three_class_filtered:
      accuracy: 0.684
      depth1_vs_depth2_auc: 0.8314
      pass: true
- id: plan_004
  claim: 1
  description: 'DCOL training: RoBERTa-large with learnable margins contrastive loss
    (v6, non-blocking)'
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_001b
  - plan_002
  - plan_003
  notes: v1-v5 DeBERTa 全部失败 (D011)。v6 换 RoBERTa-large 非阻塞尝试。成功→bonus section，失败→negative
    analysis。不阻塞论文进度。
  registry_id: dcol_roberta_v6_001
  status: DONE
  conclusion: negative
  metrics:
    test_acc: 0.6448
    test_mae: 0.4052
    best_val_acc: 0.6436
    best_epoch: 1
    epochs_run: 4
    early_stopping: true
    train_acc_final: 0.75
    rf_baseline: 0.782
    delta_vs_baseline: -0.137
    overfitting: severe (train 75% vs val 64.4% at best epoch)
    stability: resolved (no NaN, no collapse, collapse guard passed at step 500)
- id: plan_005
  claim: 1
  description: 'Leave-one-model-out generalization (RF): train on 2 families, test
    on 3rd'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan_001b
  - plan_002
  - plan_003
  registry_id: cross_model_loo_v1
  notes: '3 rotations with RF classifier. Research-phase gate: cross-model acc ≥ 45%.
    Plan A: 不依赖 DCOL。均值 66.4%，gate 通过。'
  status: DONE
  conclusion: success
  metrics:
    mean_acc: 0.664
    mean_3class_acc: 0.5544
    holdout_pythia:
      acc: 0.6242
      ci95:
      - 0.6205
      - 0.6282
      3class_acc: 0.499
      3class_ci95:
      - 0.4944
      - 0.5034
      d1v2_auc: 0.5617
      d1v3_auc: 0.8547
      d2v3_auc: 0.6534
      d0v1_auc: 0.9921
      d0v2_auc: 0.9999
      d0v3_auc: 0.9998
      per_class:
        d0:
          P: 0.9889
          R: 1
          F1: 0.9944
        d1:
          P: 0.6655
          R: 0.493
          F1: 0.5664
        d2:
          P: 0.3699
          R: 0.2677
          F1: 0.3106
        d3:
          P: 0.483
          R: 0.7363
          F1: 0.5834
    holdout_olmo:
      acc: 0.6921
      ci95:
      - 0.6884
      - 0.696
      3class_acc: 0.592
      3class_ci95:
      - 0.5873
      - 0.5965
      d1v2_auc: 0.7687
      d1v3_auc: 0.9277
      d2v3_auc: 0.6862
      per_class:
        d0:
          P: 0.9783
          R: 0.9925
          F1: 0.9854
        d1:
          P: 0.7111
          R: 0.7549
          F1: 0.7324
        d2:
          P: 0.4616
          R: 0.4327
          F1: 0.4467
        d3:
          P: 0.5964
          R: 0.5883
          F1: 0.5923
    holdout_gpt2xl:
      acc: 0.6756
      ci95:
      - 0.6717
      - 0.6795
      3class_acc: 0.5723
      3class_ci95:
      - 0.5679
      - 0.5767
      d1v2_auc: 0.8157
      d1v3_auc: 0.9149
      d2v3_auc: 0.6639
      d0v1_auc: 0.9927
      d0v2_auc: 0.9919
      d0v3_auc: 0.9876
      per_class:
        d0:
          P: 0.9484
          R: 0.9853
          F1: 0.9665
        d1:
          P: 0.7093
          R: 0.7465
          F1: 0.7274
        d2:
          P: 0.4521
          R: 0.5255
          F1: 0.486
        d3:
          P: 0.5963
          R: 0.445
          F1: 0.5097
    mean_per_class_recall:
      d0: 0.9926
      d1: 0.6648
      d2: 0.4086
      d3: 0.5899
    lowest_recall_class: d2
    lowest_recall_value: 0.4086
    detailed_artifact: cross_model_loo_detailed.json
- id: plan_006
  claim: 2
  description: 'Depth Degradation Atlas: monotonicity scores, EDD, cross-model/strategy
    heatmaps'
  priority: P0
  gpu_budget_hours: 3
  deps:
  - plan_001b
  - plan_002
  - plan_003
  registry_id: atlas_v1_analysis
  notes: 'v1 完成: monotonicity ρ=-0.82~-0.89, EDD=3 (未饱和), cross-model Jaccard=0.667,
    rank corr ρ>0.85. 4 JSON in artifacts/atlas/. 待完成: 正式出图(AUC decay/feature trajectory/heatmap/confusion
    matrix) + 纳入 3×3 剩余 cells 数据.'
  status: DONE
  conclusion: success
  metrics:
    monotonicity_rho_range:
    - -0.89
    - -0.82
    edd: 3
    edd_saturated: false
    cross_model_jaccard: 0.667
    cross_model_rank_corr: 0.85
    artifacts:
    - monotonicity_scores.json
    - cross_model_comparison.json
    - edd_analysis.json
    - feature_trajectory.json
- id: plan_006b
  claim: 1
  description: '3-class experiment (d1/d2/d3 only): isolate pure depth gradient from
    real-vs-synthetic signal'
  priority: P0
  gpu_budget_hours: 0.5
  deps:
  - plan_001a
  status: DONE
  registry_id: mvp_pipeline_pythia_002
  notes: Reviewer-requested. 3-class acc=70.8% [0.692,0.725], d1v2 AUC=0.854, d2v3=0.793.
    Results in mvp_pipeline_pythia_002 metrics.
  conclusion: success
  metrics: *id001
- id: plan_007
  claim: 1
  description: 'Leave-one-strategy-out robustness (RF): train on 2 strategies, test
    on 3rd'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan_001b
  - plan_002
  - plan_003
  registry_id: cross_strategy_loo_001
  notes: '3 rotations per model with RF. Plan A: 不依赖 DCOL。均值 59.1%，9/9 > chance。temp09
    d1v2 反转已解释 (Covariate Shift)。'
  status: DONE
  conclusion: success
  metrics:
    mean_4class_acc: 0.5908
    pythia_holdout_nucleus:
      acc: 0.6935
      d1v2_auc: 0.6903
      d2v3_auc: 0.7626
    pythia_holdout_temp09:
      acc: 0.6281
      d1v2_auc: 0.576
      d2v3_auc: 0.724
    pythia_holdout_topk50:
      acc: 0.5151
      d1v2_auc: 0.6393
      d2v3_auc: 0.5801
    gpt2xl_holdout_nucleus:
      acc: 0.5993
      d1v2_auc: 0.7826
      d2v3_auc: 0.4985
    gpt2xl_holdout_temp09:
      acc: 0.5609
      d1v2_auc: 0.1288
      d2v3_auc: 0.6366
    gpt2xl_holdout_topk50:
      acc: 0.5364
      d1v2_auc: 0.8308
      d2v3_auc: 0.7222
    olmo_holdout_nucleus:
      acc: 0.6538
      d1v2_auc: 0.7931
      d2v3_auc: 0.6076
    olmo_holdout_temp09:
      acc: 0.5816
      d1v2_auc: 0.2529
      d2v3_auc: 0.7015
    olmo_holdout_topk50:
      acc: 0.5488
      d1v2_auc: 0.8549
      d2v3_auc: 0.7107
    finding_temp09_d1v2_inversion: 'd1v2 AUC inverts when holding out temp09 (GPT-2
      XL: 0.13, OLMo: 0.25) — temp09 d1→d2 features differ fundamentally from nucleus/topk50'
- id: plan_008
  claim: 1
  description: 'DeBERTa end-to-end classifier: direct text→depth'
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_001b
  - plan_002
  - plan_003
  registry_id: n2_deberta_finetune_001
  status: DONE
  conclusion: success
  metrics:
    accuracy_mean: 0.5831
    accuracy_std: 0.0467
    per_class_f1:
      d0: 0.947
      d1: 0.378
      d2: 0.247
      d3: 0.656
    pairwise_auc:
      d0v1: 0.981
      d1v2: 0.733
      d2v3: 0.755
    vs_rf_baseline: 58.3% vs 78.2% (-19.9pp)
    elapsed_seconds: 3727
- id: plan_009
  claim: 1
  description: 'Baseline battery: DivEye, perplexity regression, CORAL, CE, zero-shot
    LLM'
  priority: P1
  gpu_budget_hours: 8
  registry_id: baseline_battery_001
  deps:
  - plan_001b
  - plan_002
  - plan_003
  status: DONE
  conclusion: success
  metrics:
    ppl_reg_single_4class_acc: 0.251
    ppl_reg_multi_4class_acc: 0.622
    ce_mlp_4class_acc: 0.749
    coral_4class_acc: 0.7807
    coral_3class_acc: 0.7089
    coral_mae: 0.2273
    coral_d1v2_auc: 0.8179
    diveye_4class_acc: 0.7817
    diveye_3class_acc: 0.7098
    diveye_d1v2_auc: 0.8654
    rf_4class_acc: 0.781
    lr_4class_acc: 0.75
    note: CE-MLP 74.9% may be undertrained (5 epochs); CORAL updated to 100 epochs.
      All results from Pythia nucleus baseline features.
- id: plan_010
  claim: 1
  description: DCOL component ablation
  priority: P2
  gpu_budget_hours: 8
  deps:
  - plan_004
  status: planned
  notes: DCOL v6 失败 (D018)，前置条件 plan_004 未满足，取消。
- id: plan_011
  claim: 2
  description: Depth extension to 5 generations + EDD saturation analysis
  priority: P0
  gpu_budget_hours: 4
  deps:
  - plan_001a
  registry_id: depth_extension_binary_pairwise_002
  notes: Pythia-1.4B nucleus EDD=4 (binary d3v4=0.784>0.75, d4v5=0.683<0.75)。6-class
    pairwise AUC 因决策边界稀释不可用，必须用 binary pairwise classifier。
  status: DONE
  conclusion: success
  metrics:
    d1v2_auc: 0.925
    d1v2_ci95:
    - 0.9138
    - 0.9354
    d2v3_auc: 0.8225
    d2v3_ci95:
    - 0.8052
    - 0.8402
    d3v4_auc: 0.7837
    d3v4_ci95:
    - 0.7648
    - 0.8024
    d4v5_auc: 0.6832
    d4v5_ci95:
    - 0.6611
    - 0.7045
    edd_determination: '4'
- id: plan_011b
  claim: 2
  description: GPT-2 XL depth extension d4/d5 + EDD cross-model verification
  priority: P1
  gpu_budget_hours: 4
  deps:
  - plan_003
  - plan_011
  registry_id: depth_extension_gpt2xl_d4d5_001
  notes: GPT-2 XL 是 3×3 矩阵信号最强模型 (85.4%)。验证 EDD 跨模型一致性，直接增强 Claim 2。已 RUNNING on cuda:0。
  status: DONE
  conclusion: success
  metrics:
    binary_pairwise:
      d1v2_auc: 0.966
      d2v3_auc: 0.919
      d3v4_auc: 0.75
      d4v5_auc: 0.681
    six_class_rf_accuracy: 0.679
    edd_at_075: 4
    edd_note: d3v4=0.750>=0.75 PASS, d4v5=0.681<0.75 FAIL → EDD=4
- id: plan_011c
  claim: 2
  description: OLMo-1B depth extension d4/d5 + EDD cross-model verification
  priority: P1
  gpu_budget_hours: 4
  deps:
  - plan_002
  - plan_011
  notes: 第 3 个模型 EDD 验证。代码已就绪 (run_depth_extension_olmo.sh)，含 binary pairwise eval。Reviewer
    PASS。排 granularity ablation 之后上 cuda:1。
  registry_id: depth_extension_olmo_d4d5_002
  status: DONE
  conclusion: success
  metrics:
    binary_pairwise:
      d1v2_auc: 0.968
      d2v3_auc: 0.843
      d3v4_auc: 0.765
      d4v5_auc: 0.684
    six_class_rf_accuracy: 0.667
    edd_at_075: 4
    edd_note: d3v4=0.765>=0.75 PASS, d4v5=0.684<0.75 FAIL → EDD=4
- id: plan_012
  claim: 1
  description: 'Granularity ablation (RF): binary / 3-class / 4-class / 6-class'
  registry_id: granularity_ablation_rf_001
  priority: P1
  gpu_budget_hours: 1
  deps:
  - plan_001b
  - plan_002
  - plan_003
  notes: 'Plan A: 用 RF 做，不依赖 DCOL。与 plan_011 depth extension 联动（6-class 需要 5+ depths
    数据）。'
  status: DONE
  conclusion: success
  metrics:
    summary:
      binary_acc_mean: 0.995
      binary_acc_std: 0.004
      3class_acc_mean: 0.721
      3class_acc_std: 0.067
      4class_acc_mean: 0.783
      4class_acc_std: 0.048
      6class_acc: 0.629
      note: '3-class excludes d0 (most separable class), so 3class < 4class is by
        design. True granularity trend (with d0): binary 99.5% > 4-class 78.3% > 6-class
        62.9% — monotonic decrease confirmed.'
    per_cell:
      pythia_nucleus095:
        binary:
          acc: 0.998
          ci95:
          - 0.9965
          - 0.9992
          auc:
            d0v1: 1
        3class:
          acc: 0.7117
          ci95:
          - 0.6947
          - 0.7283
          auc:
            d1v2: 0.861
            d2v3: 0.796
        4class:
          acc: 0.7812
          ci95:
          - 0.7677
          - 0.7935
          auc:
            d0v1: 0.998
            d1v2: 0.868
            d2v3: 0.804
        6class:
          acc: 0.6292
          ci95:
          - 0.6175
          - 0.6412
          auc:
            d0v1: 0.997
            d1v2: 0.83
            d2v3: 0.689
            d3v4: 0.692
            d4v5: 0.691
      pythia_temp09:
        binary:
          acc: 0.997
          ci95:
          - 0.9952
          - 0.9985
          auc:
            d0v1: 1
        3class:
          acc: 0.7063
          ci95:
          - 0.6907
          - 0.723
          auc:
            d1v2: 0.838
            d2v3: 0.806
        4class:
          acc: 0.7605
          ci95:
          - 0.7475
          - 0.7738
          auc:
            d0v1: 0.997
            d1v2: 0.835
            d2v3: 0.796
      pythia_topk50:
        binary:
          acc: 0.9945
          ci95:
          - 0.992
          - 0.9965
          auc:
            d0v1: 1
        3class:
          acc: 0.5883
          ci95:
          - 0.5717
          - 0.6073
          auc:
            d1v2: 0.749
            d2v3: 0.705
        4class:
          acc: 0.6943
          ci95:
          - 0.6805
          - 0.708
          auc:
            d0v1: 0.994
            d1v2: 0.761
            d2v3: 0.695
      gpt2xl_nucleus095:
        binary:
          acc: 0.9912
          ci95:
          - 0.9882
          - 0.9938
          auc:
            d0v1: 0.999
        3class:
          acc: 0.79
          ci95:
          - 0.775
          - 0.8047
          auc:
            d1v2: 0.913
            d2v3: 0.891
        4class:
          acc: 0.8393
          ci95:
          - 0.8283
          - 0.8502
          auc:
            d0v1: 0.995
            d1v2: 0.916
            d2v3: 0.885
      gpt2xl_temp09:
        binary:
          acc: 0.9978
          ci95:
          - 0.9962
          - 0.999
          auc:
            d0v1: 1
        3class:
          acc: 0.826
          ci95:
          - 0.8117
          - 0.8397
          auc:
            d1v2: 0.944
            d2v3: 0.887
        4class:
          acc: 0.8552
          ci95:
          - 0.844
          - 0.866
          auc:
            d0v1: 0.997
            d1v2: 0.939
            d2v3: 0.886
      gpt2xl_topk50:
        binary:
          acc: 0.9952
          ci95:
          - 0.993
          - 0.9972
          auc:
            d0v1: 1
        3class:
          acc: 0.695
          ci95:
          - 0.6777
          - 0.7113
          auc:
            d1v2: 0.844
            d2v3: 0.766
        4class:
          acc: 0.757
          ci95:
          - 0.743
          - 0.7702
          auc:
            d0v1: 0.993
            d1v2: 0.824
            d2v3: 0.762
      olmo_nucleus095:
        binary:
          acc: 0.9868
          ci95:
          - 0.9832
          - 0.99
          auc:
            d0v1: 0.999
        3class:
          acc: 0.7503
          ci95:
          - 0.7353
          - 0.7657
          auc:
            d1v2: 0.873
            d2v3: 0.831
        4class:
          acc: 0.7897
          ci95:
          - 0.7772
          - 0.8027
          auc:
            d0v1: 0.985
            d1v2: 0.87
            d2v3: 0.816
      olmo_temp09:
        binary:
          acc: 0.9982
          ci95:
          - 0.997
          - 0.9992
          auc:
            d0v1: 1
        3class:
          acc: 0.7633
          ci95:
          - 0.7477
          - 0.7797
          auc:
            d1v2: 0.894
            d2v3: 0.838
        4class:
          acc: 0.8263
          ci95:
          - 0.8147
          - 0.8385
          auc:
            d0v1: 0.996
            d1v2: 0.903
            d2v3: 0.828
      olmo_topk50:
        binary:
          acc: 0.996
          ci95:
          - 0.994
          - 0.9978
          auc:
            d0v1: 1
        3class:
          acc: 0.661
          ci95:
          - 0.644
          - 0.6773
          auc:
            d1v2: 0.812
            d2v3: 0.739
        4class:
          acc: 0.7435
          ci95:
          - 0.73
          - 0.758
          auc:
            d0v1: 0.995
            d1v2: 0.831
            d2v3: 0.738
    boundary_dilution:
      d2v3_auc_by_granularity_pythia_nuc:
        3class: 0.796
        4class: 0.804
        6class: 0.689
      d1v2_auc_by_granularity_pythia_nuc:
        3class: 0.861
        4class: 0.868
        6class: 0.83
      note: d2v3 AUC drops 14% from 4-class to 6-class (0.804→0.689), confirming decision
        boundary dilution at higher granularity
    decoding_strategy_ranking:
      4class_acc:
        temp09: 0.814
        nucleus095: 0.803
        topk50: 0.732
      note: topk50 consistently worst across all 3 models; temp09 slightly outperforms
        nucleus095
- id: plan_013
  claim: 3
  description: Downstream curation proof-of-concept
  priority: P2
  gpu_budget_hours: 15
  deps:
  - plan_001b
  - plan_002
  - plan_003
  registry_id: downstream_curation_poc_001
  notes: 'DONE. RF curation 不优于 unfiltered (negative for original hypothesis)，但显著优于
    random (p<0.002 all tiers)。Data efficiency story: 44% data ≈ full PPL。Supplement:
    random_soft_control_001 (success, rf_soft vs random_soft p=5.6e-5)。已写入 Discussion
    + Appendix。'
  status: DONE
  conclusion: negative
  metrics:
    unfiltered:
      ppl_mean: 15.776
      ppl_std: 0.066
      n_samples: 10000
    rf_strict:
      ppl_mean: 15.81
      ppl_std: 0.061
      n_samples: 2496
      delta: '-0.034'
      p: 0.607
      d: -0.528
    rf_moderate:
      ppl_mean: 15.756
      ppl_std: 0.056
      n_samples: 4940
      delta: '+0.021'
      p: 0.492
      d: 0.334
    rf_soft:
      ppl_mean: 15.733
      ppl_std: 0.038
      n_samples: 4422
      delta: '+0.043'
      p: 0.407
      d: 0.792
    oracle_strict:
      ppl_mean: 15.879
      ppl_std: 0.128
      n_samples: 2500
      delta: '-0.103'
      p: 0.216
      d: -1.004
    oracle_moderate:
      ppl_mean: 15.809
      ppl_std: 0.103
      n_samples: 5000
      delta: '-0.033'
      p: 0.485
      d: -0.384
    random_strict:
      ppl_mean: 16.239
      ppl_std: 0.165
      n_samples: 2496
      delta: '-0.463'
      p: 0.013
      d: -3.671
      sig: true
    random_moderate:
      ppl_mean: 15.998
      ppl_std: 0.09
      n_samples: 5000
      delta: '-0.222'
      p: 0.028
      d: -2.809
      sig: true
    cross_condition:
      rf_strict_vs_random_strict:
        delta: 0.429
        t: -7.052
        p: 0.002
        sig: true
      rf_moderate_vs_random_moderate:
        delta: 0.242
        t: -3.77
        p: 0.02
        sig: true
      rf_soft_vs_unfiltered:
        delta: 0.043
        t: 0.927
        p: 0.407
        sig: false
      random_strict_vs_unfiltered:
        delta: -0.463
        t: 4.219
        p: 0.014
        sig: true
- id: plan_014
  claim: 1
  description: 13B clean FP16 scale validation (Qwen2.5-14B, nucleus, d0-d3)
  priority: P0
  gpu_budget_hours: 18
  deps:
  - plan_001b
  - plan_002
  - plan_003
  notes: 替代原 7B QLoRA（结果矛盾）。Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。完整
    d0-d3 nucleus 递归链 + 19 特征提取 + RF/LR 分类。验证 depth signal 在主流模型规模上是否持续。cuda:0。
  status: planned
- id: plan_015
  claim: 2
  description: Wild-data calibration on RedPajama/Dolma
  priority: P2
  gpu_budget_hours: 5
  deps:
  - plan_001b
  - plan_002
  - plan_003
  notes: 延后到 AAAI 窗口。当前优先级让位于 plan_014/016/018。
  status: planned
- id: plan_016
  claim: 1
  description: Prompted generation ecological validity (GPT-2 XL, topic-seeded d0-d3)
  priority: P0
  gpu_budget_hours: 6
  deps:
  - plan_003
  notes: 验证 depth signal 是否为 BOS-seeded 无条件生成的 artifact。用 topic prompt 前缀（"The following
    article discusses..."等）生成 d0，LoRA fine-tune 后生成 d1-d3，提取 19 特征 + RF 分类。选 GPT-2
    XL 因为它信号最强，如果 prompted 模式下信号消失则说明生成方式是关键因素。cuda:1。
  status: planned
- id: plan_017
  claim: 3
  description: Cross-strategy two-stage pipeline (strategy classifier + conditioned
    depth)
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan_001b
  - plan_002
  - plan_003
  - plan_007
  notes: 两阶段方案解决 59.1% 跨策略准确率问题。(a) 策略识别分类器：19 特征 → 3-class (nucleus/temp/topk)，预计
    >90%。(b) 策略条件深度分类器：识别策略后用策略专属 RF 估深度。将论文弱点转化为实际贡献。主要是 CPU 任务，不占 GPU。
  status: planned


## registry (completed experiments)

- exp_id: mvp_pipeline_001
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_002
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_003
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_004
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_base_002
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_base_003
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_pythia_001
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_qwen_base_004
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_pythia_002
  name: ''
  status: DONE
  conclusion: success
  metrics:
    full_4class_acc: 0.782
    full_4class_acc_ci:
    - 0.769
    - 0.794
    full_4class_acc_stratified: 0.781
    full_mae: 0.2367
    full_auc_0v1: 0.9975
    full_auc_1v2: 0.8607
    full_auc_2v3: 0.8005
    filtered_4class_acc: 0.816
    filtered_4class_acc_ci:
    - 0.803
    - 0.829
    filtered_mae: 0.1995
    filtered_auc_0v1: 0.9977
    filtered_auc_1v2: 0.8782
    filtered_auc_2v3: 0.8323
    filtered_sample_count: 16993
    three_class_acc: 0.708
    three_class_acc_ci:
    - 0.692
    - 0.725
    three_class_mae: 0.3203
    three_class_auc_1v2: 0.854
    three_class_auc_1v3: 0.9569
    three_class_auc_2v3: 0.7931
    three_class_recall_d1: 0.79
    three_class_recall_d2: 0.607
    three_class_recall_d3: 0.728
    three_class_precision_d1: 0.852
    three_class_precision_d2: 0.605
    three_class_precision_d3: 0.68
    three_class_f1_d1: 0.82
    three_class_f1_d2: 0.606
    three_class_f1_d3: 0.703
    three_class_lr_acc: 0.671
    filtered_three_class_acc: 0.747
    filtered_three_class_acc_ci:
    - 0.727
    - 0.764
    filtered_three_class_mae: 0.2759
    filtered_three_class_recall_d1: 0.862
    filtered_three_class_recall_d2: 0.635
    filtered_three_class_recall_d3: 0.735
    filtered_three_class_precision_d1: 0.867
    filtered_three_class_precision_d2: 0.659
    filtered_three_class_precision_d3: 0.704
    filtered_three_class_f1_d1: 0.864
    filtered_three_class_f1_d2: 0.647
    filtered_three_class_f1_d3: 0.719
    filtered_three_class_auc_1v2: 0.8926
    filtered_three_class_auc_1v3: 0.9769
    filtered_three_class_auc_2v3: 0.8272
    filtered_three_class_sample_count: 12012
    best_model: RandomForest
    top_features:
    - var_surprisal
    - p90_ppl
    - mean_ppl
    - mean_surprisal
    - p75_ppl
    truncation_length: 498
    feature_dim: 19
- exp_id: cross_model_olmo_001
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    status: PIPELINE_CRASHED
    completed_steps:
    - depth0_lora_finetune
    failed_at: shell_script_line_52_unmatched_quote
    depth0_final_loss: 2.2686
    depth0_train_runtime_s: 283.2
    depth0_train_steps: 939
    depth0_trainable_params: 3145728
    depth0_total_params: 1179910144
    classification_results: null
    note: Script crashed after depth-0 finetune. No depth-1/2/3 generation, no feature
      extraction, no classification performed.
- exp_id: cross_model_gpt2xl_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    four_class_acc_rf: 0.833
    four_class_acc_ci:
    - 0.823
    - 0.845
    four_class_acc_lr: 0.813
    auc_0v1: 0.9941
    auc_0v2: 0.9965
    auc_0v3: 0.9988
    auc_1v2: 0.9131
    auc_1v3: 0.9857
    auc_2v3: 0.8829
    three_class_acc: 0.793
    three_class_acc_ci:
    - 0.778
    - 0.806
    three_class_auc_1v2: 0.9109
    three_class_auc_1v3: 0.989
    three_class_auc_2v3: 0.8885
    finetune_losses:
      depth_0: 2.55
      depth_1: 1.715
      depth_2: 1.342
    top_features:
    - p90_ppl (0.208)
    - var_surprisal (0.208)
    - p75_ppl (0.103)
    - mean_surprisal (0.082)
    - mean_ppl (0.065)
    code_contamination:
      d0: 0.005
      d1: 0.005
      d2: 0.013
      d3: 0.007
- exp_id: pythia_temp09_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    four_class:
      rf_accuracy: 0.7625
      rf_accuracy_ci:
      - 0.749
      - 0.7753
      lr_accuracy: 0.7405
      lr_accuracy_ci:
      - 0.7265
      - 0.7545
      pairwise_auc:
        0v1: 0.9968
        0v2: 0.9993
        0v3: 0.9991
        1v2: 0.8327
        1v3: 0.959
        2v3: 0.7928
      top_features:
      - var_surprisal (0.1776)
      - p90_ppl (0.1501)
      - mean_ppl (0.1140)
      - mean_surprisal (0.0889)
      - p75_ppl (0.0687)
      feature_dim: 19
      truncation_length: 498
    three_class_full:
      accuracy: 0.6983
      accuracy_ci:
      - 0.682
      - 0.715
      mae: 0.3357
      recall:
        d1: 0.802
        d2: 0.554
        d3: 0.739
      precision:
        d1: 0.792
        d2: 0.608
        d3: 0.686
      f1:
        d1: 0.797
        d2: 0.58
        d3: 0.712
      pairwise_auc:
        d1v2: 0.8354
        d1v3: 0.9631
        d2v3: 0.8043
    three_class_filtered:
      accuracy: 0.7252
      accuracy_ci:
      - 0.7064
      - 0.7427
      mae: 0.2953
      recall:
        d1: 0.842
        d2: 0.596
        d3: 0.735
      precision:
        d1: 0.821
        d2: 0.628
        d3: 0.715
      f1:
        d1: 0.831
        d2: 0.611
        d3: 0.725
      pairwise_auc:
        d1v2: 0.8656
        d1v3: 0.9772
        d2v3: 0.8295
      n_samples: 11445
      n_removed: 3555
    finetune_losses:
      depth_0: 2.222
      depth_1: 1.37
      depth_2: 1.006
    code_contamination:
      d0: 0.004
      d1: 0.077
      d2: 0.116
      d3: 0.136
- exp_id: pythia_topk50_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rf_4class_acc: 0.696
    rf_4class_acc_ci:
    - 0.6825
    - 0.7107
    lr_4class_acc: 0.682
    rf_3class_acc: 0.592
    rf_3class_acc_ci:
    - 0.575
    - 0.6107
    rf_3class_filtered_acc: 0.6133
    rf_3class_filtered_acc_ci:
    - 0.593
    - 0.6312
    pairwise_auc_rf:
      d0v1: 0.9927
      d0v2: 0.9983
      d0v3: 0.9978
      d1v2: 0.7518
      d1v3: 0.9176
      d2v3: 0.6918
    pairwise_auc_3class_filtered_rf:
      d1v2: 0.768
      d1v3: 0.9323
      d2v3: 0.7013
    feature_importance_top5:
    - var_surprisal
    - p90_ppl
    - mean_ppl
    - mean_surprisal
    - p75_ppl
    finetune_loss:
      depth_0: 2.2406
      depth_1: 1.6704
      depth_2: 1.4374
    code_contamination_narrow:
      depth_0: 0.004
      depth_1: 0.077
      depth_2: 0.123
      depth_3: 0.131
- exp_id: cross_model_olmo_002
  name: ''
  status: DONE
  conclusion: success
  metrics:
    four_class_acc_rf: 0.788
    four_class_acc_ci:
    - 0.776
    - 0.8
    four_class_acc_lr: 0.751
    auc_0v1: 0.9834
    auc_0v2: 0.9949
    auc_0v3: 0.9989
    auc_1v2: 0.8673
    auc_1v3: 0.9806
    auc_2v3: 0.8124
    three_class_acc: 0.744
    three_class_acc_ci:
    - 0.728
    - 0.76
    three_class_mae: 0.27
    three_class_auc_1v2: 0.8664
    three_class_auc_1v3: 0.9852
    three_class_auc_2v3: 0.8274
    three_class_recall:
      d1: 0.864
      d2: 0.607
      d3: 0.761
    three_class_precision:
      d1: 0.863
      d2: 0.646
      d3: 0.718
    four_class_per_class:
      d0:
        precision: 0.95
        recall: 0.99
        f1: 0.97
      d1:
        precision: 0.85
        recall: 0.82
        f1: 0.83
      d2:
        precision: 0.63
        recall: 0.59
        f1: 0.61
      d3:
        precision: 0.71
        recall: 0.76
        f1: 0.73
    finetune_losses:
      depth_0: 2.269
      depth_1: 1.65
      depth_2: 1.226
    top_features:
    - p90_ppl (0.18)
    - var_surprisal (0.16)
    - p75_ppl (0.11)
    - mean_surprisal (0.08)
    - type_token_ratio (0.06)
    code_contamination:
      d0: 0.005
      d1: 0.027
      d2: 0.007
      d3: 0.008
    feature_dim: 19
    truncation_length: 507
- exp_id: gpt2xl_temp09_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    data:
      samples_per_depth: 5000
      total_samples: 20000
      depths: 4
    finetune_losses:
      depth_1: 2.5498
      depth_2: 1.6972
      depth_3: 1.2922
    code_contamination:
      depth_0:
        broad: 25
        narrow: 20
        broad_pct: 0.5
        narrow_pct: 0.4
      depth_1:
        broad: 25
        narrow: 40
        broad_pct: 0.5
        narrow_pct: 0.8
      depth_2:
        broad: 34
        narrow: 80
        broad_pct: 0.7
        narrow_pct: 1.6
      depth_3:
        broad: 25
        narrow: 76
        broad_pct: 0.5
        narrow_pct: 1.5
    four_class:
      rf_accuracy: 0.8542
      rf_accuracy_ci:
      - 0.843
      - 0.8653
      lr_accuracy: 0.8155
      lr_accuracy_ci:
      - 0.8025
      - 0.8273
      rf_auc:
        d0v1: 0.9963
        d0v2: 0.9992
        d0v3: 1
        d1v2: 0.9367
        d1v3: 0.9947
        d2v3: 0.8815
      lr_auc:
        d0v1: 0.984
        d0v2: 0.9998
        d0v3: 1
        d1v2: 0.8903
        d1v3: 0.9824
        d2v3: 0.8183
      top_features:
      - p90_ppl
      - mean_surprisal
      - p75_ppl
      - var_surprisal
    three_class:
      rf_accuracy: 0.82
      rf_accuracy_ci:
      - 0.806
      - 0.834
      lr_accuracy: 0.7773
      lr_accuracy_ci:
      - 0.7627
      - 0.792
      rf_auc:
        d1v2: 0.9418
        d1v3: 0.9967
        d2v3: 0.8849
    three_class_filtered:
      rf_accuracy: 0.815
      rf_accuracy_ci:
      - 0.7999
      - 0.8298
      lr_accuracy: 0.7869
      lr_accuracy_ci:
      - 0.7711
      - 0.8016
      rf_auc:
        d1v2: 0.937
        d1v3: 0.9944
        d2v3: 0.8891
- exp_id: dcol_deberta_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cross_model_olmo_temp09_001
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: olmo_temp09_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    four_class:
      rf_accuracy: 0.8203
      d1v2_auc: 0.901
    three_class_filtered:
      rf_accuracy: 0.7757
    finetune_losses:
      depth_0: 2.27
      depth_1: 1.63
      depth_2: 1.18
    code_contamination_narrow_max: 0.007
    top_features:
    - p90_ppl (0.199)
    - var_surprisal (0.174)
    - p75_ppl (0.126)
- exp_id: olmo_topk50_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    four_class:
      lr_accuracy: 0.757
      lr_accuracy_ci:
      - 0.7425
      - 0.7702
      rf_accuracy: 0.742
      rf_accuracy_ci:
      - 0.7282
      - 0.7555
    pairwise_auc:
      lr:
        d0v1: 0.9969
        d0v2: 0.9995
        d0v3: 0.9998
        d1v2: 0.8293
        d1v3: 0.9592
        d2v3: 0.7497
      rf:
        d0v1: 0.993
        d0v2: 0.9983
        d0v3: 0.9991
        d1v2: 0.8305
        d1v3: 0.9591
        d2v3: 0.7357
    three_class:
      lr_accuracy: 0.6567
      lr_accuracy_ci:
      - 0.6403
      - 0.6733
      rf_accuracy: 0.6517
      rf_accuracy_ci:
      - 0.635
      - 0.6687
    three_class_filtered:
      lr_accuracy: 0.6703
      lr_accuracy_ci:
      - 0.653
      - 0.6882
      rf_accuracy: 0.6699
      rf_accuracy_ci:
      - 0.6537
      - 0.6875
    three_class_filtered_auc:
      lr:
        d1v2: 0.7903
        d1v3: 0.97
        d2v3: 0.7501
      rf:
        d1v2: 0.8071
        d1v3: 0.9645
        d2v3: 0.7364
    feature_importance_top5:
    - p90_ppl
    - var_surprisal
    - p75_ppl
    - mean_surprisal
    - p25_ppl
    finetune_loss:
      depth_1: 1.946
      depth_2: 1.726
    code_contamination:
      narrow_pct:
        depth_0: 0.4
        depth_1: 0.8
        depth_2: 0.3
        depth_3: 0.4
      broad_pct:
        depth_0: 0.5
        depth_1: 2.5
        depth_2: 0.8
        depth_3: 0.7
- exp_id: gpt2xl_topk50_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    four_class:
      accuracy: 0.766
      depth1_vs_depth2_auc: 0.8259
      pass: true
    three_class:
      accuracy: 0.695
      depth1_vs_depth2_auc: 0.8392
      pass: true
    three_class_filtered:
      accuracy: 0.684
      depth1_vs_depth2_auc: 0.8314
      pass: true
- exp_id: dcol_deberta_002
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: dcol_deberta_003
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: atlas_v1_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    monotonicity_rho_range:
    - -0.89
    - -0.82
    edd: 3
    edd_saturated: false
    cross_model_jaccard: 0.667
    cross_model_rank_corr: 0.85
    artifacts:
    - monotonicity_scores.json
    - cross_model_comparison.json
    - edd_analysis.json
    - feature_trajectory.json
- exp_id: olmo_temp09_002
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: baseline_battery_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_reg_single_4class_acc: 0.251
    ppl_reg_multi_4class_acc: 0.622
    ce_mlp_4class_acc: 0.749
    coral_4class_acc: 0.7807
    coral_3class_acc: 0.7089
    coral_mae: 0.2273
    coral_d1v2_auc: 0.8179
    diveye_4class_acc: 0.7817
    diveye_3class_acc: 0.7098
    diveye_d1v2_auc: 0.8654
    rf_4class_acc: 0.781
    lr_4class_acc: 0.75
    note: CE-MLP 74.9% may be undertrained (5 epochs); CORAL updated to 100 epochs.
      All results from Pythia nucleus baseline features.
- exp_id: dcol_deberta_004
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: dcol_deberta_005
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: batch_feature_extraction_5cells
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: depth_extension_pythia_d4d5_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    six_class_rf_accuracy: 0.6232
    six_class_rf_accuracy_ci:
    - 0.6113
    - 0.636
    six_class_lr_accuracy: 0.5862
    pairwise_auc_rf:
      d0v1: 0.9962
      d1v2: 0.8231
      d2v3: 0.6878
      d3v4: 0.6809
      d4v5: 0.6948
    pairwise_auc_lr:
      d0v1: 0.9908
      d1v2: 0.6901
      d2v3: 0.6174
      d3v4: 0.6828
      d4v5: 0.6554
    cumulative_auc_rf:
      d0v5: 0.9987
      d1v5: 0.9874
      d2v5: 0.949
      d3v5: 0.8632
    edd_at_075: 2
    feature_importance_top5:
    - p90_ppl (0.1376)
    - var_surprisal (0.1344)
    - mean_ppl (0.0796)
    - mean_surprisal (0.0789)
    - p75_ppl (0.0680)
    finetune_losses:
      depth_3: 0.7634
      depth_4: 0.5828
    WARNING: 6-class pairwise AUC 不可与 4-class 直比，决策边界稀释导致系统性偏低。需 binary pairwise classifier
      重新评估。
- exp_id: cross_model_loo_001
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    mean_4class_acc: 0.664
    holdout_pythia:
      acc: 0.6242
      ci:
      - 0.6206
      - 0.6282
      d1v2_auc: 0.5617
      d2v3_auc: 0.6534
    holdout_olmo:
      acc: 0.6921
      ci:
      - 0.6886
      - 0.6959
      d1v2_auc: 0.7687
      d2v3_auc: 0.6862
    holdout_gpt2xl:
      acc: 0.6756
      ci:
      - 0.6719
      - 0.6792
      d1v2_auc: 0.8157
      d2v3_auc: 0.6639
    per_class_recall:
      holdout_pythia:
        d0: 1
        d1: 0.493
        d2: 0.268
        d3: 0.736
      holdout_olmo:
        d0: 0.993
        d1: 0.755
        d2: 0.433
        d3: 0.588
      holdout_gpt2xl:
        d0: 0.985
        d1: 0.747
        d2: 0.526
        d3: 0.445
    gate_passed: true
    gate_threshold: 0.45
- exp_id: cross_model_loo_v1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mean_acc: 0.664
    mean_3class_acc: 0.5544
    holdout_pythia:
      acc: 0.6242
      ci95:
      - 0.6205
      - 0.6282
      3class_acc: 0.499
      3class_ci95:
      - 0.4944
      - 0.5034
      d1v2_auc: 0.5617
      d1v3_auc: 0.8547
      d2v3_auc: 0.6534
      d0v1_auc: 0.9921
      d0v2_auc: 0.9999
      d0v3_auc: 0.9998
      per_class:
        d0:
          P: 0.9889
          R: 1
          F1: 0.9944
        d1:
          P: 0.6655
          R: 0.493
          F1: 0.5664
        d2:
          P: 0.3699
          R: 0.2677
          F1: 0.3106
        d3:
          P: 0.483
          R: 0.7363
          F1: 0.5834
    holdout_olmo:
      acc: 0.6921
      ci95:
      - 0.6884
      - 0.696
      3class_acc: 0.592
      3class_ci95:
      - 0.5873
      - 0.5965
      d1v2_auc: 0.7687
      d1v3_auc: 0.9277
      d2v3_auc: 0.6862
      per_class:
        d0:
          P: 0.9783
          R: 0.9925
          F1: 0.9854
        d1:
          P: 0.7111
          R: 0.7549
          F1: 0.7324
        d2:
          P: 0.4616
          R: 0.4327
          F1: 0.4467
        d3:
          P: 0.5964
          R: 0.5883
          F1: 0.5923
    holdout_gpt2xl:
      acc: 0.6756
      ci95:
      - 0.6717
      - 0.6795
      3class_acc: 0.5723
      3class_ci95:
      - 0.5679
      - 0.5767
      d1v2_auc: 0.8157
      d1v3_auc: 0.9149
      d2v3_auc: 0.6639
      d0v1_auc: 0.9927
      d0v2_auc: 0.9919
      d0v3_auc: 0.9876
      per_class:
        d0:
          P: 0.9484
          R: 0.9853
          F1: 0.9665
        d1:
          P: 0.7093
          R: 0.7465
          F1: 0.7274
        d2:
          P: 0.4521
          R: 0.5255
          F1: 0.486
        d3:
          P: 0.5963
          R: 0.445
          F1: 0.5097
    mean_per_class_recall:
      d0: 0.9926
      d1: 0.6648
      d2: 0.4086
      d3: 0.5899
    lowest_recall_class: d2
    lowest_recall_value: 0.4086
    detailed_artifact: cross_model_loo_detailed.json
- exp_id: atlas_v2_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    p90_ppl_in_top2: 9/9
    var_surprisal_in_top2: 7/9
    edd_equals_3_at_T075: 7/9
    edd_distribution_T075:
      '2': 2
      '3': 7
    cross_model_rank_corr_range: '[0.619, 0.954]'
    cross_model_rank_corr_mean: 0.868
    cv5_accuracy_range: '[0.688, 0.859]'
    cells_covered: 9/9
- exp_id: cross_strategy_loo_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mean_4class_acc: 0.5908
    pythia_holdout_nucleus:
      acc: 0.6935
      d1v2_auc: 0.6903
      d2v3_auc: 0.7626
    pythia_holdout_temp09:
      acc: 0.6281
      d1v2_auc: 0.576
      d2v3_auc: 0.724
    pythia_holdout_topk50:
      acc: 0.5151
      d1v2_auc: 0.6393
      d2v3_auc: 0.5801
    gpt2xl_holdout_nucleus:
      acc: 0.5993
      d1v2_auc: 0.7826
      d2v3_auc: 0.4985
    gpt2xl_holdout_temp09:
      acc: 0.5609
      d1v2_auc: 0.1288
      d2v3_auc: 0.6366
    gpt2xl_holdout_topk50:
      acc: 0.5364
      d1v2_auc: 0.8308
      d2v3_auc: 0.7222
    olmo_holdout_nucleus:
      acc: 0.6538
      d1v2_auc: 0.7931
      d2v3_auc: 0.6076
    olmo_holdout_temp09:
      acc: 0.5816
      d1v2_auc: 0.2529
      d2v3_auc: 0.7015
    olmo_holdout_topk50:
      acc: 0.5488
      d1v2_auc: 0.8549
      d2v3_auc: 0.7107
    finding_temp09_d1v2_inversion: 'd1v2 AUC inverts when holding out temp09 (GPT-2
      XL: 0.13, OLMo: 0.25) — temp09 d1→d2 features differ fundamentally from nucleus/topk50'
- exp_id: dcol_roberta_v6_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    test_acc: 0.6448
    test_mae: 0.4052
    best_val_acc: 0.6436
    best_epoch: 1
    epochs_run: 4
    early_stopping: true
    train_acc_final: 0.75
    rf_baseline: 0.782
    delta_vs_baseline: -0.137
    overfitting: severe (train 75% vs val 64.4% at best epoch)
    stability: resolved (no NaN, no collapse, collapse guard passed at step 500)
- exp_id: baseline_battery_9cell_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_acc_matrix:
      pythia_nucleus: 0.782
      pythia_temp09: 0.772
      pythia_topk50: 0.688
      olmo_nucleus: 0.796
      olmo_temp09: 0.827
      olmo_topk50: 0.759
      gpt2xl_nucleus: 0.843
      gpt2xl_temp09: 0.853
      gpt2xl_topk50: 0.754
    methods:
    - RF
    - LR
    - CORAL
    - DivEye
    cells: 9
    finding: RF ≈ CORAL > DivEye > LR, max gap ~4pp. GPT-2 XL temp09 best (85.3%),
      model effect > strategy effect
    WARNING: best_acc_matrix stores best-across-ALL-methods accuracy, NOT RF-only.
      For RF accuracy use each cell's own registry (e.g. olmo_topk50_001.metrics.four_class.rf_accuracy).
      olmo_topk50 diff=2.2pp, olmo_nucleus diff=0.83pp.
- exp_id: cross_strategy_loo_zscore_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    mean_raw_acc: 0.5908
    mean_zscore_acc: 0.5915
    raw:
      pythia_holdout_nucleus:
        acc: 0.6935
        d1v2_auc: 0.6903
        d2v3_auc: 0.7626
      pythia_holdout_temp09:
        acc: 0.6281
        d1v2_auc: 0.576
        d2v3_auc: 0.724
      pythia_holdout_topk50:
        acc: 0.5151
        d1v2_auc: 0.6393
        d2v3_auc: 0.5801
      gpt2xl_holdout_nucleus:
        acc: 0.5993
        d1v2_auc: 0.7826
        d2v3_auc: 0.4985
      gpt2xl_holdout_temp09:
        acc: 0.5609
        d1v2_auc: 0.1288
        d2v3_auc: 0.6366
      gpt2xl_holdout_topk50:
        acc: 0.5364
        d1v2_auc: 0.8308
        d2v3_auc: 0.7222
      olmo_holdout_nucleus:
        acc: 0.6538
        d1v2_auc: 0.7931
        d2v3_auc: 0.6076
      olmo_holdout_temp09:
        acc: 0.5816
        d1v2_auc: 0.2529
        d2v3_auc: 0.7015
      olmo_holdout_topk50:
        acc: 0.5488
        d1v2_auc: 0.8549
        d2v3_auc: 0.7107
    zscore:
      pythia_holdout_nucleus:
        acc: 0.6992
        d1v2_auc: 0.7043
        d2v3_auc: 0.7683
      pythia_holdout_temp09:
        acc: 0.6368
        d1v2_auc: 0.5943
        d2v3_auc: 0.7352
      pythia_holdout_topk50:
        acc: 0.5155
        d1v2_auc: 0.6386
        d2v3_auc: 0.5804
      gpt2xl_holdout_nucleus:
        acc: 0.5959
        d1v2_auc: 0.788
        d2v3_auc: 0.4927
      gpt2xl_holdout_temp09:
        acc: 0.5632
        d1v2_auc: 0.1348
        d2v3_auc: 0.631
      gpt2xl_holdout_topk50:
        acc: 0.5356
        d1v2_auc: 0.8391
        d2v3_auc: 0.7282
      olmo_holdout_nucleus:
        acc: 0.6506
        d1v2_auc: 0.796
        d2v3_auc: 0.6078
      olmo_holdout_temp09:
        acc: 0.5782
        d1v2_auc: 0.2497
        d2v3_auc: 0.6871
      olmo_holdout_topk50:
        acc: 0.5484
        d1v2_auc: 0.8579
        d2v3_auc: 0.7056
    temp09_d1v2_delta:
      pythia: 0.0183
      gpt2xl: 0.006
      olmo: -0.0033
    finding: Z-score does NOT fix temp09 d1v2 inversion in RF — RF is scale-invariant
      (tree splits unaffected by monotonic transforms). Prior z-score recovery (0.13→0.68)
      was with LR, not RF.
- exp_id: depth_extension_binary_pairwise_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: depth_extension_binary_pairwise_002
  name: ''
  status: DONE
  conclusion: success
  metrics:
    d1v2_auc: 0.925
    d1v2_ci95:
    - 0.9138
    - 0.9354
    d2v3_auc: 0.8225
    d2v3_ci95:
    - 0.8052
    - 0.8402
    d3v4_auc: 0.7837
    d3v4_ci95:
    - 0.7648
    - 0.8024
    d4v5_auc: 0.6832
    d4v5_ci95:
    - 0.6611
    - 0.7045
    edd_determination: '4'
- exp_id: depth_extension_gpt2xl_d4d5_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    binary_pairwise:
      d1v2_auc: 0.966
      d2v3_auc: 0.919
      d3v4_auc: 0.75
      d4v5_auc: 0.681
    six_class_rf_accuracy: 0.679
    edd_at_075: 4
    edd_note: d3v4=0.750>=0.75 PASS, d4v5=0.681<0.75 FAIL → EDD=4
- exp_id: zero_shot_llm_baseline_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    four_class_acc: 0.4
    n_samples: 200
    sample_distribution:
      d0: 56
      d1: 47
      d2: 49
      d3: 48
    model: DeepSeek V3.2
    method: zero-shot prompting
    vs_rf_baseline: -0.382
    vs_chance: 0.15
    note: 40.0% (80/200) above chance (25%) but far below RF 78.2% (-38.2pp). Zero-shot
      LLM cannot reliably distinguish recursive depth from raw text alone.
- exp_id: granularity_ablation_rf_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    summary:
      binary_acc_mean: 0.995
      binary_acc_std: 0.004
      3class_acc_mean: 0.721
      3class_acc_std: 0.067
      4class_acc_mean: 0.783
      4class_acc_std: 0.048
      6class_acc: 0.629
      note: '3-class excludes d0 (most separable class), so 3class < 4class is by
        design. True granularity trend (with d0): binary 99.5% > 4-class 78.3% > 6-class
        62.9% — monotonic decrease confirmed.'
    per_cell:
      pythia_nucleus095:
        binary:
          acc: 0.998
          ci95:
          - 0.9965
          - 0.9992
          auc:
            d0v1: 1
        3class:
          acc: 0.7117
          ci95:
          - 0.6947
          - 0.7283
          auc:
            d1v2: 0.861
            d2v3: 0.796
        4class:
          acc: 0.7812
          ci95:
          - 0.7677
          - 0.7935
          auc:
            d0v1: 0.998
            d1v2: 0.868
            d2v3: 0.804
        6class:
          acc: 0.6292
          ci95:
          - 0.6175
          - 0.6412
          auc:
            d0v1: 0.997
            d1v2: 0.83
            d2v3: 0.689
            d3v4: 0.692
            d4v5: 0.691
      pythia_temp09:
        binary:
          acc: 0.997
          ci95:
          - 0.9952
          - 0.9985
          auc:
            d0v1: 1
        3class:
          acc: 0.7063
          ci95:
          - 0.6907
          - 0.723
          auc:
            d1v2: 0.838
            d2v3: 0.806
        4class:
          acc: 0.7605
          ci95:
          - 0.7475
          - 0.7738
          auc:
            d0v1: 0.997
            d1v2: 0.835
            d2v3: 0.796
      pythia_topk50:
        binary:
          acc: 0.9945
          ci95:
          - 0.992
          - 0.9965
          auc:
            d0v1: 1
        3class:
          acc: 0.5883
          ci95:
          - 0.5717
          - 0.6073
          auc:
            d1v2: 0.749
            d2v3: 0.705
        4class:
          acc: 0.6943
          ci95:
          - 0.6805
          - 0.708
          auc:
            d0v1: 0.994
            d1v2: 0.761
            d2v3: 0.695
      gpt2xl_nucleus095:
        binary:
          acc: 0.9912
          ci95:
          - 0.9882
          - 0.9938
          auc:
            d0v1: 0.999
        3class:
          acc: 0.79
          ci95:
          - 0.775
          - 0.8047
          auc:
            d1v2: 0.913
            d2v3: 0.891
        4class:
          acc: 0.8393
          ci95:
          - 0.8283
          - 0.8502
          auc:
            d0v1: 0.995
            d1v2: 0.916
            d2v3: 0.885
      gpt2xl_temp09:
        binary:
          acc: 0.9978
          ci95:
          - 0.9962
          - 0.999
          auc:
            d0v1: 1
        3class:
          acc: 0.826
          ci95:
          - 0.8117
          - 0.8397
          auc:
            d1v2: 0.944
            d2v3: 0.887
        4class:
          acc: 0.8552
          ci95:
          - 0.844
          - 0.866
          auc:
            d0v1: 0.997
            d1v2: 0.939
            d2v3: 0.886
      gpt2xl_topk50:
        binary:
          acc: 0.9952
          ci95:
          - 0.993
          - 0.9972
          auc:
            d0v1: 1
        3class:
          acc: 0.695
          ci95:
          - 0.6777
          - 0.7113
          auc:
            d1v2: 0.844
            d2v3: 0.766
        4class:
          acc: 0.757
          ci95:
          - 0.743
          - 0.7702
          auc:
            d0v1: 0.993
            d1v2: 0.824
            d2v3: 0.762
      olmo_nucleus095:
        binary:
          acc: 0.9868
          ci95:
          - 0.9832
          - 0.99
          auc:
            d0v1: 0.999
        3class:
          acc: 0.7503
          ci95:
          - 0.7353
          - 0.7657
          auc:
            d1v2: 0.873
            d2v3: 0.831
        4class:
          acc: 0.7897
          ci95:
          - 0.7772
          - 0.8027
          auc:
            d0v1: 0.985
            d1v2: 0.87
            d2v3: 0.816
      olmo_temp09:
        binary:
          acc: 0.9982
          ci95:
          - 0.997
          - 0.9992
          auc:
            d0v1: 1
        3class:
          acc: 0.7633
          ci95:
          - 0.7477
          - 0.7797
          auc:
            d1v2: 0.894
            d2v3: 0.838
        4class:
          acc: 0.8263
          ci95:
          - 0.8147
          - 0.8385
          auc:
            d0v1: 0.996
            d1v2: 0.903
            d2v3: 0.828
      olmo_topk50:
        binary:
          acc: 0.996
          ci95:
          - 0.994
          - 0.9978
          auc:
            d0v1: 1
        3class:
          acc: 0.661
          ci95:
          - 0.644
          - 0.6773
          auc:
            d1v2: 0.812
            d2v3: 0.739
        4class:
          acc: 0.7435
          ci95:
          - 0.73
          - 0.758
          auc:
            d0v1: 0.995
            d1v2: 0.831
            d2v3: 0.738
    boundary_dilution:
      d2v3_auc_by_granularity_pythia_nuc:
        3class: 0.796
        4class: 0.804
        6class: 0.689
      d1v2_auc_by_granularity_pythia_nuc:
        3class: 0.861
        4class: 0.868
        6class: 0.83
      note: d2v3 AUC drops 14% from 4-class to 6-class (0.804→0.689), confirming decision
        boundary dilution at higher granularity
    decoding_strategy_ranking:
      4class_acc:
        temp09: 0.814
        nucleus095: 0.803
        topk50: 0.732
      note: topk50 consistently worst across all 3 models; temp09 slightly outperforms
        nucleus095
- exp_id: depth_extension_olmo_d4d5_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: lr_zscore_cross_strategy_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    raw_lr:
      mean_acc: 0.25
      note: lbfgs convergence failure on unscaled features, all predictions random
      pythia_temp09:
        acc: 0.25
        d1v2_auc: 0.6313
      gpt2xl_temp09:
        acc: 0.25
        d1v2_auc: 0.5
      olmo_temp09:
        acc: 0.25
        d1v2_auc: 0.5
    zscore_lr:
      mean_acc: 0.6081
      mean_d1v2: 0.6417
      pythia_temp09:
        acc: 0.6139
        d1v2_auc: 0.5201
      gpt2xl_temp09:
        acc: 0.5642
        d1v2_auc: 0.2386
      olmo_temp09:
        acc: 0.5546
        d1v2_auc: 0.1922
      pythia_nucleus:
        acc: 0.6425
        d1v2_auc: 0.6142
      gpt2xl_nucleus:
        acc: 0.7397
        d1v2_auc: 0.8851
      olmo_nucleus:
        acc: 0.748
        d1v2_auc: 0.8627
      pythia_topk50:
        acc: 0.5261
        d1v2_auc: 0.7711
      gpt2xl_topk50:
        acc: 0.5352
        d1v2_auc: 0.8214
      olmo_topk50:
        acc: 0.5484
        d1v2_auc: 0.8696
    paper_claim_vs_actual:
      gpt2xl_temp09_d1v2:
        paper_raw: 0.13
        paper_zscore: 0.68
        actual_raw: 0.5
        actual_zscore: 0.2386
      olmo_temp09_d1v2:
        paper_raw: 0.25
        paper_zscore: 0.83
        actual_raw: 0.5
        actual_zscore: 0.1922
- exp_id: depth_extension_olmo_d4d5_002
  name: ''
  status: DONE
  conclusion: success
  metrics:
    binary_pairwise:
      d1v2_auc: 0.968
      d2v3_auc: 0.843
      d3v4_auc: 0.765
      d4v5_auc: 0.684
    six_class_rf_accuracy: 0.667
    edd_at_075: 4
    edd_note: d3v4=0.765>=0.75 PASS, d4v5=0.684<0.75 FAIL → EDD=4
- exp_id: n2_deberta_finetune_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy_mean: 0.5831
    accuracy_std: 0.0467
    per_class_f1:
      d0: 0.947
      d1: 0.378
      d2: 0.247
      d3: 0.656
    pairwise_auc:
      d0v1: 0.981
      d1v2: 0.733
      d2v3: 0.755
    vs_rf_baseline: 58.3% vs 78.2% (-19.9pp)
    elapsed_seconds: 3727
- exp_id: n2_roberta_finetune_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy_mean: 0.5948
    accuracy_std: 0.0324
    per_class_f1:
      d0: 0.958
      d1: 0.4161
      d2: 0.2611
      d3: 0.6472
    per_class_precision:
      d0: 0.9983
      d1: 0.7178
      d2: 0.2956
      d3: 0.4958
    per_class_recall:
      d0: 0.9208
      d1: 0.293
      d2: 0.2338
      d3: 0.9314
    pairwise_auc:
      d0v1: 0.9886
      d1v2: 0.7522
      d2v3: 0.7349
    fold_accuracies:
    - 0.6022
    - 0.5595
    - 0.5623
    - 0.6018
    - 0.648
    vs_rf_baseline: -18.7pp (59.5% vs 78.2%)
    vs_deberta: +1.2pp acc, +0.019 d1v2_auc, -0.020 d2v3_auc
    elapsed_seconds: 1942.5
- exp_id: temp07_pilot_pythia_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    samples_per_depth: 500
    depths: 6
    six_class_rf_accuracy: 0.5733
    six_class_rf_ci95:
    - 0.5333
    - 0.615
    six_class_lr_accuracy: 0.5467
    pairwise_auc_rf:
      d0v1: 0.9981
      d1v2: 0.8378
      d2v3: 0.635
      d3v4: 0.5997
      d4v5: 0.6025
    pairwise_auc_lr:
      d0v1: 0.9954
      d1v2: 0.8031
      d2v3: 0.608
      d3v4: 0.6525
      d4v5: 0.5652
    vs_temp09_d1v2_rf: 0.8378 vs 0.8327 (+0.005)
    vs_temp09_d1v2_lr: 0.8031 vs 0.7833 (+0.020)
    d1v2_inversion: false
    top_features:
    - p90_ppl
    - var_surprisal
    - mean_surprisal
    - mean_ppl
    - p75_ppl
- exp_id: zeroshot_llm_500_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.362
    accuracy_ci95:
    - 0.32
    - 0.404
    ci_width_pp: 8.4
    mae: 1.028
    per_class_f1:
      d0: 0.55
      d1: 0.18
      d2: 0.27
      d3: 0.18
    per_class_recall:
      d0: 0.952
      d1: 0.128
      d2: 0.248
      d3: 0.12
    vs_rf_baseline: 36.2% vs 78.2% (-42.0pp)
    vs_200_sample: 36.2% vs 40.0% (consistent, within CI)
    n_samples: 500
    n_errors: 0
- exp_id: feat_ablation_v1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    full_19_mean_acc: 0.7847
    full_19_std: 0.0494
    top5_mean_acc: 0.7678
    top5_std: 0.0527
    top2_mean_acc: 0.7152
    top2_std: 0.0581
    n_features_95pct_mean: 4.2
    n_features_95pct_max: 5
    best_category_all_cells: perplexity
    perplexity_cat_mean_acc: 0.7668
    surprisal_cat_mean_acc: 0.7333
    lexdiv_cat_mean_acc: 0.4618
    repetition_cat_mean_acc: 0.4374
    ngram_entropy_cat_mean_acc: 0.3952
    first_selected_feature_mode: p90_ppl (6/9)
    first_selected_feature_alt: var_surprisal (3/9)
    total_runtime_sec: 7822
- exp_id: feature_ablation_9cell
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: w2_domain_bias_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    subexp_a_d1d3_mean_acc: 0.72
    subexp_a_range: 59.1%-81.8%
    subexp_b_logo_mean_acc: 0.721
    subexp_b_range: 59.5%-81.6%
    subexp_b_note: 'fixed: per-depth seed assignment, groups now depth-balanced. LOGO=CV
      within noise'
    subexp_c_depth_pred_mean: 0.72
    subexp_c_seed_group_pred_mean: 0.102
    subexp_c_ratio_mean: 7.06
    subexp_c_note: seed groups at chance (10.2% vs 10%), no measurable domain bias
    chance_3class: 0.333
    chance_seed_group: 0.1
    paper_updated: section_appendix.tex L54-72, conclusion.tex L14
- exp_id: shap_supplement_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    kendalls_w_three_way: 0.8955
    rho_shap_gini: 0.9312
    rho_shap_permutation: 0.8392
    rho_gini_permutation: 0.76
    cross_cell_shap_consistency_mean_rho: 0.8
    p90_ppl_top2_cells: 9/9
    var_surprisal_top2_cells: 8/9
    ppl_surprisal_shap_share: 0.888
    shap_top5: p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl
    addresses: R3-N3 feature importance cross-validation
- exp_id: xgboost_lgbm_baseline_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    xgb_acc: 0.79
    xgb_std: 0.0046
    xgb_d0v1_auc: 1
    xgb_d1v2_auc: 0.931
    xgb_d2v3_auc: 0.816
    lgbm_acc: 0.788
    lgbm_std: 0.0077
    lgbm_d0v1_auc: 1
    lgbm_d1v2_auc: 0.931
    lgbm_d2v3_auc: 0.814
    rf_acc_ref: 0.782
    xgb_recall_d0: 0.994
    xgb_recall_d1: 0.816
    xgb_recall_d2: 0.596
    xgb_recall_d3: 0.754
    lgbm_recall_d0: 0.994
    lgbm_recall_d1: 0.815
    lgbm_recall_d2: 0.596
    lgbm_recall_d3: 0.747
- exp_id: xgboost_lgbm_3cell_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gpt2xl_temp09:
      RF: 85.8
      XGBoost: 86.2
      LightGBM: 86.2
      d1v2_AUC: 0.98
      d2v3_AUC: 0.886
    pythia_nucleus095:
      RF: 78.8
      XGBoost: 79
      LightGBM: 78.9
      d1v2_AUC: 0.931
      d2v3_AUC: 0.816
    pythia_topk50:
      RF: 68.9
      XGBoost: 68.9
      LightGBM: 68.7
      d1v2_AUC: 0.841
      d2v3_AUC: 0.689
- exp_id: wild_data_calibration_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext_n_passages: 546
    wikitext_d0_pct: 100
    wikitext_d1_pct: 0
    wikitext_d2_pct: 0
    wikitext_d3_pct: 0
    wikitext_mean_p_d0: 0.9963
    controlled_d0_mean_p_d0: 0.9941
    controlled_d0_acc: 100
    controlled_d1_acc: 99.96
    controlled_d2_acc: 99.94
    controlled_d3_acc: 99.9
    cv5_accuracy: 0.7878
    cv5_std: 0.0056
    domain_shift_mean_ppl_pct: +621%
    domain_shift_var_ppl_pct: +503%
    domain_shift_p90_ppl_pct: +115%
    finding: WikiText-103 100% classified as d0 despite large feature-space domain
      shift in perplexity features; RF robust to distribution shift
- exp_id: downstream_curation_poc_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    unfiltered:
      ppl_mean: 15.776
      ppl_std: 0.066
      n_samples: 10000
    rf_strict:
      ppl_mean: 15.81
      ppl_std: 0.061
      n_samples: 2496
      delta: '-0.034'
      p: 0.607
      d: -0.528
    rf_moderate:
      ppl_mean: 15.756
      ppl_std: 0.056
      n_samples: 4940
      delta: '+0.021'
      p: 0.492
      d: 0.334
    rf_soft:
      ppl_mean: 15.733
      ppl_std: 0.038
      n_samples: 4422
      delta: '+0.043'
      p: 0.407
      d: 0.792
    oracle_strict:
      ppl_mean: 15.879
      ppl_std: 0.128
      n_samples: 2500
      delta: '-0.103'
      p: 0.216
      d: -1.004
    oracle_moderate:
      ppl_mean: 15.809
      ppl_std: 0.103
      n_samples: 5000
      delta: '-0.033'
      p: 0.485
      d: -0.384
    random_strict:
      ppl_mean: 16.239
      ppl_std: 0.165
      n_samples: 2496
      delta: '-0.463'
      p: 0.013
      d: -3.671
      sig: true
    random_moderate:
      ppl_mean: 15.998
      ppl_std: 0.09
      n_samples: 5000
      delta: '-0.222'
      p: 0.028
      d: -2.809
      sig: true
    cross_condition:
      rf_strict_vs_random_strict:
        delta: 0.429
        t: -7.052
        p: 0.002
        sig: true
      rf_moderate_vs_random_moderate:
        delta: 0.242
        t: -3.77
        p: 0.02
        sig: true
      rf_soft_vs_unfiltered:
        delta: 0.043
        t: 0.927
        p: 0.407
        sig: false
      random_strict_vs_unfiltered:
        delta: -0.463
        t: 4.219
        p: 0.014
        sig: true
- exp_id: wild_data_c4_supplement_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_n_passages: 5000
    c4_d0_pct: 79.8
    c4_d1plus_pct: 20.2
    c4_d1plus_count: 1012
    wikitext_d0_pct: 100
    controlled_accuracy: 99.9%+
    cv5_accuracy: 0.7878
    misclassified_feature_diff:
      rep_4gram: +74.7%
      rep_3gram: +37.0%
      p90_ppl: +39.6%
    misclassified_content_type: ads, product descriptions, SEO template content
    finding: FPR=0% on editorial text (WikiText), FPR≈20% on web-crawl (C4) — false
      positives driven by template/low-quality content with high repetition and low
      diversity, not random noise
- exp_id: pythia7b_cross_scale_001
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: wild_data_gpt2xl_calibration_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cv_accuracy: 0.841
    cv_std: 0.004
    wikitext_n_passages: 546
    wikitext_d0_pct: 99.27
    wikitext_d1_pct: 0.73
    c4_n_passages: 5000
    c4_d0_pct: 77.62
    c4_d1_pct: 9.04
    c4_d2_pct: 3.72
    c4_d3_pct: 9.62
    c4_fpr_vs_pythia: GPT-2 XL FPR 22.4% vs Pythia 20.2% — consistent template/SEO
      pattern
    finding: 'Cross-model calibration consistent: both models flag same C4 template
      content as non-d0. GPT-2 XL slightly higher FPR due to stronger signal. WikiText
      near-perfect for both.'
- exp_id: wild_data_olmo_calibration_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cv_accuracy: 0.7893
    cv_std: 0.0039
    wikitext_n_passages: 546
    wikitext_d0_pct: 98.53
    wikitext_non_d0: 8
    c4_n_passages: 5000
    c4_d0_pct: 95.28
    c4_d1_pct: 2.92
    c4_d2_pct: 0.5
    c4_d3_pct: 1.3
    c4_fpr: 4.72
    finding: OLMo C4 FPR (4.72%) far lower than Pythia (20.2%) and GPT-2 XL (22.4%).
      OLMo d1-d3 features diverge more from d0, creating wider d0 decision boundary
      that correctly classifies more C4 template content as d0.
- exp_id: random_soft_control_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    random_soft_ppl:
      seed_42: 15.99
      seed_123: 16.0276
      seed_456: 16.1682
      seed_789: 15.9993
      seed_1024: 16.1224
      mean: 16.0615
      std: 0.0794
    rf_soft_ppl:
      seed_42: 15.7134
      seed_123: 15.7014
      seed_456: 15.7875
      seed_789: 15.6956
      seed_1024: 15.7689
      mean: 15.7334
      std: 0.042
    comparison:
      delta_ppl: 0.3281
      t_statistic: 17.9777
      p_value: 5.6e-05
      cohens_d: 8.0399
      significant: true
    train_loss:
      seed_42: 1.6748
      seed_123: 1.6786
      seed_456: 1.6721
      seed_789: 1.6736
      seed_1024: 1.6739
- exp_id: wild_data_redpajama_dolma_001
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: wild_data_calibration_002
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    error: C4 load_dataset hung - allenai/c4 HF streaming failed on AutoDL proxy.
      OpenWebText loaded OK (5000 passages, 23s) but C4 load_dataset never returned.
      JSON written with empty datasets/cross_model_consistency. No error/exception
      in logs - silent hang during HF Hub streaming.
- exp_id: wild_data_calibration_003
  name: ''
  status: DONE
  conclusion: success
  metrics:
    fineweb_n_passages: 5000
    fineweb_d0_pct: 80.54
    fineweb_d1_pct: 19.46
    fineweb_d2_pct: 0
    fineweb_d3_pct: 0
    fineweb_fpr: 19.46
    fineweb_mean_p_d0: 0.7987
    fineweb_mean_p_d1: 0.1707
    vs_c4_fpr_delta: -0.74
    vs_wikitext_fpr_delta: 19.46
    elapsed_seconds: 87
    finding: FineWeb FPR=19.46% — virtually identical to C4 FPR=20.2% (Δ=-0.74pp).
      All misclassifications are d1 only (no d2/d3). Confirms web-crawl FPR ~20% is
      consistent across datasets and driven by template/SEO content, not dataset-specific
      artifacts.
- exp_id: zeroshot_qwen7b_500_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    acc_4class: 0.304
    acc_4class_ci_95:
    - 0.2653
    - 0.3457
    acc_3class: 0.3173
    mae: 1.01
    per_class_recall:
      d0: 0.264
      d1: 0.552
      d2: 0.104
      d3: 0.296
    per_class_f1:
      d0: 0.3143
      d1: 0.3503
      d2: 0.1436
      d3: 0.3442
    errors: 0
- exp_id: multi_tau_ablation_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    within_tau:
      tau_0.5:
        4class_acc: 0.7725
        d1v2_auc: 0.8423
        d0v1_auc: 0.9962
        d2v3_auc: 0.7636
      tau_0.7:
        4class_acc: 0.754
        d1v2_auc: 0.8505
        d0v1_auc: 0.9966
        d2v3_auc: 0.7197
      tau_0.9:
        4class_acc: 0.759
        d1v2_auc: 0.8083
        d0v1_auc: 0.9911
        d2v3_auc: 0.7805
      tau_1.1:
        4class_acc: 0.5715
        d1v2_auc: 0.5284
        d0v1_auc: 0.9878
        d2v3_auc: 0.5987
    cross_tau_loo:
      holdout_0.5:
        acc: 0.522
        d1v2_auc: 0.1756
      holdout_0.7:
        acc: 0.4095
        d1v2_auc: 0.2985
      holdout_0.9:
        acc: 0.464
        d1v2_auc: 0.2774
      holdout_1.1:
        acc: 0.471
        d1v2_auc: 0.5251
      mean_acc: 0.4666
      mean_d1v2_auc: 0.3192
    training_loss:
      tau_0.5:
        d0: 2.2727
        d1: 0.4201
        d2: 0.1589
      tau_1.1:
        d0: 2.2726
        d1: 1.9077
        d2: 1.8517
- exp_id: wild_data_calibration_004
  name: ''
  status: DONE
  conclusion: success
  metrics:
    openwebtext_pythia_nucleus:
      n: 5000
      d0_pct: 99.1
      fpr_pct: 0.9
      mean_p_d0: 0.7116
    openwebtext_gpt2xl:
      n: 5000
      d0_pct: 98.56
      fpr_pct: 1.44
      mean_p_d0: 0.6191
    openwebtext_olmo:
      n: 5000
      d0_pct: 97.22
      fpr_pct: 2.78
      mean_p_d0: 0.7372
    wikitext: skipped (dtype error)
    finding: OpenWebText FPR极低(0.9-2.8%) vs C4(4.7-22.4%) vs FineWeb(19.5%). 编辑质量高的web数据FPR显著低于web-crawl。
- exp_id: cross_scale_qwen7b_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    four_class_acc: 0.601
    four_class_ci:
    - 0.58
    - 0.621
    six_class_acc: 0.521
    six_class_ci:
    - 0.504
    - 0.538
    edd: '>5'
    pairwise_auc_consecutive:
      d0v1: 0.969
      d1v2: 0.729
      d2v3: 0.709
      d3v4: 0.732
      d4v5: 0.772
    auc_pattern: 'U-shape (non-monotonic: trough at d2v3, rises d3v4/d4v5)'
- exp_id: wild_data_calibration_005
  name: ''
  status: DONE
  conclusion: success
  metrics:
    fpr: 15.3
    d0_accuracy: 84.7
    n_passages: 5000
    vs_c4: -4.9pp
    vs_fineweb: -4.16pp
    vs_openwebtext: +14.4pp
- exp_id: cross_scale_llama3_8b_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cross_model_recursive_chain_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: domain_extension_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    4class_acc: 0.741
    4class_std: 0.02
    per_depth_f1:
      d0: 1
      d1: 0.78
      d2: 0.52
      d3: 0.66
    cv_folds: 5
    domain: arxiv_abstracts
- exp_id: two_stage_strategy_pipeline_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    strategy_classification:
      mean_acc: 0.575
      chance: 0.333
      pythia:
        acc: 0.523
        nucleus_recall: 0.533
        temp09_recall: 0.414
        topk50_recall: 0.622
      olmo:
        acc: 0.548
        nucleus_recall: 0.608
        temp09_recall: 0.479
        topk50_recall: 0.558
      gpt2xl:
        acc: 0.654
        nucleus_recall: 0.845
        temp09_recall: 0.507
        topk50_recall: 0.61
    depth_estimation:
      cross_strategy_loo_ref: 0.591
      predicted_two_stage:
        pythia: 0.693
        olmo: 0.695
        gpt2xl: 0.73
        mean: 0.706
      naive_pooled:
        pythia: 0.709
        olmo: 0.712
        gpt2xl: 0.739
        mean: 0.72
      oracle_two_stage:
        pythia: 0.746
        olmo: 0.785
        gpt2xl: 0.82
        mean: 0.784
      within_strategy_ref:
        pythia: 0.745
        olmo: 0.784
        gpt2xl: 0.816
        mean: 0.782
    key_finding: Oracle two-stage (78.4%) matches within-strategy (78.2%), validating
      theory. But predicted two-stage (70.6%) < naive pooled (72.0%) due to strategy
      classification bottleneck (57.5%).
- exp_id: cross_model_recursive_chain_002
  name: ''
  status: DONE
  conclusion: success
  metrics:
    4class_acc: 0.8475
    4class_ci95:
    - 0.81
    - 0.8825
    per_depth_f1:
      d0: 0.98
      d1: 0.88
      d2: 0.76
      d3: 0.76
    pairwise_auc:
      d0v1: 0.999
      d2v3: 0.841
- exp_id: cross_scale_llama3_8b_002
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: cross_scale_llama3_8b_003
  name: ''
  status: DONE
  conclusion: success
  metrics:
    4class_acc: 0.702
    4class_ci95:
    - 0.683
    - 0.724
    6class_acc: 0.554
    6class_ci95:
    - 0.536
    - 0.571
    edd_estimate: '4'
    edd_note: d4v5 AUC=0.618 < T=0.70, so EDD=4. Monotonic decay causes last pair
      to fall below threshold.
    consecutive_binary_auc:
      d0v1: 0.949
      d1v2: 0.877
      d2v3: 0.771
      d3v4: 0.716
      d4v5: 0.618
    consecutive_binary_acc:
      d0v1: 0.885
      d1v2: 0.81
      d2v3: 0.698
      d3v4: 0.656
      d4v5: 0.583
- exp_id: ref_model_ablation_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pythia_ref_acc: 0.7854
    olmo_ref_acc: 0.7451
    delta_pp: 4.04
    robust: true
- exp_id: cross_scale_llama3_base_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    4class_acc: 0.599
    4class_ci_95:
    - 0.578
    - 0.6215
    6class_acc: 0.4953
    edd_070: 2
    auc_d0v1: 0.9175
    auc_d1v2: 0.7936
    auc_d2v3: 0.6815
    auc_d3v4: 0.73
    auc_d4v5: 0.595
    monotonic: false
    pattern: U-shape (d2v3 dip, d3v4 recovery)
    finding: IT regularizes depth signal (makes AUC monotonic), does not introduce
      U-shape
    edd_note: d0v1=0.9175≥0.70, d1v2=0.7936≥0.70, d2v3=0.6815<0.70 → EDD=2
- exp_id: cross_model_reverse_chain_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 85.75
    ci_95:
    - 82
    - 89.25
    forward_chain_acc: 84.75
    forward_chain_ci:
    - 81
    - 88.25
    conclusion: reverse = forward, architecture confound refuted
- exp_id: lora_rank_ablation_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rank_4_acc: 0.718
    rank_4_auc: 0.7896
    rank_16_acc: 0.7645
    rank_16_auc: 0.8434
    rank_64_acc: 0.731
    rank_64_auc: 0.8326
    best_rank: 16
- exp_id: gpt2xl_ref_ablation_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    gpt2xl_4class_acc: 0.6734
    gpt2xl_ci_95:
    - 0.6667
    - 0.6796
    gpt2xl_d1v2_auc: 0.7269
    pythia_4class_acc: 0.7854
    pythia_ci_95:
    - 0.7795
    - 0.7911
    pythia_d1v2_auc: 0.8681
    delta_pp: -11.2
- exp_id: second_seed_replication_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    4class_acc: 0.7715
    ci_95:
    - 0.764
    - 0.7815
    d1v2_auc: 0.8531
    delta_vs_baseline: -0.0105
    baseline_acc: 0.782
    top_features:
    - var_surprisal
    - p90_ppl
    - mean_ppl
    - var_ppl
    - p75_ppl
    per_class_recall:
      d0: 0.99
      d1: 0.816
      d2: 0.586
      d3: 0.694
    fold_accuracies:
    - 0.77
    - 0.77
    - 0.79
    - 0.7675
    - 0.76
- exp_id: mixed_depth_corpus_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    mixed_overall_acc: 0.855
    balanced_overall_acc: 0.7814
    delta_overall_pp: 7.36
    mixed_macro_recall: 0.7652
    balanced_macro_recall: 0.7814
    delta_macro_recall_pp: -1.62
    per_class_recall_delta:
      d0: -0.68
      d1: -2.43
      d2: -1.12
      d3: -2.24
    max_recall_delta_pp: 2.43
- exp_id: reference_free_baseline_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    4class_acc: 0.5368
    ci_95:
    - 0.5336
    - 0.5401
    d1v2_auc: 0.6252
    full_19_acc: 0.7877
    delta_pp: -25.09
    recall_d0: 0.8572
    recall_d1: 0.397
    recall_d2: 0.3176
    recall_d3: 0.5756
- exp_id: ensemble_reference_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ensemble_4class_acc: 0.7365
    ensemble_ci_95:
    - 0.7258
    - 0.7471
    pythia_acc: 0.7857
    olmo_acc: 0.7425
    gpt2xl_acc: 0.7005
    delta_vs_gpt2xl: 3.6
    delta_vs_pythia: -4.9
- exp_id: gen_length_ablation_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    acc_128: 0.6835
    ci_128:
    - 0.6765
    - 0.6905
    acc_256: 0.738
    ci_256:
    - 0.7248
    - 0.7512
    acc_512: 0.7782
    ci_512:
    - 0.768
    - 0.7885
    d1v2_auc_128: 0.7543
    d1v2_auc_256: 0.8198
    d1v2_auc_512: 0.8683
    spread_pp: 9.47
    delta_128v256_pp: -5.45
    delta_512v256_pp: 4.02
- exp_id: cross_seed_transfer_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    within_seed42_cv: 0.7868
    within_seed43_cv: 0.7745
    within_seed_avg: 0.7807
    train42_test43: 0.7785
    train43_test42: 0.7568
    cross_seed_avg: 0.7676
    delta_pp: -1.3

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
  "promptId": "758f0560-3ee1-42c7-b531-359934fe10a4",
  "type": "user",
  "uuid": "925879b0-55fa-4daf-830c-185e35aaf1c7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T08:19:14.702Z_

```json
{
  "parentUuid": "925879b0-55fa-4daf-830c-185e35aaf1c7",
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
  "uuid": "9b3d92fe-8ba1-4102-8838-bb887a28c9cf",
  "timestamp": "2026-05-17T08:19:14.702Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T08:19:14.702Z_

```json
{
  "parentUuid": "9b3d92fe-8ba1-4102-8838-bb887a28c9cf",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a542a334-ca45-4b3f-8760-5b7b529025b0",
  "timestamp": "2026-05-17T08:19:14.702Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：13B 信号严重衰减或特征结构被破坏；prompted generation 信号接近无效；scale/ecological validity 核心假设失败，需完全 reframe 为 controlled-setting atlas paper 核心假设：['13B clean FP16 accuracy…",
  "leafUuid": "a542a334-ca45-4b3f-8760-5b7b529025b0",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Ordinal depth estimation under scale and generation mode boundaries",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778"
}
```

---

### Assistant

_source line 8 · 2026-05-17T08:19:17.702Z_

I'll analyze the experiment plan and generate detailed worst-tier predictions for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a542a334-ca45-4b3f-8760-5b7b529025b0",
  "isSidechain": false,
  "requestId": "req_011Cb7p8n8JxuKB6XvmfEejr",
  "type": "assistant",
  "uuid": "27b5e4b6-b58d-4dff-8d26-716ae969938f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rogerwNgaPmphc5Cx1hHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 49007,
      "cache_read_input_tokens": 11841,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 49007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 132,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 49007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 49007
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

_source line 9 · 2026-05-17T08:19:19.547Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ayqoo88yfbttcxRPQfp7CD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27b5e4b6-b58d-4dff-8d26-716ae969938f",
  "isSidechain": false,
  "requestId": "req_011Cb7p8n8JxuKB6XvmfEejr",
  "type": "assistant",
  "uuid": "bdc1dd9e-025a-4665-a288-ac6f3984c483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rogerwNgaPmphc5Cx1hHd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 49007,
      "cache_read_input_tokens": 11841,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 49007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 132,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 49007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 49007
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

_source line 10 · 2026-05-17T08:19:19.557Z_

<details><summary>↩ Tool result · `toolu_01Ayqoo88yfbttcxRPQfp7CD`</summary>

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
  "parentUuid": "bdc1dd9e-025a-4665-a288-ac6f3984c483",
  "isSidechain": false,
  "promptId": "758f0560-3ee1-42c7-b531-359934fe10a4",
  "type": "user",
  "uuid": "677768c8-b694-43db-b722-fa125bbb426e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "bdc1dd9e-025a-4665-a288-ac6f3984c483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-17T08:20:35.086Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed worst-tier predictions for the three planned experiments in the experiment_plan:

1. **plan_014** - 13B clean FP16 scale validation (Qwen2.5-14B, nucleus, d0-d3) - status: planned
2. **plan_015** - Wild-data calibration on RedPajama/Dolma - status: planned
3. **plan_016** - Prompted generation ecological validity (GPT-2 XL, topic-seeded d0-d3) - status: planned


4. **plan_017** - Cross-strategy two-stage pipeline (strategy classifier + conditioned depth) - status: planned

I'm checking which experiments are actually marked as planned in the experiment_plan. Plan_010 was planned but got cancelled due to DCOL v6 failure, so I should exclude that and focus on the four active planned experiments.

Now I'm defining what worst-tier predictions look like for these experiments—essentially the failure modes where the 13B signal gets severely degraded, prompted generation becomes ineffective, or the core assumptions about scale and ecological validity break down. I'm looking at the specific metric ranges that would indicate this worst-case scenario across accuracy, AUC, and feature preservation metrics.

To calibrate these ranges, I'm checking against existing performance data from smaller models in the 1-1.5B range, where I can see the actual spread from best performers like GPT-2 XL down to weaker configurations, which helps me ground what "worst tier" actually means in practice. 0.94 (GPT-2 XL temp09)

Cross-scale reference:
- Qwen 7B (QLoRA): 60.1% 4-class acc, U-shape AUC pattern
- Llama3 8B IT: 70.2% 4-class acc, EDD=4, monotonic AUC
- Llama3 8B base: 59.9% 4-class acc, EDD=2, U-shape

Cross-strategy:
- Mean: 59.1%
- Strategy clf (two_stage_strategy_pipeline_001): 57.5% mean acc
- Predicted two-stage: 70.6% mean
- Naive pooled: 72.0%
- Oracle two-stage: 78.4%

Now I need to generate worst-tier predictions. For the Qwen2.5-14B model, scaling up from the 7B variant likely won't help much since the larger model's output distribution diverges significantly from what the Pythia reference can capture. I'm expecting the 4-class accuracy to drop to around 52-58%, with d1v2 AUC in the 0.58-0.65 range and a broken feature structure where the perplexity and surprise metrics fall out of the top predictors. The effective decision depth should be minimal at around 1-2 when EDD equals 0.75, possibly with residual U-shape artifacts. The wild-data calibration approach is deferred as a secondary priority.

For prompted generation, the fundamental shift in how perplexity distributes when using topic-seeded text means the signal gets heavily attenuated. I'm looking at 4-class accuracy dropping to 0.45-0.55 and d1v2 AUC around 0.55-0.60, with signal retention compared to BOS-only generation falling to just 40-60%. The two-stage pipeline doesn't show promise either—the strategy classifier stays weak at 50-60%, and the predicted two-stage approach underperforms the naive pooled baseline, so there's no practical value in pursuing that direction.

Now I'm reviewing the YAML output more carefully. Plan_010 shows "status: planned" but the notes indicate it was cancelled, so I should skip it. Plan_015 is marked for deferral to the AAAI window with lower current priority, but it's still planned so I'll include it. For plan_017, there's already a completed experiment with two_stage_strategy_pipeline_001, but the plan itself is marked as planned and addresses the cross-strategy accuracy issue, though it's primarily a CPU task.

Looking at the registry data, two_stage_strategy_pipeline_001 shows results with strategy_classification at 0.575 mean accuracy and predicted_two_stage at 0.706, which is actually worse than the naive_pooled baseline at 0.72. The plan status hasn't been updated despite the experiment running, so I'll treat all "planned" status items as needing detailed predictions, using the existing two_stage data as a baseline reference point.

Since the user asked for detailed data on each planned experiment, I need to cover plan_010 (though cancelled), plan_014, plan_015, plan_016, and plan_017. For plan_010, I should probably note it's cancelled rather than generate predictions.

Now I'm working through the worst-tier predictions systematically. For plan_014 with the 13B clean FP16 setup, the worst-case scenario assumes accuracy drops below 62%, the feature importance structure gets corrupted, or we see U-shaped artifacts. The key issue is that Pythia-160M as a reference model has much simpler vocabulary distribution compared to what Qwen2.5-14B would generate, so scaling up introduces significant complexity that could degrade performance. scores may be near-random noise for discriminating depths of a 14B model's output. Qwen 7B already showed U-shape behavior at 60.1%, and scaling to 14B could amplify this since the model has much more capacity—early LoRA iterations barely shift the weights. The feature landscape also changes fundamentally at this scale, so p90_ppl and var_surprisal may drop out of the top features entirely.

I'm expecting 4class_acc around 0.55, d1v2_auc near 0.62, and d2v3_auc around 0.58, with d0v1_auc weakening to 0.95 instead of the 0.99+ we saw at smaller scales. EDD should be 1-2 at T=0.75, and I'm anticipating a similar U-shape artifact to what we observed with Qwen 7B.

Now looking at the worst-case scenario with RedPajama and Dolma—these massive web crawl datasets introduce substantial noise and domain shift that could push FPR above 25%, making real-world deployment risky. Cross-model calibration becomes inconsistent, and classifiers trained on these datasets lose reliability.

For prompted generation with GPT-2 XL, the topic prompts constrain the generation distribution so tightly that depth features lose their discriminative power. The prompt prefix dominates the perplexity signal and masks the distributional shifts that depth creates, while LoRA fine-tuning can't cleanly shift the distribution when the prompt anchors it in place. I'm expecting 4class_acc around 0.48 and d1v2_auc near 0.57, both well below what we'd need for practical use.

The cross-strategy two-stage pipeline doesn't help much either—strategy classification maxes out around 55-60% accuracy, and the predicted two-stage pipeline underperforms naive pooling by about 4 percentage points. The oracle version shows there's potential at 78%, but the gap between what we can actually predict and what simple pooling achieves suggests this approach adds complexity without real benefit.

Actually, I'm realizing the experiment two_stage_strategy_pipeline_001 might already be completed with results showing 57.5% strategy classification and 70.6% predicted accuracy versus 72% for naive pooling. If that's the case, those numbers already fall within the worst-tier range I was projecting, so the plan status might just not have been updated yet.

Now I need to structure the YAML output properly, covering the four worst-tier experiments: the 13B model variant, wild-data approach, prompted generation, and the two-stage pipeline. I should also note plan_010 even though it's cancelled, then write detailed rationales for each result.

Generating YAML with result explanations...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "677768c8-b694-43db-b722-fa125bbb426e",
  "isSidechain": false,
  "requestId": "req_011Cb7p99HnWHy89ebUhG8JM",
  "type": "assistant",
  "uuid": "c3f8a287-6635-450b-af97-99d931f5e99e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTh26HQC4oWjzahSPoRZ2G",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 304,
      "cache_read_input_tokens": 60848,
      "output_tokens": 13528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 304,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13528,
          "cache_read_input_tokens": 60848,
          "cache_creation_input_tokens": 304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 304
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

_source line 12 · 2026-05-17T08:24:04.659Z_

```yaml
tier: worst
narrative_guidance: >
  核心 reframe：从 "robust framework for depth estimation" 转为 "first systematic
  characterization of recursive depth phenomena and the boundary conditions of
  feature-based detection." Atlas (Claim 2) 升为唯一 primary contribution。Claim 1
  重写为 bounded conclusion："ordinal depth estimation is feasible and accurate under
  controlled conditions (1–1.5B, BOS-seeded, within-strategy, 70–85%); signal
  significantly attenuates at larger scales and under prompted generation, indicating
  that current statistical-feature approaches capture a real but fragile signal."
  13B 弱结果 + prompted 弱结果写入主体 Section 6 "Boundary Conditions of the Depth
  Signal"，与 EDD 分析并列。Characterizing these boundaries IS the contribution。
  Claim 3 降为 Discussion future work。论文定位：task definition + controlled-setting
  empirical atlas + boundary characterization。EMNLP "New Missions" track 仍首选，
  但论文类型从 "framework paper" 退到 "diagnostic/benchmark paper"。

imagined_experiments:
  # ============================================================
  # plan_010 — DCOL component ablation (CANCELLED)
  # ============================================================
  - name: "DCOL component ablation"
    plan_id: "plan_010"
    description: "DCOL v6 (RoBERTa-large) 失败后前置条件 plan_004 未满足，此实验已取消。"
    expected_results:
      status: cancelled
      reason: "DCOL v6 conclusion=negative (test_acc=64.5% vs RF baseline 78.2%, -13.7pp)，无可消融的成功模型"
    result_rationale: >
      DCOL v1-v6 全线失败，最好结果仅 64.5%（RoBERTa-large v6），远低于 RF baseline。
      contrastive ordinal learning 在文本深度估计上存在固有困难：(1) 文本嵌入空间的深度梯度
      远弱于 19 维统计特征空间中的梯度，(2) 端到端学习需要从原始文本中同时学习特征提取和序数
      排列，数据量不足以支撑。消融无意义——没有成功的完整模型可以消融。
    tables: []
    figures_description: []
    analysis: >
      plan_010 取消对论文无影响。DCOL 失败本身写入 negative analysis section（约 0.5 页），
      论述"为何 contrastive ordinal learning 在此 task 上比 feature engineering 差"。
      这反而强化 Atlas（Claim 2）的 primary 定位——统计特征方法的优越性不是因为缺乏更好方法，
      而是因为任务特性（稀疏信号、微弱梯度）使端到端学习困难。

  # ============================================================
  # plan_014 — 13B clean FP16 scale validation
  # ============================================================
  - name: "13B clean FP16 scale validation (Qwen2.5-14B)"
    plan_id: "plan_014"
    description: >
      Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，nucleus p=0.95 decoding，
      d0-d3 递归链 + Pythia-160M reference model 19 特征提取 + RF/LR 分类。
      验证 depth signal 在主流模型规模上是否持续。
    expected_results:
      four_class_acc_rf: 0.55
      four_class_acc_rf_ci: [0.53, 0.57]
      four_class_acc_lr: 0.51
      d0v1_auc: 0.96
      d1v2_auc: 0.62
      d2v3_auc: 0.56
      d1v3_auc: 0.81
      three_class_acc: 0.44
      three_class_acc_ci: [0.42, 0.46]
      edd_at_075: 1
      edd_at_070: 2
      feature_top2_in_top4: false
      top_features_predicted:
        - mean_ppl
        - p75_ppl
        - type_token_ratio
        - rep_3gram
        - p90_ppl
      u_shape_artifact: true
      u_shape_pattern: "d1v2=0.62, d2v3=0.56 (trough), possible d2v3 < d3v4 recovery"
      finetune_loss_d0: 1.85
      finetune_loss_d1: 1.52
      finetune_loss_d2: 1.38
      finetune_loss_d3: 1.31
      loss_convergence_gap_d1_d2: 0.14
      per_class_recall:
        d0: 0.93
        d1: 0.48
        d2: 0.32
        d3: 0.47
      acc_vs_best_1_5b_retention_pct: 64.4
    result_rationale: >
      Worst tier 核心机制：Pythia-160M reference model 对 14B 输出的 perplexity 特征
      区分力严重不足。14B 模型的词汇分布远比 1-1.5B 复杂——Pythia-160M 对所有 14B 输出
      都给出极高 perplexity（因为 14B 的选词模式超出 160M 的建模能力），导致 p90_ppl 和
      var_surprisal 的深度梯度被压缩到一个高 perplexity plateau 上，信噪比骤降。

      具体机制链：(1) Qwen2.5-14B 的 BPE 词表（151K tokens）与 Pythia 词表（50K tokens）
      不匹配，Pythia 需要更多 subword tokens 来编码 14B 的输出，系统性地膨胀 perplexity
      baseline；(2) 14B 模型容量大，LoRA rank=16 的微调在每个深度迭代中只轻微扰动模型——
      finetune loss 序列 1.85→1.52→1.38→1.31 的衰减斜率远小于 1-1.5B 的 2.2→1.4→1.0，
      说明 14B 的 LoRA 适配器修改的分布偏移量远小于小模型；(3) 由于每步分布偏移小，
      Pythia 测量到的深度间特征差异在噪声水平附近——d1v2 AUC 仅 0.62，d2v3 仅 0.56。

      U-shape artifact 的来源：与 Qwen 7B（cross_scale_qwen7b_001, U-shape confirmed）
      同源。d2v3 出现 trough 是因为 depth-2 和 depth-3 的 LoRA 叠加效应使模型在某些
      高频 token 上出现非单调的 logit 变化，Pythia 的 perplexity 在这些位置产生混淆信号。
      Llama3 8B base 也出现了 U-shape（d2v3=0.68, d3v4=0.73 recovery），进一步支持
      这是跨规模特征迁移的系统性问题而非 Qwen 特有。

      Feature importance 结构破坏：p90_ppl 和 var_surprisal 不再占据 top-2，因为在高
      perplexity plateau 上，尾部统计量的信噪比下降最快。mean_ppl 和 p75_ppl 因为
      信号更平滑反而排名上升，但整体区分力弱。

      EDD=1（T=0.75）意味着只有 d0v1 可靠区分，即 13B 条件下 depth estimation 实质
      退化为 binary real-vs-synthetic detection。
    tables:
      - name: "Table S1: 13B vs 1-1.5B 4-class accuracy comparison"
        columns: [model, scale, 4class_acc_rf, d1v2_auc, d2v3_auc, edd_075]
        rows:
          - [Pythia-1.4B, 1.4B, 0.782, 0.861, 0.801, 3]
          - [OLMo-1B, 1B, 0.788, 0.867, 0.812, 3]
          - [GPT-2 XL, 1.5B, 0.833, 0.913, 0.883, 3]
          - [Qwen2.5-14B, 14B, 0.55, 0.62, 0.56, 1]
          - [Qwen-7B (QLoRA ref), 7B, 0.601, 0.729, 0.709, ">5 (U-shape)"]
      - name: "Table S2: 13B feature importance vs 1-1.5B consensus"
        columns: [rank, "1-1.5B consensus", "13B predicted"]
        rows:
          - [1, "p90_ppl / var_surprisal", mean_ppl]
          - [2, "var_surprisal / p90_ppl", p75_ppl]
          - [3, "mean_ppl / p75_ppl", type_token_ratio]
          - [4, "mean_surprisal", rep_3gram]
          - [5, "p75_ppl / mean_ppl", p90_ppl]
    figures_description:
      - "Fig S1: AUC decay curve 1-1.5B vs 13B — 三条 1-1.5B 曲线呈 monotonic decay（d0v1≈0.99→d2v3≈0.80-0.88），13B 曲线在显著更低位置且可能呈 U-shape（d1v2=0.62, d2v3=0.56, 可能 d3v4 轻微回升）。EDD threshold lines at T=0.70/0.75 将 13B 的 EDD 压到 1-2。"
      - "Fig S2: Finetune loss curve comparison — 1-1.5B 曲线陡峭（2.2→1.0 across 3 depths），13B 曲线平坦（1.85→1.31），说明 LoRA 在 14B 上的 per-depth distributional shift 远小于 1-1.5B。"
    analysis: >
      13B 结果证实 worst tier 核心假设：Pythia reference model 对大规模模型输出的
      perplexity 特征区分力本质受限。55% 4-class accuracy 虽然显著高于 chance（25%），
      但相比 1-1.5B 的 70-85% 有 >20pp 衰减。更关键的是 EDD=1，意味着 ordinal depth
      estimation 在 13B 条件下实质退化为 binary detection。

      叙事处理：此结果不写入 Limitations，而是写入 Section 6 "Boundary Conditions"
      的 Scale Dimension 子节。结论："feature-based depth estimation captures a real
      signal at 14B scale (55% vs 25% chance, p<0.001), but the signal is severely
      attenuated compared to 1-1.5B, with EDD collapsing from 3 to 1. The primary
      bottleneck is the cross-scale perplexity measurement gap: a 160M reference
      model's perplexity landscape compresses the depth gradient of 14B outputs."

      这为 future work 指出明确方向：(1) scale-matched reference models（用 7B 作为
      14B 的 reference），(2) reference-free features（但 reference_free_baseline_001
      已证明 reference-free 在 1-1.5B 上就差 25pp），(3) 直接使用 14B 自身的 internal
      representations 而非外部 perplexity。

  # ============================================================
  # plan_015 — Wild-data calibration on RedPajama/Dolma
  # ============================================================
  - name: "Wild-data calibration on RedPajama/Dolma"
    plan_id: "plan_015"
    description: >
      在 RedPajama 和 Dolma 真实 web 数据上评估训练好的 depth classifiers 的 calibration
      和 false positive rate。验证 controlled-setting 训练的分类器在 wild data 上的可靠性。
    expected_results:
      redpajama_n_passages: 5000
      redpajama_d0_pct: 72.0
      redpajama_fpr_pct: 28.0
      redpajama_d1_pct: 18.5
      redpajama_d2_pct: 5.8
      redpajama_d3_pct: 3.7
      dolma_n_passages: 5000
      dolma_d0_pct: 76.5
      dolma_fpr_pct: 23.5
      dolma_d1_pct: 16.2
      dolma_d2_pct: 4.3
      dolma_d3_pct: 3.0
      cross_model_fpr_range_pp: 18
      mean_p_d0_redpajama: 0.68
      mean_p_d0_dolma: 0.72
      pythia_fpr: 28.0
      gpt2xl_fpr: 30.5
      olmo_fpr: 12.0
      calibration_brier_score: 0.28
    result_rationale: >
      Worst tier 预期 FPR 在 23-30% 范围，与已有 wild data 结果一致但偏高端。

      机制分析：(1) RedPajama 包含大量 CommonCrawl 数据，其中 template content、
      SEO 文本、自动生成的产品描述占比显著。这些文本的统计特征（高 rep_3gram/rep_4gram、
      低 type_token_ratio、异常 p90_ppl）与递归生成文本在特征空间中重叠，导致误分类。
      已有证据：C4 FPR=20.2%（Pythia）、FineWeb FPR=19.5%，但 RedPajama 的
      CommonCrawl 质量过滤比 C4 更宽松，预期 FPR 更高。

      (2) Dolma 由 AI2 策划，含 CommonCrawl + Wikipedia + Books + GitHub + arXiv 等
      多域混合。Wikipedia/Books 子集 FPR 极低（参考 WikiText 0% FPR），但 CommonCrawl
      子集拉高整体 FPR。混合后预期 FPR ~23.5%。

      (3) Cross-model FPR 一致性差（range=18pp）是因为不同 reference model 的 perplexity
      landscape 对 web 噪声的敏感度不同——OLMo 在 Dolma 上训练（域匹配），FPR 较低（参考
      olmo_calibration_001 C4 FPR=4.7%），而 Pythia/GPT-2 XL 域失配导致 FPR 飙升。

      (4) Calibration 差（Brier score 0.28）说明分类器的置信度在 wild data 上不可靠，
      限制了任何基于预测概率的 graduated curation 方案。

      这些结果证实：controlled-setting 训练的分类器在 wild data 部署面临严重的 domain
      shift 问题，FPR 的高方差（12-30% 取决于 reference model）使得实际部署需要
      domain-specific calibration，大幅限制了 Claim 1 的 practical applicability。
    tables:
      - name: "Table S3: Wild-data FPR across datasets and reference models"
        columns: [dataset, pythia_fpr, gpt2xl_fpr, olmo_fpr, mean_fpr]
        rows:
          - [WikiText-103, 0.0, 1.4, 1.5, 1.0]
          - [OpenWebText, 0.9, 1.4, 2.8, 1.7]
          - [C4, 20.2, 22.4, 4.7, 15.8]
          - [FineWeb, 19.5, "~20", "~5", "~15"]
          - [RedPajama (predicted), 28.0, 30.5, 12.0, 23.5]
          - [Dolma (predicted), 25.0, 27.0, 10.0, 20.7]
    figures_description:
      - "Fig S3: FPR vs dataset quality gradient — X 轴从 WikiText（高编辑质量）到 RedPajama（低质量 web crawl），Y 轴为 FPR。三条 reference model 线均呈单调上升，但 OLMo 曲线斜率显著低于 Pythia/GPT-2 XL（域匹配效应）。"
    analysis: >
      Wild-data 结果在 worst tier 下强化 "boundary conditions" 叙事的第四维度：
      domain shift。Controlled-setting 分类器在 editorial-quality 数据上表现优异
      （WikiText FPR<2%），但在 web-crawl 数据上 FPR 高达 23-30%，且 reference
      model 依赖性强。

      这不会进入论文主体（plan_015 延后到 AAAI），但如果包含，应写入 Section 6
      "Boundary Conditions" 的 Domain Dimension：depth signal 的第四个衰减边界。
      与 scale（>1.5B attenuation）、generation mode（prompted attenuation）、
      depth（EDD=4）并列。

      对 EMNLP 投稿的影响：不纳入此实验是正确决策。Wild-data calibration 的复杂度
      足以支撑一篇独立 follow-up 论文，强行塞入当前论文会分散 Atlas 核心贡献的注意力。

  # ============================================================
  # plan_016 — Prompted generation ecological validity
  # ============================================================
  - name: "Prompted generation ecological validity (GPT-2 XL, topic-seeded)"
    plan_id: "plan_016"
    description: >
      GPT-2 XL nucleus p=0.95，用 topic prompt 前缀（"The following article discusses..."等）
      生成 d0，LoRA fine-tune 后生成 d1-d3，提取 19 特征 + RF 分类。验证 depth signal
      是否为 BOS-seeded 无条件生成的 artifact。
    expected_results:
      four_class_acc_rf: 0.50
      four_class_acc_rf_ci: [0.48, 0.52]
      four_class_acc_lr: 0.46
      d0v1_auc: 0.93
      d1v2_auc: 0.58
      d2v3_auc: 0.54
      d1v3_auc: 0.77
      three_class_acc: 0.40
      three_class_acc_ci: [0.38, 0.42]
      acc_retention_vs_bos_pct: 58.6
      acc_retention_vs_bos_pct_range: [55, 62]
      edd_at_075: 1
      edd_at_070: 1
      feature_top5_predicted:
        - p90_ppl
        - var_surprisal
        - mean_ppl
        - mean_surprisal
        - p75_ppl
      feature_importance_structure_preserved: true
      feature_importance_magnitude_attenuation_pct: 35
      per_class_recall:
        d0: 0.88
        d1: 0.42
        d2: 0.28
        d3: 0.42
      bos_reference_acc: 0.854
      prompted_acc: 0.50
      delta_pp: -35.4
      finetune_loss_d0: 2.10
      finetune_loss_d1: 1.65
      finetune_loss_d2: 1.35
      finetune_loss_d3: 1.15
    result_rationale: >
      Worst tier 核心机制：prompted generation 从根本上改变了 perplexity 特征的信号
      结构，使 depth gradient 严重衰减。

      具体机制链：

      (1) Prompt anchoring effect：topic prompt 前缀（"The following article discusses
      climate change..."等）约束了生成文本的词汇分布和主题范围。BOS-seeded 生成是
      完全无条件的——模型从空白开始，每个深度的分布偏移完整体现在输出中。Prompted
      生成中，prompt 提供了一个 distributional anchor，LoRA fine-tuning 在每个深度
      迭代中需要同时 (a) 适配 prompt-conditioned 分布 和 (b) 引入深度相关的偏移。
      这两个目标部分冲突——prompt anchor 限制了可偏移的分布空间。

      (2) Perplexity floor effect：Pythia-160M 对 prompted text 的 perplexity 整体
      更低且更集中（因为 prompt 提供了上下文，Pythia 的下文预测更准），导致 p90_ppl
      和 var_surprisal 的动态范围被压缩。具体来说，BOS-seeded d0 的 p90_ppl ≈ 180-220，
      但 prompted d0 可能只有 120-150（prompt 提供了 context），深度梯度的绝对变化量
      从 ~80 points 压缩到 ~30 points，信噪比下降约 60%。

      (3) Feature importance 结构保留但幅度衰减：p90_ppl 和 var_surprisal 仍在 top-5
      （不同于 13B 的结构性破坏），因为 prompted generation 不改变哪些特征有信息量，
      只是缩小了信息量的幅度。这是 worst tier 中一个"不是最差"的维度——prompted 的
      问题是信号衰减而非信号结构破坏。

      (4) d1v2 AUC 0.58 的来源：depth-1 和 depth-2 的 prompted 输出在 Pythia 视角
      下几乎不可区分，因为 LoRA 在 prompted 条件下的 per-depth 分布偏移量更小（loss
      convergence gap d1-d2 仅 0.30 vs BOS 模式下的 0.84）。prompt 的 constraint
      使得连续深度的输出分布差异主要体现在远离 prompt 的 token 位置，而特征提取
      使用固定 truncation length（498 tokens），可能截断了信号最强的尾部区域。

      (5) 58.6% retention 意味着 prompted 条件下约 41% 的信号丢失。GPT-2 XL 是
      1-1.5B 中信号最强的（85.4%），如果它在 prompted 模式下降到 50%，那么 Pythia
      和 OLMo 在 prompted 模式下可能只有 40-45%，接近 chance。这使得 "depth signal
      persists under prompted generation" 的 Claim 1 表述不可持续。

      (6) EDD=1（T=0.75 和 T=0.70）意味着在 prompted 条件下只有 d0v1 boundary
      可靠，depth estimation 退化为 binary real-vs-synthetic detection，与 13B
      worst tier 的结论一致。
    tables:
      - name: "Table S4: Prompted vs BOS-seeded accuracy (GPT-2 XL nucleus)"
        columns: [condition, 4class_acc, d1v2_auc, d2v3_auc, edd_075, retention_pct]
        rows:
          - [BOS-seeded, 0.854, 0.937, 0.882, 3, 100]
          - [Prompted (worst), 0.50, 0.58, 0.54, 1, 58.6]
          - [Delta, -0.354, -0.357, -0.342, -2, null]
      - name: "Table S5: Prompted per-class recall vs BOS"
        columns: [depth, bos_recall, prompted_recall, delta]
        rows:
          - [d0, 0.996, 0.88, -0.116]
          - [d1, 0.816, 0.42, -0.396]
          - [d2, 0.596, 0.28, -0.316]
          - [d3, 0.754, 0.42, -0.334]
      - name: "Table S6: Finetune loss comparison"
        columns: [depth, bos_loss, prompted_loss, delta]
        rows:
          - [d0, 2.55, 2.10, -0.45]
          - [d1, 1.72, 1.65, -0.07]
          - [d2, 1.29, 1.35, +0.06]
          - [d3, null, 1.15, null]
    figures_description:
      - "Fig S4: Feature distribution violin plots (BOS vs Prompted) — p90_ppl 和 var_surprisal 的 4-depth violin plots 并排比较。BOS 版本显示清晰的深度梯度（d0 宽高分布→d3 窄低分布），Prompted 版本整体压缩且深度间重叠严重，尤其 d1/d2 几乎完全重叠。"
      - "Fig S5: AUC decay curve overlay — BOS 曲线（smooth monotonic decay from 0.99 to 0.88）vs Prompted 曲线（steep drop, d1v2=0.58, d2v3=0.54），两者在 d0v1 接近但迅速分离。EDD threshold line 显示 prompted EDD=1 vs BOS EDD=3。"
    analysis: >
      Prompted generation 在 worst tier 下证实了 ecological validity 核心假设失败：
      depth signal 高度依赖 BOS-seeded 无条件生成模式。50% accuracy（vs BOS 85.4%）
      意味着 prompted 条件下分类器只比 chance 高 25pp，而 BOS 条件下高 60pp——
      超过 60% 的相对信号在 prompted 模式下消失。

      叙事处理：此结果写入 Section 6 "Boundary Conditions of the Depth Signal" 的
      Generation Mode Dimension。关键措辞："The depth signal is substantially attenuated
      under prompted (topic-seeded) generation — 4-class accuracy drops from 85.4%
      (BOS-seeded) to 50.0% (prompted), with EDD collapsing from 3 to 1. This indicates
      that a significant portion of the BOS-seeded depth signal arises from the
      unconstrained distributional freedom of unconditional generation, which LoRA
      fine-tuning can fully exploit at each depth iteration. Prompted generation
      constrains this freedom, compressing the per-depth distributional shift and
      reducing the feature-space gradient available to classifiers."

      好消息：feature importance 结构保留（p90_ppl/var_surprisal 仍 top-2），说明
      信号的性质不变（同类特征仍最有信息量），只是幅度衰减。这支持"信号是真实的但
      脆弱的"叙事，而非"信号是 artifact"。

      对论文定位的影响：Claim 1 必须退到 "feasible under controlled conditions"，
      ecological validity 成为一个明确的 boundary condition 而非已解决的问题。
      这与 "diagnostic/boundary characterization paper" 定位一致。

  # ============================================================
  # plan_017 — Cross-strategy two-stage pipeline
  # ============================================================
  - name: "Cross-strategy two-stage pipeline (strategy clf + conditioned depth)"
    plan_id: "plan_017"
    description: >
      两阶段方案：(a) 19 特征 → 3-class strategy classifier (nucleus/temp/topk)，
      (b) 识别策略后用策略专属 RF 估深度。解决 59.1% 跨策略准确率问题。
    expected_results:
      strategy_clf_overall_acc: 0.575
      strategy_clf_per_model:
        pythia: 0.523
        olmo: 0.548
        gpt2xl: 0.654
      strategy_clf_per_strategy_recall:
        nucleus: 0.662
        temp09: 0.467
        topk50: 0.597
      predicted_two_stage_acc:
        pythia: 0.693
        olmo: 0.695
        gpt2xl: 0.730
        mean: 0.706
      naive_pooled_acc:
        pythia: 0.709
        olmo: 0.712
        gpt2xl: 0.739
        mean: 0.720
      oracle_two_stage_acc:
        pythia: 0.746
        olmo: 0.785
        gpt2xl: 0.820
        mean: 0.784
      within_strategy_ref_acc:
        pythia: 0.745
        olmo: 0.784
        gpt2xl: 0.816
        mean: 0.782
      predicted_vs_naive_gap_pp: -1.4
      oracle_vs_within_gap_pp: 0.2
      strategy_clf_bottleneck: true
      temp09_clf_recall: 0.467
      temp09_misclass_as_nucleus_pct: 38
    result_rationale: >
      Worst tier 核心问题：strategy classifier 准确率仅 57.5%（chance=33.3%），
      远低于预期的 >90%，导致 predicted two-stage（70.6%）反而低于 naive pooled
      （72.0%），pipeline 无实际价值。

      机制分析：

      (1) 策略不可分性的根因：19 个 perplexity/surprisal 统计特征的设计目的是
      捕捉深度信号，不是策略信号。深度梯度（across depths within a strategy）远大于
      策略梯度（across strategies within a depth）——这恰恰是深度估计成功的原因，
      但也是策略分类失败的原因。三种策略在 depth-0 上使用相同 base model 生成，
      特征完全相同；depth-1+ 的策略差异主要体现在 token-level 分布形状（nucleus
      截断 vs temperature 缩放 vs topk 截断），而 19 个 summary statistics
      将 500 tokens 的 token-level 信息压缩为单个数值，丢失了大部分策略判别信息。

      (2) Temperature 最难分类（recall 46.7%）：temperature sampling 的均匀 logit
      缩放不改变 token rank order，只改变 softmax 后的概率分布平滑度。在 Pythia
      reference model 的 perplexity 视角下，这种平滑度变化被 mean_ppl 和 p90_ppl
      部分吸收但不够 distinctive——temperature 的很多样本在特征空间中落入 nucleus
      和 topk 的重叠区域。38% 的 temp09 样本被误分为 nucleus，因为两者的 perplexity
      尾部分布高度相似（nucleus 截断概率 < 0.05 的 tokens，temperature 降低但保留
      所有 tokens 的概率——在 Pythia 眼中，两者都产生 "somewhat surprising" 的输出）。

      (3) Predicted < Naive 的数学原因：设 strategy clf error rate = e ≈ 0.425。
      误分类的样本被送入错误的 strategy-conditioned depth classifier，其性能等于
      cross-strategy LOO 水平（~59%）。正确分类的样本使用 within-strategy classifier
      （~78%）。加权平均：0.575 × 0.78 + 0.425 × 0.59 = 0.449 + 0.251 = 0.700 ≈ 70.6%。
      Naive pooled（全部数据 train single RF）≈ 72%，因为 pooling 虽然模糊了策略边界，
      但避免了 misrouting 的惩罚。当 strategy clf acc < ~75% 时，two-stage 数学上
      必然劣于 naive pooled。

      (4) Oracle vs within-strategy gap 仅 0.2pp（78.4% vs 78.2%），完美验证了
      理论：如果策略已知，conditioned depth estimation 可以完全恢复 within-strategy
      性能。但这是 oracle 条件——现实中策略未知，pipeline 的瓶颈完全在策略识别环节。

      (5) Worst tier 结论：strategy classification 准确率无法超过 60%（因为 19 个
      特征的设计先天不适合策略判别），predicted two-stage 始终 ≤ naive pooled，
      pipeline 无实际部署价值。Claim 3 不具备作为独立 contribution 的条件。
    tables:
      - name: "Table S7: Two-stage pipeline accuracy decomposition"
        columns: [condition, pythia, olmo, gpt2xl, mean]
        rows:
          - [Cross-strategy LOO (baseline), 0.612, 0.595, 0.566, 0.591]
          - [Naive pooled, 0.709, 0.712, 0.739, 0.720]
          - [Predicted two-stage, 0.693, 0.695, 0.730, 0.706]
          - [Oracle two-stage, 0.746, 0.785, 0.820, 0.784]
          - [Within-strategy (ceiling), 0.745, 0.784, 0.816, 0.782]
      - name: "Table S8: Strategy classification confusion matrix (3-model mean)"
        columns: [true/predicted, nucleus, temp09, topk50]
        rows:
          - [nucleus, 0.662, 0.182, 0.156]
          - [temp09, 0.380, 0.467, 0.153]
          - [topk50, 0.163, 0.240, 0.597]
    figures_description:
      - "Fig S6: Strategy classification accuracy vs depth estimation gain — 横轴 strategy clf acc (40-100%)，纵轴 depth estimation acc。两条线：predicted two-stage（从 ~59% at clf=33% 上升到 ~78% at clf=100%）和 naive pooled（水平线 72%）。交叉点在 clf≈75%，标注 'breakeven point'。当前 clf=57.5% 明确低于 breakeven。"
    analysis: >
      Two-stage pipeline 在 worst tier 下证实了 Claim 3 的失败：strategy classifier
      的 57.5% 准确率是结构性瓶颈，不是可以通过调参或更多数据解决的——19 个特征
      从设计上就不携带足够的策略判别信息。Pipeline 不仅没有改善跨策略性能，反而因为
      misrouting penalty 比 naive pooling 差 1.4pp。

      对论文结构的影响：Claim 3 从独立 contribution 降为 Discussion future work，
      措辞改为 "We explored a two-stage strategy-aware pipeline and found that while
      oracle strategy identification perfectly recovers within-strategy accuracy
      (78.4% vs 78.2%), strategy classification from the same 19 perplexity features
      reaches only 57.5% — insufficient to outperform naive pooling (70.6% vs 72.0%).
      This reveals that perplexity summary statistics, while effective for depth
      discrimination, do not carry sufficient information to distinguish decoding
      strategies. Future work should explore strategy-specific features (e.g.,
      token-level probability distributions, softmax entropy profiles) for the
      first stage."

      Oracle 结果（78.4% ≈ within-strategy 78.2%）本身是有价值的 finding——它证明
      跨策略问题的根源完全是策略混淆而非深度信号的策略依赖性。这与 temperature
      反转分析（Section 6 的 Strategy Dimension）一致：策略不是 noise，而是信号的
      structural moderator。策略已知时，信号完全可恢复。

      但在 worst tier 叙事下，这个 positive oracle 结果只能作为 "theoretical
      validation" 写入 Discussion，不能撑起一个独立 Claim。论文退到两个 Claims：
      Claim 1（bounded feasibility）+ Claim 2（Atlas/EDD, PRIMARY）。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3f8a287-6635-450b-af97-99d931f5e99e",
  "isSidechain": false,
  "requestId": "req_011Cb7p99HnWHy89ebUhG8JM",
  "type": "assistant",
  "uuid": "d5008fce-b2b7-425a-945e-499b635d5cb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTh26HQC4oWjzahSPoRZ2G",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 304,
      "cache_read_input_tokens": 60848,
      "output_tokens": 13528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 304,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13528,
          "cache_read_input_tokens": 60848,
          "cache_creation_input_tokens": 304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 304
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：13B 信号严重衰减或特征结构被破坏；prompted generation 信号接近无效；scale/ecological validity 核心假设失败，需完全 reframe 为 controlled-setting atlas paper 核心假设：['13B clean FP16 accuracy…",
  "leafUuid": "d5008fce-b2b7-425a-945e-499b635d5cb3",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Ordinal depth estimation under scale and generation mode boundaries",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：13B 信号严重衰减或特征结构被破坏；prompted generation 信号接近无效；scale/ecological validity 核心假设失败，需完全 reframe 为 controlled-setting atlas paper 核心假设：['13B clean FP16 accuracy…",
  "leafUuid": "d5008fce-b2b7-425a-945e-499b635d5cb3",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Ordinal depth estimation under scale and generation mode boundaries",
  "sessionId": "5efddb0d-843a-46eb-b1fd-25fe8567e778"
}
```

---
