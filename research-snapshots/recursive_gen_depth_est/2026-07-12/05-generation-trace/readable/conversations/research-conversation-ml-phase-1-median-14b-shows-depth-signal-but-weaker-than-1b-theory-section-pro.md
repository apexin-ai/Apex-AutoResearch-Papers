# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：14B shows depth signal but weaker than 1B, theory section provides post-ho

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50.jsonl`
- **Structured JSON:** [`cccb0f968edf76d9a964.json`](../../sessions/cc/cccb0f968edf76d9a964.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T16:15:28.131Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T16:15:28.131Z",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：14B shows depth signal but weaker than 1B, theory section provides post-hoc rationalization but not predictive bounds, existing detectors show weak ordinal capability — claims need scope hedging, paper is borderline accept\n核心假设：['14B 4-class acc 55-72%, p90_ppl in top-5 but var_surprisal drops out of top-5 or rank inverts', \"14B EDD=3 (d3v4 AUC < 0.75), lower than 1B's EDD=4 → scale-dependent EDD attenuation\", \"Theory section provides qualitative connection (tail erosion narrative) but cannot derive precise EDD bound; Dohmatob contraction analysis yields loose bound (EDD ≤ 8) that doesn't constrain\", \"Binoculars/Fast-DetectGPT achieve 40-55% ordinal acc → partial overlap with our shallow-depth discrimination, weakening 'new task' exclusivity\", '3/3 seed stability confirmed but one model shows >3pp variance, requiring explicit variance-aware CI reporting', \"Instruct model weakness + 14B signal degradation creates 'small base model only?' reviewer question\"]\n关键指标范围：{'14b_4class_acc': [0.55, 0.72], '14b_d1v2_auc': [0.65, 0.8], '14b_edd': [3, 3], '14b_top2_feature_overlap_with_1b': [1, 1], 'existing_detector_ordinal_4class_acc': [0.4, 0.55], 'seed_robustness_max_delta_pp': [2.0, 5.0], 'theory_edd_bound_vs_empirical_error': [2, 4], 'simulated_reviewer_meta_score': [3.0, 3.5], 'accept_probability': [0.25, 0.45]}\n叙事方向：需要调整 Claims 强度，但不降级目标 venue。 Claim 1: \"feasible, accurate, robust across scales\" 改为 \"feasible and accurate at 1-1.5B, with attenuated but persistent signal at 14B scale\"。 删除 \"robust across scales\" 的无条件断言，改为 \"scale-dependent signal strength with consistent feature family (perplexity tail statistics)\"。 Claim 2 (Atlas): EDD 从 \"=4 across models and scales\" 改为 \"=4 at 1B, =3 at 14B, suggesting scale-dependent discriminability horizon\"。 理论节降格为 \"Theoretical Motivation\" 而非 \"Theoretical Analysis\"——提供 intuition 而非 derivation。 可以新增一条 finding: \"depth signal attenuates with model capacity, consistent with larger models producing more uniform recursive degradation\"。 Claim 3: 不变（跨策略 pipeline 独立于 scale）。 对 existing detector: 承认 Binoculars 在 d0v1 上接近我们的表现，但论证 ordinal depth (d1/d2/d3 区分) 仍是我们独有的贡献。 需要 AC champion 或 revision opportunity。补充实验可能包括: 14B 多策略覆盖、intermediate scale (3B/7B) 连续曲线。 关键 reviewer rebuttal: \"signal attenuation at scale is itself a scientifically valuable finding — it characterizes the boundary of feasibility\"。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: recursive_gen_depth_est\nfocus: Evaluate whether adding a theoretical analysis section (connecting to model collapse theory) plus completed 14B scale validation and 3/3 model seed robustness coverage can push the paper from 3.0 Findings to 4.0 Conference accept. Pay special attention to: (1) whether the theory section adequately addresses the 'no algorithmic contribution' concern, (2) remaining gaps that would prevent 4.0, (3) whether the paper's positioning as 'empirical study + theoretical grounding + task formalization' is sufficient for EMNLP Main.\n\n## paper_framing.md\n\n# Paper Framing — recursive_gen_depth_est\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\n- EMNLP 2026 special theme \"New Missions for NLP Research\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\n\n## Core Claims (3 条 + Discussion implication)\n\n1. **Ordinal depth estimation is feasible, accurate, and robust across scales and generation modes**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark (1–1.5B), Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all settings. **Scale robustness**: Clean FP16 13B experiment (Qwen2.5-14B, no quantization) confirms depth signal persists at mainstream model scale, addressing the \"small model only\" concern from prior 7B QLoRA experiments. **Ecological validity**: Prompted generation experiment (topic-seeded text, not BOS-only unconditional) confirms depth signal is not an artifact of unnatural generation mode.\n\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the d1/d2 boundary remains open. This atlas spans 3 model families × 3 decoding strategies, with scale consistency confirmed at 14B.\n\n3. **Cross-strategy depth estimation via two-stage pipeline + strategy-invariant signal discovery**: Naive cross-strategy transfer degrades to 59.1% with d1v2 boundary inversion. We propose a two-stage solution: (a) strategy identification classifier (57.8% — strategies share more feature space than expected), then (b) strategy-conditioned depth classifiers. The pipeline improves cross-strategy accuracy by **+11.5pp** on average (59.1% → 70.5%), with per-model results: GPT-2 XL 73.0%, OLMo 69.4%, Pythia 69.3%. Oracle ceiling at 78.3%. **Caveat**: improvement is consistent across models but absolute accuracy varies (2/3 models individually below 70%); paper must claim \"+11.5pp improvement\" rather than \"≥70% universal recovery\". The surprising finding: even with imperfect strategy routing, the pipeline works because depth signal has a **strategy-invariant core** (~60% accuracy floor) plus a strategy-specific component. This reframes cross-strategy transfer from \"broken\" to \"substantially improved with clear ceiling for future work\".\n\n4. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).\n\n## Story Spine\n\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \"is this synthetic?\" but not \"how many recursive cycles has this undergone?\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\n\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\n\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark spanning 1B–14B models across 3 decoding strategies and 4 depths, and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all settings, (b) model-dependent strategy interaction effects with an identified root cause, and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, and propose a two-stage strategy-aware pipeline that solves the cross-strategy deployment challenge. The depth signal persists under prompted generation (not just BOS-seeded), confirming ecological relevance.\n\n- **Headline result template**: \"On our multi-generational benchmark spanning model scales from 1B to 14B and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all settings. The depth signal persists under prompted (topic-seeded) generation and at 14B scale without quantization. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75). We identify strategy-dependent feature trajectory reversal and propose a two-stage pipeline that restores near within-strategy accuracy for cross-strategy deployment.\"\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) completed via plan_011.\n\n## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)\n\nDCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。\n\n- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**\n- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL\n- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（\"contrastive ordinal learning 在文本深度估计的固有局限\"）\n- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）\n- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP \"New Missions\" track\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding; (e) **cross-strategy two-stage pipeline (Claim 3)** is a concrete practical contribution, not just analysis. EMNLP \"New Missions\" track explicitly values problem formalization.\n- **Controlled vs wild gap**: Mitigation: prompted generation experiment validates signal under realistic generation conditions (topic-seeded, not BOS-only). Honest scoping — controlled setting is primary, prompted generation bridges toward ecological validity.\n- **\"No novel method\" concern**: Mitigation: (a) RF/CORAL are tools, not the contribution; (b) the two-stage cross-strategy pipeline IS a novel practical method for strategy-aware depth estimation; (c) 13B clean experiment shows method scales without modification. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).\n- **\"Small model only\" concern**: Eliminated by clean 13B FP16 experiment. Prior 7B QLoRA results were contradictory due to quantization artifacts; 13B clean run provides definitive scale evidence.\n\n## Dream-Derived Requirements (D002, 2026-05-14)\n\n三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：\n\n### 论文写作硬约束\n1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式\n2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。\"Atlas without maps is a contradiction\"\n3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)\n4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity\n\n### 指标报告硬约束\n5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection\n6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值\n7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis\n\n### Framing 方向\n8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 \"one strong method within the framework\"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。\n9. **\"First systematic empirical map\" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage\n\n### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)\n10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 \"soft sampling\"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 \"soft sampling\" 分组已被反转数据推翻。\n11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。\n12. **Limitations 必须写明跨策略部署约束** — \"跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。\"不可仅将反转作为正面发现消化。\n\n## Anticipated Reviewer Concerns\n\n1. \"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 \"three models all achieve statistically significant EDD=4\"。正确措辞：\"d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)\"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。\n2. \"Why ordinal and not just binary?\" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\n3. \"Generalization to unseen models/strategies?\" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation could recover d1v2 AUC remains open. Discuss as \"strategy shapes degradation trajectory\" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).\n4. \"No novel method — just RF on features\" → (a) Contribution is task formalization + Atlas + EDD + systematic findings, not just method; (b) the two-stage cross-strategy pipeline (Claim 3) IS a novel practical method that solves the deployment challenge; (c) 13B clean experiment confirms the approach scales without modification. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9+ settings is itself a finding.\n5. \"d0 confound inflates headline metrics\" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy\n6. \"EDD threshold is arbitrary\" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)\n7. \"No figures for Atlas\" → Minimum 4 figures (Dream D002)\n8. \"Bibliography too thin\" → 25+ refs covering all relevant subfields (Dream D002)\n9. \"Model-strategy interaction is just noise\" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.\n10. \"Cross-strategy deployment is unreliable\" → **Now addressed by Claim 3**: Two-stage pipeline (strategy identification → strategy-conditioned depth classification) provides a practical solution. Strategy classifier achieves 57.8% accuracy on 19 features (below the expected >90%), indicating strategy distributions are less separable than anticipated. A two-stage pipeline (oracle strategy identification + strategy-conditioned depth classification) recovers 11.5pp over naive LOO, though practical deployment still requires either strategy metadata or improved routing. The root cause (temperature's accelerated convergence) is identified and the mechanism explained.\n11. \"Signal is an artifact of unconditional BOS-seeded generation\" → Prompted generation experiment (plan_016) tests depth signal under topic-seeded generation. If signal persists → validates ecological relevance; if not → important finding about generation mode dependence (written as limitation).\n12. \"Only tested on small models (1–1.5B)\" → Clean 13B FP16 experiment (Qwen2.5-14B, plan_017) confirms scale robustness without quantization confounds. Prior 7B QLoRA results were contradictory — now superseded by clean experiment.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001a\n  claim: 1\n  description: Pythia-1.4B recursive chain — nucleus p=0.95 (MVP)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  notes: '4 depths × 1 strategy. 78.2% 4-class acc, d1v2 AUC 0.861. Content-type control:\n    81.6%.'\n  registry_id: mvp_pipeline_pythia_002\n  conclusion: success\n  metrics: &id001\n    full_4class_acc: 0.782\n    full_4class_acc_ci:\n    - 0.769\n    - 0.794\n    full_4class_acc_stratified: 0.781\n    full_mae: 0.2367\n    full_auc_0v1: 0.9975\n    full_auc_1v2: 0.8607\n    full_auc_2v3: 0.8005\n    filtered_4class_acc: 0.816\n    filtered_4class_acc_ci:\n    - 0.803\n    - 0.829\n    filtered_mae: 0.1995\n    filtered_auc_0v1: 0.9977\n    filtered_auc_1v2: 0.8782\n    filtered_auc_2v3: 0.8323\n    filtered_sample_count: 16993\n    three_class_acc: 0.708\n    three_class_acc_ci:\n    - 0.692\n    - 0.725\n    three_class_mae: 0.3203\n    three_class_auc_1v2: 0.854\n    three_class_auc_1v3: 0.9569\n    three_class_auc_2v3: 0.7931\n    three_class_recall_d1: 0.79\n    three_class_recall_d2: 0.607\n    three_class_recall_d3: 0.728\n    three_class_precision_d1: 0.852\n    three_class_precision_d2: 0.605\n    three_class_precision_d3: 0.68\n    three_class_f1_d1: 0.82\n    three_class_f1_d2: 0.606\n    three_class_f1_d3: 0.703\n    three_class_lr_acc: 0.671\n    filtered_three_class_acc: 0.747\n    filtered_three_class_acc_ci:\n    - 0.727\n    - 0.764\n    filtered_three_class_mae: 0.2759\n    filtered_three_class_recall_d1: 0.862\n    filtered_three_class_recall_d2: 0.635\n    filtered_three_class_recall_d3: 0.735\n    filtered_three_class_precision_d1: 0.867\n    filtered_three_class_precision_d2: 0.659\n    filtered_three_class_precision_d3: 0.704\n    filtered_three_class_f1_d1: 0.864\n    filtered_three_class_f1_d2: 0.647\n    filtered_three_class_f1_d3: 0.719\n    filtered_three_class_auc_1v2: 0.8926\n    filtered_three_class_auc_1v3: 0.9769\n    filtered_three_class_auc_2v3: 0.8272\n    filtered_three_class_sample_count: 12012\n    best_model: RandomForest\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    truncation_length: 498\n    feature_dim: 19\n- id: plan_001b\n  claim: 1\n  description: Pythia-1.4B — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: pythia_temp09_001\n  notes: τ=0.9 temp-only decoding. Data→data/pythia_temp09/. Launched on cuda:0 after\n    OLMo.\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.7625\n      rf_accuracy_ci:\n      - 0.749\n      - 0.7753\n      lr_accuracy: 0.7405\n      lr_accuracy_ci:\n      - 0.7265\n      - 0.7545\n      pairwise_auc:\n        0v1: 0.9968\n        0v2: 0.9993\n        0v3: 0.9991\n        1v2: 0.8327\n        1v3: 0.959\n        2v3: 0.7928\n      top_features:\n      - var_surprisal (0.1776)\n      - p90_ppl (0.1501)\n      - mean_ppl (0.1140)\n      - mean_surprisal (0.0889)\n      - p75_ppl (0.0687)\n      feature_dim: 19\n      truncation_length: 498\n    three_class_full:\n      accuracy: 0.6983\n      accuracy_ci:\n      - 0.682\n      - 0.715\n      mae: 0.3357\n      recall:\n        d1: 0.802\n        d2: 0.554\n        d3: 0.739\n      precision:\n        d1: 0.792\n        d2: 0.608\n        d3: 0.686\n      f1:\n        d1: 0.797\n        d2: 0.58\n        d3: 0.712\n      pairwise_auc:\n        d1v2: 0.8354\n        d1v3: 0.9631\n        d2v3: 0.8043\n    three_class_filtered:\n      accuracy: 0.7252\n      accuracy_ci:\n      - 0.7064\n      - 0.7427\n      mae: 0.2953\n      recall:\n        d1: 0.842\n        d2: 0.596\n        d3: 0.735\n      precision:\n        d1: 0.821\n        d2: 0.628\n        d3: 0.715\n      f1:\n        d1: 0.831\n        d2: 0.611\n        d3: 0.725\n      pairwise_auc:\n        d1v2: 0.8656\n        d1v3: 0.9772\n        d2v3: 0.8295\n      n_samples: 11445\n      n_removed: 3555\n    finetune_losses:\n      depth_0: 2.222\n      depth_1: 1.37\n      depth_2: 1.006\n    code_contamination:\n      d0: 0.004\n      d1: 0.077\n      d2: 0.116\n      d3: 0.136\n- id: plan_001c\n  claim: 1\n  description: Pythia-1.4B — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: pythia_topk50_001\n  notes: top-k k=50 decoding. Data→data/pythia_topk50/. Queued for cuda:1 after GPT-2\n    XL.\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.696\n    rf_4class_acc_ci:\n    - 0.6825\n    - 0.7107\n    lr_4class_acc: 0.682\n    rf_3class_acc: 0.592\n    rf_3class_acc_ci:\n    - 0.575\n    - 0.6107\n    rf_3class_filtered_acc: 0.6133\n    rf_3class_filtered_acc_ci:\n    - 0.593\n    - 0.6312\n    pairwise_auc_rf:\n      d0v1: 0.9927\n      d0v2: 0.9983\n      d0v3: 0.9978\n      d1v2: 0.7518\n      d1v3: 0.9176\n      d2v3: 0.6918\n    pairwise_auc_3class_filtered_rf:\n      d1v2: 0.768\n      d1v3: 0.9323\n      d2v3: 0.7013\n    feature_importance_top5:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    finetune_loss:\n      depth_0: 2.2406\n      depth_1: 1.6704\n      depth_2: 1.4374\n    code_contamination_narrow:\n      depth_0: 0.004\n      depth_1: 0.077\n      depth_2: 0.123\n      depth_3: 0.131\n- id: plan_002\n  claim: 1\n  description: OLMo-1B recursive chain (4 depths × 3 strategies)\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: cross_model_olmo_002\n  notes: OLMo-1B on Dolma. q_proj/k_proj/v_proj LoRA. olmo_001 failed (script bug),\n    olmo_002 重跑。等 cuda:0 释放。\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.788\n    four_class_acc_ci:\n    - 0.776\n    - 0.8\n    four_class_acc_lr: 0.751\n    auc_0v1: 0.9834\n    auc_0v2: 0.9949\n    auc_0v3: 0.9989\n    auc_1v2: 0.8673\n    auc_1v3: 0.9806\n    auc_2v3: 0.8124\n    three_class_acc: 0.744\n    three_class_acc_ci:\n    - 0.728\n    - 0.76\n    three_class_mae: 0.27\n    three_class_auc_1v2: 0.8664\n    three_class_auc_1v3: 0.9852\n    three_class_auc_2v3: 0.8274\n    three_class_recall:\n      d1: 0.864\n      d2: 0.607\n      d3: 0.761\n    three_class_precision:\n      d1: 0.863\n      d2: 0.646\n      d3: 0.718\n    four_class_per_class:\n      d0:\n        precision: 0.95\n        recall: 0.99\n        f1: 0.97\n      d1:\n        precision: 0.85\n        recall: 0.82\n        f1: 0.83\n      d2:\n        precision: 0.63\n        recall: 0.59\n        f1: 0.61\n      d3:\n        precision: 0.71\n        recall: 0.76\n        f1: 0.73\n    finetune_losses:\n      depth_0: 2.269\n      depth_1: 1.65\n      depth_2: 1.226\n    top_features:\n    - p90_ppl (0.18)\n    - var_surprisal (0.16)\n    - p75_ppl (0.11)\n    - mean_surprisal (0.08)\n    - type_token_ratio (0.06)\n    code_contamination:\n      d0: 0.005\n      d1: 0.027\n      d2: 0.007\n      d3: 0.008\n    feature_dim: 19\n    truncation_length: 507\n- id: plan_003\n  claim: 1\n  description: GPT-2 XL 1.5B recursive chain (4 depths × 3 strategies)\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: cross_model_gpt2xl_001\n  notes: GPT-2 most studied in collapse literature. WebText training data. c_attn/c_proj\n    LoRA.\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.833\n    four_class_acc_ci:\n    - 0.823\n    - 0.845\n    four_class_acc_lr: 0.813\n    auc_0v1: 0.9941\n    auc_0v2: 0.9965\n    auc_0v3: 0.9988\n    auc_1v2: 0.9131\n    auc_1v3: 0.9857\n    auc_2v3: 0.8829\n    three_class_acc: 0.793\n    three_class_acc_ci:\n    - 0.778\n    - 0.806\n    three_class_auc_1v2: 0.9109\n    three_class_auc_1v3: 0.989\n    three_class_auc_2v3: 0.8885\n    finetune_losses:\n      depth_0: 2.55\n      depth_1: 1.715\n      depth_2: 1.342\n    top_features:\n    - p90_ppl (0.208)\n    - var_surprisal (0.208)\n    - p75_ppl (0.103)\n    - mean_surprisal (0.082)\n    - mean_ppl (0.065)\n    code_contamination:\n      d0: 0.005\n      d1: 0.005\n      d2: 0.013\n      d3: 0.007\n- id: plan_002b\n  claim: 1\n  description: OLMo-1B — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: olmo_temp09_001\n  notes: 3×3 matrix cell. OLMo temp09. olmo_temp09_001 正在运行 (PID 205384, cuda:1)。之前被\n    cron 子进程误报为 failed，已修正。olmo_temp09_002 已取消。\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.8203\n      d1v2_auc: 0.901\n    three_class_filtered:\n      rf_accuracy: 0.7757\n    finetune_losses:\n      depth_0: 2.27\n      depth_1: 1.63\n      depth_2: 1.18\n    code_contamination_narrow_max: 0.007\n    top_features:\n    - p90_ppl (0.199)\n    - var_surprisal (0.174)\n    - p75_ppl (0.126)\n- id: plan_002c\n  claim: 1\n  description: OLMo-1B — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: olmo_topk50_001\n  notes: 3×3 matrix cell. OLMo topk50. 等 cuda:1 释放后提交。\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      lr_accuracy: 0.757\n      lr_accuracy_ci:\n      - 0.7425\n      - 0.7702\n      rf_accuracy: 0.742\n      rf_accuracy_ci:\n      - 0.7282\n      - 0.7555\n    pairwise_auc:\n      lr:\n        d0v1: 0.9969\n        d0v2: 0.9995\n        d0v3: 0.9998\n        d1v2: 0.8293\n        d1v3: 0.9592\n        d2v3: 0.7497\n      rf:\n        d0v1: 0.993\n        d0v2: 0.9983\n        d0v3: 0.9991\n        d1v2: 0.8305\n        d1v3: 0.9591\n        d2v3: 0.7357\n    three_class:\n      lr_accuracy: 0.6567\n      lr_accuracy_ci:\n      - 0.6403\n      - 0.6733\n      rf_accuracy: 0.6517\n      rf_accuracy_ci:\n      - 0.635\n      - 0.6687\n    three_class_filtered:\n      lr_accuracy: 0.6703\n      lr_accuracy_ci:\n      - 0.653\n      - 0.6882\n      rf_accuracy: 0.6699\n      rf_accuracy_ci:\n      - 0.6537\n      - 0.6875\n    three_class_filtered_auc:\n      lr:\n        d1v2: 0.7903\n        d1v3: 0.97\n        d2v3: 0.7501\n      rf:\n        d1v2: 0.8071\n        d1v3: 0.9645\n        d2v3: 0.7364\n    feature_importance_top5:\n    - p90_ppl\n    - var_surprisal\n    - p75_ppl\n    - mean_surprisal\n    - p25_ppl\n    finetune_loss:\n      depth_1: 1.946\n      depth_2: 1.726\n    code_contamination:\n      narrow_pct:\n        depth_0: 0.4\n        depth_1: 0.8\n        depth_2: 0.3\n        depth_3: 0.4\n      broad_pct:\n        depth_0: 0.5\n        depth_1: 2.5\n        depth_2: 0.8\n        depth_3: 0.7\n- id: plan_003b\n  claim: 1\n  description: GPT-2 XL — temperature τ=0.9 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: gpt2xl_temp09_001\n  notes: 3×3 matrix cell. Running on cuda:1.\n  status: DONE\n  conclusion: success\n  metrics:\n    data:\n      samples_per_depth: 5000\n      total_samples: 20000\n      depths: 4\n    finetune_losses:\n      depth_1: 2.5498\n      depth_2: 1.6972\n      depth_3: 1.2922\n    code_contamination:\n      depth_0:\n        broad: 25\n        narrow: 20\n        broad_pct: 0.5\n        narrow_pct: 0.4\n      depth_1:\n        broad: 25\n        narrow: 40\n        broad_pct: 0.5\n        narrow_pct: 0.8\n      depth_2:\n        broad: 34\n        narrow: 80\n        broad_pct: 0.7\n        narrow_pct: 1.6\n      depth_3:\n        broad: 25\n        narrow: 76\n        broad_pct: 0.5\n        narrow_pct: 1.5\n    four_class:\n      rf_accuracy: 0.8542\n      rf_accuracy_ci:\n      - 0.843\n      - 0.8653\n      lr_accuracy: 0.8155\n      lr_accuracy_ci:\n      - 0.8025\n      - 0.8273\n      rf_auc:\n        d0v1: 0.9963\n        d0v2: 0.9992\n        d0v3: 1\n        d1v2: 0.9367\n        d1v3: 0.9947\n        d2v3: 0.8815\n      lr_auc:\n        d0v1: 0.984\n        d0v2: 0.9998\n        d0v3: 1\n        d1v2: 0.8903\n        d1v3: 0.9824\n        d2v3: 0.8183\n      top_features:\n      - p90_ppl\n      - mean_surprisal\n      - p75_ppl\n      - var_surprisal\n    three_class:\n      rf_accuracy: 0.82\n      rf_accuracy_ci:\n      - 0.806\n      - 0.834\n      lr_accuracy: 0.7773\n      lr_accuracy_ci:\n      - 0.7627\n      - 0.792\n      rf_auc:\n        d1v2: 0.9418\n        d1v3: 0.9967\n        d2v3: 0.8849\n    three_class_filtered:\n      rf_accuracy: 0.815\n      rf_accuracy_ci:\n      - 0.7999\n      - 0.8298\n      lr_accuracy: 0.7869\n      lr_accuracy_ci:\n      - 0.7711\n      - 0.8016\n      rf_auc:\n        d1v2: 0.937\n        d1v3: 0.9944\n        d2v3: 0.8891\n- id: plan_003c\n  claim: 1\n  description: GPT-2 XL — top-k k=50 chain (4 depths)\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: gpt2xl_topk50_001\n  notes: 3×3 matrix cell. GPT-2 XL topk50.\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      accuracy: 0.766\n      depth1_vs_depth2_auc: 0.8259\n      pass: true\n    three_class:\n      accuracy: 0.695\n      depth1_vs_depth2_auc: 0.8392\n      pass: true\n    three_class_filtered:\n      accuracy: 0.684\n      depth1_vs_depth2_auc: 0.8314\n      pass: true\n- id: plan_004\n  claim: 1\n  description: 'DCOL training: RoBERTa-large with learnable margins contrastive loss\n    (v6, non-blocking)'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: v1-v5 DeBERTa 全部失败 (D011)。v6 换 RoBERTa-large 非阻塞尝试。成功→bonus section，失败→negative\n    analysis。不阻塞论文进度。\n  registry_id: dcol_roberta_v6_001\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.6448\n    test_mae: 0.4052\n    best_val_acc: 0.6436\n    best_epoch: 1\n    epochs_run: 4\n    early_stopping: true\n    train_acc_final: 0.75\n    rf_baseline: 0.782\n    delta_vs_baseline: -0.137\n    overfitting: severe (train 75% vs val 64.4% at best epoch)\n    stability: resolved (no NaN, no collapse, collapse guard passed at step 500)\n- id: plan_005\n  claim: 1\n  description: 'Leave-one-model-out generalization (RF): train on 2 families, test\n    on 3rd'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: cross_model_loo_v1\n  notes: '3 rotations with RF classifier. Research-phase gate: cross-model acc ≥ 45%.\n    Plan A: 不依赖 DCOL。均值 66.4%，gate 通过。'\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_acc: 0.664\n    mean_3class_acc: 0.5544\n    holdout_pythia:\n      acc: 0.6242\n      ci95:\n      - 0.6205\n      - 0.6282\n      3class_acc: 0.499\n      3class_ci95:\n      - 0.4944\n      - 0.5034\n      d1v2_auc: 0.5617\n      d1v3_auc: 0.8547\n      d2v3_auc: 0.6534\n      d0v1_auc: 0.9921\n      d0v2_auc: 0.9999\n      d0v3_auc: 0.9998\n      per_class:\n        d0:\n          P: 0.9889\n          R: 1\n          F1: 0.9944\n        d1:\n          P: 0.6655\n          R: 0.493\n          F1: 0.5664\n        d2:\n          P: 0.3699\n          R: 0.2677\n          F1: 0.3106\n        d3:\n          P: 0.483\n          R: 0.7363\n          F1: 0.5834\n    holdout_olmo:\n      acc: 0.6921\n      ci95:\n      - 0.6884\n      - 0.696\n      3class_acc: 0.592\n      3class_ci95:\n      - 0.5873\n      - 0.5965\n      d1v2_auc: 0.7687\n      d1v3_auc: 0.9277\n      d2v3_auc: 0.6862\n      per_class:\n        d0:\n          P: 0.9783\n          R: 0.9925\n          F1: 0.9854\n        d1:\n          P: 0.7111\n          R: 0.7549\n          F1: 0.7324\n        d2:\n          P: 0.4616\n          R: 0.4327\n          F1: 0.4467\n        d3:\n          P: 0.5964\n          R: 0.5883\n          F1: 0.5923\n    holdout_gpt2xl:\n      acc: 0.6756\n      ci95:\n      - 0.6717\n      - 0.6795\n      3class_acc: 0.5723\n      3class_ci95:\n      - 0.5679\n      - 0.5767\n      d1v2_auc: 0.8157\n      d1v3_auc: 0.9149\n      d2v3_auc: 0.6639\n      d0v1_auc: 0.9927\n      d0v2_auc: 0.9919\n      d0v3_auc: 0.9876\n      per_class:\n        d0:\n          P: 0.9484\n          R: 0.9853\n          F1: 0.9665\n        d1:\n          P: 0.7093\n          R: 0.7465\n          F1: 0.7274\n        d2:\n          P: 0.4521\n          R: 0.5255\n          F1: 0.486\n        d3:\n          P: 0.5963\n          R: 0.445\n          F1: 0.5097\n    mean_per_class_recall:\n      d0: 0.9926\n      d1: 0.6648\n      d2: 0.4086\n      d3: 0.5899\n    lowest_recall_class: d2\n    lowest_recall_value: 0.4086\n    detailed_artifact: cross_model_loo_detailed.json\n- id: plan_006\n  claim: 2\n  description: 'Depth Degradation Atlas: monotonicity scores, EDD, cross-model/strategy\n    heatmaps'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: atlas_v1_analysis\n  notes: 'v1 完成: monotonicity ρ=-0.82~-0.89, EDD=3 (未饱和), cross-model Jaccard=0.667,\n    rank corr ρ>0.85. 4 JSON in artifacts/atlas/. 待完成: 正式出图(AUC decay/feature trajectory/heatmap/confusion\n    matrix) + 纳入 3×3 剩余 cells 数据.'\n  status: DONE\n  conclusion: success\n  metrics:\n    monotonicity_rho_range:\n    - -0.89\n    - -0.82\n    edd: 3\n    edd_saturated: false\n    cross_model_jaccard: 0.667\n    cross_model_rank_corr: 0.85\n    artifacts:\n    - monotonicity_scores.json\n    - cross_model_comparison.json\n    - edd_analysis.json\n    - feature_trajectory.json\n- id: plan_006b\n  claim: 1\n  description: '3-class experiment (d1/d2/d3 only): isolate pure depth gradient from\n    real-vs-synthetic signal'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_001a\n  status: DONE\n  registry_id: mvp_pipeline_pythia_002\n  notes: Reviewer-requested. 3-class acc=70.8% [0.692,0.725], d1v2 AUC=0.854, d2v3=0.793.\n    Results in mvp_pipeline_pythia_002 metrics.\n  conclusion: success\n  metrics: *id001\n- id: plan_007\n  claim: 1\n  description: 'Leave-one-strategy-out robustness (RF): train on 2 strategies, test\n    on 3rd'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: cross_strategy_loo_001\n  notes: '3 rotations per model with RF. Plan A: 不依赖 DCOL。均值 59.1%，9/9 > chance。temp09\n    d1v2 反转已解释 (Covariate Shift)。'\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_4class_acc: 0.5908\n    pythia_holdout_nucleus:\n      acc: 0.6935\n      d1v2_auc: 0.6903\n      d2v3_auc: 0.7626\n    pythia_holdout_temp09:\n      acc: 0.6281\n      d1v2_auc: 0.576\n      d2v3_auc: 0.724\n    pythia_holdout_topk50:\n      acc: 0.5151\n      d1v2_auc: 0.6393\n      d2v3_auc: 0.5801\n    gpt2xl_holdout_nucleus:\n      acc: 0.5993\n      d1v2_auc: 0.7826\n      d2v3_auc: 0.4985\n    gpt2xl_holdout_temp09:\n      acc: 0.5609\n      d1v2_auc: 0.1288\n      d2v3_auc: 0.6366\n    gpt2xl_holdout_topk50:\n      acc: 0.5364\n      d1v2_auc: 0.8308\n      d2v3_auc: 0.7222\n    olmo_holdout_nucleus:\n      acc: 0.6538\n      d1v2_auc: 0.7931\n      d2v3_auc: 0.6076\n    olmo_holdout_temp09:\n      acc: 0.5816\n      d1v2_auc: 0.2529\n      d2v3_auc: 0.7015\n    olmo_holdout_topk50:\n      acc: 0.5488\n      d1v2_auc: 0.8549\n      d2v3_auc: 0.7107\n    finding_temp09_d1v2_inversion: 'd1v2 AUC inverts when holding out temp09 (GPT-2\n      XL: 0.13, OLMo: 0.25) — temp09 d1→d2 features differ fundamentally from nucleus/topk50'\n- id: plan_008\n  claim: 1\n  description: 'DeBERTa end-to-end classifier: direct text→depth'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: n2_deberta_finetune_001\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_mean: 0.5831\n    accuracy_std: 0.0467\n    per_class_f1:\n      d0: 0.947\n      d1: 0.378\n      d2: 0.247\n      d3: 0.656\n    pairwise_auc:\n      d0v1: 0.981\n      d1v2: 0.733\n      d2v3: 0.755\n    vs_rf_baseline: 58.3% vs 78.2% (-19.9pp)\n    elapsed_seconds: 3727\n- id: plan_009\n  claim: 1\n  description: 'Baseline battery: DivEye, perplexity regression, CORAL, CE, zero-shot\n    LLM'\n  priority: P1\n  gpu_budget_hours: 8\n  registry_id: baseline_battery_001\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_reg_single_4class_acc: 0.251\n    ppl_reg_multi_4class_acc: 0.622\n    ce_mlp_4class_acc: 0.749\n    coral_4class_acc: 0.7807\n    coral_3class_acc: 0.7089\n    coral_mae: 0.2273\n    coral_d1v2_auc: 0.8179\n    diveye_4class_acc: 0.7817\n    diveye_3class_acc: 0.7098\n    diveye_d1v2_auc: 0.8654\n    rf_4class_acc: 0.781\n    lr_4class_acc: 0.75\n    note: CE-MLP 74.9% may be undertrained (5 epochs); CORAL updated to 100 epochs.\n      All results from Pythia nucleus baseline features.\n- id: plan_010\n  claim: 1\n  description: DCOL component ablation\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_004\n  status: planned\n  notes: DCOL v6 失败 (D018)，前置条件 plan_004 未满足，取消。\n- id: plan_011\n  claim: 2\n  description: Depth extension to 5 generations + EDD saturation analysis\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  registry_id: depth_extension_binary_pairwise_002\n  notes: Pythia-1.4B nucleus EDD=4 (binary d3v4=0.784>0.75, d4v5=0.683<0.75)。6-class\n    pairwise AUC 因决策边界稀释不可用，必须用 binary pairwise classifier。\n  status: DONE\n  conclusion: success\n  metrics:\n    d1v2_auc: 0.925\n    d1v2_ci95:\n    - 0.9138\n    - 0.9354\n    d2v3_auc: 0.8225\n    d2v3_ci95:\n    - 0.8052\n    - 0.8402\n    d3v4_auc: 0.7837\n    d3v4_ci95:\n    - 0.7648\n    - 0.8024\n    d4v5_auc: 0.6832\n    d4v5_ci95:\n    - 0.6611\n    - 0.7045\n    edd_determination: '4'\n- id: plan_011b\n  claim: 2\n  description: GPT-2 XL depth extension d4/d5 + EDD cross-model verification\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - plan_003\n  - plan_011\n  registry_id: depth_extension_gpt2xl_d4d5_001\n  notes: GPT-2 XL 是 3×3 矩阵信号最强模型 (85.4%)。验证 EDD 跨模型一致性，直接增强 Claim 2。已 RUNNING on cuda:0。\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.966\n      d2v3_auc: 0.919\n      d3v4_auc: 0.75\n      d4v5_auc: 0.681\n    six_class_rf_accuracy: 0.679\n    edd_at_075: 4\n    edd_note: d3v4=0.750>=0.75 PASS, d4v5=0.681<0.75 FAIL → EDD=4\n- id: plan_011c\n  claim: 2\n  description: OLMo-1B depth extension d4/d5 + EDD cross-model verification\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - plan_002\n  - plan_011\n  notes: 第 3 个模型 EDD 验证。代码已就绪 (run_depth_extension_olmo.sh)，含 binary pairwise eval。Reviewer\n    PASS。排 granularity ablation 之后上 cuda:1。\n  registry_id: depth_extension_olmo_d4d5_002\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.968\n      d2v3_auc: 0.843\n      d3v4_auc: 0.765\n      d4v5_auc: 0.684\n    six_class_rf_accuracy: 0.667\n    edd_at_075: 4\n    edd_note: d3v4=0.765>=0.75 PASS, d4v5=0.684<0.75 FAIL → EDD=4\n- id: plan_012\n  claim: 1\n  description: 'Granularity ablation (RF): binary / 3-class / 4-class / 6-class'\n  registry_id: granularity_ablation_rf_001\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: 'Plan A: 用 RF 做，不依赖 DCOL。与 plan_011 depth extension 联动（6-class 需要 5+ depths\n    数据）。'\n  status: DONE\n  conclusion: success\n  metrics:\n    summary:\n      binary_acc_mean: 0.995\n      binary_acc_std: 0.004\n      3class_acc_mean: 0.721\n      3class_acc_std: 0.067\n      4class_acc_mean: 0.783\n      4class_acc_std: 0.048\n      6class_acc: 0.629\n      note: '3-class excludes d0 (most separable class), so 3class < 4class is by\n        design. True granularity trend (with d0): binary 99.5% > 4-class 78.3% > 6-class\n        62.9% — monotonic decrease confirmed.'\n    per_cell:\n      pythia_nucleus095:\n        binary:\n          acc: 0.998\n          ci95:\n          - 0.9965\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7117\n          ci95:\n          - 0.6947\n          - 0.7283\n          auc:\n            d1v2: 0.861\n            d2v3: 0.796\n        4class:\n          acc: 0.7812\n          ci95:\n          - 0.7677\n          - 0.7935\n          auc:\n            d0v1: 0.998\n            d1v2: 0.868\n            d2v3: 0.804\n        6class:\n          acc: 0.6292\n          ci95:\n          - 0.6175\n          - 0.6412\n          auc:\n            d0v1: 0.997\n            d1v2: 0.83\n            d2v3: 0.689\n            d3v4: 0.692\n            d4v5: 0.691\n      pythia_temp09:\n        binary:\n          acc: 0.997\n          ci95:\n          - 0.9952\n          - 0.9985\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7063\n          ci95:\n          - 0.6907\n          - 0.723\n          auc:\n            d1v2: 0.838\n            d2v3: 0.806\n        4class:\n          acc: 0.7605\n          ci95:\n          - 0.7475\n          - 0.7738\n          auc:\n            d0v1: 0.997\n            d1v2: 0.835\n            d2v3: 0.796\n      pythia_topk50:\n        binary:\n          acc: 0.9945\n          ci95:\n          - 0.992\n          - 0.9965\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.5883\n          ci95:\n          - 0.5717\n          - 0.6073\n          auc:\n            d1v2: 0.749\n            d2v3: 0.705\n        4class:\n          acc: 0.6943\n          ci95:\n          - 0.6805\n          - 0.708\n          auc:\n            d0v1: 0.994\n            d1v2: 0.761\n            d2v3: 0.695\n      gpt2xl_nucleus095:\n        binary:\n          acc: 0.9912\n          ci95:\n          - 0.9882\n          - 0.9938\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.79\n          ci95:\n          - 0.775\n          - 0.8047\n          auc:\n            d1v2: 0.913\n            d2v3: 0.891\n        4class:\n          acc: 0.8393\n          ci95:\n          - 0.8283\n          - 0.8502\n          auc:\n            d0v1: 0.995\n            d1v2: 0.916\n            d2v3: 0.885\n      gpt2xl_temp09:\n        binary:\n          acc: 0.9978\n          ci95:\n          - 0.9962\n          - 0.999\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.826\n          ci95:\n          - 0.8117\n          - 0.8397\n          auc:\n            d1v2: 0.944\n            d2v3: 0.887\n        4class:\n          acc: 0.8552\n          ci95:\n          - 0.844\n          - 0.866\n          auc:\n            d0v1: 0.997\n            d1v2: 0.939\n            d2v3: 0.886\n      gpt2xl_topk50:\n        binary:\n          acc: 0.9952\n          ci95:\n          - 0.993\n          - 0.9972\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.695\n          ci95:\n          - 0.6777\n          - 0.7113\n          auc:\n            d1v2: 0.844\n            d2v3: 0.766\n        4class:\n          acc: 0.757\n          ci95:\n          - 0.743\n          - 0.7702\n          auc:\n            d0v1: 0.993\n            d1v2: 0.824\n            d2v3: 0.762\n      olmo_nucleus095:\n        binary:\n          acc: 0.9868\n          ci95:\n          - 0.9832\n          - 0.99\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.7503\n          ci95:\n          - 0.7353\n          - 0.7657\n          auc:\n            d1v2: 0.873\n            d2v3: 0.831\n        4class:\n          acc: 0.7897\n          ci95:\n          - 0.7772\n          - 0.8027\n          auc:\n            d0v1: 0.985\n            d1v2: 0.87\n            d2v3: 0.816\n      olmo_temp09:\n        binary:\n          acc: 0.9982\n          ci95:\n          - 0.997\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7633\n          ci95:\n          - 0.7477\n          - 0.7797\n          auc:\n            d1v2: 0.894\n            d2v3: 0.838\n        4class:\n          acc: 0.8263\n          ci95:\n          - 0.8147\n          - 0.8385\n          auc:\n            d0v1: 0.996\n            d1v2: 0.903\n            d2v3: 0.828\n      olmo_topk50:\n        binary:\n          acc: 0.996\n          ci95:\n          - 0.994\n          - 0.9978\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.661\n          ci95:\n          - 0.644\n          - 0.6773\n          auc:\n            d1v2: 0.812\n            d2v3: 0.739\n        4class:\n          acc: 0.7435\n          ci95:\n          - 0.73\n          - 0.758\n          auc:\n            d0v1: 0.995\n            d1v2: 0.831\n            d2v3: 0.738\n    boundary_dilution:\n      d2v3_auc_by_granularity_pythia_nuc:\n        3class: 0.796\n        4class: 0.804\n        6class: 0.689\n      d1v2_auc_by_granularity_pythia_nuc:\n        3class: 0.861\n        4class: 0.868\n        6class: 0.83\n      note: d2v3 AUC drops 14% from 4-class to 6-class (0.804→0.689), confirming decision\n        boundary dilution at higher granularity\n    decoding_strategy_ranking:\n      4class_acc:\n        temp09: 0.814\n        nucleus095: 0.803\n        topk50: 0.732\n      note: topk50 consistently worst across all 3 models; temp09 slightly outperforms\n        nucleus095\n- id: plan_013\n  claim: 3\n  description: Downstream curation proof-of-concept\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  registry_id: downstream_curation_poc_001\n  notes: 'DONE. RF curation 不优于 unfiltered (negative for original hypothesis)，但显著优于\n    random (p<0.002 all tiers)。Data efficiency story: 44% data ≈ full PPL。Supplement:\n    random_soft_control_001 (success, rf_soft vs random_soft p=5.6e-5)。已写入 Discussion\n    + Appendix。'\n  status: DONE\n  conclusion: negative\n  metrics:\n    unfiltered:\n      ppl_mean: 15.776\n      ppl_std: 0.066\n      n_samples: 10000\n    rf_strict:\n      ppl_mean: 15.81\n      ppl_std: 0.061\n      n_samples: 2496\n      delta: '-0.034'\n      p: 0.607\n      d: -0.528\n    rf_moderate:\n      ppl_mean: 15.756\n      ppl_std: 0.056\n      n_samples: 4940\n      delta: '+0.021'\n      p: 0.492\n      d: 0.334\n    rf_soft:\n      ppl_mean: 15.733\n      ppl_std: 0.038\n      n_samples: 4422\n      delta: '+0.043'\n      p: 0.407\n      d: 0.792\n    oracle_strict:\n      ppl_mean: 15.879\n      ppl_std: 0.128\n      n_samples: 2500\n      delta: '-0.103'\n      p: 0.216\n      d: -1.004\n    oracle_moderate:\n      ppl_mean: 15.809\n      ppl_std: 0.103\n      n_samples: 5000\n      delta: '-0.033'\n      p: 0.485\n      d: -0.384\n    random_strict:\n      ppl_mean: 16.239\n      ppl_std: 0.165\n      n_samples: 2496\n      delta: '-0.463'\n      p: 0.013\n      d: -3.671\n      sig: true\n    random_moderate:\n      ppl_mean: 15.998\n      ppl_std: 0.09\n      n_samples: 5000\n      delta: '-0.222'\n      p: 0.028\n      d: -2.809\n      sig: true\n    cross_condition:\n      rf_strict_vs_random_strict:\n        delta: 0.429\n        t: -7.052\n        p: 0.002\n        sig: true\n      rf_moderate_vs_random_moderate:\n        delta: 0.242\n        t: -3.77\n        p: 0.02\n        sig: true\n      rf_soft_vs_unfiltered:\n        delta: 0.043\n        t: 0.927\n        p: 0.407\n        sig: false\n      random_strict_vs_unfiltered:\n        delta: -0.463\n        t: 4.219\n        p: 0.014\n        sig: true\n- id: plan_014\n  claim: 1\n  description: 13B clean FP16 scale validation (Qwen2.5-14B, nucleus, d0-d3)\n  priority: P0\n  gpu_budget_hours: 18\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: 替代原 7B QLoRA（结果矛盾）。Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。完整\n    d0-d3 nucleus 递归链 + 19 特征提取 + RF/LR 分类。验证 depth signal 在主流模型规模上是否持续。cuda:0。\n  registry_id: qwen25_14b_scale_002\n  status: RUNNING\n  conclusion: null\n- id: plan_015\n  claim: 2\n  description: 'Wild-data calibration: C4/FineWeb/RedPajama subsets → trained RF depth\n    classification'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  notes: D038 reactivated. 从 C4/FineWeb/RedPajama 抽取子集，用已训练 reference model 提取 19\n    特征，用 3×3 训练好的 RF 分类器做 depth 预测 + 分布分析。验证 depth signal 在野生数据中是否存在。需要 GPU 跑 reference\n    model 推理。\n  status: planned\n- id: plan_016\n  claim: 1\n  description: Prompted generation ecological validity (GPT-2 XL, topic-seeded d0-d3)\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_003\n  notes: 验证 depth signal 是否为 BOS-seeded 无条件生成的 artifact。用 topic prompt 前缀（\"The following\n    article discusses...\"等）生成 d0，LoRA fine-tune 后生成 d1-d3，提取 19 特征 + RF 分类。选 GPT-2\n    XL 因为它信号最强，如果 prompted 模式下信号消失则说明生成方式是关键因素。cuda:1。\n  registry_id: prompted_gen_gpt2xl_001\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.6952\n    rf_4class_ci:\n    - 0.689\n    - 0.7015\n    bos_baseline_acc: 0.833\n    delta_vs_bos: -0.1378\n    auc_d0v1: 0.9162\n    auc_d0v2: 0.9934\n    auc_d0v3: 0.9974\n    auc_d1v2: 0.7823\n    auc_d1v3: 0.9553\n    auc_d2v3: 0.7444\n    top5_features:\n    - - p90_ppl\n      - 0.1887\n    - - p75_ppl\n      - 0.1335\n    - - mean_surprisal\n      - 0.0916\n    - - var_surprisal\n      - 0.0849\n    - - p50_ppl\n      - 0.0612\n    n_samples: 20000\n    fold_accuracies:\n    - 0.6885\n    - 0.707\n    - 0.6987\n    - 0.6943\n    - 0.6877\n- id: plan_017\n  claim: 3\n  description: Cross-strategy two-stage pipeline (strategy classifier + conditioned\n    depth)\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  - plan_007\n  notes: 两阶段方案解决 59.1% 跨策略准确率问题。(a) 策略识别分类器：19 特征 → 3-class (nucleus/temp/topk)，预计\n    >90%。(b) 策略条件深度分类器：识别策略后用策略专属 RF 估深度。将论文弱点转化为实际贡献。主要是 CPU 任务，不占 GPU。\n  registry_id: cross_strategy_pipeline_001\n  status: DONE\n  conclusion: success\n  metrics:\n    strategy_clf_rf_acc: 0.5779\n    strategy_clf_lr_acc: 0.5291\n    pipeline_depth_acc: 0.7053\n    oracle_depth_acc: 0.7831\n    loo_ref_acc: 0.5908\n    improvement_vs_loo: 0.1145\n    gap_pipeline_vs_oracle: 0.0778\n    pipeline_depth_acc_pythia: 0.6925\n    pipeline_depth_acc_olmo: 0.6937\n    pipeline_depth_acc_gpt2xl: 0.7297\n- id: plan_018\n  claim: 1\n  description: 'Existing detector ordinal baseline: Binoculars + Fast-DetectGPT scores\n    calibrated for ordinal depth estimation'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  - plan_002\n  - plan_003\n  notes: 'Dream 三档一致 #1 缺口。将 Binoculars/Fast-DetectGPT 连续分数校准为 ordinal bin，在 3×3 已有数据上评估。即使\n    negative 也加强论文。需要少量 GPU 跑推理。D036。'\n  status: planned\n- id: plan_019\n  claim: 1\n  description: 'MLP on 19 features: neural classifier baseline on same feature set'\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_001a\n  registry_id: mlp_19feat_001\n  notes: DONE. MLP delta ≤3pp vs RF，确认特征是瓶颈而非分类器选择。CPU only。\n  status: DONE\n  conclusion: success\n  metrics:\n    mlp_128_128_acc: 0.7866\n    mlp_64_128_64_acc: 0.7895\n    mlp_poly_top5_acc: 0.7906\n    best_delta_vs_rf: 0.0086\n    d0v1_auc: 0.997\n    d1v2_auc: 0.878\n    d2v3_auc: 0.821\n- id: plan_020\n  claim: 1\n  description: 'Table 1 bootstrap CIs: 5-fold CV bootstrap confidence intervals for\n    all 9 cells'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  - plan_002\n  - plan_003\n  notes: Dream 三档均要求。从已有 5-fold CV 结果计算 bootstrap CI。纯 CPU 分析任务。\n  status: planned\n- id: plan_021\n  claim: 1\n  description: 'Instruction-tuned model validation: Qwen2.5-1.5B-Instruct recursive\n    chain (nucleus, d0-d3) to test depth signal on instruct models'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001a\n  notes: D037 Manager 自查发现最大缺口。2024-2025 检测论文标配 instruct model。Qwen2.5-1.5B-Instruct\n    nucleus d0-d3，19 特征提取 + RF/LR 分类。结果进 Appendix。cuda:1 在 plan_016 完成后跑。\n  registry_id: qwen25-1p5b-instruct-001\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.4742\n    rf_4class_ci:\n    - 0.467\n    - 0.4811\n    lr_4class_acc: 0.4256\n    rf_3class_acc: 0.4987\n    pairwise_auc_rf:\n      d0v1: 0.653\n      d0v2: 0.819\n      d0v3: 0.902\n      d1v2: 0.62\n      d1v3: 0.807\n      d2v3: 0.664\n    pairwise_auc_lr:\n      d0v1: 0.619\n      d0v2: 0.773\n      d0v3: 0.838\n      d1v2: 0.594\n      d1v3: 0.734\n      d2v3: 0.621\n    top_features:\n    - surprisal_range\n    - surprisal_position_corr\n    - prob_std\n    - surprisal_first_half_minus_second\n    - surprisal_std\n    n_samples: 19992\n- id: plan_022\n  claim: 1\n  description: 'Text length sensitivity analysis: evaluate depth estimation accuracy\n    at 50/100/200/500 token truncation lengths'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  - plan_002\n  - plan_003\n  registry_id: text_length_sensitivity_001\n  notes: DONE. 准确率随截断长度优雅降级，关键特征(surprisal moments, entropy)在100-200 tokens内收敛，方法对短文本实用。\n  status: DONE\n  conclusion: success\n- id: plan_023\n  claim: 2\n  description: 'Theoretical analysis: connect depth signal to model collapse theory,\n    derive EDD upper bound'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  - plan_006\n  notes: 'D038. CPU/写作任务。(1) 为什么 p90_ppl 和 var_surprisal 能区分 depth: 连接到 Shumailov\n    et al. 2024 model collapse 中 tail distribution 消失现象。(2) EDD 上界推导: 基于递归生成的 fixed-point\n    attractor 理论。(3) 与实验 EDD=4 结果对照验证。产出: paper Theory section 草稿。'\n  status: planned\n- id: plan_024\n  claim: 3\n  description: 'Downstream benchmark impact: depth-filtered training data → HellaSwag/ARC\n    evaluation'\n  priority: P0\n  gpu_budget_hours: 12\n  deps:\n  - plan_001a\n  - plan_013\n  notes: D038. 扩展 plan_013 data efficiency story。用 depth estimator 过滤训练数据(移除 high-depth\n    text)，在 HellaSwag/ARC/PIQA 上评估下游 LM 质量。3 个过滤阈值 × 3 个 benchmark。需要 GPU 做 LM training\n    + eval。\n  registry_id: downstream_benchmark_001\n  status: DONE\n  conclusion: failed\n- id: plan_025\n  claim: 1\n  description: 'Learned depth estimator: metric learning on 19-feature space for zero-shot\n    cross-model generalization'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_001b\n  - plan_002\n  - plan_003\n  - plan_005\n  notes: 'D038. 从 RF 特征重要性出发，训练 lightweight MLP/prototypical network 做 ordinal depth\n    estimation，目标: 在 leave-one-model-out 上超过 RF baseline (66.4%)。如果成功→方法贡献升级；失败→作为\n    negative analysis 支持\"特征是瓶颈\"结论。'\n  registry_id: learned_estimator_001\n  status: DONE\n  conclusion: negative\n- id: plan_026\n  claim: 1\n  description: 'API model recursive chains: GPT-4o-mini fine-tuning API + prompted\n    chain for d0-d3 depth estimation'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001a\n  notes: 'D038. 两种方式验证 API 模型: (a) GPT-4o-mini fine-tuning API 递归链 (需 OpenAI key)。(b)\n    Prompted recursive chain (rewrite/continue, 无需 fine-tune, 可用任意 API)。验证 depth signal\n    在商用模型中是否存在。'\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_004\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_base_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_base_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_pythia_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_qwen_base_004\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_pythia_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_4class_acc: 0.782\n    full_4class_acc_ci:\n    - 0.769\n    - 0.794\n    full_4class_acc_stratified: 0.781\n    full_mae: 0.2367\n    full_auc_0v1: 0.9975\n    full_auc_1v2: 0.8607\n    full_auc_2v3: 0.8005\n    filtered_4class_acc: 0.816\n    filtered_4class_acc_ci:\n    - 0.803\n    - 0.829\n    filtered_mae: 0.1995\n    filtered_auc_0v1: 0.9977\n    filtered_auc_1v2: 0.8782\n    filtered_auc_2v3: 0.8323\n    filtered_sample_count: 16993\n    three_class_acc: 0.708\n    three_class_acc_ci:\n    - 0.692\n    - 0.725\n    three_class_mae: 0.3203\n    three_class_auc_1v2: 0.854\n    three_class_auc_1v3: 0.9569\n    three_class_auc_2v3: 0.7931\n    three_class_recall_d1: 0.79\n    three_class_recall_d2: 0.607\n    three_class_recall_d3: 0.728\n    three_class_precision_d1: 0.852\n    three_class_precision_d2: 0.605\n    three_class_precision_d3: 0.68\n    three_class_f1_d1: 0.82\n    three_class_f1_d2: 0.606\n    three_class_f1_d3: 0.703\n    three_class_lr_acc: 0.671\n    filtered_three_class_acc: 0.747\n    filtered_three_class_acc_ci:\n    - 0.727\n    - 0.764\n    filtered_three_class_mae: 0.2759\n    filtered_three_class_recall_d1: 0.862\n    filtered_three_class_recall_d2: 0.635\n    filtered_three_class_recall_d3: 0.735\n    filtered_three_class_precision_d1: 0.867\n    filtered_three_class_precision_d2: 0.659\n    filtered_three_class_precision_d3: 0.704\n    filtered_three_class_f1_d1: 0.864\n    filtered_three_class_f1_d2: 0.647\n    filtered_three_class_f1_d3: 0.719\n    filtered_three_class_auc_1v2: 0.8926\n    filtered_three_class_auc_1v3: 0.9769\n    filtered_three_class_auc_2v3: 0.8272\n    filtered_three_class_sample_count: 12012\n    best_model: RandomForest\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    truncation_length: 498\n    feature_dim: 19\n- exp_id: cross_model_olmo_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    status: PIPELINE_CRASHED\n    completed_steps:\n    - depth0_lora_finetune\n    failed_at: shell_script_line_52_unmatched_quote\n    depth0_final_loss: 2.2686\n    depth0_train_runtime_s: 283.2\n    depth0_train_steps: 939\n    depth0_trainable_params: 3145728\n    depth0_total_params: 1179910144\n    classification_results: null\n    note: Script crashed after depth-0 finetune. No depth-1/2/3 generation, no feature\n      extraction, no classification performed.\n- exp_id: cross_model_gpt2xl_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.833\n    four_class_acc_ci:\n    - 0.823\n    - 0.845\n    four_class_acc_lr: 0.813\n    auc_0v1: 0.9941\n    auc_0v2: 0.9965\n    auc_0v3: 0.9988\n    auc_1v2: 0.9131\n    auc_1v3: 0.9857\n    auc_2v3: 0.8829\n    three_class_acc: 0.793\n    three_class_acc_ci:\n    - 0.778\n    - 0.806\n    three_class_auc_1v2: 0.9109\n    three_class_auc_1v3: 0.989\n    three_class_auc_2v3: 0.8885\n    finetune_losses:\n      depth_0: 2.55\n      depth_1: 1.715\n      depth_2: 1.342\n    top_features:\n    - p90_ppl (0.208)\n    - var_surprisal (0.208)\n    - p75_ppl (0.103)\n    - mean_surprisal (0.082)\n    - mean_ppl (0.065)\n    code_contamination:\n      d0: 0.005\n      d1: 0.005\n      d2: 0.013\n      d3: 0.007\n- exp_id: pythia_temp09_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.7625\n      rf_accuracy_ci:\n      - 0.749\n      - 0.7753\n      lr_accuracy: 0.7405\n      lr_accuracy_ci:\n      - 0.7265\n      - 0.7545\n      pairwise_auc:\n        0v1: 0.9968\n        0v2: 0.9993\n        0v3: 0.9991\n        1v2: 0.8327\n        1v3: 0.959\n        2v3: 0.7928\n      top_features:\n      - var_surprisal (0.1776)\n      - p90_ppl (0.1501)\n      - mean_ppl (0.1140)\n      - mean_surprisal (0.0889)\n      - p75_ppl (0.0687)\n      feature_dim: 19\n      truncation_length: 498\n    three_class_full:\n      accuracy: 0.6983\n      accuracy_ci:\n      - 0.682\n      - 0.715\n      mae: 0.3357\n      recall:\n        d1: 0.802\n        d2: 0.554\n        d3: 0.739\n      precision:\n        d1: 0.792\n        d2: 0.608\n        d3: 0.686\n      f1:\n        d1: 0.797\n        d2: 0.58\n        d3: 0.712\n      pairwise_auc:\n        d1v2: 0.8354\n        d1v3: 0.9631\n        d2v3: 0.8043\n    three_class_filtered:\n      accuracy: 0.7252\n      accuracy_ci:\n      - 0.7064\n      - 0.7427\n      mae: 0.2953\n      recall:\n        d1: 0.842\n        d2: 0.596\n        d3: 0.735\n      precision:\n        d1: 0.821\n        d2: 0.628\n        d3: 0.715\n      f1:\n        d1: 0.831\n        d2: 0.611\n        d3: 0.725\n      pairwise_auc:\n        d1v2: 0.8656\n        d1v3: 0.9772\n        d2v3: 0.8295\n      n_samples: 11445\n      n_removed: 3555\n    finetune_losses:\n      depth_0: 2.222\n      depth_1: 1.37\n      depth_2: 1.006\n    code_contamination:\n      d0: 0.004\n      d1: 0.077\n      d2: 0.116\n      d3: 0.136\n- exp_id: pythia_topk50_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.696\n    rf_4class_acc_ci:\n    - 0.6825\n    - 0.7107\n    lr_4class_acc: 0.682\n    rf_3class_acc: 0.592\n    rf_3class_acc_ci:\n    - 0.575\n    - 0.6107\n    rf_3class_filtered_acc: 0.6133\n    rf_3class_filtered_acc_ci:\n    - 0.593\n    - 0.6312\n    pairwise_auc_rf:\n      d0v1: 0.9927\n      d0v2: 0.9983\n      d0v3: 0.9978\n      d1v2: 0.7518\n      d1v3: 0.9176\n      d2v3: 0.6918\n    pairwise_auc_3class_filtered_rf:\n      d1v2: 0.768\n      d1v3: 0.9323\n      d2v3: 0.7013\n    feature_importance_top5:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - mean_surprisal\n    - p75_ppl\n    finetune_loss:\n      depth_0: 2.2406\n      depth_1: 1.6704\n      depth_2: 1.4374\n    code_contamination_narrow:\n      depth_0: 0.004\n      depth_1: 0.077\n      depth_2: 0.123\n      depth_3: 0.131\n- exp_id: cross_model_olmo_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc_rf: 0.788\n    four_class_acc_ci:\n    - 0.776\n    - 0.8\n    four_class_acc_lr: 0.751\n    auc_0v1: 0.9834\n    auc_0v2: 0.9949\n    auc_0v3: 0.9989\n    auc_1v2: 0.8673\n    auc_1v3: 0.9806\n    auc_2v3: 0.8124\n    three_class_acc: 0.744\n    three_class_acc_ci:\n    - 0.728\n    - 0.76\n    three_class_mae: 0.27\n    three_class_auc_1v2: 0.8664\n    three_class_auc_1v3: 0.9852\n    three_class_auc_2v3: 0.8274\n    three_class_recall:\n      d1: 0.864\n      d2: 0.607\n      d3: 0.761\n    three_class_precision:\n      d1: 0.863\n      d2: 0.646\n      d3: 0.718\n    four_class_per_class:\n      d0:\n        precision: 0.95\n        recall: 0.99\n        f1: 0.97\n      d1:\n        precision: 0.85\n        recall: 0.82\n        f1: 0.83\n      d2:\n        precision: 0.63\n        recall: 0.59\n        f1: 0.61\n      d3:\n        precision: 0.71\n        recall: 0.76\n        f1: 0.73\n    finetune_losses:\n      depth_0: 2.269\n      depth_1: 1.65\n      depth_2: 1.226\n    top_features:\n    - p90_ppl (0.18)\n    - var_surprisal (0.16)\n    - p75_ppl (0.11)\n    - mean_surprisal (0.08)\n    - type_token_ratio (0.06)\n    code_contamination:\n      d0: 0.005\n      d1: 0.027\n      d2: 0.007\n      d3: 0.008\n    feature_dim: 19\n    truncation_length: 507\n- exp_id: gpt2xl_temp09_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data:\n      samples_per_depth: 5000\n      total_samples: 20000\n      depths: 4\n    finetune_losses:\n      depth_1: 2.5498\n      depth_2: 1.6972\n      depth_3: 1.2922\n    code_contamination:\n      depth_0:\n        broad: 25\n        narrow: 20\n        broad_pct: 0.5\n        narrow_pct: 0.4\n      depth_1:\n        broad: 25\n        narrow: 40\n        broad_pct: 0.5\n        narrow_pct: 0.8\n      depth_2:\n        broad: 34\n        narrow: 80\n        broad_pct: 0.7\n        narrow_pct: 1.6\n      depth_3:\n        broad: 25\n        narrow: 76\n        broad_pct: 0.5\n        narrow_pct: 1.5\n    four_class:\n      rf_accuracy: 0.8542\n      rf_accuracy_ci:\n      - 0.843\n      - 0.8653\n      lr_accuracy: 0.8155\n      lr_accuracy_ci:\n      - 0.8025\n      - 0.8273\n      rf_auc:\n        d0v1: 0.9963\n        d0v2: 0.9992\n        d0v3: 1\n        d1v2: 0.9367\n        d1v3: 0.9947\n        d2v3: 0.8815\n      lr_auc:\n        d0v1: 0.984\n        d0v2: 0.9998\n        d0v3: 1\n        d1v2: 0.8903\n        d1v3: 0.9824\n        d2v3: 0.8183\n      top_features:\n      - p90_ppl\n      - mean_surprisal\n      - p75_ppl\n      - var_surprisal\n    three_class:\n      rf_accuracy: 0.82\n      rf_accuracy_ci:\n      - 0.806\n      - 0.834\n      lr_accuracy: 0.7773\n      lr_accuracy_ci:\n      - 0.7627\n      - 0.792\n      rf_auc:\n        d1v2: 0.9418\n        d1v3: 0.9967\n        d2v3: 0.8849\n    three_class_filtered:\n      rf_accuracy: 0.815\n      rf_accuracy_ci:\n      - 0.7999\n      - 0.8298\n      lr_accuracy: 0.7869\n      lr_accuracy_ci:\n      - 0.7711\n      - 0.8016\n      rf_auc:\n        d1v2: 0.937\n        d1v3: 0.9944\n        d2v3: 0.8891\n- exp_id: dcol_deberta_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cross_model_olmo_temp09_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: olmo_temp09_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      rf_accuracy: 0.8203\n      d1v2_auc: 0.901\n    three_class_filtered:\n      rf_accuracy: 0.7757\n    finetune_losses:\n      depth_0: 2.27\n      depth_1: 1.63\n      depth_2: 1.18\n    code_contamination_narrow_max: 0.007\n    top_features:\n    - p90_ppl (0.199)\n    - var_surprisal (0.174)\n    - p75_ppl (0.126)\n- exp_id: olmo_topk50_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      lr_accuracy: 0.757\n      lr_accuracy_ci:\n      - 0.7425\n      - 0.7702\n      rf_accuracy: 0.742\n      rf_accuracy_ci:\n      - 0.7282\n      - 0.7555\n    pairwise_auc:\n      lr:\n        d0v1: 0.9969\n        d0v2: 0.9995\n        d0v3: 0.9998\n        d1v2: 0.8293\n        d1v3: 0.9592\n        d2v3: 0.7497\n      rf:\n        d0v1: 0.993\n        d0v2: 0.9983\n        d0v3: 0.9991\n        d1v2: 0.8305\n        d1v3: 0.9591\n        d2v3: 0.7357\n    three_class:\n      lr_accuracy: 0.6567\n      lr_accuracy_ci:\n      - 0.6403\n      - 0.6733\n      rf_accuracy: 0.6517\n      rf_accuracy_ci:\n      - 0.635\n      - 0.6687\n    three_class_filtered:\n      lr_accuracy: 0.6703\n      lr_accuracy_ci:\n      - 0.653\n      - 0.6882\n      rf_accuracy: 0.6699\n      rf_accuracy_ci:\n      - 0.6537\n      - 0.6875\n    three_class_filtered_auc:\n      lr:\n        d1v2: 0.7903\n        d1v3: 0.97\n        d2v3: 0.7501\n      rf:\n        d1v2: 0.8071\n        d1v3: 0.9645\n        d2v3: 0.7364\n    feature_importance_top5:\n    - p90_ppl\n    - var_surprisal\n    - p75_ppl\n    - mean_surprisal\n    - p25_ppl\n    finetune_loss:\n      depth_1: 1.946\n      depth_2: 1.726\n    code_contamination:\n      narrow_pct:\n        depth_0: 0.4\n        depth_1: 0.8\n        depth_2: 0.3\n        depth_3: 0.4\n      broad_pct:\n        depth_0: 0.5\n        depth_1: 2.5\n        depth_2: 0.8\n        depth_3: 0.7\n- exp_id: gpt2xl_topk50_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class:\n      accuracy: 0.766\n      depth1_vs_depth2_auc: 0.8259\n      pass: true\n    three_class:\n      accuracy: 0.695\n      depth1_vs_depth2_auc: 0.8392\n      pass: true\n    three_class_filtered:\n      accuracy: 0.684\n      depth1_vs_depth2_auc: 0.8314\n      pass: true\n- exp_id: dcol_deberta_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: dcol_deberta_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: atlas_v1_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    monotonicity_rho_range:\n    - -0.89\n    - -0.82\n    edd: 3\n    edd_saturated: false\n    cross_model_jaccard: 0.667\n    cross_model_rank_corr: 0.85\n    artifacts:\n    - monotonicity_scores.json\n    - cross_model_comparison.json\n    - edd_analysis.json\n    - feature_trajectory.json\n- exp_id: olmo_temp09_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: baseline_battery_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_reg_single_4class_acc: 0.251\n    ppl_reg_multi_4class_acc: 0.622\n    ce_mlp_4class_acc: 0.749\n    coral_4class_acc: 0.7807\n    coral_3class_acc: 0.7089\n    coral_mae: 0.2273\n    coral_d1v2_auc: 0.8179\n    diveye_4class_acc: 0.7817\n    diveye_3class_acc: 0.7098\n    diveye_d1v2_auc: 0.8654\n    rf_4class_acc: 0.781\n    lr_4class_acc: 0.75\n    note: CE-MLP 74.9% may be undertrained (5 epochs); CORAL updated to 100 epochs.\n      All results from Pythia nucleus baseline features.\n- exp_id: dcol_deberta_004\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: dcol_deberta_005\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: batch_feature_extraction_5cells\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: depth_extension_pythia_d4d5_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    six_class_rf_accuracy: 0.6232\n    six_class_rf_accuracy_ci:\n    - 0.6113\n    - 0.636\n    six_class_lr_accuracy: 0.5862\n    pairwise_auc_rf:\n      d0v1: 0.9962\n      d1v2: 0.8231\n      d2v3: 0.6878\n      d3v4: 0.6809\n      d4v5: 0.6948\n    pairwise_auc_lr:\n      d0v1: 0.9908\n      d1v2: 0.6901\n      d2v3: 0.6174\n      d3v4: 0.6828\n      d4v5: 0.6554\n    cumulative_auc_rf:\n      d0v5: 0.9987\n      d1v5: 0.9874\n      d2v5: 0.949\n      d3v5: 0.8632\n    edd_at_075: 2\n    feature_importance_top5:\n    - p90_ppl (0.1376)\n    - var_surprisal (0.1344)\n    - mean_ppl (0.0796)\n    - mean_surprisal (0.0789)\n    - p75_ppl (0.0680)\n    finetune_losses:\n      depth_3: 0.7634\n      depth_4: 0.5828\n    WARNING: 6-class pairwise AUC 不可与 4-class 直比，决策边界稀释导致系统性偏低。需 binary pairwise classifier\n      重新评估。\n- exp_id: cross_model_loo_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    mean_4class_acc: 0.664\n    holdout_pythia:\n      acc: 0.6242\n      ci:\n      - 0.6206\n      - 0.6282\n      d1v2_auc: 0.5617\n      d2v3_auc: 0.6534\n    holdout_olmo:\n      acc: 0.6921\n      ci:\n      - 0.6886\n      - 0.6959\n      d1v2_auc: 0.7687\n      d2v3_auc: 0.6862\n    holdout_gpt2xl:\n      acc: 0.6756\n      ci:\n      - 0.6719\n      - 0.6792\n      d1v2_auc: 0.8157\n      d2v3_auc: 0.6639\n    per_class_recall:\n      holdout_pythia:\n        d0: 1\n        d1: 0.493\n        d2: 0.268\n        d3: 0.736\n      holdout_olmo:\n        d0: 0.993\n        d1: 0.755\n        d2: 0.433\n        d3: 0.588\n      holdout_gpt2xl:\n        d0: 0.985\n        d1: 0.747\n        d2: 0.526\n        d3: 0.445\n    gate_passed: true\n    gate_threshold: 0.45\n- exp_id: cross_model_loo_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_acc: 0.664\n    mean_3class_acc: 0.5544\n    holdout_pythia:\n      acc: 0.6242\n      ci95:\n      - 0.6205\n      - 0.6282\n      3class_acc: 0.499\n      3class_ci95:\n      - 0.4944\n      - 0.5034\n      d1v2_auc: 0.5617\n      d1v3_auc: 0.8547\n      d2v3_auc: 0.6534\n      d0v1_auc: 0.9921\n      d0v2_auc: 0.9999\n      d0v3_auc: 0.9998\n      per_class:\n        d0:\n          P: 0.9889\n          R: 1\n          F1: 0.9944\n        d1:\n          P: 0.6655\n          R: 0.493\n          F1: 0.5664\n        d2:\n          P: 0.3699\n          R: 0.2677\n          F1: 0.3106\n        d3:\n          P: 0.483\n          R: 0.7363\n          F1: 0.5834\n    holdout_olmo:\n      acc: 0.6921\n      ci95:\n      - 0.6884\n      - 0.696\n      3class_acc: 0.592\n      3class_ci95:\n      - 0.5873\n      - 0.5965\n      d1v2_auc: 0.7687\n      d1v3_auc: 0.9277\n      d2v3_auc: 0.6862\n      per_class:\n        d0:\n          P: 0.9783\n          R: 0.9925\n          F1: 0.9854\n        d1:\n          P: 0.7111\n          R: 0.7549\n          F1: 0.7324\n        d2:\n          P: 0.4616\n          R: 0.4327\n          F1: 0.4467\n        d3:\n          P: 0.5964\n          R: 0.5883\n          F1: 0.5923\n    holdout_gpt2xl:\n      acc: 0.6756\n      ci95:\n      - 0.6717\n      - 0.6795\n      3class_acc: 0.5723\n      3class_ci95:\n      - 0.5679\n      - 0.5767\n      d1v2_auc: 0.8157\n      d1v3_auc: 0.9149\n      d2v3_auc: 0.6639\n      d0v1_auc: 0.9927\n      d0v2_auc: 0.9919\n      d0v3_auc: 0.9876\n      per_class:\n        d0:\n          P: 0.9484\n          R: 0.9853\n          F1: 0.9665\n        d1:\n          P: 0.7093\n          R: 0.7465\n          F1: 0.7274\n        d2:\n          P: 0.4521\n          R: 0.5255\n          F1: 0.486\n        d3:\n          P: 0.5963\n          R: 0.445\n          F1: 0.5097\n    mean_per_class_recall:\n      d0: 0.9926\n      d1: 0.6648\n      d2: 0.4086\n      d3: 0.5899\n    lowest_recall_class: d2\n    lowest_recall_value: 0.4086\n    detailed_artifact: cross_model_loo_detailed.json\n- exp_id: atlas_v2_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    p90_ppl_in_top2: 9/9\n    var_surprisal_in_top2: 7/9\n    edd_equals_3_at_T075: 7/9\n    edd_distribution_T075:\n      '2': 2\n      '3': 7\n    cross_model_rank_corr_range: '[0.619, 0.954]'\n    cross_model_rank_corr_mean: 0.868\n    cv5_accuracy_range: '[0.688, 0.859]'\n    cells_covered: 9/9\n- exp_id: cross_strategy_loo_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_4class_acc: 0.5908\n    pythia_holdout_nucleus:\n      acc: 0.6935\n      d1v2_auc: 0.6903\n      d2v3_auc: 0.7626\n    pythia_holdout_temp09:\n      acc: 0.6281\n      d1v2_auc: 0.576\n      d2v3_auc: 0.724\n    pythia_holdout_topk50:\n      acc: 0.5151\n      d1v2_auc: 0.6393\n      d2v3_auc: 0.5801\n    gpt2xl_holdout_nucleus:\n      acc: 0.5993\n      d1v2_auc: 0.7826\n      d2v3_auc: 0.4985\n    gpt2xl_holdout_temp09:\n      acc: 0.5609\n      d1v2_auc: 0.1288\n      d2v3_auc: 0.6366\n    gpt2xl_holdout_topk50:\n      acc: 0.5364\n      d1v2_auc: 0.8308\n      d2v3_auc: 0.7222\n    olmo_holdout_nucleus:\n      acc: 0.6538\n      d1v2_auc: 0.7931\n      d2v3_auc: 0.6076\n    olmo_holdout_temp09:\n      acc: 0.5816\n      d1v2_auc: 0.2529\n      d2v3_auc: 0.7015\n    olmo_holdout_topk50:\n      acc: 0.5488\n      d1v2_auc: 0.8549\n      d2v3_auc: 0.7107\n    finding_temp09_d1v2_inversion: 'd1v2 AUC inverts when holding out temp09 (GPT-2\n      XL: 0.13, OLMo: 0.25) — temp09 d1→d2 features differ fundamentally from nucleus/topk50'\n- exp_id: dcol_roberta_v6_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.6448\n    test_mae: 0.4052\n    best_val_acc: 0.6436\n    best_epoch: 1\n    epochs_run: 4\n    early_stopping: true\n    train_acc_final: 0.75\n    rf_baseline: 0.782\n    delta_vs_baseline: -0.137\n    overfitting: severe (train 75% vs val 64.4% at best epoch)\n    stability: resolved (no NaN, no collapse, collapse guard passed at step 500)\n- exp_id: baseline_battery_9cell_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_acc_matrix:\n      pythia_nucleus: 0.782\n      pythia_temp09: 0.772\n      pythia_topk50: 0.688\n      olmo_nucleus: 0.796\n      olmo_temp09: 0.827\n      olmo_topk50: 0.759\n      gpt2xl_nucleus: 0.843\n      gpt2xl_temp09: 0.853\n      gpt2xl_topk50: 0.754\n    methods:\n    - RF\n    - LR\n    - CORAL\n    - DivEye\n    cells: 9\n    finding: RF ≈ CORAL > DivEye > LR, max gap ~4pp. GPT-2 XL temp09 best (85.3%),\n      model effect > strategy effect\n    WARNING: best_acc_matrix stores best-across-ALL-methods accuracy, NOT RF-only.\n      For RF accuracy use each cell's own registry (e.g. olmo_topk50_001.metrics.four_class.rf_accuracy).\n      olmo_topk50 diff=2.2pp, olmo_nucleus diff=0.83pp.\n- exp_id: cross_strategy_loo_zscore_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mean_raw_acc: 0.5908\n    mean_zscore_acc: 0.5915\n    raw:\n      pythia_holdout_nucleus:\n        acc: 0.6935\n        d1v2_auc: 0.6903\n        d2v3_auc: 0.7626\n      pythia_holdout_temp09:\n        acc: 0.6281\n        d1v2_auc: 0.576\n        d2v3_auc: 0.724\n      pythia_holdout_topk50:\n        acc: 0.5151\n        d1v2_auc: 0.6393\n        d2v3_auc: 0.5801\n      gpt2xl_holdout_nucleus:\n        acc: 0.5993\n        d1v2_auc: 0.7826\n        d2v3_auc: 0.4985\n      gpt2xl_holdout_temp09:\n        acc: 0.5609\n        d1v2_auc: 0.1288\n        d2v3_auc: 0.6366\n      gpt2xl_holdout_topk50:\n        acc: 0.5364\n        d1v2_auc: 0.8308\n        d2v3_auc: 0.7222\n      olmo_holdout_nucleus:\n        acc: 0.6538\n        d1v2_auc: 0.7931\n        d2v3_auc: 0.6076\n      olmo_holdout_temp09:\n        acc: 0.5816\n        d1v2_auc: 0.2529\n        d2v3_auc: 0.7015\n      olmo_holdout_topk50:\n        acc: 0.5488\n        d1v2_auc: 0.8549\n        d2v3_auc: 0.7107\n    zscore:\n      pythia_holdout_nucleus:\n        acc: 0.6992\n        d1v2_auc: 0.7043\n        d2v3_auc: 0.7683\n      pythia_holdout_temp09:\n        acc: 0.6368\n        d1v2_auc: 0.5943\n        d2v3_auc: 0.7352\n      pythia_holdout_topk50:\n        acc: 0.5155\n        d1v2_auc: 0.6386\n        d2v3_auc: 0.5804\n      gpt2xl_holdout_nucleus:\n        acc: 0.5959\n        d1v2_auc: 0.788\n        d2v3_auc: 0.4927\n      gpt2xl_holdout_temp09:\n        acc: 0.5632\n        d1v2_auc: 0.1348\n        d2v3_auc: 0.631\n      gpt2xl_holdout_topk50:\n        acc: 0.5356\n        d1v2_auc: 0.8391\n        d2v3_auc: 0.7282\n      olmo_holdout_nucleus:\n        acc: 0.6506\n        d1v2_auc: 0.796\n        d2v3_auc: 0.6078\n      olmo_holdout_temp09:\n        acc: 0.5782\n        d1v2_auc: 0.2497\n        d2v3_auc: 0.6871\n      olmo_holdout_topk50:\n        acc: 0.5484\n        d1v2_auc: 0.8579\n        d2v3_auc: 0.7056\n    temp09_d1v2_delta:\n      pythia: 0.0183\n      gpt2xl: 0.006\n      olmo: -0.0033\n    finding: Z-score does NOT fix temp09 d1v2 inversion in RF — RF is scale-invariant\n      (tree splits unaffected by monotonic transforms). Prior z-score recovery (0.13→0.68)\n      was with LR, not RF.\n- exp_id: depth_extension_binary_pairwise_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: depth_extension_binary_pairwise_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d1v2_auc: 0.925\n    d1v2_ci95:\n    - 0.9138\n    - 0.9354\n    d2v3_auc: 0.8225\n    d2v3_ci95:\n    - 0.8052\n    - 0.8402\n    d3v4_auc: 0.7837\n    d3v4_ci95:\n    - 0.7648\n    - 0.8024\n    d4v5_auc: 0.6832\n    d4v5_ci95:\n    - 0.6611\n    - 0.7045\n    edd_determination: '4'\n- exp_id: depth_extension_gpt2xl_d4d5_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.966\n      d2v3_auc: 0.919\n      d3v4_auc: 0.75\n      d4v5_auc: 0.681\n    six_class_rf_accuracy: 0.679\n    edd_at_075: 4\n    edd_note: d3v4=0.750>=0.75 PASS, d4v5=0.681<0.75 FAIL → EDD=4\n- exp_id: zero_shot_llm_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc: 0.4\n    n_samples: 200\n    sample_distribution:\n      d0: 56\n      d1: 47\n      d2: 49\n      d3: 48\n    model: DeepSeek V3.2\n    method: zero-shot prompting\n    vs_rf_baseline: -0.382\n    vs_chance: 0.15\n    note: 40.0% (80/200) above chance (25%) but far below RF 78.2% (-38.2pp). Zero-shot\n      LLM cannot reliably distinguish recursive depth from raw text alone.\n- exp_id: granularity_ablation_rf_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    summary:\n      binary_acc_mean: 0.995\n      binary_acc_std: 0.004\n      3class_acc_mean: 0.721\n      3class_acc_std: 0.067\n      4class_acc_mean: 0.783\n      4class_acc_std: 0.048\n      6class_acc: 0.629\n      note: '3-class excludes d0 (most separable class), so 3class < 4class is by\n        design. True granularity trend (with d0): binary 99.5% > 4-class 78.3% > 6-class\n        62.9% — monotonic decrease confirmed.'\n    per_cell:\n      pythia_nucleus095:\n        binary:\n          acc: 0.998\n          ci95:\n          - 0.9965\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7117\n          ci95:\n          - 0.6947\n          - 0.7283\n          auc:\n            d1v2: 0.861\n            d2v3: 0.796\n        4class:\n          acc: 0.7812\n          ci95:\n          - 0.7677\n          - 0.7935\n          auc:\n            d0v1: 0.998\n            d1v2: 0.868\n            d2v3: 0.804\n        6class:\n          acc: 0.6292\n          ci95:\n          - 0.6175\n          - 0.6412\n          auc:\n            d0v1: 0.997\n            d1v2: 0.83\n            d2v3: 0.689\n            d3v4: 0.692\n            d4v5: 0.691\n      pythia_temp09:\n        binary:\n          acc: 0.997\n          ci95:\n          - 0.9952\n          - 0.9985\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7063\n          ci95:\n          - 0.6907\n          - 0.723\n          auc:\n            d1v2: 0.838\n            d2v3: 0.806\n        4class:\n          acc: 0.7605\n          ci95:\n          - 0.7475\n          - 0.7738\n          auc:\n            d0v1: 0.997\n            d1v2: 0.835\n            d2v3: 0.796\n      pythia_topk50:\n        binary:\n          acc: 0.9945\n          ci95:\n          - 0.992\n          - 0.9965\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.5883\n          ci95:\n          - 0.5717\n          - 0.6073\n          auc:\n            d1v2: 0.749\n            d2v3: 0.705\n        4class:\n          acc: 0.6943\n          ci95:\n          - 0.6805\n          - 0.708\n          auc:\n            d0v1: 0.994\n            d1v2: 0.761\n            d2v3: 0.695\n      gpt2xl_nucleus095:\n        binary:\n          acc: 0.9912\n          ci95:\n          - 0.9882\n          - 0.9938\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.79\n          ci95:\n          - 0.775\n          - 0.8047\n          auc:\n            d1v2: 0.913\n            d2v3: 0.891\n        4class:\n          acc: 0.8393\n          ci95:\n          - 0.8283\n          - 0.8502\n          auc:\n            d0v1: 0.995\n            d1v2: 0.916\n            d2v3: 0.885\n      gpt2xl_temp09:\n        binary:\n          acc: 0.9978\n          ci95:\n          - 0.9962\n          - 0.999\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.826\n          ci95:\n          - 0.8117\n          - 0.8397\n          auc:\n            d1v2: 0.944\n            d2v3: 0.887\n        4class:\n          acc: 0.8552\n          ci95:\n          - 0.844\n          - 0.866\n          auc:\n            d0v1: 0.997\n            d1v2: 0.939\n            d2v3: 0.886\n      gpt2xl_topk50:\n        binary:\n          acc: 0.9952\n          ci95:\n          - 0.993\n          - 0.9972\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.695\n          ci95:\n          - 0.6777\n          - 0.7113\n          auc:\n            d1v2: 0.844\n            d2v3: 0.766\n        4class:\n          acc: 0.757\n          ci95:\n          - 0.743\n          - 0.7702\n          auc:\n            d0v1: 0.993\n            d1v2: 0.824\n            d2v3: 0.762\n      olmo_nucleus095:\n        binary:\n          acc: 0.9868\n          ci95:\n          - 0.9832\n          - 0.99\n          auc:\n            d0v1: 0.999\n        3class:\n          acc: 0.7503\n          ci95:\n          - 0.7353\n          - 0.7657\n          auc:\n            d1v2: 0.873\n            d2v3: 0.831\n        4class:\n          acc: 0.7897\n          ci95:\n          - 0.7772\n          - 0.8027\n          auc:\n            d0v1: 0.985\n            d1v2: 0.87\n            d2v3: 0.816\n      olmo_temp09:\n        binary:\n          acc: 0.9982\n          ci95:\n          - 0.997\n          - 0.9992\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.7633\n          ci95:\n          - 0.7477\n          - 0.7797\n          auc:\n            d1v2: 0.894\n            d2v3: 0.838\n        4class:\n          acc: 0.8263\n          ci95:\n          - 0.8147\n          - 0.8385\n          auc:\n            d0v1: 0.996\n            d1v2: 0.903\n            d2v3: 0.828\n      olmo_topk50:\n        binary:\n          acc: 0.996\n          ci95:\n          - 0.994\n          - 0.9978\n          auc:\n            d0v1: 1\n        3class:\n          acc: 0.661\n          ci95:\n          - 0.644\n          - 0.6773\n          auc:\n            d1v2: 0.812\n            d2v3: 0.739\n        4class:\n          acc: 0.7435\n          ci95:\n          - 0.73\n          - 0.758\n          auc:\n            d0v1: 0.995\n            d1v2: 0.831\n            d2v3: 0.738\n    boundary_dilution:\n      d2v3_auc_by_granularity_pythia_nuc:\n        3class: 0.796\n        4class: 0.804\n        6class: 0.689\n      d1v2_auc_by_granularity_pythia_nuc:\n        3class: 0.861\n        4class: 0.868\n        6class: 0.83\n      note: d2v3 AUC drops 14% from 4-class to 6-class (0.804→0.689), confirming decision\n        boundary dilution at higher granularity\n    decoding_strategy_ranking:\n      4class_acc:\n        temp09: 0.814\n        nucleus095: 0.803\n        topk50: 0.732\n      note: topk50 consistently worst across all 3 models; temp09 slightly outperforms\n        nucleus095\n- exp_id: depth_extension_olmo_d4d5_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lr_zscore_cross_strategy_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    raw_lr:\n      mean_acc: 0.25\n      note: lbfgs convergence failure on unscaled features, all predictions random\n      pythia_temp09:\n        acc: 0.25\n        d1v2_auc: 0.6313\n      gpt2xl_temp09:\n        acc: 0.25\n        d1v2_auc: 0.5\n      olmo_temp09:\n        acc: 0.25\n        d1v2_auc: 0.5\n    zscore_lr:\n      mean_acc: 0.6081\n      mean_d1v2: 0.6417\n      pythia_temp09:\n        acc: 0.6139\n        d1v2_auc: 0.5201\n      gpt2xl_temp09:\n        acc: 0.5642\n        d1v2_auc: 0.2386\n      olmo_temp09:\n        acc: 0.5546\n        d1v2_auc: 0.1922\n      pythia_nucleus:\n        acc: 0.6425\n        d1v2_auc: 0.6142\n      gpt2xl_nucleus:\n        acc: 0.7397\n        d1v2_auc: 0.8851\n      olmo_nucleus:\n        acc: 0.748\n        d1v2_auc: 0.8627\n      pythia_topk50:\n        acc: 0.5261\n        d1v2_auc: 0.7711\n      gpt2xl_topk50:\n        acc: 0.5352\n        d1v2_auc: 0.8214\n      olmo_topk50:\n        acc: 0.5484\n        d1v2_auc: 0.8696\n    paper_claim_vs_actual:\n      gpt2xl_temp09_d1v2:\n        paper_raw: 0.13\n        paper_zscore: 0.68\n        actual_raw: 0.5\n        actual_zscore: 0.2386\n      olmo_temp09_d1v2:\n        paper_raw: 0.25\n        paper_zscore: 0.83\n        actual_raw: 0.5\n        actual_zscore: 0.1922\n- exp_id: depth_extension_olmo_d4d5_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    binary_pairwise:\n      d1v2_auc: 0.968\n      d2v3_auc: 0.843\n      d3v4_auc: 0.765\n      d4v5_auc: 0.684\n    six_class_rf_accuracy: 0.667\n    edd_at_075: 4\n    edd_note: d3v4=0.765>=0.75 PASS, d4v5=0.684<0.75 FAIL → EDD=4\n- exp_id: n2_deberta_finetune_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_mean: 0.5831\n    accuracy_std: 0.0467\n    per_class_f1:\n      d0: 0.947\n      d1: 0.378\n      d2: 0.247\n      d3: 0.656\n    pairwise_auc:\n      d0v1: 0.981\n      d1v2: 0.733\n      d2v3: 0.755\n    vs_rf_baseline: 58.3% vs 78.2% (-19.9pp)\n    elapsed_seconds: 3727\n- exp_id: n2_roberta_finetune_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_mean: 0.5948\n    accuracy_std: 0.0324\n    per_class_f1:\n      d0: 0.958\n      d1: 0.4161\n      d2: 0.2611\n      d3: 0.6472\n    per_class_precision:\n      d0: 0.9983\n      d1: 0.7178\n      d2: 0.2956\n      d3: 0.4958\n    per_class_recall:\n      d0: 0.9208\n      d1: 0.293\n      d2: 0.2338\n      d3: 0.9314\n    pairwise_auc:\n      d0v1: 0.9886\n      d1v2: 0.7522\n      d2v3: 0.7349\n    fold_accuracies:\n    - 0.6022\n    - 0.5595\n    - 0.5623\n    - 0.6018\n    - 0.648\n    vs_rf_baseline: -18.7pp (59.5% vs 78.2%)\n    vs_deberta: +1.2pp acc, +0.019 d1v2_auc, -0.020 d2v3_auc\n    elapsed_seconds: 1942.5\n- exp_id: temp07_pilot_pythia_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples_per_depth: 500\n    depths: 6\n    six_class_rf_accuracy: 0.5733\n    six_class_rf_ci95:\n    - 0.5333\n    - 0.615\n    six_class_lr_accuracy: 0.5467\n    pairwise_auc_rf:\n      d0v1: 0.9981\n      d1v2: 0.8378\n      d2v3: 0.635\n      d3v4: 0.5997\n      d4v5: 0.6025\n    pairwise_auc_lr:\n      d0v1: 0.9954\n      d1v2: 0.8031\n      d2v3: 0.608\n      d3v4: 0.6525\n      d4v5: 0.5652\n    vs_temp09_d1v2_rf: 0.8378 vs 0.8327 (+0.005)\n    vs_temp09_d1v2_lr: 0.8031 vs 0.7833 (+0.020)\n    d1v2_inversion: false\n    top_features:\n    - p90_ppl\n    - var_surprisal\n    - mean_surprisal\n    - mean_ppl\n    - p75_ppl\n- exp_id: zeroshot_llm_500_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.362\n    accuracy_ci95:\n    - 0.32\n    - 0.404\n    ci_width_pp: 8.4\n    mae: 1.028\n    per_class_f1:\n      d0: 0.55\n      d1: 0.18\n      d2: 0.27\n      d3: 0.18\n    per_class_recall:\n      d0: 0.952\n      d1: 0.128\n      d2: 0.248\n      d3: 0.12\n    vs_rf_baseline: 36.2% vs 78.2% (-42.0pp)\n    vs_200_sample: 36.2% vs 40.0% (consistent, within CI)\n    n_samples: 500\n    n_errors: 0\n- exp_id: feat_ablation_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full_19_mean_acc: 0.7847\n    full_19_std: 0.0494\n    top5_mean_acc: 0.7678\n    top5_std: 0.0527\n    top2_mean_acc: 0.7152\n    top2_std: 0.0581\n    n_features_95pct_mean: 4.2\n    n_features_95pct_max: 5\n    best_category_all_cells: perplexity\n    perplexity_cat_mean_acc: 0.7668\n    surprisal_cat_mean_acc: 0.7333\n    lexdiv_cat_mean_acc: 0.4618\n    repetition_cat_mean_acc: 0.4374\n    ngram_entropy_cat_mean_acc: 0.3952\n    first_selected_feature_mode: p90_ppl (6/9)\n    first_selected_feature_alt: var_surprisal (3/9)\n    total_runtime_sec: 7822\n- exp_id: feature_ablation_9cell\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: w2_domain_bias_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subexp_a_d1d3_mean_acc: 0.72\n    subexp_a_range: 59.1%-81.8%\n    subexp_b_logo_mean_acc: 0.721\n    subexp_b_range: 59.5%-81.6%\n    subexp_b_note: 'fixed: per-depth seed assignment, groups now depth-balanced. LOGO=CV\n      within noise'\n    subexp_c_depth_pred_mean: 0.72\n    subexp_c_seed_group_pred_mean: 0.102\n    subexp_c_ratio_mean: 7.06\n    subexp_c_note: seed groups at chance (10.2% vs 10%), no measurable domain bias\n    chance_3class: 0.333\n    chance_seed_group: 0.1\n    paper_updated: section_appendix.tex L54-72, conclusion.tex L14\n- exp_id: shap_supplement_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kendalls_w_three_way: 0.8955\n    rho_shap_gini: 0.9312\n    rho_shap_permutation: 0.8392\n    rho_gini_permutation: 0.76\n    cross_cell_shap_consistency_mean_rho: 0.8\n    p90_ppl_top2_cells: 9/9\n    var_surprisal_top2_cells: 8/9\n    ppl_surprisal_shap_share: 0.888\n    shap_top5: p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl\n    addresses: R3-N3 feature importance cross-validation\n- exp_id: xgboost_lgbm_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    xgb_acc: 0.79\n    xgb_std: 0.0046\n    xgb_d0v1_auc: 1\n    xgb_d1v2_auc: 0.931\n    xgb_d2v3_auc: 0.816\n    lgbm_acc: 0.788\n    lgbm_std: 0.0077\n    lgbm_d0v1_auc: 1\n    lgbm_d1v2_auc: 0.931\n    lgbm_d2v3_auc: 0.814\n    rf_acc_ref: 0.782\n    xgb_recall_d0: 0.994\n    xgb_recall_d1: 0.816\n    xgb_recall_d2: 0.596\n    xgb_recall_d3: 0.754\n    lgbm_recall_d0: 0.994\n    lgbm_recall_d1: 0.815\n    lgbm_recall_d2: 0.596\n    lgbm_recall_d3: 0.747\n- exp_id: xgboost_lgbm_3cell_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt2xl_temp09:\n      RF: 85.8\n      XGBoost: 86.2\n      LightGBM: 86.2\n      d1v2_AUC: 0.98\n      d2v3_AUC: 0.886\n    pythia_nucleus095:\n      RF: 78.8\n      XGBoost: 79\n      LightGBM: 78.9\n      d1v2_AUC: 0.931\n      d2v3_AUC: 0.816\n    pythia_topk50:\n      RF: 68.9\n      XGBoost: 68.9\n      LightGBM: 68.7\n      d1v2_AUC: 0.841\n      d2v3_AUC: 0.689\n- exp_id: wild_data_calibration_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext_n_passages: 546\n    wikitext_d0_pct: 100\n    wikitext_d1_pct: 0\n    wikitext_d2_pct: 0\n    wikitext_d3_pct: 0\n    wikitext_mean_p_d0: 0.9963\n    controlled_d0_mean_p_d0: 0.9941\n    controlled_d0_acc: 100\n    controlled_d1_acc: 99.96\n    controlled_d2_acc: 99.94\n    controlled_d3_acc: 99.9\n    cv5_accuracy: 0.7878\n    cv5_std: 0.0056\n    domain_shift_mean_ppl_pct: +621%\n    domain_shift_var_ppl_pct: +503%\n    domain_shift_p90_ppl_pct: +115%\n    finding: WikiText-103 100% classified as d0 despite large feature-space domain\n      shift in perplexity features; RF robust to distribution shift\n- exp_id: downstream_curation_poc_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    unfiltered:\n      ppl_mean: 15.776\n      ppl_std: 0.066\n      n_samples: 10000\n    rf_strict:\n      ppl_mean: 15.81\n      ppl_std: 0.061\n      n_samples: 2496\n      delta: '-0.034'\n      p: 0.607\n      d: -0.528\n    rf_moderate:\n      ppl_mean: 15.756\n      ppl_std: 0.056\n      n_samples: 4940\n      delta: '+0.021'\n      p: 0.492\n      d: 0.334\n    rf_soft:\n      ppl_mean: 15.733\n      ppl_std: 0.038\n      n_samples: 4422\n      delta: '+0.043'\n      p: 0.407\n      d: 0.792\n    oracle_strict:\n      ppl_mean: 15.879\n      ppl_std: 0.128\n      n_samples: 2500\n      delta: '-0.103'\n      p: 0.216\n      d: -1.004\n    oracle_moderate:\n      ppl_mean: 15.809\n      ppl_std: 0.103\n      n_samples: 5000\n      delta: '-0.033'\n      p: 0.485\n      d: -0.384\n    random_strict:\n      ppl_mean: 16.239\n      ppl_std: 0.165\n      n_samples: 2496\n      delta: '-0.463'\n      p: 0.013\n      d: -3.671\n      sig: true\n    random_moderate:\n      ppl_mean: 15.998\n      ppl_std: 0.09\n      n_samples: 5000\n      delta: '-0.222'\n      p: 0.028\n      d: -2.809\n      sig: true\n    cross_condition:\n      rf_strict_vs_random_strict:\n        delta: 0.429\n        t: -7.052\n        p: 0.002\n        sig: true\n      rf_moderate_vs_random_moderate:\n        delta: 0.242\n        t: -3.77\n        p: 0.02\n        sig: true\n      rf_soft_vs_unfiltered:\n        delta: 0.043\n        t: 0.927\n        p: 0.407\n        sig: false\n      random_strict_vs_unfiltered:\n        delta: -0.463\n        t: 4.219\n        p: 0.014\n        sig: true\n- exp_id: wild_data_c4_supplement_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_n_passages: 5000\n    c4_d0_pct: 79.8\n    c4_d1plus_pct: 20.2\n    c4_d1plus_count: 1012\n    wikitext_d0_pct: 100\n    controlled_accuracy: 99.9%+\n    cv5_accuracy: 0.7878\n    misclassified_feature_diff:\n      rep_4gram: +74.7%\n      rep_3gram: +37.0%\n      p90_ppl: +39.6%\n    misclassified_content_type: ads, product descriptions, SEO template content\n    finding: FPR=0% on editorial text (WikiText), FPR≈20% on web-crawl (C4) — false\n      positives driven by template/low-quality content with high repetition and low\n      diversity, not random noise\n- exp_id: pythia7b_cross_scale_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: wild_data_gpt2xl_calibration_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_accuracy: 0.841\n    cv_std: 0.004\n    wikitext_n_passages: 546\n    wikitext_d0_pct: 99.27\n    wikitext_d1_pct: 0.73\n    c4_n_passages: 5000\n    c4_d0_pct: 77.62\n    c4_d1_pct: 9.04\n    c4_d2_pct: 3.72\n    c4_d3_pct: 9.62\n    c4_fpr_vs_pythia: GPT-2 XL FPR 22.4% vs Pythia 20.2% — consistent template/SEO\n      pattern\n    finding: 'Cross-model calibration consistent: both models flag same C4 template\n      content as non-d0. GPT-2 XL slightly higher FPR due to stronger signal. WikiText\n      near-perfect for both.'\n- exp_id: wild_data_olmo_calibration_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_accuracy: 0.7893\n    cv_std: 0.0039\n    wikitext_n_passages: 546\n    wikitext_d0_pct: 98.53\n    wikitext_non_d0: 8\n    c4_n_passages: 5000\n    c4_d0_pct: 95.28\n    c4_d1_pct: 2.92\n    c4_d2_pct: 0.5\n    c4_d3_pct: 1.3\n    c4_fpr: 4.72\n    finding: OLMo C4 FPR (4.72%) far lower than Pythia (20.2%) and GPT-2 XL (22.4%).\n      OLMo d1-d3 features diverge more from d0, creating wider d0 decision boundary\n      that correctly classifies more C4 template content as d0.\n- exp_id: random_soft_control_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_soft_ppl:\n      seed_42: 15.99\n      seed_123: 16.0276\n      seed_456: 16.1682\n      seed_789: 15.9993\n      seed_1024: 16.1224\n      mean: 16.0615\n      std: 0.0794\n    rf_soft_ppl:\n      seed_42: 15.7134\n      seed_123: 15.7014\n      seed_456: 15.7875\n      seed_789: 15.6956\n      seed_1024: 15.7689\n      mean: 15.7334\n      std: 0.042\n    comparison:\n      delta_ppl: 0.3281\n      t_statistic: 17.9777\n      p_value: 5.6e-05\n      cohens_d: 8.0399\n      significant: true\n    train_loss:\n      seed_42: 1.6748\n      seed_123: 1.6786\n      seed_456: 1.6721\n      seed_789: 1.6736\n      seed_1024: 1.6739\n- exp_id: wild_data_redpajama_dolma_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: wild_data_calibration_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: C4 load_dataset hung - allenai/c4 HF streaming failed on AutoDL proxy.\n      OpenWebText loaded OK (5000 passages, 23s) but C4 load_dataset never returned.\n      JSON written with empty datasets/cross_model_consistency. No error/exception\n      in logs - silent hang during HF Hub streaming.\n- exp_id: wild_data_calibration_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fineweb_n_passages: 5000\n    fineweb_d0_pct: 80.54\n    fineweb_d1_pct: 19.46\n    fineweb_d2_pct: 0\n    fineweb_d3_pct: 0\n    fineweb_fpr: 19.46\n    fineweb_mean_p_d0: 0.7987\n    fineweb_mean_p_d1: 0.1707\n    vs_c4_fpr_delta: -0.74\n    vs_wikitext_fpr_delta: 19.46\n    elapsed_seconds: 87\n    finding: FineWeb FPR=19.46% — virtually identical to C4 FPR=20.2% (Δ=-0.74pp).\n      All misclassifications are d1 only (no d2/d3). Confirms web-crawl FPR ~20% is\n      consistent across datasets and driven by template/SEO content, not dataset-specific\n      artifacts.\n- exp_id: zeroshot_qwen7b_500_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    acc_4class: 0.304\n    acc_4class_ci_95:\n    - 0.2653\n    - 0.3457\n    acc_3class: 0.3173\n    mae: 1.01\n    per_class_recall:\n      d0: 0.264\n      d1: 0.552\n      d2: 0.104\n      d3: 0.296\n    per_class_f1:\n      d0: 0.3143\n      d1: 0.3503\n      d2: 0.1436\n      d3: 0.3442\n    errors: 0\n- exp_id: multi_tau_ablation_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_tau:\n      tau_0.5:\n        4class_acc: 0.7725\n        d1v2_auc: 0.8423\n        d0v1_auc: 0.9962\n        d2v3_auc: 0.7636\n      tau_0.7:\n        4class_acc: 0.754\n        d1v2_auc: 0.8505\n        d0v1_auc: 0.9966\n        d2v3_auc: 0.7197\n      tau_0.9:\n        4class_acc: 0.759\n        d1v2_auc: 0.8083\n        d0v1_auc: 0.9911\n        d2v3_auc: 0.7805\n      tau_1.1:\n        4class_acc: 0.5715\n        d1v2_auc: 0.5284\n        d0v1_auc: 0.9878\n        d2v3_auc: 0.5987\n    cross_tau_loo:\n      holdout_0.5:\n        acc: 0.522\n        d1v2_auc: 0.1756\n      holdout_0.7:\n        acc: 0.4095\n        d1v2_auc: 0.2985\n      holdout_0.9:\n        acc: 0.464\n        d1v2_auc: 0.2774\n      holdout_1.1:\n        acc: 0.471\n        d1v2_auc: 0.5251\n      mean_acc: 0.4666\n      mean_d1v2_auc: 0.3192\n    training_loss:\n      tau_0.5:\n        d0: 2.2727\n        d1: 0.4201\n        d2: 0.1589\n      tau_1.1:\n        d0: 2.2726\n        d1: 1.9077\n        d2: 1.8517\n- exp_id: wild_data_calibration_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    openwebtext_pythia_nucleus:\n      n: 5000\n      d0_pct: 99.1\n      fpr_pct: 0.9\n      mean_p_d0: 0.7116\n    openwebtext_gpt2xl:\n      n: 5000\n      d0_pct: 98.56\n      fpr_pct: 1.44\n      mean_p_d0: 0.6191\n    openwebtext_olmo:\n      n: 5000\n      d0_pct: 97.22\n      fpr_pct: 2.78\n      mean_p_d0: 0.7372\n    wikitext: skipped (dtype error)\n    finding: OpenWebText FPR极低(0.9-2.8%) vs C4(4.7-22.4%) vs FineWeb(19.5%). 编辑质量高的web数据FPR显著低于web-crawl。\n- exp_id: cross_scale_qwen7b_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    four_class_acc: 0.601\n    four_class_ci:\n    - 0.58\n    - 0.621\n    six_class_acc: 0.521\n    six_class_ci:\n    - 0.504\n    - 0.538\n    edd: '>5'\n    pairwise_auc_consecutive:\n      d0v1: 0.969\n      d1v2: 0.729\n      d2v3: 0.709\n      d3v4: 0.732\n      d4v5: 0.772\n    auc_pattern: 'U-shape (non-monotonic: trough at d2v3, rises d3v4/d4v5)'\n- exp_id: wild_data_calibration_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fpr: 15.3\n    d0_accuracy: 84.7\n    n_passages: 5000\n    vs_c4: -4.9pp\n    vs_fineweb: -4.16pp\n    vs_openwebtext: +14.4pp\n- exp_id: cross_scale_llama3_8b_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cross_model_recursive_chain_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: domain_extension_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.741\n    4class_std: 0.02\n    per_depth_f1:\n      d0: 1\n      d1: 0.78\n      d2: 0.52\n      d3: 0.66\n    cv_folds: 5\n    domain: arxiv_abstracts\n- exp_id: two_stage_strategy_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    strategy_classification:\n      mean_acc: 0.575\n      chance: 0.333\n      pythia:\n        acc: 0.523\n        nucleus_recall: 0.533\n        temp09_recall: 0.414\n        topk50_recall: 0.622\n      olmo:\n        acc: 0.548\n        nucleus_recall: 0.608\n        temp09_recall: 0.479\n        topk50_recall: 0.558\n      gpt2xl:\n        acc: 0.654\n        nucleus_recall: 0.845\n        temp09_recall: 0.507\n        topk50_recall: 0.61\n    depth_estimation:\n      cross_strategy_loo_ref: 0.591\n      predicted_two_stage:\n        pythia: 0.693\n        olmo: 0.695\n        gpt2xl: 0.73\n        mean: 0.706\n      naive_pooled:\n        pythia: 0.709\n        olmo: 0.712\n        gpt2xl: 0.739\n        mean: 0.72\n      oracle_two_stage:\n        pythia: 0.746\n        olmo: 0.785\n        gpt2xl: 0.82\n        mean: 0.784\n      within_strategy_ref:\n        pythia: 0.745\n        olmo: 0.784\n        gpt2xl: 0.816\n        mean: 0.782\n    key_finding: Oracle two-stage (78.4%) matches within-strategy (78.2%), validating\n      theory. But predicted two-stage (70.6%) < naive pooled (72.0%) due to strategy\n      classification bottleneck (57.5%).\n- exp_id: cross_model_recursive_chain_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.8475\n    4class_ci95:\n    - 0.81\n    - 0.8825\n    per_depth_f1:\n      d0: 0.98\n      d1: 0.88\n      d2: 0.76\n      d3: 0.76\n    pairwise_auc:\n      d0v1: 0.999\n      d2v3: 0.841\n- exp_id: cross_scale_llama3_8b_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cross_scale_llama3_8b_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.702\n    4class_ci95:\n    - 0.683\n    - 0.724\n    6class_acc: 0.554\n    6class_ci95:\n    - 0.536\n    - 0.571\n    edd_estimate: '4'\n    edd_note: d4v5 AUC=0.618 < T=0.70, so EDD=4. Monotonic decay causes last pair\n      to fall below threshold.\n    consecutive_binary_auc:\n      d0v1: 0.949\n      d1v2: 0.877\n      d2v3: 0.771\n      d3v4: 0.716\n      d4v5: 0.618\n    consecutive_binary_acc:\n      d0v1: 0.885\n      d1v2: 0.81\n      d2v3: 0.698\n      d3v4: 0.656\n      d4v5: 0.583\n- exp_id: ref_model_ablation_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_ref_acc: 0.7854\n    olmo_ref_acc: 0.7451\n    delta_pp: 4.04\n    robust: true\n- exp_id: cross_scale_llama3_base_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.599\n    4class_ci_95:\n    - 0.578\n    - 0.6215\n    6class_acc: 0.4953\n    edd_070: 2\n    auc_d0v1: 0.9175\n    auc_d1v2: 0.7936\n    auc_d2v3: 0.6815\n    auc_d3v4: 0.73\n    auc_d4v5: 0.595\n    monotonic: false\n    pattern: U-shape (d2v3 dip, d3v4 recovery)\n    finding: IT regularizes depth signal (makes AUC monotonic), does not introduce\n      U-shape\n    edd_note: d0v1=0.9175≥0.70, d1v2=0.7936≥0.70, d2v3=0.6815<0.70 → EDD=2\n- exp_id: cross_model_reverse_chain_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.75\n    ci_95:\n    - 82\n    - 89.25\n    forward_chain_acc: 84.75\n    forward_chain_ci:\n    - 81\n    - 88.25\n    conclusion: reverse = forward, architecture confound refuted\n- exp_id: lora_rank_ablation_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rank_4_acc: 0.718\n    rank_4_auc: 0.7896\n    rank_16_acc: 0.7645\n    rank_16_auc: 0.8434\n    rank_64_acc: 0.731\n    rank_64_auc: 0.8326\n    best_rank: 16\n- exp_id: gpt2xl_ref_ablation_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    gpt2xl_4class_acc: 0.6734\n    gpt2xl_ci_95:\n    - 0.6667\n    - 0.6796\n    gpt2xl_d1v2_auc: 0.7269\n    pythia_4class_acc: 0.7854\n    pythia_ci_95:\n    - 0.7795\n    - 0.7911\n    pythia_d1v2_auc: 0.8681\n    delta_pp: -11.2\n- exp_id: second_seed_replication_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    4class_acc: 0.7715\n    ci_95:\n    - 0.764\n    - 0.7815\n    d1v2_auc: 0.8531\n    delta_vs_baseline: -0.0105\n    baseline_acc: 0.782\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - var_ppl\n    - p75_ppl\n    per_class_recall:\n      d0: 0.99\n      d1: 0.816\n      d2: 0.586\n      d3: 0.694\n    fold_accuracies:\n    - 0.77\n    - 0.77\n    - 0.79\n    - 0.7675\n    - 0.76\n- exp_id: mixed_depth_corpus_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mixed_overall_acc: 0.855\n    balanced_overall_acc: 0.7814\n    delta_overall_pp: 7.36\n    mixed_macro_recall: 0.7652\n    balanced_macro_recall: 0.7814\n    delta_macro_recall_pp: -1.62\n    per_class_recall_delta:\n      d0: -0.68\n      d1: -2.43\n      d2: -1.12\n      d3: -2.24\n    max_recall_delta_pp: 2.43\n- exp_id: reference_free_baseline_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    4class_acc: 0.5368\n    ci_95:\n    - 0.5336\n    - 0.5401\n    d1v2_auc: 0.6252\n    full_19_acc: 0.7877\n    delta_pp: -25.09\n    recall_d0: 0.8572\n    recall_d1: 0.397\n    recall_d2: 0.3176\n    recall_d3: 0.5756\n- exp_id: ensemble_reference_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ensemble_4class_acc: 0.7365\n    ensemble_ci_95:\n    - 0.7258\n    - 0.7471\n    pythia_acc: 0.7857\n    olmo_acc: 0.7425\n    gpt2xl_acc: 0.7005\n    delta_vs_gpt2xl: 3.6\n    delta_vs_pythia: -4.9\n- exp_id: gen_length_ablation_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    acc_128: 0.6835\n    ci_128:\n    - 0.6765\n    - 0.6905\n    acc_256: 0.738\n    ci_256:\n    - 0.7248\n    - 0.7512\n    acc_512: 0.7782\n    ci_512:\n    - 0.768\n    - 0.7885\n    d1v2_auc_128: 0.7543\n    d1v2_auc_256: 0.8198\n    d1v2_auc_512: 0.8683\n    spread_pp: 9.47\n    delta_128v256_pp: -5.45\n    delta_512v256_pp: 4.02\n- exp_id: cross_seed_transfer_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_seed42_cv: 0.7868\n    within_seed43_cv: 0.7745\n    within_seed_avg: 0.7807\n    train42_test43: 0.7785\n    train43_test42: 0.7568\n    cross_seed_avg: 0.7676\n    delta_pp: -1.3\n- exp_id: cross_strategy_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    strategy_clf_rf_acc: 0.5779\n    strategy_clf_lr_acc: 0.5291\n    pipeline_depth_acc: 0.7053\n    oracle_depth_acc: 0.7831\n    loo_ref_acc: 0.5908\n    improvement_vs_loo: 0.1145\n    gap_pipeline_vs_oracle: 0.0778\n    pipeline_depth_acc_pythia: 0.6925\n    pipeline_depth_acc_olmo: 0.6937\n    pipeline_depth_acc_gpt2xl: 0.7297\n- exp_id: prompted_gen_gpt2xl_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.6952\n    rf_4class_ci:\n    - 0.689\n    - 0.7015\n    bos_baseline_acc: 0.833\n    delta_vs_bos: -0.1378\n    auc_d0v1: 0.9162\n    auc_d0v2: 0.9934\n    auc_d0v3: 0.9974\n    auc_d1v2: 0.7823\n    auc_d1v3: 0.9553\n    auc_d2v3: 0.7444\n    top5_features:\n    - - p90_ppl\n      - 0.1887\n    - - p75_ppl\n      - 0.1335\n    - - mean_surprisal\n      - 0.0916\n    - - var_surprisal\n      - 0.0849\n    - - p50_ppl\n      - 0.0612\n    n_samples: 20000\n    fold_accuracies:\n    - 0.6885\n    - 0.707\n    - 0.6987\n    - 0.6943\n    - 0.6877\n- exp_id: qwen25_14b_scale_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mlp_19feat_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mlp_128_128_acc: 0.7866\n    mlp_64_128_64_acc: 0.7895\n    mlp_poly_top5_acc: 0.7906\n    best_delta_vs_rf: 0.0086\n    d0v1_auc: 0.997\n    d1v2_auc: 0.878\n    d2v3_auc: 0.821\n- exp_id: qwen25_14b_scale_002\n  name: ''\n  status: RUNNING\n  conclusion: null\n  metrics: {}\n- exp_id: text_length_sensitivity_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: bootstrap_ci_table1_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.4742\n    rf_4class_ci:\n    - 0.467\n    - 0.4811\n    lr_4class_acc: 0.4256\n    rf_3class_acc: 0.4987\n    pairwise_auc_rf:\n      d0v1: 0.653\n      d0v2: 0.819\n      d0v3: 0.902\n      d1v2: 0.62\n      d1v3: 0.807\n      d2v3: 0.664\n    pairwise_auc_lr:\n      d0v1: 0.619\n      d0v2: 0.773\n      d0v3: 0.838\n      d1v2: 0.594\n      d1v3: 0.734\n      d2v3: 0.621\n    top_features:\n    - surprisal_range\n    - surprisal_position_corr\n    - prob_std\n    - surprisal_first_half_minus_second\n    - surprisal_std\n    n_samples: 19992\n- exp_id: plan_018_binoculars_baseline\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: detector_ord_baseline_001\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: wild_data_features_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_depth_dist:\n      d0: 6598\n      d1: 3354\n      d2: 18\n      d3: 30\n    c4_pct:\n      d0: 65.98\n      d1: 33.54\n      d2: 0.18\n      d3: 0.3\n    c4_fpr: 34.02\n    fineweb_depth_dist:\n      d0: 8285\n      d1: 1708\n      d2: 4\n      d3: 3\n    fineweb_pct:\n      d0: 82.85\n      d1: 17.08\n      d2: 0.04\n      d3: 0.03\n    fineweb_fpr: 17.15\n    total_c4: 10000\n    total_fineweb: 10000\n    rf_n_estimators: 200\n    rf_train_samples: 20000\n- exp_id: learned_estimator_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: downstream_benchmark_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: downstream_benchmark_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baseline_ppl: 5.67\n    d0_only_ppl: 5.65\n    d1_only_ppl: 5.55\n    d2_only_ppl: 5.56\n    mixed_all_ppl: 5.55\n    best_model: d1_only\n    ppl_improvement_vs_baseline: 0.12 (2.1%)\n- exp_id: learned_estimator_proto_fix_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_accuracy: 0.6664\n    gpt2xl_acc: 0.6835\n    pythia_acc: 0.6155\n    olmo_acc: 0.7001\n    mean_mae: 0.384\n    mean_pairwise_auc: 0.874\n    gpt2xl_auc: 0.8926\n    pythia_auc: 0.8415\n    olmo_auc: 0.9004\n- exp_id: learned_estimator_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    xgboost_pythia: 63.72\n    xgboost_olmo: 69.76\n    xgboost_gpt2xl: 68.05\n    xgboost_mean: 67.18\n    ordinal_mlp_pythia: 62.52\n    ordinal_mlp_olmo: 69.69\n    ordinal_mlp_gpt2xl: 67.9\n    ordinal_mlp_mean: 66.7\n    prototypical_pythia: 61.55\n    prototypical_olmo: 70.01\n    prototypical_gpt2xl: 68.35\n    prototypical_mean: 66.64\n    rf_baseline_mean: 66.4\n    best_single: proto_olmo_70.01\n    best_method_mean: xgboost_67.18\n- exp_id: qwen25-1p5b-instruct-001-phase45\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-001-ph45\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-001-ph45v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-001-ph45v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25-1p5b-instruct-002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen25_14b_scale_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: gpt2xl_seed43_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    rf_4class_acc: 86.32\n    rf_4class_ci_lower: 86.17\n    rf_4class_ci_upper: 86.49\n    d1v2_auc: 0.9489\n    per_class_recall:\n      d0: 99.4\n      d1: 92\n      d2: 73.4\n      d3: 80.5\n    seed42_rerun_acc: 84.28\n    seed42_rerun_ci:\n    - 83.89\n    - 84.77\n    delta_vs_seed42: 2.04\n- exp_id: pythia_seed43_001\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    rf_4class_acc: 0.7884\n    rf_4class_ci_lower: 0.7813\n    rf_4class_ci_upper: 0.7952\n    d1v2_auc: 0.8759\n    per_class_recall:\n      d0: 0.992\n      d1: 0.8248\n      d2: 0.5882\n      d3: 0.7486\n    fold_accs:\n    - 0.8015\n    - 0.7855\n    - 0.786\n    - 0.7932\n    - 0.7758\n    delta_vs_seed42: 0.0064\n    seed42_baseline: 0.782\n    top_features:\n    - var_surprisal\n    - p90_ppl\n    - mean_ppl\n    - var_ppl\n    - mean_surprisal\n- exp_id: olmo_seed43_001\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: theory_section\n  claim: '2'\n  description: 'Theoretical analysis section connecting depth signal to model collapse\n    theory: (1) tail erosion mechanism explaining p90_ppl/var_surprisal dominance\n    via Shumailov et al., (2) EDD upper bound derivation from Dohmatob contraction\n    rates, (3) strategy-dependent convergence rate explaining temp09 trajectory reversal.\n    Half-page theoretical sketch with experimental validation.'\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T16:15:28.136Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T16:15:28.136Z",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-18T16:15:28.161Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：14B shows depth signal but weaker than 1B, theory section provides post-hoc rationalization but not predictive bounds, existing detectors show weak ordinal capability — claims need scope hedging, paper is borderline accept
核心假设：['14B 4-class acc 55-72%, p90_ppl in top-5 but var_surprisal drops out of top-5 or rank inverts', "14B EDD=3 (d3v4 AUC < 0.75), lower than 1B's EDD=4 → scale-dependent EDD attenuation", "Theory section provides qualitative connection (tail erosion narrative) but cannot derive precise EDD bound; Dohmatob contraction analysis yields loose bound (EDD ≤ 8) that doesn't constrain", "Binoculars/Fast-DetectGPT achieve 40-55% ordinal acc → partial overlap with our shallow-depth discrimination, weakening 'new task' exclusivity", '3/3 seed stability confirmed but one model shows >3pp variance, requiring explicit variance-aware CI reporting', "Instruct model weakness + 14B signal degradation creates 'small base model only?' reviewer question"]
关键指标范围：{'14b_4class_acc': [0.55, 0.72], '14b_d1v2_auc': [0.65, 0.8], '14b_edd': [3, 3], '14b_top2_feature_overlap_with_1b': [1, 1], 'existing_detector_ordinal_4class_acc': [0.4, 0.55], 'seed_robustness_max_delta_pp': [2.0, 5.0], 'theory_edd_bound_vs_empirical_error': [2, 4], 'simulated_reviewer_meta_score': [3.0, 3.5], 'accept_probability': [0.25, 0.45]}
叙事方向：需要调整 Claims 强度，但不降级目标 venue。 Claim 1: "feasible, accurate, robust across scales" 改为 "feasible and accurate at 1-1.5B, with attenuated but persistent signal at 14B scale"。 删除 "robust across scales" 的无条件断言，改为 "scale-dependent signal strength with consistent feature family (perplexity tail statistics)"。 Claim 2 (Atlas): EDD 从 "=4 across models and scales" 改为 "=4 at 1B, =3 at 14B, suggesting scale-dependent discriminability horizon"。 理论节降格为 "Theoretical Motivation" 而非 "Theoretical Analysis"——提供 intuition 而非 derivation。 可以新增一条 finding: "depth signal attenuates with model capacity, consistent with larger models producing more uniform recursive degradation"。 Claim 3: 不变（跨策略 pipeline 独立于 scale）。 对 existing detector: 承认 Binoculars 在 d0v1 上接近我们的表现，但论证 ordinal depth (d1/d2/d3 区分) 仍是我们独有的贡献。 需要 AC champion 或 revision opportunity。补充实验可能包括: 14B 多策略覆盖、intermediate scale (3B/7B) 连续曲线。 关键 reviewer rebuttal: "signal attenuation at scale is itself a scientifically valuable finding — it characterizes the boundary of feasibility"。


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
  "promptId": "a8988d14-4fb9-44a9-a67d-1ba993b82e65",
  "type": "user",
  "uuid": "cf9544a9-4527-4a7d-8d1a-1d22e36aaf7f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T16:15:28.158Z_

```json
{
  "parentUuid": "cf9544a9-4527-4a7d-8d1a-1d22e36aaf7f",
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
  "uuid": "6266f24b-d22c-40b3-b25b-b94c37ccb2e2",
  "timestamp": "2026-05-18T16:15:28.158Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T16:15:28.158Z_

```json
{
  "parentUuid": "6266f24b-d22c-40b3-b25b-b94c37ccb2e2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "31af2d2e-3937-4f49-990c-3361eb076f48",
  "timestamp": "2026-05-18T16:15:28.158Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：14B shows depth signal but weaker than 1B, theory section provides post-hoc rationalization but not predictive bounds, existing detectors show weak ordin…",
  "leafUuid": "31af2d2e-3937-4f49-990c-3361eb076f48",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate scale robustness and theory grounding for EMNLP 2026",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50"
}
```

---

### Assistant

_source line 8 · 2026-05-18T16:17:06.794Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each **planned** experiment in the experiment_plan, under the **median** tier definition. Let me identify all experiments with `status: planned` or `status: RUNNING`:

1. **plan_014** (RUNNING) - 13B clean FP16 scale validation (Qwen2.5-14B)
2. **plan_015** (planned) - Wild-data calibration: C4/FineWeb/RedPajama
3. **plan_018** (planned) - Existing detector ordinal baseline: Binoculars + Fast-DetectGPT


4. **plan_020** (planned) - Table 1 bootstrap CIs
5. **plan_023** (planned) - Theoretical analysis
6. **plan_026** (planned) - API model recursive chains

Plus the theory_section what_if for theoretical analysis. I'm skipping plan_010 since it's marked as cancelled despite the planned status.

Now I need to work through each one under the median tier constraints, where the 14B model shows weaker depth signals than the 1B, the theory section provides post-hoc explanations without predictive bounds, and existing detectors have baseline performance characteristics.

Looking at the key metrics here: the 14B 4-class accuracy ranges from 0.55 to 0.72, the AUC sits between 0.65 and 0.8, and the existing detector ordinal accuracy is notably lower at 0.4 to 0.55. The theory-empirical error gap is around 2-4 points, and the simulated reviewer score hovers near 3.0-3.5, putting this paper in borderline accept territory with acceptance probability between 0.25 and 0.45.

Now I'm working through detailed predictions for each planned experiment, starting with plan_014 on the Qwen2.5-14B scale validation that's currently running.

For the 14B model, I'm expecting the 4-class accuracy to land around 0.63 as a middle estimate, with the d1v2 AUC around 0.72. The EDD should be 3, which would be lower than the 1B baseline's EDD of 4. This puts the 14B performance notably below what we saw with the smaller models—the 1B variants hit accuracy in the high 70s to low 80s range, so the 14B at median would represent a meaningful drop, suggesting the ordinal capability doesn't scale as cleanly as expected.

Looking at the feature rankings, p90_ppl stays dominant but var_surprisal loses its top-5 position, likely replaced by mean_ppl or p75_ppl. The d0v1_auc remains strong around 0.96, while d2v3_auc drops to around 0.62. The intuition here is that larger models smooth out the recursive degradation signal across depths because their increased capacity maintains more uniform surprisal distributions, so the tail behavior (p90_ppl) still matters but the variance signal weakens. This aligns with the hypothesis that bigger models produce more uniform degradation patterns.

Now I'm moving to the wild-data calibration phase under the median tier, which involves applying the trained random forest to C4, FineWeb, and RedPajama data. Looking at the false positive rates across these datasets, the median prediction would show similar patterns when applied to the additional corpora. For plan_018, existing detectors like Binoculars and Fast-DetectGPT would achieve only partial ordinal discrimination around 40-55% accuracy. Plan_020 is straightforward—just computing confidence intervals from what we already have, with standard widths and possibly one model showing variance over 3 percentage points. The theoretical analysis in plan_023 provides post-hoc explanations rather than predictive bounds, with the contraction analysis yielding a loose bound that doesn't meaningfully constrain the results. For plan_026 with GPT-4o-mini, I'd expect weaker signal than the base models due to RLHF alignment effects, similar to the instruct model weakness I noted earlier. Now I need to compile the full YAML output covering all planned experiments, including plan_010 which was marked cancelled, plan_014 which is running, and the others through plan_023.

Looking at the registry, I notice plan_020's bootstrap confidence intervals are already marked done, though the plan status still shows planned—there might be a mismatch there. Let me work through each experiment systematically and draft the complete output, starting with plan_014's 14B scale validation results.

For the Qwen2.5-14B tier, I'm expecting the random forest to hit around 0.63 accuracy on the 4-class task with logistic regression at 0.58, while the AUC metrics show strong separation on the first comparison but degrade across subsequent tiers. The feature importance should remain consistent with perplexity percentiles leading, though the larger model's smoother distributions mean the recursive degradation pattern becomes more gradual and uniform compared to smaller models.

The key insight is that while the tail erosion signal from extreme percentiles persists, the variance signal weakens because the model's broader vocabulary use reduces surprisal variation across depths. This causes the classifier to struggle more with adjacent depth boundaries, especially between d1/d2 and d2/d3, pushing the effective depth discrimination down from 4 to 3 tiers.

Now I'm shifting to applying these trained classifiers against wild data to see how well they generalize, expecting the C4 false positive rate to land somewhere in the 25-35% range depending on which model we're evaluating.

Looking at the wild data results across different sources: FineWeb shows lower FPR around 17-20%, RedPajama sits between 15-25%, and the models tend to agree on roughly 70% of their flagged passages. The pattern that emerges is that FPR correlates strongly with how much template and boilerplate content is present in each dataset. This makes sense because web-crawled data contains a lot of repetitive, low-diversity content that statistically resembles recursively-generated text, so the classifier trained on controlled recursive chains picks up those same "low quality" signals. It's not really a failure—it's revealing that depth estimation implicitly captures data quality. Higher-quality sources like OpenWebText and WikiText show almost no false positives. The cross-model consistency is only moderate because different reference models have different perplexity scales, which shifts where the d0 decision boundary lands.

Now I'm looking at how existing detectors perform on the ordinal baseline task. Binoculars and Fast-DetectGPT both achieve around 0.45-0.48 accuracy on the 4-class problem, with strong AUC scores on the binary d0v1 task (0.92-0.95) but much weaker performance on deeper ordinal comparisons. Both detectors are fundamentally built for binary detection rather than ranking depth levels. for binary real-vs-synthetic detection, so their continuous scores carry substantial d0v1 discrimination. However, the ordinal depth signal beyond d0v1 is subtle — the statistical differences between d1 and d2 text are much smaller than between d0 and d1. These detectors' scores are primarily sensitive to the "human vs machine" boundary, not to recursive degradation depth. Binoculars slightly outperforms Fast-DetectGPT because its cross-model perplexity ratio captures some of the same tail statistics (p90_ppl) that our feature-based approach uses. The 40-55% ordinal accuracy is well above chance (25%) but substantially below our feature-based approach (70-85%), demonstrating that ordinal depth estimation is a genuinely harder task that requires purpose-built features. The partial overlap at d0v1 weakens the "completely new task" framing but the d1/d2/d3 discrimination remains our unique contribution.

Now I'm thinking through the bootstrap confidence intervals for Table 1. Most cells show tight intervals around ±1.5-2.5 percentage points across the five-fold cross-validation, with one outlier like Pythia topk50 reaching ±3.5pp. The topk50 strategy consistently exhibits wider variance because truncating the distribution creates more discrete changes across depths, making the feature space more sensitive to random sample composition. Seed variance maxes out at 2-5 percentage points between runs, with one model potentially exceeding 3pp, though all confidence intervals still overlap within each model, confirming the results hold.

For the theoretical analysis, I can provide a qualitative connection between tail erosion and the empirical observations but can't derive a tight bound — the Dohmatob contraction analysis gives an upper bound of 8 for EDD, which is loose compared to the empirical value of 4. The gap between theory and practice suggests the mechanism is more nuanced than the contraction framework captures, and I'll need to explain the temp09 reversal through qualitative reasoning about strategy convergence rather than formal derivation. accelerated attractor convergence
- Section title: "Theoretical Motivation" (not "Theoretical Analysis")

Rationale: The model collapse theory literature establishes that iterative training on synthetic data causes distribution contraction toward a fixed-point attractor, which provides intuition for why p90_ppl captures tail erosion best. But translating the contraction rate constants to a precise EDD bound requires knowing the exact KL divergence between consecutive depth distributions—something that's model-dependent and analytically intractable for transformers. The resulting bound is too loose to be predictive, so this becomes a motivated narrative rather than a rigorous derivation. The temperature convergence explanation works better because it's a direct mechanistic argument about how uniform logit scaling accelerates convergence.

Now I'm looking at the API model experiments with recursive chains. Fine-tuning GPT-4o-mini drops accuracy significantly due to RLHF alignment compressing the depth signal, while prompted chains without fine-tuning show weaker degradation. The feature landscape appears to shift toward surprisal-based metrics over perplexity-based ones, and I'm considering how post-RLHF models like GPT-4o-mini might behave differently from base models in this context. I'm finishing up the theory section with qualitative connections, then moving on to compile the full YAML output with detailed expected results and rationales for each plan. I should also note that plan_010 is actually cancelled due to DCOL v6 failure, so I'll add that clarification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31af2d2e-3937-4f49-990c-3361eb076f48",
  "isSidechain": false,
  "requestId": "req_011CbALFy558UfaHC59drgD4",
  "type": "assistant",
  "uuid": "4e217d6a-055f-4858-9e44-d17740da50de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2aSaqcvu2RydhUQAyaed2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 54527,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 54527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12854,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 54527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 54527
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

_source line 9 · 2026-05-18T16:20:07.271Z_

```yaml
tier: median
narrative_guidance: >
  14B shows depth signal but weaker than 1B, theory section provides post-hoc rationalization
  but not predictive bounds, existing detectors show weak ordinal capability — claims need
  scope hedging, paper is borderline accept. Claim 1 revised to "feasible and accurate at
  1-1.5B, with attenuated but persistent signal at 14B scale". EDD from "=4 across scales"
  to "=4 at 1B, =3 at 14B". Theory section downgraded to "Theoretical Motivation".
  Binoculars partial overlap at d0v1 acknowledged, ordinal d1/d2/d3 discrimination remains
  unique contribution. Need AC champion or revision opportunity.

imagined_experiments:
  - name: "14B_scale_validation"
    plan_id: "plan_014"
    description: >
      Qwen2.5-14B FP16 + LoRA on 96GB GPU, nucleus p=0.95, d0-d3 recursive chain.
      19 statistical features extracted via Pythia-1.4B reference model. RF/LR 5-fold CV classification.
    expected_results:
      rf_4class_acc: 0.632
      rf_4class_ci: [0.618, 0.646]
      lr_4class_acc: 0.578
      lr_4class_ci: [0.563, 0.593]
      rf_3class_acc: 0.521
      rf_3class_ci: [0.504, 0.538]
      auc_d0v1: 0.962
      auc_d0v2: 0.988
      auc_d0v3: 0.994
      auc_d1v2: 0.718
      auc_d1v3: 0.912
      auc_d2v3: 0.624
      auc_d3v4_binary: 0.708
      edd_at_075: 3
      edd_at_070: 3
      top_features:
        - "p90_ppl (0.165)"
        - "p75_ppl (0.128)"
        - "mean_ppl (0.098)"
        - "mean_surprisal (0.076)"
        - "var_surprisal (0.058)"
      var_surprisal_rank: 5
      top2_feature_overlap_with_1b: 1  # p90_ppl overlaps, var_surprisal drops from top-2
      finetune_losses:
        depth_0: 1.85
        depth_1: 1.12
        depth_2: 0.88
      per_class_recall:
        d0: 0.96
        d1: 0.68
        d2: 0.42
        d3: 0.55
      delta_vs_1b_mean: -0.155  # 1B mean ~78.7%, 14B at 63.2% = -15.5pp
      n_samples: 20000
    result_rationale: >
      14B Qwen2.5 has ~10× the parameters of 1B models. Greater capacity produces smoother
      output distributions — the model maintains broader vocabulary utilization and more
      calibrated probabilities even under recursive LoRA fine-tuning. This causes recursive
      degradation to be more gradual and uniform across depths, attenuating the statistical
      differences that 1B models exhibit. Specifically: (1) p90_ppl remains the top feature
      because extreme tail behavior is still affected by recursive generation — even 14B
      models eventually lose tail diversity — but the magnitude of the p90_ppl gap between
      adjacent depths shrinks (~40% smaller than at 1B). (2) var_surprisal drops from
      consistent top-2 (at 1B) to #5 because 14B models produce more uniform surprisal
      distributions across all depths — the variance difference between d1 and d2 falls
      below the RF discrimination threshold. This is the "scale-dependent EDD attenuation"
      core hypothesis: larger models produce more uniform recursive degradation, compressing
      the feature space between adjacent depths. (3) EDD drops to 3 because the d3v4
      boundary (AUC ~0.71) falls below T=0.75 — the signal that was marginal at 1B
      (Pythia d3v4=0.784, GPT-2 XL d3v4=0.750) is pushed below threshold by the ~15%
      AUC attenuation at 14B scale. (4) d0v1 remains high (0.96) because the human-vs-
      machine gap persists at all scales — this is the easiest discrimination and is
      largely scale-independent. (5) The 3-class accuracy (52.1%) is notably lower than
      1B (70-82%) because without the easy d0 class boosting the headline, the d1/d2/d3
      confusion becomes the dominant factor. Per-class recall shows d2 at 42% — the
      "middle depth" confusion that plagues 1B models is amplified at 14B.
    tables:
      - name: "Table_14B_comparison"
        description: >
          Side-by-side: 1B models (3×3 mean) vs 14B. Columns: 4-class acc, 3-class acc,
          d1v2 AUC, d2v3 AUC, EDD, top-2 features. Shows systematic attenuation.
    figures_description:
      - "AUC decay curve: 14B vs 1B mean, showing parallel but downward-shifted curve with EDD=3 vs EDD=4 threshold crossing"
    analysis: >
      14B result confirms depth signal persists at mainstream model scale (63.2% >> 25%
      chance) but with systematic attenuation. The signal attenuation itself is scientifically
      valuable — it characterizes the boundary of feasibility and is consistent with the
      theoretical prediction that larger models produce more uniform recursive degradation.
      Feature family consistency (perplexity-based features dominate at both scales) supports
      the Atlas's universality claim, even though var_surprisal's rank inversion at 14B
      means the feature *ranking* is scale-dependent. This forces Claim 1 revision: "feasible
      and accurate at 1-1.5B, with attenuated but persistent signal at 14B scale" and Claim 2
      revision: "EDD=4 at 1B, EDD=3 at 14B, suggesting scale-dependent discriminability
      horizon." The finding is reframed as: depth signal attenuation at scale is itself
      the contribution, not a weakness.

  - name: "wild_data_calibration"
    plan_id: "plan_015"
    description: >
      Apply trained 3×3 RF classifiers (Pythia/OLMo/GPT-2 XL reference models) to
      C4, FineWeb, and RedPajama subsets. Extract 19 features per passage, predict depth
      distribution. Cross-model agreement analysis.
    expected_results:
      c4:
        n_passages: 10000
        depth_distribution_pythia: {d0: 66.0, d1: 30.5, d2: 2.0, d3: 1.5}
        depth_distribution_gpt2xl: {d0: 62.0, d1: 32.0, d2: 3.5, d3: 2.5}
        depth_distribution_olmo: {d0: 80.0, d1: 17.5, d2: 1.5, d3: 1.0}
        fpr_range: [20.0, 38.0]
        cross_model_agreement_d0: 0.72
      fineweb:
        n_passages: 10000
        depth_distribution_pythia: {d0: 80.0, d1: 18.0, d2: 1.2, d3: 0.8}
        fpr_range: [17.0, 22.0]
      redpajama:
        n_passages: 10000
        depth_distribution_pythia: {d0: 75.0, d1: 22.0, d2: 2.0, d3: 1.0}
        fpr_range: [20.0, 28.0]
      cross_model_agreement_on_flagged_passages: 0.68
      misclassification_content_profile: "template, SEO, product descriptions, boilerplate"
    result_rationale: >
      Prior wild-data experiments (wild_data_calibration_001 through 005, wild_data_features_001)
      established that web-crawl FPR is ~17-34% depending on reference model, with
      misclassifications concentrated in template/SEO/boilerplate content. C4 shows higher
      FPR than FineWeb because C4 includes more raw web-crawl without the quality filtering
      that FineWeb applies. RedPajama is intermediate — its Common Crawl component drives
      FPR up while its curated components (Wikipedia, ArXiv, GitHub) pull it down.
      Cross-model agreement on flagged passages is moderate (~68%) because different reference
      models have different perplexity scales and d0 decision boundaries: OLMo's Dolma-trained
      distributions diverge more from d0, creating a wider d0 boundary that correctly
      classifies more template content as d0 (hence OLMo's consistently lower FPR, consistent
      with wild_data_olmo_calibration_001 showing 4.72% FPR vs Pythia's 20.2%). The
      disagreement between models on borderline cases is itself informative — it identifies
      the "twilight zone" of web content that shares statistical properties with shallow
      recursive text. Almost all misclassifications are d0→d1 (not d2/d3), consistent with
      wild_data_features_001 and wild_data_calibration_003.
    tables:
      - name: "Table_wild_data_depth_distribution"
        description: >
          Rows: C4 / FineWeb / RedPajama. Columns per reference model: %d0, %d1, %d2, %d3, FPR.
          Shows consistent pattern across datasets with model-dependent FPR.
    figures_description:
      - "Stacked bar chart: depth distribution across 3 wild datasets × 3 reference models, with OpenWebText/WikiText as clean baselines"
    analysis: >
      Wild-data calibration confirms the classifier is deployable but requires FPR-aware
      interpretation. The ~20-30% FPR on raw web-crawl is not a classifier failure but
      reveals that template/boilerplate content genuinely shares statistical properties
      with shallow recursive text — this is a data quality signal, not noise. For paper
      framing: this supports Discussion Claim 4 (depth-graduated curation) by showing that
      the classifier can be used as a quality proxy, though the FPR must be honestly reported.
      The cross-model disagreement on borderline cases suggests an ensemble approach could
      reduce FPR (passages flagged by all 3 models → high-confidence non-d0).

  - name: "existing_detector_ordinal_baseline"
    plan_id: "plan_018"
    description: >
      Run Binoculars and Fast-DetectGPT on the 3×3 benchmark data (9 cells × 4 depths).
      Calibrate continuous detection scores into ordinal depth bins using isotonic regression.
      Evaluate 4-class ordinal accuracy and pairwise AUC.
    expected_results:
      binoculars:
        4class_acc: 0.48
        4class_acc_ci: [0.46, 0.50]
        d0v1_auc: 0.952
        d1v2_auc: 0.582
        d1v3_auc: 0.74
        d2v3_auc: 0.523
        3class_acc: 0.39
        per_class_recall: {d0: 0.94, d1: 0.42, d2: 0.28, d3: 0.38}
      fast_detectgpt:
        4class_acc: 0.45
        4class_acc_ci: [0.43, 0.47]
        d0v1_auc: 0.928
        d1v2_auc: 0.554
        d1v3_auc: 0.71
        d2v3_auc: 0.505
        3class_acc: 0.36
        per_class_recall: {d0: 0.91, d1: 0.38, d2: 0.25, d3: 0.35}
      our_rf_mean:
        4class_acc: 0.783
        d0v1_auc: 0.993
        d1v2_auc: 0.873
        d2v3_auc: 0.805
      delta_binoculars_vs_ours: -0.303
      delta_fastdetectgpt_vs_ours: -0.333
      binoculars_d0v1_competitive: true  # within 5pp of our d0v1
      ordinal_d1d2d3_discrimination_unique: true  # >20pp gap on d1v2, d2v3
    result_rationale: >
      Binoculars (Hans et al. ICML 2024) computes a cross-model perplexity ratio that is
      primarily optimized for the human-vs-machine boundary. Its continuous score carries
      strong d0v1 signal (AUC ~0.95) because the d0-vs-d1 gap is the same binary detection
      task it was designed for. However, the ordinal d1→d2→d3 progression produces only
      small, monotonic changes in the Binoculars score because recursive degradation at
      adjacent depths creates subtle distributional shifts that a single scalar score cannot
      resolve. Specifically, Binoculars' perplexity ratio captures some of the same p90_ppl
      tail signal that our feature-based approach uses, but lacks the multi-dimensional
      feature space (19 features including surprisal variance, lexical diversity, etc.)
      needed to discriminate adjacent depths. Fast-DetectGPT (Bao et al. 2024) uses
      curvature-based detection, which is even less sensitive to depth-specific distributional
      shifts — its score primarily reflects "how machine-like" the text is, not "how many
      recursive cycles." The 40-55% ordinal accuracy range (vs 25% chance) means these
      detectors have *weak* ordinal capability — enough to partially order depths but not
      enough for reliable estimation. The d0v1 overlap (~5pp gap with our method) weakens
      the "completely new task" framing but the d1v2 gap (28-32pp) and d2v3 gap (28-30pp)
      firmly establish ordinal depth estimation beyond d0 as our unique contribution.
      Binoculars' slight edge over Fast-DetectGPT is because its perplexity ratio is more
      directly related to our p90_ppl feature than Fast-DetectGPT's curvature metric.
    tables:
      - name: "Table_detector_comparison"
        description: >
          Rows: Our RF (19-feat) / Binoculars / Fast-DetectGPT / Chance.
          Columns: 4-class acc, d0v1 AUC, d1v2 AUC, d2v3 AUC, 3-class acc (d1-d3 only).
          Highlights the ordinal discrimination gap.
    figures_description:
      - "Pairwise AUC bar chart: 3 methods × 3 depth pairs (d0v1, d1v2, d2v3), showing convergence at d0v1 and divergence at deeper pairs"
    analysis: >
      Existing detectors achieve 40-55% ordinal accuracy — above chance but far below
      our feature-based approach (78.3%). Critically, their d0v1 performance (92-95% AUC)
      approaches ours (99.3%), so the binary detection aspect of our task is not novel.
      However, the d1v2 and d2v3 discrimination — the core of ordinal depth estimation —
      remains exclusively our domain (28-33pp gap). Paper must acknowledge: "Binoculars
      achieves near-parity on the d0-vs-d1 boundary, confirming that binary machine text
      detection is well-addressed by existing methods. Our contribution lies in ordinal
      depth discrimination (d1/d2/d3), where existing detectors show only weak capability."
      This weakens the "entirely new task" positioning but strengthens the "ordinal depth
      is genuinely harder and requires purpose-built features" argument.

  - name: "bootstrap_confidence_intervals"
    plan_id: "plan_020"
    description: >
      Compute bootstrap 95% CIs for all 9 cells in Table 1 (3 models × 3 strategies)
      from existing 5-fold CV results. Report CI width, inter-seed variance, and identify
      cells with >3pp variance.
    expected_results:
      ci_widths:
        pythia_nucleus: 2.1
        pythia_temp09: 2.3
        pythia_topk50: 2.8
        olmo_nucleus: 2.0
        olmo_temp09: 1.9
        olmo_topk50: 2.5
        gpt2xl_nucleus: 1.8
        gpt2xl_temp09: 2.2
        gpt2xl_topk50: 2.6
      mean_ci_width_pp: 2.24
      max_ci_width_pp: 2.8
      seed_variance:
        pythia_nucleus_max_delta: 1.05  # plan_001a vs second_seed_replication_001: 78.2 vs 77.15
        gpt2xl_temp09_max_delta: 3.3    # gpt2xl_seed43_001: 86.32 vs 84.28 seed42 rerun
        pythia_temp09_max_delta: 1.8
      models_with_gt_3pp_variance: 1  # GPT-2 XL temp09
      variance_aware_ci_required: true
      all_cells_above_chance: true
      all_cells_ci_nonoverlapping_with_chance: true
    result_rationale: >
      Bootstrap CIs from 5-fold CV on 20,000 samples per cell yield ±1.8-2.8pp widths.
      This is standard for RF classifiers on this sample size. The topk50 strategy
      consistently shows wider CIs across all models (mean +0.6pp vs nucleus/temp09) because
      top-k truncation creates more discrete distributional modes, making the feature space
      more sensitive to random sample composition — different folds capture different
      proportions of "near-boundary" samples. GPT-2 XL temp09 shows >3pp inter-seed
      variance (gpt2xl_seed43_001 accuracy 86.32% vs seed42 rerun 84.28% = 2.04pp delta,
      and with bootstrap resampling this extends to ~3.3pp max delta) because this cell has
      the strongest signal overall (85.4%) but also the highest sensitivity to the specific
      training data composition — the temp09 × GPT-2 XL combination produces the widest
      feature space separation, making the RF decision boundaries more variable across seeds.
      This triggers the median-tier requirement for "explicit variance-aware CI reporting" —
      all Table 1 entries must include ±CI, and a footnote must note the GPT-2 XL temp09
      variance. The finding doesn't undermine the results (all cells remain far above chance
      even at CI lower bounds) but requires honest reporting.
    tables:
      - name: "Table_1_with_CIs"
        description: >
          Full 3×3 grid with RF 4-class accuracy ± 95% CI. Footnote on GPT-2 XL temp09
          inter-seed variance.
    figures_description: []
    analysis: >
      CIs confirm all 9 cells are statistically significant (lower bounds all >55%, chance=25%).
      The GPT-2 XL temp09 >3pp variance doesn't invalidate the result but requires careful
      reporting. Paper should present Table 1 with explicit CIs and note: "We observe
      inter-seed variance up to 3.3pp in the strongest cell (GPT-2 XL τ=0.9); all reported
      accuracies are means with 95% bootstrap CIs."

  - name: "theoretical_analysis_section"
    plan_id: "plan_023"
    description: >
      Theory section connecting depth signal to model collapse theory. Three components:
      (1) tail erosion mechanism via Shumailov et al. explaining p90_ppl/var_surprisal
      dominance, (2) EDD upper bound from Dohmatob contraction rates, (3) strategy-dependent
      convergence rate explaining temp09 reversal. Output: ~1.5 page "Theoretical Motivation"
      section draft.
    expected_results:
      tail_erosion_narrative:
        quality: "qualitative — convincing intuition, not formal proof"
        connection_strength: "moderate"
        cites: ["Shumailov et al. 2024", "Alemohammad et al. 2024"]
        key_argument: >
          Recursive generation progressively erodes distribution tails because each
          fine-tuning step compresses the model's output distribution toward its mode.
          p90_ppl captures this tail erosion directly — high-perplexity tokens (the tail)
          are the first casualties of recursive collapse. var_surprisal captures the
          second-order effect: as tails erode, the surprisal distribution narrows,
          reducing variance.
      edd_bound:
        derived_bound: "EDD ≤ 8"
        empirical_edd: 4
        bound_gap: 4
        bound_tightness: "loose — does not constrain"
        method: "Dohmatob (2024) contraction rate analysis applied to KL divergence between consecutive depths"
        limitation: >
          Requires Gaussian approximation of token distribution and known contraction
          rate constant. Transformer output distributions are heavy-tailed, making the
          Gaussian bound loose. The contraction rate is model-dependent and not
          analytically tractable for transformers.
      strategy_convergence:
        quality: "strong mechanistic argument"
        key_argument: >
          Temperature sampling applies uniform logit scaling (z/τ), which accelerates
          convergence to the attractor distribution by amplifying the effect of each
          recursive step on the probability mass distribution. Nucleus/top-k truncation
          preserves relative ordering within the selected set, producing slower convergence.
          This explains why temp09 depth N features ≈ nucleus depth N+1.
        formalization: "inequality relating convergence rate to temperature parameter"
      section_title: "Theoretical Motivation"
      section_length_pages: 1.5
      theory_edd_bound_vs_empirical_error: 4
      reviewer_assessment: "provides useful intuition but does not meet the bar for 'theoretical contribution'"
    result_rationale: >
      The median tier predicts theory provides "post-hoc rationalization but not predictive
      bounds." This is because: (1) The tail erosion narrative is qualitatively compelling —
      Shumailov et al. 2024 showed that iterative training causes "model collapse" where
      minority modes are lost first, and p90_ppl directly measures the health of the
      distribution tail. However, this is a *post-hoc* explanation of why p90_ppl works,
      not a *prediction* that it should work. A reviewer would note: "this explains the
      finding after the fact but does not derive it." (2) The EDD bound from Dohmatob's
      contraction analysis yields EDD ≤ 8 because the contraction rate constant for
      Gaussian approximations is ~0.85-0.92 per iteration, and log(1/ε)/log(1/ρ) for
      AUC-detectable differences gives ~8 steps. But empirical EDD=4 — the bound is 2×
      too loose. This is because transformer token distributions are heavy-tailed (not
      Gaussian), and the actual contraction rate is faster than the Gaussian approximation
      suggests. The bound doesn't constrain or predict — it's consistent with EDD=4 but
      would also be consistent with EDD=2 or EDD=7. (3) The strategy convergence argument
      is the strongest theoretical contribution because it's a direct mechanistic claim
      (temperature uniformly scales logits → faster convergence) with empirical verification
      (temp09 d1 p90_ppl ≈ nucleus d2 p90_ppl). This is the one theoretical result that
      a reviewer would find genuinely informative. Overall, the section is downgraded from
      "Theoretical Analysis" to "Theoretical Motivation" — it provides framing and intuition
      but the paper's strength remains empirical.
    tables: []
    figures_description:
      - "Schematic: distribution contraction across recursive depths, showing tail erosion with p90_ppl threshold marked"
    analysis: >
      The theory section addresses the "no algorithmic contribution" concern partially but
      not fully. It provides enough intellectual scaffolding to argue the paper is "empirical
      study with theoretical grounding" rather than "just tables." The EDD bound failure
      (8 vs 4) must be honestly reported — "our theoretical upper bound (EDD ≤ 8) is
      consistent with but does not predict the empirical EDD=4, suggesting tighter bounds
      require distribution-specific analysis beyond Gaussian approximations." The strategy
      convergence mechanism is the strongest contribution and should be highlighted. A
      reviewer at EMNLP would likely write: "The theoretical section provides useful context
      but falls short of a formal contribution. The paper's strength remains its empirical
      thoroughness."

  - name: "api_model_recursive_chains"
    plan_id: "plan_026"
    description: >
      Two approaches: (a) GPT-4o-mini fine-tuning API for d0-d3 recursive chain,
      (b) prompted recursive chain (rewrite/continue prompts) without fine-tuning.
      Extract 19 features via Pythia-1.4B reference model, evaluate RF classification.
    expected_results:
      finetuned_chain:
        rf_4class_acc: 0.42
        rf_4class_ci: [0.40, 0.44]
        d0v1_auc: 0.72
        d1v2_auc: 0.55
        d2v3_auc: 0.48
        top_features: ["surprisal_range", "prob_std", "surprisal_position_corr", "var_surprisal", "p90_ppl"]
        feature_family_shift: true  # surprisal-based features overtake perplexity-based
      prompted_chain:
        rf_4class_acc: 0.35
        rf_4class_ci: [0.33, 0.37]
        d0v1_auc: 0.65
        d1v2_auc: 0.50
        d2v3_auc: 0.45
      instruct_baseline_comparison: 0.474  # plan_021 Qwen-1.5B-Instruct
      delta_vs_base_1b: -0.35  # vs ~78% base model mean
    result_rationale: >
      API models (GPT-4o-mini) are post-RLHF, which fundamentally alters the recursive
      degradation signal. RLHF alignment regularizes the output distribution by penalizing
      low-quality/repetitive text and rewarding coherent responses. This means: (1) Each
      recursive fine-tuning step produces less distributional shift than in base models
      because the RLHF "prior" acts as a regularizer that resists collapse. The tail
      erosion is slower and more uniform, reducing p90_ppl's discriminative power.
      (2) The feature dominance shifts from perplexity-based to surprisal-based because
      RLHF models have calibrated confidence — their perplexity distributions are already
      compressed (lower variance), so surprisal-based features (which capture token-level
      prediction patterns) become more informative for detecting the subtle depth differences
      that remain. This is consistent with plan_021 (Qwen-1.5B-Instruct) where the top
      features were surprisal_range and surprisal_position_corr — completely different from
      the p90_ppl/var_surprisal family that dominates base models. (3) The prompted chain
      approach (no fine-tuning, just prompted rewriting) shows even weaker signal because
      prompted rewriting doesn't create the same recursive LoRA-based distributional shift.
      Each "rewrite" passes through the model's RLHF-aligned generation process, which
      actively normalizes the output toward the model's preferred distribution. The depth
      signal becomes a subtle stylistic shift rather than a distributional collapse.
      (4) 42% accuracy for fine-tuned chain is above chance (25%) but below instruct
      models (47.4%), because GPT-4o-mini has stronger RLHF regularization than
      Qwen-1.5B-Instruct. This compounds the "small base model only?" reviewer concern —
      the paper must honestly report that depth estimation accuracy degrades substantially
      for RLHF-aligned models.
    tables:
      - name: "Table_model_type_comparison"
        description: >
          Rows: Base 1B (mean), Base 14B, Instruct 1.5B, API fine-tuned, API prompted.
          Columns: 4-class acc, d0v1 AUC, d1v2 AUC, top-2 features.
          Shows monotonic degradation: base > instruct > API.
    figures_description: []
    analysis: >
      API model results strengthen the "instruct model weakness" finding into a systematic
      pattern: base models (78%) >> instruct models (47%) >> API-RLHF models (42%) >>
      prompted chains (35%). This is scientifically valuable — it maps the relationship
      between alignment strength and depth signal. For the paper, this creates a clear
      limitation: "Depth estimation as formalized here is most effective for base language
      models. RLHF alignment progressively attenuates the recursive degradation signal,
      reducing accuracy toward chance for strongly aligned models." This is honest and
      defensible — the paper's contribution is the task formalization and empirical
      characterization, not a universal solution. However, it gives reviewers ammunition
      for the "practical utility is limited to base models" concern.

  - name: "theory_section_whatif"
    plan_id: "what_if:theory_section"
    description: >
      Hypothetical theory section as described in what_if. Same content as plan_023
      but framed as the section's contribution to overall paper scoring.
    expected_results:
      contribution_to_paper_score: "+0.2 to +0.4 meta-score points"
      addresses_no_algorithmic_contribution: "partially"
      reviewer_reaction: >
        R1 (methods-focused): "The theory section provides context but does not constitute
        a theoretical contribution. The EDD bound is too loose to be useful."
        R2 (empirical-focused): "Appreciated the connection to model collapse theory.
        The tail erosion narrative is compelling even if informal."
        R3 (application-focused): "Theory section is fine. More concerned about practical
        deployment."
      simulated_reviewer_meta_score_with_theory: 3.3
      simulated_reviewer_meta_score_without_theory: 2.9
      accept_probability_with_theory: 0.35
      accept_probability_without_theory: 0.20
    result_rationale: >
      The theory section moves the paper from "purely empirical study" (meta-score ~2.9) to
      "empirical study with theoretical grounding" (meta-score ~3.3). This is a meaningful
      but not decisive shift. The section earns credit for: (a) connecting to established
      model collapse theory (shows the authors understand the broader context), (b) providing
      a mechanistic explanation for feature dominance (p90_ppl ↔ tail erosion), (c) the
      strategy convergence argument (temperature accelerates attractor convergence). It
      loses credit for: (a) the loose EDD bound (8 vs 4), which a sharp reviewer will
      note provides no actual constraint, (b) post-hoc rationalization flavor — the theory
      explains rather than predicts. At EMNLP, this is borderline — the "New Missions"
      track is more tolerant of empirical papers, but even there, reviewers expect some
      formal grounding. The 0.35 accept probability reflects that the paper needs an AC
      champion who values the task formalization + Atlas contributions over the theoretical
      gap. Without the theory section, the paper is likely rejected as "just an empirical
      study." With it, the paper is borderline — revision could push it over if
      supplementary experiments (14B multi-strategy, intermediate scales) fill remaining gaps.
    tables: []
    figures_description: []
    analysis: >
      Theory section is load-bearing for the paper's survival at EMNLP even if it's not
      a strong contribution in isolation. It transforms the paper's positioning from
      "benchmark paper" to "empirical study with theoretical motivation" — a crucial
      distinction for reviewer psychology. The key rebuttal line it enables: "Our paper
      provides both empirical characterization AND theoretical explanation for the observed
      phenomena, connecting depth estimation to established model collapse theory." Without
      it, the paper has no response to "this is just tables."

  - name: "dcol_component_ablation_cancelled"
    plan_id: "plan_010"
    description: >
      DCOL component ablation — CANCELLED. Pre-requisite plan_004 (DCOL v6 RoBERTa)
      concluded negative (test acc 64.5% vs RF baseline 78.2%). No ablation to perform.
    expected_results:
      status: "cancelled"
      reason: "DCOL v6 failed (plan_004 negative), no model to ablate"
    result_rationale: >
      DCOL v6 (RoBERTa-large) showed severe overfitting (train 75% vs val 64.4%) and
      was 13.7pp below RF baseline. Since the contrastive ordinal learning approach
      itself failed, there is no meaningful ablation to perform. This is consistent
      with the DCOL contingency plan (D010/D011) — DCOL demoted to negative analysis
      in Appendix, Atlas/EDD promoted to primary contribution.
    tables: []
    figures_description: []
    analysis: "N/A — cancelled experiment."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e217d6a-055f-4858-9e44-d17740da50de",
  "isSidechain": false,
  "requestId": "req_011CbALFy558UfaHC59drgD4",
  "type": "assistant",
  "uuid": "026283e6-df8c-4bbe-b506-9b944384a537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2aSaqcvu2RydhUQAyaed2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 54527,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 54527,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12854,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 54527,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 54527
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：14B shows depth signal but weaker than 1B, theory section provides post-hoc rationalization but not predictive bounds, existing detectors show weak ordin…",
  "leafUuid": "026283e6-df8c-4bbe-b506-9b944384a537",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate scale robustness and theory grounding for EMNLP 2026",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：14B shows depth signal but weaker than 1B, theory section provides post-hoc rationalization but not predictive bounds, existing detectors show weak ordin…",
  "leafUuid": "026283e6-df8c-4bbe-b506-9b944384a537",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate scale robustness and theory grounding for EMNLP 2026",
  "sessionId": "5cfb2032-8f05-4aa3-b4b9-3d7d4482fa50"
}
```

---
