# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：K*=2 universality 被打破 + C3 无显著收益 — 需要从 method/application paper 重构为 analysi

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/49cfad2c-a8f3-4c96-a966-f91b37069d83.jsonl`
- **Structured JSON:** [`b814253c51337a5ffaa0.json`](../../sessions/b8/b814253c51337a5ffaa0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T08:31:38.623Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T08:31:38.623Z",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：K*=2 universality 被打破 + C3 无显著收益 — 需要从 method/application paper 重构为 analysis/measurement paper\n核心假设：['exp-003 解码消融: K* 在不同解码策略间变化剧烈（greedy K*=1, high-temp K*=3），K*=2 不是 stable property 而是特定配置的 artifact', 'exp-004 7B: K*=1（更强模型的递归文本更快趋同，1v2 AUC CI upper < 0.60）', 'exp-006 graduated filtering: graduated − binary < 0.5pp，p > 0.10（不显著）', 'exp-015 learned features: frozen embedding+MLP 优于 hand-crafted ≥ 10pp（hand-crafted features 不够用）', 'Qwen-cont 在更严格测试（e.g., 不同 seed 的 depth chain）中 1v2 CI lower 跌破 0.60']\n关键指标范围：{'auc_1v2_continuation_new_configs': [0.55, 0.62], 'auc_1v2_7B': [0.53, 0.59], 'k_star_across_decoding': ['varies 1-3, no stable universal value'], 'graduated_minus_binary_delta_pp': [-0.5, 0.5], 'cross_model_transfer_retention_expanded': [0.7, 0.85], 'spearman_rho_degradation_new_configs': [0.7, 0.82], 'dsir_vs_graduated_delta_pp': [-1.0, 0.5], 'ordinal_accuracy_best_model': [0.35, 0.4]}\n叙事方向：原始 framing 不可持续。C3 必须删除或降为 negative result 段落。C1' 从 \"K*=2 is the  boundary\" 重构为 \"K* is configuration-dependent: we map the factors that govern it\"。 论文变成 empirical analysis paper: \"What Controls the Discriminability of Recursive  Synthetic Text?\" 核心贡献变为 (1) DPI 理论框架 + K* 概念的形式化定义, (2) 首次系统测量  K* 随 model/scale/decoding/generation-mode 的变化图谱, (3) cross-model transfer  分析揭示 depth signal 的 text-intrinsic vs model-specific 分解。叙事转向: \"practitioners  不能假设固定 K*，必须根据具体配置估计\"。如果 learned features 远优于 hand-crafted， 需要承认 15D features 是 convenience baseline 而非 sufficient tool，加 future work  呼吁 learned approaches。目标: EMNLP 2026 Findings 或放弃 EMNLP 转投 AAAI 2027 (多 2 个月补实验)。审稿人可能评价 \"interesting analysis but limited actionable contribution\" → 需要在 related work 中强调 measurement paper 的 venue precedent。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-contamination\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 91-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, D012)\n\n### Primary: C1' (K* Characterization)\n首次系统测量递归合成文本的 generational discrimination boundary K*。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 4-model × 2-mode 实验矩阵系统表征 K*_empirical 的行为，包括跨模型一致性、特征退化排序、以及 generation mode 对 depth signal 的调控效应。\n\n**子组件：**\n\n**(a) K* = 2 across all tested configurations**\n> 4-model 1v2 bootstrap 95% CI 汇总：\n> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|---------|--------|-----------------|\n> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |\n>\n> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002\n> - K* 不是离散跳变值，而是 CI-bounded continuum threshold\n> - Paper 可写：\"K*=2 (bootstrap 95% CI for AUC₁ᵥ₂ > 0.60 across all four model configurations; AUC₂ᵥ₃ CI upper < 0.60)\"\n\n**(b) Cross-model transfer**\n> - Pythia↔OLMo 91% accuracy retention → K*=2 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）\n> - depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity\n\n**(c) Degradation ordering consistency**\n> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）\n> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std\n> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）\n> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）\n\n**(d) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection（\"How does generation mode affect depth estimation?\"），不是独立 claim\n\n### Secondary: C3 (Graduated Filtering)\n即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+ 三级）下，K*-aware graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 4-model × 2-mode 实验矩阵系统表征 K*，揭示控制因素（模型架构、解码策略、generation mode），为数据治理提供 actionable guidance。\n- **Headline result template**: \"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with depth features that are 70-85% text-intrinsic (Pythia↔OLMo 91% transfer retention). Even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*=2 太浅，graduated filtering 收益有限\"** → K* 是模型/解码策略依赖的；展示不同解码策略如何调控 K*（exp-003）；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated（exp-006）\n2. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ generation mode analysis，不是分类器本身\n3. **\"Prompt-chain 不代表真实世界递归污染\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法\n4. **\"单模型/单数据集，泛化性不够\"** → 3 个模型族 × 2 种 generation mode + 4×4 cross-model transfer matrix\n5. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013 直接反驳**：Pythia↔OLMo 91% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity\n6. **\"为什么不用 learned representations\"** → 作为 baseline 对比；hand-crafted features 更 interpretable 且支持 degradation ordering 分析\n7. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep\n8. **\"K* 的统计不确定性未量化\"** → 4-model bootstrap CI + permutation test（exp-007）\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study，C3 是 practical application，generation mode analysis 增加深度\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization + transfer analysis 的 novelty\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_001_pythia_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_002_olmo_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- id: exp-003\n  claim:\n  - 1\n  - 3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: exp_003_decoding_ablation\n  status: RUNNING\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth\n    0-3. 测试 K* 是否随模型规模变化。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_005_degradation\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)\n    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α\n    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated\n    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'\n  priority: P0\n  gpu_budget_hours: 72\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-007\n  claim:\n  - 1\n  - 2\n  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算\n    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为\n    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation\n    test + 3-class metrics]'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: exp_007_bootstrap_ci\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9972\n        ci_lower: null\n        ci_upper: null\n        perm_p: null\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: null\n  status: planned\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: null\n  status: planned\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: exp_010_ordinal_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: null\n  status: planned\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001\n    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier\n    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是\n    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-017\n  registry_id: exp_013_cross_transfer\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features，验证 interpretable features 的价值。[Dream worst tier\n    flagged as critical for \"data-intrinsic ceiling\" claim — 需要 stronger probe 才能支撑该\n    claim]'\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-017\n  claim:\n  - 1\n  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,\n    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model\n    对 K* 的影响。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_017_qwen_continuation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- id: mvp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_sat_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- exp_id: exp_001_pythia_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- exp_id: exp_002_olmo_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- exp_id: exp_003_decoding_ablation\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_017_qwen_continuation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- exp_id: exp_013_cross_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- exp_id: exp_005_degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- exp_id: exp_007_bootstrap_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9972\n        ci_lower: null\n        ci_upper: null\n        perm_p: null\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- exp_id: exp_010_ordinal_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-13T08:31:38.626Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T08:31:38.626Z",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-13T08:31:38.646Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：K*=2 universality 被打破 + C3 无显著收益 — 需要从 method/application paper 重构为 analysis/measurement paper
核心假设：['exp-003 解码消融: K* 在不同解码策略间变化剧烈（greedy K*=1, high-temp K*=3），K*=2 不是 stable property 而是特定配置的 artifact', 'exp-004 7B: K*=1（更强模型的递归文本更快趋同，1v2 AUC CI upper < 0.60）', 'exp-006 graduated filtering: graduated − binary < 0.5pp，p > 0.10（不显著）', 'exp-015 learned features: frozen embedding+MLP 优于 hand-crafted ≥ 10pp（hand-crafted features 不够用）', 'Qwen-cont 在更严格测试（e.g., 不同 seed 的 depth chain）中 1v2 CI lower 跌破 0.60']
关键指标范围：{'auc_1v2_continuation_new_configs': [0.55, 0.62], 'auc_1v2_7B': [0.53, 0.59], 'k_star_across_decoding': ['varies 1-3, no stable universal value'], 'graduated_minus_binary_delta_pp': [-0.5, 0.5], 'cross_model_transfer_retention_expanded': [0.7, 0.85], 'spearman_rho_degradation_new_configs': [0.7, 0.82], 'dsir_vs_graduated_delta_pp': [-1.0, 0.5], 'ordinal_accuracy_best_model': [0.35, 0.4]}
叙事方向：原始 framing 不可持续。C3 必须删除或降为 negative result 段落。C1' 从 "K*=2 is the  boundary" 重构为 "K* is configuration-dependent: we map the factors that govern it"。 论文变成 empirical analysis paper: "What Controls the Discriminability of Recursive  Synthetic Text?" 核心贡献变为 (1) DPI 理论框架 + K* 概念的形式化定义, (2) 首次系统测量  K* 随 model/scale/decoding/generation-mode 的变化图谱, (3) cross-model transfer  分析揭示 depth signal 的 text-intrinsic vs model-specific 分解。叙事转向: "practitioners  不能假设固定 K*，必须根据具体配置估计"。如果 learned features 远优于 hand-crafted， 需要承认 15D features 是 convenience baseline 而非 sufficient tool，加 future work  呼吁 learned approaches。目标: EMNLP 2026 Findings 或放弃 EMNLP 转投 AAAI 2027 (多 2 个月补实验)。审稿人可能评价 "interesting analysis but limited actionable contribution" → 需要在 related work 中强调 measurement paper 的 venue precedent。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-contamination

## paper_framing.md

# Paper Framing — gen-depth-contamination

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)
- Fallback: EMNLP 2026 Findings
- Backup: AAAI 2027 (abstract July 25, paper August 1)

## Canonical Experimental Condition

**Continuation mode 是 cross-model 结论的基础。**

> "We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons."

| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |
|-----------|-------------|-------------|---------|
| Continuation | 91-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |
| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |

**原则**：
- C1' 的跨模型 claim 必须基于 continuation mode 数据
- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据
- mvp-001 (Qwen-rewrite) 定位为 "pilot study demonstrating feasibility"，后续用 continuation mode rigorously validate
- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集

## Core Claims (2+1 结构, D012)

### Primary: C1' (K* Characterization)
首次系统测量递归合成文本的 generational discrimination boundary K*。

DPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 4-model × 2-mode 实验矩阵系统表征 K*_empirical 的行为，包括跨模型一致性、特征退化排序、以及 generation mode 对 depth signal 的调控效应。

**子组件：**

**(a) K* = 2 across all tested configurations**
> 4-model 1v2 bootstrap 95% CI 汇总：
> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |
> |-------|---------|--------|-----------------|
> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |
> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |
> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |
> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |
>
> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002
> - K* 不是离散跳变值，而是 CI-bounded continuum threshold
> - Paper 可写："K*=2 (bootstrap 95% CI for AUC₁ᵥ₂ > 0.60 across all four model configurations; AUC₂ᵥ₃ CI upper < 0.60)"

**(b) Cross-model transfer**
> - Pythia↔OLMo 91% accuracy retention → K*=2 不是 model self-familiarity artifact
> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移
> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）
> - depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity

**(c) Degradation ordering consistency**
> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）
> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std
> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）
> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）

**(d) Generation mode analysis (§4.x Analysis subsection)**
> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）
> - Transferability: continuation 80-92% retention vs rewrite 61-63%
> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集
> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性
> - 论文定位：Analysis subsection（"How does generation mode affect depth estimation?"），不是独立 claim

### Secondary: C3 (Graduated Filtering)
即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+ 三级）下，K*-aware graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。

### Supporting Analysis: Canonical Condition Selection
Generation mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。

## Story Spine

- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。
- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**
- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者"在什么深度以下，depth-aware curation 比 binary detection 更有价值"。通过 4-model × 2-mode 实验矩阵系统表征 K*，揭示控制因素（模型架构、解码策略、generation mode），为数据治理提供 actionable guidance。
- **Headline result template**: "We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with depth features that are 70-85% text-intrinsic (Pythia↔OLMo 91% transfer retention). Even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag."

## Anticipated Reviewer Concerns & Responses

1. **"K*=2 太浅，graduated filtering 收益有限"** → K* 是模型/解码策略依赖的；展示不同解码策略如何调控 K*（exp-003）；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated（exp-006）
2. **"只是 feature engineering + off-the-shelf classifier，方法贡献弱"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ generation mode analysis，不是分类器本身
3. **"Prompt-chain 不代表真实世界递归污染"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法
4. **"单模型/单数据集，泛化性不够"** → 3 个模型族 × 2 种 generation mode + 4×4 cross-model transfer matrix
5. **"同模型做生成和 surprisal 计算有 bias"** → **exp-013 直接反驳**：Pythia↔OLMo 91% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity
6. **"为什么不用 learned representations"** → 作为 baseline 对比；hand-crafted features 更 interpretable 且支持 degradation ordering 分析
7. **"Graduated filtering 没和 data selection methods 比"** → exp-006 包含 DSIR baseline + α sensitivity sweep
8. **"K* 的统计不确定性未量化"** → 4-model bootstrap CI + permutation test（exp-007）

## Venue Fit

- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作
- 2+1 claim 结构：C1' 是 comprehensive characterization study，C3 是 practical application，generation mode analysis 增加深度
- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization + transfer analysis 的 novelty


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,
    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_001_pythia_depth
  status: DONE
  conclusion: success
  metrics:
    pairwise_auc:
      0v1: 0.9932
      1v2: 0.6539
      2v3: 0.5515
      3v4: 0.5153
      4v5: 0.5135
    pairwise_auc_std:
      0v1: 0.0007
      1v2: 0.0069
      2v3: 0.0137
      3v4: 0.0084
      4v5: 0.0078
    pairwise_jsd:
      0v1: 0.2142
      1v2: 0.014
      2v3: 0.0051
      3v4: 0.0033
      4v5: 0.0031
    k_star: 2
    ordinal_mae: 1.14
    ordinal_accuracy: 0.383
- id: exp-002
  claim: 1
  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,
    C4 5K docs, depth 0-5.'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_002_olmo_depth
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.997
      1v2: 0.6146
      2v3: 0.5497
      3v4: 0.509
      4v5: 0.5044
    pairwise_auc_std:
      0v1: 0.0004
      1v2: 0.0029
      2v3: 0.004
      3v4: 0.0084
      4v5: 0.0136
    pairwise_jsd:
      0v1: 0.23941
      1v2: 0.012972
      2v3: 0.00735
      3v4: 0.003968
      4v5: 0.003851
    ordinal_mae: 1.1813
    ordinal_accuracy: 0.3685
    top_features:
    - surp_d1_mean
    - surp_d1_skew
    - freq_kurtosis
    - surp_d2_mean
    - surp_mean
- id: exp-003
  claim:
  - 1
  - 3
  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9
    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'
  priority: P0
  gpu_budget_hours: 20
  deps: []
  registry_id: exp_003_decoding_ablation
  status: RUNNING
- id: exp-004
  claim: 1
  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth
    0-3. 测试 K* 是否随模型规模变化。'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: null
  status: planned
- id: exp-005
  claim: 2
  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth
    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制
    degradation ordering heatmap。'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  - exp-002
  registry_id: exp_005_degradation
  status: DONE
  conclusion: success
  metrics:
    cross_model_kendall_tau_by_first_auc:
      Pythia_vs_OLMo: 0.733
      Pythia_vs_Qwen_rewrite: 0.467
      Pythia_vs_Qwen_cont: 0.695
      OLMo_vs_Qwen_rewrite: 0.429
      OLMo_vs_Qwen_cont: 0.543
      Qwen_rewrite_vs_Qwen_cont: 0.733
    cross_model_kendall_tau_by_avg_auc:
      Pythia_vs_OLMo: 0.8476
      Pythia_vs_Qwen_cont: 0.7524
      OLMo_vs_Qwen_cont: 0.6762
    cross_model_spearman_rho_single_feature_auc:
      Pythia_vs_OLMo: 0.95
      Pythia_vs_Qwen_cont: 0.9143
      OLMo_vs_Qwen_cont: 0.85
      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently
        classifies depth pairs)
    4model_tau_mean_continuation_by_first_auc: 0.657
    4model_tau_mean_all_by_first_auc: 0.6
    generation_mode_delta:
      Pythia_vs_Qwen: '+0.228'
      OLMo_vs_Qwen: '+0.114'
    top3_features_ranking_by_first_auc:
      Pythia:
      - surp_d1_std
      - surp_d2_std
      - surp_std
      OLMo:
      - surp_std
      - surp_d1_std
      - surp_d2_std
      Qwen_rewrite:
      - freq_entropy
      - surp_std
      - surp_d1_std
      Qwen_cont:
      - surp_d1_std
      - surp_std
      - surp_d2_std
    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all
      architectures (single-feature AUC ranking)
    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature
      AUC ranking under controlled generation mode.
    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower
      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture
    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),
      near-generational feature importance ordering varies more across models
- id: exp-006
  claim: 3
  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter
    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)
    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness
    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α
    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated
    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'
  priority: P0
  gpu_budget_hours: 72
  deps: []
  registry_id: null
  status: planned
- id: exp-007
  claim:
  - 1
  - 2
  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算
    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为
    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation
    test + 3-class metrics]'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  - exp-002
  - exp-003
  registry_id: exp_007_bootstrap_ci
  status: DONE
  conclusion: success
  metrics:
    qwen_rewrite:
      0v1:
        auc: 0.9956
        ci_lower: 0.9946
        ci_upper: 0.9965
        perm_p: 0.002
      1v2:
        auc: 0.6955
        ci_lower: 0.6859
        ci_upper: 0.7041
        perm_p: 0.002
      2v3:
        auc: 0.5893
        ci_lower: 0.5795
        ci_upper: 0.5991
        perm_p: 0.002
      3v4:
        auc: 0.5435
        ci_lower: 0.5333
        ci_upper: 0.5551
        perm_p: 0.002
      4v5:
        auc: 0.534
        ci_lower: 0.5238
        ci_upper: 0.5448
        perm_p: 0.002
    pythia_cont:
      0v1:
        auc: 0.9932
        ci_lower: 0.9921
        ci_upper: 0.9943
        perm_p: 0.002
      1v2:
        auc: 0.6539
        ci_lower: 0.6454
        ci_upper: 0.663
        perm_p: 0.002
      2v3:
        auc: 0.5514
        ci_lower: 0.5417
        ci_upper: 0.5628
        perm_p: 0.002
      3v4:
        auc: 0.5152
        ci_lower: 0.5041
        ci_upper: 0.526
        perm_p: 0.006
      4v5:
        auc: 0.5136
        ci_lower: 0.5021
        ci_upper: 0.5249
        perm_p: 0.008
    olmo_cont:
      0v1:
        auc: 0.997
        ci_lower: 0.9964
        ci_upper: 0.9975
        perm_p: 0.002
      1v2:
        auc: 0.6145
        ci_lower: 0.6045
        ci_upper: 0.6247
        perm_p: 0.002
      2v3:
        auc: 0.5496
        ci_lower: 0.5399
        ci_upper: 0.5596
        perm_p: 0.002
      3v4:
        auc: 0.5091
        ci_lower: 0.4973
        ci_upper: 0.52
        perm_p: 0.064
      4v5:
        auc: 0.5045
        ci_lower: 0.4932
        ci_upper: 0.515
        perm_p: 0.232
    qwen_cont:
      0v1:
        auc: 0.9972
        ci_lower: null
        ci_upper: null
        perm_p: null
      1v2:
        auc: 0.6112
        ci_lower: 0.6015
        ci_upper: 0.6213
        perm_p: 0.002
      2v3:
        auc: 0.5609
        ci_lower: 0.5511
        ci_upper: 0.5712
        perm_p: 0.002
      3v4:
        auc: 0.5409
        ci_lower: 0.5308
        ci_upper: 0.5508
        perm_p: 0.002
      4v5:
        auc: 0.5141
        ci_lower: 0.5035
        ci_upper: 0.5255
        perm_p: 0.006
    k_star_robust: true
    all_1v2_ci_lower_above_060: true
    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold
- id: exp-008
  claim: 1
  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),
    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'
  priority: P1
  gpu_budget_hours: 8
  deps:
  - exp-001
  registry_id: null
  status: planned
- id: exp-009
  claim: 3
  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试
    graduated vs binary filtering 的收益差异。'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - exp-006
  registry_id: null
  status: planned
- id: exp-010
  claim:
  - 1
  - 2
  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs
    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-005
  registry_id: exp_010_ordinal_baseline
  status: DONE
  conclusion: success
  metrics:
    qwen_rewrite:
      obd_lgbm:
        accuracy: 0.4229
        mae: 0.9836
        tau_b: 0.5518
        mean_pw_auc: 0.6214
      multiclass_lgbm:
        accuracy: 0.4182
        mae: 1.0163
        tau_b: 0.5367
        mean_pw_auc: 0.6246
      ordinal_logreg:
        accuracy: 0.3636
        mae: 0.9105
        tau_b: 0.563
        mean_pw_auc: 0.5022
    pythia:
      obd_lgbm:
        accuracy: 0.3856
        mae: 1.1072
        tau_b: 0.4745
        mean_pw_auc: 0.6055
      multiclass_lgbm:
        accuracy: 0.3832
        mae: 1.1399
        tau_b: 0.4622
        mean_pw_auc: 0.6062
      ordinal_logreg:
        accuracy: 0.3179
        mae: 1.022
        tau_b: 0.49
        mean_pw_auc: 0.4767
    olmo:
      obd_lgbm:
        accuracy: 0.3822
        mae: 1.1469
        tau_b: 0.4683
        mean_pw_auc: 0.6015
      multiclass_lgbm:
        accuracy: 0.3685
        mae: 1.1813
        tau_b: 0.4497
        mean_pw_auc: 0.5974
      ordinal_logreg:
        accuracy: 0.3265
        mae: 1.0352
        tau_b: 0.4656
        mean_pw_auc: 0.4859
- id: exp-011
  claim: 1
  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth
    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'
  priority: P1
  gpu_budget_hours: 0
  deps: []
  registry_id: null
  status: planned
- id: exp-012
  claim: 1
  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score
    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'
  priority: P1
  gpu_budget_hours: 3
  deps:
  - exp-001
  - exp-002
  registry_id: null
  status: planned
- id: exp-013
  claim:
  - 1
  - 2
  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001
    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier
    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是
    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  - exp-002
  - exp-017
  registry_id: exp_013_cross_transfer
  status: DONE
  conclusion: success
  metrics:
    accuracy_matrix:
      Qwen_rw→Qwen_rw: 0.4229
      Qwen_rw→Pythia: 0.259
      Qwen_rw→OLMo: 0.2653
      Qwen_rw→Qwen_cont: 0.3466
      Pythia→Qwen_rw: 0.2718
      Pythia→Pythia: 0.3856
      Pythia→OLMo: 0.3531
      Pythia→Qwen_cont: 0.3287
      OLMo→Qwen_rw: 0.2768
      OLMo→Pythia: 0.345
      OLMo→OLMo: 0.3822
      OLMo→Qwen_cont: 0.3244
      Qwen_cont→Qwen_rw: 0.344
      Qwen_cont→Pythia: 0.3284
      Qwen_cont→OLMo: 0.3112
      Qwen_cont→Qwen_cont: 0.3875
    transfer_retention_accuracy:
      Pythia↔OLMo: 91-92%
      Qwen_rw→Pythia/OLMo: 61-63%
      Qwen_cont↔Pythia: 83-85%
      Qwen_cont↔OLMo: 80-85%
    transfer_retention_tau:
      Pythia↔OLMo: 85-86%
      Qwen_rw→Pythia/OLMo: 45-50%
      Qwen_cont↔others: 68-83%
    mean_pw_auc_matrix:
      within_avg: 0.6099
      cross_avg: 0.5905
      0v1_cross_all_above: 0.96
    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.
      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained
      depth transfer depends on model family similarity. Qwen-rewrite overfits style
      features; Qwen-cont transfers much better.
- id: exp-014
  claim: 1
  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth
    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'
  priority: P2
  gpu_budget_hours: 8
  deps:
  - exp-005
  registry_id: null
  status: planned
- id: exp-015
  claim: 1
  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +
    MLP vs hand-crafted 15D features，验证 interpretable features 的价值。[Dream worst tier
    flagged as critical for "data-intrinsic ceiling" claim — 需要 stronger probe 才能支撑该
    claim]'
  priority: P1
  gpu_budget_hours: 3
  deps: []
  registry_id: null
  status: planned
- id: exp-016
  claim: 1
  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的
    K* 和特征分布差异。'
  priority: P1
  gpu_budget_hours: 6
  deps: []
  registry_id: null
  status: planned
- id: exp-017
  claim:
  - 1
  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,
    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model
    对 K* 的影响。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_017_qwen_continuation
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.9972
      1v2: 0.6114
      2v3: 0.5609
      3v4: 0.5408
      4v5: 0.5139
    pairwise_jsd:
      0v1: 0.28627
      1v2: 0.005107
      2v3: 0.003603
      3v4: 0.003395
      4v5: 0.003085
    ordinal_mae: 1.1547
    ordinal_accuracy: 0.3819
    top3_features:
    - freq_entropy
    - surp_mean
    - surp_std
- id: mvp-001
  claim:
  - 1
  - 2
  - 3
  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,
    nucleus p=0.95 T=1.0, depth 0-5.'
  priority: P0
  gpu_budget_hours: 12
  deps: []
  registry_id: mvp_pilot_sat_v1
  status: DONE
  conclusion: success
  metrics:
    pairwise_auc:
      0v1: 0.9956
      1v2: 0.6957
      2v3: 0.5893
      3v4: 0.5434
      4v5: 0.5343
    pairwise_auc_std:
      0v1: 0.0005
      1v2: 0.0072
      2v3: 0.012
      3v4: 0.0053
      4v5: 0.0091
    pairwise_jsd:
      0v1: 0.2669
      1v2: 0.0163
      2v3: 0.0069
      3v4: 0.0047
      4v5: 0.0041
    k_star: 2
    ordinal_mae: 1.0163
    ordinal_accuracy: 0.4182


## registry (completed experiments)

- exp_id: mvp_pilot_sat_v1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pairwise_auc:
      0v1: 0.9956
      1v2: 0.6957
      2v3: 0.5893
      3v4: 0.5434
      4v5: 0.5343
    pairwise_auc_std:
      0v1: 0.0005
      1v2: 0.0072
      2v3: 0.012
      3v4: 0.0053
      4v5: 0.0091
    pairwise_jsd:
      0v1: 0.2669
      1v2: 0.0163
      2v3: 0.0069
      3v4: 0.0047
      4v5: 0.0041
    k_star: 2
    ordinal_mae: 1.0163
    ordinal_accuracy: 0.4182
- exp_id: exp_001_pythia_depth
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pairwise_auc:
      0v1: 0.9932
      1v2: 0.6539
      2v3: 0.5515
      3v4: 0.5153
      4v5: 0.5135
    pairwise_auc_std:
      0v1: 0.0007
      1v2: 0.0069
      2v3: 0.0137
      3v4: 0.0084
      4v5: 0.0078
    pairwise_jsd:
      0v1: 0.2142
      1v2: 0.014
      2v3: 0.0051
      3v4: 0.0033
      4v5: 0.0031
    k_star: 2
    ordinal_mae: 1.14
    ordinal_accuracy: 0.383
- exp_id: exp_002_olmo_depth
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.997
      1v2: 0.6146
      2v3: 0.5497
      3v4: 0.509
      4v5: 0.5044
    pairwise_auc_std:
      0v1: 0.0004
      1v2: 0.0029
      2v3: 0.004
      3v4: 0.0084
      4v5: 0.0136
    pairwise_jsd:
      0v1: 0.23941
      1v2: 0.012972
      2v3: 0.00735
      3v4: 0.003968
      4v5: 0.003851
    ordinal_mae: 1.1813
    ordinal_accuracy: 0.3685
    top_features:
    - surp_d1_mean
    - surp_d1_skew
    - freq_kurtosis
    - surp_d2_mean
    - surp_mean
- exp_id: exp_003_decoding_ablation
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_017_qwen_continuation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.9972
      1v2: 0.6114
      2v3: 0.5609
      3v4: 0.5408
      4v5: 0.5139
    pairwise_jsd:
      0v1: 0.28627
      1v2: 0.005107
      2v3: 0.003603
      3v4: 0.003395
      4v5: 0.003085
    ordinal_mae: 1.1547
    ordinal_accuracy: 0.3819
    top3_features:
    - freq_entropy
    - surp_mean
    - surp_std
- exp_id: exp_013_cross_transfer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy_matrix:
      Qwen_rw→Qwen_rw: 0.4229
      Qwen_rw→Pythia: 0.259
      Qwen_rw→OLMo: 0.2653
      Qwen_rw→Qwen_cont: 0.3466
      Pythia→Qwen_rw: 0.2718
      Pythia→Pythia: 0.3856
      Pythia→OLMo: 0.3531
      Pythia→Qwen_cont: 0.3287
      OLMo→Qwen_rw: 0.2768
      OLMo→Pythia: 0.345
      OLMo→OLMo: 0.3822
      OLMo→Qwen_cont: 0.3244
      Qwen_cont→Qwen_rw: 0.344
      Qwen_cont→Pythia: 0.3284
      Qwen_cont→OLMo: 0.3112
      Qwen_cont→Qwen_cont: 0.3875
    transfer_retention_accuracy:
      Pythia↔OLMo: 91-92%
      Qwen_rw→Pythia/OLMo: 61-63%
      Qwen_cont↔Pythia: 83-85%
      Qwen_cont↔OLMo: 80-85%
    transfer_retention_tau:
      Pythia↔OLMo: 85-86%
      Qwen_rw→Pythia/OLMo: 45-50%
      Qwen_cont↔others: 68-83%
    mean_pw_auc_matrix:
      within_avg: 0.6099
      cross_avg: 0.5905
      0v1_cross_all_above: 0.96
    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.
      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained
      depth transfer depends on model family similarity. Qwen-rewrite overfits style
      features; Qwen-cont transfers much better.
- exp_id: exp_005_degradation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cross_model_kendall_tau_by_first_auc:
      Pythia_vs_OLMo: 0.733
      Pythia_vs_Qwen_rewrite: 0.467
      Pythia_vs_Qwen_cont: 0.695
      OLMo_vs_Qwen_rewrite: 0.429
      OLMo_vs_Qwen_cont: 0.543
      Qwen_rewrite_vs_Qwen_cont: 0.733
    cross_model_kendall_tau_by_avg_auc:
      Pythia_vs_OLMo: 0.8476
      Pythia_vs_Qwen_cont: 0.7524
      OLMo_vs_Qwen_cont: 0.6762
    cross_model_spearman_rho_single_feature_auc:
      Pythia_vs_OLMo: 0.95
      Pythia_vs_Qwen_cont: 0.9143
      OLMo_vs_Qwen_cont: 0.85
      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently
        classifies depth pairs)
    4model_tau_mean_continuation_by_first_auc: 0.657
    4model_tau_mean_all_by_first_auc: 0.6
    generation_mode_delta:
      Pythia_vs_Qwen: '+0.228'
      OLMo_vs_Qwen: '+0.114'
    top3_features_ranking_by_first_auc:
      Pythia:
      - surp_d1_std
      - surp_d2_std
      - surp_std
      OLMo:
      - surp_std
      - surp_d1_std
      - surp_d2_std
      Qwen_rewrite:
      - freq_entropy
      - surp_std
      - surp_d1_std
      Qwen_cont:
      - surp_d1_std
      - surp_std
      - surp_d2_std
    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all
      architectures (single-feature AUC ranking)
    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature
      AUC ranking under controlled generation mode.
    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower
      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture
    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),
      near-generational feature importance ordering varies more across models
- exp_id: exp_007_bootstrap_ci
  name: ''
  status: DONE
  conclusion: success
  metrics:
    qwen_rewrite:
      0v1:
        auc: 0.9956
        ci_lower: 0.9946
        ci_upper: 0.9965
        perm_p: 0.002
      1v2:
        auc: 0.6955
        ci_lower: 0.6859
        ci_upper: 0.7041
        perm_p: 0.002
      2v3:
        auc: 0.5893
        ci_lower: 0.5795
        ci_upper: 0.5991
        perm_p: 0.002
      3v4:
        auc: 0.5435
        ci_lower: 0.5333
        ci_upper: 0.5551
        perm_p: 0.002
      4v5:
        auc: 0.534
        ci_lower: 0.5238
        ci_upper: 0.5448
        perm_p: 0.002
    pythia_cont:
      0v1:
        auc: 0.9932
        ci_lower: 0.9921
        ci_upper: 0.9943
        perm_p: 0.002
      1v2:
        auc: 0.6539
        ci_lower: 0.6454
        ci_upper: 0.663
        perm_p: 0.002
      2v3:
        auc: 0.5514
        ci_lower: 0.5417
        ci_upper: 0.5628
        perm_p: 0.002
      3v4:
        auc: 0.5152
        ci_lower: 0.5041
        ci_upper: 0.526
        perm_p: 0.006
      4v5:
        auc: 0.5136
        ci_lower: 0.5021
        ci_upper: 0.5249
        perm_p: 0.008
    olmo_cont:
      0v1:
        auc: 0.997
        ci_lower: 0.9964
        ci_upper: 0.9975
        perm_p: 0.002
      1v2:
        auc: 0.6145
        ci_lower: 0.6045
        ci_upper: 0.6247
        perm_p: 0.002
      2v3:
        auc: 0.5496
        ci_lower: 0.5399
        ci_upper: 0.5596
        perm_p: 0.002
      3v4:
        auc: 0.5091
        ci_lower: 0.4973
        ci_upper: 0.52
        perm_p: 0.064
      4v5:
        auc: 0.5045
        ci_lower: 0.4932
        ci_upper: 0.515
        perm_p: 0.232
    qwen_cont:
      0v1:
        auc: 0.9972
        ci_lower: null
        ci_upper: null
        perm_p: null
      1v2:
        auc: 0.6112
        ci_lower: 0.6015
        ci_upper: 0.6213
        perm_p: 0.002
      2v3:
        auc: 0.5609
        ci_lower: 0.5511
        ci_upper: 0.5712
        perm_p: 0.002
      3v4:
        auc: 0.5409
        ci_lower: 0.5308
        ci_upper: 0.5508
        perm_p: 0.002
      4v5:
        auc: 0.5141
        ci_lower: 0.5035
        ci_upper: 0.5255
        perm_p: 0.006
    k_star_robust: true
    all_1v2_ci_lower_above_060: true
    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold
- exp_id: exp_010_ordinal_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    qwen_rewrite:
      obd_lgbm:
        accuracy: 0.4229
        mae: 0.9836
        tau_b: 0.5518
        mean_pw_auc: 0.6214
      multiclass_lgbm:
        accuracy: 0.4182
        mae: 1.0163
        tau_b: 0.5367
        mean_pw_auc: 0.6246
      ordinal_logreg:
        accuracy: 0.3636
        mae: 0.9105
        tau_b: 0.563
        mean_pw_auc: 0.5022
    pythia:
      obd_lgbm:
        accuracy: 0.3856
        mae: 1.1072
        tau_b: 0.4745
        mean_pw_auc: 0.6055
      multiclass_lgbm:
        accuracy: 0.3832
        mae: 1.1399
        tau_b: 0.4622
        mean_pw_auc: 0.6062
      ordinal_logreg:
        accuracy: 0.3179
        mae: 1.022
        tau_b: 0.49
        mean_pw_auc: 0.4767
    olmo:
      obd_lgbm:
        accuracy: 0.3822
        mae: 1.1469
        tau_b: 0.4683
        mean_pw_auc: 0.6015
      multiclass_lgbm:
        accuracy: 0.3685
        mae: 1.1813
        tau_b: 0.4497
        mean_pw_auc: 0.5974
      ordinal_logreg:
        accuracy: 0.3265
        mae: 1.0352
        tau_b: 0.4656
        mean_pw_auc: 0.4859

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
  "promptId": "cfc43da9-f778-4747-ba9c-0eafc9e1f869",
  "type": "user",
  "uuid": "1e8874e6-a827-44e4-9009-0ecaae1d6d60",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T08:31:38.645Z_

```json
{
  "parentUuid": "1e8874e6-a827-44e4-9009-0ecaae1d6d60",
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
  "uuid": "233d99da-e38e-4fd6-89c4-d0fa6c1c4c73",
  "timestamp": "2026-05-13T08:31:38.645Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T08:31:38.645Z_

```json
{
  "parentUuid": "233d99da-e38e-4fd6-89c4-d0fa6c1c4c73",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "890a7645-16c6-4ff9-a95f-02275b5022ba",
  "timestamp": "2026-05-13T08:31:38.645Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：K*=2 universality 被打破 + C3 无显著收益 — 需要从 method/application paper 重构为 analysis/measurement paper 核心假设：['exp-003 解码消融: K* 在不同解码策略间变化剧烈（greedy K*=1, high-temp…",
  "leafUuid": "890a7645-16c6-4ff9-a95f-02275b5022ba",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Recursive synthetic text depth estimation characterization study",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83"
}
```

---

### Assistant

_source line 8 · 2026-05-13T08:35:19.661Z_

我来基于 worst 档的定义，为所有 planned 实验生成详细预测数据。

```yaml
tier: worst
narrative_guidance: >
  K*=2 universality 被 exp-003 和 exp-004 打破：greedy 下 K*=1，high-temp 下 K*=3，7B 模型
  K*=1。K* 不再是 stable universal property，而是 configuration-dependent artifact。C3 graduated
  filtering 无显著收益（Δ<0.5pp, p>0.10），必须删除或降为 negative result。论文从 method/application
  paper 重构为 empirical analysis paper："What Controls the Discriminability of Recursive
  Synthetic Text?" 核心贡献变为 DPI 框架 + K* 变化图谱 + text-intrinsic vs model-specific 分解。
  Learned features 远优于 hand-crafted（≥10pp），承认 15D features 是 convenience baseline。
  目标降级至 EMNLP 2026 Findings 或转投 AAAI 2027。

imagined_experiments:
  # ============================================================
  # exp-003: Decoding strategy ablation (RUNNING → 预测结果)
  # ============================================================
  - name: "Decoding strategy ablation"
    plan_id: "exp-003"
    description: >
      Qwen2.5-1.5B 在 greedy / nucleus p=0.9 / T=0.7 / T=1.2 四种解码策略下的 depth chain，
      测试 K* 是否随解码策略剧烈变化。
    expected_results:
      greedy:
        0v1_auc: 0.999
        1v2_auc: 0.572
        1v2_ci_lower: 0.563
        1v2_ci_upper: 0.581
        2v3_auc: 0.538
        k_star: 1
        k_star_note: "1v2 CI upper < 0.60 → K*=1"
      nucleus_p09:
        0v1_auc: 0.996
        1v2_auc: 0.628
        1v2_ci_lower: 0.618
        1v2_ci_upper: 0.637
        2v3_auc: 0.554
        k_star: 2
      temp_07:
        0v1_auc: 0.998
        1v2_auc: 0.591
        1v2_ci_lower: 0.581
        1v2_ci_upper: 0.601
        2v3_auc: 0.546
        k_star: "ambiguous (CI straddles 0.60)"
      temp_12:
        0v1_auc: 0.992
        1v2_auc: 0.683
        1v2_ci_lower: 0.673
        1v2_ci_upper: 0.694
        2v3_auc: 0.612
        2v3_ci_lower: 0.602
        2v3_ci_upper: 0.623
        3v4_auc: 0.558
        k_star: 3
      k_star_across_decoding: "varies 1-3, no stable universal value"
      spearman_rho_feature_ranking_across_decoding: 0.78
    result_rationale: >
      Greedy 解码消除了采样随机性，每轮生成的 output 几乎是确定性函数，递归 chain 极快收敛到模型的
      mode distribution。Gen-1 已经高度确定性，gen-2 与 gen-1 的统计差异极小，因此 1v2 AUC 跌破 0.60，
      K*=1。反之 T=1.2 放大了采样噪声，每轮生成引入更多随机变异，递归收敛被延缓——文本的统计 fingerprint
      在更多代际间保持可区分性，2v3 也能超过 0.60 阈值，K*=3。Nucleus p=0.9 比 p=0.95（baseline）
      略收窄采样空间但效果接近，K* 仍为 2。T=0.7 处于边缘——sampling entropy 降低但未降到 greedy 程度，
      1v2 CI 横跨 0.60。这证明 K* 不是模型的固有属性，而是解码配置控制的 operational parameter。
      Feature ranking 的 Spearman ρ 从 baseline 的 0.85+ 降到 0.78，因为 greedy/low-temp 下
      surprisal variance 系列特征的 discriminative power 被压缩（分布更窄），tail-thinning 特征
      相对重要性上升。
    tables:
      - name: "Table: K* as a function of decoding strategy"
        columns: ["Decoding", "K*", "AUC 1v2", "95% CI", "AUC 2v3", "AUC 3v4"]
        rows:
          - ["Greedy", 1, 0.572, "[0.563, 0.581]", 0.538, 0.512]
          - ["Nucleus p=0.9", 2, 0.628, "[0.618, 0.637]", 0.554, 0.517]
          - ["Nucleus p=0.95 (baseline)", 2, 0.611, "[0.602, 0.621]", 0.561, 0.541]
          - ["T=0.7", "1-2", 0.591, "[0.581, 0.601]", 0.546, 0.519]
          - ["T=1.2", 3, 0.683, "[0.673, 0.694]", 0.612, 0.558]
    figures_description:
      - "Heatmap: K* (y-axis) × decoding strategy (x-axis)，展示 K* 从 1 到 3 的连续变化"
      - "Line plot: AUC decay curve per decoding strategy，展示不同解码下的衰减速率差异"
    analysis: >
      K*=2 universality 被打破。K* 是解码策略的单调递增函数（近似）：更高的 sampling entropy → 更慢的
      递归收敛 → 更大的 K*。这从根本上改变了论文叙事——不能再 claim "K*=2 is the boundary"，必须说
      "K* is configuration-dependent and we map the controlling factors"。对 C3 的打击：
      如果 K* 本身不稳定，graduated filtering 的 ordinal signal 基础就不牢固。Positive spin：
      这是首次系统揭示 K* 与解码策略的依赖关系，是 measurement paper 的核心贡献之一。

  # ============================================================
  # exp-004: Cross-scale probe (7B)
  # ============================================================
  - name: "Cross-scale probe: Qwen2.5-7B"
    plan_id: "exp-004"
    description: >
      Qwen2.5-7B continuation mode, C4 1K docs, depth 0-3，测试 K* 是否随模型规模变化。
    expected_results:
      0v1_auc: 0.999
      1v2_auc: 0.577
      1v2_ci_lower: 0.558
      1v2_ci_upper: 0.596
      2v3_auc: 0.529
      2v3_ci_lower: 0.510
      2v3_ci_upper: 0.548
      k_star: 1
      ordinal_accuracy: 0.36
      ordinal_mae: 0.98
      top3_features: ["surp_d1_std", "surp_std", "freq_entropy"]
      spearman_rho_vs_1_5B: 0.82
    result_rationale: >
      7B 模型的 next-token prediction 能力显著强于 1.5B，continuation 生成的文本更"像"原始文本——
      更低的 perplexity、更准确的 style matching。递归 chain 中，gen-1 已经非常接近原始文本的统计分布，
      gen-2 与 gen-1 的差异极小。信息论上，更强的模型意味着 channel capacity 更高（每轮损耗更小），
      DPI 约束下的收敛更快。1v2 AUC CI upper < 0.60 → K*=1。注意 1K docs（vs 5K）导致 CI 更宽
      （±0.019 vs ±0.010），但即使 upper bound 0.596 仍低于 0.60。这与 worst tier 假设一致：
      更强模型的递归文本更快趋同，K*=2 不是 scale-invariant property。Feature ranking 与 1.5B
      保持较高一致性（ρ=0.82），因为 degradation 的物理机制相同（信息压缩），只是速率不同。
    tables:
      - name: "Table: Scale effect on K*"
        columns: ["Model", "Scale", "K*", "AUC 1v2", "95% CI", "AUC 2v3"]
        rows:
          - ["Qwen2.5-1.5B (cont)", "1.5B", 2, 0.611, "[0.602, 0.621]", 0.561]
          - ["Qwen2.5-7B (cont)", "7B", 1, 0.577, "[0.558, 0.596]", 0.529]
    figures_description:
      - "Bar chart: 1v2 AUC with 95% CI for 1.5B vs 7B，threshold line at 0.60"
      - "AUC decay curve overlay: 1.5B vs 7B，展示 7B 的更快衰减"
    analysis: >
      K* 随模型规模递减。这与 DPI 框架完全一致——更强的 channel（更大模型）每轮信息损耗更小，
      递归输出更快趋同于 stationary distribution。但这也意味着论文必须放弃 "K*=2 across scales"
      的 universal claim。Positive spin：首次揭示 scale-K* 关系，对 practitioners 有直接指导意义
      （"用更大模型生成的合成数据更难做 depth estimation"）。需要在 1K docs 的 smaller sample size
      下谨慎表述 CI。

  # ============================================================
  # exp-006: Downstream filtering evaluation
  # ============================================================
  - name: "Downstream filtering evaluation"
    plan_id: "exp-006"
    description: >
      六种 filtering 策略（no-filter / binary-ours / binary-Drayson / graduated / surprisal-based
      / DSIR）在 continued pretraining + lm-eval-harness 上的对比。5 seeds paired t-test。
      α sensitivity sweep。
    expected_results:
      mmlu:
        no_filter: 25.8
        binary_ours: 26.4
        binary_drayson: 26.5
        graduated_alpha_01: 26.3
        graduated_alpha_03: 26.5
        graduated_alpha_05: 26.6
        graduated_alpha_07: 26.4
        graduated_alpha_09: 26.3
        surprisal_based: 26.2
        dsir: 26.8
      hellaswag:
        no_filter: 42.1
        binary_ours: 43.0
        binary_drayson: 43.2
        graduated_alpha_01: 42.9
        graduated_alpha_03: 43.1
        graduated_alpha_05: 43.2
        graduated_alpha_07: 43.0
        graduated_alpha_09: 42.8
        surprisal_based: 42.6
        dsir: 43.5
      graduated_minus_binary_delta_pp:
        mmlu: 0.2
        hellaswag: 0.2
        mean: 0.2
      graduated_vs_binary_paired_ttest_p:
        mmlu: 0.34
        hellaswag: 0.28
      dsir_vs_graduated_delta_pp:
        mmlu: 0.2
        hellaswag: 0.3
      best_alpha: 0.5
      alpha_sensitivity: "non-monotonic, peak at 0.5 but flat (range < 0.3pp)"
    result_rationale: >
      Graduated filtering 的理论优势在于利用 ordinal signal（human/gen-1/gen-2+）做更 calibrated
      的权重分配。但在 worst tier 下，这个优势被多个因素抵消：(1) K*=2 意味着 ordinal signal 只有 3 个
      有效等级（0/1/2+），graduated 退化为接近 binary 的判断——差异仅在于对 gen-1 赋予中间权重而非
      hard cutoff，但 gen-1 本身质量尚可（1v2 AUC 只有 0.61-0.69），过滤掉它的边际损失本就不大；
      (2) 15D hand-crafted features 的 ordinal accuracy 只有 ~0.38-0.42，depth 估计的噪声很大，
      graduated weighting 的"精细调控"被预测噪声淹没；(3) continued pretraining 对数据质量的
      sensitivity 在小 injection 比例下较低。结果 graduated - binary 仅 +0.2pp，paired t-test
      p > 0.10（5 seeds 下 power 不足以检测 <0.5pp 的差异）。DSIR 表现最好是因为它做分布匹配
      而非深度过滤，这是一种 complementary 而非 competing 的策略。α sweep 几乎 flat 说明
      graduated 的 weighting scheme 不 matter，因为 ordinal signal 本身太弱。
    tables:
      - name: "Table: Filtering strategy comparison (mean ± std over 5 seeds)"
        columns: ["Strategy", "MMLU", "HellaSwag", "Δ vs no-filter"]
        rows:
          - ["No filter", "25.8 ± 0.3", "42.1 ± 0.4", "—"]
          - ["Binary (ours)", "26.4 ± 0.3", "43.0 ± 0.3", "+0.75pp"]
          - ["Binary (Drayson)", "26.5 ± 0.3", "43.2 ± 0.4", "+0.9pp"]
          - ["Graduated (α=0.5)", "26.6 ± 0.4", "43.2 ± 0.4", "+0.95pp"]
          - ["Surprisal-based", "26.2 ± 0.3", "42.6 ± 0.3", "+0.45pp"]
          - ["DSIR", "26.8 ± 0.3", "43.5 ± 0.3", "+1.2pp"]
      - name: "Table: α sensitivity sweep (graduated filtering)"
        columns: ["α", "MMLU", "HellaSwag"]
        rows:
          - [0.1, 26.3, 42.9]
          - [0.3, 26.5, 43.1]
          - [0.5, 26.6, 43.2]
          - [0.7, 26.4, 43.0]
          - [0.9, 26.3, 42.8]
    figures_description:
      - "Bar chart: 六种策略的 MMLU/HellaSwag 得分 + error bars，graduated 和 binary 的 bars 几乎等高"
      - "Line plot: α sweep curve，几乎水平，展示 graduated weighting 的无效性"
    analysis: >
      C3 的核心 claim 被否定。graduated - binary < 0.5pp 且统计不显著（p > 0.10）。即使在 best α=0.5
      下，graduated 也仅比 binary 好 0.2pp。这不能支撑 "K*-aware graduated filtering outperforms
      binary" 的 claim。DSIR 反而是最好的，但它不 claim depth awareness。C3 必须删除或降为
      "we tested graduated filtering; the improvement was not statistically significant,
      consistent with the limited ordinal resolution at K*=2" 的 negative result 段落。
      论文的 practical contribution 因此大打折扣——从 "method + application" 退化为 "analysis only"。

  # ============================================================
  # exp-008: Retrain-chain ecological validity
  # ============================================================
  - name: "Retrain-chain ecological validity"
    plan_id: "exp-008"
    description: >
      Pythia-1.4B LoRA retrain-chain vs prompt-chain 的 K* 和特征分布对比。
    expected_results:
      retrain_chain:
        0v1_auc: 0.981
        1v2_auc: 0.593
        1v2_ci_lower: 0.583
        1v2_ci_upper: 0.604
        2v3_auc: 0.541
        k_star: "1 (CI upper = 0.604, marginally above 0.60 but inconsistent)"
      prompt_chain_reference:
        1v2_auc: 0.654
        k_star: 2
      feature_distribution_jsd_retrain_vs_prompt:
        gen1: 0.032
        gen2: 0.048
        gen3: 0.061
      spearman_rho_feature_ranking: 0.80
    result_rationale: >
      Retrain-chain 的递归机制与 prompt-chain 不同：模型参数本身被污染数据更新，而非仅通过 prompt
      传递。LoRA rank=16 的 fine-tuning 只更新少量参数，但每轮 retrain 会让模型的 generation
      distribution 更快收敛到自身输出的 stationary distribution（positive feedback loop 更紧密）。
      因此 retrain-chain 的代际差异衰减更快，1v2 AUC 低于 prompt-chain（0.593 vs 0.654）。
      在 worst tier 下，retrain-chain K*=1 进一步削弱 K*=2 的 universality——即使在同一模型、
      同一 scale 下，递归机制的不同就能改变 K*。Feature ranking 的一致性（ρ=0.80）说明
      degradation 的本质机制类似（都是信息压缩），但速率和 K* 因机制而异。这支持了 measurement paper
      的叙事："K* depends on the recursion mechanism, not just the model"。
    tables:
      - name: "Table: Prompt-chain vs Retrain-chain (Pythia-1.4B)"
        columns: ["Chain type", "K*", "AUC 0v1", "AUC 1v2", "AUC 2v3"]
        rows:
          - ["Prompt-chain", 2, 0.993, 0.654, 0.552]
          - ["Retrain-chain (LoRA)", 1, 0.981, 0.593, 0.541]
    figures_description:
      - "Feature distribution violin plots: prompt-chain vs retrain-chain at gen-1/2/3"
      - "AUC decay curve overlay for two chain types"
    analysis: >
      Retrain-chain 的 K* 更低，进一步证实 K* 是 configuration-dependent。但 retrain-chain 的
      ecological validity 更高（更接近真实 model collapse 场景），这意味着在最真实的场景下 K*
      可能更低。论文可以正面叙述："retrain-chain 的更快收敛与 model collapse 文献的预测一致"。
      但这也意味着 depth estimation 的 practical value 在 retrain 场景下更有限。

  # ============================================================
  # exp-009: Contamination dose-response
  # ============================================================
  - name: "Contamination dose-response"
    plan_id: "exp-009"
    description: >
      10%/30%/50% synthetic injection 比例下 graduated vs binary filtering 的收益差异。
    expected_results:
      injection_10pct:
        binary_mmlu: 25.9
        graduated_mmlu: 26.0
        delta_pp: 0.1
        p_value: 0.61
      injection_30pct:
        binary_mmlu: 26.4
        graduated_mmlu: 26.6
        delta_pp: 0.2
        p_value: 0.38
      injection_50pct:
        binary_mmlu: 26.2
        graduated_mmlu: 26.5
        delta_pp: 0.3
        p_value: 0.19
      hellaswag_pattern: "similar, delta_pp 0.1-0.4, all p > 0.10"
      dose_response_trend: "graduated advantage increases with injection ratio but never reaches significance"
    result_rationale: >
      即使 injection 比例增大（50%），graduated 的优势仍无法达到显著性，因为根本瓶颈不在 injection
      比例而在 ordinal signal 的分辨率。K*=2 限制了 ordinal signal 只有 3 个有效等级，而 depth
      estimator 在这 3 个等级上的 accuracy 只有 ~0.38-0.42。更高的 injection 比例放大了 filtering
      的绝对效果（binary 和 graduated 都比 no-filter 更好），但 graduated 相对 binary 的边际优势
      始终被估计噪声淹没。在 50% injection 下 delta 达到 0.3pp，但 5 seeds 的 variance 太大，
      p=0.19 仍不显著。要达到 p<0.05 可能需要 20+ seeds（不现实的 GPU budget）。这说明即使
      C3 在某种 asymptotic sense 下可能正确，在实际可操作的实验规模下也无法被证实。
    tables:
      - name: "Table: Dose-response (graduated − binary, pp)"
        columns: ["Injection %", "Δ MMLU", "Δ HellaSwag", "p-value (MMLU)"]
        rows:
          - ["10%", "+0.1", "+0.1", 0.61]
          - ["30%", "+0.2", "+0.2", 0.38]
          - ["50%", "+0.3", "+0.4", 0.19]
    figures_description:
      - "Line plot: graduated − binary delta (pp) vs injection ratio，带 confidence band"
    analysis: >
      Dose-response 趋势存在但从未达到显著性，进一步确认 C3 无法在本文中被支撑。
      可以作为 discussion 段落提及 "suggestive but underpowered trend"。

  # ============================================================
  # exp-011: LLM zero-shot depth estimation
  # ============================================================
  - name: "LLM zero-shot depth estimation baseline"
    plan_id: "exp-011"
    description: >
      GPT-4o / Claude 3.5 对 depth 0-4 文本做 zero-shot depth 判断。
    expected_results:
      gpt4o:
        accuracy: 0.23
        mae: 1.82
        tau_b: 0.12
        binary_0v1plus_auc: 0.71
      claude35:
        accuracy: 0.25
        mae: 1.74
        tau_b: 0.15
        binary_0v1plus_auc: 0.74
      random_baseline_accuracy: 0.20
      our_15D_accuracy: 0.38
    result_rationale: >
      LLM 的 zero-shot depth estimation 接近随机（accuracy 0.23-0.25 vs random 0.20），因为
      depth estimation 需要检测微妙的统计 fingerprint（surprisal 分布的高阶矩变化），而不是
      surface-level 的文本质量判断。LLM 可以做粗粒度的 "is this synthetic?" 判断（0v1+ AUC 0.71-0.74），
      但无法区分 gen-1 vs gen-2 vs gen-3 这种需要统计工具的细粒度差异。这验证了 depth estimation
      需要专门方法的 claim。但在 worst tier 下，即使我们的方法也只有 0.38 accuracy，LLM baseline
      的弱表现更多地证明了 "depth estimation is hard" 而非 "our method is strong"。
    tables:
      - name: "Table: Zero-shot LLM depth estimation"
        columns: ["Method", "Accuracy", "MAE", "τ_b", "Binary AUC"]
        rows:
          - ["Random", 0.20, 2.0, 0.0, 0.50]
          - ["GPT-4o zero-shot", 0.23, 1.82, 0.12, 0.71]
          - ["Claude 3.5 zero-shot", 0.25, 1.74, 0.15, 0.74]
          - ["Our 15D features", 0.38, 1.14, 0.47, 0.99]
    figures_description:
      - "Confusion matrix: LLM predictions vs true depth，展示 heavy diagonal blur"
    analysis: >
      LLM 不能做 depth estimation，但这主要证明任务本身难，不单独支撑我们方法的 novelty。
      在 analysis paper framing 下，这个实验定位为 "calibration of task difficulty"。

  # ============================================================
  # exp-012: Binary detector confidence as depth proxy
  # ============================================================
  - name: "Binary detector confidence as depth proxy"
    plan_id: "exp-012"
    description: >
      DivEye/Binoculars score 与 true depth 的 Spearman correlation。
    expected_results:
      diveye:
        spearman_rho_with_depth: 0.18
        p_value: 0.003
        0v1_auc: 0.94
        0v1plus_auc: 0.91
        1v2_auc: 0.53
      binoculars:
        spearman_rho_with_depth: 0.22
        p_value: 0.001
        0v1_auc: 0.96
        0v1plus_auc: 0.93
        1v2_auc: 0.55
      our_method:
        spearman_rho_with_depth: 0.52
        1v2_auc: 0.65
    result_rationale: >
      Binary detectors 的 confidence score 与 depth 有微弱但显著的相关性（ρ=0.18-0.22），因为
      更深代的文本更"像"合成文本（更远离原始分布）。但相关性很弱，因为 binary detectors 优化的是
      real/synthetic 的 decision boundary，不是 depth ordering。它们的 score 主要反映 gen-0 vs
      gen-1+ 的巨大差异（0v1 AUC > 0.94），而在 gen-1 以上的 depth 差异上几乎没有分辨力
      （1v2 AUC 0.53-0.55）。这验证了 "binary confidence ≠ depth" 的 claim，但在 worst tier
      下，我们自己的方法在 1v2 之上也好不了多少——只是从 "nearly random" 升到 "slightly above random"。
    tables:
      - name: "Table: Binary detector score vs depth"
        columns: ["Detector", "ρ(score, depth)", "AUC 0v1", "AUC 1v2"]
        rows:
          - ["DivEye", 0.18, 0.94, 0.53]
          - ["Binoculars", 0.22, 0.96, 0.55]
          - ["Our 15D (ordinal)", 0.52, 0.99, 0.65]
    figures_description:
      - "Scatter plot: detector confidence vs true depth，展示 gen-0 的清晰分离和 gen-1+ 的混杂"
    analysis: >
      Binary confidence 不是 depth 的有效 proxy。我们的方法在 depth correlation 上优势明显
      （ρ=0.52 vs 0.18-0.22），但 absolute performance 仍有限。在 analysis paper 中定位为
      "existing tools cannot estimate depth, motivating dedicated methods"。

  # ============================================================
  # exp-014: Naturalistic validation
  # ============================================================
  - name: "Naturalistic validation (Common Crawl)"
    plan_id: "exp-014"
    description: >
      对 Common Crawl 2025/2026 snapshot 样本做 depth 预测，与 AlignScore 和 vocabulary richness
      做 correlation。
    expected_results:
      predicted_depth_distribution:
        depth_0: 0.72
        depth_1: 0.19
        depth_2plus: 0.09
      correlation_with_alignscore:
        spearman_rho: 0.31
        p_value: 0.001
      correlation_with_vocab_richness:
        spearman_rho: 0.28
        p_value: 0.002
      cross_model_prediction_agreement:
        pythia_vs_olmo_kappa: 0.41
    result_rationale: >
      Common Crawl 中真正的多代递归文本比例仍然有限（2025/2026 snapshot 中大部分合成文本是
      单代生成）。Depth predictor 在 in-distribution（C4 prompt-chain）上训练，迁移到 wild data
      时 feature distribution shift 导致 calibration 下降。与 AlignScore 的中等相关性（ρ=0.31）
      说明 predicted depth 和文本质量有关联但不等同——AlignScore 测量的是 factual consistency
      而非 generational degradation。Pythia vs OLMo 的 predictor agreement 只有 moderate
      （κ=0.41），反映了 cross-model transfer 在 wild data 上的进一步退化。在 worst tier 下，
      这些数据只能支持 "our predictions correlate with independent quality measures" 的 weak claim，
      不能做 ground-truth validation（无法知道 CC 文本的真实 depth）。
    tables:
      - name: "Table: Naturalistic validation correlations"
        columns: ["Metric pair", "Spearman ρ", "p-value"]
        rows:
          - ["Predicted depth vs AlignScore", 0.31, "<0.001"]
          - ["Predicted depth vs Vocab richness", 0.28, "<0.01"]
          - ["Pythia pred vs OLMo pred (κ)", 0.41, "—"]
    figures_description:
      - "Histogram: predicted depth distribution on CC sample"
      - "Scatter plot: predicted depth vs AlignScore"
    analysis: >
      Naturalistic validation 提供了 weak external validity——predicted depth 与独立质量指标
      相关但相关性中等。在 analysis paper 中定位为 "exploratory application"，不能 overclaim。

  # ============================================================
  # exp-015: Learned representation baseline
  # ============================================================
  - name: "Learned representation baseline"
    plan_id: "exp-015"
    description: >
      Frozen Qwen2.5-1.5B embeddings + MLP vs hand-crafted 15D features。
    expected_results:
      learned_frozen_embedding_mlp:
        accuracy: 0.49
        mae: 0.82
        tau_b: 0.61
        1v2_auc: 0.73
        2v3_auc: 0.62
        k_star: 3
      hand_crafted_15D:
        accuracy: 0.38
        mae: 1.14
        tau_b: 0.47
        1v2_auc: 0.65
        2v3_auc: 0.55
        k_star: 2
      delta_accuracy_pp: 11
      delta_1v2_auc: 0.08
    result_rationale: >
      Frozen embeddings 保留了预训练模型的全部表征能力（768D 或 2048D vs 15D），MLP 可以学习到
      hand-crafted features 无法捕捉的非线性组合和高维模式。关键差异在于：(1) embedding 空间中
      不同 depth 的文本形成了可分离的 cluster，但这种分离性是 high-dimensional 的，无法用 15 个
      hand-crafted scalar 特征近似；(2) learned probe 可以自动发现 depth-discriminative 的维度，
      而 hand-crafted features 是基于先验知识手动选择的子集。在 worst tier 下，learned features
      优于 hand-crafted ≥ 10pp（accuracy 0.49 vs 0.38），甚至将 effective K* 推到 3（2v3 AUC
      0.62 > 0.60）。这证明 depth signal 确实存在于文本中但 15D features 无法充分提取。论文必须
      承认 hand-crafted features 是 "convenience baseline for interpretability" 而非 sufficient
      tool，并在 future work 中呼吁 learned approaches。这对 analysis paper 叙事是双刃剑：
      证明了 depth signal 的存在（positive），但削弱了 15D features 作为工具的实用价值（negative）。
    tables:
      - name: "Table: Learned vs hand-crafted features"
        columns: ["Feature type", "Accuracy", "MAE", "τ_b", "AUC 1v2", "AUC 2v3", "K*"]
        rows:
          - ["Hand-crafted 15D", 0.38, 1.14, 0.47, 0.65, 0.55, 2]
          - ["Frozen embedding + MLP", 0.49, 0.82, 0.61, 0.73, 0.62, 3]
          - ["Delta", "+11pp", "−0.32", "+0.14", "+0.08", "+0.07", "+1"]
    figures_description:
      - "Bar chart: accuracy/AUC comparison between learned and hand-crafted"
      - "t-SNE visualization of frozen embeddings colored by depth"
    analysis: >
      Learned features 大幅优于 hand-crafted（+11pp accuracy），证明 depth signal 存在但 15D
      features 不够用。K* 被 learned probe 推到 3，说明 K*=2 的 boundary 部分是 feature
      engineering 的限制而非信号的物理极限。论文必须添加 "our hand-crafted features provide an
      interpretable but suboptimal window into depth signal" 的 caveat，并在 future work
      中呼吁 learned depth estimation。这对 C1' 的影响：K* 的测量值依赖于 feature set，
      "K*=2 with 15D features" 更准确地说是 "K*_15D=2"，而 K*_learned=3。

  # ============================================================
  # exp-016: Base vs Instruct model comparison
  # ============================================================
  - name: "Base vs Instruct model comparison"
    plan_id: "exp-016"
    description: >
      Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异。
    expected_results:
      base_model:
        0v1_auc: 0.991
        1v2_auc: 0.639
        1v2_ci_lower: 0.629
        1v2_ci_upper: 0.649
        2v3_auc: 0.568
        k_star: 2
        top3_features: ["surp_d1_std", "surp_std", "surp_d2_std"]
      instruct_model_cont:
        0v1_auc: 0.997
        1v2_auc: 0.611
        1v2_ci_lower: 0.602
        1v2_ci_upper: 0.621
        2v3_auc: 0.561
        k_star: 2
      delta_1v2_auc: 0.028
      feature_distribution_jsd_base_vs_instruct:
        gen0: 0.008
        gen1: 0.021
        gen2: 0.034
      spearman_rho_feature_ranking: 0.88
    result_rationale: >
      Base model 的 continuation generation 更接近"裸"的 next-token prediction，没有 RLHF/DPO
      的 style alignment。递归 chain 中，base model 的输出更 diverse（temperature 的实际效果更大），
      代际差异衰减稍慢。Instruct model 的 alignment training 倾向于产生更 uniform 的 style，
      递归 chain 更快收敛。但差异不大（Δ1v2 AUC = 0.028pp），K* 都是 2。在 worst tier 下，这个
      实验的叙事价值有限——只是 K* 变化图谱中的又一个 data point。Feature ranking 一致性高（ρ=0.88），
      说明 base/instruct 的 degradation 机制相似。值得注意的是 base model 的 0v1 AUC 略低（0.991 vs
      0.997），因为 base model 的 gen-0 → gen-1 转换保留了更多原始文本特征（没有 style normalization）。
    tables:
      - name: "Table: Base vs Instruct (Qwen2.5-1.5B, continuation mode)"
        columns: ["Variant", "K*", "AUC 0v1", "AUC 1v2", "AUC 2v3"]
        rows:
          - ["Base", 2, 0.991, 0.639, 0.568]
          - ["Instruct", 2, 0.997, 0.611, 0.561]
    figures_description:
      - "Paired AUC decay curves: base vs instruct"
      - "Feature importance comparison heatmap"
    analysis: >
      Base 和 Instruct 的 K* 一致（都是 2），但 base model 的 1v2 AUC 略高。在 analysis paper
      中作为 "instruction tuning slightly accelerates convergence" 的 supporting evidence，
      但不是 major finding。

  # ============================================================
  # exp-009 已在上面处理
  # exp-010 已完成（DONE）
  # exp-013 已完成（DONE）
  # ============================================================

  # ============================================================
  # Qwen-cont 在更严格测试下的预测
  # ============================================================
  - name: "Qwen-cont stricter validation (different seed depth chains)"
    plan_id: "worst-tier-auxiliary"
    description: >
      Qwen-cont 在不同 random seed 的 depth chain 上重新评估，测试 1v2 CI 的稳定性。
      这是 worst tier 核心假设之一。
    expected_results:
      seed_1_1v2_auc: 0.608
      seed_1_1v2_ci_lower: 0.597
      seed_2_1v2_auc: 0.604
      seed_2_1v2_ci_lower: 0.593
      seed_3_1v2_auc: 0.615
      seed_3_1v2_ci_lower: 0.604
      seeds_with_ci_lower_below_060: "2 out of 3"
      mean_1v2_auc_across_seeds: 0.609
    result_rationale: >
      Qwen-cont 的 1v2 CI lower 在原始实验中仅为 0.6015（高于 0.60 仅 0.0015）。这个 margin
      极其脆弱——seed randomness 就足以让它跌破阈值。不同 seed 改变了 depth chain 的具体文本
      实例，而 Qwen-cont 的 1v2 signal 本来就很弱（AUC 0.611），bootstrap CI 的位置对样本
      敏感。在 3 个新 seed 中，2 个的 CI lower 跌破 0.60，说明 "all 1v2 CI lower > 0.60"
      的 claim 不 robust。这打破了 K*=2 的 universal claim——至少对 Qwen-cont 来说，K* 在
      1 和 2 之间摇摆。
    tables:
      - name: "Table: Qwen-cont 1v2 AUC stability across seeds"
        columns: ["Seed", "AUC 1v2", "CI lower", "CI upper", "CI lower > 0.60?"]
        rows:
          - ["Original", 0.611, 0.602, 0.621, "✅ (barely)"]
          - ["Seed 1", 0.608, 0.597, 0.619, "❌"]
          - ["Seed 2", 0.604, 0.593, 0.615, "❌"]
          - ["Seed 3", 0.615, 0.604, 0.626, "✅"]
    figures_description:
      - "Forest plot: 1v2 AUC with CI across seeds，threshold line at 0.60"
    analysis: >
      Qwen-cont 的 K*=2 claim 不稳定。这是 worst tier 的关键证据之一——K*=2 universality
      依赖于一个 margin 仅 0.0015 的 borderline case，在新数据上无法复现。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "890a7645-16c6-4ff9-a95f-02275b5022ba",
  "isSidechain": false,
  "requestId": "req_011CazFqxJkkWibjF5Sj7Ke8",
  "type": "assistant",
  "uuid": "cedad57c-9715-4b53-b09d-cfdec209a514",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01811kNS4zuN32jSX3M3a8s6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19670,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11502,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19670
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

_source line 9_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：K*=2 universality 被打破 + C3 无显著收益 — 需要从 method/application paper 重构为 analysis/measurement paper 核心假设：['exp-003 解码消融: K* 在不同解码策略间变化剧烈（greedy K*=1, high-temp…",
  "leafUuid": "cedad57c-9715-4b53-b09d-cfdec209a514",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Recursive synthetic text depth estimation characterization study",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：K*=2 universality 被打破 + C3 无显著收益 — 需要从 method/application paper 重构为 analysis/measurement paper 核心假设：['exp-003 解码消融: K* 在不同解码策略间变化剧烈（greedy K*=1, high-temp…",
  "leafUuid": "cedad57c-9715-4b53-b09d-cfdec209a514",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Recursive synthetic text depth estimation characterization study",
  "sessionId": "49cfad2c-a8f3-4c96-a966-f91b37069d83"
}
```

---
