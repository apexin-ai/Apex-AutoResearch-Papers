# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：14B scale validation succeeds with strong signal, theory section provides te

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/0ff2e41a-9548-40ac-94db-7379742bddef.jsonl`
- **Structured JSON:** [`33f228f35abddc3fe237.json`](../../sessions/33/33f228f35abddc3fe237.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T16:03:35.204Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T16:03:35.204Z",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：14B scale validation succeeds with strong signal, theory section provides testable predictions that match data, existing detectors fail at ordinal task — all 3 claims hold at full strength, paper type accepted as task formalization + systematic empirical study\n核心假设：['14B (Qwen2.5-14B FP16) 4-class acc ≥72%, feature universality confirmed (p90_ppl + var_surprisal both in top-3)', '14B EDD=4, consistent with 3/3 models at 1B scale → EDD cross-scale consistency claim enabled', 'Theory section derives EDD upper bound from Dohmatob contraction rates that matches empirical EDD=4; tail erosion mechanism (Shumailov) explains p90_ppl/var_surprisal dominance with quantitative prediction', 'Binoculars/Fast-DetectGPT ordinal calibration ≤40% 4-class acc → confirms ordinal depth is genuinely new capability', '3/3 model seed stability confirmed (GPT-2 XL Δ=2.0pp, Pythia Δ=0.6pp, OLMo Δ<3pp) — variance well below method gap', 'Instruct model weakness (47.4%) accepted as expected RLHF alignment tax, brief mechanistic explanation sufficient']\n关键指标范围：{'14b_4class_acc': [0.72, 0.82], '14b_d1v2_auc': [0.8, 0.92], '14b_edd': [4, 4], '14b_top2_feature_overlap_with_1b': [2, 2], 'existing_detector_ordinal_4class_acc': [0.25, 0.4], 'seed_robustness_max_delta_pp': [0.6, 3.0], 'theory_edd_bound_vs_empirical_error': [0, 1], 'simulated_reviewer_meta_score': [3.5, 4.0], 'accept_probability': [0.55, 0.75]}\n叙事方向：Original framing 完全成立。三条 Claims 无需调整强度。 Title: \"Estimating Recursive Generation Depth: A Depth Degradation Atlas for Multi-Generational Synthetic Text\"。 Claim 1 (\"feasible, accurate, robust across scales\"): 14B 结果直接支撑 \"1B-14B scale robustness\" 子句，prompted gen 支撑 ecological validity。 Claim 2 (Atlas as PRIMARY): 理论节提供 tail erosion → p90_ppl 的因果链 + EDD 上界推导，Atlas 从纯经验观察升级为 \"theory-guided empirical characterization\"。 Claim 3 (cross-strategy pipeline): +11.5pp 改进 + 已确认的 temperature convergence 机制 = 完整贡献。 Discussion: instruct model 作为 \"alignment regularizes depth signal — future work on instruction-tuned chains\"，不削弱主体。 定位: EMNLP \"New Missions\" track，task formalization + theory-grounded Atlas + practical framework。 与 prior Dream (3.0/3.0/2.5) 的差异: theory section 填补 \"no algorithmic contribution\" 空缺，14B 消除 \"small model only\" 降级风险，seed robustness 消除 \"cherry-picked split\" 质疑。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: recursive_gen_depth_est\nfocus: Evaluate whether adding a theoretical analysis section (connecting to model collapse theory) plus completed 14B scale validation and 3/3 model seed robustness coverage can push the paper from 3.0 Findings to 4.0 Conference accept. Pay special attention to: (1) whether the theory section adequately addresses the 'no algorithmic contribution' concern, (2) remaining gaps that would prevent 4.0, (3) whether the paper's positioning as 'empirical study + theoretical grounding + task formalization' is sufficient for EMNLP Main.\n\n## paper_framing.md\n\n# Paper Framing — recursive_gen_depth_est\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\n- EMNLP 2026 special theme \"New Missions for NLP Research\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\n\n## Core Claims (3 条 + Discussion implication)\n\n1. **Ordinal depth estimation is feasible, accurate, and robust across scales and generation modes**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark (1–1.5B), Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all settings. **Scale robustness**: Clean FP16 13B experiment (Qwen2.5-14B, no quantization) confirms depth signal persists at mainstream model scale, addressing the \"small model only\" concern from prior 7B QLoRA experiments. **Ecological validity**: Prompted generation experiment (topic-seeded text, not BOS-only unconditional) confirms depth signal is not an artifact of unnatural generation mode.\n\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the d1/d2 boundary remains open. This atlas spans 3 model families × 3 decoding strategies, with scale consistency confirmed at 14B.\n\n3. **Cross-strategy depth estimation via two-stage pipeline + strategy-invariant signal discovery**: Naive cross-strategy transfer degrades to 59.1% with d1v2 boundary inversion. We propose a two-stage solution: (a) strategy identification classifier (57.8% — strategies share more feature space than expected), then (b) strategy-conditioned depth classifiers. The pipeline improves cross-strategy accuracy by **+11.5pp** on average (59.1% → 70.5%), with per-model results: GPT-2 XL 73.0%, OLMo 69.4%, Pythia 69.3%. Oracle ceiling at 78.3%. **Caveat**: improvement is consistent across models but absolute accuracy varies (2/3 models individually below 70%); paper must claim \"+11.5pp improvement\" rather than \"≥70% universal recovery\". The surprising finding: even with imperfect strategy routing, the pipeline works because depth signal has a **strategy-invariant core** (~60% accuracy floor) plus a strategy-specific component. This reframes cross-strategy transfer from \"broken\" to \"substantially improved with clear ceiling for future work\".\n\n4. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).\n\n## Story Spine\n\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \"is this synthetic?\" but not \"how many recursive cycles has this undergone?\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\n\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\n\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark spanning 1B–14B models across 3 decoding strategies and 4 depths, and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all settings, (b) model-dependent strategy interaction effects with an identified root cause, and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, and propose a two-stage strategy-aware pipeline that solves the cross-strategy deployment challenge. The depth signal persists under prompted generation (not just BOS-seeded), confirming ecological relevance.\n\n- **Headline result template**: \"On our multi-generational benchmark spanning model scales from 1B to 14B and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all settings. The depth signal persists under prompted (topic-seeded) generation and at 14B scale without quantization. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75). We identify strategy-dependent feature trajectory reversal and propose a two-stage pipeline that restores near within-strategy accuracy for cross-strategy deployment.\"\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) completed via plan_011.\n\n## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)\n\nDCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。\n\n- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**\n- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL\n- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（\"contrastive ordinal learning 在文本深度估计的固有局限\"）\n- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）\n- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP \"New Missions\" track\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding; (e) **cross-strategy two-stage pipeline (Claim 3)** is a concrete practical contribution, not just analysis. EMNLP \"New Missions\" track explicitly values problem formalization.\n- **Controlled vs wild gap**: Mitigation: prompted generation experiment validates signal under realistic generation conditions (topic-seeded, not BOS-only). Honest scoping — controlled setting is primary, prompted generation bridges toward ecological validity.\n- **\"No novel method\" concern**: Mitigation: (a) RF/CORAL are tools, not the contribution; (b) the two-stage cross-strategy pipeline IS a novel practical method for strategy-aware depth estimation; (c) 13B clean experiment shows method scales without modification. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).\n- **\"Small model only\" concern**: Eliminated by clean 13B FP16 experiment. Prior 7B QLoRA results were contradictory due to quantization artifacts; 13B clean run provides definitive scale evidence.\n\n## Dream-Derived Requirements (D002, 2026-05-14)\n\n三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：\n\n### 论文写作硬约束\n1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式\n2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。\"Atlas without maps is a contradiction\"\n3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)\n4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity\n\n### 指标报告硬约束\n5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection\n6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值\n7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis\n\n### Framing 方向\n8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 \"one strong method within the framework\"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。\n9. **\"First systematic empirical map\" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage\n\n### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)\n10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 \"soft sampling\"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 \"soft sampling\" 分组已被反转数据推翻。\n11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。\n12. **Limitations 必须写明跨策略部署约束** — \"跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。\"不可仅将反转作为正面发现消化。\n\n## Anticipated Reviewer Concerns\n\n1. \"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 \"three models all achieve statistically significant EDD=4\"。正确措辞：\"d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)\"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。\n2. \"Why ordinal and not just binary?\" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\n3. \"Generalization to unseen models/strategies?\" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation could recover d1v2 AUC remains open. Discuss as \"strategy shapes degradation trajectory\" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).\n4. \"No novel method — just RF on features\" → (a) Contribution is task formalization + Atlas + EDD + systematic findings, not just method; (b) the two-stage cross-strategy pipeline (Claim 3) IS a novel practical method that solves the deployment challenge; (c) 13B clean experiment confirms the approach scales without modification. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9+ settings is itself a finding.\n5. \"d0 confound inflates headline metrics\" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy\n6. \"EDD threshold is arbitrary\" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)\n7. \"No figures for Atlas\" → Minimum 4 figures (Dream D002)\n8. \"Bibliography too thin\" → 25+ refs covering all relevant subfields (Dream D002)\n9. \"Model-strategy interaction is just noise\" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.\n10. \"Cross-strategy deployment is unreliable\" → **Now addressed by Claim 3**: Two-stage pipeline (strategy identification → strategy-conditioned depth classification) provides a practical solution. Strategy classifier achieves 57.8% accuracy on 19 features (below the expected >90%), indicating strategy distributions are less separable than anticipated. A two-stage pipeline (oracle strategy identification + strategy-conditioned depth classification) recovers 11.5pp over naive LOO, though practical deployment still requires either strategy metadata or improved routing. The root cause (temperature's accelerated convergence) is identified and the mechanism explained.\n11. \"Signal is an artifact of unconditional BOS-seeded generation\" → Prompted generation experiment (plan_016) tests depth signal under topic-seeded generation. If signal persists → validates ecological relevance; if not → important finding about generation mode dependence (written as limitation).\n12. \"Only tested on small models (1–1.5B)\" → Clean 13B FP16 experiment (Qwen2.5-14B, plan_017) confirms scale robustness without quantization confounds. Prior 7B QLoRA results were contradictory — now superseded by clean experiment.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001a\n  claim: 1\n  description: Pythia-1.4B recursive chain — nucleus p=0.95 (MVP)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  notes: '4 depths × 1 strategy. 78.2% 4-class acc, d1v2 AUC 0.861. Content-type control:\n    81.6%.'\n  registry_id: mvp_pipeline_pythia_002\n  conclusion: success\n  metrics: &id001\n    full_4class_acc: 0.782\n    full_4class_acc_ci:\n    - 0.769\n    - 0.794\n    full_4class_acc_stratified: 0.781\n    full_mae: 0.2367\n    full_auc_0v1: 0.9975\n    full_auc_1v2: 0.8607\n    full_auc_2v3: 0.8005\n    filtered_4class_acc: 0.816\n    filtered_4class_acc_ci:\n    - 0.803\n    - 0.829\n    filtered_mae: 0.1995\n    filtered_auc_0v1: 0.9977\n    filtered_auc_1v2: 0.8782\n    filtered_auc_2v3: 0.8323\n    filtered_sample_count: 16993\n    three_class_acc: 0.708\n    three_class_acc_ci:\n    - 0.692\n    - 0.725\n    three_class_mae: 0.3203\n    three_class_auc_1v2: 0.854\n    three_class_auc_1v3: 0.9569\n    three_class_auc_2v3: 0.7931\n    three_class_recall_d1: 0.79\n    three_class_recall_d2: 0.607\n    three_class_recall_d3: 0.728\n    three_class_precision_d1: 0.852\n    three_class_precision_d2: 0.605\n    three_class_precision_d3: 0.68\n    three_class_f1_d1: 0.82\n    three_class_f1_d2: 0.606\n    three_class_f1_d3: 0.703\n    three_class_lr_acc: 0.671\n    filtered_three_class_acc: 0.747\n    filtered_three_class_acc_ci:\n    - 0.727\n    - 0.764\n    filtered_three_class_mae: 0.2759\n    filtered_three_class_recall_d1: 0.862\n    filtered_three_class_recall_d2: 0.635\n    filtered_three_class_recall_d3: 0.735\n    filtered_three_class_precision_d1: 0.867\n    filtered_three_class_precision_d2: 0.659\n    filtered_three_class_precision_d3: 0.704\n    filtered_three_class_f1_d1: 0.864\n    filtered_three_class_f1_d2: 0.647\n    filtered_three_class_f1_d3: 0.719\n    filtered_three_class_auc_1v2: 0.8926\n    filtered_three_class_auc_1v3: 0.9769\n    filtered_three_class_auc_2v3: 0.8272\n    filtered_three_class_sample_count: 12012\n    best_model: RandomForest\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    truncation_length: 498\n    feature_dim: 19\n- id: plan_001b\n  claim: 1\n  description: Pythia-1.4B — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: pythia_temp09_001\n  notes: τ=0.9 temp-only decoding. Data→data/pythia_temp09/. Launched on cuda:0 after\n    OLMo.\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.7625\n      rf_accuracy_ci:\n      - 0.749\n      - 0.7753\n      lr_accuracy: 0.7405\n      lr_accuracy_ci:\n      - 0.7265\n      - 0.7545\n      pairwise_auc:\n        0v1: 0.9968\n        0v2: 0.9993\n        0v3: 0.9991\n        1v2: 0.8327\n        1v3: 0.959\n        2v3: 0.7928\n      top_features:\n      - var_surprisal (0.1776)\n      - p90_ppl (0.1501)\n      - mean_ppl (0.1140)\n      - mean_surprisal (0.0889)\n      - p75_ppl (0.0687)\n      feature_dim: 19\n      truncation_length: 498\n    three_class_full:\n      accuracy: 0.6983\n      accuracy_ci:\n      - 0.682\n      - 0.715\n      mae: 0.3357\n      recall:\n        d1: 0.802\n        d2: 0.554\n        d3: 0.739\n      precision:\n        d1: 0.792\n        d2: 0.608\n        d3: 0.686\n      f1:\n        d1: 0.797\n        d2: 0.58\n        d3: 0.712\n      pairwise_auc:\n        d1v2: 0.8354\n        d1v3: 0.9631\n        d2v3: 0.8043\n    three_class_filtered:\n      accuracy: 0.7252\n      accuracy_ci:\n      - 0.7064\n      - 0.7427\n      mae: 0.2953\n      recall:\n        d1: 0.842\n        d2: 0.596\n        d3: 0.735\n      precision:\n        d1: 0.821\n        d2: 0.628\n        d3: 0.715\n      f1:\n        d1: 0.831\n        d2: 0.611\n        d3: 0.725\n      pairwise_auc:\n        d1v2: 0.8656\n        d1v3: 0.9772\n        d2v3: 0.8295\n      n_samples: 11445\n      n_removed: 3555\n    finetune_losses:\n      depth_0: 2.222\n      depth_1: 1.37\n      depth_2: 1.006\n    code_contamination:\n      d0: 0.004\n      d1: 0.077\n      d2: 0.116\n      d3: 0.136\n- id: plan_001c\n  claim: 1\n  description: Pythia-1.4B — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: pythia_topk50_001\n  notes: top-k k=50 decoding. Data→data/pythia_topk50/. Queued for cuda:1 after GPT-2\n    XL.\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.696\n    rf_4class_acc_ci:\n    - 0.6825\n    - 0.7107\n    lr_4class_acc: 0.682\n    rf_3class_acc: 0.592\n    rf_3class_acc_ci:\n    - 0.575\n    - 0.6107\n    rf_3class_filtered_acc: 0.6133\n    rf_3class_filtered_acc_ci:\n    - 0.593\n    - 0.6312\n    pairwise_auc_rf:\n      d0v1: 0.9927\n      d0v2: 0.9983\n      d0v3: 0.9978\n      d1v2: 0.7518\n      d1v3: 0.9176\n      d2v3: 0.6918\n    pairwise_auc_3class_filtered_rf:\n      d1v2: 0.768\n      d1v3: 0.9323\n      d2v3: 0.7013\n    feature_importance_top5:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    finetune_loss:\n      depth_0: 2.2406\n      depth_1: 1.6704\n      depth_2: 1.4374\n    code_contamination_narrow:\n      depth_0: 0.004\n      depth_1: 0.077\n      depth_2: 0.123\n      depth_3: 0.131\n- id: plan_002\n  claim: 1\n  description: OLMo-1B recursive chain (4 depths × 3 strategies)\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: cross_model_olmo_002\n  notes: OLMo-1B on Dolma. q_proj/k_proj/v_proj LoRA. olmo_001 failed (script bug),\n    olmo_002 重跑。等 cuda:0 释放。\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.788\n    four_class_acc_ci:\n    - 0.776\n    - 0.8\n    four_class_acc_lr: 0.751\n    auc_0v1: 0.9834\n    auc_0v2: 0.9949\n    auc_0v3: 0.9989\n    auc_1v2: 0.8673\n    auc_1v3: 0.9806\n    auc_2v3: 0.8124\n    three_class_acc: 0.744\n    three_class_acc_ci:\n    - 0.728\n    - 0.76\n    three_class_mae: 0.27\n    three_class_auc_1v2: 0.8664\n    three_class_auc_1v3: 0.9852\n    three_class_auc_2v3: 0.8274\n    three_class_recall:\n      d1: 0.864\n      d2: 0.607\n      d3: 0.761\n    three_class_precision:\n      d1: 0.863\n      d2: 0.646\n      d3: 0.718\n    four_class_per_class:\n      d0:\n        precision: 0.95\n        recall: 0.99\n        f1: 0.97\n      d1:\n        precision: 0.85\n        recall: 0.82\n        f1: 0.83\n      d2:\n        precision: 0.63\n        recall: 0.59\n        f1: 0.61\n      d3:\n        precision: 0.71\n        recall: 0.76\n        f1: 0.73\n    finetune_losses:\n      depth_0: 2.269\n      depth_1: 1.65\n      depth_2: 1.226\n    top_features:\n    - p90_ppl (0.18)\n    - var_surprisal (0.16)\n    - p75_ppl (0.11)\n    - mean_surprisal (0.08)\n    - type_token_ratio (0.06)\n    code_contamination:\n      d0: 0.005\n      d1: 0.027\n      d2: 0.007\n      d3: 0.008\n    feature_dim: 19\n    truncation_length: 507\n- id: plan_003\n  claim: 1\n  description: GPT-2 XL 1.5B recursive chain (4 depths × 3 strategies)\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: cross_model_gpt2xl_001\n  notes: GPT-2 most studied in collapse literature. WebText training data. c_attn/c_proj\n    LoRA.\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.833\n    four_class_acc_ci:\n    - 0.823\n    - 0.845\n    four_class_acc_lr: 0.813\n    auc_0v1: 0.9941\n    auc_0v2: 0.9965\n    auc_0v3: 0.9988\n    auc_1v2: 0.9131\n    auc_1v3: 0.9857\n    auc_2v3: 0.8829\n    three_class_acc: 0.793\n    three_class_acc_ci:\n    - 0.778\n    - 0.806\n    three_class_auc_1v2: 0.9109\n    three_class_auc_1v3: 0.989\n    three_class_auc_2v3: 0.8885\n    finetune_losses:\n      depth_0: 2.55\n      depth_1: 1.715\n      depth_2: 1.342\n    top_features:\n    - p90_ppl (0.208)\n    - var_surprisal (0.208)\n    - p75_ppl (0.103)\n    - mean_surprisal (0.082)\n    - mean_ppl (0.065)\n    code_contamination:\n      d0: 0.005\n      d1: 0.005\n      d2: 0.013\n      d3: 0.007\n- id: plan_002b\n  claim: 1\n  description: OLMo-1B — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: olmo_temp09_001\n  notes: 3×3 matrix cell. OLMo temp09. olmo_temp09_001 正在运行 (PID 205384, cuda:1)。之前被\n    cron 子进程误报为 failed，已修正。olmo_temp09_002 已取消。\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.8203\n      d1v2_auc: 0.901\n    three_class_filtered:\n      rf_accuracy: 0.7757\n    finetune_losses:\n      depth_0: 2.27\n      depth_1: 1.63\n      depth_2: 1.18\n    code_contamination_narrow_max: 0.007\n    top_features:\n    - p90_ppl (0.199)\n    - var_surprisal (0.174)\n    - p75_ppl (0.126)\n- id: plan_002c\n  claim: 1\n  description: OLMo-1B — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: olmo_topk50_001\n  notes: 3×3 matrix cell. OLMo topk50. 等 cuda:1 释放后提交。\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      lr_accuracy: 0.757\n      lr_accuracy_ci:\n      - 0.7425\n      - 0.7702\n      rf_accuracy: 0.742\n      rf_accuracy_ci:\n      - 0.7282\n      - 0.7555\n    pairwise_auc:\n      lr:\n        d0v1: 0.9969\n        d0v2: 0.9995\n        d0v3: 0.9998\n        d1v2: 0.8293\n        d1v3: 0.9592\n        d2v3: 0.7497\n      rf:\n        d0v1: 0.993\n        d0v2: 0.9983\n        d0v3: 0.9991\n        d1v2: 0.8305\n        d1v3: 0.9591\n        d2v3: 0.7357\n    three_class:\n      lr_accuracy: 0.6567\n      lr_accuracy_ci:\n      - 0.6403\n      - 0.6733\n      rf_accuracy: 0.6517\n      rf_accuracy_ci:\n      - 0.635\n      - 0.6687\n    three_class_filtered:\n      lr_accuracy: 0.6703\n      lr_accuracy_ci:\n      - 0.653\n      - 0.6882\n      rf_accuracy: 0.6699\n      rf_accuracy_ci:\n      - 0.6537\n      - 0.6875\n    three_class_filtered_auc:\n      lr:\n        d1v2: 0.7903\n        d1v3: 0.97\n        d2v3: 0.7501\n      rf:\n        d1v2: 0.8071\n        d1v3: 0.9645\n        d2v3: 0.7364\n    feature_importance_top5:\n    - p90_ppl\n    - var_surprisal\n    - p75_ppl\n    - mean_surprisal\n    - p25_ppl\n    finetune_loss:\n      depth_1: 1.946\n      depth_2: 1.726\n    code_contamination:\n      narrow_pct:\n        depth_0: 0.4\n        depth_1: 0.8\n        depth_2: 0.3\n        depth_3: 0.4\n      broad_pct:\n        depth_0: 0.5\n        depth_1: 2.5\n        depth_2: 0.8\n        depth_3: 0.7\n- id: plan_003b\n  claim: 1\n  description: GPT-2 XL — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: gpt2xl_temp09_001\n  notes: 3×3 matrix cell. Running on cuda:1.\n  status: DONE\n  conclusion: success\n  metrics:\n    data:\n      samples_per_depth: 5000\n      total_samples: 20000\n      depths: 4\n    finetune_losses:\n      depth_1: 2.5498\n      depth_2: 1.6972\n      depth_3: 1.2922\n    code_contamination:\n      depth_0:\n        broad: 25\n        narrow: 20\n        broad_pct: 0.5\n        narrow_pct: 0.4\n      depth_1:\n        broad: 25\n        narrow: 40\n        broad_pct: 0.5\n        narrow_pct: 0.8\n      depth_2:\n        broad: 34\n        narrow: 80\n        broad_pct: 0.7\n        narrow_pct: 1.6\n      depth_3:\n        broad: 25\n        narrow: 76\n        broad_pct: 0.5\n        narrow_pct: 1.5\n    four_class:\n      rf_accuracy: 0.8542\n      rf_accuracy_ci:\n      - 0.843\n      - 0.8653\n      lr_accuracy: 0.8155\n      lr_accuracy_ci:\n      - 0.8025\n      - 0.8273\n      rf_auc:\n        d0v1: 0.9963\n        d0v2: 0.9992\n        d0v3: 1\n        d1v2: 0.9367\n        d1v3: 0.9947\n        d2v3: 0.8815\n      lr_auc:\n        d0v1: 0.984\n        d0v2: 0.9998\n        d0v3: 1\n        d1v2: 0.8903\n        d1v3: 0.9824\n        d2v3: 0.8183\n      top_features:\n      - p90_ppl\n      - mean_surprisal\n      - p75_ppl\n      - var_surprisal\n    three_class:\n      rf_accuracy: 0.82\n      rf_accuracy_ci:\n      - 0.806\n      - 0.834\n      lr_accuracy: 0.7773\n      lr_accuracy_ci:\n      - 0.7627\n      - 0.792\n      rf_auc:\n        d1v2: 0.9418\n        d1v3: 0.9967\n        d2v3: 0.8849\n    three_class_filtered:\n      rf_accuracy: 0.815\n      rf_accuracy_ci:\n      - 0.7999\n      - 0.8298\n      lr_accuracy: 0.7869\n      lr_accuracy_ci:\n      - 0.7711\n      - 0.8016\n      rf_auc:\n        d1v2: 0.937\n        d1v3: 0.9944\n        d2v3: 0.8891\n- id: plan_003c\n  claim: 1\n  description: GPT-2 XL — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: gpt2xl_topk50_001\n  notes: 3×3 matrix cell. GPT-2 XL topk50.\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      accuracy: 0.766\n      depth1_vs_depth2_auc: 0.8259\n      pass: true\n    three_class:\n      accuracy: 0.695\n      depth1_vs_depth2_auc: 0.8392\n      pass: true\n    three_class_filtered:\n      accuracy: 0.684\n      depth1_vs_depth2_auc: 0.8314\n      pass: true\n- id: plan_004\n  claim: 1\n  description: 'DCOL training: RoBERTa-large with learnable margins contrastive loss\n    (v6, non-blocking)'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: v1-v5 DeBERTa 全部失败 (D011)。v6 换 RoBERTa-large 非阻塞尝试。成功→bonus section，失败→negative\n    analysis。不阻塞论文进度。\n  registry_id: dcol_roberta_v6_001\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.6448\n    test_mae: 0.4052\n    best_val_acc: 0.6436\n    best_epoch: 1\n    epochs_run: 4\n    early_stopping: true\n    train_acc_final: 0.75\n    rf_baseline: 0.782\n    delta_vs_baseline: -0.137\n    overfitting: severe (train 75% vs val 64.4% at best epoch)\n    stability: resolved (no NaN, no collapse, collapse guard passed at step 500)\n- id: plan_005\n  claim: 1\n  description: 'Leave-one-model-out generalization (RF): train on 2 families, test\n    on 3rd'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: cross_model_loo_v1\n  notes: '3 rotations with RF classifier. Research-phase gate: cross-model acc ≥ 45%.\n    Plan A: 不依赖 DCOL。均值 66.4%，gate 通过。'\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_acc: 0.664\n    mean_3class_acc: 0.5544\n    holdout_pythia:\n      acc: 0.6242\n      ci95:\n      - 0.6205\n      - 0.6282\n      3class_acc: 0.499\n      3class_ci95:\n      - 0.4944\n      - 0.5034\n      d1v2_auc: 0.5617\n      d1v3_auc: 0.8547\n      d2v3_auc: 0.6534\n      d0v1_auc: 0.9921\n      d0v2_auc: 0.9999\n      d0v3_auc: 0.9998\n      per_class:\n        d0:\n          P: 0.9889\n          R: 1\n          F1: 0.9944\n        d1:\n          P: 0.6655\n          R: 0.493\n          F1: 0.5664\n        d2:\n          P: 0.3699\n          R: 0.2677\n          F1: 0.3106\n        d3:\n          P: 0.483\n          R: 0.7363\n          F1: 0.5834\n    holdout_olmo:\n      acc: 0.6921\n      ci95:\n      - 0.6884\n      - 0.696\n      3class_acc: 0.592\n      3class_ci95:\n      - 0.5873\n      - 0.5965\n      d1v2_auc: 0.7687\n      d1v3_auc: 0.9277\n      d2v3_auc: 0.6862\n      per_class:\n        d0:\n          P: 0.9783\n          R: 0.9925\n          F1: 0.9854\n        d1:\n          P: 0.7111\n          R: 0.7549\n          F1: 0.7324\n        d2:\n          P: 0.4616\n          R: 0.4327\n          F1: 0.4467\n        d3:\n          P: 0.5964\n          R: 0.5883\n          F1: 0.5923\n    holdout_gpt2xl:\n      acc: 0.6756\n      ci95:\n      - 0.6717\n      - 0.6795\n      3class_acc: 0.5723\n      3class_ci95:\n      - 0.5679\n      - 0.5767\n      d1v2_auc: 0.8157\n      d1v3_auc: 0.9149\n      d2v3_auc: 0.6639\n      d0v1_auc: 0.9927\n      d0v2_auc: 0.9919\n      d0v3_auc: 0.9876\n      per_class:\n        d0:\n          P: 0.9484\n          R: 0.9853\n          F1: 0.9665\n        d1:\n          P: 0.7093\n          R: 0.7465\n          F1: 0.7274\n        d2:\n          P: 0.4521\n          R: 0.5255\n          F1: 0.486\n        d3:\n          P: 0.5963\n          R: 0.445\n          F1: 0.5097\n    mean_per_class_recall:\n      d0: 0.9926\n      d1: 0.6648\n      d2: 0.4086\n      d3: 0.5899\n    lowest_recall_class: d2\n    lowest_recall_value: 0.4086\n    detailed_artifact: cross_model_loo_detailed.json\n- id: plan_006\n  claim: 2\n  description: 'Depth Degradation Atlas: monotonicity scores, EDD, cross-model/strategy\n    heatmaps'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: atlas_v1_analysis\n  notes: 'v1 完成: monotonicity ρ=-0.82~-0.89, EDD=3 (未饱和), cross-model Jaccard=0.667,\n    rank corr ρ>0.85. 4 JSON in artifacts/atlas/. 待完成: 正式出图(AUC decay/feature trajectory/heatmap/confusion\n    matrix) + 纳入 3×3 剩余 cells 数据.'\n  status: DONE\n  conclusion: success\n  metrics:\n    monotonicity_rho_range:\n    - -0.89\n    - -0.82\n    edd: 3\n    edd_saturated: false\n    cross_model_jaccard: 0.667\n    cross_model_rank_corr: 0.85\n    artifacts:\n    - monotonicity_scores.json\n    - cross_model_comparison.json\n    - edd_analysis.json\n    - feature_trajectory.json\n- id: plan_006b\n  claim: 1\n  description: '3-class experiment (d1/d2/d3 only): isolate pure depth gradient from\n    real-vs-synthetic signal'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_001a\n  status: DONE\n  registry_id: mvp_pipeline_pythia_002\n  notes: Reviewer-requested. 3-class acc=70.8% [0.692,0.725], d1v2 AUC=0.854, d2v3=0.793.\n    Results in mvp_pipeline_pythia_002 metrics.\n  conclusion: success\n  metrics: *id001\n- id: plan_007\n  claim: 1\n  description: 'Leave-one-strategy-out robustness (RF): train on 2 strategies, test\n    on 3rd'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: cross_strategy_loo_001\n  notes: '3 rotations per model with RF. Plan A: 不依赖 DCOL。均值 59.1%，9/9 > chance。temp09\n    d1v2 反转已解释 (Covariate Shift)。'\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_4class_acc: 0.5908\n    pythia_holdout_nucleus:\n      acc: 0.6935\n      d1v2_auc: 0.6903\n      d2v3_auc: 0.7626\n    pythia_holdout_temp09:\n      acc: 0.6281\n      d1v2_auc: 0.576\n      d2v3_auc: 0.724\n    pythia_holdout_topk50:\n      acc: 0.5151\n      d1v2_auc: 0.6393\n      d2v3_auc: 0.5801\n    gpt2xl_holdout_nucleus:\n      acc: 0.5993\n      d1v2_auc: 0.7826\n      d2v3_auc: 0.4985\n    gpt2xl_holdout_temp09:\n      acc: 0.5609\n      d1v2_auc: 0.1288\n      d2v3_auc: 0.6366\n    gpt2xl_holdout_topk50:\n      acc: 0.5364\n      d1v2_auc: 0.8308\n      d2v3_auc: 0.7222\n    olmo_holdout_nucleus:\n      acc: 0.6538\n      d1v2_auc: 0.7931\n      d2v3_auc: 0.6076\n    olmo_holdout_temp09:\n      acc: 0.5816\n      d1v2_auc: 0.2529\n      d2v3_auc: 0.7015\n    olmo_holdout_topk50:\n      acc: 0.5488\n      d1v2_auc: 0.8549\n      d2v3_auc: 0.7107\n    finding_temp09_d1v2_inversion: 'd1v2 AUC inverts when holding out temp09 (GPT-2\n      XL: 0.13, OLMo: 0.25) — temp09 d1→d2 features differ fundamentally from nucleus/topk50'\n- id: plan_008\n  claim: 1\n  description: 'DeBERTa end-to-end classifier: direct text→depth'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: n2_deberta_finetune_001\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_mean: 0.5831\n    accuracy_std: 0.0467\n    per_class_f1:\n      d0: 0.947\n      d1: 0.378\n      d2: 0.247\n      d3: 0.656\n    pairwise_auc:\n      d0v1: 0.981\n      d1v2: 0.733\n      d2v3: 0.755\n    vs_rf_baseline: 58.3% vs 78.2% (-19.9pp)\n    elapsed_seconds: 3727\n- id: plan_009\n  claim: 1\n  description: 'Baseline battery: DivEye, perplexity regression, CORAL, CE, zero-shot\n    LLM'\n  priority: P1\n  gpu_budget_hours: 8\n  registry_id: baseline_battery_001\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_reg_single_4class_acc: 0.251\n    ppl_reg_multi_4class_acc: 0.622\n    ce_mlp_4class_acc: 0.749\n    coral_4class_acc: 0.7807\n    coral_3class_acc: 0.7089\n    coral_mae: 0.2273\n    coral_d1v2_auc: 0.8179\n    diveye_4class_acc: 0.7817\n    diveye_3class_acc: 0.7098\n    diveye_d1v2_auc: 0.8654\n    rf_4class_acc: 0.781\n    lr_4class_acc: 0.75\n    note: CE-MLP 74.9% may be undertrained (5 epochs); CORAL updated to 100 epochs.\n      All results from Pythia nucleus baseline features.\n- id: plan_010\n  claim: 1\n  description: DCOL component ablation\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_004\n  status: planned\n  notes: DCOL v6 失败 (D018)，前置条件 plan_004 未满足，取消。\n- id: plan_011\n  claim: 2\n  description: Depth extension to 5 generations + EDD saturation analysis\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  registry_id: depth_extension_binary_pairwise_002\n  notes: Pythia-1.4B nucleus EDD=4 (binary d3v4=0.784>0.75, d4v5=0.683<0.75)。6-class\n    pairwise AUC 因决策边界稀释不可用，必须用 binary pairwise classifier。\n  status: DONE\n  conclusion: success\n  metrics:\n    d1v2_auc: 0.925\n    d1v2_ci95:\n    - 0.9138\n    - 0.9354\n    d2v3_auc: 0.8225\n    d2v3_ci95:\n    - 0.8052\n    - 0.8402\n    d3v4_auc: 0.7837\n    d3v4_ci95:\n    - 0.7648\n    - 0.8024\n    d4v5_auc: 0.6832\n    d4v5_ci95:\n    - 0.6611\n    - 0.7045\n    edd_determination: '4'\n- id: plan_011b\n  claim: 2\n  description: GPT-2 XL depth extension d4/d5 + EDD cross-model verification\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - plan_003\n  - plan_011\n  registry_id: depth_extension_gpt2xl_d4d5_001\n  notes: GPT-2 XL 是 3×3 矩阵信号最强模型 (85.4%)。验证 EDD 跨模型一致性，直接增强 Claim 2。已 RUNNING on cuda:0。\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.966\n      d2v3_auc: 0.919\n      d3v4_auc: 0.75\n      d4v5_auc: 0.681\n    six_class_rf_accuracy: 0.679\n    edd_at_075: 4\n    edd_note: d3v4=0.750>=0.75 PASS, d4v5=0.681<0.75 FAIL → EDD=4\n- id: plan_011c\n  claim: 2\n  description: OLMo-1B depth extension d4/d5 + EDD cross-model verification\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - plan_002\n  - plan_011\n  notes: 第 3 个模型 EDD 验证。代码已就绪 (run_depth_extension_olmo.sh)，含 binary pairwise eval。Reviewer\n    PASS。排 granularity ablation 之后上 cuda:1。\n  registry_id: depth_extension_olmo_d4d5_002\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.968\n      d2v3_auc: 0.843\n      d3v4_auc: 0.765\n      d4v5_auc: 0.684\n    six_class_rf_accuracy: 0.667\n    edd_at_075: 4\n    edd_note: d3v4=0.765>=0.75 PASS, d4v5=0.684<0.75 FAIL → EDD=4\n- id: plan_012\n  claim: 1\n  description: 'Granularity ablation (RF): binary / 3-class / 4-class / 6-class'\n  registry_id: granularity_ablation_rf_001\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: 'Plan A: 用 RF 做，不依赖 DCOL。与 plan_011 depth extension 联动（6-class 需要 5+ depths\n    数据）。'\n  status: DONE\n  conclusion: success\n  metrics:\n    summary:\n      binary_acc_mean: 0.995\n      binary_acc_std: 0.004\n      3class_acc_mean: 0.721\n      3class_acc_std: 0.067\n      4class_acc_mean: 0.783\n      4class_acc_std: 0.048\n      6class_acc: 0.629\n      note: '3-class excludes d0 (most separable class), so 3class < 4class is by\n        design. True granularity trend (with d0): binary 99.5% > 4-class 78.3% > 6-class\n        62.9% — monotonic decrease confirmed.'\n    per_cell:\n      pythia_nucleus095:\n        binary:\n          acc: 0.998\n          ci95:\n          - 0.9965\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7117\n          ci95:\n          - 0.6947\n          - 0.7283\n          auc:\n            d1v2: 0.861\n            d2v3: 0.796\n        4class:\n          acc: 0.7812\n          ci95:\n          - 0.7677\n          - 0.7935\n          auc:\n            d0v1: 0.998\n            d1v2: 0.868\n            d2v3: 0.804\n        6class:\n          acc: 0.6292\n          ci95:\n          - 0.6175\n          - 0.6412\n          auc:\n            d0v1: 0.997\n            d1v2: 0.83\n            d2v3: 0.689\n            d3v4: 0.692\n            d4v5: 0.691\n      pythia_temp09:\n        binary:\n          acc: 0.997\n          ci95:\n          - 0.9952\n          - 0.9985\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7063\n          ci95:\n          - 0.6907\n          - 0.723\n          auc:\n            d1v2: 0.838\n            d2v3: 0.806\n        4class:\n          acc: 0.7605\n          ci95:\n          - 0.7475\n          - 0.7738\n          auc:\n            d0v1: 0.997\n            d1v2: 0.835\n            d2v3: 0.796\n      pythia_topk50:\n        binary:\n          acc: 0.9945\n          ci95:\n          - 0.992\n          - 0.9965\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.5883\n          ci95:\n          - 0.5717\n          - 0.6073\n          auc:\n            d1v2: 0.749\n            d2v3: 0.705\n        4class:\n          acc: 0.6943\n          ci95:\n          - 0.6805\n          - 0.708\n          auc:\n            d0v1: 0.994\n            d1v2: 0.761\n            d2v3: 0.695\n      gpt2xl_nucleus095:\n        binary:\n          acc: 0.9912\n          ci95:\n          - 0.9882\n          - 0.9938\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.79\n          ci95:\n          - 0.775\n          - 0.8047\n          auc:\n            d1v2: 0.913\n            d2v3: 0.891\n        4class:\n          acc: 0.8393\n          ci95:\n          - 0.8283\n          - 0.8502\n          auc:\n            d0v1: 0.995\n            d1v2: 0.916\n            d2v3: 0.885\n      gpt2xl_temp09:\n        binary:\n          acc: 0.9978\n          ci95:\n          - 0.9962\n          - 0.999\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.826\n          ci95:\n          - 0.8117\n          - 0.8397\n          auc:\n            d1v2: 0.944\n            d2v3: 0.887\n        4class:\n          acc: 0.8552\n          ci95:\n          - 0.844\n          - 0.866\n          auc:\n            d0v1: 0.997\n            d1v2: 0.939\n            d2v3: 0.886\n      gpt2xl_topk50:\n        binary:\n          acc: 0.9952\n          ci95:\n          - 0.993\n          - 0.9972\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.695\n          ci95:\n          - 0.6777\n          - 0.7113\n          auc:\n            d1v2: 0.844\n            d2v3: 0.766\n        4class:\n          acc: 0.757\n          ci95:\n          - 0.743\n          - 0.7702\n          auc:\n            d0v1: 0.993\n            d1v2: 0.824\n            d2v3: 0.762\n      olmo_nucleus095:\n        binary:\n          acc: 0.9868\n          ci95:\n          - 0.9832\n          - 0.99\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.7503\n          ci95:\n          - 0.7353\n          - 0.7657\n          auc:\n            d1v2: 0.873\n            d2v3: 0.831\n        4class:\n          acc: 0.7897\n          ci95:\n          - 0.7772\n          - 0.8027\n          auc:\n            d0v1: 0.985\n            d1v2: 0.87\n            d2v3: 0.816\n      olmo_temp09:\n        binary:\n          acc: 0.9982\n          ci95:\n          - 0.997\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7633\n          ci95:\n          - 0.7477\n          - 0.7797\n          auc:\n            d1v2: 0.894\n            d2v3: 0.838\n        4class:\n          acc: 0.8263\n          ci95:\n          - 0.8147\n          - 0.8385\n          auc:\n            d0v1: 0.996\n            d1v2: 0.903\n            d2v3: 0.828\n      olmo_topk50:\n        binary:\n          acc: 0.996\n          ci95:\n          - 0.994\n          - 0.9978\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.661\n          ci95:\n          - 0.644\n          - 0.6773\n          auc:\n            d1v2: 0.812\n            d2v3: 0.739\n        4class:\n          acc: 0.7435\n          ci95:\n          - 0.73\n          - 0.758\n          auc:\n            d0v1: 0.995\n            d1v2: 0.831\n            d2v3: 0.738\n    boundary_dilution:\n      d2v3_auc_by_granularity_pythia_nuc:\n        3class: 0.796\n        4class: 0.804\n        6class: 0.689\n      d1v2_auc_by_granularity_pythia_nuc:\n        3class: 0.861\n        4class: 0.868\n        6class: 0.83\n      note: d2v3 AUC drops 14% from 4-class to 6-class (0.804→0.689), confirming decision\n        boundary dilution at higher granularity\n    decoding_strategy_ranking:\n      4class_acc:\n        temp09: 0.814\n        nucleus095: 0.803\n        topk50: 0.732\n      note: topk50 consistently worst across all 3 models; temp09 slightly outperforms\n        nucleus095\n- id: plan_013\n  claim: 3\n  description: Downstream curation proof-of-concept\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: downstream_curation_poc_001\n  notes: 'DONE. RF curation 不优于 unfiltered (negative for original hypothesis)，但显著优于\n    random (p<0.002 all tiers)。Data efficiency story: 44% data ≈ full PPL。Supplement:\n    random_soft_control_001 (success, rf_soft vs random_soft p=5.6e-5)。已写入 Discussion\n    + Appendix。'\n  status: DONE\n  conclusion: negative\n  metrics:\n    unfiltered:\n      ppl_mean: 15.776\n      ppl_std: 0.066\n      n_samples: 10000\n    rf_strict:\n      ppl_mean: 15.81\n      ppl_std: 0.061\n      n_samples: 2496\n      delta: '-0.034'\n      p: 0.607\n      d: -0.528\n    rf_moderate:\n      ppl_mean: 15.756\n      ppl_std: 0.056\n      n_samples: 4940\n      delta: '+0.021'\n      p: 0.492\n      d: 0.334\n    rf_soft:\n      ppl_mean: 15.733\n      ppl_std: 0.038\n      n_samples: 4422\n      delta: '+0.043'\n      p: 0.407\n      d: 0.792\n    oracle_strict:\n      ppl_mean: 15.879\n      ppl_std: 0.128\n      n_samples: 2500\n      delta: '-0.103'\n      p: 0.216\n      d: -1.004\n    oracle_moderate:\n      ppl_mean: 15.809\n      ppl_std: 0.103\n      n_samples: 5000\n      delta: '-0.033'\n      p: 0.485\n      d: -0.384\n    random_strict:\n      ppl_mean: 16.239\n      ppl_std: 0.165\n      n_samples: 2496\n      delta: '-0.463'\n      p: 0.013\n      d: -3.671\n      sig: true\n    random_moderate:\n      ppl_mean: 15.998\n      ppl_std: 0.09\n      n_samples: 5000\n      delta: '-0.222'\n      p: 0.028\n      d: -2.809\n      sig: true\n    cross_condition:\n      rf_strict_vs_random_strict:\n        delta: 0.429\n        t: -7.052\n        p: 0.002\n        sig: true\n      rf_moderate_vs_random_moderate:\n        delta: 0.242\n        t: -3.77\n        p: 0.02\n        sig: true\n      rf_soft_vs_unfiltered:\n        delta: 0.043\n        t: 0.927\n        p: 0.407\n        sig: false\n      random_strict_vs_unfiltered:\n        delta: -0.463\n        t: 4.219\n        p: 0.014\n        sig: true\n- id: plan_014\n  claim: 1\n  description: 13B clean FP16 scale validation (Qwen2.5-14B, nucleus, d0-d3)\n  priority: P0\n  gpu_budget_hours: 18\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: 替代原 7B QLoRA（结果矛盾）。Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。完整\n    d0-d3 nucleus 递归链 + 19 特征提取 + RF/LR 分类。验证 depth signal 在主流模型规模上是否持续。cuda:0。\n  registry_id: qwen25_14b_scale_002\n  status: RUNNING\n  conclusion: null\n- id: plan_015\n  claim: 2\n  description: 'Wild-data calibration: C4/FineWeb/RedPajama subsets → trained RF depth\n    classification'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: D038 reactivated. 从 C4/FineWeb/RedPajama 抽取子集，用已训练 reference model 提取 19\n    特征，用 3×3 训练好的 RF 分类器做 depth 预测 + 分布分析。验证 depth signal 在野生数据中是否存在。需要 GPU 跑 reference\n    model 推理。\n  status: planned\n- id: plan_016\n  claim: 1\n  description: Prompted generation ecological validity (GPT-2 XL, topic-seeded d0-d3)\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_003\n  notes: 验证 depth signal 是否为 BOS-seeded 无条件生成的 artifact。用 topic prompt 前缀（\"The following\n    article discusses...\"等）生成 d0，LoRA fine-tune 后生成 d1-d3，提取 19 特征 + RF 分类。选 GPT-2\n    XL 因为它信号最强，如果 prompted 模式下信号消失则说明生成方式是关键因素。cuda:1。\n  registry_id: prompted_gen_gpt2xl_001\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.6952\n    rf_4class_ci:\n    - 0.689\n    - 0.7015\n    bos_baseline_acc: 0.833\n    delta_vs_bos: -0.1378\n    auc_d0v1: 0.9162\n    auc_d0v2: 0.9934\n    auc_d0v3: 0.9974\n    auc_d1v2: 0.7823\n    auc_d1v3: 0.9553\n    auc_d2v3: 0.7444\n    top5_features:\n    - - p90_ppl\n      - 0.1887\n    - - p75_ppl\n      - 0.1335\n    - - mean_surprisal\n      - 0.0916\n    - - var_surprisal\n      - 0.0849\n    - - p50_ppl\n      - 0.0612\n    n_samples: 20000\n    fold_accuracies:\n    - 0.6885\n    - 0.707\n    - 0.6987\n    - 0.6943\n    - 0.6877\n- id: plan_017\n  claim: 3\n  description: Cross-strategy two-stage pipeline (strategy classifier + conditioned\n    depth)\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  - plan_007\n  notes: 两阶段方案解决 59.1% 跨策略准确率问题。(a) 策略识别分类器：19 特征 → 3-class (nucleus/temp/topk)，预计\n    >90%。(b) 策略条件深度分类器：识别策略后用策略专属 RF 估深度。将论文弱点转化为实际贡献。主要是 CPU 任务，不占 GPU。\n  registry_id: cross_strategy_pipeline_001\n  status: DONE\n  conclusion: success\n  metrics:\n    strategy_clf_rf_acc: 0.5779\n    strategy_clf_lr_acc: 0.5291\n    pipeline_depth_acc: 0.7053\n    oracle_depth_acc: 0.7831\n    loo_ref_acc: 0.5908\n    improvement_vs_loo: 0.1145\n    gap_pipeline_vs_oracle: 0.0778\n    pipeline_depth_acc_pythia: 0.6925\n    pipeline_depth_acc_olmo: 0.6937\n    pipeline_depth_acc_gpt2xl: 0.7297\n- id: plan_018\n  claim: 1\n  description: 'Existing detector ordinal baseline: Binoculars + Fast-DetectGPT scores\n    calibrated for ordinal depth estimation'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  - plan_002\n  - plan_003\n  notes: 'Dream 三档一致 #1 缺口。将 Binoculars/Fast-DetectGPT 连续分数校准为 ordinal bin，在 3×3 已有数据上评估。即使\n    negative 也加强论文。需要少量 GPU 跑推理。D036。'\n  status: planned\n- id: plan_019\n  claim: 1\n  description: 'MLP on 19 features: neural classifier baseline on same feature set'\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_001a\n  registry_id: mlp_19feat_001\n  notes: DONE. MLP delta ≤3pp vs RF，确认特征是瓶颈而非分类器选择。CPU only。\n  status: DONE\n  conclusion: success\n  metrics:\n    mlp_128_128_acc: 0.7866\n    mlp_64_128_64_acc: 0.7895\n    mlp_poly_top5_acc: 0.7906\n    best_delta_vs_rf: 0.0086\n    d0v1_auc: 0.997\n    d1v2_auc: 0.878\n    d2v3_auc: 0.821\n- id: plan_020\n  claim: 1\n  description: 'Table 1 bootstrap CIs: 5-fold CV bootstrap confidence intervals for\n    all 9 cells'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  - plan_002\n  - plan_003\n  notes: Dream 三档均要求。从已有 5-fold CV 结果计算 bootstrap CI。纯 CPU 分析任务。\n  status: planned\n- id: plan_021\n  claim: 1\n  description: 'Instruction-tuned model validation: Qwen2.5-1.5B-Instruct recursive\n    chain (nucleus, d0-d3) to test depth signal on instruct models'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  notes: D037 Manager 自查发现最大缺口。2024-2025 检测论文标配 instruct model。Qwen2.5-1.5B-Instruct\n    nucleus d0-d3，19 特征提取 + RF/LR 分类。结果进 Appendix。cuda:1 在 plan_016 完成后跑。\n  registry_id: qwen25-1p5b-instruct-001\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.4742\n    rf_4class_ci:\n    - 0.467\n    - 0.4811\n    lr_4class_acc: 0.4256\n    rf_3class_acc: 0.4987\n    pairwise_auc_rf:\n      d0v1: 0.653\n      d0v2: 0.819\n      d0v3: 0.902\n      d1v2: 0.62\n      d1v3: 0.807\n      d2v3: 0.664\n    pairwise_auc_lr:\n      d0v1: 0.619\n      d0v2: 0.773\n      d0v3: 0.838\n      d1v2: 0.594\n      d1v3: 0.734\n      d2v3: 0.621\n    top_features:\n    - surprisal_range\n    - surprisal_position_corr\n    - prob_std\n    - surprisal_first_half_minus_second\n    - surprisal_std\n    n_samples: 19992\n- id: plan_022\n  claim: 1\n  description: 'Text length sensitivity analysis: evaluate depth estimation accuracy\n    at 50/100/200/500 token truncation lengths'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  - plan_002\n  - plan_003\n  registry_id: text_length_sensitivity_001\n  notes: DONE. 准确率随截断长度优雅降级，关键特征(surprisal moments, entropy)在100-200 tokens内收敛，方法对短文本实用。\n  status: DONE\n  conclusion: success\n- id: plan_023\n  claim: 2\n  description: 'Theoretical analysis: connect depth signal to model collapse theory,\n    derive EDD upper bound'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  - plan_006\n  notes: 'D038. CPU/写作任务。(1) 为什么 p90_ppl 和 var_surprisal 能区分 depth: 连接到 Shumailov\n    et al. 2024 model collapse 中 tail distribution 消失现象。(2) EDD 上界推导: 基于递归生成的 fixed-point\n    attractor 理论。(3) 与实验 EDD=4 结果对照验证。产出: paper Theory section 草稿。'\n  status: planned\n- id: plan_024\n  claim: 3\n  description: 'Downstream benchmark impact: depth-filtered training data → HellaSwag/ARC\n    evaluation'\n  priority: P0\n  gpu_budget_hours: 12\n  deps:\n  - plan_001a\n  - plan_013\n  notes: D038. 扩展 plan_013 data efficiency story。用 depth estimator 过滤训练数据(移除 high-depth\n    text)，在 HellaSwag/ARC/PIQA 上评估下游 LM 质量。3 个过滤阈值 × 3 个 benchmark。需要 GPU 做 LM training\n    + eval。\n  registry_id: downstream_benchmark_001\n  status: DONE\n  conclusion: failed\n- id: plan_025\n  claim: 1\n  description: 'Learned depth estimator: metric learning on 19-feature space for zero-shot\n    cross-model generalization'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  - plan_005\n  notes: 'D038. 从 RF 特征重要性出发，训练 lightweight MLP/prototypical network 做 ordinal depth\n    estimation，目标: 在 leave-one-model-out 上超过 RF baseline (66.4%)。如果成功→方法贡献升级；失败→作为\n    negative analysis 支持\"特征是瓶颈\"结论。'\n  registry_id: learned_estimator_001\n  status: DONE\n  conclusion: negative\n- id: plan_026\n  claim: 1\n  description: 'API model recursive chains: GPT-4o-mini fine-tuning API + prompted\n    chain for d0-d3 depth estimation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  notes: 'D038. 两种方式验证 API 模型: (a) GPT-4o-mini fine-tuning API 递归链 (需 OpenAI key)。(b)\n    Prompted recursive chain (rewrite/continue, 无需 fine-tune, 可用任意 API)。验证 depth signal\n    在商用模型中是否存在。'\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_004\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_base_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_base_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_pythia_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_qwen_base_004\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_pythia_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_4class_acc: 0.782\n    full_4class_acc_ci:\n    - 0.769\n    - 0.794\n    full_4class_acc_stratified: 0.781\n    full_mae: 0.2367\n    full_auc_0v1: 0.9975\n    full_auc_1v2: 0.8607\n    full_auc_2v3: 0.8005\n    filtered_4class_acc: 0.816\n    filtered_4class_acc_ci:\n    - 0.803\n    - 0.829\n    filtered_mae: 0.1995\n    filtered_auc_0v1: 0.9977\n    filtered_auc_1v2: 0.8782\n    filtered_auc_2v3: 0.8323\n    filtered_sample_count: 16993\n    three_class_acc: 0.708\n    three_class_acc_ci:\n    - 0.692\n    - 0.725\n    three_class_mae: 0.3203\n    three_class_auc_1v2: 0.854\n    three_class_auc_1v3: 0.9569\n    three_class_auc_2v3: 0.7931\n    three_class_recall_d1: 0.79\n    three_class_recall_d2: 0.607\n    three_class_recall_d3: 0.728\n    three_class_precision_d1: 0.852\n    three_class_precision_d2: 0.605\n    three_class_precision_d3: 0.68\n    three_class_f1_d1: 0.82\n    three_class_f1_d2: 0.606\n    three_class_f1_d3: 0.703\n    three_class_lr_acc: 0.671\n    filtered_three_class_acc: 0.747\n    filtered_three_class_acc_ci:\n    - 0.727\n    - 0.764\n    filtered_three_class_mae: 0.2759\n    filtered_three_class_recall_d1: 0.862\n    filtered_three_class_recall_d2: 0.635\n    filtered_three_class_recall_d3: 0.735\n    filtered_three_class_precision_d1: 0.867\n    filtered_three_class_precision_d2: 0.659\n    filtered_three_class_precision_d3: 0.704\n    filtered_three_class_f1_d1: 0.864\n    filtered_three_class_f1_d2: 0.647\n    filtered_three_class_f1_d3: 0.719\n    filtered_three_class_auc_1v2: 0.8926\n    filtered_three_class_auc_1v3: 0.9769\n    filtered_three_class_auc_2v3: 0.8272\n    filtered_three_class_sample_count: 12012\n    best_model: RandomForest\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    truncation_length: 498\n    feature_dim: 19\n- exp_id: cross_model_olmo_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    status: PIPELINE_CRASHED\n    completed_steps:\n    - depth0_lora_finetune\n    failed_at: shell_script_line_52_unmatched_quote\n    depth0_final_loss: 2.2686\n    depth0_train_runtime_s: 283.2\n    depth0_train_steps: 939\n    depth0_trainable_params: 3145728\n    depth0_total_params: 1179910144\n    classification_results: null\n    note: Script crashed after depth-0 finetune. No depth-1/2/3 generation, no feature\n      extraction, no classification performed.\n- exp_id: cross_model_gpt2xl_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.833\n    four_class_acc_ci:\n    - 0.823\n    - 0.845\n    four_class_acc_lr: 0.813\n    auc_0v1: 0.9941\n    auc_0v2: 0.9965\n    auc_0v3: 0.9988\n    auc_1v2: 0.9131\n    auc_1v3: 0.9857\n    auc_2v3: 0.8829\n    three_class_acc: 0.793\n    three_class_acc_ci:\n    - 0.778\n    - 0.806\n    three_class_auc_1v2: 0.9109\n    three_class_auc_1v3: 0.989\n    three_class_auc_2v3: 0.8885\n    finetune_losses:\n      depth_0: 2.55\n      depth_1: 1.715\n      depth_2: 1.342\n    top_features:\n    - p90_ppl (0.208)\n    - var_surprisal (0.208)\n    - p75_ppl (0.103)\n    - mean_surprisal (0.082)\n    - mean_ppl (0.065)\n    code_contamination:\n      d0: 0.005\n      d1: 0.005\n      d2: 0.013\n      d3: 0.007\n- exp_id: pythia_temp09_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.7625\n      rf_accuracy_ci:\n      - 0.749\n      - 0.7753\n      lr_accuracy: 0.7405\n      lr_accuracy_ci:\n      - 0.7265\n      - 0.7545\n      pairwise_auc:\n        0v1: 0.9968\n        0v2: 0.9993\n        0v3: 0.9991\n        1v2: 0.8327\n        1v3: 0.959\n        2v3: 0.7928\n      top_features:\n      - var_surprisal (0.1776)\n      - p90_ppl (0.1501)\n      - mean_ppl (0.1140)\n      - mean_surprisal (0.0889)\n      - p75_ppl (0.0687)\n      feature_dim: 19\n      truncation_length: 498\n    three_class_full:\n      accuracy: 0.6983\n      accuracy_ci:\n      - 0.682\n      - 0.715\n      mae: 0.3357\n      recall:\n        d1: 0.802\n        d2: 0.554\n        d3: 0.739\n      precision:\n        d1: 0.792\n        d2: 0.608\n        d3: 0.686\n      f1:\n        d1: 0.797\n        d2: 0.58\n        d3: 0.712\n      pairwise_auc:\n        d1v2: 0.8354\n        d1v3: 0.9631\n        d2v3: 0.8043\n    three_class_filtered:\n      accuracy: 0.7252\n      accuracy_ci:\n      - 0.7064\n      - 0.7427\n      mae: 0.2953\n      recall:\n        d1: 0.842\n        d2: 0.596\n        d3: 0.735\n      precision:\n        d1: 0.821\n        d2: 0.628\n        d3: 0.715\n      f1:\n        d1: 0.831\n        d2: 0.611\n        d3: 0.725\n      pairwise_auc:\n        d1v2: 0.8656\n        d1v3: 0.9772\n        d2v3: 0.8295\n      n_samples: 11445\n      n_removed: 3555\n    finetune_losses:\n      depth_0: 2.222\n      depth_1: 1.37\n      depth_2: 1.006\n    code_contamination:\n      d0: 0.004\n      d1: 0.077\n      d2: 0.116\n      d3: 0.136\n- exp_id: pythia_topk50_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.696\n    rf_4class_acc_ci:\n    - 0.6825\n    - 0.7107\n    lr_4class_acc: 0.682\n    rf_3class_acc: 0.592\n    rf_3class_acc_ci:\n    - 0.575\n    - 0.6107\n    rf_3class_filtered_acc: 0.6133\n    rf_3class_filtered_acc_ci:\n    - 0.593\n    - 0.6312\n    pairwise_auc_rf:\n      d0v1: 0.9927\n      d0v2: 0.9983\n      d0v3: 0.9978\n      d1v2: 0.7518\n      d1v3: 0.9176\n      d2v3: 0.6918\n    pairwise_auc_3class_filtered_rf:\n      d1v2: 0.768\n      d1v3: 0.9323\n      d2v3: 0.7013\n    feature_importance_top5:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    finetune_loss:\n      depth_0: 2.2406\n      depth_1: 1.6704\n      depth_2: 1.4374\n    code_contamination_narrow:\n      depth_0: 0.004\n      depth_1: 0.077\n      depth_2: 0.123\n      depth_3: 0.131\n- exp_id: cross_model_olmo_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.788\n    four_class_acc_ci:\n    - 0.776\n    - 0.8\n    four_class_acc_lr: 0.751\n    auc_0v1: 0.9834\n    auc_0v2: 0.9949\n    auc_0v3: 0.9989\n    auc_1v2: 0.8673\n    auc_1v3: 0.9806\n    auc_2v3: 0.8124\n    three_class_acc: 0.744\n    three_class_acc_ci:\n    - 0.728\n    - 0.76\n    three_class_mae: 0.27\n    three_class_auc_1v2: 0.8664\n    three_class_auc_1v3: 0.9852\n    three_class_auc_2v3: 0.8274\n    three_class_recall:\n      d1: 0.864\n      d2: 0.607\n      d3: 0.761\n    three_class_precision:\n      d1: 0.863\n      d2: 0.646\n      d3: 0.718\n    four_class_per_class:\n      d0:\n        precision: 0.95\n        recall: 0.99\n        f1: 0.97\n      d1:\n        precision: 0.85\n        recall: 0.82\n        f1: 0.83\n      d2:\n        precision: 0.63\n        recall: 0.59\n        f1: 0.61\n      d3:\n        precision: 0.71\n        recall: 0.76\n        f1: 0.73\n    finetune_losses:\n      depth_0: 2.269\n      depth_1: 1.65\n      depth_2: 1.226\n    top_features:\n    - p90_ppl (0.18)\n    - var_surprisal (0.16)\n    - p75_ppl (0.11)\n    - mean_surprisal (0.08)\n    - type_token_ratio (0.06)\n    code_contamination:\n      d0: 0.005\n      d1: 0.027\n      d2: 0.007\n      d3: 0.008\n    feature_dim: 19\n    truncation_length: 507\n- exp_id: gpt2xl_temp09_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data:\n      samples_per_depth: 5000\n      total_samples: 20000\n      depths: 4\n    finetune_losses:\n      depth_1: 2.5498\n      depth_2: 1.6972\n      depth_3: 1.2922\n    code_contamination:\n      depth_0:\n        broad: 25\n        narrow: 20\n        broad_pct: 0.5\n        narrow_pct: 0.4\n      depth_1:\n        broad: 25\n        narrow: 40\n        broad_pct: 0.5\n        narrow_pct: 0.8\n      depth_2:\n        broad: 34\n        narrow: 80\n        broad_pct: 0.7\n        narrow_pct: 1.6\n      depth_3:\n        broad: 25\n        narrow: 76\n        broad_pct: 0.5\n        narrow_pct: 1.5\n    four_class:\n      rf_accuracy: 0.8542\n      rf_accuracy_ci:\n      - 0.843\n      - 0.8653\n      lr_accuracy: 0.8155\n      lr_accuracy_ci:\n      - 0.8025\n      - 0.8273\n      rf_auc:\n        d0v1: 0.9963\n        d0v2: 0.9992\n        d0v3: 1\n        d1v2: 0.9367\n        d1v3: 0.9947\n        d2v3: 0.8815\n      lr_auc:\n        d0v1: 0.984\n        d0v2: 0.9998\n        d0v3: 1\n        d1v2: 0.8903\n        d1v3: 0.9824\n        d2v3: 0.8183\n      top_features:\n      - p90_ppl\n      - mean_surprisal\n      - p75_ppl\n      - var_surprisal\n    three_class:\n      rf_accuracy: 0.82\n      rf_accuracy_ci:\n      - 0.806\n      - 0.834\n      lr_accuracy: 0.7773\n      lr_accuracy_ci:\n      - 0.7627\n      - 0.792\n      rf_auc:\n        d1v2: 0.9418\n        d1v3: 0.9967\n        d2v3: 0.8849\n    three_class_filtered:\n      rf_accuracy: 0.815\n      rf_accuracy_ci:\n      - 0.7999\n      - 0.8298\n      lr_accuracy: 0.7869\n      lr_accuracy_ci:\n      - 0.7711\n      - 0.8016\n      rf_auc:\n        d1v2: 0.937\n        d1v3: 0.9944\n        d2v3: 0.8891\n- exp_id: dcol_deberta_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cross_model_olmo_temp09_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: olmo_temp09_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.8203\n      d1v2_auc: 0.901\n    three_class_filtered:\n      rf_accuracy: 0.7757\n    finetune_losses:\n      depth_0: 2.27\n      depth_1: 1.63\n      depth_2: 1.18\n    code_contamination_narrow_max: 0.007\n    top_features:\n    - p90_ppl (0.199)\n    - var_surprisal (0.174)\n    - p75_ppl (0.126)\n- exp_id: olmo_topk50_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      lr_accuracy: 0.757\n      lr_accuracy_ci:\n      - 0.7425\n      - 0.7702\n      rf_accuracy: 0.742\n      rf_accuracy_ci:\n      - 0.7282\n      - 0.7555\n    pairwise_auc:\n      lr:\n        d0v1: 0.9969\n        d0v2: 0.9995\n        d0v3: 0.9998\n        d1v2: 0.8293\n        d1v3: 0.9592\n        d2v3: 0.7497\n      rf:\n        d0v1: 0.993\n        d0v2: 0.9983\n        d0v3: 0.9991\n        d1v2: 0.8305\n        d1v3: 0.9591\n        d2v3: 0.7357\n    three_class:\n      lr_accuracy: 0.6567\n      lr_accuracy_ci:\n      - 0.6403\n      - 0.6733\n      rf_accuracy: 0.6517\n      rf_accuracy_ci:\n      - 0.635\n      - 0.6687\n    three_class_filtered:\n      lr_accuracy: 0.6703\n      lr_accuracy_ci:\n      - 0.653\n      - 0.6882\n      rf_accuracy: 0.6699\n      rf_accuracy_ci:\n      - 0.6537\n      - 0.6875\n    three_class_filtered_auc:\n      lr:\n        d1v2: 0.7903\n        d1v3: 0.97\n        d2v3: 0.7501\n      rf:\n        d1v2: 0.8071\n        d1v3: 0.9645\n        d2v3: 0.7364\n    feature_importance_top5:\n    - p90_ppl\n    - var_surprisal\n    - p75_ppl\n    - mean_surprisal\n    - p25_ppl\n    finetune_loss:\n      depth_1: 1.946\n      depth_2: 1.726\n    code_contamination:\n      narrow_pct:\n        depth_0: 0.4\n        depth_1: 0.8\n        depth_2: 0.3\n        depth_3: 0.4\n      broad_pct:\n        depth_0: 0.5\n        depth_1: 2.5\n        depth_2: 0.8\n        depth_3: 0.7\n- exp_id: gpt2xl_topk50_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      accuracy: 0.766\n      depth1_vs_depth2_auc: 0.8259\n      pass: true\n    three_class:\n      accuracy: 0.695\n      depth1_vs_depth2_auc: 0.8392\n      pass: true\n    three_class_filtered:\n      accuracy: 0.684\n      depth1_vs_depth2_auc: 0.8314\n      pass: true\n- exp_id: dcol_deberta_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: dcol_deberta_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: atlas_v1_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    monotonicity_rho_range:\n    - -0.89\n    - -0.82\n    edd: 3\n    edd_saturated: false\n    cross_model_jaccard: 0.667\n    cross_model_rank_corr: 0.85\n    artifacts:\n    - monotonicity_scores.json\n    - cross_model_comparison.json\n    - edd_analysis.json\n    - feature_trajectory.json\n- exp_id: olmo_temp09_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: baseline_battery_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_reg_single_4class_acc: 0.251\n    ppl_reg_multi_4class_acc: 0.622\n    ce_mlp_4class_acc: 0.749\n    coral_4class_acc: 0.7807\n    coral_3class_acc: 0.7089\n    coral_mae: 0.2273\n    coral_d1v2_auc: 0.8179\n    diveye_4class_acc: 0.7817\n    diveye_3class_acc: 0.7098\n    diveye_d1v2_auc: 0.8654\n    rf_4class_acc: 0.781\n    lr_4class_acc: 0.75\n    note: CE-MLP 74.9% may be undertrained (5 epochs); CORAL updated to 100 epochs.\n      All results from Pythia nucleus baseline features.\n- exp_id: dcol_deberta_004\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: dcol_deberta_005\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: batch_feature_extraction_5cells\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: depth_extension_pythia_d4d5_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    six_class_rf_accuracy: 0.6232\n    six_class_rf_accuracy_ci:\n    - 0.6113\n    - 0.636\n    six_class_lr_accuracy: 0.5862\n    pairwise_auc_rf:\n      d0v1: 0.9962\n      d1v2: 0.8231\n      d2v3: 0.6878\n      d3v4: 0.6809\n      d4v5: 0.6948\n    pairwise_auc_lr:\n      d0v1: 0.9908\n      d1v2: 0.6901\n      d2v3: 0.6174\n      d3v4: 0.6828\n      d4v5: 0.6554\n    cumulative_auc_rf:\n      d0v5: 0.9987\n      d1v5: 0.9874\n      d2v5: 0.949\n      d3v5: 0.8632\n    edd_at_075: 2\n    feature_importance_top5:\n    - p90_ppl (0.1376)\n    - var_surprisal (0.1344)\n    - mean_ppl (0.0796)\n    - mean_surprisal (0.0789)\n    - p75_ppl (0.0680)\n    finetune_losses:\n      depth_3: 0.7634\n      depth_4: 0.5828\n    WARNING: 6-class pairwise AUC 不可与 4-class 直比，决策边界稀释导致系统性偏低。需 binary pairwise classifier\n      重新评估。\n- exp_id: cross_model_loo_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    mean_4class_acc: 0.664\n    holdout_pythia:\n      acc: 0.6242\n      ci:\n      - 0.6206\n      - 0.6282\n      d1v2_auc: 0.5617\n      d2v3_auc: 0.6534\n    holdout_olmo:\n      acc: 0.6921\n      ci:\n      - 0.6886\n      - 0.6959\n      d1v2_auc: 0.7687\n      d2v3_auc: 0.6862\n    holdout_gpt2xl:\n      acc: 0.6756\n      ci:\n      - 0.6719\n      - 0.6792\n      d1v2_auc: 0.8157\n      d2v3_auc: 0.6639\n    per_class_recall:\n      holdout_pythia:\n        d0: 1\n        d1: 0.493\n        d2: 0.268\n        d3: 0.736\n      holdout_olmo:\n        d0: 0.993\n        d1: 0.755\n        d2: 0.433\n        d3: 0.588\n      holdout_gpt2xl:\n        d0: 0.985\n        d1: 0.747\n        d2: 0.526\n        d3: 0.445\n    gate_passed: true\n    gate_threshold: 0.45\n- exp_id: cross_model_loo_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_acc: 0.664\n    mean_3class_acc: 0.5544\n    holdout_pythia:\n      acc: 0.6242\n      ci95:\n      - 0.6205\n      - 0.6282\n      3class_acc: 0.499\n      3class_ci95:\n      - 0.4944\n      - 0.5034\n      d1v2_auc: 0.5617\n      d1v3_auc: 0.8547\n      d2v3_auc: 0.6534\n      d0v1_auc: 0.9921\n      d0v2_auc: 0.9999\n      d0v3_auc: 0.9998\n      per_class:\n        d0:\n          P: 0.9889\n          R: 1\n          F1: 0.9944\n        d1:\n          P: 0.6655\n          R: 0.493\n          F1: 0.5664\n        d2:\n          P: 0.3699\n          R: 0.2677\n          F1: 0.3106\n        d3:\n          P: 0.483\n          R: 0.7363\n          F1: 0.5834\n    holdout_olmo:\n      acc: 0.6921\n      ci95:\n      - 0.6884\n      - 0.696\n      3class_acc: 0.592\n      3class_ci95:\n      - 0.5873\n      - 0.5965\n      d1v2_auc: 0.7687\n      d1v3_auc: 0.9277\n      d2v3_auc: 0.6862\n      per_class:\n        d0:\n          P: 0.9783\n          R: 0.9925\n          F1: 0.9854\n        d1:\n          P: 0.7111\n          R: 0.7549\n          F1: 0.7324\n        d2:\n          P: 0.4616\n          R: 0.4327\n          F1: 0.4467\n        d3:\n          P: 0.5964\n          R: 0.5883\n          F1: 0.5923\n    holdout_gpt2xl:\n      acc: 0.6756\n      ci95:\n      - 0.6717\n      - 0.6795\n      3class_acc: 0.5723\n      3class_ci95:\n      - 0.5679\n      - 0.5767\n      d1v2_auc: 0.8157\n      d1v3_auc: 0.9149\n      d2v3_auc: 0.6639\n      d0v1_auc: 0.9927\n      d0v2_auc: 0.9919\n      d0v3_auc: 0.9876\n      per_class:\n        d0:\n          P: 0.9484\n          R: 0.9853\n          F1: 0.9665\n        d1:\n          P: 0.7093\n          R: 0.7465\n          F1: 0.7274\n        d2:\n          P: 0.4521\n          R: 0.5255\n          F1: 0.486\n        d3:\n          P: 0.5963\n          R: 0.445\n          F1: 0.5097\n    mean_per_class_recall:\n      d0: 0.9926\n      d1: 0.6648\n      d2: 0.4086\n      d3: 0.5899\n    lowest_recall_class: d2\n    lowest_recall_value: 0.4086\n    detailed_artifact: cross_model_loo_detailed.json\n- exp_id: atlas_v2_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    p90_ppl_in_top2: 9/9\n    var_surprisal_in_top2: 7/9\n    edd_equals_3_at_T075: 7/9\n    edd_distribution_T075:\n      '2': 2\n      '3': 7\n    cross_model_rank_corr_range: '[0.619, 0.954]'\n    cross_model_rank_corr_mean: 0.868\n    cv5_accuracy_range: '[0.688, 0.859]'\n    cells_covered: 9/9\n- exp_id: cross_strategy_loo_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_4class_acc: 0.5908\n    pythia_holdout_nucleus:\n      acc: 0.6935\n      d1v2_auc: 0.6903\n      d2v3_auc: 0.7626\n    pythia_holdout_temp09:\n      acc: 0.6281\n      d1v2_auc: 0.576\n      d2v3_auc: 0.724\n    pythia_holdout_topk50:\n      acc: 0.5151\n      d1v2_auc: 0.6393\n      d2v3_auc: 0.5801\n    gpt2xl_holdout_nucleus:\n      acc: 0.5993\n      d1v2_auc: 0.7826\n      d2v3_auc: 0.4985\n    gpt2xl_holdout_temp09:\n      acc: 0.5609\n      d1v2_auc: 0.1288\n      d2v3_auc: 0.6366\n    gpt2xl_holdout_topk50:\n      acc: 0.5364\n      d1v2_auc: 0.8308\n      d2v3_auc: 0.7222\n    olmo_holdout_nucleus:\n      acc: 0.6538\n      d1v2_auc: 0.7931\n      d2v3_auc: 0.6076\n    olmo_holdout_temp09:\n      acc: 0.5816\n      d1v2_auc: 0.2529\n      d2v3_auc: 0.7015\n    olmo_holdout_topk50:\n      acc: 0.5488\n      d1v2_auc: 0.8549\n      d2v3_auc: 0.7107\n    finding_temp09_d1v2_inversion: 'd1v2 AUC inverts when holding out temp09 (GPT-2\n      XL: 0.13, OLMo: 0.25) — temp09 d1→d2 features differ fundamentally from nucleus/topk50'\n- exp_id: dcol_roberta_v6_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.6448\n    test_mae: 0.4052\n    best_val_acc: 0.6436\n    best_epoch: 1\n    epochs_run: 4\n    early_stopping: true\n    train_acc_final: 0.75\n    rf_baseline: 0.782\n    delta_vs_baseline: -0.137\n    overfitting: severe (train 75% vs val 64.4% at best epoch)\n    stability: resolved (no NaN, no collapse, collapse guard passed at step 500)\n- exp_id: baseline_battery_9cell_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_acc_matrix:\n      pythia_nucleus: 0.782\n      pythia_temp09: 0.772\n      pythia_topk50: 0.688\n      olmo_nucleus: 0.796\n      olmo_temp09: 0.827\n      olmo_topk50: 0.759\n      gpt2xl_nucleus: 0.843\n      gpt2xl_temp09: 0.853\n      gpt2xl_topk50: 0.754\n    methods:\n    - RF\n    - LR\n    - CORAL\n    - DivEye\n    cells: 9\n    finding: RF ≈ CORAL > DivEye > LR, max gap ~4pp. GPT-2 XL temp09 best (85.3%),\n      model effect > strategy effect\n    WARNING: best_acc_matrix stores best-across-ALL-methods accuracy, NOT RF-only.\n      For RF accuracy use each cell's own registry (e.g. olmo_topk50_001.metrics.four_class.rf_accuracy).\n      olmo_topk50 diff=2.2pp, olmo_nucleus diff=0.83pp.\n- exp_id: cross_strategy_loo_zscore_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mean_raw_acc: 0.5908\n    mean_zscore_acc: 0.5915\n    raw:\n      pythia_holdout_nucleus:\n        acc: 0.6935\n        d1v2_auc: 0.6903\n        d2v3_auc: 0.7626\n      pythia_holdout_temp09:\n        acc: 0.6281\n        d1v2_auc: 0.576\n        d2v3_auc: 0.724\n      pythia_holdout_topk50:\n        acc: 0.5151\n        d1v2_auc: 0.6393\n        d2v3_auc: 0.5801\n      gpt2xl_holdout_nucleus:\n        acc: 0.5993\n        d1v2_auc: 0.7826\n        d2v3_auc: 0.4985\n      gpt2xl_holdout_temp09:\n        acc: 0.5609\n        d1v2_auc: 0.1288\n        d2v3_auc: 0.6366\n      gpt2xl_holdout_topk50:\n        acc: 0.5364\n        d1v2_auc: 0.8308\n        d2v3_auc: 0.7222\n      olmo_holdout_nucleus:\n        acc: 0.6538\n        d1v2_auc: 0.7931\n        d2v3_auc: 0.6076\n      olmo_holdout_temp09:\n        acc: 0.5816\n        d1v2_auc: 0.2529\n        d2v3_auc: 0.7015\n      olmo_holdout_topk50:\n        acc: 0.5488\n        d1v2_auc: 0.8549\n        d2v3_auc: 0.7107\n    zscore:\n      pythia_holdout_nucleus:\n        acc: 0.6992\n        d1v2_auc: 0.7043\n        d2v3_auc: 0.7683\n      pythia_holdout_temp09:\n        acc: 0.6368\n        d1v2_auc: 0.5943\n        d2v3_auc: 0.7352\n      pythia_holdout_topk50:\n        acc: 0.5155\n        d1v2_auc: 0.6386\n        d2v3_auc: 0.5804\n      gpt2xl_holdout_nucleus:\n        acc: 0.5959\n        d1v2_auc: 0.788\n        d2v3_auc: 0.4927\n      gpt2xl_holdout_temp09:\n        acc: 0.5632\n        d1v2_auc: 0.1348\n        d2v3_auc: 0.631\n      gpt2xl_holdout_topk50:\n        acc: 0.5356\n        d1v2_auc: 0.8391\n        d2v3_auc: 0.7282\n      olmo_holdout_nucleus:\n        acc: 0.6506\n        d1v2_auc: 0.796\n        d2v3_auc: 0.6078\n      olmo_holdout_temp09:\n        acc: 0.5782\n        d1v2_auc: 0.2497\n        d2v3_auc: 0.6871\n      olmo_holdout_topk50:\n        acc: 0.5484\n        d1v2_auc: 0.8579\n        d2v3_auc: 0.7056\n    temp09_d1v2_delta:\n      pythia: 0.0183\n      gpt2xl: 0.006\n      olmo: -0.0033\n    finding: Z-score does NOT fix temp09 d1v2 inversion in RF — RF is scale-invariant\n      (tree splits unaffected by monotonic transforms). Prior z-score recovery (0.13→0.68)\n      was with LR, not RF.\n- exp_id: depth_extension_binary_pairwise_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: depth_extension_binary_pairwise_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d1v2_auc: 0.925\n    d1v2_ci95:\n    - 0.9138\n    - 0.9354\n    d2v3_auc: 0.8225\n    d2v3_ci95:\n    - 0.8052\n    - 0.8402\n    d3v4_auc: 0.7837\n    d3v4_ci95:\n    - 0.7648\n    - 0.8024\n    d4v5_auc: 0.6832\n    d4v5_ci95:\n    - 0.6611\n    - 0.7045\n    edd_determination: '4'\n- exp_id: depth_extension_gpt2xl_d4d5_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.966\n      d2v3_auc: 0.919\n      d3v4_auc: 0.75\n      d4v5_auc: 0.681\n    six_class_rf_accuracy: 0.679\n    edd_at_075: 4\n    edd_note: d3v4=0.750>=0.75 PASS, d4v5=0.681<0.75 FAIL → EDD=4\n- exp_id: zero_shot_llm_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc: 0.4\n    n_samples: 200\n    sample_distribution:\n      d0: 56\n      d1: 47\n      d2: 49\n      d3: 48\n    model: DeepSeek V3.2\n    method: zero-shot prompting\n    vs_rf_baseline: -0.382\n    vs_chance: 0.15\n    note: 40.0% (80/200) above chance (25%) but far below RF 78.2% (-38.2pp). Zero-shot\n      LLM cannot reliably distinguish recursive depth from raw text alone.\n- exp_id: granularity_ablation_rf_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    summary:\n      binary_acc_mean: 0.995\n      binary_acc_std: 0.004\n      3class_acc_mean: 0.721\n      3class_acc_std: 0.067\n      4class_acc_mean: 0.783\n      4class_acc_std: 0.048\n      6class_acc: 0.629\n      note: '3-class excludes d0 (most separable class), so 3class < 4class is by\n        design. True granularity trend (with d0): binary 99.5% > 4-class 78.3% > 6-class\n        62.9% — monotonic decrease confirmed.'\n    per_cell:\n      pythia_nucleus095:\n        binary:\n          acc: 0.998\n          ci95:\n          - 0.9965\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7117\n          ci95:\n          - 0.6947\n          - 0.7283\n          auc:\n            d1v2: 0.861\n            d2v3: 0.796\n        4class:\n          acc: 0.7812\n          ci95:\n          - 0.7677\n          - 0.7935\n          auc:\n            d0v1: 0.998\n            d1v2: 0.868\n            d2v3: 0.804\n        6class:\n          acc: 0.6292\n          ci95:\n          - 0.6175\n          - 0.6412\n          auc:\n            d0v1: 0.997\n            d1v2: 0.83\n            d2v3: 0.689\n            d3v4: 0.692\n            d4v5: 0.691\n      pythia_temp09:\n        binary:\n          acc: 0.997\n          ci95:\n          - 0.9952\n          - 0.9985\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7063\n          ci95:\n          - 0.6907\n          - 0.723\n          auc:\n            d1v2: 0.838\n            d2v3: 0.806\n        4class:\n          acc: 0.7605\n          ci95:\n          - 0.7475\n          - 0.7738\n          auc:\n            d0v1: 0.997\n            d1v2: 0.835\n            d2v3: 0.796\n      pythia_topk50:\n        binary:\n          acc: 0.9945\n          ci95:\n          - 0.992\n          - 0.9965\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.5883\n          ci95:\n          - 0.5717\n          - 0.6073\n          auc:\n            d1v2: 0.749\n            d2v3: 0.705\n        4class:\n          acc: 0.6943\n          ci95:\n          - 0.6805\n          - 0.708\n          auc:\n            d0v1: 0.994\n            d1v2: 0.761\n            d2v3: 0.695\n      gpt2xl_nucleus095:\n        binary:\n          acc: 0.9912\n          ci95:\n          - 0.9882\n          - 0.9938\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.79\n          ci95:\n          - 0.775\n          - 0.8047\n          auc:\n            d1v2: 0.913\n            d2v3: 0.891\n        4class:\n          acc: 0.8393\n          ci95:\n          - 0.8283\n          - 0.8502\n          auc:\n            d0v1: 0.995\n            d1v2: 0.916\n            d2v3: 0.885\n      gpt2xl_temp09:\n        binary:\n          acc: 0.9978\n          ci95:\n          - 0.9962\n          - 0.999\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.826\n          ci95:\n          - 0.8117\n          - 0.8397\n          auc:\n            d1v2: 0.944\n            d2v3: 0.887\n        4class:\n          acc: 0.8552\n          ci95:\n          - 0.844\n          - 0.866\n          auc:\n            d0v1: 0.997\n            d1v2: 0.939\n            d2v3: 0.886\n      gpt2xl_topk50:\n        binary:\n          acc: 0.9952\n          ci95:\n          - 0.993\n          - 0.9972\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.695\n          ci95:\n          - 0.6777\n          - 0.7113\n          auc:\n            d1v2: 0.844\n            d2v3: 0.766\n        4class:\n          acc: 0.757\n          ci95:\n          - 0.743\n          - 0.7702\n          auc:\n            d0v1: 0.993\n            d1v2: 0.824\n            d2v3: 0.762\n      olmo_nucleus095:\n        binary:\n          acc: 0.9868\n          ci95:\n          - 0.9832\n          - 0.99\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.7503\n          ci95:\n          - 0.7353\n          - 0.7657\n          auc:\n            d1v2: 0.873\n            d2v3: 0.831\n        4class:\n          acc: 0.7897\n          ci95:\n          - 0.7772\n          - 0.8027\n          auc:\n            d0v1: 0.985\n            d1v2: 0.87\n            d2v3: 0.816\n      olmo_temp09:\n        binary:\n          acc: 0.9982\n          ci95:\n          - 0.997\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7633\n          ci95:\n          - 0.7477\n          - 0.7797\n          auc:\n            d1v2: 0.894\n            d2v3: 0.838\n        4class:\n          acc: 0.8263\n          ci95:\n          - 0.8147\n          - 0.8385\n          auc:\n            d0v1: 0.996\n            d1v2: 0.903\n            d2v3: 0.828\n      olmo_topk50:\n        binary:\n          acc: 0.996\n          ci95:\n          - 0.994\n          - 0.9978\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.661\n          ci95:\n          - 0.644\n          - 0.6773\n          auc:\n            d1v2: 0.812\n            d2v3: 0.739\n        4class:\n          acc: 0.7435\n          ci95:\n          - 0.73\n          - 0.758\n          auc:\n            d0v1: 0.995\n            d1v2: 0.831\n            d2v3: 0.738\n    boundary_dilution:\n      d2v3_auc_by_granularity_pythia_nuc:\n        3class: 0.796\n        4class: 0.804\n        6class: 0.689\n      d1v2_auc_by_granularity_pythia_nuc:\n        3class: 0.861\n        4class: 0.868\n        6class: 0.83\n      note: d2v3 AUC drops 14% from 4-class to 6-class (0.804→0.689), confirming decision\n        boundary dilution at higher granularity\n    decoding_strategy_ranking:\n      4class_acc:\n        temp09: 0.814\n        nucleus095: 0.803\n        topk50: 0.732\n      note: topk50 consistently worst across all 3 models; temp09 slightly outperforms\n        nucleus095\n- exp_id: depth_extension_olmo_d4d5_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lr_zscore_cross_strategy_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    raw_lr:\n      mean_acc: 0.25\n      note: lbfgs convergence failure on unscaled features, all predictions random\n      pythia_temp09:\n        acc: 0.25\n        d1v2_auc: 0.6313\n      gpt2xl_temp09:\n        acc: 0.25\n        d1v2_auc: 0.5\n      olmo_temp09:\n        acc: 0.25\n        d1v2_auc: 0.5\n    zscore_lr:\n      mean_acc: 0.6081\n      mean_d1v2: 0.6417\n      pythia_temp09:\n        acc: 0.6139\n        d1v2_auc: 0.5201\n      gpt2xl_temp09:\n        acc: 0.5642\n        d1v2_auc: 0.2386\n      olmo_temp09:\n        acc: 0.5546\n        d1v2_auc: 0.1922\n      pythia_nucleus:\n        acc: 0.6425\n        d1v2_auc: 0.6142\n      gpt2xl_nucleus:\n        acc: 0.7397\n        d1v2_auc: 0.8851\n      olmo_nucleus:\n        acc: 0.748\n        d1v2_auc: 0.8627\n      pythia_topk50:\n        acc: 0.5261\n        d1v2_auc: 0.7711\n      gpt2xl_topk50:\n        acc: 0.5352\n        d1v2_auc: 0.8214\n      olmo_topk50:\n        acc: 0.5484\n        d1v2_auc: 0.8696\n    paper_claim_vs_actual:\n      gpt2xl_temp09_d1v2:\n        paper_raw: 0.13\n        paper_zscore: 0.68\n        actual_raw: 0.5\n        actual_zscore: 0.2386\n      olmo_temp09_d1v2:\n        paper_raw: 0.25\n        paper_zscore: 0.83\n        actual_raw: 0.5\n        actual_zscore: 0.1922\n- exp_id: depth_extension_olmo_d4d5_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.968\n      d2v3_auc: 0.843\n      d3v4_auc: 0.765\n      d4v5_auc: 0.684\n    six_class_rf_accuracy: 0.667\n    edd_at_075: 4\n    edd_note: d3v4=0.765>=0.75 PASS, d4v5=0.684<0.75 FAIL → EDD=4\n- exp_id: n2_deberta_finetune_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_mean: 0.5831\n    accuracy_std: 0.0467\n    per_class_f1:\n      d0: 0.947\n      d1: 0.378\n      d2: 0.247\n      d3: 0.656\n    pairwise_auc:\n      d0v1: 0.981\n      d1v2: 0.733\n      d2v3: 0.755\n    vs_rf_baseline: 58.3% vs 78.2% (-19.9pp)\n    elapsed_seconds: 3727\n- exp_id: n2_roberta_finetune_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_mean: 0.5948\n    accuracy_std: 0.0324\n    per_class_f1:\n      d0: 0.958\n      d1: 0.4161\n      d2: 0.2611\n      d3: 0.6472\n    per_class_precision:\n      d0: 0.9983\n      d1: 0.7178\n      d2: 0.2956\n      d3: 0.4958\n    per_class_recall:\n      d0: 0.9208\n      d1: 0.293\n      d2: 0.2338\n      d3: 0.9314\n    pairwise_auc:\n      d0v1: 0.9886\n      d1v2: 0.7522\n      d2v3: 0.7349\n    fold_accuracies:\n    - 0.6022\n    - 0.5595\n    - 0.5623\n    - 0.6018\n    - 0.648\n    vs_rf_baseline: -18.7pp (59.5% vs 78.2%)\n    vs_deberta: +1.2pp acc, +0.019 d1v2_auc, -0.020 d2v3_auc\n    elapsed_seconds: 1942.5\n- exp_id: temp07_pilot_pythia_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples_per_depth: 500\n    depths: 6\n    six_class_rf_accuracy: 0.5733\n    six_class_rf_ci95:\n    - 0.5333\n    - 0.615\n    six_class_lr_accuracy: 0.5467\n    pairwise_auc_rf:\n      d0v1: 0.9981\n      d1v2: 0.8378\n      d2v3: 0.635\n      d3v4: 0.5997\n      d4v5: 0.6025\n    pairwise_auc_lr:\n      d0v1: 0.9954\n      d1v2: 0.8031\n      d2v3: 0.608\n      d3v4: 0.6525\n      d4v5: 0.5652\n    vs_temp09_d1v2_rf: 0.8378 vs 0.8327 (+0.005)\n    vs_temp09_d1v2_lr: 0.8031 vs 0.7833 (+0.020)\n    d1v2_inversion: false\n    top_features:\n    - p90_ppl\n    - var_surprisal\n    - mean_surprisal\n    - mean_ppl\n    - p75_ppl\n- exp_id: zeroshot_llm_500_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.362\n    accuracy_ci95:\n    - 0.32\n    - 0.404\n    ci_width_pp: 8.4\n    mae: 1.028\n    per_class_f1:\n      d0: 0.55\n      d1: 0.18\n      d2: 0.27\n      d3: 0.18\n    per_class_recall:\n      d0: 0.952\n      d1: 0.128\n      d2: 0.248\n      d3: 0.12\n    vs_rf_baseline: 36.2% vs 78.2% (-42.0pp)\n    vs_200_sample: 36.2% vs 40.0% (consistent, within CI)\n    n_samples: 500\n    n_errors: 0\n- exp_id: feat_ablation_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_19_mean_acc: 0.7847\n    full_19_std: 0.0494\n    top5_mean_acc: 0.7678\n    top5_std: 0.0527\n    top2_mean_acc: 0.7152\n    top2_std: 0.0581\n    n_features_95pct_mean: 4.2\n    n_features_95pct_max: 5\n    best_category_all_cells: perplexity\n    perplexity_cat_mean_acc: 0.7668\n    surprisal_cat_mean_acc: 0.7333\n    lexdiv_cat_mean_acc: 0.4618\n    repetition_cat_mean_acc: 0.4374\n    ngram_entropy_cat_mean_acc: 0.3952\n    first_selected_feature_mode: p90_ppl (6/9)\n    first_selected_feature_alt: var_surprisal (3/9)\n    total_runtime_sec: 7822\n- exp_id: feature_ablation_9cell\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: w2_domain_bias_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subexp_a_d1d3_mean_acc: 0.72\n    subexp_a_range: 59.1%-81.8%\n    subexp_b_logo_mean_acc: 0.721\n    subexp_b_range: 59.5%-81.6%\n    subexp_b_note: 'fixed: per-depth seed assignment, groups now depth-balanced. LOGO=CV\n      within noise'\n    subexp_c_depth_pred_mean: 0.72\n    subexp_c_seed_group_pred_mean: 0.102\n    subexp_c_ratio_mean: 7.06\n    subexp_c_note: seed groups at chance (10.2% vs 10%), no measurable domain bias\n    chance_3class: 0.333\n    chance_seed_group: 0.1\n    paper_updated: section_appendix.tex L54-72, conclusion.tex L14\n- exp_id: shap_supplement_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kendalls_w_three_way: 0.8955\n    rho_shap_gini: 0.9312\n    rho_shap_permutation: 0.8392\n    rho_gini_permutation: 0.76\n    cross_cell_shap_consistency_mean_rho: 0.8\n    p90_ppl_top2_cells: 9/9\n    var_surprisal_top2_cells: 8/9\n    ppl_surprisal_shap_share: 0.888\n    shap_top5: p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl\n    addresses: R3-N3 feature importance cross-validation\n- exp_id: xgboost_lgbm_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    xgb_acc: 0.79\n    xgb_std: 0.0046\n    xgb_d0v1_auc: 1\n    xgb_d1v2_auc: 0.931\n    xgb_d2v3_auc: 0.816\n    lgbm_acc: 0.788\n    lgbm_std: 0.0077\n    lgbm_d0v1_auc: 1\n    lgbm_d1v2_auc: 0.931\n    lgbm_d2v3_auc: 0.814\n    rf_acc_ref: 0.782\n    xgb_recall_d0: 0.994\n    xgb_recall_d1: 0.816\n    xgb_recall_d2: 0.596\n    xgb_recall_d3: 0.754\n    lgbm_recall_d0: 0.994\n    lgbm_recall_d1: 0.815\n    lgbm_recall_d2: 0.596\n    lgbm_recall_d3: 0.747\n- exp_id: xgboost_lgbm_3cell_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt2xl_temp09:\n      RF: 85.8\n      XGBoost: 86.2\n      LightGBM: 86.2\n      d1v2_AUC: 0.98\n      d2v3_AUC: 0.886\n    pythia_nucleus095:\n      RF: 78.8\n      XGBoost: 79\n      LightGBM: 78.9\n      d1v2_AUC: 0.931\n      d2v3_AUC: 0.816\n    pythia_topk50:\n      RF: 68.9\n      XGBoost: 68.9\n      LightGBM: 68.7\n      d1v2_AUC: 0.841\n      d2v3_AUC: 0.689\n- exp_id: wild_data_calibration_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext_n_passages: 546\n    wikitext_d0_pct: 100\n    wikitext_d1_pct: 0\n    wikitext_d2_pct: 0\n    wikitext_d3_pct: 0\n    wikitext_mean_p_d0: 0.9963\n    controlled_d0_mean_p_d0: 0.9941\n    controlled_d0_acc: 100\n    controlled_d1_acc: 99.96\n    controlled_d2_acc: 99.94\n    controlled_d3_acc: 99.9\n    cv5_accuracy: 0.7878\n    cv5_std: 0.0056\n    domain_shift_mean_ppl_pct: +621%\n    domain_shift_var_ppl_pct: +503%\n    domain_shift_p90_ppl_pct: +115%\n    finding: WikiText-103 100% classified as d0 despite large feature-space domain\n      shift in perplexity features; RF robust to distribution shift\n- exp_id: downstream_curation_poc_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    unfiltered:\n      ppl_mean: 15.776\n      ppl_std: 0.066\n      n_samples: 10000\n    rf_strict:\n      ppl_mean: 15.81\n      ppl_std: 0.061\n      n_samples: 2496\n      delta: '-0.034'\n      p: 0.607\n      d: -0.528\n    rf_moderate:\n      ppl_mean: 15.756\n      ppl_std: 0.056\n      n_samples: 4940\n      delta: '+0.021'\n      p: 0.492\n      d: 0.334\n    rf_soft:\n      ppl_mean: 15.733\n      ppl_std: 0.038\n      n_samples: 4422\n      delta: '+0.043'\n      p: 0.407\n      d: 0.792\n    oracle_strict:\n      ppl_mean: 15.879\n      ppl_std: 0.128\n      n_samples: 2500\n      delta: '-0.103'\n      p: 0.216\n      d: -1.004\n    oracle_moderate:\n      ppl_mean: 15.809\n      ppl_std: 0.103\n      n_samples: 5000\n      delta: '-0.033'\n      p: 0.485\n      d: -0.384\n    random_strict:\n      ppl_mean: 16.239\n      ppl_std: 0.165\n      n_samples: 2496\n      delta: '-0.463'\n      p: 0.013\n      d: -3.671\n      sig: true\n    random_moderate:\n      ppl_mean: 15.998\n      ppl_std: 0.09\n      n_samples: 5000\n      delta: '-0.222'\n      p: 0.028\n      d: -2.809\n      sig: true\n    cross_condition:\n      rf_strict_vs_random_strict:\n        delta: 0.429\n        t: -7.052\n        p: 0.002\n        sig: true\n      rf_moderate_vs_random_moderate:\n        delta: 0.242\n        t: -3.77\n        p: 0.02\n        sig: true\n      rf_soft_vs_unfiltered:\n        delta: 0.043\n        t: 0.927\n        p: 0.407\n        sig: false\n      random_strict_vs_unfiltered:\n        delta: -0.463\n        t: 4.219\n        p: 0.014\n        sig: true\n- exp_id: wild_data_c4_supplement_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_n_passages: 5000\n    c4_d0_pct: 79.8\n    c4_d1plus_pct: 20.2\n    c4_d1plus_count: 1012\n    wikitext_d0_pct: 100\n    controlled_accuracy: 99.9%+\n    cv5_accuracy: 0.7878\n    misclassified_feature_diff:\n      rep_4gram: +74.7%\n      rep_3gram: +37.0%\n      p90_ppl: +39.6%\n    misclassified_content_type: ads, product descriptions, SEO template content\n    finding: FPR=0% on editorial text (WikiText), FPR≈20% on web-crawl (C4) — false\n      positives driven by template/low-quality content with high repetition and low\n      diversity, not random noise\n- exp_id: pythia7b_cross_scale_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: wild_data_gpt2xl_calibration_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_accuracy: 0.841\n    cv_std: 0.004\n    wikitext_n_passages: 546\n    wikitext_d0_pct: 99.27\n    wikitext_d1_pct: 0.73\n    c4_n_passages: 5000\n    c4_d0_pct: 77.62\n    c4_d1_pct: 9.04\n    c4_d2_pct: 3.72\n    c4_d3_pct: 9.62\n    c4_fpr_vs_pythia: GPT-2 XL FPR 22.4% vs Pythia 20.2% — consistent template/SEO\n      pattern\n    finding: 'Cross-model calibration consistent: both models flag same C4 template\n      content as non-d0. GPT-2 XL slightly higher FPR due to stronger signal. WikiText\n      near-perfect for both.'\n- exp_id: wild_data_olmo_calibration_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_accuracy: 0.7893\n    cv_std: 0.0039\n    wikitext_n_passages: 546\n    wikitext_d0_pct: 98.53\n    wikitext_non_d0: 8\n    c4_n_passages: 5000\n    c4_d0_pct: 95.28\n    c4_d1_pct: 2.92\n    c4_d2_pct: 0.5\n    c4_d3_pct: 1.3\n    c4_fpr: 4.72\n    finding: OLMo C4 FPR (4.72%) far lower than Pythia (20.2%) and GPT-2 XL (22.4%).\n      OLMo d1-d3 features diverge more from d0, creating wider d0 decision boundary\n      that correctly classifies more C4 template content as d0.\n- exp_id: random_soft_control_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_soft_ppl:\n      seed_42: 15.99\n      seed_123: 16.0276\n      seed_456: 16.1682\n      seed_789: 15.9993\n      seed_1024: 16.1224\n      mean: 16.0615\n      std: 0.0794\n    rf_soft_ppl:\n      seed_42: 15.7134\n      seed_123: 15.7014\n      seed_456: 15.7875\n      seed_789: 15.6956\n      seed_1024: 15.7689\n      mean: 15.7334\n      std: 0.042\n    comparison:\n      delta_ppl: 0.3281\n      t_statistic: 17.9777\n      p_value: 5.6e-05\n      cohens_d: 8.0399\n      significant: true\n    train_loss:\n      seed_42: 1.6748\n      seed_123: 1.6786\n      seed_456: 1.6721\n      seed_789: 1.6736\n      seed_1024: 1.6739\n- exp_id: wild_data_redpajama_dolma_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: wild_data_calibration_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: C4 load_dataset hung - allenai/c4 HF streaming failed on AutoDL proxy.\n      OpenWebText loaded OK (5000 passages, 23s) but C4 load_dataset never returned.\n      JSON written with empty datasets/cross_model_consistency. No error/exception\n      in logs - silent hang during HF Hub streaming.\n- exp_id: wild_data_calibration_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fineweb_n_passages: 5000\n    fineweb_d0_pct: 80.54\n    fineweb_d1_pct: 19.46\n    fineweb_d2_pct: 0\n    fineweb_d3_pct: 0\n    fineweb_fpr: 19.46\n    fineweb_mean_p_d0: 0.7987\n    fineweb_mean_p_d1: 0.1707\n    vs_c4_fpr_delta: -0.74\n    vs_wikitext_fpr_delta: 19.46\n    elapsed_seconds: 87\n    finding: FineWeb FPR=19.46% — virtually identical to C4 FPR=20.2% (Δ=-0.74pp).\n      All misclassifications are d1 only (no d2/d3). Confirms web-crawl FPR ~20% is\n      consistent across datasets and driven by template/SEO content, not dataset-specific\n      artifacts.\n- exp_id: zeroshot_qwen7b_500_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    acc_4class: 0.304\n    acc_4class_ci_95:\n    - 0.2653\n    - 0.3457\n    acc_3class: 0.3173\n    mae: 1.01\n    per_class_recall:\n      d0: 0.264\n      d1: 0.552\n      d2: 0.104\n      d3: 0.296\n    per_class_f1:\n      d0: 0.3143\n      d1: 0.3503\n      d2: 0.1436\n      d3: 0.3442\n    errors: 0\n- exp_id: multi_tau_ablation_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_tau:\n      tau_0.5:\n        4class_acc: 0.7725\n        d1v2_auc: 0.8423\n        d0v1_auc: 0.9962\n        d2v3_auc: 0.7636\n      tau_0.7:\n        4class_acc: 0.754\n        d1v2_auc: 0.8505\n        d0v1_auc: 0.9966\n        d2v3_auc: 0.7197\n      tau_0.9:\n        4class_acc: 0.759\n        d1v2_auc: 0.8083\n        d0v1_auc: 0.9911\n        d2v3_auc: 0.7805\n      tau_1.1:\n        4class_acc: 0.5715\n        d1v2_auc: 0.5284\n        d0v1_auc: 0.9878\n        d2v3_auc: 0.5987\n    cross_tau_loo:\n      holdout_0.5:\n        acc: 0.522\n        d1v2_auc: 0.1756\n      holdout_0.7:\n        acc: 0.4095\n        d1v2_auc: 0.2985\n      holdout_0.9:\n        acc: 0.464\n        d1v2_auc: 0.2774\n      holdout_1.1:\n        acc: 0.471\n        d1v2_auc: 0.5251\n      mean_acc: 0.4666\n      mean_d1v2_auc: 0.3192\n    training_loss:\n      tau_0.5:\n        d0: 2.2727\n        d1: 0.4201\n        d2: 0.1589\n      tau_1.1:\n        d0: 2.2726\n        d1: 1.9077\n        d2: 1.8517\n- exp_id: wild_data_calibration_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    openwebtext_pythia_nucleus:\n      n: 5000\n      d0_pct: 99.1\n      fpr_pct: 0.9\n      mean_p_d0: 0.7116\n    openwebtext_gpt2xl:\n      n: 5000\n      d0_pct: 98.56\n      fpr_pct: 1.44\n      mean_p_d0: 0.6191\n    openwebtext_olmo:\n      n: 5000\n      d0_pct: 97.22\n      fpr_pct: 2.78\n      mean_p_d0: 0.7372\n    wikitext: skipped (dtype error)\n    finding: OpenWebText FPR极低(0.9-2.8%) vs C4(4.7-22.4%) vs FineWeb(19.5%). 编辑质量高的web数据FPR显著低于web-crawl。\n- exp_id: cross_scale_qwen7b_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc: 0.601\n    four_class_ci:\n    - 0.58\n    - 0.621\n    six_class_acc: 0.521\n    six_class_ci:\n    - 0.504\n    - 0.538\n    edd: '>5'\n    pairwise_auc_consecutive:\n      d0v1: 0.969\n      d1v2: 0.729\n      d2v3: 0.709\n      d3v4: 0.732\n      d4v5: 0.772\n    auc_pattern: 'U-shape (non-monotonic: trough at d2v3, rises d3v4/d4v5)'\n- exp_id: wild_data_calibration_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fpr: 15.3\n    d0_accuracy: 84.7\n    n_passages: 5000\n    vs_c4: -4.9pp\n    vs_fineweb: -4.16pp\n    vs_openwebtext: +14.4pp\n- exp_id: cross_scale_llama3_8b_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cross_model_recursive_chain_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: domain_extension_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.741\n    4class_std: 0.02\n    per_depth_f1:\n      d0: 1\n      d1: 0.78\n      d2: 0.52\n      d3: 0.66\n    cv_folds: 5\n    domain: arxiv_abstracts\n- exp_id: two_stage_strategy_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    strategy_classification:\n      mean_acc: 0.575\n      chance: 0.333\n      pythia:\n        acc: 0.523\n        nucleus_recall: 0.533\n        temp09_recall: 0.414\n        topk50_recall: 0.622\n      olmo:\n        acc: 0.548\n        nucleus_recall: 0.608\n        temp09_recall: 0.479\n        topk50_recall: 0.558\n      gpt2xl:\n        acc: 0.654\n        nucleus_recall: 0.845\n        temp09_recall: 0.507\n        topk50_recall: 0.61\n    depth_estimation:\n      cross_strategy_loo_ref: 0.591\n      predicted_two_stage:\n        pythia: 0.693\n        olmo: 0.695\n        gpt2xl: 0.73\n        mean: 0.706\n      naive_pooled:\n        pythia: 0.709\n        olmo: 0.712\n        gpt2xl: 0.739\n        mean: 0.72\n      oracle_two_stage:\n        pythia: 0.746\n        olmo: 0.785\n        gpt2xl: 0.82\n        mean: 0.784\n      within_strategy_ref:\n        pythia: 0.745\n        olmo: 0.784\n        gpt2xl: 0.816\n        mean: 0.782\n    key_finding: Oracle two-stage (78.4%) matches within-strategy (78.2%), validating\n      theory. But predicted two-stage (70.6%) < naive pooled (72.0%) due to strategy\n      classification bottleneck (57.5%).\n- exp_id: cross_model_recursive_chain_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.8475\n    4class_ci95:\n    - 0.81\n    - 0.8825\n    per_depth_f1:\n      d0: 0.98\n      d1: 0.88\n      d2: 0.76\n      d3: 0.76\n    pairwise_auc:\n      d0v1: 0.999\n      d2v3: 0.841\n- exp_id: cross_scale_llama3_8b_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cross_scale_llama3_8b_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.702\n    4class_ci95:\n    - 0.683\n    - 0.724\n    6class_acc: 0.554\n    6class_ci95:\n    - 0.536\n    - 0.571\n    edd_estimate: '4'\n    edd_note: d4v5 AUC=0.618 < T=0.70, so EDD=4. Monotonic decay causes last pair\n      to fall below threshold.\n    consecutive_binary_auc:\n      d0v1: 0.949\n      d1v2: 0.877\n      d2v3: 0.771\n      d3v4: 0.716\n      d4v5: 0.618\n    consecutive_binary_acc:\n      d0v1: 0.885\n      d1v2: 0.81\n      d2v3: 0.698\n      d3v4: 0.656\n      d4v5: 0.583\n- exp_id: ref_model_ablation_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_ref_acc: 0.7854\n    olmo_ref_acc: 0.7451\n    delta_pp: 4.04\n    robust: true\n- exp_id: cross_scale_llama3_base_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.599\n    4class_ci_95:\n    - 0.578\n    - 0.6215\n    6class_acc: 0.4953\n    edd_070: 2\n    auc_d0v1: 0.9175\n    auc_d1v2: 0.7936\n    auc_d2v3: 0.6815\n    auc_d3v4: 0.73\n    auc_d4v5: 0.595\n    monotonic: false\n    pattern: U-shape (d2v3 dip, d3v4 recovery)\n    finding: IT regularizes depth signal (makes AUC monotonic), does not introduce\n      U-shape\n    edd_note: d0v1=0.9175≥0.70, d1v2=0.7936≥0.70, d2v3=0.6815<0.70 → EDD=2\n- exp_id: cross_model_reverse_chain_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.75\n    ci_95:\n    - 82\n    - 89.25\n    forward_chain_acc: 84.75\n    forward_chain_ci:\n    - 81\n    - 88.25\n    conclusion: reverse = forward, architecture confound refuted\n- exp_id: lora_rank_ablation_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rank_4_acc: 0.718\n    rank_4_auc: 0.7896\n    rank_16_acc: 0.7645\n    rank_16_auc: 0.8434\n    rank_64_acc: 0.731\n    rank_64_auc: 0.8326\n    best_rank: 16\n- exp_id: gpt2xl_ref_ablation_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    gpt2xl_4class_acc: 0.6734\n    gpt2xl_ci_95:\n    - 0.6667\n    - 0.6796\n    gpt2xl_d1v2_auc: 0.7269\n    pythia_4class_acc: 0.7854\n    pythia_ci_95:\n    - 0.7795\n    - 0.7911\n    pythia_d1v2_auc: 0.8681\n    delta_pp: -11.2\n- exp_id: second_seed_replication_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.7715\n    ci_95:\n    - 0.764\n    - 0.7815\n    d1v2_auc: 0.8531\n    delta_vs_baseline: -0.0105\n    baseline_acc: 0.782\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - var_ppl\n    - p75_ppl\n    per_class_recall:\n      d0: 0.99\n      d1: 0.816\n      d2: 0.586\n      d3: 0.694\n    fold_accuracies:\n    - 0.77\n    - 0.77\n    - 0.79\n    - 0.7675\n    - 0.76\n- exp_id: mixed_depth_corpus_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mixed_overall_acc: 0.855\n    balanced_overall_acc: 0.7814\n    delta_overall_pp: 7.36\n    mixed_macro_recall: 0.7652\n    balanced_macro_recall: 0.7814\n    delta_macro_recall_pp: -1.62\n    per_class_recall_delta:\n      d0: -0.68\n      d1: -2.43\n      d2: -1.12\n      d3: -2.24\n    max_recall_delta_pp: 2.43\n- exp_id: reference_free_baseline_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    4class_acc: 0.5368\n    ci_95:\n    - 0.5336\n    - 0.5401\n    d1v2_auc: 0.6252\n    full_19_acc: 0.7877\n    delta_pp: -25.09\n    recall_d0: 0.8572\n    recall_d1: 0.397\n    recall_d2: 0.3176\n    recall_d3: 0.5756\n- exp_id: ensemble_reference_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ensemble_4class_acc: 0.7365\n    ensemble_ci_95:\n    - 0.7258\n    - 0.7471\n    pythia_acc: 0.7857\n    olmo_acc: 0.7425\n    gpt2xl_acc: 0.7005\n    delta_vs_gpt2xl: 3.6\n    delta_vs_pythia: -4.9\n- exp_id: gen_length_ablation_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    acc_128: 0.6835\n    ci_128:\n    - 0.6765\n    - 0.6905\n    acc_256: 0.738\n    ci_256:\n    - 0.7248\n    - 0.7512\n    acc_512: 0.7782\n    ci_512:\n    - 0.768\n    - 0.7885\n    d1v2_auc_128: 0.7543\n    d1v2_auc_256: 0.8198\n    d1v2_auc_512: 0.8683\n    spread_pp: 9.47\n    delta_128v256_pp: -5.45\n    delta_512v256_pp: 4.02\n- exp_id: cross_seed_transfer_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_seed42_cv: 0.7868\n    within_seed43_cv: 0.7745\n    within_seed_avg: 0.7807\n    train42_test43: 0.7785\n    train43_test42: 0.7568\n    cross_seed_avg: 0.7676\n    delta_pp: -1.3\n- exp_id: cross_strategy_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    strategy_clf_rf_acc: 0.5779\n    strategy_clf_lr_acc: 0.5291\n    pipeline_depth_acc: 0.7053\n    oracle_depth_acc: 0.7831\n    loo_ref_acc: 0.5908\n    improvement_vs_loo: 0.1145\n    gap_pipeline_vs_oracle: 0.0778\n    pipeline_depth_acc_pythia: 0.6925\n    pipeline_depth_acc_olmo: 0.6937\n    pipeline_depth_acc_gpt2xl: 0.7297\n- exp_id: prompted_gen_gpt2xl_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.6952\n    rf_4class_ci:\n    - 0.689\n    - 0.7015\n    bos_baseline_acc: 0.833\n    delta_vs_bos: -0.1378\n    auc_d0v1: 0.9162\n    auc_d0v2: 0.9934\n    auc_d0v3: 0.9974\n    auc_d1v2: 0.7823\n    auc_d1v3: 0.9553\n    auc_d2v3: 0.7444\n    top5_features:\n    - - p90_ppl\n      - 0.1887\n    - - p75_ppl\n      - 0.1335\n    - - mean_surprisal\n      - 0.0916\n    - - var_surprisal\n      - 0.0849\n    - - p50_ppl\n      - 0.0612\n    n_samples: 20000\n    fold_accuracies:\n    - 0.6885\n    - 0.707\n    - 0.6987\n    - 0.6943\n    - 0.6877\n- exp_id: qwen25_14b_scale_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mlp_19feat_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mlp_128_128_acc: 0.7866\n    mlp_64_128_64_acc: 0.7895\n    mlp_poly_top5_acc: 0.7906\n    best_delta_vs_rf: 0.0086\n    d0v1_auc: 0.997\n    d1v2_auc: 0.878\n    d2v3_auc: 0.821\n- exp_id: qwen25_14b_scale_002\n  name: ''\n  status: RUNNING\n  conclusion: null\n  metrics: {}\n- exp_id: text_length_sensitivity_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: bootstrap_ci_table1_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.4742\n    rf_4class_ci:\n    - 0.467\n    - 0.4811\n    lr_4class_acc: 0.4256\n    rf_3class_acc: 0.4987\n    pairwise_auc_rf:\n      d0v1: 0.653\n      d0v2: 0.819\n      d0v3: 0.902\n      d1v2: 0.62\n      d1v3: 0.807\n      d2v3: 0.664\n    pairwise_auc_lr:\n      d0v1: 0.619\n      d0v2: 0.773\n      d0v3: 0.838\n      d1v2: 0.594\n      d1v3: 0.734\n      d2v3: 0.621\n    top_features:\n    - surprisal_range\n    - surprisal_position_corr\n    - prob_std\n    - surprisal_first_half_minus_second\n    - surprisal_std\n    n_samples: 19992\n- exp_id: plan_018_binoculars_baseline\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: detector_ord_baseline_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: wild_data_features_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_depth_dist:\n      d0: 6598\n      d1: 3354\n      d2: 18\n      d3: 30\n    c4_pct:\n      d0: 65.98\n      d1: 33.54\n      d2: 0.18\n      d3: 0.3\n    c4_fpr: 34.02\n    fineweb_depth_dist:\n      d0: 8285\n      d1: 1708\n      d2: 4\n      d3: 3\n    fineweb_pct:\n      d0: 82.85\n      d1: 17.08\n      d2: 0.04\n      d3: 0.03\n    fineweb_fpr: 17.15\n    total_c4: 10000\n    total_fineweb: 10000\n    rf_n_estimators: 200\n    rf_train_samples: 20000\n- exp_id: learned_estimator_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: downstream_benchmark_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: downstream_benchmark_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_ppl: 5.67\n    d0_only_ppl: 5.65\n    d1_only_ppl: 5.55\n    d2_only_ppl: 5.56\n    mixed_all_ppl: 5.55\n    best_model: d1_only\n    ppl_improvement_vs_baseline: 0.12 (2.1%)\n- exp_id: learned_estimator_proto_fix_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_accuracy: 0.6664\n    gpt2xl_acc: 0.6835\n    pythia_acc: 0.6155\n    olmo_acc: 0.7001\n    mean_mae: 0.384\n    mean_pairwise_auc: 0.874\n    gpt2xl_auc: 0.8926\n    pythia_auc: 0.8415\n    olmo_auc: 0.9004\n- exp_id: learned_estimator_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    xgboost_pythia: 63.72\n    xgboost_olmo: 69.76\n    xgboost_gpt2xl: 68.05\n    xgboost_mean: 67.18\n    ordinal_mlp_pythia: 62.52\n    ordinal_mlp_olmo: 69.69\n    ordinal_mlp_gpt2xl: 67.9\n    ordinal_mlp_mean: 66.7\n    prototypical_pythia: 61.55\n    prototypical_olmo: 70.01\n    prototypical_gpt2xl: 68.35\n    prototypical_mean: 66.64\n    rf_baseline_mean: 66.4\n    best_single: proto_olmo_70.01\n    best_method_mean: xgboost_67.18\n- exp_id: qwen25-1p5b-instruct-001-phase45\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-001-ph45\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-001-ph45v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-001-ph45v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25_14b_scale_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: gpt2xl_seed43_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 86.32\n    rf_4class_ci_lower: 86.17\n    rf_4class_ci_upper: 86.49\n    d1v2_auc: 0.9489\n    per_class_recall:\n      d0: 99.4\n      d1: 92\n      d2: 73.4\n      d3: 80.5\n    seed42_rerun_acc: 84.28\n    seed42_rerun_ci:\n    - 83.89\n    - 84.77\n    delta_vs_seed42: 2.04\n- exp_id: pythia_seed43_001\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.7884\n    rf_4class_ci_lower: 0.7813\n    rf_4class_ci_upper: 0.7952\n    d1v2_auc: 0.8759\n    per_class_recall:\n      d0: 0.992\n      d1: 0.8248\n      d2: 0.5882\n      d3: 0.7486\n    fold_accs:\n    - 0.8015\n    - 0.7855\n    - 0.786\n    - 0.7932\n    - 0.7758\n    delta_vs_seed42: 0.0064\n    seed42_baseline: 0.782\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - var_ppl\n    - mean_surprisal\n- exp_id: olmo_seed43_001\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: theory_section\n  claim: '2'\n  description: 'Theoretical analysis section connecting depth signal to model collapse\n    theory: (1) tail erosion mechanism explaining p90_ppl/var_surprisal dominance\n    via Shumailov et al., (2) EDD upper bound derivation from Dohmatob contraction\n    rates, (3) strategy-dependent convergence rate explaining temp09 trajectory reversal.\n    Half-page theoretical sketch with experimental validation.'\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T16:03:35.207Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T16:03:35.207Z",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-18T16:03:35.236Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：14B scale validation succeeds with strong signal, theory section provides testable predictions that match data, existing detectors fail at ordinal task — all 3 claims hold at full strength, paper type accepted as task formalization + systematic empirical study
核心假设：['14B (Qwen2.5-14B FP16) 4-class acc ≥72%, feature universality confirmed (p90_ppl + var_surprisal both in top-3)', '14B EDD=4, consistent with 3/3 models at 1B scale → EDD cross-scale consistency claim enabled', 'Theory section derives EDD upper bound from Dohmatob contraction rates that matches empirical EDD=4; tail erosion mechanism (Shumailov) explains p90_ppl/var_surprisal dominance with quantitative prediction', 'Binoculars/Fast-DetectGPT ordinal calibration ≤40% 4-class acc → confirms ordinal depth is genuinely new capability', '3/3 model seed stability confirmed (GPT-2 XL Δ=2.0pp, Pythia Δ=0.6pp, OLMo Δ<3pp) — variance well below method gap', 'Instruct model weakness (47.4%) accepted as expected RLHF alignment tax, brief mechanistic explanation sufficient']
关键指标范围：{'14b_4class_acc': [0.72, 0.82], '14b_d1v2_auc': [0.8, 0.92], '14b_edd': [4, 4], '14b_top2_feature_overlap_with_1b': [2, 2], 'existing_detector_ordinal_4class_acc': [0.25, 0.4], 'seed_robustness_max_delta_pp': [0.6, 3.0], 'theory_edd_bound_vs_empirical_error': [0, 1], 'simulated_reviewer_meta_score': [3.5, 4.0], 'accept_probability': [0.55, 0.75]}
叙事方向：Original framing 完全成立。三条 Claims 无需调整强度。 Title: "Estimating Recursive Generation Depth: A Depth Degradation Atlas for Multi-Generational Synthetic Text"。 Claim 1 ("feasible, accurate, robust across scales"): 14B 结果直接支撑 "1B-14B scale robustness" 子句，prompted gen 支撑 ecological validity。 Claim 2 (Atlas as PRIMARY): 理论节提供 tail erosion → p90_ppl 的因果链 + EDD 上界推导，Atlas 从纯经验观察升级为 "theory-guided empirical characterization"。 Claim 3 (cross-strategy pipeline): +11.5pp 改进 + 已确认的 temperature convergence 机制 = 完整贡献。 Discussion: instruct model 作为 "alignment regularizes depth signal — future work on instruction-tuned chains"，不削弱主体。 定位: EMNLP "New Missions" track，task formalization + theory-grounded Atlas + practical framework。 与 prior Dream (3.0/3.0/2.5) 的差异: theory section 填补 "no algorithmic contribution" 空缺，14B 消除 "small model only" 降级风险，seed robustness 消除 "cherry-picked split" 质疑。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: recursive_gen_depth_est
focus: Evaluate whether adding a theoretical analysis section (connecting to model collapse theory) plus completed 14B scale validation and 3/3 model seed robustness coverage can push the paper from 3.0 Findings to 4.0 Conference accept. Pay special attention to: (1) whether the theory section adequately addresses the 'no algorithmic contribution' concern, (2) remaining gaps that would prevent 4.0, (3) whether the paper's positioning as 'empirical study + theoretical grounding + task formalization' is sufficient for EMNLP Main.

## paper_framing.md

# Paper Framing — recursive_gen_depth_est

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25, 2026)
- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)
- EMNLP 2026 special theme "New Missions for NLP Research" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit

## Core Claims (3 条 + Discussion implication)

1. **Ordinal depth estimation is feasible, accurate, and robust across scales and generation modes**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark (1–1.5B), Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all settings. **Scale robustness**: Clean FP16 13B experiment (Qwen2.5-14B, no quantization) confirms depth signal persists at mainstream model scale, addressing the "small model only" concern from prior 7B QLoRA experiments. **Ecological validity**: Prompted generation experiment (topic-seeded text, not BOS-only unconditional) confirms depth signal is not an artifact of unnatural generation mode.

2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the d1/d2 boundary remains open. This atlas spans 3 model families × 3 decoding strategies, with scale consistency confirmed at 14B.

3. **Cross-strategy depth estimation via two-stage pipeline + strategy-invariant signal discovery**: Naive cross-strategy transfer degrades to 59.1% with d1v2 boundary inversion. We propose a two-stage solution: (a) strategy identification classifier (57.8% — strategies share more feature space than expected), then (b) strategy-conditioned depth classifiers. The pipeline improves cross-strategy accuracy by **+11.5pp** on average (59.1% → 70.5%), with per-model results: GPT-2 XL 73.0%, OLMo 69.4%, Pythia 69.3%. Oracle ceiling at 78.3%. **Caveat**: improvement is consistent across models but absolute accuracy varies (2/3 models individually below 70%); paper must claim "+11.5pp improvement" rather than "≥70% universal recovery". The surprising finding: even with imperfect strategy routing, the pipeline works because depth signal has a **strategy-invariant core** (~60% accuracy floor) plus a strategy-specific component. This reframes cross-strategy transfer from "broken" to "substantially improved with clear ceiling for future work".

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
10. "Cross-strategy deployment is unreliable" → **Now addressed by Claim 3**: Two-stage pipeline (strategy identification → strategy-conditioned depth classification) provides a practical solution. Strategy classifier achieves 57.8% accuracy on 19 features (below the expected >90%), indicating strategy distributions are less separable than anticipated. A two-stage pipeline (oracle strategy identification + strategy-conditioned depth classification) recovers 11.5pp over naive LOO, though practical deployment still requires either strategy metadata or improved routing. The root cause (temperature's accelerated convergence) is identified and the mechanism explained.
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
  registry_id: qwen25_14b_scale_002
  status: RUNNING
  conclusion: null
- id: plan_015
  claim: 2
  description: 'Wild-data calibration: C4/FineWeb/RedPajama subsets → trained RF depth
    classification'
  priority: P0
  gpu_budget_hours: 6
  deps:
  - plan_001b
  - plan_002
  - plan_003
  notes: D038 reactivated. 从 C4/FineWeb/RedPajama 抽取子集，用已训练 reference model 提取 19
    特征，用 3×3 训练好的 RF 分类器做 depth 预测 + 分布分析。验证 depth signal 在野生数据中是否存在。需要 GPU 跑 reference
    model 推理。
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
  registry_id: prompted_gen_gpt2xl_001
  status: DONE
  conclusion: success
  metrics:
    rf_4class_acc: 0.6952
    rf_4class_ci:
    - 0.689
    - 0.7015
    bos_baseline_acc: 0.833
    delta_vs_bos: -0.1378
    auc_d0v1: 0.9162
    auc_d0v2: 0.9934
    auc_d0v3: 0.9974
    auc_d1v2: 0.7823
    auc_d1v3: 0.9553
    auc_d2v3: 0.7444
    top5_features:
    - - p90_ppl
      - 0.1887
    - - p75_ppl
      - 0.1335
    - - mean_surprisal
      - 0.0916
    - - var_surprisal
      - 0.0849
    - - p50_ppl
      - 0.0612
    n_samples: 20000
    fold_accuracies:
    - 0.6885
    - 0.707
    - 0.6987
    - 0.6943
    - 0.6877
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
  registry_id: cross_strategy_pipeline_001
  status: DONE
  conclusion: success
  metrics:
    strategy_clf_rf_acc: 0.5779
    strategy_clf_lr_acc: 0.5291
    pipeline_depth_acc: 0.7053
    oracle_depth_acc: 0.7831
    loo_ref_acc: 0.5908
    improvement_vs_loo: 0.1145
    gap_pipeline_vs_oracle: 0.0778
    pipeline_depth_acc_pythia: 0.6925
    pipeline_depth_acc_olmo: 0.6937
    pipeline_depth_acc_gpt2xl: 0.7297
- id: plan_018
  claim: 1
  description: 'Existing detector ordinal baseline: Binoculars + Fast-DetectGPT scores
    calibrated for ordinal depth estimation'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - plan_001a
  - plan_002
  - plan_003
  notes: 'Dream 三档一致 #1 缺口。将 Binoculars/Fast-DetectGPT 连续分数校准为 ordinal bin，在 3×3 已有数据上评估。即使
    negative 也加强论文。需要少量 GPU 跑推理。D036。'
  status: planned
- id: plan_019
  claim: 1
  description: 'MLP on 19 features: neural classifier baseline on same feature set'
  priority: P1
  gpu_budget_hours: 0.5
  deps:
  - plan_001a
  registry_id: mlp_19feat_001
  notes: DONE. MLP delta ≤3pp vs RF，确认特征是瓶颈而非分类器选择。CPU only。
  status: DONE
  conclusion: success
  metrics:
    mlp_128_128_acc: 0.7866
    mlp_64_128_64_acc: 0.7895
    mlp_poly_top5_acc: 0.7906
    best_delta_vs_rf: 0.0086
    d0v1_auc: 0.997
    d1v2_auc: 0.878
    d2v3_auc: 0.821
- id: plan_020
  claim: 1
  description: 'Table 1 bootstrap CIs: 5-fold CV bootstrap confidence intervals for
    all 9 cells'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001a
  - plan_002
  - plan_003
  notes: Dream 三档均要求。从已有 5-fold CV 结果计算 bootstrap CI。纯 CPU 分析任务。
  status: planned
- id: plan_021
  claim: 1
  description: 'Instruction-tuned model validation: Qwen2.5-1.5B-Instruct recursive
    chain (nucleus, d0-d3) to test depth signal on instruct models'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - plan_001a
  notes: D037 Manager 自查发现最大缺口。2024-2025 检测论文标配 instruct model。Qwen2.5-1.5B-Instruct
    nucleus d0-d3，19 特征提取 + RF/LR 分类。结果进 Appendix。cuda:1 在 plan_016 完成后跑。
  registry_id: qwen25-1p5b-instruct-001
  status: DONE
  conclusion: success
  metrics:
    rf_4class_acc: 0.4742
    rf_4class_ci:
    - 0.467
    - 0.4811
    lr_4class_acc: 0.4256
    rf_3class_acc: 0.4987
    pairwise_auc_rf:
      d0v1: 0.653
      d0v2: 0.819
      d0v3: 0.902
      d1v2: 0.62
      d1v3: 0.807
      d2v3: 0.664
    pairwise_auc_lr:
      d0v1: 0.619
      d0v2: 0.773
      d0v3: 0.838
      d1v2: 0.594
      d1v3: 0.734
      d2v3: 0.621
    top_features:
    - surprisal_range
    - surprisal_position_corr
    - prob_std
    - surprisal_first_half_minus_second
    - surprisal_std
    n_samples: 19992
- id: plan_022
  claim: 1
  description: 'Text length sensitivity analysis: evaluate depth estimation accuracy
    at 50/100/200/500 token truncation lengths'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001a
  - plan_002
  - plan_003
  registry_id: text_length_sensitivity_001
  notes: DONE. 准确率随截断长度优雅降级，关键特征(surprisal moments, entropy)在100-200 tokens内收敛，方法对短文本实用。
  status: DONE
  conclusion: success
- id: plan_023
  claim: 2
  description: 'Theoretical analysis: connect depth signal to model collapse theory,
    derive EDD upper bound'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001a
  - plan_006
  notes: 'D038. CPU/写作任务。(1) 为什么 p90_ppl 和 var_surprisal 能区分 depth: 连接到 Shumailov
    et al. 2024 model collapse 中 tail distribution 消失现象。(2) EDD 上界推导: 基于递归生成的 fixed-point
    attractor 理论。(3) 与实验 EDD=4 结果对照验证。产出: paper Theory section 草稿。'
  status: planned
- id: plan_024
  claim: 3
  description: 'Downstream benchmark impact: depth-filtered training data → HellaSwag/ARC
    evaluation'
  priority: P0
  gpu_budget_hours: 12
  deps:
  - plan_001a
  - plan_013
  notes: D038. 扩展 plan_013 data efficiency story。用 depth estimator 过滤训练数据(移除 high-depth
    text)，在 HellaSwag/ARC/PIQA 上评估下游 LM 质量。3 个过滤阈值 × 3 个 benchmark。需要 GPU 做 LM training
    + eval。
  registry_id: downstream_benchmark_001
  status: DONE
  conclusion: failed
- id: plan_025
  claim: 1
  description: 'Learned depth estimator: metric learning on 19-feature space for zero-shot
    cross-model generalization'
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_001b
  - plan_002
  - plan_003
  - plan_005
  notes: 'D038. 从 RF 特征重要性出发，训练 lightweight MLP/prototypical network 做 ordinal depth
    estimation，目标: 在 leave-one-model-out 上超过 RF baseline (66.4%)。如果成功→方法贡献升级；失败→作为
    negative analysis 支持"特征是瓶颈"结论。'
  registry_id: learned_estimator_001
  status: DONE
  conclusion: negative
- id: plan_026
  claim: 1
  description: 'API model recursive chains: GPT-4o-mini fine-tuning API + prompted
    chain for d0-d3 depth estimation'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001a
  notes: 'D038. 两种方式验证 API 模型: (a) GPT-4o-mini fine-tuning API 递归链 (需 OpenAI key)。(b)
    Prompted recursive chain (rewrite/continue, 无需 fine-tune, 可用任意 API)。验证 depth signal
    在商用模型中是否存在。'
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
- exp_id: cross_strategy_pipeline_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    strategy_clf_rf_acc: 0.5779
    strategy_clf_lr_acc: 0.5291
    pipeline_depth_acc: 0.7053
    oracle_depth_acc: 0.7831
    loo_ref_acc: 0.5908
    improvement_vs_loo: 0.1145
    gap_pipeline_vs_oracle: 0.0778
    pipeline_depth_acc_pythia: 0.6925
    pipeline_depth_acc_olmo: 0.6937
    pipeline_depth_acc_gpt2xl: 0.7297
- exp_id: prompted_gen_gpt2xl_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rf_4class_acc: 0.6952
    rf_4class_ci:
    - 0.689
    - 0.7015
    bos_baseline_acc: 0.833
    delta_vs_bos: -0.1378
    auc_d0v1: 0.9162
    auc_d0v2: 0.9934
    auc_d0v3: 0.9974
    auc_d1v2: 0.7823
    auc_d1v3: 0.9553
    auc_d2v3: 0.7444
    top5_features:
    - - p90_ppl
      - 0.1887
    - - p75_ppl
      - 0.1335
    - - mean_surprisal
      - 0.0916
    - - var_surprisal
      - 0.0849
    - - p50_ppl
      - 0.0612
    n_samples: 20000
    fold_accuracies:
    - 0.6885
    - 0.707
    - 0.6987
    - 0.6943
    - 0.6877
- exp_id: qwen25_14b_scale_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mlp_19feat_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mlp_128_128_acc: 0.7866
    mlp_64_128_64_acc: 0.7895
    mlp_poly_top5_acc: 0.7906
    best_delta_vs_rf: 0.0086
    d0v1_auc: 0.997
    d1v2_auc: 0.878
    d2v3_auc: 0.821
- exp_id: qwen25_14b_scale_002
  name: ''
  status: RUNNING
  conclusion: null
  metrics: {}
- exp_id: text_length_sensitivity_001
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: bootstrap_ci_table1_001
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: qwen25-1p5b-instruct-001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rf_4class_acc: 0.4742
    rf_4class_ci:
    - 0.467
    - 0.4811
    lr_4class_acc: 0.4256
    rf_3class_acc: 0.4987
    pairwise_auc_rf:
      d0v1: 0.653
      d0v2: 0.819
      d0v3: 0.902
      d1v2: 0.62
      d1v3: 0.807
      d2v3: 0.664
    pairwise_auc_lr:
      d0v1: 0.619
      d0v2: 0.773
      d0v3: 0.838
      d1v2: 0.594
      d1v3: 0.734
      d2v3: 0.621
    top_features:
    - surprisal_range
    - surprisal_position_corr
    - prob_std
    - surprisal_first_half_minus_second
    - surprisal_std
    n_samples: 19992
- exp_id: plan_018_binoculars_baseline
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: detector_ord_baseline_001
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: wild_data_features_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_depth_dist:
      d0: 6598
      d1: 3354
      d2: 18
      d3: 30
    c4_pct:
      d0: 65.98
      d1: 33.54
      d2: 0.18
      d3: 0.3
    c4_fpr: 34.02
    fineweb_depth_dist:
      d0: 8285
      d1: 1708
      d2: 4
      d3: 3
    fineweb_pct:
      d0: 82.85
      d1: 17.08
      d2: 0.04
      d3: 0.03
    fineweb_fpr: 17.15
    total_c4: 10000
    total_fineweb: 10000
    rf_n_estimators: 200
    rf_train_samples: 20000
- exp_id: learned_estimator_001
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: downstream_benchmark_001
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: downstream_benchmark_002
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    baseline_ppl: 5.67
    d0_only_ppl: 5.65
    d1_only_ppl: 5.55
    d2_only_ppl: 5.56
    mixed_all_ppl: 5.55
    best_model: d1_only
    ppl_improvement_vs_baseline: 0.12 (2.1%)
- exp_id: learned_estimator_proto_fix_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mean_accuracy: 0.6664
    gpt2xl_acc: 0.6835
    pythia_acc: 0.6155
    olmo_acc: 0.7001
    mean_mae: 0.384
    mean_pairwise_auc: 0.874
    gpt2xl_auc: 0.8926
    pythia_auc: 0.8415
    olmo_auc: 0.9004
- exp_id: learned_estimator_002
  name: ''
  status: DONE
  conclusion: success
  metrics:
    xgboost_pythia: 63.72
    xgboost_olmo: 69.76
    xgboost_gpt2xl: 68.05
    xgboost_mean: 67.18
    ordinal_mlp_pythia: 62.52
    ordinal_mlp_olmo: 69.69
    ordinal_mlp_gpt2xl: 67.9
    ordinal_mlp_mean: 66.7
    prototypical_pythia: 61.55
    prototypical_olmo: 70.01
    prototypical_gpt2xl: 68.35
    prototypical_mean: 66.64
    rf_baseline_mean: 66.4
    best_single: proto_olmo_70.01
    best_method_mean: xgboost_67.18
- exp_id: qwen25-1p5b-instruct-001-phase45
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen25-1p5b-instruct-001-ph45
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen25-1p5b-instruct-001-ph45v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen25-1p5b-instruct-001-ph45v3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen25-1p5b-instruct-002
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen25_14b_scale_003
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: gpt2xl_seed43_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    rf_4class_acc: 86.32
    rf_4class_ci_lower: 86.17
    rf_4class_ci_upper: 86.49
    d1v2_auc: 0.9489
    per_class_recall:
      d0: 99.4
      d1: 92
      d2: 73.4
      d3: 80.5
    seed42_rerun_acc: 84.28
    seed42_rerun_ci:
    - 83.89
    - 84.77
    delta_vs_seed42: 2.04
- exp_id: pythia_seed43_001
  name: ''
  status: ANALYZING
  conclusion: success
  metrics:
    rf_4class_acc: 0.7884
    rf_4class_ci_lower: 0.7813
    rf_4class_ci_upper: 0.7952
    d1v2_auc: 0.8759
    per_class_recall:
      d0: 0.992
      d1: 0.8248
      d2: 0.5882
      d3: 0.7486
    fold_accs:
    - 0.8015
    - 0.7855
    - 0.786
    - 0.7932
    - 0.7758
    delta_vs_seed42: 0.0064
    seed42_baseline: 0.782
    top_features:
    - var_surprisal
    - p90_ppl
    - mean_ppl
    - var_ppl
    - mean_surprisal
- exp_id: olmo_seed43_001
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics: {}


## what_if (hypothetical experiments — additive)

- name: theory_section
  claim: '2'
  description: 'Theoretical analysis section connecting depth signal to model collapse
    theory: (1) tail erosion mechanism explaining p90_ppl/var_surprisal dominance
    via Shumailov et al., (2) EDD upper bound derivation from Dohmatob contraction
    rates, (3) strategy-dependent convergence rate explaining temp09 trajectory reversal.
    Half-page theoretical sketch with experimental validation.'
  estimated_gpu_hours: 0.0

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
  "promptId": "91d69094-6e31-4251-b8ae-2ccda51109fb",
  "type": "user",
  "uuid": "0f7d5409-ae57-4760-ad41-84451c8a0e2c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T16:03:35.231Z_

```json
{
  "parentUuid": "0f7d5409-ae57-4760-ad41-84451c8a0e2c",
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
  "uuid": "329b4188-c4ef-4bf6-aaf5-0eb75f5778fb",
  "timestamp": "2026-05-18T16:03:35.231Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T16:03:35.231Z_

```json
{
  "parentUuid": "329b4188-c4ef-4bf6-aaf5-0eb75f5778fb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fe66f9b8-ae0a-48a1-ba6a-80df1d299ab5",
  "timestamp": "2026-05-18T16:03:35.231Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：14B scale validation succeeds with strong signal, theory section provides testable predictions that match data, existing detectors fail at ordinal task — a…",
  "leafUuid": "fe66f9b8-ae0a-48a1-ba6a-80df1d299ab5",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation for recursive synthetic text with model collapse theory",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

### Assistant

_source line 8 · 2026-05-18T16:10:53.912Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for every `planned` experiment in the experiment_plan, under the "best" tier definition. Let me identify all planned experiments:

1. **plan_014** (RUNNING) - 13B clean FP16 scale validation (Qwen2.5-14B)
2. **plan_015** (planned) - Wild-data calibration: C4/FineWeb/RedPajama
3. **plan_018** (planned) - Existing detector ordinal baseline: Binoculars + Fast-DetectGPT


4. **plan_020** (planned) - Table 1 bootstrap CIs
5. **plan_023** (planned) - Theoretical analysis
6. **plan_026** (planned) - API model recursive chains

I also need to handle the what_if for the theoretical analysis section. Let me double-check which experiments actually have status "planned" — plan_010 is marked as planned but was cancelled due to DCOL v6 failure, so I should exclude it. The active planned experiments are plan_015, plan_018, plan_020, plan_023, and plan_026.

Actually, plan_014 is currently RUNNING, not planned, but since it's central to the best tier's core assumptions around 14B validation, I should include it. Looking at the best tier definition, the critical assumptions are that 14B achieves 4-class accuracy ≥72% with confirmed feature universality, EDD=4 consistent across scales, and a theoretical section that derives the EDD upper bound from contraction rates while explaining the dominance of p90_ppl and var_surprisal through tail erosion mechanisms.

The next tier requirements include confirming that Binoculars and Fast-DetectGPT ordinal calibration stays below 40% 4-class accuracy to validate ordinal depth as a genuinely new capability, verifying seed stability across the three models with variance well below the method gap, and accepting the instruct model weakness at 47.4% as an expected RLHF alignment cost. The key metric ranges I'm tracking are 14B 4-class accuracy between 0.72-0.82, D1V2 AUC between 0.8-0.92, and EDD fixed at 4.

Now I'm looking at the expected ranges for feature overlap with the 1B model, existing detector ordinal performance, seed robustness variance, and the theory-to-empirical error bounds. These metrics feed into my simulated reviewer score and overall accept probability estimate. I need to map out all the remaining experiments—both those currently running and those still planned—to construct detailed predictions for each one under the best-case tier. So I'm looking at the planned experiments and the one that's currently running. Plan_014 is the Qwen2.5-14B scale validation that's still in progress, and I need to set expectations for what the best tier results should show - around 72% accuracy on the 4-class task, AUC between 0.8 and 0.92 for the d1v2 metric, an EDD of 4, and both p90_ppl and var_surprisal performing in the top 3 metrics.

At the 14B scale, the model has substantially more capacity than the 1B baseline, which should make it more resistant to distribution collapse during recursive fine-tuning since it can maintain more information across depth steps. However, the core mechanism of tail distribution erosion still applies because it's fundamentally constrained by the finite training data bottleneck rather than model capacity. The best tier prediction assumes this signal remains strong enough to hit that 72%+ accuracy threshold. The same statistical features should generalize across scales since they're capturing underlying distributional properties that don't depend on model size.

I'm expecting the 4-class accuracy to land around 0.76, sitting comfortably in the 0.72-0.82 range though potentially slightly lower than the 1B best case since larger models degrade more gradually. The d1v2 AUC should come in around 0.86.

Now I'm looking at the remaining metrics — d0v1 should be nearly perfect at 0.99, d2v3 around 0.78, and the EDD estimate is 4 based on binary pairwise comparisons across depths 0-5. The top discriminative features are p90_ppl and var_surprisal, both landing in the top-3.

For the wild data calibration work, I'm extending the existing analysis by evaluating C4, FineWeb, and RedPajama subsets using the trained RF classifiers. Looking at what's already been done, WikiText shows clean d0 classification while C4 sits around 80% d0 accuracy with roughly 20% false positive rate, FineWeb performs better at 17% FPR, and OpenWebText is nearly perfect with FPR between 0.9-2.8%.

The wild data patterns are holding up well — false positives cluster around template and SEO content, and I'm seeing consistent behavior across different models. For the Binoculars and Fast-DetectGPT baseline, I expect these binary detectors to struggle with the ordinal task, probably hitting around 40% accuracy on 4-class classification since they were never designed to discriminate between depth levels. The bootstrap confidence intervals for Table 1 should be tight enough to validate the claims. On the theoretical side, I'm aiming to derive an upper bound for EDD that matches the empirical value of 4 within a [0,1] error margin, with the tail erosion mechanism explaining why p90_ppl and var_surprisal dominate. For the API model recursive chains work, I'm still setting up the framework.

Now I'm checking whether the depth signal shows up consistently across API models too, which would strengthen the universality claim. I also need to account for the OLMo seed43 experiment since seed robustness factors into the best tier criteria, though that one's still running. Let me focus on the planned experiments from the registry and map out the YAML structure for the detailed data breakdown.

Looking at the experiment_plan entries, I'm filtering for status=planned and including plan_014 even though it's RUNNING since it's directly relevant. I'll skip plan_010 since it's marked cancelled. For the Qwen2.5-14B FP16 validation, I'm predicting that the larger model will show slower collapse dynamics compared to the 1B baseline—the per-step signal weakens but the model still hits the finite data bottleneck. At 14B scale, discriminability should hold at least as far as the 1B results, so I'm expecting the 4-class accuracy around 0.76 with a range of 0.72-0.82.

For the detailed metrics, I'm setting the AUC progression to show strong early separation (0.990 at d0v1) that gradually erodes through the fine-tuning steps, hitting the EDD threshold of 4 where d3v4 stays above 0.75 but d4v5 drops below. The top features should remain consistent with the 1B findings—perplexity percentiles and surprisal variance dominating the signal. The key insight is that the 14B model's larger capacity means each fine-tuning iteration produces a smaller distributional shift, so tail erosion from the recursive process takes longer to manifest, but the underlying mechanism is identical, which is why EDD stays at 4 rather than extending further.

Now I'm moving to the wild-data calibration plan, where I'll use the existing FPR baselines from C4 and FineWeb to predict how the trained classifiers should perform across the distribution shift tiers. The expectation is that C4's lower data quality shows higher false positive rates early on, while FineWeb's cleaner distribution maintains better separation through the later tiers.

The key insight here is that web-crawl corpora naturally contain low-quality content—templates, SEO spam, machine translations—that genuinely shares statistical properties with synthetic text, so these aren't really false positives but rather the classifier correctly flagging text with synthetic-like characteristics. FineWeb's aggressive filtering explains its higher d0 accuracy, and RedPajama should land somewhere in between based on its curation approach.

Now looking at how existing detectors perform on the ordinal classification task: Binoculars and Fast-DetectGPT both excel at the binary real-versus-synthetic distinction but struggle significantly when trying to distinguish between intermediate depth levels. They're optimized around a single scalar metric—cross-perplexity ratio or conditional probability curvature—which captures the boundary between d0 and synthetic text but lacks the granularity needed for finer-grained depth discrimination.

The core issue is that their score distributions for d1, d2, and d3 overlap substantially because a single dimension can't encode the multi-faceted signal of recursive degradation. Without multi-dimensional features, calibrating continuous scores to ordinal bins becomes underdetermined. Since these detectors were built for the sharp human-machine divide rather than the gradual progression through depth levels, ordinal estimation genuinely requires a different approach with richer feature representations.

For the bootstrap confidence intervals on Table 1, I'm expecting all nine cells to have sufficiently narrow intervals to support the claims, with mean CI widths around 2.5–3.5 percentage points and no cell crossing the 25% chance threshold.  Given roughly 20,000 samples per cell and 5-fold cross-validation, the intervals should be tight (±1.5–2pp), and since fold-level variance is already small, bootstrap resampling will confirm the statistical reliability of the existing results.

For the theoretical analysis, I'm deriving an upper bound on effective decision depth that should match the empirical EDD of 4 within reasonable error, with tail erosion explaining why certain features dominate the classification. / log(1/γ)⌉ where γ is the contraction rate from Dohmatob (2024)
- For typical γ ≈ 0.7-0.8 and ε ≈ 0.05 (AUC resolution), bound gives EDD ≤ 4-5
- Empirical EDD=4 falls within the theoretical bound
- Tail erosion mechanism: connects Shumailov's "tail trimming" to p90_ppl dominance
  - Each recursive step shrinks the tail of the token probability distribution
  - p90_ppl captures exactly this tail contraction
  - var_surprisal captures the reduced spread of the surprisal distribution as tails erode
  - Quantitative prediction: p90_ppl should decrease monotonically with depth (confirmed in atlas data)
- Strategy-dependent convergence: temperature's uniform logit scaling accelerates convergence to the attractor by rescaling rather than truncating, which shifts more probability mass per step. The theoretical foundation here is Dohmatob's result showing that iterative retraining on synthetic data produces distributions converging geometrically to a fixed point, with contraction rate γ determined by the ratio of synthetic to real data and model capacity. For full-synthetic chains, γ depends on how well the model approximates its own output distribution, and at each step the KL divergence contracts by factor γ. The EDD threshold is where consecutive distributions fall below the classifier's detection threshold ε, giving roughly log(ε)/log(γ), which for Pythia-1.4B with γ ≈ 0.75 yields the observed behavior.

Now I'm looking at the fine-tuning loss progression across depths—it drops from 2.22 at d0 to 1.37 at d1, then 1.01 at d2, and stabilizes around 0.83 at d3, with the contraction ratio staying between 0.73-0.78. This empirical contraction rate aligns well with the theoretical γ, and when I map the AUC=0.75 detection threshold to KL divergence around 0.05, the bound predicts EDD ≈ 10.4, but the actual EDD=4 suggests the classifier operates at roughly 40% efficiency relative to the information-theoretic limit, which makes sense for a random forest on 19 features. Next I'm planning to test this on API models with GPT-4o-mini fine-tuning chains expecting 4-class accuracy around 65-72%.

For the recursive chain approach without fine-tuning, I expect accuracy to drop to 55-65% because the prompted rewrites don't fully replace the model's base distribution—they just condition it. The depth signal should still be present but weaker since API models are heavily regularized through RLHF and DPO alignment, similar to how the instruct model baseline only achieved 47.4%. The fine-tuning variant should recover stronger depth signal by more closely mimicking our base model pipeline, and feature universality should partially hold with p90_ppl and var_surprisal appearing in the top-5 features even if not consistently top-2.

Now I'm deciding whether to include the cancelled plan_010 in the full experiment writeup since the user asked for all planned experiments, then working through how to structure plan_023 and the theory section together since they're essentially the same experiment. I'm also refining the metric predictions for the 14B model tier, setting the 4-class accuracy estimate around 0.76 with a range of 0.72-0.82, and establishing the corresponding AUC bounds.

For the seed robustness work, I'm noting that GPT-2 XL and Pythia are already done with their deltas measured, while OLMo is still being analyzed but expected to stay under 3pp difference for the best tier. I'm about to write out the full YAML output now, being careful to match the requested format and checking the registry to confirm which seed experiments are still in progress versus completed. Looking at what's already been done through the wild_data experiments, I can see that plan_015's core components—cross-model calibration on C4, FineWeb, and RedPajama—are largely covered across multiple runs with different reference models. What's missing is the systematic aggregation and depth prediction analysis across all three models together, which is what plan_015 specifically calls for.

For the best tier completion, I need to focus on the remaining gaps: running RedPajama with GPT-2 XL and OLMo to match the Pythia baseline, analyzing consistency patterns across all three models, and characterizing how FPR varies systematically across datasets. I should also structure the final output with detailed metric predictions for each planned experiment, making sure each prediction includes the reasoning behind it.

Now I'm organizing the full set of experiments for the best tier—there are several key studies to include: the 14B scale validation, wild-data calibration work, existing detector baselines, bootstrap confidence intervals for the main table, theoretical analysis connecting to model collapse phenomena, and API model experiments with recursive chains. I notice the theoretical analysis and theory section are overlapping, so I should consolidate those rather than duplicate the effort.

For the OLMo seed43 experiment currently marked as analyzing with no metrics yet, I'll hold off on making predictions until the data comes in.

Now I'm laying out the final structure: plan_014 as the most critical running experiment, followed by the planned validations and theoretical work, with plan_010 noted as cancelled. For the best-tier predictions, I need to be precise with the numbers—assuming OLMo stays within a 3 percentage point improvement range and grounding each estimate in what I'm seeing from the 1B results.

Looking at the nucleus performance across models at 1B scale, I'm seeing a range from about 78% to 83%, with GPT-2 XL performing best. At 14B, the key question is how the recursive degradation pattern changes—the larger model will fit its own generated training data more tightly, which could compress the loss gaps between depths and reduce the feature divergence, though the fundamental issue of training on model outputs should still create some performance drop.

For the best tier estimate, I'm settling on around 76% as a reasonable point, with the d1v2 AUC of 0.87 seeming plausible. But I need to reconsider the reference model setup—it's still Pythia-1.4B across all experiments, so the feature extraction quality doesn't change. The real question is whether Qwen2.5-14B's recursive chain produces distinguishable depth levels when measured through those same reference features. Since the 14B model generates higher-quality text at each depth, the d1 output will be closer to human text than what a 1B model produces, which likely compresses the depth-to-depth signal somewhat.

Looking at my estimates for 14B: d0v1 stays very high at 0.985 given the large human-versus-synthetic gap, d1v2 drops slightly to 0.87 due to that compressed signal, d2v3 lands at 0.78, and the 4-class accuracy comes in at 0.76. The p90_ppl feature should still dominate since tail erosion follows the same mechanism, though I might see slightly different feature rankings emerge. For EDD across 6 depths, I'm estimating d3v4 at 0.76, d4v5 at 0.69, giving an EDD of 4.

Now I'm moving on to consider Binoculars combined with Fast-DetectGPT...

Binoculars works by comparing perplexity ratios between two models while Fast-DetectGPT uses conditional probability curvature from perturbations, both producing single scalars. For binary classification between real and synthetic, both should excel above 0.9 AUC, but the core issue is that d1, d2, and d3 all register as "synthetic" to these detectors, causing their scalar scores to overlap significantly. I'll need to calibrate by finding optimal thresholds to map the continuous scores into 4 bins. I'm expecting Binoculars to hit around 0.95-0.98 AUC on the binary d0v1 task, but the ordinal 4-class performance will likely drop to around 32% due to that overlap problem.

Fast-DetectGPT should perform similarly on the binary task at 0.92-0.96 AUC, with 4-class accuracy around 30%. The low 4-class performance makes sense because d0 separates cleanly and gets classified correctly most of the time, while d1, d2, and d3 all get lumped into the same bin. Since d0 comprises about 25% of the data with roughly 90% recall, and d1/d2/d3 each make up about 20% with only 20% recall each, the overall accuracy works out to roughly 37.5% when I account for the distribution.

For the tier predictions, I'm expecting Binoculars around 35% and Fast-DetectGPT at 31%. Looking at the pairwise AUCs, d0 versus d1 should hit around 0.96 and 0.93, while the harder distinctions like d1 versus d2 and d2 versus d3 will be much closer to random at 0.53-0.56.

Now I'm moving on to plan_015, which focuses on calibrating with wild data. The main work left involves running RedPajama and Dolma evaluations across all three reference models.

For the C4 systematic analysis, I'm expecting false positive rates in the best tier to fall between 20-34%, with FineWeb coming in tighter at 17-20%. RedPajama should land around 12-18% based on what I've seen with Pythia, and cross-model consistency should stay within about 8 percentage points. The high-quality editorial datasets like WikiText and OpenWebText should perform much better, staying under 3%.

For the bootstrap confidence intervals, I'm anticipating widths of 2-4 percentage points across all nine cells, averaging around 3pp, with all intervals comfortably above the 25% chance baseline. The ranking of strategies should hold up within these intervals, with temp09 performing at least as well as nucleus, which outperforms topk50.

Plan_023 involves writing and theoretical analysis rather than running experiments.

For the theoretical section, I need to establish a formal bound on expected divergence distance as a function of the contraction rate and epsilon, then validate it against the observed EDD of 4 across all three models. I should also connect tail erosion formally to Shumailov's findings and explain why p90_ppl dominance emerges, plus derive why uniform temperature scaling converges faster to the attractor compared to truncation methods.

For the API model recursive chains, GPT-4o-mini achieves around 68% accuracy on the 4-class task when fine-tuned, which is lower than local 1B models—likely because API fine-tuning doesn't fully override the base distribution and RLHF regularization persists. Without fine-tuning, just using prompting gets me to about 55% accuracy, which is much weaker since each generation step is just following instructions rather than learning the pattern.

The depth signal is present but heavily suppressed. I have enough detail now to write the YAML output. I should check whether the user wants predictions for the OLMo seed43 experiment—looking at the experiment plan, seed experiments aren't listed as separate entries, they're tracked in the registry as supplementary work, so I'll skip those. Though I should mention seed robustness in the narrative guidance since it's a core assumption for the best-tier results.

Looking back at plan_014 more carefully, the prompted generation experiment showed GPT-2 XL dropped from 83.3% down to 69.5% when switching away from BOS tokens, a loss of 13.8 percentage points.

For the 14B scale, I'd expect more modest attenuation than what a mode change produces. The instruct model hit 47.4%, but that's RLHF-tuned, not a base model. The previous 7B QLoRA attempt gave contradictory results due to quantization artifacts, so the clean FP16 14B approach avoids that problem. With nucleus sampling and Pythia reference features, the generated text should appear more human-like to the reference model, which might push p90_ppl slightly higher for d0, making it harder to distinguish from d1. But the recursive collapse still drives features in the same direction, so 76% feels reasonable—slightly below the 78-79% average for 1B nucleus models but solidly within the expected range. Let me reconsider this estimate though.

Qwen2.5-14B is substantially stronger than the 1B models, so d1 text quality will be much higher. The catch is that features are extracted using Pythia-1.4B as the reference model, meaning perplexity and surprisal are computed by running the generated text through Pythia. Since Qwen and Pythia have different training data and tokenizers, the d0 text from Qwen's training distribution will have different statistics when measured through Pythia's lens compared to d1 generated text.

The core question is whether the depth signal persists when using a 14B generative model measured against a 1.4B reference. I think it should, because the mechanism—tail erosion in the text's statistical properties—operates independently of which model generated the text, and Pythia should detect these distributional shifts regardless. For the best tier classification accuracy, I'm settling on 0.76, which sits comfortably in the expected range and reflects that 14B models produce higher-quality text that might compress the signal somewhat.

Now I'm thinking through the experimental outputs—what tables and figures each plan would actually produce. For the 14B scaling experiment, I'd add an accuracy row to the main table and overlay the AUC decay curves to show the effective depth dimension holds across model sizes, plus a feature importance comparison to demonstrate the universality of the signal. The detector comparison plan needs a table showing how Binoculars and Fast-DetectGPT perform on the ordinal task alongside our methods, with a corresponding score distribution plot. The confidence interval update is straightforward, and the theoretical bound work would be visualized as a figure showing the EDD limit.

I'm also checking the OLMo seed experiment status—it's still running with empty metrics, so I won't create a separate prediction for it since it's not listed as its own entry, though I should note it in the narrative guidance. Before finalizing everything in YAML, I need to be careful about precision with the metrics and make sure my rationales are thorough.

The user wants the output in YAML with English field names to match the existing data format, but I'm noticing the rationales should be in Chinese based on their request. I'll keep the technical content and metrics in English while writing the result_rationale sections in Chinese to align with what they're asking for.

Now I'm verifying my metric predictions for plan_014 against the best tier ranges to make sure they're consistent before finalizing the output. b_top2_feature_overlap_with_1b: [2, 2] → I predict 2 (p90_ppl + var_surprisal both in top-3) ✓

For plan_018:
- existing_detector_ordinal_4class_acc: [0.25, 0.4] → Binoculars 0.35, FDGPT 0.31 ✓

For seed robustness:
- seed_robustness_max_delta_pp: [0.6, 3.0] → GPT-2 XL 2.04pp (done), Pythia 0.64pp (done), OLMo expected <3pp ✓

For theory:
- theory_edd_bound_vs_empirical_error: [0, 1] → predict error = 0 (bound exactly matches EDD=4) or error = 1 (bound gives 5, empirical 4)

Now I'm looking at the nucleus sampling metrics across the 1B models to establish a baseline before extrapolating to 14B performance. I'm examining the accuracy and divergence patterns for Pythia, OLMo, and GPT-2 XL, then using those to estimate what I'd expect at the larger scale. lower accuracy due to higher-quality synthetic text
- But potentially higher d0v1 AUC because Qwen-14B d0 (real text) is quite different from the synthetic chain
- Overall: 76% accuracy, d1v2=0.87, d2v3=0.79

For 14B per-class predictions:
- d0 recall: ~0.97 (slightly lower than 1B's ~0.99 because Qwen's real data might have different characteristics from Pythia's perspective)
- d1 recall: ~0.82
- d2 recall: ~0.58
- d3 recall: ~0.72

These are consistent with the 1B pattern where d2 is the hardest class.

For 14B 3-class (d1/d2/d3 only):
- 3-class acc: ~0.71

When I extend to deeper depths with 14B, the d3v4 AUC hits 0.76 which just crosses the threshold, suggesting an EDD of 4, but d4v5 drops to 0.69 and fails. Looking at the fine-tuning losses, Qwen-14B achieves around 2.0 on its own generated d0 text, then 1.3 for d1 and 0.95 for d2, showing the model fits progressively better as the text becomes more synthetic. I'm confirming that ordinal depth represents a genuinely novel capability, with all three core claims fully supported: the 1B to 14B scaling progression with prompted generation and seed stability validates the first claim, the theory-guided Atlas evolves into an empirical map grounded in theoretical principles for the second, and the pipeline achieves an 11.5 percentage point improvement with confirmed convergence mechanisms for the third. The narrative arc flows from identifying the unknown problem through formalization and systematic mapping to theoretical explanation and empirical validation at scale, culminating in a practical two-stage solution positioned for EMNLP's "New Missions" track.

Now I'm laying out the validation experiments, particularly a large-scale test using Qwen2.5-14B in full precision on high-end hardware, running recursive depth chains through LoRA fine-tuning with feature extraction and cross-validated classification to confirm the expected accuracy metrics around 76% for the four-class random forest model and 72% for logistic regression. Looking at the feature importance rankings, the top predictors are perplexity-based metrics like p90_ppl and variance in surprisal, with notable overlap to the 1B model's top features. The finetuning losses show steady improvement across depth levels, while the pairwise AUC scores reveal that distinguishing between adjacent depth classes gets progressively harder as depth increases.

The 14B model's superior capacity produces higher-quality synthetic text at each generation step, making its depth-1 outputs closer to human text than the 1B model's equivalent, which compresses the feature gap and explains the accuracy drop from 80.1% to 76%. But the tail erosion effect from recursive finetuning is independent of model size—the sampling process inherently truncates low-probability events, and p90_ppl is precisely capturing this tail behavior that accumulates across generations.

The p90_ppl metric shows how extreme tokens become progressively rarer at each depth, while var_surprisal tracks the narrowing of the surprisal distribution as the model converges toward lower entropy. These are properties of the text distribution itself, not the architecture, so the feature universality holds across scales. The EDD=4 threshold aligns between models because the 0.75 AUC is reached at the same relative convergence point—the 14B model's slower contraction rate is balanced by the reference model's reduced sensitivity to distributional nuances at that scale, and the d3v4 AUC of 0.76 shows the signal is still present but fading at depth 4.

The d4v5 AUC drops to 0.69 below threshold, fitting the geometric convergence pattern. I'm also documenting the validation tables showing the 14B model's accuracy and AUC metrics alongside the 1B baselines, along with the per-class performance and binary pairwise AUC data used to determine EDD. The figures show the AUC decay curve overlaying the 14B results on the 1B models to demonstrate EDD=4 consistency across scales, and a feature importance comparison between the 14B and reference models.

The 14B results directly support the scale robustness claim—76% accuracy is 31 percentage points above chance, confirming the ordinal depth signal holds at mainstream model scale without quantization artifacts. The feature universality finding is particularly strong: p90_ppl and var_surprisal consistently rank in the top features across four model families and numerous settings. This cross-scale consistency for EDD=4 transforms the Atlas property from a 1B-specific observation into a scale-invariant structural characteristic of recursive generation, with the ~4pp accuracy drop versus 1B averages being expected given the larger model's slower collapse dynamics.

Now I'm setting up the wild-data calibration experiments across C4, FineWeb, RedPajama, and Dolma using trained random forest classifiers to extract features and analyze depth prediction distributions across reference models. Now I'm looking at the false positive rates across different content types—editorial sources like WikiText and OpenWebText show minimal FPR under 3%, while web-crawled data from C4 and FineWeb ranges from 15-34%, which the multi-model analysis confirms isn't just a quirk of one reference model. The ~20% FPR on C4 likely reflects genuine template-heavy and machine-translated content that statistically resembles model output, and the strong cross-model agreement around 88-91% on d0 classifications suggests this pattern is consistent across different models.

The distribution skews heavily toward d1 (shallow model-like text) rather than d2 or d3, which makes sense since most synthetic-looking web content mimics basic model output rather than deeply recursive patterns. RedPajama and Dolma show slightly lower false positive rates than C4 because they incorporate higher-quality sources like Wikipedia and books, and the overall calibration suggests the depth classifier is working as intended—flagging low-quality and template-generated content even if they're not technically model-generated.

Generating markdown table...

The wild-data results show a coherent pattern: high-quality editorial text gets classified as d0, template-driven content clusters at d1, and there's no spurious detection of deeper recursion levels. This supports using depth-graduated curation strategies, and the paper frames it as the classifier meaningfully distinguishing between editorial and template-generated content on uncurated web text, even though we can't definitively label what's truly model-generated in the wild.

Now I'm setting up baseline comparisons with existing detectors like Binoculars and Fast-DetectGPT, converting their continuous scores into ordinal depth predictions through threshold optimization. Looking at the expected performance metrics across the 4-class depth discrimination task. Looking at the performance gaps between our random forest model and the baseline methods—our approach achieves 78.3% accuracy while Binoculars and Fast-DetectGPT show gaps of 43.3% and 47.3% respectively. The core issue is that both baseline methods rely on single scalar scores designed specifically for the human-versus-machine distinction, which works well for that binary boundary but fails to capture the subtle distributional shifts across the synthetic model progression from d1 to d3.

The real problem is that compressing a 19-dimensional feature space into one dimension loses the ordinal structure entirely—Binoculars captures average quality degradation but misses the tail-specific erosion patterns, while Fast-DetectGPT saturates once you move beyond the sharp human-to-synthetic transition. The score distributions for d1, d2, and d3 overlap significantly with Kolmogorov-Smirnov distances around 0.08-0.12 between adjacent depths, making threshold-based classification essentially random for non-d0 classes. The performance difference between Binoculars and Fast-DetectGPT reflects Binoculars' marginal advantage in detecting progressive quality degradation through its dual-model approach.

Both fall dramatically short of our random forest's 78.3% accuracy—a 43-47 percentage point gap that demonstrates ordinal depth estimation is fundamentally different from binary detection and can't be solved by repurposing existing detectors. I'm also noting the relevant tables and figures that show the score distributions and pairwise comparisons across depth levels.

The core insight here is that this gap directly validates our paper's main claim: existing state-of-the-art detectors max out around 31-35% on ordinal tasks, confirming that depth estimation requires the multi-dimensional feature approach we've developed. This also strengthens our position on novelty—the contribution isn't just the random forest classifier itself, but the feature engineering and task formalization that enable discrimination where current tools fail.

Now I need to compute bootstrap confidence intervals for the 3-model comparison table... I'm finishing out the confidence intervals for all nine model-strategy combinations, then verifying that the rankings remain stable within those bounds—both across decoding strategies and between models. The rationale confirms that with this sample size and cross-validation setup, the bootstrap distributions should be well-behaved, with confidence interval widths driven primarily by fold-level variance rather than insufficient data. 20+ pp above chance (25%), so no CI will approach chance level. The strategy ranking (temp09 > nucleus > topk50) is preserved within CIs because the effect size (~5-8pp between strategies) exceeds the CI width (~3pp). Similarly, the model ranking (GPT-2 XL > OLMo ≈ Pythia) is stable because GPT-2 XL consistently leads by 4-7pp. The only potential overlap is between nucleus and temp09 for Pythia (where the gap is smallest), but this is a minor nuance, not a narrative threat.

Bootstrap CIs are essential for establishing that accuracy differences between models and strategies are statistically meaningful rather than artifacts of the train/test split, and they give me the statistical backing to make ranked claims like "GPT-2 XL consistently achieves the highest accuracy."

Now I'm moving into the theoretical analysis section, which will connect the depth signal to model collapse theory by deriving an EDD upper bound from contraction rates and explaining why p90_ppl and var_surprisal dominate through tail erosion mechanisms, then predicting how temperature accelerates these effects. convergence from logit scaling analysis. Produces half-page theory sketch with experimental validation.

The expected results show an EDD upper bound formula based on contraction rate and detection threshold, predicting a bound of 5 against an empirical value of 4. Tail erosion and variance of surprisal both decrease with depth as predicted, and temperature scaling contracts probability mass more gradually than nucleus or top-k sampling. The top-2 features match between theory and empirical ranking—p90 percentile perplexity and variance of surprisal lead both lists.

This aligns with Dohmatob's framework on geometric convergence: the model's contraction rate depends on how well it reproduces its training distribution when operating entirely on synthetic recursive chains. The theoretical bound of 12 assumes perfect classifier efficiency, but the random forest actually operates at around 40% efficiency with 19 features, bringing the practical limit down to about 5 — which aligns well with the observed EDD of 4. The tail erosion mechanism connects to Shumailov's findings on how recursive training erodes low-probability events first: p90_ppl directly measures this tail behavior through the 90th percentile of per-token perplexity, while var_surprisal captures how the distribution narrows as it concentrates, and temperature accelerates this convergence through the log relationship.

Temperature works differently from nucleus or top-k sampling — instead of truncating or removing the tail entirely, it rescales logit differences uniformly, amplifying high-probability tokens and accelerating concentration toward the mode. This explains why temperature at 0.9 produces similar d1 features to nucleus or top-k at d2, which accounts for the trajectory reversal I'm seeing in cross-strategy transfer.

Now I'm looking at the theoretical bounds and empirical validation across models and scales, along with visualizations showing how tail erosion manifests in perplexity trajectories and how the contraction rate model predicts the observed AUC decay. The key insight is that this theory section transforms the work from pure empirical observation into a mechanistic framework — I've got a falsifiable prediction (EDD ≤ 5, validated at 4), a causal explanation linking tail erosion to perplexity degradation, and a mechanistic account for why temperature scaling reverses the dominance trajectory. This grounds the Atlas in theory rather than just pattern-matching.

The bound derivation itself isn't novel in isolation, but applying convergence theory to depth estimation is a fresh contribution appropriate for an empirical paper. The contraction rate estimate around 0.75 can be independently verified from the finetuning loss data, which makes the whole framework self-validating.

I'm also planning to test whether this depth signal transfers to commercial API models through two parallel approaches — fine-tuning GPT-4o-mini on recursive depth chains and running prompted recursive chains without any fine-tuning. Both will extract 19 features and use random forest classification to see if the depth signal holds across different model architectures.

Looking at the expected results, the fine-tuned approach shows stronger performance with 68% accuracy on the 4-class task and clean AUC separation across depth pairs, while the prompted approach drops to 55% accuracy but still captures some signal. The top discriminative features are consistent across both — perplexity metrics and surprisal variance dominate — with decent overlap to what the local models found. The prompted chain approach doesn't actually shift the model's underlying distribution—it's just the same model generating text conditioned on previous outputs, so the depth effect comes from accumulated stylistic drift rather than genuine retraining. This produces weaker results at 55% accuracy, establishing a floor for how much signal exists in the lightest transfer setting, though the key features like perplexity and surprise variance still rank highly since the tail erosion mechanism persists regardless of whether the shift comes from fine-tuning or generation. I'm comparing these results across API fine-tuned, prompted, and local baselines in the supplementary tables and figures. Accuracy comparison across generation modes (local fine-tune / API fine-tune / prompted chain / instruct) showing depth signal gradient. API results provide ecological validity while the fine-tuned chain confirms depth signal persists in commercial models. Even without fine-tuning, prompted generation introduces detectable depth signal—the instruct model hit 47.4% and prompted generation reached 69.5%, showing depth signal is robust across approaches but weakened by RLHF and prompted versus fine-tuned generation. The paper frames this as depth signal being a general property of recursive text generation, with magnitude proportional to distribution shift.

The DCOL component ablation is cancelled because all six attempts failed across different architectures—DeBERTa variants collapsed or hit memory limits while RoBERTa severely overfit. The underlying issue appears structural rather than a tuning problem. I'm working through the calibration mechanics for these detectors—taking their continuous scores and finding optimal thresholds to bin them into four depth classes. My rough calculation suggests around 47% accuracy if Binoculars discriminates well on the easiest class but performs randomly on the harder ones, though that's higher than my initial 35% prediction, so I need to reconsider the assumptions.

The scores probably aren't completely random across d1/d2/d3—there's likely some weak signal where deeper generations score slightly more synthetic—but the distributions overlap so much that even with optimized thresholds, I'd expect d0 to hit around 85% recall while d1/d2/d3 each fall in the 20-30% range, bringing the overall accuracy down closer to my original estimate. Now I'm working through FDGPT's recall estimates across the difficulty tiers, which comes out to around 32%, then recalculating Binoculars with adjusted individual tier contributions to get a more precise total.

I'm settling on 35% for Binoculars and 31% for FDGPT as reasonable estimates within the expected range, then checking whether there were prior attempts at plan_018 in the registry—I see they were killed but the experiment is still scheduled. Before finalizing, I'm also considering whether to include the what_if theory_section separately from plan_023 since they're nearly identical.

I'll consolidate them under plan_023 and note the correspondence. Now I'm reviewing plan_015 more carefully by looking at the completed wild data experiments—I'm seeing calibration runs across different models like Pythia, GPT-2 XL, and OLMo on various datasets with their respective detection rates.

Looking at what's already been done, plan_015 appears largely complete, though it's still marked as planned. The gaps seem to be testing on Dolma, doing systematic cross-model analysis on RedPajama and FineWeb like was done for C4, and putting together a formal write-up with consistent methodology.

Let me reconsider plan_015's actual scope—extracting subsets from those three corpora, using the reference model to pull 19 features, then applying the trained random forest classifiers for depth prediction and distribution analysis to verify the depth signal exists in wild data. Most of that work is already done, so I'll generate predictions for the full experiment based on the existing results: C4 should land around 66-80% d0 depending on methodology choices, FineWeb around 80-83%, and RedPajama around 85%.

Now looking at the cross-model consistency patterns—OLMo shows the highest d0 percentage with the widest decision boundary, GPT-2 XL sits in the middle, and Pythia gives the lowest. I have what I need to write out the final YAML structure now.

For the narrative, I should tie together how these experiments collectively support the best tier claims. I also want to account for the fact that qwen25_14b_scale_002 and qwen25_14b_scale_003 are both running, which suggests the 14B experiment is actively in progress and possibly iterating—but for best tier assumptions, I'm treating it as successful.

The key nuance here is that best tier requires all three claims to hold at full strength simultaneously, so I need to make sure the imagined results reflect that scenario.

Now I'm compiling the confidence intervals from the existing data across all the sampling strategies and models to use for plan_020.

I realize these are cross-validation CIs rather than bootstrap CIs, but the widths should be comparable enough to work with. For the missing cells, I'll estimate based on the patterns I'm seeing in the data.

Let me just write out the YAML with reasonable estimates rather than getting stuck on this. I should also explicitly call out the overlap between the what_if theory section and plan_023 in my notes.

I need to make sure each experiment has a properly formatted result_rationale as the user requested, and I should think through the table and figure requirements more carefully—the Dream spec calls for at least four figures, starting with the AUC decay curve across depth.

Now I'm organizing the figure descriptions to align with those requirements: the AUC decay with EDD threshold, the feature trajectory panel stratified by model, the confusion matrix heatmap, and the atlas feature×depth grid. Time to put together the final YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe66f9b8-ae0a-48a1-ba6a-80df1d299ab5",
  "isSidechain": false,
  "requestId": "req_011CbAKMQzovxe1odaQTEBFV",
  "type": "assistant",
  "uuid": "6e8ecf7c-4411-4f28-867c-93dff00699cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZMFiYFgi9GdeToBFZsyBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 54520,
      "cache_read_input_tokens": 11841,
      "output_tokens": 21135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 54520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21135,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 54520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 54520
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

_source line 9 · 2026-05-18T16:10:53.916Z_

Let我先确认 experiment_plan 中所有 planned/RUNNING 实验的状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e8ecf7c-4411-4f28-867c-93dff00699cc",
  "isSidechain": false,
  "requestId": "req_011CbAKMQzovxe1odaQTEBFV",
  "type": "assistant",
  "uuid": "e5214d29-6552-4a4d-b0a4-eb8db50e2bb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZMFiYFgi9GdeToBFZsyBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 54520,
      "cache_read_input_tokens": 11841,
      "output_tokens": 21135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 54520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21135,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 54520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 54520
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

_source line 10 · 2026-05-18T16:10:54.938Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UhxxjyU9H6B2FzUgbC52ba`</summary>

```json
{
  "pattern": "**/*experiment_plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5214d29-6552-4a4d-b0a4-eb8db50e2bb7",
  "isSidechain": false,
  "requestId": "req_011CbAKMQzovxe1odaQTEBFV",
  "type": "assistant",
  "uuid": "9d278835-c52c-4b02-8223-b5b28e0c6164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZMFiYFgi9GdeToBFZsyBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 54520,
      "cache_read_input_tokens": 11841,
      "output_tokens": 21135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 54520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21135,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 54520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 54520
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

_source line 11 · 2026-05-18T16:10:54.964Z_

<details><summary>↩ Tool result · `toolu_01UhxxjyU9H6B2FzUgbC52ba`</summary>

```text
projects/recursive_gen_depth_est/experiment_plan.lock
projects/recursive_gen_depth_est/logs/workers/worker_experiment_plan_005_cross_model_loo_detailed_20260515T050435.log
projects/recursive_gen_depth_est/logs/workers/worker_experiment_plan_005_cross_model_loo_detailed_20260515T050435_result.json
projects/recursive_gen_depth_est/logs/workers/worker_experiment_plan_007_cross_strategy_loo_zscore_20260515T050637.log
projects/recursive_gen_depth_est/logs/workers/worker_experiment_plan_007_cross_strategy_loo_zscore_20260515T050637_result.json
projects/recursive_gen_depth_est/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d278835-c52c-4b02-8223-b5b28e0c6164",
  "isSidechain": false,
  "promptId": "91d69094-6e31-4251-b8ae-2ccda51109fb",
  "type": "user",
  "uuid": "9efd0737-d486-4cba-a2e8-c2bb72800eb6",
  "toolUseResult": {
    "filenames": [
      "projects/recursive_gen_depth_est/experiment_plan.lock",
      "projects/recursive_gen_depth_est/logs/workers/worker_experiment_plan_005_cross_model_loo_detailed_20260515T050435.log",
      "projects/recursive_gen_depth_est/logs/workers/worker_experiment_plan_005_cross_model_loo_detailed_20260515T050435_result.json",
      "projects/recursive_gen_depth_est/logs/workers/worker_experiment_plan_007_cross_strategy_loo_zscore_20260515T050637.log",
      "projects/recursive_gen_depth_est/logs/workers/worker_experiment_plan_007_cross_strategy_loo_zscore_20260515T050637_result.json",
      "projects/recursive_gen_depth_est/experiment_plan.yaml"
    ],
    "durationMs": 15,
    "numFiles": 6,
    "truncated": false
  },
  "sourceToolAssistantUUID": "9d278835-c52c-4b02-8223-b5b28e0c6164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T16:10:55.567Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014RsXvWnas71h8NBe76je5k`</summary>

```json
{
  "pattern": "**/*registry*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9efd0737-d486-4cba-a2e8-c2bb72800eb6",
  "isSidechain": false,
  "requestId": "req_011CbAKMQzovxe1odaQTEBFV",
  "type": "assistant",
  "uuid": "631beb21-c7ec-4a9f-b42c-76402020581a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZMFiYFgi9GdeToBFZsyBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 54520,
      "cache_read_input_tokens": 11841,
      "output_tokens": 21135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 54520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21135,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 54520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 54520
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

_source line 13 · 2026-05-18T16:10:55.590Z_

<details><summary>↩ Tool result · `toolu_014RsXvWnas71h8NBe76je5k`</summary>

```text
global/logs/workers/registry.lock
projects/distill_kv_rag_cache/registry.lock
projects/distill_kv_rag_cache/registry.yaml
projects/distill_kv_rag_cache/dream_registry.lock
projects/error_type_pref_optim/dream_registry.lock
projects/recursive_gen_depth_est/registry.lock
projects/recursive_gen_depth_est/dream_registry.lock
global/registry.lock
global/registry.yaml
config/venue_registry.yaml
global/logs/registry_audit.jsonl
projects/recursive_gen_depth_est/registry.yaml
projects/recursive_gen_depth_est/dream_registry.yaml.bak
projects/recursive_gen_depth_est/dream_registry.yaml
global/logs/workers/registry.json.bak
global/logs/workers/registry.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "631beb21-c7ec-4a9f-b42c-76402020581a",
  "isSidechain": false,
  "promptId": "91d69094-6e31-4251-b8ae-2ccda51109fb",
  "type": "user",
  "uuid": "c87f58f9-21a6-4aab-9e81-8778d8e05765",
  "toolUseResult": {
    "filenames": [
      "global/logs/workers/registry.lock",
      "projects/distill_kv_rag_cache/registry.lock",
      "projects/distill_kv_rag_cache/registry.yaml",
      "projects/distill_kv_rag_cache/dream_registry.lock",
      "projects/error_type_pref_optim/dream_registry.lock",
      "projects/recursive_gen_depth_est/registry.lock",
      "projects/recursive_gen_depth_est/dream_registry.lock",
      "global/registry.lock",
      "global/registry.yaml",
      "config/venue_registry.yaml",
      "global/logs/registry_audit.jsonl",
      "projects/recursive_gen_depth_est/registry.yaml",
      "projects/recursive_gen_depth_est/dream_registry.yaml.bak",
      "projects/recursive_gen_depth_est/dream_registry.yaml",
      "global/logs/workers/registry.json.bak",
      "global/logs/workers/registry.json"
    ],
    "durationMs": 15,
    "numFiles": 16,
    "truncated": false
  },
  "sourceToolAssistantUUID": "631beb21-c7ec-4a9f-b42c-76402020581a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：14B scale validation succeeds with strong signal, theory section provides testable predictions that match data, existing detectors fail at ordinal task — a…",
  "leafUuid": "c87f58f9-21a6-4aab-9e81-8778d8e05765",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation for recursive synthetic text with model collapse theory",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

### Tool call

_source line 16 · 2026-05-18T16:10:59.218Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XmaPahkHtU2rqBgJ2BvL42`</summary>

```json
{
  "command": "grep -n \"status: planned\\|status: RUNNING\" projects/recursive_gen_depth_est/experiment_plan.yaml",
  "description": "Find all planned/RUNNING experiments in experiment_plan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c87f58f9-21a6-4aab-9e81-8778d8e05765",
  "isSidechain": false,
  "requestId": "req_011CbAKusbrFd6MhBFTwKyhj",
  "type": "assistant",
  "uuid": "216e6947-2037-4153-975a-d7cdf8b9a27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VhLd5Z9ubgAitGNW3BLSn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21560,
      "cache_read_input_tokens": 66361,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 66361,
          "cache_creation_input_tokens": 21560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21560
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

_source line 17 · 2026-05-18T16:10:59.415Z_

<details><summary>↩ Tool result · `toolu_01XmaPahkHtU2rqBgJ2BvL42`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "216e6947-2037-4153-975a-d7cdf8b9a27c",
  "isSidechain": false,
  "promptId": "91d69094-6e31-4251-b8ae-2ccda51109fb",
  "type": "user",
  "uuid": "10cec824-4b0d-4621-a600-fd0f6a263934",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "216e6947-2037-4153-975a-d7cdf8b9a27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T16:11:02.157Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UnqPhZkiDDFsHNUma8T6Su`</summary>

```json
{
  "command": "grep -n \"status: planned\\|status: RUNNING\" projects/recursive_gen_depth_est/experiment_plan.yaml",
  "description": "Find planned/RUNNING experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10cec824-4b0d-4621-a600-fd0f6a263934",
  "isSidechain": false,
  "requestId": "req_011CbAKv9ut1s8gR8XFY4hir",
  "type": "assistant",
  "uuid": "9cef19da-c6c3-43ad-a654-060beee8302f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJ7GfMPrqsvneUjgFpjeo3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 125,
      "cache_read_input_tokens": 87921,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 125,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 87921,
          "cache_creation_input_tokens": 125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 125
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

_source line 19 · 2026-05-18T16:11:02.230Z_

<details><summary>↩ Tool result · `toolu_01UnqPhZkiDDFsHNUma8T6Su`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cef19da-c6c3-43ad-a654-060beee8302f",
  "isSidechain": false,
  "promptId": "91d69094-6e31-4251-b8ae-2ccda51109fb",
  "type": "user",
  "uuid": "c59f5d69-b31a-4c42-9046-c6c1cdbf29d8",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9cef19da-c6c3-43ad-a654-060beee8302f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T16:11:05.207Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V8jQxMEN1WqfoXEzgTj8K8`</summary>

```json
{
  "command": "grep -n \"status:\" projects/recursive_gen_depth_est/experiment_plan.yaml | head -30",
  "description": "Check experiment statuses in experiment_plan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c59f5d69-b31a-4c42-9046-c6c1cdbf29d8",
  "isSidechain": false,
  "requestId": "req_011CbAKvMyugfwkTwdcxSbKe",
  "type": "assistant",
  "uuid": "0ad0f4a2-677f-4093-b20c-b51d2834d8b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162Ns6R9hieCTi5ijTLDmEy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 120,
      "cache_read_input_tokens": 88046,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 88046,
          "cache_creation_input_tokens": 120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 120
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

_source line 21 · 2026-05-18T16:11:05.359Z_

<details><summary>↩ Tool result · `toolu_01V8jQxMEN1WqfoXEzgTj8K8`</summary>

```text
8:  status: done
129:  status: done
174:  status: cancelled
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ad0f4a2-677f-4093-b20c-b51d2834d8b5",
  "isSidechain": false,
  "promptId": "91d69094-6e31-4251-b8ae-2ccda51109fb",
  "type": "user",
  "uuid": "bbe4a00c-8d22-4574-8268-3b549ceb6804",
  "toolUseResult": {
    "stdout": "8:  status: done\n129:  status: done\n174:  status: cancelled",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0ad0f4a2-677f-4093-b20c-b51d2834d8b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T16:11:07.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_015foWXkAokUJniPLpLBmhFg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbe4a00c-8d22-4574-8268-3b549ceb6804",
  "isSidechain": false,
  "requestId": "req_011CbAKvbM5ShKrGZHAK8AKi",
  "type": "assistant",
  "uuid": "9b1c34f5-aa38-4434-a154-e4d48576abe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNrhNPvKdU9uX1sGenCK2F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 132,
      "cache_read_input_tokens": 88166,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 88166,
          "cache_creation_input_tokens": 132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 132
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

_source line 23 · 2026-05-18T16:11:07.887Z_

<details><summary>↩ Tool result · `toolu_015foWXkAokUJniPLpLBmhFg`</summary>

```text
1	experiments:
2	- id: plan_001a
3	  claim: 1
4	  description: Pythia-1.4B recursive chain — nucleus p=0.95 (MVP)
5	  priority: P0
6	  gpu_budget_hours: 2
7	  deps: []
8	  status: done
9	  notes: '4 depths × 1 strategy. 78.2% 4-class acc, d1v2 AUC 0.861. Content-type control:
10	    81.6%.'
11	  registry_id: mvp_pipeline_pythia_002
12	- id: plan_001b
13	  claim: 1
14	  description: Pythia-1.4B — temperature τ=0.9 chain (4 depths)
15	  priority: P0
16	  gpu_budget_hours: 2
17	  deps: []
18	  registry_id: pythia_temp09_001
19	  notes: τ=0.9 temp-only decoding. Data→data/pythia_temp09/. Launched on cuda:0 after
20	    OLMo.
21	- id: plan_001c
22	  claim: 1
23	  description: Pythia-1.4B — top-k k=50 chain (4 depths)
24	  priority: P0
25	  gpu_budget_hours: 2
26	  deps: []
27	  registry_id: pythia_topk50_001
28	  notes: top-k k=50 decoding. Data→data/pythia_topk50/. Queued for cuda:1 after GPT-2
29	    XL.
30	- id: plan_002
31	  claim: 1
32	  description: OLMo-1B recursive chain (4 depths × 3 strategies)
33	  priority: P0
34	  gpu_budget_hours: 8
35	  deps: []
36	  registry_id: cross_model_olmo_002
37	  notes: OLMo-1B on Dolma. q_proj/k_proj/v_proj LoRA. olmo_001 failed (script bug),
38	    olmo_002 重跑。等 cuda:0 释放。
39	- id: plan_003
40	  claim: 1
41	  description: GPT-2 XL 1.5B recursive chain (4 depths × 3 strategies)
42	  priority: P0
43	  gpu_budget_hours: 8
44	  deps: []
45	  registry_id: cross_model_gpt2xl_001
46	  notes: GPT-2 most studied in collapse literature. WebText training data. c_attn/c_proj
47	    LoRA.
48	- id: plan_002b
49	  claim: 1
50	  description: OLMo-1B — temperature τ=0.9 chain (4 depths)
51	  priority: P0
52	  gpu_budget_hours: 2
53	  deps: []
54	  registry_id: olmo_temp09_001
55	  notes: 3×3 matrix cell. OLMo temp09. olmo_temp09_001 正在运行 (PID 205384, cuda:1)。之前被
56	    cron 子进程误报为 failed，已修正。olmo_temp09_002 已取消。
57	- id: plan_002c
58	  claim: 1
59	  description: OLMo-1B — top-k k=50 chain (4 depths)
60	  priority: P0
61	  gpu_budget_hours: 2
62	  deps: []
63	  registry_id: olmo_topk50_001
64	  notes: 3×3 matrix cell. OLMo topk50. 等 cuda:1 释放后提交。
65	- id: plan_003b
66	  claim: 1
67	  description: GPT-2 XL — temperature τ=0.9 chain (4 depths)
68	  priority: P0
69	  gpu_budget_hours: 2
70	  deps: []
71	  registry_id: gpt2xl_temp09_001
72	  notes: 3×3 matrix cell. Running on cuda:1.
73	- id: plan_003c
74	  claim: 1
75	  description: GPT-2 XL — top-k k=50 chain (4 depths)
76	  priority: P0
77	  gpu_budget_hours: 2
78	  deps: []
79	  registry_id: gpt2xl_topk50_001
80	  notes: 3×3 matrix cell. GPT-2 XL topk50.
81	- id: plan_004
82	  claim: 1
83	  description: 'DCOL training: RoBERTa-large with learnable margins contrastive loss
84	    (v6, non-blocking)'
85	  priority: P1
86	  gpu_budget_hours: 8
87	  deps:
88	  - plan_001b
89	  - plan_002
90	  - plan_003
91	  notes: v1-v5 DeBERTa 全部失败 (D011)。v6 换 RoBERTa-large 非阻塞尝试。成功→bonus section，失败→negative
92	    analysis。不阻塞论文进度。
93	  registry_id: dcol_roberta_v6_001
94	- id: plan_005
95	  claim: 1
96	  description: 'Leave-one-model-out generalization (RF): train on 2 families, test
97	    on 3rd'
98	  priority: P0
99	  gpu_budget_hours: 2
100	  deps:
101	  - plan_001b
102	  - plan_002
103	  - plan_003
104	  registry_id: cross_model_loo_v1
105	  notes: '3 rotations with RF classifier. Research-phase gate: cross-model acc ≥ 45%.
106	    Plan A: 不依赖 DCOL。均值 66.4%，gate 通过。'
107	- id: plan_006
108	  claim: 2
109	  description: 'Depth Degradation Atlas: monotonicity scores, EDD, cross-model/strategy
110	    heatmaps'
111	  priority: P0
112	  gpu_budget_hours: 3
113	  deps:
114	  - plan_001b
115	  - plan_002
116	  - plan_003
117	  registry_id: atlas_v1_analysis
118	  notes: 'v1 完成: monotonicity ρ=-0.82~-0.89, EDD=3 (未饱和), cross-model Jaccard=0.667,
119	    rank corr ρ>0.85. 4 JSON in artifacts/atlas/. 待完成: 正式出图(AUC decay/feature trajectory/heatmap/confusion
120	    matrix) + 纳入 3×3 剩余 cells 数据.'
121	- id: plan_006b
122	  claim: 1
123	  description: '3-class experiment (d1/d2/d3 only): isolate pure depth gradient from
124	    real-vs-synthetic signal'
125	  priority: P0
126	  gpu_budget_hours: 0.5
127	  deps:
128	  - plan_001a
129	  status: done
130	  registry_id: mvp_pipeline_pythia_002
131	  notes: Reviewer-requested. 3-class acc=70.8% [0.692,0.725], d1v2 AUC=0.854, d2v3=0.793.
132	    Results in mvp_pipeline_pythia_002 metrics.
133	- id: plan_007
134	  claim: 1
135	  description: 'Leave-one-strategy-out robustness (RF): train on 2 strategies, test
136	    on 3rd'
137	  priority: P0
138	  gpu_budget_hours: 2
139	  deps:
140	  - plan_001b
141	  - plan_002
142	  - plan_003
143	  registry_id: cross_strategy_loo_001
144	  notes: '3 rotations per model with RF. Plan A: 不依赖 DCOL。均值 59.1%，9/9 > chance。temp09
145	    d1v2 反转已解释 (Covariate Shift)。'
146	- id: plan_008
147	  claim: 1
148	  description: 'DeBERTa end-to-end classifier: direct text→depth'
149	  priority: P1
150	  gpu_budget_hours: 10
151	  deps:
152	  - plan_001b
153	  - plan_002
154	  - plan_003
155	  registry_id: n2_deberta_finetune_001
156	- id: plan_009
157	  claim: 1
158	  description: 'Baseline battery: DivEye, perplexity regression, CORAL, CE, zero-shot
159	    LLM'
160	  priority: P1
161	  gpu_budget_hours: 8
162	  registry_id: baseline_battery_001
163	  deps:
164	  - plan_001b
165	  - plan_002
166	  - plan_003
167	- id: plan_010
168	  claim: 1
169	  description: DCOL component ablation
170	  priority: P2
171	  gpu_budget_hours: 8
172	  deps:
173	  - plan_004
174	  status: cancelled
175	  notes: DCOL v6 失败 (D018)，前置条件 plan_004 未满足，取消。
176	- id: plan_011
177	  claim: 2
178	  description: Depth extension to 5 generations + EDD saturation analysis
179	  priority: P0
180	  gpu_budget_hours: 4
181	  deps:
182	  - plan_001a
183	  registry_id: depth_extension_binary_pairwise_002
184	  notes: Pythia-1.4B nucleus EDD=4 (binary d3v4=0.784>0.75, d4v5=0.683<0.75)。6-class
185	    pairwise AUC 因决策边界稀释不可用，必须用 binary pairwise classifier。
186	- id: plan_011b
187	  claim: 2
188	  description: GPT-2 XL depth extension d4/d5 + EDD cross-model verification
189	  priority: P1
190	  gpu_budget_hours: 4
191	  deps:
192	  - plan_003
193	  - plan_011
194	  registry_id: depth_extension_gpt2xl_d4d5_001
195	  notes: GPT-2 XL 是 3×3 矩阵信号最强模型 (85.4%)。验证 EDD 跨模型一致性，直接增强 Claim 2。已 RUNNING on cuda:0。
196	- id: plan_011c
197	  claim: 2
198	  description: OLMo-1B depth extension d4/d5 + EDD cross-model verification
199	  priority: P1
200	  gpu_budget_hours: 4
201	  deps:
202	  - plan_002
203	  - plan_011
204	  notes: 第 3 个模型 EDD 验证。代码已就绪 (run_depth_extension_olmo.sh)，含 binary pairwise eval。Reviewer
205	    PASS。排 granularity ablation 之后上 cuda:1。
206	  registry_id: depth_extension_olmo_d4d5_002
207	- id: plan_012
208	  claim: 1
209	  description: 'Granularity ablation (RF): binary / 3-class / 4-class / 6-class'
210	  registry_id: granularity_ablation_rf_001
211	  priority: P1
212	  gpu_budget_hours: 1
213	  deps:
214	  - plan_001b
215	  - plan_002
216	  - plan_003
217	  notes: 'Plan A: 用 RF 做，不依赖 DCOL。与 plan_011 depth extension 联动（6-class 需要 5+ depths
218	    数据）。'
219	- id: plan_013
220	  claim: 3
221	  description: Downstream curation proof-of-concept
222	  priority: P2
223	  gpu_budget_hours: 15
224	  deps:
225	  - plan_001b
226	  - plan_002
227	  - plan_003
228	  registry_id: downstream_curation_poc_001
229	  notes: 'DONE. RF curation 不优于 unfiltered (negative for original hypothesis)，但显著优于
230	    random (p<0.002 all tiers)。Data efficiency story: 44% data ≈ full PPL。Supplement:
231	    random_soft_control_001 (success, rf_soft vs random_soft p=5.6e-5)。已写入 Discussion
232	    + Appendix。'
233	- id: plan_014
234	  claim: 1
235	  description: 13B clean FP16 scale validation (Qwen2.5-14B, nucleus, d0-d3)
236	  priority: P0
237	  gpu_budget_hours: 18
238	  deps:
239	  - plan_001b
240	  - plan_002
241	  - plan_003
242	  notes: 替代原 7B QLoRA（结果矛盾）。Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。完整
243	    d0-d3 nucleus 递归链 + 19 特征提取 + RF/LR 分类。验证 depth signal 在主流模型规模上是否持续。cuda:0。
244	  registry_id: qwen25_14b_scale_002
245	- id: plan_015
246	  claim: 2
247	  description: 'Wild-data calibration: C4/FineWeb/RedPajama subsets → trained RF depth
248	    classification'
249	  priority: P0
250	  gpu_budget_hours: 6
251	  deps:
252	  - plan_001b
253	  - plan_002
254	  - plan_003
255	  notes: D038 reactivated. 从 C4/FineWeb/RedPajama 抽取子集，用已训练 reference model 提取 19
256	    特征，用 3×3 训练好的 RF 分类器做 depth 预测 + 分布分析。验证 depth signal 在野生数据中是否存在。需要 GPU 跑 reference
257	    model 推理。
258	- id: plan_016
259	  claim: 1
260	  description: Prompted generation ecological validity (GPT-2 XL, topic-seeded d0-d3)
261	  priority: P0
262	  gpu_budget_hours: 6
263	  deps:
264	  - plan_003
265	  notes: 验证 depth signal 是否为 BOS-seeded 无条件生成的 artifact。用 topic prompt 前缀（"The following
266	    article discusses..."等）生成 d0，LoRA fine-tune 后生成 d1-d3，提取 19 特征 + RF 分类。选 GPT-2
267	    XL 因为它信号最强，如果 prompted 模式下信号消失则说明生成方式是关键因素。cuda:1。
268	  registry_id: prompted_gen_gpt2xl_001
269	- id: plan_017
270	  claim: 3
271	  description: Cross-strategy two-stage pipeline (strategy classifier + conditioned
272	    depth)
273	  priority: P0
274	  gpu_budget_hours: 2
275	  deps:
276	  - plan_001b
277	  - plan_002
278	  - plan_003
279	  - plan_007
280	  notes: 两阶段方案解决 59.1% 跨策略准确率问题。(a) 策略识别分类器：19 特征 → 3-class (nucleus/temp/topk)，预计
281	    >90%。(b) 策略条件深度分类器：识别策略后用策略专属 RF 估深度。将论文弱点转化为实际贡献。主要是 CPU 任务，不占 GPU。
282	  registry_id: cross_strategy_pipeline_001
283	- id: plan_018
284	  claim: 1
285	  description: 'Existing detector ordinal baseline: Binoculars + Fast-DetectGPT scores
286	    calibrated for ordinal depth estimation'
287	  priority: P0
288	  gpu_budget_hours: 4
289	  deps:
290	  - plan_001a
291	  - plan_002
292	  - plan_003
293	  notes: 'Dream 三档一致 #1 缺口。将 Binoculars/Fast-DetectGPT 连续分数校准为 ordinal bin，在 3×3 已有数据上评估。即使
294	    negative 也加强论文。需要少量 GPU 跑推理。D036。'
295	- id: plan_019
296	  claim: 1
297	  description: 'MLP on 19 features: neural classifier baseline on same feature set'
298	  priority: P1
299	  gpu_budget_hours: 0.5
300	  deps:
301	  - plan_001a
302	  registry_id: mlp_19feat_001
303	  notes: DONE. MLP delta ≤3pp vs RF，确认特征是瓶颈而非分类器选择。CPU only。
304	- id: plan_020
305	  claim: 1
306	  description: 'Table 1 bootstrap CIs: 5-fold CV bootstrap confidence intervals for
307	    all 9 cells'
308	  priority: P0
309	  gpu_budget_hours: 0
310	  deps:
311	  - plan_001a
312	  - plan_002
313	  - plan_003
314	  notes: Dream 三档均要求。从已有 5-fold CV 结果计算 bootstrap CI。纯 CPU 分析任务。
315	- id: plan_021
316	  claim: 1
317	  description: 'Instruction-tuned model validation: Qwen2.5-1.5B-Instruct recursive
318	    chain (nucleus, d0-d3) to test depth signal on instruct models'
319	  priority: P0
320	  gpu_budget_hours: 4
321	  deps:
322	  - plan_001a
323	  notes: D037 Manager 自查发现最大缺口。2024-2025 检测论文标配 instruct model。Qwen2.5-1.5B-Instruct
324	    nucleus d0-d3，19 特征提取 + RF/LR 分类。结果进 Appendix。cuda:1 在 plan_016 完成后跑。
325	  registry_id: qwen25-1p5b-instruct-001
326	- id: plan_022
327	  claim: 1
328	  description: 'Text length sensitivity analysis: evaluate depth estimation accuracy
329	    at 50/100/200/500 token truncation lengths'
330	  priority: P0
331	  gpu_budget_hours: 0
332	  deps:
333	  - plan_001a
334	  - plan_002
335	  - plan_003
336	  registry_id: text_length_sensitivity_001
337	  notes: DONE. 准确率随截断长度优雅降级，关键特征(surprisal moments, entropy)在100-200 tokens内收敛，方法对短文本实用。
338	- id: plan_023
339	  claim: 2
340	  description: 'Theoretical analysis: connect depth signal to model collapse theory,
341	    derive EDD upper bound'
342	  priority: P0
343	  gpu_budget_hours: 0
344	  deps:
345	  - plan_001a
346	  - plan_006
347	  notes: 'D038. CPU/写作任务。(1) 为什么 p90_ppl 和 var_surprisal 能区分 depth: 连接到 Shumailov
348	    et al. 2024 model collapse 中 tail distribution 消失现象。(2) EDD 上界推导: 基于递归生成的 fixed-point
349	    attractor 理论。(3) 与实验 EDD=4 结果对照验证。产出: paper Theory section 草稿。'
350	- id: plan_024
351	  claim: 3
352	  description: 'Downstream benchmark impact: depth-filtered training data → HellaSwag/ARC
353	    evaluation'
354	  priority: P0
355	  gpu_budget_hours: 12
356	  deps:
357	  - plan_001a
358	  - plan_013
359	  notes: D038. 扩展 plan_013 data efficiency story。用 depth estimator 过滤训练数据(移除 high-depth
360	    text)，在 HellaSwag/ARC/PIQA 上评估下游 LM 质量。3 个过滤阈值 × 3 个 benchmark。需要 GPU 做 LM training
361	    + eval。
362	  registry_id: downstream_benchmark_001
363	- id: plan_025
364	  claim: 1
365	  description: 'Learned depth estimator: metric learning on 19-feature space for zero-shot
366	    cross-model generalization'
367	  priority: P1
368	  gpu_budget_hours: 8
369	  deps:
370	  - plan_001b
371	  - plan_002
372	  - plan_003
373	  - plan_005
374	  notes: 'D038. 从 RF 特征重要性出发，训练 lightweight MLP/prototypical network 做 ordinal depth
375	    estimation，目标: 在 leave-one-model-out 上超过 RF baseline (66.4%)。如果成功→方法贡献升级；失败→作为
376	    negative analysis 支持"特征是瓶颈"结论。'
377	  registry_id: learned_estimator_001
378	- id: plan_026
379	  claim: 1
380	  description: 'API model recursive chains: GPT-4o-mini fine-tuning API + prompted
381	    chain for d0-d3 depth estimation'
382	  priority: P1
383	  gpu_budget_hours: 0
384	  deps:
385	  - plan_001a
386	  notes: 'D038. 两种方式验证 API 模型: (a) GPT-4o-mini fine-tuning API 递归链 (需 OpenAI key)。(b)
387	    Prompted recursive chain (rewrite/continue, 无需 fine-tune, 可用任意 API)。验证 depth signal
388	    在商用模型中是否存在。'
389	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b1c34f5-aa38-4434-a154-e4d48576abe7",
  "isSidechain": false,
  "promptId": "91d69094-6e31-4251-b8ae-2ccda51109fb",
  "type": "user",
  "uuid": "c04d6907-3336-47c3-b82d-80c02246a150",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001a\n  claim: 1\n  description: Pythia-1.4B recursive chain — nucleus p=0.95 (MVP)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  status: done\n  notes: '4 depths × 1 strategy. 78.2% 4-class acc, d1v2 AUC 0.861. Content-type control:\n    81.6%.'\n  registry_id: mvp_pipeline_pythia_002\n- id: plan_001b\n  claim: 1\n  description: Pythia-1.4B — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: pythia_temp09_001\n  notes: τ=0.9 temp-only decoding. Data→data/pythia_temp09/. Launched on cuda:0 after\n    OLMo.\n- id: plan_001c\n  claim: 1\n  description: Pythia-1.4B — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: pythia_topk50_001\n  notes: top-k k=50 decoding. Data→data/pythia_topk50/. Queued for cuda:1 after GPT-2\n    XL.\n- id: plan_002\n  claim: 1\n  description: OLMo-1B recursive chain (4 depths × 3 strategies)\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: cross_model_olmo_002\n  notes: OLMo-1B on Dolma. q_proj/k_proj/v_proj LoRA. olmo_001 failed (script bug),\n    olmo_002 重跑。等 cuda:0 释放。\n- id: plan_003\n  claim: 1\n  description: GPT-2 XL 1.5B recursive chain (4 depths × 3 strategies)\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: cross_model_gpt2xl_001\n  notes: GPT-2 most studied in collapse literature. WebText training data. c_attn/c_proj\n    LoRA.\n- id: plan_002b\n  claim: 1\n  description: OLMo-1B — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: olmo_temp09_001\n  notes: 3×3 matrix cell. OLMo temp09. olmo_temp09_001 正在运行 (PID 205384, cuda:1)。之前被\n    cron 子进程误报为 failed，已修正。olmo_temp09_002 已取消。\n- id: plan_002c\n  claim: 1\n  description: OLMo-1B — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: olmo_topk50_001\n  notes: 3×3 matrix cell. OLMo topk50. 等 cuda:1 释放后提交。\n- id: plan_003b\n  claim: 1\n  description: GPT-2 XL — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: gpt2xl_temp09_001\n  notes: 3×3 matrix cell. Running on cuda:1.\n- id: plan_003c\n  claim: 1\n  description: GPT-2 XL — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: gpt2xl_topk50_001\n  notes: 3×3 matrix cell. GPT-2 XL topk50.\n- id: plan_004\n  claim: 1\n  description: 'DCOL training: RoBERTa-large with learnable margins contrastive loss\n    (v6, non-blocking)'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: v1-v5 DeBERTa 全部失败 (D011)。v6 换 RoBERTa-large 非阻塞尝试。成功→bonus section，失败→negative\n    analysis。不阻塞论文进度。\n  registry_id: dcol_roberta_v6_001\n- id: plan_005\n  claim: 1\n  description: 'Leave-one-model-out generalization (RF): train on 2 families, test\n    on 3rd'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: cross_model_loo_v1\n  notes: '3 rotations with RF classifier. Research-phase gate: cross-model acc ≥ 45%.\n    Plan A: 不依赖 DCOL。均值 66.4%，gate 通过。'\n- id: plan_006\n  claim: 2\n  description: 'Depth Degradation Atlas: monotonicity scores, EDD, cross-model/strategy\n    heatmaps'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: atlas_v1_analysis\n  notes: 'v1 完成: monotonicity ρ=-0.82~-0.89, EDD=3 (未饱和), cross-model Jaccard=0.667,\n    rank corr ρ>0.85. 4 JSON in artifacts/atlas/. 待完成: 正式出图(AUC decay/feature trajectory/heatmap/confusion\n    matrix) + 纳入 3×3 剩余 cells 数据.'\n- id: plan_006b\n  claim: 1\n  description: '3-class experiment (d1/d2/d3 only): isolate pure depth gradient from\n    real-vs-synthetic signal'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_001a\n  status: done\n  registry_id: mvp_pipeline_pythia_002\n  notes: Reviewer-requested. 3-class acc=70.8% [0.692,0.725], d1v2 AUC=0.854, d2v3=0.793.\n    Results in mvp_pipeline_pythia_002 metrics.\n- id: plan_007\n  claim: 1\n  description: 'Leave-one-strategy-out robustness (RF): train on 2 strategies, test\n    on 3rd'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: cross_strategy_loo_001\n  notes: '3 rotations per model with RF. Plan A: 不依赖 DCOL。均值 59.1%，9/9 > chance。temp09\n    d1v2 反转已解释 (Covariate Shift)。'\n- id: plan_008\n  claim: 1\n  description: 'DeBERTa end-to-end classifier: direct text→depth'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: n2_deberta_finetune_001\n- id: plan_009\n  claim: 1\n  description: 'Baseline battery: DivEye, perplexity regression, CORAL, CE, zero-shot\n    LLM'\n  priority: P1\n  gpu_budget_hours: 8\n  registry_id: baseline_battery_001\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n- id: plan_010\n  claim: 1\n  description: DCOL component ablation\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_004\n  status: cancelled\n  notes: DCOL v6 失败 (D018)，前置条件 plan_004 未满足，取消。\n- id: plan_011\n  claim: 2\n  description: Depth extension to 5 generations + EDD saturation analysis\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  registry_id: depth_extension_binary_pairwise_002\n  notes: Pythia-1.4B nucleus EDD=4 (binary d3v4=0.784>0.75, d4v5=0.683<0.75)。6-class\n    pairwise AUC 因决策边界稀释不可用，必须用 binary pairwise classifier。\n- id: plan_011b\n  claim: 2\n  description: GPT-2 XL depth extension d4/d5 + EDD cross-model verification\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - plan_003\n  - plan_011\n  registry_id: depth_extension_gpt2xl_d4d5_001\n  notes: GPT-2 XL 是 3×3 矩阵信号最强模型 (85.4%)。验证 EDD 跨模型一致性，直接增强 Claim 2。已 RUNNING on cuda:0。\n- id: plan_011c\n  claim: 2\n  description: OLMo-1B depth extension d4/d5 + EDD cross-model verification\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - plan_002\n  - plan_011\n  notes: 第 3 个模型 EDD 验证。代码已就绪 (run_depth_extension_olmo.sh)，含 binary pairwise eval。Reviewer\n    PASS。排 granularity ablation 之后上 cuda:1。\n  registry_id: depth_extension_olmo_d4d5_002\n- id: plan_012\n  claim: 1\n  description: 'Granularity ablation (RF): binary / 3-class / 4-class / 6-class'\n  registry_id: granularity_ablation_rf_001\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: 'Plan A: 用 RF 做，不依赖 DCOL。与 plan_011 depth extension 联动（6-class 需要 5+ depths\n    数据）。'\n- id: plan_013\n  claim: 3\n  description: Downstream curation proof-of-concept\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: downstream_curation_poc_001\n  notes: 'DONE. RF curation 不优于 unfiltered (negative for original hypothesis)，但显著优于\n    random (p<0.002 all tiers)。Data efficiency story: 44% data ≈ full PPL。Supplement:\n    random_soft_control_001 (success, rf_soft vs random_soft p=5.6e-5)。已写入 Discussion\n    + Appendix。'\n- id: plan_014\n  claim: 1\n  description: 13B clean FP16 scale validation (Qwen2.5-14B, nucleus, d0-d3)\n  priority: P0\n  gpu_budget_hours: 18\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: 替代原 7B QLoRA（结果矛盾）。Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。完整\n    d0-d3 nucleus 递归链 + 19 特征提取 + RF/LR 分类。验证 depth signal 在主流模型规模上是否持续。cuda:0。\n  registry_id: qwen25_14b_scale_002\n- id: plan_015\n  claim: 2\n  description: 'Wild-data calibration: C4/FineWeb/RedPajama subsets → trained RF depth\n    classification'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: D038 reactivated. 从 C4/FineWeb/RedPajama 抽取子集，用已训练 reference model 提取 19\n    特征，用 3×3 训练好的 RF 分类器做 depth 预测 + 分布分析。验证 depth signal 在野生数据中是否存在。需要 GPU 跑 reference\n    model 推理。\n- id: plan_016\n  claim: 1\n  description: Prompted generation ecological validity (GPT-2 XL, topic-seeded d0-d3)\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_003\n  notes: 验证 depth signal 是否为 BOS-seeded 无条件生成的 artifact。用 topic prompt 前缀（\"The following\n    article discusses...\"等）生成 d0，LoRA fine-tune 后生成 d1-d3，提取 19 特征 + RF 分类。选 GPT-2\n    XL 因为它信号最强，如果 prompted 模式下信号消失则说明生成方式是关键因素。cuda:1。\n  registry_id: prompted_gen_gpt2xl_001\n- id: plan_017\n  claim: 3\n  description: Cross-strategy two-stage pipeline (strategy classifier + conditioned\n    depth)\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  - plan_007\n  notes: 两阶段方案解决 59.1% 跨策略准确率问题。(a) 策略识别分类器：19 特征 → 3-class (nucleus/temp/topk)，预计\n    >90%。(b) 策略条件深度分类器：识别策略后用策略专属 RF 估深度。将论文弱点转化为实际贡献。主要是 CPU 任务，不占 GPU。\n  registry_id: cross_strategy_pipeline_001\n- id: plan_018\n  claim: 1\n  description: 'Existing detector ordinal baseline: Binoculars + Fast-DetectGPT scores\n    calibrated for ordinal depth estimation'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  - plan_002\n  - plan_003\n  notes: 'Dream 三档一致 #1 缺口。将 Binoculars/Fast-DetectGPT 连续分数校准为 ordinal bin，在 3×3 已有数据上评估。即使\n    negative 也加强论文。需要少量 GPU 跑推理。D036。'\n- id: plan_019\n  claim: 1\n  description: 'MLP on 19 features: neural classifier baseline on same feature set'\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_001a\n  registry_id: mlp_19feat_001\n  notes: DONE. MLP delta ≤3pp vs RF，确认特征是瓶颈而非分类器选择。CPU only。\n- id: plan_020\n  claim: 1\n  description: 'Table 1 bootstrap CIs: 5-fold CV bootstrap confidence intervals for\n    all 9 cells'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  - plan_002\n  - plan_003\n  notes: Dream 三档均要求。从已有 5-fold CV 结果计算 bootstrap CI。纯 CPU 分析任务。\n- id: plan_021\n  claim: 1\n  description: 'Instruction-tuned model validation: Qwen2.5-1.5B-Instruct recursive\n    chain (nucleus, d0-d3) to test depth signal on instruct models'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  notes: D037 Manager 自查发现最大缺口。2024-2025 检测论文标配 instruct model。Qwen2.5-1.5B-Instruct\n    nucleus d0-d3，19 特征提取 + RF/LR 分类。结果进 Appendix。cuda:1 在 plan_016 完成后跑。\n  registry_id: qwen25-1p5b-instruct-001\n- id: plan_022\n  claim: 1\n  description: 'Text length sensitivity analysis: evaluate depth estimation accuracy\n    at 50/100/200/500 token truncation lengths'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  - plan_002\n  - plan_003\n  registry_id: text_length_sensitivity_001\n  notes: DONE. 准确率随截断长度优雅降级，关键特征(surprisal moments, entropy)在100-200 tokens内收敛，方法对短文本实用。\n- id: plan_023\n  claim: 2\n  description: 'Theoretical analysis: connect depth signal to model collapse theory,\n    derive EDD upper bound'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  - plan_006\n  notes: 'D038. CPU/写作任务。(1) 为什么 p90_ppl 和 var_surprisal 能区分 depth: 连接到 Shumailov\n    et al. 2024 model collapse 中 tail distribution 消失现象。(2) EDD 上界推导: 基于递归生成的 fixed-point\n    attractor 理论。(3) 与实验 EDD=4 结果对照验证。产出: paper Theory section 草稿。'\n- id: plan_024\n  claim: 3\n  description: 'Downstream benchmark impact: depth-filtered training data → HellaSwag/ARC\n    evaluation'\n  priority: P0\n  gpu_budget_hours: 12\n  deps:\n  - plan_001a\n  - plan_013\n  notes: D038. 扩展 plan_013 data efficiency story。用 depth estimator 过滤训练数据(移除 high-depth\n    text)，在 HellaSwag/ARC/PIQA 上评估下游 LM 质量。3 个过滤阈值 × 3 个 benchmark。需要 GPU 做 LM training\n    + eval。\n  registry_id: downstream_benchmark_001\n- id: plan_025\n  claim: 1\n  description: 'Learned depth estimator: metric learning on 19-feature space for zero-shot\n    cross-model generalization'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  - plan_005\n  notes: 'D038. 从 RF 特征重要性出发，训练 lightweight MLP/prototypical network 做 ordinal depth\n    estimation，目标: 在 leave-one-model-out 上超过 RF baseline (66.4%)。如果成功→方法贡献升级；失败→作为\n    negative analysis 支持\"特征是瓶颈\"结论。'\n  registry_id: learned_estimator_001\n- id: plan_026\n  claim: 1\n  description: 'API model recursive chains: GPT-4o-mini fine-tuning API + prompted\n    chain for d0-d3 depth estimation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  notes: 'D038. 两种方式验证 API 模型: (a) GPT-4o-mini fine-tuning API 递归链 (需 OpenAI key)。(b)\n    Prompted recursive chain (rewrite/continue, 无需 fine-tune, 可用任意 API)。验证 depth signal\n    在商用模型中是否存在。'\n",
      "numLines": 389,
      "startLine": 1,
      "totalLines": 389
    }
  },
  "sourceToolAssistantUUID": "9b1c34f5-aa38-4434-a154-e4d48576abe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24 · 2026-05-18T16:11:07.960Z_

````json
{
  "parentUuid": "c04d6907-3336-47c3-b82d-80c02246a150",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**recursive_gen_depth_est**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"recursive_gen_depth_est\")` 或 `load_project_config(\"recursive_gen_depth_est\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### paper-writing-norms\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/recursive_gen_depth_est/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "2f289a58-c3c0-48d2-af5f-b8f4b518a8be",
  "timestamp": "2026-05-18T16:11:07.960Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：14B scale validation succeeds with strong signal, theory section provides testable predictions that match data, existing detectors fail at ordinal task — a…",
  "leafUuid": "2f289a58-c3c0-48d2-af5f-b8f4b518a8be",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation for recursive synthetic text with model collapse theory",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

### Assistant

_source line 27 · 2026-05-18T16:11:16.339Z_

<details><summary>Logged reasoning block</summary>

```text
OK so looking at the actual experiment_plan.yaml file, the status field is only explicitly set for plan_001a (done), plan_006b (done), and plan_010 (cancelled). The rest don't have explicit status fields in the YAML file, meaning they inherit from the context provided in the user's message.

Based on the user's message context:
- plan_014: RUNNING
- plan_015: planned
- plan_018: planned
- plan_020: planned
- plan_023: planned
- plan_026: planned

Plus plan_010 (cancelled) and the what_if theory_section.


Now I'm ready to generate the comprehensive YAML output with all the experiment plans and their statuses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f289a58-c3c0-48d2-af5f-b8f4b518a8be",
  "isSidechain": false,
  "requestId": "req_011CbAKvnTKQF2CQBzjNAjZF",
  "type": "assistant",
  "uuid": "a5816f7d-f375-4413-8719-c96ff04fde5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5GhLqR4aaoXwSjJoUXKfw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12861,
      "cache_read_input_tokens": 88298,
      "output_tokens": 11301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11301,
          "cache_read_input_tokens": 88298,
          "cache_creation_input_tokens": 12861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12861
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

_source line 28 · 2026-05-18T16:15:25.765Z_

Based on the experiment plan and best tier definition, here are detailed predictions for all planned/RUNNING experiments.

```yaml
tier: best
narrative_guidance: >
  Best 档叙事弧完整闭合。14B clean FP16 (plan_014) 消除 "small model only" 降级风险，
  理论节 (plan_023) 从 Dohmatob contraction rates 推导 EDD 上界、Shumailov tail erosion 
  解释 p90_ppl/var_surprisal 主导地位——填补 Dream 3.0 "no algorithmic contribution" 空缺。
  Binoculars/Fast-DetectGPT ordinal ≤35% (plan_018) 确认 ordinal depth 是全新能力，
  与 RF 78.3% 形成 43+pp 对比。三条 Claims 全部满强度：
  Claim 1 — 1B→14B scale + prompted gen + 3/3 seed stability (Δ<3pp) 完整支撑 "feasible, accurate, robust";
  Claim 2 — theory-guided Atlas 从纯经验升级为 "empirical map + theoretical grounding"，EDD=4 跨尺度一致;
  Claim 3 — +11.5pp two-stage pipeline + temperature convergence 机制完整。
  Paper type: task formalization + theory-grounded Atlas + practical framework → EMNLP "New Missions" track。
  Simulated reviewer meta-score 3.5-4.0，accept probability 55-75%。

imagined_experiments:

  - name: "14B Clean FP16 Scale Validation"
    plan_id: "plan_014"
    description: >
      Qwen2.5-14B FP16 (无量化) on 96GB RTX PRO 6000。Nucleus p=0.95，d0-d3 递归 LoRA 
      fine-tuning 链。Pythia-1.4B reference model 提取 19 维统计特征。RF/LR 5-fold CV。
      Binary pairwise d0-d5 确定 EDD。验证 depth signal 在 14B 规模是否持续。
    expected_results:
      rf_4class_acc: 0.76
      rf_4class_ci: [0.745, 0.775]
      lr_4class_acc: 0.72
      lr_4class_ci: [0.705, 0.735]
      rf_3class_acc: 0.71
      rf_3class_ci: [0.692, 0.728]
      pairwise_auc_rf:
        d0v1: 0.988
        d0v2: 0.997
        d0v3: 0.999
        d1v2: 0.87
        d1v3: 0.975
        d2v3: 0.79
      per_class_recall:
        d0: 0.97
        d1: 0.82
        d2: 0.58
        d3: 0.72
      per_class_f1:
        d0: 0.96
        d1: 0.81
        d2: 0.60
        d3: 0.70
      top_features:
        - "p90_ppl (0.19)"
        - "var_surprisal (0.16)"
        - "p75_ppl (0.11)"
        - "mean_surprisal (0.09)"
        - "mean_ppl (0.07)"
      feature_overlap_with_1b_top2: 2
      finetune_losses:
        depth_0: 1.95
        depth_1: 1.25
        depth_2: 0.92
      binary_pairwise_auc:
        d1v2: 0.93
        d2v3: 0.86
        d3v4: 0.76
        d4v5: 0.69
      edd_at_075: 4
      code_contamination_narrow_max: 0.02
    result_rationale: >
      14B 模型容量 ~10x 于 1B，每步递归 fine-tuning 产生的分布偏移更小（更强的模型更接近地复制训练数据），
      导致 per-step 特征差异压缩。这解释了 ~4pp 的准确率下降（76% vs 1B nucleus 均值 80.1%）。
      
      但 tail erosion 机制 (Shumailov 2024) 是 scale-invariant 的：递归训练在有限样本上系统性地
      under-represent 低概率事件，与模型大小无关。因为采样过程本身截断了真实分布的尾部——无论模型多大，
      从有限样本 fine-tune 都会丢失 tail events。p90_ppl 直接度量这种 tail contraction（每步递归
      第 90 百分位 per-token perplexity 下降），var_surprisal 捕获 surprisal 分布随分布集中向 mode 
      的收窄。两者在 14B 仍然 top-2/3 是因为度量的是文本分布属性而非模型架构属性。
      
      EDD=4 匹配 1B 是因为：更大模型的更慢收缩率被 reference model (Pythia-1.4B) 对更精细分布差异的
      同样降低的敏感度所抵消——14B d3 和 d4 的差异更微妙，但 Pythia 对 14B 生成文本的基线敏感度也更低
      （domain shift），两个效应大致相消，使得 AUC=0.75 阈值在同一相对位置（depth 4）被达到。
      
      d3v4 AUC 0.76（刚过阈值）反映 depth 4 的信号仍可检测但微弱；d4v5 0.69 跌破阈值，符合几何收敛
      到 attractor 的预期。d2 recall 最低 (0.58) 与 1B 模式一致——d2 被夹在 d1 和 d3 之间，
      是最难区分的 depth class。
    tables:
      - "Table 2: Scale validation — Qwen2.5-14B row alongside 3×1B models (4-class acc, d1v2 AUC, EDD)"
      - "Table S2: 14B per-class precision/recall/F1 + binary pairwise AUC for EDD determination"
    figures_description:
      - >
        Figure 5 (AUC decay overlay): X-axis depth pairs (d1v2...d4v5), Y-axis binary AUC。
        14B 曲线 (实线, 红色) 叠加在 3 条 1B 曲线 (虚线) 上。水平线 T=0.75。
        四条曲线都在 d3v4 穿越阈值、d4v5 跌破——视觉上一致的 EDD=4。
        14B 曲线略低于 GPT-2 XL 但在 Pythia/OLMo 范围内。
      - >
        Figure 6 (Feature importance comparison): Grouped bar chart, 4 models × top-5 features。
        p90_ppl 和 var_surprisal 在所有 4 个模型中标注为 top-3——视觉确认 scale-invariant 
        feature universality。
    analysis: >
      14B 结果直接启用 Claim 1 中 "1B-14B scale robustness" 子句。76% 是 chance (25%) 的 3 倍，
      确认 ordinal depth signal 在主流模型规模持续存在且无需量化（消除 7B QLoRA 矛盾结果的干扰）。
      Feature universality 现在覆盖 4 个模型家族、10+ settings——论文最强实证发现。
      EDD=4 跨尺度一致性将 Atlas 从 "1B-only observation" 升级为 "scale-invariant structural 
      property of recursive generation"。~4pp 下降是预期中的且可解释（larger model, slower collapse），
      不是弱点而是支撑 tail erosion 理论的额外证据。

  - name: "Wild-data Calibration (C4/FineWeb/RedPajama)"
    plan_id: "plan_015"
    description: >
      系统化 wild-data 评估。用 Pythia/OLMo/GPT-2 XL 三个 reference model 分别提取 19 特征，
      在 C4、FineWeb、RedPajama 各 10K passages 上用 3×3 训练好的 RF 分类器做 depth 预测。
      分析 depth 分布、FPR 模式、跨 reference model 一致性。
    expected_results:
      c4:
        n_passages: 10000
        d0_pct_mean: 72.0
        d0_pct_range_across_ref: [66.0, 95.3]
        d1_pct_mean: 22.0
        d2_pct_mean: 3.5
        d3_pct_mean: 2.5
        fpr_mean: 28.0
        fpr_range_across_ref: [4.7, 34.0]
        cross_model_d0_agreement_pct: 88
      fineweb:
        n_passages: 10000
        d0_pct_mean: 82.0
        d0_pct_range_across_ref: [78.0, 88.0]
        d1_pct_mean: 15.5
        d2_pct_mean: 1.5
        d3_pct_mean: 1.0
        fpr_mean: 18.0
        fpr_range_across_ref: [12.0, 22.0]
        cross_model_d0_agreement_pct: 91
      redpajama:
        n_passages: 10000
        d0_pct_mean: 81.0
        d0_pct_range_across_ref: [76.0, 90.0]
        d1_pct_mean: 15.0
        d2_pct_mean: 2.5
        d3_pct_mean: 1.5
        fpr_mean: 19.0
        fpr_range_across_ref: [10.0, 24.0]
        cross_model_d0_agreement_pct: 89
      editorial_text_fpr: "<3%"
      template_content_fpr: "35-50%"
      cross_model_rank_corr_d0_pct: 0.82
      olmo_systematic_lowest_fpr: true
    result_rationale: >
      已有 wild-data 实验已建立核心模式：编辑质量高的文本 (WikiText, OpenWebText) FPR <3%，
      web-crawl (C4, FineWeb) FPR 15-34%。三模型系统化分析确认这不是单一 reference model 的 artifact。
      
      FPR 差异的根因已确认：web-crawl 语料中 15-30% 是 template/SEO/机器翻译内容，这些文本与
      模型生成文本共享统计指纹（高重复率、压缩的 perplexity tail、低词汇多样性）。这不是真正的 
      false positive——分类器正确识别了具有 "shallow synthetic" 特征的文本。
      
      OLMo 系统性 FPR 最低（已确认：C4 4.72% vs Pythia 20.2%/GPT-2 XL 22.4%），因为 OLMo 
      d1-d3 特征与 d0 的差异更大，产生更宽的 d0 决策边界。GPT-2 XL FPR 最高因为信号最强——
      d0 和 d1 的 feature gap 更小，导致 template 内容更容易落入 d1 范围。
      
      Cross-model d0 agreement ~88-91% 意味着三个 reference model 对同一段 passage 的 d0/non-d0
      判断高度一致，确认信号在文本本身而非 reference model 的偏差。d1-heavy 分布（vs d2/d3 近零）
      符合预期：大多数 "synthetic-looking" web 文本类似浅层模型输出，不是深度递归文本。
      
      FineWeb 和 RedPajama 的 FPR 低于 C4 反映了各自的质量过滤：FineWeb 有激进的去重和质量过滤，
      RedPajama 混合了 Wikipedia/books/ArXiv 等高质量源。
    tables:
      - "Table 5: Wild-data depth distributions — corpus × reference model (3×3 grid)"
      - "Table S5: FPR breakdown by content type (editorial vs template vs SEO), with examples"
    figures_description:
      - >
        Figure 8: Cross-corpus FPR bar chart, grouped by reference model (3 bars per corpus)。
        Editorial baselines (WikiText, OpenWebText) 作为 near-zero 参考线。
        Annotation: "FPR correlates with editorial quality, not dataset size"
    analysis: >
      Wild-data calibration 弥合 controlled→ecological validity 的最后一步。分类器在真实语料上
      行为连贯：高质量文本→d0，template 内容→d1，无虚假 d2/d3。支撑 Discussion 中 
      "depth-graduated curation" 论点。论文表述："our classifier exhibits meaningful behavior on 
      uncurated web text, correctly separating editorial from template-generated content, though 
      definitive depth labels are unavailable for wild data."

  - name: "Existing Detector Ordinal Baseline (Binoculars + Fast-DetectGPT)"
    plan_id: "plan_018"
    description: >
      将 Binoculars (Hans et al., ICML 2024) 和 Fast-DetectGPT (Bao et al., 2024) 的
      连续分数校准为 ordinal depth bins。在 3×3 benchmark 数据上跑推理，optimal threshold 
      search 做 4-class assignment。评估 d0/d1/d2/d3 区分能力。
    expected_results:
      binoculars:
        ordinal_4class_acc: 0.35
        ordinal_4class_ci: [0.32, 0.38]
        binary_d0v1_auc: 0.96
        ordinal_d1v2_auc: 0.56
        ordinal_d2v3_auc: 0.53
        per_class_recall:
          d0: 0.85
          d1: 0.25
          d2: 0.15
          d3: 0.18
        per_class_f1:
          d0: 0.62
          d1: 0.22
          d2: 0.14
          d3: 0.17
        confusion_pattern: "d1/d2/d3 heavily confused; most non-d0 samples assigned to d1 or d3 bins"
      fast_detectgpt:
        ordinal_4class_acc: 0.31
        ordinal_4class_ci: [0.28, 0.34]
        binary_d0v1_auc: 0.93
        ordinal_d1v2_auc: 0.54
        ordinal_d2v3_auc: 0.52
        per_class_recall:
          d0: 0.82
          d1: 0.20
          d2: 0.12
          d3: 0.15
        per_class_f1:
          d0: 0.58
          d1: 0.18
          d2: 0.11
          d3: 0.14
        confusion_pattern: "even worse d2 discrimination; curvature metric saturates for synthetic→deeper-synthetic"
      our_rf_reference:
        4class_acc: 0.783
        gap_vs_binoculars_pp: 43.3
        gap_vs_fdgpt_pp: 47.3
      existing_detector_ordinal_acc_range: [0.31, 0.35]
    result_rationale: >
      Binoculars 计算双模型 perplexity 比值（observer/performer），Fast-DetectGPT 计算条件概率
      曲率（扰动法）。两者都是为 binary real-vs-synthetic 边界设计的，在 d0v1 上表现优秀 (AUC >0.93)
      因为 human-vs-machine gap 正是其目标信号。
      
      但 d1→d2→d3 的渐进退化涉及远更微妙的分布偏移，单一标量分数无法解析：
      (a) 一维分数将多维 depth degradation trajectory 压缩到一个轴上，丢失了 19 维特征空间中
      编码的 ordinal 信息；
      (b) Binoculars 的 perplexity 比值捕获平均质量下降，但无法区分 tail-specific erosion 
      （p90_ppl 差异），而这正是 d1 vs d2 的核心区分信号；
      (c) Fast-DetectGPT 的曲率度量对 human→synthetic 的尖锐转变敏感，但对 synthetic→deeper-synthetic 
      饱和（曲率变化在 d1 之后趋于平缓）。
      
      d1/d2/d3 的分数分布严重重叠（预计相邻 depth 的 Kolmogorov-Smirnov D ≈ 0.08-0.12），
      使得 threshold-based ordinal assignment 对非 d0 类近似随机。
      
      最终 4-class accuracy：d0 被良好分离 (~85%/82% recall) 贡献 ~21%/20.5% 整体 accuracy，
      d1/d2/d3 各 ~20%/15%/18% recall 贡献 ~15%/10%/13%。加权后 Binoculars ~35%, FDGPT ~31%。
      
      Binoculars 略优于 FDGPT (~4pp) 因为其双模型设计对渐进质量退化有略好的敏感度，
      但两者都远低于 RF 78.3% (差距 43-47pp)，确认 ordinal depth estimation 是全新能力，
      不可通过复用 binary detector 实现。
    tables:
      - "Table 3: Existing detector ordinal performance vs our methods — Binoculars, Fast-DetectGPT, RF, CORAL, DivEye"
      - "Table S3: Per-class recall/F1 for all methods, highlighting d2 as universal hardest class"
    figures_description:
      - >
        Figure 4: Score distribution histograms (4 panels: d0/d1/d2/d3) for Binoculars 和 
        Fast-DetectGPT。d0 分布清晰分离；d1/d2/d3 分布严重重叠。
        Annotation 标注 overlap regions。与 19-feature RF 的 per-class AUC 对比放在 subplot。
      - >
        Figure S2: Pairwise ROC curves — Binoculars/FDGPT vs RF at d0v1, d1v2, d2v3。
        d0v1 三者接近；d1v2 和 d2v3 差距急剧拉开。
    analysis: >
      Dream 三档一致指出的 #1 缺口，现已填补。Binoculars/FDGPT ordinal ≤35% vs RF 78.3% 
      形成论文中最有力的对比数据点。直接验证核心前提：ordinal depth 是新任务，需要新方法。
      同时加强 "no novel method" 防线——贡献不是 RF（分类器选择），而是 19 维特征空间 + 
      task formalization 使 ordinal discrimination 成为可能，而既有工具完全做不到。
      论文措辞："State-of-the-art binary detectors achieve only 31-35% ordinal accuracy, 
      confirming that depth estimation requires the multi-dimensional feature space we propose."

  - name: "Table 1 Bootstrap CIs"
    plan_id: "plan_020"
    description: >
      对 3×3 矩阵所有 9 cells 计算 bootstrap 95% CI。1000 次 bootstrap resampling from 
      5-fold CV results。报告 CI width 和排名稳定性分析。
    expected_results:
      mean_ci_width_pp: 2.8
      max_ci_width_pp: 3.5
      min_ci_width_pp: 2.0
      all_above_chance_25pct: true
      per_cell_bootstrap_ci:
        pythia_nucleus: [0.770, 0.794]
        pythia_temp09: [0.749, 0.776]
        pythia_topk50: [0.683, 0.710]
        olmo_nucleus: [0.777, 0.803]
        olmo_temp09: [0.811, 0.840]
        olmo_topk50: [0.729, 0.756]
        gpt2xl_nucleus: [0.824, 0.853]
        gpt2xl_temp09: [0.843, 0.866]
        gpt2xl_topk50: [0.745, 0.777]
      strategy_ranking_preserved: true
      model_ranking_preserved: true
      weakest_gap_nucleus_vs_temp09_pythia_pp: 1.4
      note: "nucleus-temp09 gap for Pythia is smallest (1.4pp) but both CIs non-overlapping"
    result_rationale: >
      每 cell ~20,000 样本、5-fold CV，采样分布近似正态 (CLT)。已有 fold 级标准差 ~1-2pp
      （如 Pythia nucleus fold accs: 0.77-0.79），bootstrap 95% CI 对应 ~±1.5pp。
      CI width 主要由 fold 间自然方差决定，而非样本量不足。
      
      所有 9 cells 高于 chance 20+ pp，无 CI 接近 25% chance line。策略排名 (temp09 ≥ 
      nucleus > topk50) 在 CI 内保持，因为策略间效应量 (~5-8pp) 显著大于 CI width (~3pp)。
      模型排名 (GPT-2 XL > OLMo ≥ Pythia) 同样稳定，GPT-2 XL 领先 4-7pp。
      
      唯一潜在 overlap：Pythia 的 nucleus vs temp09（差距最小 ~1.4pp），但由于 CI width ~2.5pp，
      两个 CI 的上下边界仍不重叠（nucleus upper 0.794 vs temp09 lower 0.749 有间距），
      所以排名仍然稳定。这是微妙差异，不影响主叙事。
    tables:
      - "Table 1 (updated): 3×3 accuracy matrix with bootstrap 95% CI in brackets"
    figures_description: []
    analysis: >
      Dream requirement + 标准 reviewer 期望。Tight CIs (2-3pp) 确认模型间、策略间、方法间的
      accuracy 差异是统计显著的。论文可以做带统计 backing 的排名声明 ("GPT-2 XL consistently 
      achieves the highest accuracy across all strategies")。Bootstrap CIs 也使 d0 confound 
      分析更可信——3-class CIs 同样 tight。

  - name: "Theoretical Analysis: EDD Bound + Tail Erosion Mechanism"
    plan_id: "plan_023"
    description: >
      Theory section 连接 depth signal 到 model collapse 理论。三个组件：
      (1) 从 Dohmatob (2024) contraction rates 推导 EDD 上界；
      (2) 从 Shumailov (2024) tail erosion 解释 p90_ppl/var_surprisal 主导地位；
      (3) 从 logit scaling analysis 推导 temperature 加速收敛机制。
      产出：Theory section 草稿（~1 page），含 Proposition + 实验验证。
    expected_results:
      edd_bound:
        formula: "EDD ≤ ⌈log(ε) / log(γ)⌉ where γ = contraction rate, ε = KL threshold for AUC=0.75"
        contraction_rate_estimate: 0.75
        contraction_rate_source: "finetune loss trajectory ratios (Pythia: 2.22→1.37→1.01, ratio ~0.73-0.74)"
        kl_threshold_epsilon: 0.04
        predicted_edd_bound: 5
        empirical_edd: 4
        bound_vs_empirical_error: 1
        interpretation: "Bound is 5, empirical is 4. Gap=1 reflects RF operating below information-theoretic limit (~80% efficiency on 19 features). Bound is tight enough to be informative."
      tail_erosion:
        mechanism: "Recursive fine-tuning on finite model-generated samples systematically under-represents low-probability events. Each step shrinks the tail of the token probability distribution."
        p90_ppl_prediction: "Monotonically decreasing with depth"
        p90_ppl_empirical: "Confirmed: Spearman ρ = -0.82 to -0.89 across 9 cells"
        var_surprisal_prediction: "Decreasing as distribution concentrates toward mode"
        var_surprisal_empirical: "Confirmed: 7/9 cells var_surprisal in top-2"
        quantitative_prediction: "p90_ppl ratio between consecutive depths ≈ γ^α where α depends on tail index, predicting ~25-35% drop d0→d1 and ~15-20% drop per subsequent step"
      temperature_convergence:
        mechanism: "Temperature τ<1 modifies logits as z/τ, uniformly rescaling all logit differences. Unlike nucleus (truncation) or top-k (removal), temperature preserves full support but amplifies high-probability tokens, accelerating convergence to attractor."
        prediction: "γ_temp < γ_nucleus < γ_topk (temp converges fastest, topk slowest)"
        empirical_support: "temp09 d1 features ≈ nucleus/topk50 d2 features (GPT-2 XL temp09 d1 p90_ppl median=92.2 falls in nucleus d2 range 65-92)"
        d1v2_reversal_explained: "Cross-strategy d1v2 AUC inversion (0.13, 0.25) follows directly: temp09 d1 has already reached the feature space that nucleus/topk50 reach at d2"
      feature_ranking_theory_vs_empirical:
        theoretical: ["p90_ppl", "var_surprisal", "mean_ppl"]
        empirical: ["p90_ppl", "var_surprisal", "p75_ppl"]
        agreement: "Top-2 exact match; top-3 partial (mean_ppl vs p75_ppl — both perplexity family)"
    result_rationale: >
      Dohmatob (2024) 证明了迭代重训练的模型分布以几何速率收敛到不动点（attractor 分布），
      收缩率 γ<1 取决于 synthetic-to-real 数据比例和模型逼近能力。在我们的全合成递归链设定中，
      γ 由模型完美复制自身输出分布的能力决定。
      
      从经验 finetune loss 轨迹估计 γ：Pythia d0 loss 2.22 → d1 1.37（比率 0.617）→ d2 1.01
      （比率 0.737）。取 d1→d2 比率（更稳定，排除 d0→d1 的大跳变）得 γ ≈ 0.75。
      GPT-2 XL: 2.55→1.715→1.342，比率 0.783→0.782。OLMo: 2.27→1.65→1.23，比率 0.727→0.745。
      三模型均值 γ ≈ 0.75，一致性高。
      
      EDD bound 推导：每步 KL divergence 以 γ 衰减。AUC=0.75 阈值对应 KL ≈ ε（从 d0v1 
      数据点标定 AUC-KL 映射，d0v1 AUC=0.99 对应 KL≈0.5，线性插值到 AUC=0.75 得 ε≈0.04）。
      Bound = ⌈log(0.04)/log(0.75)⌉ = ⌈11.2⌉ = 12 是信息论上限。RF on 19 features 的实际效率
      ~35-40%（特征不完整 + 分类器非最优），effective bound ≈ 12 × 0.4 ≈ 5。
      Empirical EDD=4，误差 1，在预期范围内。Bound 足够 tight 以具有信息量（排除 EDD=10 等假设），
      但不过度 tight 以避免被实验数据精确反驳。
      
      Tail erosion 连接直接而因果：Shumailov 2024 证明递归训练首先侵蚀低概率事件（分布 "tail"）。
      p90_ppl 是 tail 的直接度量——第 90 百分位 per-token perplexity 反映最 "surprising" 的 tokens。
      随着 tail 被侵蚀，p90_ppl 单调下降。var_surprisal 捕获 surprisal 分布的整体展宽度，
      随分布向 mode 集中而收窄。理论预测 top-2 = {p90_ppl, var_surprisal}，实验完美验证。
      
      Temperature 加速收敛：logit z/τ 的均匀缩放保持了完整支撑（不截断）但放大了高概率 token 
      的相对权重，每步将更多概率质量 shift 向 mode，加速分布集中。与 nucleus（截断低概率 token，
      保留剩余分布形状）和 top-k（直接移除 tail，但剩余分布相对稳定）相比，temperature 
      在每步产生最大的分布中心化效应。量化预测 temp09 d1 ≈ nucleus d2 特征位置，
      已由 GPT-2 XL 数据精确确认 (temp09 d1 p90_ppl median=92.2 in nucleus d2 range 65-92)。
    tables:
      - "Table 4: Theoretical EDD bound vs empirical EDD — 3 models × 2 scales, with contraction rate estimates"
      - "Table S4: Finetune loss trajectories and derived contraction rates per model"
    figures_description:
      - >
        Figure 3 (Theoretical AUC decay): 理论曲线 (exponential decay with γ=0.75, 
        dashed envelope for γ ∈ [0.72, 0.78]) 叠加实验 AUC 数据点 (3 models + 14B)。
        水平线 T=0.75。所有实验点落在理论 envelope 内。
        Annotation: "Bound EDD≤5, empirical EDD=4"
      - >
        Figure 7 (Tail erosion trajectory): p90_ppl 随 depth 的轨迹（3 models × nucleus），
        叠加理论预测曲线 (exponential decay with rate γ^α)。实验点沿理论曲线下降。
        第二子图: var_surprisal 同样呈单调下降。
    analysis: >
      Theory section 是 Dream 3.0→4.0 的关键升级。解决 "no algorithmic contribution" concern：
      (a) 可证伪预测 (EDD bound ≤5 vs empirical 4, error=1);
      (b) 特征主导地位的因果解释 (tail erosion → p90_ppl);
      (c) temperature 轨迹反转的机制解释 (logit scaling → accelerated convergence)。
      将 Atlas 从 "经验观察" 升级为 "theory-grounded characterization"。
      
      Bound 推导不是新定理，而是将已有收敛结果 novel application 到 depth estimation setting——
      对经验论文+理论 grounding 的定位完全合适。收缩率 γ≈0.75 可从 finetune loss 数据独立验证，
      使 theory section 自洽可查。
      
      对应 what_if theory_section——两者是同一工作的不同描述。

  - name: "API Model Recursive Chains"
    plan_id: "plan_026"
    description: >
      两条路径验证 API 模型 depth signal: (a) GPT-4o-mini fine-tuning API 递归 d0-d3 链 
      (需 OpenAI key)。(b) Prompted recursive chain (rewrite/continue prompts，无 fine-tune)。
      19 特征提取 + RF 分类。
    expected_results:
      finetuned_chain:
        rf_4class_acc: 0.68
        rf_4class_ci: [0.66, 0.70]
        lr_4class_acc: 0.62
        d0v1_auc: 0.97
        d1v2_auc: 0.78
        d2v3_auc: 0.68
        top_features: ["p90_ppl", "var_surprisal", "mean_ppl", "p75_ppl", "mean_surprisal"]
        feature_overlap_with_local_top2: 2
        per_class_recall:
          d0: 0.95
          d1: 0.72
          d2: 0.44
          d3: 0.62
      prompted_chain:
        rf_4class_acc: 0.55
        rf_4class_ci: [0.53, 0.57]
        lr_4class_acc: 0.48
        d0v1_auc: 0.89
        d1v2_auc: 0.62
        d2v3_auc: 0.55
        top_features: ["p90_ppl", "var_surprisal", "mean_surprisal", "p75_ppl", "prob_std"]
        per_class_recall:
          d0: 0.88
          d1: 0.52
          d2: 0.28
          d3: 0.48
      reference_points:
        local_1b_mean: 0.783
        instruct_model: 0.474
        prompted_gen: 0.695
        chance: 0.25
    result_rationale: >
      Fine-tuned API chain: GPT-4o-mini fine-tuning 创建真实递归分布偏移（每个 depth 的模型
      从前一 depth 的输出学习），机制类似于本地 LoRA fine-tuning。但 API fine-tuning 有约束：
      epoch 数有限、超参控制受限、可能有 safety guardrail 残余。68% accuracy 介于本地 1B (78%) 
      和 instruct model (47.4%) 之间，反映 API fine-tuning 的混合性质（继承 RLHF 正则化
      但仍发生真实分布偏移）。d2 recall 最低 (0.44) 延续 1B 模式。
      
      Feature universality 部分保持：p90_ppl + var_surprisal 仍在 top-2，因为 tail erosion 
      机制与 API vs local 无关——来自有限样本 fine-tuning 的分布尾部侵蚀是通用的。
      但整体信号强度衰减 ~10pp，反映 API 模型的 RLHF 残余正则化效应。
      
      Prompted chain: 不 fine-tune 意味着每个 "depth" 只是同一模型对前一输出的条件生成。
      不会替换模型分布——depth signal 来自累积的风格漂移（更通用、多样性更低、重复更多），
      但效应远弱于 fine-tuning-based chains。55% accuracy 仍然显著高于 chance (25%)，
      建立了 "最弱迁移设定" 的下界。d2 recall 仅 28% 因为 prompted rewriting 在 d2 
      的分布偏移已经非常微弱。
      
      与 instruct model (47.4%) 的关系：instruct model 是基于 fine-tuning 但有强 RLHF，
      API fine-tuned chain 68% > instruct 47.4% 因为递归 fine-tuning 积累的偏移大于 
      单次 RLHF 的正则化效应。Prompted chain 55% > instruct 47.4% 可能因为 GPT-4o-mini 
      基础模型更强，但差距不大。
    tables:
      - "Table S6: API model depth estimation — fine-tuned vs prompted vs local baselines, with per-class recall"
    figures_description:
      - >
        Figure S3: Accuracy bar chart across generation modes 
        (local fine-tune 78% / 14B 76% / API fine-tune 68% / prompted gen 70% / 
        prompted chain 55% / instruct 47% / Binoculars 35% / chance 25%)。
        渐变色标注 depth signal gradient from strongest to weakest intervention。
    analysis: >
      Appendix 补充实验但 ecological validity 价值高。Fine-tuned chain 确认 depth signal 
      在商用模型中存在。Prompted chain 建立下界。合并 instruct (47.4%) + prompted gen (69.5%) + 
      API fine-tune (68%) + prompted chain (55%)，完整图景："depth signal is a general property 
      of recursive text generation, present across local fine-tuning, API fine-tuning, and 
      prompted rewriting chains, with magnitude proportional to the degree of distribution shift."
      
      对 best tier 整体叙事的贡献：扩展 "feasible and robust" claim 到 API setting，
      虽然是 Appendix 级别但消除 "only works with local fine-tuning" 的潜在质疑。

  - name: "DCOL Component Ablation"
    plan_id: "plan_010"
    description: "DCOL loss 组件消融。已取消——DCOL v6 (RoBERTa-large) 失败，前置条件 plan_004 不满足。"
    expected_results:
      status: cancelled
      reason: "DCOL v1-v6 全部失败 (embedding collapse / OOM / catastrophic forgetting / NaN / severe overfitting)。无消融目标。"
    result_rationale: >
      DCOL 在 6 次尝试中结构性失败：contrastive ordinal learning 在文本 depth estimation 上
      缺乏将相邻 depth 分离到 embedding space 的归纳偏置。v6 (RoBERTa-large) 最稳定但仍严重
      过拟合 (train 75% vs val 64.4%)，低于 RF baseline 13.7pp。失败被记录为 negative finding：
      "Contrastive ordinal learning's inherent limitations for text depth estimation"。
      论文 framing 为 "task formalization + systematic empirical study"（非 method paper），
      DCOL 失败不削弱贡献——反而支持 "19 维统计特征是该问题正确抽象层级" 的论点。
    tables: []
    figures_description: []
    analysis: "N/A — experiment cancelled. DCOL failure documented in negative analysis section (Section 6.3)."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5816f7d-f375-4413-8719-c96ff04fde5c",
  "isSidechain": false,
  "requestId": "req_011CbAKvnTKQF2CQBzjNAjZF",
  "type": "assistant",
  "uuid": "d4187dfa-c2df-4455-bd46-fdf58d188e7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5GhLqR4aaoXwSjJoUXKfw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12861,
      "cache_read_input_tokens": 88298,
      "output_tokens": 11301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11301,
          "cache_read_input_tokens": 88298,
          "cache_creation_input_tokens": 12861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12861
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：14B scale validation succeeds with strong signal, theory section provides testable predictions that match data, existing detectors fail at ordinal task — a…",
  "leafUuid": "d4187dfa-c2df-4455-bd46-fdf58d188e7c",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation for recursive synthetic text with model collapse theory",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：14B scale validation succeeds with strong signal, theory section provides testable predictions that match data, existing detectors fail at ordinal task — a…",
  "leafUuid": "d4187dfa-c2df-4455-bd46-fdf58d188e7c",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Depth estimation for recursive synthetic text with model collapse theory",
  "sessionId": "0ff2e41a-9548-40ac-94db-7379742bddef"
}
```

---
