# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：C1' 全面成立 + C3 downstream 收益显著 — 原始 2+1 claim 结构可直接支撑 EMNLP main 核心假设：['exp-0

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/17a0a56a-c5cc-4d9c-b9dc-64f84dc25266.jsonl`
- **Structured JSON:** [`a723d59cd5e0d0d6f9a1.json`](../../sessions/a7/a723d59cd5e0d0d6f9a1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T08:09:24.673Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T08:09:24.673Z",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：C1' 全面成立 + C3 downstream 收益显著 — 原始 2+1 claim 结构可直接支撑 EMNLP main\n核心假设：['exp-003 解码消融: K*=2 在 ≥3/4 解码配置下成立，至少一个配置 K*=3（证明 K* 可被解码策略调控）', 'exp-004 7B: 1v2 AUC ≥ 0.65，K*≥2（scale 不削弱 depth signal，可能增强）', 'exp-006 graduated filtering: 至少一个 benchmark 上 graduated − binary ≥ 2pp，paired t-test p < 0.05', 'exp-015 learned features: 15D hand-crafted 与 frozen embedding+MLP 差距 < 3pp AUC（支撑 interpretable features 叙事）', 'Qwen-cont 1v2 CI 在重复实验中稳定高于 0.60（消除 0.0015 margin 的脆弱性）']\n关键指标范围：{'auc_1v2_continuation_new_configs': [0.62, 0.7], 'auc_1v2_7B': [0.65, 0.75], 'k_star_across_decoding': ['2 in ≥3/4 configs, possibly 3 in low-temp'], 'graduated_minus_binary_delta_pp': [2.0, 4.0], 'cross_model_transfer_retention_expanded': [0.82, 0.95], 'spearman_rho_degradation_new_configs': [0.85, 0.95], 'dsir_vs_graduated_delta_pp': [1.0, 3.0], 'ordinal_accuracy_best_model': [0.42, 0.48]}\n叙事方向：原始 framing 完全成立。Title 可写 \"K*=2: The Generational Discrimination Boundary  for Recursive Synthetic Text\"。C1' 展示 K*=2 跨模型/解码/规模的鲁棒性 + 可调控性， C3 展示即使 K*=2 这种粗粒度 ordinal signal 也能在 downstream 产生显著收益。 解码策略对 K* 的调控效应（部分 config K*=3）回应 \"K*=2 太浅\" 的审稿人质疑。 Generation mode analysis 作为 methodological insight 增加论文深度。 目标: EMNLP 2026 Main，reviewer score 预期 3.5-4.0。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-contamination\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 91-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, D012)\n\n### Primary: C1' (K* Characterization)\n首次系统测量递归合成文本的 generational discrimination boundary K*。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 4-model × 2-mode 实验矩阵系统表征 K*_empirical 的行为，包括跨模型一致性、特征退化排序、以及 generation mode 对 depth signal 的调控效应。\n\n**子组件：**\n\n**(a) K* = 2 across all tested configurations**\n> 4-model 1v2 bootstrap 95% CI 汇总：\n> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|---------|--------|-----------------|\n> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |\n>\n> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002\n> - K* 不是离散跳变值，而是 CI-bounded continuum threshold\n> - Paper 可写：\"K*=2 (bootstrap 95% CI for AUC₁ᵥ₂ > 0.60 across all four model configurations; AUC₂ᵥ₃ CI upper < 0.60)\"\n\n**(b) Cross-model transfer**\n> - Pythia↔OLMo 91% accuracy retention → K*=2 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）\n> - depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity\n\n**(c) Degradation ordering consistency**\n> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）\n> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std\n> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）\n> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）\n\n**(d) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection（\"How does generation mode affect depth estimation?\"），不是独立 claim\n\n### Secondary: C3 (Graduated Filtering)\n即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+ 三级）下，K*-aware graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 4-model × 2-mode 实验矩阵系统表征 K*，揭示控制因素（模型架构、解码策略、generation mode），为数据治理提供 actionable guidance。\n- **Headline result template**: \"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with depth features that are 70-85% text-intrinsic (Pythia↔OLMo 91% transfer retention). Even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*=2 太浅，graduated filtering 收益有限\"** → K* 是模型/解码策略依赖的；展示不同解码策略如何调控 K*（exp-003）；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated（exp-006）\n2. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ generation mode analysis，不是分类器本身\n3. **\"Prompt-chain 不代表真实世界递归污染\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法\n4. **\"单模型/单数据集，泛化性不够\"** → 3 个模型族 × 2 种 generation mode + 4×4 cross-model transfer matrix\n5. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013 直接反驳**：Pythia↔OLMo 91% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity\n6. **\"为什么不用 learned representations\"** → 作为 baseline 对比；hand-crafted features 更 interpretable 且支持 degradation ordering 分析\n7. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep\n8. **\"K* 的统计不确定性未量化\"** → 4-model bootstrap CI + permutation test（exp-007）\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study，C3 是 practical application，generation mode analysis 增加深度\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization + transfer analysis 的 novelty\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_001_pythia_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_002_olmo_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- id: exp-003\n  claim:\n  - 1\n  - 3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: exp_003_decoding_ablation\n  status: RUNNING\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth\n    0-3. 测试 K* 是否随模型规模变化。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_005_degradation\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)\n    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α\n    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated\n    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'\n  priority: P0\n  gpu_budget_hours: 72\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-007\n  claim:\n  - 1\n  - 2\n  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算\n    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为\n    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation\n    test + 3-class metrics]'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: exp_007_bootstrap_ci\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9972\n        ci_lower: null\n        ci_upper: null\n        perm_p: null\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: null\n  status: planned\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: null\n  status: planned\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: exp_010_ordinal_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: null\n  status: planned\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001\n    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier\n    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是\n    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-017\n  registry_id: exp_013_cross_transfer\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features，验证 interpretable features 的价值。[Dream worst tier\n    flagged as critical for \"data-intrinsic ceiling\" claim — 需要 stronger probe 才能支撑该\n    claim]'\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-017\n  claim:\n  - 1\n  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,\n    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model\n    对 K* 的影响。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_017_qwen_continuation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- id: mvp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_sat_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- exp_id: exp_001_pythia_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- exp_id: exp_002_olmo_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- exp_id: exp_003_decoding_ablation\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_017_qwen_continuation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- exp_id: exp_013_cross_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- exp_id: exp_005_degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- exp_id: exp_007_bootstrap_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9972\n        ci_lower: null\n        ci_upper: null\n        perm_p: null\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- exp_id: exp_010_ordinal_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-13T08:09:24.677Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T08:09:24.677Z",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-13T08:09:24.698Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：C1' 全面成立 + C3 downstream 收益显著 — 原始 2+1 claim 结构可直接支撑 EMNLP main
核心假设：['exp-003 解码消融: K*=2 在 ≥3/4 解码配置下成立，至少一个配置 K*=3（证明 K* 可被解码策略调控）', 'exp-004 7B: 1v2 AUC ≥ 0.65，K*≥2（scale 不削弱 depth signal，可能增强）', 'exp-006 graduated filtering: 至少一个 benchmark 上 graduated − binary ≥ 2pp，paired t-test p < 0.05', 'exp-015 learned features: 15D hand-crafted 与 frozen embedding+MLP 差距 < 3pp AUC（支撑 interpretable features 叙事）', 'Qwen-cont 1v2 CI 在重复实验中稳定高于 0.60（消除 0.0015 margin 的脆弱性）']
关键指标范围：{'auc_1v2_continuation_new_configs': [0.62, 0.7], 'auc_1v2_7B': [0.65, 0.75], 'k_star_across_decoding': ['2 in ≥3/4 configs, possibly 3 in low-temp'], 'graduated_minus_binary_delta_pp': [2.0, 4.0], 'cross_model_transfer_retention_expanded': [0.82, 0.95], 'spearman_rho_degradation_new_configs': [0.85, 0.95], 'dsir_vs_graduated_delta_pp': [1.0, 3.0], 'ordinal_accuracy_best_model': [0.42, 0.48]}
叙事方向：原始 framing 完全成立。Title 可写 "K*=2: The Generational Discrimination Boundary  for Recursive Synthetic Text"。C1' 展示 K*=2 跨模型/解码/规模的鲁棒性 + 可调控性， C3 展示即使 K*=2 这种粗粒度 ordinal signal 也能在 downstream 产生显著收益。 解码策略对 K* 的调控效应（部分 config K*=3）回应 "K*=2 太浅" 的审稿人质疑。 Generation mode analysis 作为 methodological insight 增加论文深度。 目标: EMNLP 2026 Main，reviewer score 预期 3.5-4.0。


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
  "promptId": "f0aadf8a-7724-44de-8d60-79ac7400a729",
  "type": "user",
  "uuid": "8ed3091e-627f-47b1-ba0d-32c2cae938d6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T08:09:24.696Z_

```json
{
  "parentUuid": "8ed3091e-627f-47b1-ba0d-32c2cae938d6",
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
  "uuid": "89a53a84-ddb5-4095-ad1c-de38993183fa",
  "timestamp": "2026-05-13T08:09:24.696Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T08:09:24.696Z_

```json
{
  "parentUuid": "89a53a84-ddb5-4095-ad1c-de38993183fa",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4912e9de-24f2-4310-ae11-0f33fc103b87",
  "timestamp": "2026-05-13T08:09:24.696Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1' 全面成立 + C3 downstream 收益显著 — 原始 2+1 claim 结构可直接支撑 EMNLP main 核心假设：['exp-003 解码消融: K*=2 在 ≥3/4 解码配置下成立，至少一个配置 K*=3（证明 K* 可被解码策略调控）', 'exp-004 7B: 1v2 AUC…",
  "leafUuid": "4912e9de-24f2-4310-ae11-0f33fc103b87",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "K*=2: Generational discrimination boundary for recursive synthetic text",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266"
}
```

---

### Assistant

_source line 8 · 2026-05-13T08:09:30.305Z_

我先检查项目目录结构和已有文件，确保预测基于完整上下文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4912e9de-24f2-4310-ae11-0f33fc103b87",
  "isSidechain": false,
  "requestId": "req_011CazE9d77tkThsC9nU1dNg",
  "type": "assistant",
  "uuid": "89d3c4a2-37d5-4f39-ac02-9729b0a5447c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184vN8YEAxhbY2c5M4MgLzW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19555,
      "cache_read_input_tokens": 11841,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 191,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19555
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

_source line 9 · 2026-05-13T08:09:31.761Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017QcumYojDHLLxb4oYocCqB`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89d3c4a2-37d5-4f39-ac02-9729b0a5447c",
  "isSidechain": false,
  "requestId": "req_011CazE9d77tkThsC9nU1dNg",
  "type": "assistant",
  "uuid": "72c0d82c-1df5-4b4c-8e51-487c84108a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184vN8YEAxhbY2c5M4MgLzW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19555,
      "cache_read_input_tokens": 11841,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 191,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19555
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

_source line 10 · 2026-05-13T08:09:31.778Z_

<details><summary>↩ Tool result · `toolu_017QcumYojDHLLxb4oYocCqB`</summary>

```text
.claude/sessions/no_project_edcaccf8/CLAUDE.md
.claude/sessions/no_project_edcaccf8/AGENTS.md
.claude/sessions/idea_reviewer_37cfbcb3/CLAUDE.md
.claude/sessions/idea_reviewer_37cfbcb3/AGENTS.md
projects/gen-depth-contamination/artifacts/_project/report/related_work_structure.md
projects/gen-depth-contamination/docs/claim_routes.md
projects/gen-depth-contamination/artifacts/_project/report/claim_routes.md
projects/gen-depth-contamination/docs/theory_framework.md
projects/gen-depth-contamination/artifacts/_project/report/theory_framework.md
projects/gen-depth-contamination/artifacts/_project/report/full_study_plan.md
projects/gen-depth-contamination/task_context/history/reviewer/loop_1.md
projects/gen-depth-contamination/artifacts/_project/report/methodology_draft.md
projects/gen-depth-contamination/docs/figure_plan.md
projects/gen-depth-contamination/artifacts/_project/report/figure_plan.md
projects/gen-depth-contamination/docs/IDEA_BRIEF.md
projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/review_report.md
projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/review_report.md
projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/review_report.md
projects/gen-depth-contamination/artifacts/_project/report/literature_scan_2025_2026.md
projects/gen-depth-contamination/artifacts/literature_scan_2025_2026.md
projects/gen-depth-contamination/docs/methodology_draft.md
projects/gen-depth-contamination/docs/related_work_structure.md
projects/gen-depth-contamination/docs/full_study_plan.md
projects/gen-depth-contamination/task_context/director.md
projects/gen-depth-contamination/task_context/reviewer.md
projects/gen-depth-contamination/task_context/agent.md
projects/gen-depth-contamination/artifacts/_project/report/literature_positioning_notes.md
projects/gen-depth-contamination/artifacts/_project/report/literature_positioning_notes_d23bf4.md
projects/gen-depth-contamination/artifacts/literature_positioning_notes.md
projects/gen-depth-contamination/.claude/sessions/agent_35bd0e91/CLAUDE.md
projects/gen-depth-contamination/.claude/sessions/agent_35bd0e91/AGENTS.md
projects/gen-depth-contamination/memory.md
projects/gen-depth-contamination/report.md
projects/gen-depth-contamination/paper_framing.md
projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55/CLAUDE.md
projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55/AGENTS.md
projects/gen-depth-contamination/ROADMAP.md
projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f/CLAUDE.md
projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
projects/gen-depth-contamination/.claude/CLAUDE.md
projects/gen-depth-contamination/AGENTS.md
projects/gen-depth-contamination/.claude/sessions/director_b268826c/CLAUDE.md
projects/gen-depth-contamination/.claude/sessions/director_b268826c/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72c0d82c-1df5-4b4c-8e51-487c84108a7a",
  "isSidechain": false,
  "promptId": "f0aadf8a-7724-44de-8d60-79ac7400a729",
  "type": "user",
  "uuid": "d44a6fd3-2caf-4ffa-9e9a-1799e84fbf26",
  "toolUseResult": {
    "filenames": [
      ".claude/sessions/no_project_edcaccf8/CLAUDE.md",
      ".claude/sessions/no_project_edcaccf8/AGENTS.md",
      ".claude/sessions/idea_reviewer_37cfbcb3/CLAUDE.md",
      ".claude/sessions/idea_reviewer_37cfbcb3/AGENTS.md",
      "projects/gen-depth-contamination/artifacts/_project/report/related_work_structure.md",
      "projects/gen-depth-contamination/docs/claim_routes.md",
      "projects/gen-depth-contamination/artifacts/_project/report/claim_routes.md",
      "projects/gen-depth-contamination/docs/theory_framework.md",
      "projects/gen-depth-contamination/artifacts/_project/report/theory_framework.md",
      "projects/gen-depth-contamination/artifacts/_project/report/full_study_plan.md",
      "projects/gen-depth-contamination/task_context/history/reviewer/loop_1.md",
      "projects/gen-depth-contamination/artifacts/_project/report/methodology_draft.md",
      "projects/gen-depth-contamination/docs/figure_plan.md",
      "projects/gen-depth-contamination/artifacts/_project/report/figure_plan.md",
      "projects/gen-depth-contamination/docs/IDEA_BRIEF.md",
      "projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/review_report.md",
      "projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/review_report.md",
      "projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/review_report.md",
      "projects/gen-depth-contamination/artifacts/_project/report/literature_scan_2025_2026.md",
      "projects/gen-depth-contamination/artifacts/literature_scan_2025_2026.md",
      "projects/gen-depth-contamination/docs/methodology_draft.md",
      "projects/gen-depth-contamination/docs/related_work_structure.md",
      "projects/gen-depth-contamination/docs/full_study_plan.md",
      "projects/gen-depth-contamination/task_context/director.md",
      "projects/gen-depth-contamination/task_context/reviewer.md",
      "projects/gen-depth-contamination/task_context/agent.md",
      "projects/gen-depth-contamination/artifacts/_project/report/literature_positioning_notes.md",
      "projects/gen-depth-contamination/artifacts/_project/report/literature_positioning_notes_d23bf4.md",
      "projects/gen-depth-contamination/artifacts/literature_positioning_notes.md",
      "projects/gen-depth-contamination/.claude/sessions/agent_35bd0e91/CLAUDE.md",
      "projects/gen-depth-contamination/.claude/sessions/agent_35bd0e91/AGENTS.md",
      "projects/gen-depth-contamination/memory.md",
      "projects/gen-depth-contamination/report.md",
      "projects/gen-depth-contamination/paper_framing.md",
      "projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55/CLAUDE.md",
      "projects/gen-depth-contamination/.claude/sessions/agent_2bb8bf55/AGENTS.md",
      "projects/gen-depth-contamination/ROADMAP.md",
      "projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f/CLAUDE.md",
      "projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f/AGENTS.md",
      ".claude/CLAUDE.md",
      "AGENTS.md",
      "projects/gen-depth-contamination/.claude/CLAUDE.md",
      "projects/gen-depth-contamination/AGENTS.md",
      "projects/gen-depth-contamination/.claude/sessions/director_b268826c/CLAUDE.md",
      "projects/gen-depth-contamination/.claude/sessions/director_b268826c/AGENTS.md"
    ],
    "durationMs": 8,
    "numFiles": 45,
    "truncated": false
  },
  "sourceToolAssistantUUID": "72c0d82c-1df5-4b4c-8e51-487c84108a7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T08:09:32.106Z_

<details><summary>↩ Tool result · `toolu_016z27p1vs2ia3b3KfVEpLfK`</summary>

```text
config/approvals.yaml
config/feishu.yaml
workspace.yaml
config/backend.yaml
global/approvals.yaml
config/secrets/gen-depth-contamination/manifest.yaml
projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml
projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/imagined_experiments.yaml
projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/imagined_experiments.yaml
config/projects/gen-depth-contamination.yaml
projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/meta.yaml
projects/gen-depth-contamination/literature_map.yaml
idea_generator/ideas.yaml
projects/gen-depth-contamination/artifacts/manifest.yaml
projects/gen-depth-contamination/registry.yaml
config/resources.yaml
projects/gen-depth-contamination/experiment_plan.yaml
projects/gen-depth-contamination/decisions.yaml
config/crons.yaml
projects/gen-depth-contamination/dream_registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40cf4081-6c67-41cb-bc75-f20a66908184",
  "isSidechain": false,
  "promptId": "f0aadf8a-7724-44de-8d60-79ac7400a729",
  "type": "user",
  "uuid": "ebbc3675-f4c6-46cc-ab5b-4047498fbe5b",
  "toolUseResult": {
    "filenames": [
      "config/approvals.yaml",
      "config/feishu.yaml",
      "workspace.yaml",
      "config/backend.yaml",
      "global/approvals.yaml",
      "config/secrets/gen-depth-contamination/manifest.yaml",
      "projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml",
      "projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/imagined_experiments.yaml",
      "projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/imagined_experiments.yaml",
      "config/projects/gen-depth-contamination.yaml",
      "projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/meta.yaml",
      "projects/gen-depth-contamination/literature_map.yaml",
      "idea_generator/ideas.yaml",
      "projects/gen-depth-contamination/artifacts/manifest.yaml",
      "projects/gen-depth-contamination/registry.yaml",
      "config/resources.yaml",
      "projects/gen-depth-contamination/experiment_plan.yaml",
      "projects/gen-depth-contamination/decisions.yaml",
      "config/crons.yaml",
      "projects/gen-depth-contamination/dream_registry.yaml"
    ],
    "durationMs": 6,
    "numFiles": 20,
    "truncated": false
  },
  "sourceToolAssistantUUID": "40cf4081-6c67-41cb-bc75-f20a66908184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T08:09:32.096Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016z27p1vs2ia3b3KfVEpLfK`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d44a6fd3-2caf-4ffa-9e9a-1799e84fbf26",
  "isSidechain": false,
  "requestId": "req_011CazE9d77tkThsC9nU1dNg",
  "type": "assistant",
  "uuid": "40cf4081-6c67-41cb-bc75-f20a66908184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0184vN8YEAxhbY2c5M4MgLzW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19555,
      "cache_read_input_tokens": 11841,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 191,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19555
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

_source line 13 · 2026-05-13T08:09:36.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HsyK58LdNM2os9wiQ1Jm2w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebbc3675-f4c6-46cc-ab5b-4047498fbe5b",
  "isSidechain": false,
  "requestId": "req_011CazEAAtZn1fi6JLnz3xfS",
  "type": "assistant",
  "uuid": "6dd2b78c-a2fe-4333-a527-4e68a4af9537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01583b23mjMsFsHaHr56dhet",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 31396,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 31396,
          "cache_creation_input_tokens": 1477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1477
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

_source line 14 · 2026-05-13T08:09:36.361Z_

<details><summary>↩ Tool result · `toolu_01HsyK58LdNM2os9wiQ1Jm2w`</summary>

```text
1	experiments:
2	- id: exp-001
3	  claim: 1
4	  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,
5	    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'
6	  priority: P0
7	  gpu_budget_hours: 6
8	  deps: []
9	  registry_id: exp_001_pythia_depth
10	- id: exp-002
11	  claim: 1
12	  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,
13	    C4 5K docs, depth 0-5.'
14	  priority: P0
15	  gpu_budget_hours: 6
16	  deps: []
17	  registry_id: exp_002_olmo_depth
18	- id: exp-003
19	  claim:
20	  - 1
21	  - 3
22	  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9
23	    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'
24	  priority: P0
25	  gpu_budget_hours: 20
26	  deps: []
27	  registry_id: exp_003_decoding_ablation
28	- id: exp-004
29	  claim: 1
30	  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth
31	    0-3. 测试 K* 是否随模型规模变化。'
32	  priority: P0
33	  gpu_budget_hours: 8
34	  deps: []
35	  registry_id: null
36	- id: exp-005
37	  claim: 2
38	  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth
39	    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制
40	    degradation ordering heatmap。'
41	  priority: P0
42	  gpu_budget_hours: 2
43	  deps:
44	  - exp-001
45	  - exp-002
46	  registry_id: exp_005_degradation
47	- id: exp-006
48	  claim: 3
49	  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter
50	    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)
51	    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness
52	    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α
53	    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated
54	    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'
55	  priority: P0
56	  gpu_budget_hours: 72
57	  deps: []
58	  registry_id: null
59	- id: exp-007
60	  claim:
61	  - 1
62	  - 2
63	  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算
64	    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为
65	    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation
66	    test + 3-class metrics]'
67	  priority: P0
68	  gpu_budget_hours: 2
69	  deps:
70	  - exp-001
71	  - exp-002
72	  - exp-003
73	  registry_id: exp_007_bootstrap_ci
74	- id: exp-008
75	  claim: 1
76	  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),
77	    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'
78	  priority: P1
79	  gpu_budget_hours: 8
80	  deps:
81	  - exp-001
82	  registry_id: null
83	- id: exp-009
84	  claim: 3
85	  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试
86	    graduated vs binary filtering 的收益差异。'
87	  priority: P1
88	  gpu_budget_hours: 15
89	  deps:
90	  - exp-006
91	  registry_id: null
92	- id: exp-010
93	  claim:
94	  - 1
95	  - 2
96	  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs
97	    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'
98	  priority: P1
99	  gpu_budget_hours: 2
100	  deps:
101	  - exp-005
102	  registry_id: exp_010_ordinal_baseline
103	- id: exp-011
104	  claim: 1
105	  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth
106	    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'
107	  priority: P1
108	  gpu_budget_hours: 0
109	  deps: []
110	  registry_id: null
111	- id: exp-012
112	  claim: 1
113	  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score
114	    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'
115	  priority: P1
116	  gpu_budget_hours: 3
117	  deps:
118	  - exp-001
119	  - exp-002
120	  registry_id: null
121	- id: exp-013
122	  claim:
123	  - 1
124	  - 2
125	  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001
126	    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier
127	    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是
128	    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'
129	  priority: P0
130	  gpu_budget_hours: 2
131	  deps:
132	  - exp-001
133	  - exp-002
134	  - exp-017
135	  registry_id: exp_013_cross_transfer
136	- id: exp-014
137	  claim: 1
138	  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth
139	    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'
140	  priority: P2
141	  gpu_budget_hours: 8
142	  deps:
143	  - exp-005
144	  registry_id: null
145	- id: exp-015
146	  claim: 1
147	  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +
148	    MLP vs hand-crafted 15D features，验证 interpretable features 的价值。[Dream worst tier
149	    flagged as critical for "data-intrinsic ceiling" claim — 需要 stronger probe 才能支撑该
150	    claim]'
151	  priority: P1
152	  gpu_budget_hours: 3
153	  deps: []
154	  registry_id: null
155	- id: exp-016
156	  claim: 1
157	  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的
158	    K* 和特征分布差异。'
159	  priority: P1
160	  gpu_budget_hours: 6
161	  deps: []
162	  registry_id: null
163	- id: exp-017
164	  claim:
165	  - 1
166	  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,
167	    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model
168	    对 K* 的影响。'
169	  priority: P0
170	  gpu_budget_hours: 6
171	  deps: []
172	  registry_id: exp_017_qwen_continuation
173	- id: mvp-001
174	  claim:
175	  - 1
176	  - 2
177	  - 3
178	  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,
179	    nucleus p=0.95 T=1.0, depth 0-5.'
180	  priority: P0
181	  gpu_budget_hours: 12
182	  deps: []
183	  registry_id: mvp_pilot_sat_v1
184	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dd2b78c-a2fe-4333-a527-4e68a4af9537",
  "isSidechain": false,
  "promptId": "f0aadf8a-7724-44de-8d60-79ac7400a729",
  "type": "user",
  "uuid": "ccadac8b-052d-4133-ac93-acdfdfae928a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/experiment_plan.yaml",
      "content": "experiments:\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_001_pythia_depth\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_002_olmo_depth\n- id: exp-003\n  claim:\n  - 1\n  - 3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: exp_003_decoding_ablation\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth\n    0-3. 测试 K* 是否随模型规模变化。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_005_degradation\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)\n    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α\n    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated\n    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'\n  priority: P0\n  gpu_budget_hours: 72\n  deps: []\n  registry_id: null\n- id: exp-007\n  claim:\n  - 1\n  - 2\n  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算\n    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为\n    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation\n    test + 3-class metrics]'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: exp_007_bootstrap_ci\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: null\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: null\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: exp_010_ordinal_baseline\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: null\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001\n    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier\n    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是\n    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-017\n  registry_id: exp_013_cross_transfer\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features，验证 interpretable features 的价值。[Dream worst tier\n    flagged as critical for \"data-intrinsic ceiling\" claim — 需要 stronger probe 才能支撑该\n    claim]'\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: null\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: null\n- id: exp-017\n  claim:\n  - 1\n  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,\n    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model\n    对 K* 的影响。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_017_qwen_continuation\n- id: mvp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n",
      "numLines": 184,
      "startLine": 1,
      "totalLines": 184
    }
  },
  "sourceToolAssistantUUID": "6dd2b78c-a2fe-4333-a527-4e68a4af9537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T08:09:36.965Z_

<details open><summary>🔧 Tool call — Read · `toolu_018c3kPrF7RH4dGJp9qhBKkJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccadac8b-052d-4133-ac93-acdfdfae928a",
  "isSidechain": false,
  "requestId": "req_011CazEAAtZn1fi6JLnz3xfS",
  "type": "assistant",
  "uuid": "6149ca36-5a42-4b5d-824f-06d369aa9325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01583b23mjMsFsHaHr56dhet",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 31396,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 31396,
          "cache_creation_input_tokens": 1477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1477
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

_source line 16 · 2026-05-13T08:09:37.279Z_

<details><summary>↩ Tool result · `toolu_018c3kPrF7RH4dGJp9qhBKkJ`</summary>

```text
1	tier: best
2	narrative_guidance: 'Original framing holds intact. K* is a first-measured, modulable
3	  information-theoretic boundary. Story: "We establish K* as a fundamental quantity
4	  that varies predictably with model scale and decoding strategy (K*=2 at 1.5B, K*=3
5	  at 7B / high-temperature), reveal a universal degradation ordering (lexical diversity
6	  collapses before distributional dynamics), and show that even a coarse 3-class depth
7	  signal yields 1.5-3.5% downstream improvement over binary filtering." All three
8	  claims (C1 saturation boundary, C2 degradation ordering, C3 graduated filtering)
9	  are well-supported. K* modulability directly addresses the "K*=2 is too shallow"
10	  concern. Target: EMNLP 2026 Main.
11	
12	  '
13	imagined_experiments:
14	- name: Pythia-1.4B depth chain generation
15	  plan_id: exp-001
16	  description: Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5
17	  expected_results:
18	    pairwise_auc_0v1: 0.991
19	    pairwise_auc_1v2: 0.672
20	    pairwise_auc_2v3: 0.571
21	    pairwise_auc_3v4: 0.533
22	    pairwise_auc_4v5: 0.521
23	    pairwise_jsd_0v1: 0.243
24	    pairwise_jsd_1v2: 0.014
25	    pairwise_jsd_2v3: 0.005
26	    pairwise_jsd_3v4: 0.003
27	    pairwise_jsd_4v5: 0.002
28	    k_star: 2
29	    ordinal_accuracy: 0.401
30	    ordinal_mae: 1.08
31	  result_rationale: 'Pythia-1.4B 与 MVP 的 Qwen2.5-1.5B 参数规模相近但架构更旧（GPT-NeoX 基础）， 预训练数据量和质量略逊于
32	    Qwen2.5。因此 0v1 AUC 仍极高（递归首代信息损失显著）， 但 1v2 AUC 略低于 Qwen（0.672 vs 0.696），因为 Pythia
33	    生成质量本身更低， 递归代际间的边际信息损失更小——即"起点已经更差，所以每代退化的增量更不明显"。 K* 仍为 2，因为在 1.5B 规模 + 标准解码下，DPI
34	    决定的信息瓶颈位置一致。 JSD 衰减模式与 MVP 高度一致（0v1 远大于后续），验证跨模型的 DPI 收敛规律。
35	
36	    '
37	  tables:
38	  - caption: Pythia-1.4B pairwise discrimination across depths
39	    columns:
40	    - depth_pair
41	    - AUC_mean
42	    - AUC_std
43	    - JSD
44	    rows:
45	    - - 0v1
46	      - 0.991
47	      - 0.001
48	      - 0.243
49	    - - 1v2
50	      - 0.672
51	      - 0.008
52	      - 0.014
53	    - - 2v3
54	      - 0.571
55	      - 0.011
56	      - 0.005
57	    - - 3v4
58	      - 0.533
59	      - 0.006
60	      - 0.003
61	    - - 4v5
62	      - 0.521
63	      - 0.009
64	      - 0.002
65	  figures_description:
66	  - JSD decay curve (depth pair vs JSD) for Pythia-1.4B, overlaid with MVP Qwen2.5-1.5B
67	    curve. 两条曲线在 depth≥2 后近乎重叠，视觉上确认 K*=2 的跨模型一致性。
68	  analysis: 'Pythia 确认 1.5B 规模下 K*=2 的鲁棒性。1v2 AUC=0.672 落入 best 档 [0.65, 0.75] 范围。
69	    与 MVP 的差异（Δ AUC_1v2 = -0.024）方向符合预期：更弱的预训练基础 → 更浅的代际信号。 这支持 C1：K* 是模型能力的函数而非固定常数。
70	
71	    '
72	- name: OLMo-1B depth chain generation
73	  plan_id: exp-002
74	  description: OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5
75	  expected_results:
76	    pairwise_auc_0v1: 0.988
77	    pairwise_auc_1v2: 0.654
78	    pairwise_auc_2v3: 0.558
79	    pairwise_auc_3v4: 0.527
80	    pairwise_auc_4v5: 0.515
81	    pairwise_jsd_0v1: 0.221
82	    pairwise_jsd_1v2: 0.012
83	    pairwise_jsd_2v3: 0.004
84	    pairwise_jsd_3v4: 0.003
85	    pairwise_jsd_4v5: 0.002
86	    k_star: 2
87	    ordinal_accuracy: 0.388
88	    ordinal_mae: 1.12
89	  result_rationale: 'OLMo-1B 参数量最小（1B vs 1.4-1.5B），且 OLMo 的 Dolma 预训练数据虽公开透明但 多样性略低于
90	    Qwen 的预训练混合。更小的模型容量意味着单次生成的信息保持率更低， 因此 0v1 JSD 略低（起始分布差异稍小）。但关键是 1v2 AUC=0.654
91	    仍在 best 档下限附近， K* 仍为 2——DPI 理论预测的收敛行为不依赖于具体架构细节，只依赖于信道容量， 而 1B 级模型的信道容量与 1.5B
92	    级处于同一量级。ordinal 性能略低因信号更弱。
93	
94	    '
95	  tables:
96	  - caption: OLMo-1B pairwise discrimination across depths
97	    columns:
98	    - depth_pair
99	    - AUC_mean
100	    - AUC_std
101	    - JSD
102	    rows:
103	    - - 0v1
104	      - 0.988
105	      - 0.001
106	      - 0.221
107	    - - 1v2
108	      - 0.654
109	      - 0.009
110	      - 0.012
111	    - - 2v3
112	      - 0.558
113	      - 0.013
114	      - 0.004
115	    - - 3v4
116	      - 0.527
117	      - 0.007
118	      - 0.003
119	    - - 4v5
120	      - 0.515
121	      - 0.01
122	      - 0.002
123	  figures_description:
124	  - 三模型 JSD decay 对比图（Qwen/Pythia/OLMo），清晰展示 K*=2 在所有 1B-1.5B 模型上一致，但初始 JSD 随模型容量单调递增。
125	  analysis: 'OLMo 作为最小模型提供了 scale 连续体的下端锚点。1v2 AUC=0.654 恰在 best 档下限， 表明 1B 级是当前实验设置下
126	    depth signal 的近似下界。三模型一致的 K*=2 强力支持 C1：K* 在 1-1.5B 规模下是信息论约束的稳健结果，而非某个模型的 artifact。
127	
128	    '
129	- name: Qwen2.5-1.5B decoding strategy ablation
130	  plan_id: exp-003
131	  description: 'Qwen2.5-1.5B: greedy / nucleus p=0.9 / T=0.7 / T=1.2, C4 5K docs,
132	    depth 0-5'
133	  expected_results:
134	    greedy:
135	      k_star: 2
136	      pairwise_auc_1v2: 0.651
137	      pairwise_auc_2v3: 0.554
138	      pairwise_jsd_0v1: 0.234
139	    nucleus_p0.9:
140	      k_star: 2
141	      pairwise_auc_1v2: 0.688
142	      pairwise_auc_2v3: 0.582
143	      pairwise_jsd_0v1: 0.259
144	    temp_0.7:
145	      k_star: 2
146	      pairwise_auc_1v2: 0.668
147	      pairwise_auc_2v3: 0.563
148	      pairwise_jsd_0v1: 0.241
149	    temp_1.2:
150	      k_star: 3
151	      pairwise_auc_1v2: 0.723
152	      pairwise_auc_2v3: 0.648
153	      pairwise_auc_3v4: 0.574
154	      pairwise_auc_4v5: 0.531
155	      pairwise_jsd_0v1: 0.312
156	      pairwise_jsd_1v2: 0.028
157	      pairwise_jsd_2v3: 0.011
158	      pairwise_jsd_3v4: 0.005
159	  result_rationale: '解码策略通过控制 generation entropy 直接调控信道的有效容量。 Greedy 解码（T→0）将输出限制在最高概率
160	    token，递归代际间差异被压缩到很窄的 mode 附近， 导致 1v2 AUC 最低——信息损失在首代就已经高度集中，后续代际几乎无额外损失可测。 T=0.7
161	    和 nucleus p=0.9 居于中间：适度随机性保留了更多分布结构供后续代际逐步丢失。 T=1.2 是关键条件：高温度扩大了 token 采样空间，使得每代生成引入更多"非主流"token
162	    选择， 这些选择在递归中被逐步"洗掉"——但因为起始多样性更高，这个洗掉过程需要更多代际才能饱和。 信息论解释：高温度提高了初始互信息 I(X;Y₁)，DPI
163	    保证 I(X;Yₖ) 单调递减， 但更高的起点意味着降到阈值需要更多步——因此 K* 从 2 升到 3。 这直接验证核心假设 1，且 2v3 AUC=0.648
164	    落入 best 档 [0.62, 0.70]。
165	
166	    '
167	  tables:
168	  - caption: 'Decoding strategy ablation: K* and key pairwise AUCs'
169	    columns:
170	    - decoding
171	    - K*
172	    - AUC_0v1
173	    - AUC_1v2
174	    - AUC_2v3
175	    - AUC_3v4
176	    - JSD_0v1
177	    rows:
178	    - - greedy
179	      - 2
180	      - 0.993
181	      - 0.651
182	      - 0.554
183	      - 0.526
184	      - 0.234
185	    - - nucleus p=0.9
186	      - 2
187	      - 0.994
188	      - 0.688
189	      - 0.582
190	      - 0.538
191	      - 0.259
192	    - - T=0.7
193	      - 2
194	      - 0.993
195	      - 0.668
196	      - 0.563
197	      - 0.53
198	      - 0.241
199	    - - T=1.2
200	      - 3
201	      - 0.997
202	      - 0.723
203	      - 0.648
204	      - 0.574
205	      - 0.312
206	    - - MVP (p=0.95 T=1.0)
207	      - 2
208	      - 0.996
209	      - 0.696
210	      - 0.589
211	      - 0.543
212	      - 0.267
213	  figures_description:
214	  - K* vs decoding entropy 散点图，x 轴为解码策略的 effective entropy（用实际 token 分布熵估计），y 轴为 K*。T=1.2
215	    明确跳到 K*=3，形成清晰的阶跃。
216	  - 五条件 JSD decay 曲线族谱图。T=1.2 曲线在 depth=3 处才穿过阈值线，其余条件在 depth=2 处穿过。
217	  analysis: '这是论文的核心实验之一。T=1.2 → K*=3 直接证明 K* 是可调控的，消解"K*=2 太浅"的审稿人顾虑。 解码策略形成清晰的 K*
218	    调控梯度：greedy ≤ low-temp ≤ standard nucleus ≤ high-temp。 这为 C1 提供了因果方向性证据：不是分类器能力限制了
219	    K*，而是信道特性决定了 K*。
220	
221	    '
222	- name: Qwen2.5-7B cross-scale probe
223	  plan_id: exp-004
224	  description: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3
225	  expected_results:
226	    pairwise_auc_0v1: 0.998
227	    pairwise_auc_1v2: 0.741
228	    pairwise_auc_2v3: 0.662
229	    pairwise_jsd_0v1: 0.341
230	    pairwise_jsd_1v2: 0.032
231	    pairwise_jsd_2v3: 0.013
232	    k_star: 3
233	    ordinal_accuracy: 0.518
234	    ordinal_mae: 0.81
235	  result_rationale: '7B 模型的关键优势是更大的参数空间编码了更丰富的语言分布。递归生成时， 每代输出保留了更多原始分布的细微结构（rare
236	    n-grams、长距离依赖、discourse patterns）， 因此代际间的信息损失更"均匀地分散"到更多代际中，而不是在前两代就急剧塌缩。 具体机制：7B
237	    模型的 next-token 分布具有更长的"有意义尾巴"（tail tokens 仍携带语义信息）， 递归第二代仍能保留这些尾巴 token 的部分分布特征，到第三代才显著丢失——
238	    因此 2v3 AUC=0.662 仍远高于机会水平，K* 达到 3。 这与 1.5B 级（K*=2）形成鲜明对比，建立了 scale → K* 的因果关系。
239	    ordinal_accuracy=0.518 和 mae=0.81 均落入 best 档最优区间，因为更丰富的代际信号 使 ordinal classifier
240	    有更多可利用的特征梯度。 注意 1K docs（vs 5K）引入更大方差，但 7B 的信号强度弥补了样本量不足。
241	
242	    '
243	  tables:
244	  - caption: Qwen2.5-7B vs 1.5B pairwise discrimination comparison
245	    columns:
246	    - depth_pair
247	    - 7B_AUC
248	    - 7B_JSD
249	    - 1.5B_AUC (MVP)
250	    - 1.5B_JSD (MVP)
251	    rows:
252	    - - 0v1
253	      - 0.998
254	      - 0.341
255	      - 0.996
256	      - 0.267
257	    - - 1v2
258	      - 0.741
259	      - 0.032
260	      - 0.696
261	      - 0.016
262	    - - 2v3
263	      - 0.662
264	      - 0.013
265	      - 0.589
266	      - 0.007
267	  figures_description:
268	  - 'Scale-K* 关系图：x 轴为模型参数量（log scale: 1B, 1.4B, 1.5B, 7B），y 轴为 K*。在 7B 处 K* 跳到 3，暗示更大模型可能支持更深的辨别。'
269	  - 7B vs 1.5B JSD decay 对比，7B 曲线整体右移，穿过阈值的 depth 更深。
270	  analysis: '7B 实验确认核心假设 2：模型规模是 K* 的杠杆。K*=3 且 ordinal accuracy=0.518 证明更大模型在标准解码下就能支持更细粒度的
271	    depth estimation。 结合 exp-003 (T=1.2 → K*=3)，两条独立路径都能将 K* 推到 3， 彻底消解"K*=2 是天花板"的叙事风险。对
272	    EMNLP 审稿人的回应： "K*=2 is not a ceiling but a floor that rises with model scale and
273	    decoding entropy."
274	
275	    '
276	- name: Feature group ablation + degradation ordering
277	  plan_id: exp-005
278	  description: 对每个模型的 depth chain，按 feature group 分析饱和深度和 degradation ordering
279	  expected_results:
280	    saturation_depth_vocabulary_diversity:
281	      pythia_1.4b: 1
282	      olmo_1b: 1
283	      qwen_1.5b: 1
284	    saturation_depth_surprisal_dynamics:
285	      pythia_1.4b: 2
286	      olmo_1b: 2
287	      qwen_1.5b: 2
288	    saturation_depth_tail_thinning:
289	      pythia_1.4b: 2
290	      olmo_1b: 1
291	      qwen_1.5b: 2
292	    degradation_ordering_kendall_tau:
293	      pythia_vs_qwen: 0.87
294	      olmo_vs_qwen: 0.82
295	      pythia_vs_olmo: 0.84
296	      mean: 0.84
297	    feature_group_auc_at_depth1:
298	      vocabulary_diversity: 0.612
299	      surprisal_dynamics: 0.693
300	      tail_thinning: 0.641
301	  result_rationale: 'DPI 约束下，不同语言特征编码的互信息量不同，因此对递归损失的敏感度不同。 Vocabulary diversity（type-token
302	    ratio、hapax ratio 等）依赖于 token 分布的尾部—— 递归生成首先"修剪"低频 token（因为模型倾向于生成高概率 token），
303	    导致 vocabulary diversity 在 depth=1 就显著下降并迅速饱和。 Surprisal dynamics（mean surprisal、surprisal
304	    variance、auto-MI）编码的是序列级分布结构， 这种高阶统计量需要更多代际的累积损失才会饱和——因为即使 token 频率分布已经变窄， token
305	    间的条件依赖结构仍然部分保持。 Tail-thinning 特征居于中间：它捕捉分布尾部的厚度，与 vocabulary diversity 相关但更稳健。
306	    三个模型族的 ordering 高度一致（Kendall tau ≥ 0.82），因为这个 ordering 反映的是 信息论的结构性规律（边际统计量先于条件统计量饱和），而非特定模型的
307	    artifact。
308	
309	    '
310	  tables:
311	  - caption: Feature group saturation depth by model
312	    columns:
313	    - feature_group
314	    - Pythia-1.4B
315	    - OLMo-1B
316	    - Qwen2.5-1.5B
317	    rows:
318	    - - vocabulary_diversity
319	      - 1
320	      - 1
321	      - 1
322	    - - surprisal_dynamics
323	      - 2
324	      - 2
325	      - 2
326	    - - tail_thinning
327	      - 2
328	      - 1
329	      - 2
330	  - caption: Cross-model degradation ordering consistency (Kendall tau)
331	    columns:
332	    - model_pair
333	    - tau
334	    rows:
335	    - - Pythia vs Qwen
336	      - 0.87
337	    - - OLMo vs Qwen
338	      - 0.82
339	    - - Pythia vs OLMo
340	      - 0.84
341	  figures_description:
342	  - Degradation ordering heatmap：行为 feature group，列为 depth pair，颜色为 pairwise AUC。清晰展示
343	    vocabulary diversity 行在 depth=1 后即全暗（饱和），surprisal dynamics 行保持亮色到 depth=2。
344	  - 三模型 ordering 的 rank correlation 矩阵图，所有 pair 的 tau ≥ 0.82。
345	  analysis: 'Kendall tau 均值 0.84 落入 best 档 [0.8, 1.0]。vocabulary diversity 一致在 depth=1
346	    饱和 而 surprisal dynamics 在 depth=2 饱和，这为 C2 提供了直接证据。 OLMo 的 tail-thinning 在 depth=1
347	    就饱和（vs 其他模型的 depth=2）是因为 1B 模型 本身的 tail 更薄，可在 discussion 中讨论。ordering 的跨模型一致性表明这是
348	    递归生成的结构性规律而非模型特异现象。
349	
350	    '
351	- name: Downstream filtering evaluation
352	  plan_id: exp-006
353	  description: Qwen2.5-1.5B depth chain, no-filter / binary / graduated / surprisal-based,
354	    3 seeds, MMLU+HellaSwag
355	  expected_results:
356	    mmlu_pp:
357	      no_filter: 25.31
358	      binary: 26.18
359	      graduated: 28.42
360	      surprisal_based: 27.89
361	    hellaswag_pp:
362	      no_filter: 42.67
363	      binary: 43.54
364	      graduated: 45.61
365	      surprisal_based: 45.12
366	    mmlu_std_across_seeds:
367	      no_filter: 0.23
368	      binary: 0.31
369	      graduated: 0.28
370	      surprisal_based: 0.35
371	    hellaswag_std_across_seeds:
372	      no_filter: 0.19
373	      binary: 0.25
374	      graduated: 0.22
375	      surprisal_based: 0.29
376	    graduated_vs_binary_delta_mmlu_pp: 2.24
377	    graduated_vs_binary_delta_hellaswag_pp: 2.07
378	    graduated_vs_binary_p_value_mmlu: 0.008
379	    graduated_vs_binary_p_value_hellaswag: 0.013
380	  result_rationale: 'Binary filtering 将所有合成文本等同对待——保留或移除。但 gen-1 文本质量远高于 gen-3+， binary
381	    策略要么丢掉高质量的 gen-1（过滤过严 → 损失有用数据）要么保留低质量的 gen-3+（过滤过松 → 引入噪声）。 Graduated filtering
382	    利用 3-class ordinal signal（human / gen-1 / gen-2+）在阈值附近做更精细的决策： 对 gen-1 降权但不完全移除（因为它仍包含大部分原始信息），对
383	    gen-2+ 移除（因为已过 K*）。 这种"软阈值"效应在 binary 策略的 precision-recall 权衡最痛苦的区间（gen-1 附近）
384	    提供了 1.5-3.5 个百分点的改善。MMLU 收益（+2.24pp）略高于 HellaSwag（+2.07pp）， 因为 MMLU 对知识密度更敏感——graduated
385	    filtering 保留的 gen-1 中知识保真度高于 binary 移除后的缺失。 Surprisal-based 策略也优于 binary 但不及 graduated，因为它只用单一特征维度做决策，
386	    而 graduated 利用了 ordinal classifier 融合的多维信号。 3 seeds 的 std 均 < 0.35pp，p 值 < 0.05，确认统计显著性。
387	
388	    '
389	  tables:
390	  - caption: 'Downstream evaluation: continued pretraining perplexity and benchmark
391	      performance'
392	    columns:
393	    - strategy
394	    - MMLU (pp)
395	    - MMLU_std
396	    - HellaSwag (pp)
397	    - HS_std
398	    rows:
399	    - - no-filter
400	      - 25.31
401	      - 0.23
402	      - 42.67
403	      - 0.19
404	    - - binary
405	      - 26.18
406	      - 0.31
407	      - 43.54
408	      - 0.25
409	    - - graduated (3-class)
410	      - 28.42
411	      - 0.28
412	      - 45.61
413	      - 0.22
414	    - - surprisal-based
415	      - 27.89
416	      - 0.35
417	      - 45.12
418	      - 0.29
419	  - caption: 'Statistical significance: graduated vs binary (paired t-test, 3 seeds)'
420	    columns:
421	    - benchmark
422	    - Δ (pp)
423	    - p-value
424	    - significant
425	    rows:
426	    - - MMLU
427	      - 2.24
428	      - 0.008
429	      - 'yes'
430	    - - HellaSwag
431	      - 2.07
432	      - 0.013
433	      - 'yes'
434	  figures_description:
435	  - 四策略 benchmark bar chart with error bars (3 seeds)，graduated 明显最高，binary 和 surprisal-based
436	    居中，no-filter 最低。
437	  - Filtering precision-recall curve：在 gen-1 附近（quality threshold ambiguous zone），graduated
438	    的 calibration 明显优于 binary 的阶跃函数。
439	  analysis: 'graduated vs binary Δ=2.24pp (MMLU) 和 2.07pp (HellaSwag) 均落入 best 档范围
440	    [1.5, 3.5] / [1.0, 3.0]。 p < 0.05 跨 3 seeds 确认 C3 成立。graduated 的优势来源明确：对 gen-1
441	    的精细化处理。 surprisal-based 的存在证明即使单一特征也优于 binary，但多维 ordinal signal 更优。
442	
443	    '
444	- name: K* sensitivity analysis
445	  plan_id: exp-007
446	  description: 在 AUC 阈值 0.55/0.60/0.65/0.70 下计算 K*，展示稳健性
447	  expected_results:
448	    qwen_1.5b_mvp:
449	      threshold_0.55: 3
450	      threshold_0.60: 2
451	      threshold_0.65: 2
452	      threshold_0.70: 1
453	    pythia_1.4b:
454	      threshold_0.55: 3
455	      threshold_0.60: 2
456	      threshold_0.65: 2
457	      threshold_0.70: 1
458	    olmo_1b:
459	      threshold_0.55: 2
460	      threshold_0.60: 2
461	      threshold_0.65: 2
462	      threshold_0.70: 1
463	    qwen_1.5b_temp_1.2:
464	      threshold_0.55: 4
465	      threshold_0.60: 3
466	      threshold_0.65: 3
467	      threshold_0.70: 2
468	    k_star_stability_within_0.60_0.65: all models K*=2, perfectly stable
469	  result_rationale: 'K* 本质是"pairwise AUC 首次低于阈值的 depth"，因此它对阈值有阶跃依赖。 但在合理的阈值范围内（0.60-0.65，即"明显高于
470	    chance 但不要求 near-perfect"）， K* 应当稳定。原因：MVP 数据显示 AUC 从 1v2 (0.696) 到 2v3 (0.589)
471	    有显著跳跃， 这意味着任何落在 0.589-0.696 之间的阈值都会给出同一个 K*=2。 0.55 阈值过松（2v3 AUC=0.589 > 0.55），所以
472	    K* 升到 3； 0.70 阈值过严（1v2 AUC=0.696 < 0.70 对部分模型），所以 K* 降到 1。 T=1.2 条件下所有阈值的 K* 都系统性地高
473	    1，反映其更强的代际信号。 关键发现：在论文推荐的 0.60 阈值下，K* 在所有标准解码条件下一致为 2，稳健。
474	
475	    '
476	  tables:
477	  - caption: K* sensitivity to AUC threshold
478	    columns:
479	    - model_condition
480	    - θ=0.55
481	    - θ=0.60
482	    - θ=0.65
483	    - θ=0.70
484	    rows:
485	    - - Qwen2.5-1.5B (p=0.95,T=1.0)
486	      - 3
487	      - 2
488	      - 2
489	      - 1
490	    - - Pythia-1.4B (p=0.95,T=1.0)
491	      - 3
492	      - 2
493	      - 2
494	      - 1
495	    - - OLMo-1B (p=0.95,T=1.0)
496	      - 2
497	      - 2
498	      - 2
499	      - 1
500	    - - Qwen2.5-1.5B (T=1.2)
501	      - 4
502	      - 3
503	      - 3
504	      - 2
505	  figures_description:
506	  - K* vs threshold heatmap：行为 model/condition，列为 threshold，颜色为 K*。中间两列（0.60, 0.65）颜色高度一致，两端发散。
507	  analysis: 'K* 在 θ∈[0.60, 0.65] 的"合理区间"内完全稳定，消解了"K* 是阈值选择的 artifact"的顾虑。 θ=0.60 作为默认推荐有理论支撑（显著高于
508	    0.5 chance level）和实证支撑（稳定区间中心）。 T=1.2 条件的系统性偏移进一步证实 K* 的调控效应是真实的而非阈值敏感的幻觉。
509	
510	    '
511	- name: Retrain-chain ecological validity
512	  plan_id: exp-008
513	  description: Pythia-1.4B LoRA retrain-chain vs prompt-chain, C4 5K docs, depth 0-4
514	  expected_results:
515	    retrain_chain:
516	      k_star: 2
517	      pairwise_auc_0v1: 0.987
518	      pairwise_auc_1v2: 0.658
519	      pairwise_auc_2v3: 0.563
520	      pairwise_auc_3v4: 0.529
521	      pairwise_jsd_0v1: 0.231
522	    prompt_chain:
523	      k_star: 2
524	      pairwise_auc_0v1: 0.991
525	      pairwise_auc_1v2: 0.672
526	      pairwise_auc_2v3: 0.571
527	      pairwise_auc_3v4: 0.533
528	    kstar_diff: 0
529	    feature_distribution_jsd_retrain_vs_prompt:
530	      depth_0: 0.002
531	      depth_1: 0.018
532	      depth_2: 0.031
533	      depth_3: 0.042
534	  result_rationale: 'Retrain-chain（每代在前一代输出上 LoRA 微调后生成）比 prompt-chain 更接近真实世界的 model
535	    collapse 场景。但在 LoRA rank=16 / alpha=32 的轻量微调设置下， 模型权重的实际变化有限（LoRA 只修改了参数空间的低秩子空间），
536	    因此 retrain-chain 的输出分布与 prompt-chain 高度相似。 K* 一致为 2（diff=0，落入 best 档 [0,1]），因为
537	    DPI 的约束是拓扑性的—— 只要信道是有损的（retrain 后仍是有损信道），收敛行为就保持。 但 retrain-chain 的 AUC 系统性地略低于
538	    prompt-chain（Δ≈0.01-0.02）， 因为 LoRA 微调引入了微小的分布偏移使代际边界更模糊。 Feature distribution
539	    JSD 随 depth 递增——更深的代际中，retrain 和 prompt 的累积偏差更大， 但始终在可接受范围内（< 0.05），确认 prompt-chain
540	    是 retrain-chain 的合理代理。
541	
542	    '
543	  tables:
544	  - caption: Retrain-chain vs prompt-chain comparison (Pythia-1.4B)
545	    columns:
546	    - depth_pair
547	    - Retrain AUC
548	    - Prompt AUC
549	    - Δ AUC
550	    rows:
551	    - - 0v1
552	      - 0.987
553	      - 0.991
554	      - -0.004
555	    - - 1v2
556	      - 0.658
557	      - 0.672
558	      - -0.014
559	    - - 2v3
560	      - 0.563
561	      - 0.571
562	      - -0.008
563	    - - 3v4
564	      - 0.529
565	      - 0.533
566	      - -0.004
567	  - caption: Feature distribution divergence (retrain vs prompt)
568	    columns:
569	    - depth
570	    - JSD
571	    rows:
572	    - - 0
573	      - 0.002
574	    - - 1
575	      - 0.018
576	    - - 2
577	      - 0.031
578	    - - 3
579	      - 0.042
580	  figures_description:
581	  - Retrain vs prompt JSD decay 对比图，两条曲线近乎重叠，附 95% CI shading。
582	  - Feature space t-SNE：retrain 和 prompt 在同一 depth 的点高度混合，不同 depth 之间有清晰分离。
583	  analysis: 'K* diff=0 完美落入 best 档 [0,1]，直接验证假设 6。prompt-chain 作为 controlled proxy
584	    的生态效度得到确认。审稿人关于"prompt-chain 不代表真实递归污染"的顾虑被有力回应。 Feature distribution JSD 随 depth
585	    缓慢递增的模式也可报告为 supplementary finding。
586	
587	    '
588	- name: Contamination dose-response
589	  plan_id: exp-009
590	  description: 10%/30%/50% synthetic injection, graduated vs binary filtering, MMLU+HellaSwag
591	  expected_results:
592	    mmlu_delta_graduated_vs_binary:
593	      injection_10pct: 0.82
594	      injection_30pct: 2.24
595	      injection_50pct: 3.41
596	    hellaswag_delta_graduated_vs_binary:
597	      injection_10pct: 0.54
598	      injection_30pct: 2.07
599	      injection_50pct: 2.89
600	    graduated_advantage_trend: monotonically increasing with injection rate
601	  result_rationale: '低污染率（10%）时，binary filtering 已经足够好——需要移除的合成文本少， 错分 gen-1 为"全部合成"的代价也小（因为总量少），所以
602	    graduated 的边际收益有限（< 1pp）。 30% 污染率对应论文主实验（exp-006）条件，graduated 优势约 2pp。 50% 污染率时，binary
603	    filtering 的困境最大：半数数据是合成的，其中包含大量质量尚可的 gen-1， 全部移除导致训练数据量骤降，保留则引入大量 gen-2+ 噪声。graduated
604	    filtering 通过 "保留 gen-1 降权 + 移除 gen-2+"的策略在数据量和质量间取得更好平衡， 优势达到 ~3.4pp (MMLU) /
605	    ~2.9pp (HellaSwag)。 单调递增趋势证明 graduated filtering 的价值随污染严重程度而增加—— 即"问题越严重，我们的方法越有价值"，这是强有力的叙事。
606	
607	    '
608	  tables:
609	  - caption: 'Dose-response: graduated vs binary Δ by contamination rate'
610	    columns:
611	    - injection_rate
612	    - Δ_MMLU (pp)
613	    - Δ_HellaSwag (pp)
614	    rows:
615	    - - 10%
616	      - 0.82
617	      - 0.54
618	    - - 30%
619	      - 2.24
620	      - 2.07
621	    - - 50%
622	      - 3.41
623	      - 2.89
624	  figures_description:
625	  - Dose-response curve：x 轴为 injection rate，y 轴为 graduated vs binary Δ。两条线（MMLU/HellaSwag）均单调递增，暗示实际
626	    web 数据（估计 30-50% 合成）中的应用价值。
627	  analysis: '单调递增的 dose-response 关系是 C3 的有力补充证据。在预计的 web-scale 污染率（30-50%）下， graduated
628	    filtering 的优势最为显著。这为 practical impact 叙事提供了直接支撑： "随着合成文本在 web 数据中的比例持续增长，depth-aware
629	    curation 的价值只会越来越大。"
630	
631	    '
632	- name: Ordinal vs multinomial vs regression baseline
633	  plan_id: exp-010
634	  description: CORAL vs standard multiclass vs ordinal regression on depth classification
635	  expected_results:
636	    coral_ordinal:
637	      accuracy: 0.483
638	      mae: 0.87
639	      adjacent_accuracy: 0.821
640	    multinomial:
641	      accuracy: 0.472
642	      mae: 1.03
643	      adjacent_accuracy: 0.784
644	    ordinal_regression:
645	      accuracy: 0.461
646	      mae: 0.91
647	      adjacent_accuracy: 0.808
648	  result_rationale: 'Depth 具有天然的 ordinal 结构：gen-1 比 gen-3 更接近 gen-2，这种关系应被建模利用。 CORAL（Consistent
649	    Rank Logits）通过共享权重的累积概率建模天然适配 ordinal data， 在 MAE 上显著优于 multinomial（0.87 vs 1.03）——因为
650	    multinomial 将 gen-1 和 gen-3 的 混淆视为与 gen-1 和 gen-2 的混淆同等严重，而 CORAL 的损失函数惩罚距离更远的错误。
651	    Ordinal regression（proportional odds model）也利用了序数结构但参数化更受限（平行线假设）， 在 depth 数据的非等间距分布下表现略逊于
652	    CORAL。 Accuracy 差异较小（因为所有模型都集中犯"±1 depth 错误"）， 但 MAE 和 adjacent accuracy 差异清晰地展示了
653	    ordinal structure 的价值。
654	
655	    '
656	  tables:
657	  - caption: Classifier architecture comparison
658	    columns:
659	    - method
660	    - accuracy
661	    - MAE
662	    - adjacent_acc
663	    rows:
664	    - - CORAL (ordinal)
665	      - 0.483
666	      - 0.87
667	      - 0.821
668	    - - multinomial
669	      - 0.472
670	      - 1.03
671	      - 0.784
672	    - - ordinal regression
673	      - 0.461
674	      - 0.91
675	      - 0.808
676	  figures_description:
677	  - Confusion matrices (3 panels)：CORAL 的 off-diagonal mass 集中在 ±1 对角线，multinomial
678	    更分散。
679	  analysis: 'CORAL 在所有指标上最优，验证了 ordinal structure 的必要性。MAE 差异（0.87 vs 1.03） 对应下游 filtering
680	    中每个错分导致的质量估计偏差，直接影响 graduated filtering 性能。 这为论文的方法论选择提供了消融实验支撑。
681	
682	    '
683	- name: LLM zero-shot depth estimation
684	  plan_id: exp-011
685	  description: GPT-4o / Claude 3.5 zero-shot depth判断, depth 0-4, 200 samples per depth
686	  expected_results:
687	    gpt4o:
688	      accuracy: 0.187
689	      mae: 1.82
690	      kendall_tau_with_true_depth: 0.11
691	    claude_3_5:
692	      accuracy: 0.203
693	      mae: 1.71
694	      kendall_tau_with_true_depth: 0.14
695	    human_baseline_estimated:
696	      accuracy: 0.162
697	      mae: 1.94
698	  result_rationale: 'LLM 的 zero-shot depth estimation 近乎随机，原因有三： (1) Depth 信号是统计性的（需要对比同一
699	    domain 的多样本分布），单文本缺乏参照系； (2) LLM 未被训练理解"递归生成导致的信息损失"这一概念，其质量判断偏向 fluency 和 coherence，
700	    而这些高层语义特征恰恰是最后才饱和的（与 C2 一致）——即使 gen-3 文本的 vocabulary diversity 已经严重退化，LLM 仍可能判定其"写得不错"因为它仍然
701	    fluent； (3) Prompt 中无法有效传达"相对于 seed 域的偏移"信息。 Claude 略优于 GPT-4o 可能是偶然（差异在 noise
702	    range 内），也可能反映其对文本微妙质量差异的 slightly better calibration，但两者都远低于我们的 ordinal classifier（accuracy
703	    0.48 vs 0.19）。 这个结果直接回应"为什么不直接让 LLM 判断"的审稿人问题。
704	
705	    '
706	  tables:
707	  - caption: Zero-shot depth estimation by frontier LLMs
708	    columns:
709	    - model
710	    - accuracy
711	    - MAE
712	    - Kendall tau
713	    rows:
714	    - - GPT-4o
715	      - 0.187
716	      - 1.82
717	      - 0.11
718	    - - Claude 3.5 Sonnet
719	      - 0.203
720	      - 1.71
721	      - 0.14
722	    - - Our ordinal classifier
723	      - 0.483
724	      - 0.87
725	      - 0.52
726	  figures_description:
727	  - Confusion matrix 对比：LLM 预测近乎 uniform 分布，ordinal classifier 显示清晰的对角线主导结构。
728	  analysis: 'LLM zero-shot 性能仅略高于 random chance (0.20 for 5-class)，而 ordinal classifier
729	    是其 2.5 倍。这确立了 depth estimation 作为一个需要专门方法的 task—— 不能被 frontier LLM 的 general intelligence
730	    "免费"解决。强力支持论文的 problem formulation 贡献。
731	
732	    '
733	- name: Binary detector confidence as depth proxy
734	  plan_id: exp-012
735	  description: DivEye/Binoculars score 与 true depth 的 Spearman correlation
736	  expected_results:
737	    diveye:
738	      spearman_rho: 0.23
739	      spearman_p_value: 0.001
740	      depth_discrimination_auc_0v1: 0.94
741	      depth_discrimination_auc_1v2: 0.53
742	    binoculars:
743	      spearman_rho: 0.19
744	      spearman_p_value: 0.003
745	      depth_discrimination_auc_0v1: 0.92
746	      depth_discrimination_auc_1v2: 0.51
747	  result_rationale: 'Binary detectors 被优化为区分 human vs synthetic，其 confidence score
748	    理论上与"合成程度"正相关。 但这种相关性极弱（ρ < 0.25），因为： (1) Binary detectors 的训练目标是最大化 real/synthetic
749	    的决策边界，不是估计"多 synthetic"； (2) 它们的 score 在 gen-1 处已经几乎饱和（AUC_0v1 > 0.92）， 之后 gen-1
750	    到 gen-5 的 score 差异被压缩到极窄的高 confidence 区间内—— 即"所有合成文本都长得差不多 synthetic"，无法区分代际；
751	    (3) Depth signal 是细粒度的分布特征偏移，而 binary detectors 用的 summary statistics （如 min-k%
752	    概率）在 gen-1 之后就进入了平坦区。 Spearman ρ 显著但极弱，证明 binary confidence ≠ depth，binary 框架本质上不足以捕捉
753	    ordinal structure。
754	
755	    '
756	  tables:
757	  - caption: Binary detector scores as depth proxy
758	    columns:
759	    - detector
760	    - Spearman ρ
761	    - p-value
762	    - AUC 0v1
763	    - AUC 1v2
764	    rows:
765	    - - DivEye
766	      - 0.23
767	      - 0.001
768	      - 0.94
769	      - 0.53
770	    - - Binoculars
771	      - 0.19
772	      - 0.003
773	      - 0.92
774	      - 0.51
775	    - - Our features (15D)
776	      - '-'
777	      - '-'
778	      - 0.996
779	      - 0.696
780	  figures_description:
781	  - Binary score vs true depth scatter plot：score 在 depth=0 和 depth=1 之间有大跳跃，depth≥1
782	    后几乎平坦，形成明显的 ceiling effect。
783	  analysis: 'Binary detectors 在 0v1 分辨上强劲但在 1v2 上近乎 chance level， 直接证明"binary detection
784	    ≠ depth estimation"的核心论点。 这是论文 related work positioning 的关键数据点：现有方法解决的是不同的问题。
785	
786	    '
787	- name: Cross-model transfer
788	  plan_id: exp-013
789	  description: Model A 训练的 depth classifier 在 Model B 的 chain 上的 transfer accuracy
790	  expected_results:
791	    transfer_matrix_accuracy:
792	      pythia_to_olmo: 0.364
793	      pythia_to_qwen: 0.371
794	      olmo_to_pythia: 0.352
795	      olmo_to_qwen: 0.358
796	      qwen_to_pythia: 0.387
797	      qwen_to_olmo: 0.374
798	    in_domain_accuracy:
799	      pythia: 0.401
800	      olmo: 0.388
801	      qwen: 0.418
802	    transfer_retention_pct:
803	      mean: 74.6
804	      min: 70.3
805	      max: 78.9
806	    transfer_ordinal_mae:
807	      mean: 1.14
808	  result_rationale: 'Cross-model transfer 成功率反映了 depth signal 中"模型无关成分"的比例。 在 best
809	    档下，transfer retention ≥70% 因为： (1) vocabulary diversity 特征（type-token ratio、hapax
810	    ratio）测量的是分布的通用统计性质， 不依赖于具体模型的 token 偏好——任何模型的递归生成都会收窄词汇分布； (2) surprisal dynamics
811	    在 cross-model 设置下仍有 partial transfer， 因为虽然绝对 surprisal 值因模型而异，但相对变化模式（递归导致 surprisal
812	    下降）是通用的； (3) 15D 特征中的 7-8 维是"模型无关"的，占特征预测力的大部分。 Qwen → others 的 transfer 最好（78.9%），因为
813	    Qwen 作为最强模型学到的 decision boundary 更准确、更 general；OLMo → others 最差（70.3%），因为 1B 模型的信号更弱，
814	    学到的 boundary 更 noisy。
815	
816	    '
817	  tables:
818	  - caption: Cross-model transfer accuracy matrix
819	    columns:
820	    - train\test
821	    - Pythia
822	    - OLMo
823	    - Qwen
824	    - mean_transfer
825	    rows:
826	    - - Pythia
827	      - 0.401*
828	      - 0.364
829	      - 0.371
830	      - 0.368
831	    - - OLMo
832	      - 0.352
833	      - 0.388*
834	      - 0.358
835	      - 0.355
836	    - - Qwen
837	      - 0.387
838	      - 0.374
839	      - 0.418*
840	      - 0.381
841	  - caption: Transfer retention (%)
842	    columns:
843	    - train→test
844	    - retention %
845	    rows:
846	    - - Pythia→OLMo
847	      - 73.1
848	    - - Pythia→Qwen
849	      - 74.2
850	    - - OLMo→Pythia
851	      - 70.3
852	    - - OLMo→Qwen
853	      - 71.5
854	    - - Qwen→Pythia
855	      - 77.4
856	    - - Qwen→OLMo
857	      - 78.9
858	  figures_description:
859	  - Transfer retention heatmap：对角线（in-domain）标星，off-diagonal 颜色在 70-79% 范围，视觉上接近但非相同。
860	  analysis: 'Mean transfer retention 74.6% 落入 best 档 [70, 80]。这证明 depth signal 主要由
861	    模型无关的语言统计量驱动，支持 C1 的"信息论基本量"叙事—— K* 不是某个特定模型的 artifact，而是递归信道的通用性质。 Qwen → others
862	    最优暗示更强模型的 depth boundary 更 transferable。
863	
864	    '
865	- name: Naturalistic validation (Common Crawl)
866	  plan_id: exp-014
867	  description: 对 Common Crawl 2025/2026 snapshot 做 depth 预测，与 AlignScore 和 vocabulary
868	    richness correlation
869	  expected_results:
870	    spearman_predicted_depth_vs_alignscore: -0.31
871	    spearman_predicted_depth_vs_vocab_richness: -0.37
872	    pct_samples_predicted_depth_geq_1: 18.4
873	    pct_samples_predicted_depth_geq_2: 7.2
874	  result_rationale: 'Common Crawl 中的真实合成文本比例和代际深度无法获得 ground truth， 因此只能通过与外部质量指标的
875	    correlation 间接验证。 Predicted depth 与 AlignScore（事实一致性指标）呈负相关（ρ≈-0.31）， 因为更深代际的文本事实偏差更大（递归"电话游戏效应"）。
876	    与 vocabulary richness 的负相关更强（ρ≈-0.37），与 C2 一致：vocabulary diversity 是最先退化的特征。 ~18%
877	    样本被预测为 depth≥1 与 2025-2026 时期 web 合成文本比例的外部估计（15-25%）一致。 depth≥2 仅 7.2%，但这正是 graduated
878	    filtering 最有价值的区间。 相关性不高是预期中的——wild data 的噪声、domain 多样性、unknown model 族都会稀释信号。
879	
880	    '
881	  tables:
882	  - caption: Naturalistic validation on Common Crawl
883	    columns:
884	    - metric
885	    - value
886	    rows:
887	    - - Spearman(depth, AlignScore)
888	      - -0.31
889	    - - Spearman(depth, vocab richness)
890	      - -0.37
891	    - - '% predicted depth≥1'
892	      - 18.4%
893	    - - '% predicted depth≥2'
894	      - 7.2%
895	  figures_description:
896	  - Predicted depth 分布直方图：depth=0 占约 82%，depth=1 约 11%，depth=2+ 约 7%。与 web 合成文本比例估计一致。
897	  - 'Scatter: predicted depth vs AlignScore，带 LOESS smooth line，下降趋势清晰但散点稀疏。'
898	  analysis: 'Naturalistic validation 提供了"proof of concept"级别的 wild-data 证据。 相关性中等偏弱但方向正确且显著，足以支持
899	    appendix 或 discussion section 的 generalizability 论述。 不足以作为 main claim 但有效回应"只在
900	    controlled 设置下验证"的审稿人顾虑。
901	
902	    '
903	- name: Learned representation baseline
904	  plan_id: exp-015
905	  description: Frozen Qwen2.5-1.5B embeddings + MLP vs hand-crafted 15D features
906	  expected_results:
907	    frozen_embeddings_mlp:
908	      accuracy: 0.452
909	      mae: 0.94
910	      training_time_gpu_hours: 2.8
911	      feature_dim: 4096
912	    handcrafted_15d:
913	      accuracy: 0.483
914	      mae: 0.87
915	      training_time_gpu_hours: 0.1
916	      feature_dim: 15
917	  result_rationale: 'Frozen embeddings 包含丰富的语义信息但存在两个劣势： (1) 4096 维中大部分编码的是内容语义（topic、entity）而非递归退化信号，
918	    MLP 需要从高维空间中"挖掘"少数相关维度，在 5K 样本量下容易过拟合； (2) Frozen embeddings 来自同一模型（Qwen2.5-1.5B），引入了自我参照偏差——
919	    模型对自己生成的文本的 embedding 可能有系统性偏向， 但这种偏向在 cross-model 设置下不 transfer。 Hand-crafted
920	    15D features 虽然维度低，但每个特征都直接编码了与递归退化相关的统计量 （diversity、surprisal、tail weight），特征工程的人类先验弥补了维度不足。
921	    更重要的是，15D 特征支持 degradation ordering 分析（C2）和 feature group ablation（exp-005）， 这是
922	    frozen embeddings 无法提供的。 Hand-crafted 优于 frozen 的幅度不大（accuracy +3.1pp），但 interpretability
923	    和 efficiency 优势明显。
924	
925	    '
926	  tables:
927	  - caption: Learned vs hand-crafted features comparison
928	    columns:
929	    - method
930	    - accuracy
931	    - MAE
932	    - dim
933	    - GPU hours
934	    rows:
935	    - - frozen embeddings + MLP
936	      - 0.452
937	      - 0.94
938	      - 4096
939	      - 2.8
940	    - - hand-crafted 15D
941	      - 0.483
942	      - 0.87
943	      - 15
944	      - 0.1
945	  figures_description:
946	  - Performance vs interpretability scatter：x 轴 feature dim (log)，y 轴 accuracy。Hand-crafted
947	    在低维高性能象限，frozen 在高维低性能象限。
948	  analysis: 'Hand-crafted features 在所有指标上优于或持平 frozen embeddings，且维度低 270 倍、训练快 28
949	    倍。 这验证了论文"选择 interpretable features 不是妥协而是优势"的叙事， 回应审稿人"为什么不用 learned representations"的问题。
950	
951	    '
952	- name: Base vs Instruct model comparison
953	  plan_id: exp-016
954	  description: Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异
955	  expected_results:
956	    base:
957	      k_star: 2
958	      pairwise_auc_0v1: 0.993
959	      pairwise_auc_1v2: 0.714
960	      pairwise_auc_2v3: 0.598
961	      pairwise_jsd_0v1: 0.289
962	    instruct:
963	      k_star: 2
964	      pairwise_auc_0v1: 0.996
965	      pairwise_auc_1v2: 0.696
966	      pairwise_auc_2v3: 0.589
967	      pairwise_jsd_0v1: 0.267
968	    base_vs_instruct_auc_1v2_diff: 0.018
969	    base_vs_instruct_feature_divergence:
970	      surprisal_mean_shift: -0.12
971	      vocab_diversity_shift: 0.04
972	  result_rationale: 'Base model 的 depth signal 略强于 Instruct（AUC_1v2: 0.714 vs 0.696），原因：
973	    Instruct 微调（RLHF/DPO）将模型输出拉向"人类偏好的模式"——更规范的句式、更安全的措辞、 更集中的 vocabulary 选择。这种 alignment
974	    相当于对输出分布施加了额外约束， 使得即使是 gen-0（human text passed through instruct model）也已经部分"标准化"了。
975	    因此 instruct 模型的递归代际间差异更小——每代输出都被拉向同一个"preferred mode"。 但 K* 仍为 2，因为 alignment
976	    的影响是 quantitative（减弱信号）而非 qualitative（改变收敛行为）。 Surprisal mean shift 为负（instruct
977	    的 surprisal 更低），反映其输出更"可预测"； vocab diversity shift 为正（instruct 的词汇稍微更多样），反映 RLHF
978	    鼓励的表达多样性。 这些差异小但方向一致，为 discussion 中关于"检测 instruct model 输出"的段落提供数据。
979	
980	    '
981	  tables:
982	  - caption: Base vs Instruct comparison (Qwen2.5-1.5B)
983	    columns:
984	    - variant
985	    - K*
986	    - AUC_0v1
987	    - AUC_1v2
988	    - AUC_2v3
989	    - JSD_0v1
990	    rows:
991	    - - base
992	      - 2
993	      - 0.993
994	      - 0.714
995	      - 0.598
996	      - 0.289
997	    - - instruct (MVP)
998	      - 2
999	      - 0.996
1000	      - 0.696
1001	      - 0.589
1002	      - 0.267
1003	  figures_description:
1004	  - Base vs Instruct JSD decay 对比图：base 曲线始终略高于 instruct，差距在 depth 1-2 最明显。
1005	  - Feature distribution violin plots：base vs instruct 在 depth=1 的 surprisal 和 diversity
1006	    分布差异。
1007	  analysis: Base model 信号略强但 K* 不变，表明 RLHF alignment 压缩了代际差异但未改变信息论收敛行为。 这个结果对实际应用有意义：野外数据可能来自
1008	    base 或 instruct model， K*=2 在两种设置下都成立意味着 graduated filtering 框架对两者都适用。
1009	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6149ca36-5a42-4b5d-824f-06d369aa9325",
  "isSidechain": false,
  "promptId": "f0aadf8a-7724-44de-8d60-79ac7400a729",
  "type": "user",
  "uuid": "ca95460c-2532-4d3a-a3d9-e463dbec9c3c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: 'Original framing holds intact. K* is a first-measured, modulable\n  information-theoretic boundary. Story: \"We establish K* as a fundamental quantity\n  that varies predictably with model scale and decoding strategy (K*=2 at 1.5B, K*=3\n  at 7B / high-temperature), reveal a universal degradation ordering (lexical diversity\n  collapses before distributional dynamics), and show that even a coarse 3-class depth\n  signal yields 1.5-3.5% downstream improvement over binary filtering.\" All three\n  claims (C1 saturation boundary, C2 degradation ordering, C3 graduated filtering)\n  are well-supported. K* modulability directly addresses the \"K*=2 is too shallow\"\n  concern. Target: EMNLP 2026 Main.\n\n  '\nimagined_experiments:\n- name: Pythia-1.4B depth chain generation\n  plan_id: exp-001\n  description: Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5\n  expected_results:\n    pairwise_auc_0v1: 0.991\n    pairwise_auc_1v2: 0.672\n    pairwise_auc_2v3: 0.571\n    pairwise_auc_3v4: 0.533\n    pairwise_auc_4v5: 0.521\n    pairwise_jsd_0v1: 0.243\n    pairwise_jsd_1v2: 0.014\n    pairwise_jsd_2v3: 0.005\n    pairwise_jsd_3v4: 0.003\n    pairwise_jsd_4v5: 0.002\n    k_star: 2\n    ordinal_accuracy: 0.401\n    ordinal_mae: 1.08\n  result_rationale: 'Pythia-1.4B 与 MVP 的 Qwen2.5-1.5B 参数规模相近但架构更旧（GPT-NeoX 基础）， 预训练数据量和质量略逊于\n    Qwen2.5。因此 0v1 AUC 仍极高（递归首代信息损失显著）， 但 1v2 AUC 略低于 Qwen（0.672 vs 0.696），因为 Pythia\n    生成质量本身更低， 递归代际间的边际信息损失更小——即\"起点已经更差，所以每代退化的增量更不明显\"。 K* 仍为 2，因为在 1.5B 规模 + 标准解码下，DPI\n    决定的信息瓶颈位置一致。 JSD 衰减模式与 MVP 高度一致（0v1 远大于后续），验证跨模型的 DPI 收敛规律。\n\n    '\n  tables:\n  - caption: Pythia-1.4B pairwise discrimination across depths\n    columns:\n    - depth_pair\n    - AUC_mean\n    - AUC_std\n    - JSD\n    rows:\n    - - 0v1\n      - 0.991\n      - 0.001\n      - 0.243\n    - - 1v2\n      - 0.672\n      - 0.008\n      - 0.014\n    - - 2v3\n      - 0.571\n      - 0.011\n      - 0.005\n    - - 3v4\n      - 0.533\n      - 0.006\n      - 0.003\n    - - 4v5\n      - 0.521\n      - 0.009\n      - 0.002\n  figures_description:\n  - JSD decay curve (depth pair vs JSD) for Pythia-1.4B, overlaid with MVP Qwen2.5-1.5B\n    curve. 两条曲线在 depth≥2 后近乎重叠，视觉上确认 K*=2 的跨模型一致性。\n  analysis: 'Pythia 确认 1.5B 规模下 K*=2 的鲁棒性。1v2 AUC=0.672 落入 best 档 [0.65, 0.75] 范围。\n    与 MVP 的差异（Δ AUC_1v2 = -0.024）方向符合预期：更弱的预训练基础 → 更浅的代际信号。 这支持 C1：K* 是模型能力的函数而非固定常数。\n\n    '\n- name: OLMo-1B depth chain generation\n  plan_id: exp-002\n  description: OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5\n  expected_results:\n    pairwise_auc_0v1: 0.988\n    pairwise_auc_1v2: 0.654\n    pairwise_auc_2v3: 0.558\n    pairwise_auc_3v4: 0.527\n    pairwise_auc_4v5: 0.515\n    pairwise_jsd_0v1: 0.221\n    pairwise_jsd_1v2: 0.012\n    pairwise_jsd_2v3: 0.004\n    pairwise_jsd_3v4: 0.003\n    pairwise_jsd_4v5: 0.002\n    k_star: 2\n    ordinal_accuracy: 0.388\n    ordinal_mae: 1.12\n  result_rationale: 'OLMo-1B 参数量最小（1B vs 1.4-1.5B），且 OLMo 的 Dolma 预训练数据虽公开透明但 多样性略低于\n    Qwen 的预训练混合。更小的模型容量意味着单次生成的信息保持率更低， 因此 0v1 JSD 略低（起始分布差异稍小）。但关键是 1v2 AUC=0.654\n    仍在 best 档下限附近， K* 仍为 2——DPI 理论预测的收敛行为不依赖于具体架构细节，只依赖于信道容量， 而 1B 级模型的信道容量与 1.5B\n    级处于同一量级。ordinal 性能略低因信号更弱。\n\n    '\n  tables:\n  - caption: OLMo-1B pairwise discrimination across depths\n    columns:\n    - depth_pair\n    - AUC_mean\n    - AUC_std\n    - JSD\n    rows:\n    - - 0v1\n      - 0.988\n      - 0.001\n      - 0.221\n    - - 1v2\n      - 0.654\n      - 0.009\n      - 0.012\n    - - 2v3\n      - 0.558\n      - 0.013\n      - 0.004\n    - - 3v4\n      - 0.527\n      - 0.007\n      - 0.003\n    - - 4v5\n      - 0.515\n      - 0.01\n      - 0.002\n  figures_description:\n  - 三模型 JSD decay 对比图（Qwen/Pythia/OLMo），清晰展示 K*=2 在所有 1B-1.5B 模型上一致，但初始 JSD 随模型容量单调递增。\n  analysis: 'OLMo 作为最小模型提供了 scale 连续体的下端锚点。1v2 AUC=0.654 恰在 best 档下限， 表明 1B 级是当前实验设置下\n    depth signal 的近似下界。三模型一致的 K*=2 强力支持 C1：K* 在 1-1.5B 规模下是信息论约束的稳健结果，而非某个模型的 artifact。\n\n    '\n- name: Qwen2.5-1.5B decoding strategy ablation\n  plan_id: exp-003\n  description: 'Qwen2.5-1.5B: greedy / nucleus p=0.9 / T=0.7 / T=1.2, C4 5K docs,\n    depth 0-5'\n  expected_results:\n    greedy:\n      k_star: 2\n      pairwise_auc_1v2: 0.651\n      pairwise_auc_2v3: 0.554\n      pairwise_jsd_0v1: 0.234\n    nucleus_p0.9:\n      k_star: 2\n      pairwise_auc_1v2: 0.688\n      pairwise_auc_2v3: 0.582\n      pairwise_jsd_0v1: 0.259\n    temp_0.7:\n      k_star: 2\n      pairwise_auc_1v2: 0.668\n      pairwise_auc_2v3: 0.563\n      pairwise_jsd_0v1: 0.241\n    temp_1.2:\n      k_star: 3\n      pairwise_auc_1v2: 0.723\n      pairwise_auc_2v3: 0.648\n      pairwise_auc_3v4: 0.574\n      pairwise_auc_4v5: 0.531\n      pairwise_jsd_0v1: 0.312\n      pairwise_jsd_1v2: 0.028\n      pairwise_jsd_2v3: 0.011\n      pairwise_jsd_3v4: 0.005\n  result_rationale: '解码策略通过控制 generation entropy 直接调控信道的有效容量。 Greedy 解码（T→0）将输出限制在最高概率\n    token，递归代际间差异被压缩到很窄的 mode 附近， 导致 1v2 AUC 最低——信息损失在首代就已经高度集中，后续代际几乎无额外损失可测。 T=0.7\n    和 nucleus p=0.9 居于中间：适度随机性保留了更多分布结构供后续代际逐步丢失。 T=1.2 是关键条件：高温度扩大了 token 采样空间，使得每代生成引入更多\"非主流\"token\n    选择， 这些选择在递归中被逐步\"洗掉\"——但因为起始多样性更高，这个洗掉过程需要更多代际才能饱和。 信息论解释：高温度提高了初始互信息 I(X;Y₁)，DPI\n    保证 I(X;Yₖ) 单调递减， 但更高的起点意味着降到阈值需要更多步——因此 K* 从 2 升到 3。 这直接验证核心假设 1，且 2v3 AUC=0.648\n    落入 best 档 [0.62, 0.70]。\n\n    '\n  tables:\n  - caption: 'Decoding strategy ablation: K* and key pairwise AUCs'\n    columns:\n    - decoding\n    - K*\n    - AUC_0v1\n    - AUC_1v2\n    - AUC_2v3\n    - AUC_3v4\n    - JSD_0v1\n    rows:\n    - - greedy\n      - 2\n      - 0.993\n      - 0.651\n      - 0.554\n      - 0.526\n      - 0.234\n    - - nucleus p=0.9\n      - 2\n      - 0.994\n      - 0.688\n      - 0.582\n      - 0.538\n      - 0.259\n    - - T=0.7\n      - 2\n      - 0.993\n      - 0.668\n      - 0.563\n      - 0.53\n      - 0.241\n    - - T=1.2\n      - 3\n      - 0.997\n      - 0.723\n      - 0.648\n      - 0.574\n      - 0.312\n    - - MVP (p=0.95 T=1.0)\n      - 2\n      - 0.996\n      - 0.696\n      - 0.589\n      - 0.543\n      - 0.267\n  figures_description:\n  - K* vs decoding entropy 散点图，x 轴为解码策略的 effective entropy（用实际 token 分布熵估计），y 轴为 K*。T=1.2\n    明确跳到 K*=3，形成清晰的阶跃。\n  - 五条件 JSD decay 曲线族谱图。T=1.2 曲线在 depth=3 处才穿过阈值线，其余条件在 depth=2 处穿过。\n  analysis: '这是论文的核心实验之一。T=1.2 → K*=3 直接证明 K* 是可调控的，消解\"K*=2 太浅\"的审稿人顾虑。 解码策略形成清晰的 K*\n    调控梯度：greedy ≤ low-temp ≤ standard nucleus ≤ high-temp。 这为 C1 提供了因果方向性证据：不是分类器能力限制了\n    K*，而是信道特性决定了 K*。\n\n    '\n- name: Qwen2.5-7B cross-scale probe\n  plan_id: exp-004\n  description: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3\n  expected_results:\n    pairwise_auc_0v1: 0.998\n    pairwise_auc_1v2: 0.741\n    pairwise_auc_2v3: 0.662\n    pairwise_jsd_0v1: 0.341\n    pairwise_jsd_1v2: 0.032\n    pairwise_jsd_2v3: 0.013\n    k_star: 3\n    ordinal_accuracy: 0.518\n    ordinal_mae: 0.81\n  result_rationale: '7B 模型的关键优势是更大的参数空间编码了更丰富的语言分布。递归生成时， 每代输出保留了更多原始分布的细微结构（rare\n    n-grams、长距离依赖、discourse patterns）， 因此代际间的信息损失更\"均匀地分散\"到更多代际中，而不是在前两代就急剧塌缩。 具体机制：7B\n    模型的 next-token 分布具有更长的\"有意义尾巴\"（tail tokens 仍携带语义信息）， 递归第二代仍能保留这些尾巴 token 的部分分布特征，到第三代才显著丢失——\n    因此 2v3 AUC=0.662 仍远高于机会水平，K* 达到 3。 这与 1.5B 级（K*=2）形成鲜明对比，建立了 scale → K* 的因果关系。\n    ordinal_accuracy=0.518 和 mae=0.81 均落入 best 档最优区间，因为更丰富的代际信号 使 ordinal classifier\n    有更多可利用的特征梯度。 注意 1K docs（vs 5K）引入更大方差，但 7B 的信号强度弥补了样本量不足。\n\n    '\n  tables:\n  - caption: Qwen2.5-7B vs 1.5B pairwise discrimination comparison\n    columns:\n    - depth_pair\n    - 7B_AUC\n    - 7B_JSD\n    - 1.5B_AUC (MVP)\n    - 1.5B_JSD (MVP)\n    rows:\n    - - 0v1\n      - 0.998\n      - 0.341\n      - 0.996\n      - 0.267\n    - - 1v2\n      - 0.741\n      - 0.032\n      - 0.696\n      - 0.016\n    - - 2v3\n      - 0.662\n      - 0.013\n      - 0.589\n      - 0.007\n  figures_description:\n  - 'Scale-K* 关系图：x 轴为模型参数量（log scale: 1B, 1.4B, 1.5B, 7B），y 轴为 K*。在 7B 处 K* 跳到 3，暗示更大模型可能支持更深的辨别。'\n  - 7B vs 1.5B JSD decay 对比，7B 曲线整体右移，穿过阈值的 depth 更深。\n  analysis: '7B 实验确认核心假设 2：模型规模是 K* 的杠杆。K*=3 且 ordinal accuracy=0.518 证明更大模型在标准解码下就能支持更细粒度的\n    depth estimation。 结合 exp-003 (T=1.2 → K*=3)，两条独立路径都能将 K* 推到 3， 彻底消解\"K*=2 是天花板\"的叙事风险。对\n    EMNLP 审稿人的回应： \"K*=2 is not a ceiling but a floor that rises with model scale and\n    decoding entropy.\"\n\n    '\n- name: Feature group ablation + degradation ordering\n  plan_id: exp-005\n  description: 对每个模型的 depth chain，按 feature group 分析饱和深度和 degradation ordering\n  expected_results:\n    saturation_depth_vocabulary_diversity:\n      pythia_1.4b: 1\n      olmo_1b: 1\n      qwen_1.5b: 1\n    saturation_depth_surprisal_dynamics:\n      pythia_1.4b: 2\n      olmo_1b: 2\n      qwen_1.5b: 2\n    saturation_depth_tail_thinning:\n      pythia_1.4b: 2\n      olmo_1b: 1\n      qwen_1.5b: 2\n    degradation_ordering_kendall_tau:\n      pythia_vs_qwen: 0.87\n      olmo_vs_qwen: 0.82\n      pythia_vs_olmo: 0.84\n      mean: 0.84\n    feature_group_auc_at_depth1:\n      vocabulary_diversity: 0.612\n      surprisal_dynamics: 0.693\n      tail_thinning: 0.641\n  result_rationale: 'DPI 约束下，不同语言特征编码的互信息量不同，因此对递归损失的敏感度不同。 Vocabulary diversity（type-token\n    ratio、hapax ratio 等）依赖于 token 分布的尾部—— 递归生成首先\"修剪\"低频 token（因为模型倾向于生成高概率 token），\n    导致 vocabulary diversity 在 depth=1 就显著下降并迅速饱和。 Surprisal dynamics（mean surprisal、surprisal\n    variance、auto-MI）编码的是序列级分布结构， 这种高阶统计量需要更多代际的累积损失才会饱和——因为即使 token 频率分布已经变窄， token\n    间的条件依赖结构仍然部分保持。 Tail-thinning 特征居于中间：它捕捉分布尾部的厚度，与 vocabulary diversity 相关但更稳健。\n    三个模型族的 ordering 高度一致（Kendall tau ≥ 0.82），因为这个 ordering 反映的是 信息论的结构性规律（边际统计量先于条件统计量饱和），而非特定模型的\n    artifact。\n\n    '\n  tables:\n  - caption: Feature group saturation depth by model\n    columns:\n    - feature_group\n    - Pythia-1.4B\n    - OLMo-1B\n    - Qwen2.5-1.5B\n    rows:\n    - - vocabulary_diversity\n      - 1\n      - 1\n      - 1\n    - - surprisal_dynamics\n      - 2\n      - 2\n      - 2\n    - - tail_thinning\n      - 2\n      - 1\n      - 2\n  - caption: Cross-model degradation ordering consistency (Kendall tau)\n    columns:\n    - model_pair\n    - tau\n    rows:\n    - - Pythia vs Qwen\n      - 0.87\n    - - OLMo vs Qwen\n      - 0.82\n    - - Pythia vs OLMo\n      - 0.84\n  figures_description:\n  - Degradation ordering heatmap：行为 feature group，列为 depth pair，颜色为 pairwise AUC。清晰展示\n    vocabulary diversity 行在 depth=1 后即全暗（饱和），surprisal dynamics 行保持亮色到 depth=2。\n  - 三模型 ordering 的 rank correlation 矩阵图，所有 pair 的 tau ≥ 0.82。\n  analysis: 'Kendall tau 均值 0.84 落入 best 档 [0.8, 1.0]。vocabulary diversity 一致在 depth=1\n    饱和 而 surprisal dynamics 在 depth=2 饱和，这为 C2 提供了直接证据。 OLMo 的 tail-thinning 在 depth=1\n    就饱和（vs 其他模型的 depth=2）是因为 1B 模型 本身的 tail 更薄，可在 discussion 中讨论。ordering 的跨模型一致性表明这是\n    递归生成的结构性规律而非模型特异现象。\n\n    '\n- name: Downstream filtering evaluation\n  plan_id: exp-006\n  description: Qwen2.5-1.5B depth chain, no-filter / binary / graduated / surprisal-based,\n    3 seeds, MMLU+HellaSwag\n  expected_results:\n    mmlu_pp:\n      no_filter: 25.31\n      binary: 26.18\n      graduated: 28.42\n      surprisal_based: 27.89\n    hellaswag_pp:\n      no_filter: 42.67\n      binary: 43.54\n      graduated: 45.61\n      surprisal_based: 45.12\n    mmlu_std_across_seeds:\n      no_filter: 0.23\n      binary: 0.31\n      graduated: 0.28\n      surprisal_based: 0.35\n    hellaswag_std_across_seeds:\n      no_filter: 0.19\n      binary: 0.25\n      graduated: 0.22\n      surprisal_based: 0.29\n    graduated_vs_binary_delta_mmlu_pp: 2.24\n    graduated_vs_binary_delta_hellaswag_pp: 2.07\n    graduated_vs_binary_p_value_mmlu: 0.008\n    graduated_vs_binary_p_value_hellaswag: 0.013\n  result_rationale: 'Binary filtering 将所有合成文本等同对待——保留或移除。但 gen-1 文本质量远高于 gen-3+， binary\n    策略要么丢掉高质量的 gen-1（过滤过严 → 损失有用数据）要么保留低质量的 gen-3+（过滤过松 → 引入噪声）。 Graduated filtering\n    利用 3-class ordinal signal（human / gen-1 / gen-2+）在阈值附近做更精细的决策： 对 gen-1 降权但不完全移除（因为它仍包含大部分原始信息），对\n    gen-2+ 移除（因为已过 K*）。 这种\"软阈值\"效应在 binary 策略的 precision-recall 权衡最痛苦的区间（gen-1 附近）\n    提供了 1.5-3.5 个百分点的改善。MMLU 收益（+2.24pp）略高于 HellaSwag（+2.07pp）， 因为 MMLU 对知识密度更敏感——graduated\n    filtering 保留的 gen-1 中知识保真度高于 binary 移除后的缺失。 Surprisal-based 策略也优于 binary 但不及 graduated，因为它只用单一特征维度做决策，\n    而 graduated 利用了 ordinal classifier 融合的多维信号。 3 seeds 的 std 均 < 0.35pp，p 值 < 0.05，确认统计显著性。\n\n    '\n  tables:\n  - caption: 'Downstream evaluation: continued pretraining perplexity and benchmark\n      performance'\n    columns:\n    - strategy\n    - MMLU (pp)\n    - MMLU_std\n    - HellaSwag (pp)\n    - HS_std\n    rows:\n    - - no-filter\n      - 25.31\n      - 0.23\n      - 42.67\n      - 0.19\n    - - binary\n      - 26.18\n      - 0.31\n      - 43.54\n      - 0.25\n    - - graduated (3-class)\n      - 28.42\n      - 0.28\n      - 45.61\n      - 0.22\n    - - surprisal-based\n      - 27.89\n      - 0.35\n      - 45.12\n      - 0.29\n  - caption: 'Statistical significance: graduated vs binary (paired t-test, 3 seeds)'\n    columns:\n    - benchmark\n    - Δ (pp)\n    - p-value\n    - significant\n    rows:\n    - - MMLU\n      - 2.24\n      - 0.008\n      - 'yes'\n    - - HellaSwag\n      - 2.07\n      - 0.013\n      - 'yes'\n  figures_description:\n  - 四策略 benchmark bar chart with error bars (3 seeds)，graduated 明显最高，binary 和 surprisal-based\n    居中，no-filter 最低。\n  - Filtering precision-recall curve：在 gen-1 附近（quality threshold ambiguous zone），graduated\n    的 calibration 明显优于 binary 的阶跃函数。\n  analysis: 'graduated vs binary Δ=2.24pp (MMLU) 和 2.07pp (HellaSwag) 均落入 best 档范围\n    [1.5, 3.5] / [1.0, 3.0]。 p < 0.05 跨 3 seeds 确认 C3 成立。graduated 的优势来源明确：对 gen-1\n    的精细化处理。 surprisal-based 的存在证明即使单一特征也优于 binary，但多维 ordinal signal 更优。\n\n    '\n- name: K* sensitivity analysis\n  plan_id: exp-007\n  description: 在 AUC 阈值 0.55/0.60/0.65/0.70 下计算 K*，展示稳健性\n  expected_results:\n    qwen_1.5b_mvp:\n      threshold_0.55: 3\n      threshold_0.60: 2\n      threshold_0.65: 2\n      threshold_0.70: 1\n    pythia_1.4b:\n      threshold_0.55: 3\n      threshold_0.60: 2\n      threshold_0.65: 2\n      threshold_0.70: 1\n    olmo_1b:\n      threshold_0.55: 2\n      threshold_0.60: 2\n      threshold_0.65: 2\n      threshold_0.70: 1\n    qwen_1.5b_temp_1.2:\n      threshold_0.55: 4\n      threshold_0.60: 3\n      threshold_0.65: 3\n      threshold_0.70: 2\n    k_star_stability_within_0.60_0.65: all models K*=2, perfectly stable\n  result_rationale: 'K* 本质是\"pairwise AUC 首次低于阈值的 depth\"，因此它对阈值有阶跃依赖。 但在合理的阈值范围内（0.60-0.65，即\"明显高于\n    chance 但不要求 near-perfect\"）， K* 应当稳定。原因：MVP 数据显示 AUC 从 1v2 (0.696) 到 2v3 (0.589)\n    有显著跳跃， 这意味着任何落在 0.589-0.696 之间的阈值都会给出同一个 K*=2。 0.55 阈值过松（2v3 AUC=0.589 > 0.55），所以\n    K* 升到 3； 0.70 阈值过严（1v2 AUC=0.696 < 0.70 对部分模型），所以 K* 降到 1。 T=1.2 条件下所有阈值的 K* 都系统性地高\n    1，反映其更强的代际信号。 关键发现：在论文推荐的 0.60 阈值下，K* 在所有标准解码条件下一致为 2，稳健。\n\n    '\n  tables:\n  - caption: K* sensitivity to AUC threshold\n    columns:\n    - model_condition\n    - θ=0.55\n    - θ=0.60\n    - θ=0.65\n    - θ=0.70\n    rows:\n    - - Qwen2.5-1.5B (p=0.95,T=1.0)\n      - 3\n      - 2\n      - 2\n      - 1\n    - - Pythia-1.4B (p=0.95,T=1.0)\n      - 3\n      - 2\n      - 2\n      - 1\n    - - OLMo-1B (p=0.95,T=1.0)\n      - 2\n      - 2\n      - 2\n      - 1\n    - - Qwen2.5-1.5B (T=1.2)\n      - 4\n      - 3\n      - 3\n      - 2\n  figures_description:\n  - K* vs threshold heatmap：行为 model/condition，列为 threshold，颜色为 K*。中间两列（0.60, 0.65）颜色高度一致，两端发散。\n  analysis: 'K* 在 θ∈[0.60, 0.65] 的\"合理区间\"内完全稳定，消解了\"K* 是阈值选择的 artifact\"的顾虑。 θ=0.60 作为默认推荐有理论支撑（显著高于\n    0.5 chance level）和实证支撑（稳定区间中心）。 T=1.2 条件的系统性偏移进一步证实 K* 的调控效应是真实的而非阈值敏感的幻觉。\n\n    '\n- name: Retrain-chain ecological validity\n  plan_id: exp-008\n  description: Pythia-1.4B LoRA retrain-chain vs prompt-chain, C4 5K docs, depth 0-4\n  expected_results:\n    retrain_chain:\n      k_star: 2\n      pairwise_auc_0v1: 0.987\n      pairwise_auc_1v2: 0.658\n      pairwise_auc_2v3: 0.563\n      pairwise_auc_3v4: 0.529\n      pairwise_jsd_0v1: 0.231\n    prompt_chain:\n      k_star: 2\n      pairwise_auc_0v1: 0.991\n      pairwise_auc_1v2: 0.672\n      pairwise_auc_2v3: 0.571\n      pairwise_auc_3v4: 0.533\n    kstar_diff: 0\n    feature_distribution_jsd_retrain_vs_prompt:\n      depth_0: 0.002\n      depth_1: 0.018\n      depth_2: 0.031\n      depth_3: 0.042\n  result_rationale: 'Retrain-chain（每代在前一代输出上 LoRA 微调后生成）比 prompt-chain 更接近真实世界的 model\n    collapse 场景。但在 LoRA rank=16 / alpha=32 的轻量微调设置下， 模型权重的实际变化有限（LoRA 只修改了参数空间的低秩子空间），\n    因此 retrain-chain 的输出分布与 prompt-chain 高度相似。 K* 一致为 2（diff=0，落入 best 档 [0,1]），因为\n    DPI 的约束是拓扑性的—— 只要信道是有损的（retrain 后仍是有损信道），收敛行为就保持。 但 retrain-chain 的 AUC 系统性地略低于\n    prompt-chain（Δ≈0.01-0.02）， 因为 LoRA 微调引入了微小的分布偏移使代际边界更模糊。 Feature distribution\n    JSD 随 depth 递增——更深的代际中，retrain 和 prompt 的累积偏差更大， 但始终在可接受范围内（< 0.05），确认 prompt-chain\n    是 retrain-chain 的合理代理。\n\n    '\n  tables:\n  - caption: Retrain-chain vs prompt-chain comparison (Pythia-1.4B)\n    columns:\n    - depth_pair\n    - Retrain AUC\n    - Prompt AUC\n    - Δ AUC\n    rows:\n    - - 0v1\n      - 0.987\n      - 0.991\n      - -0.004\n    - - 1v2\n      - 0.658\n      - 0.672\n      - -0.014\n    - - 2v3\n      - 0.563\n      - 0.571\n      - -0.008\n    - - 3v4\n      - 0.529\n      - 0.533\n      - -0.004\n  - caption: Feature distribution divergence (retrain vs prompt)\n    columns:\n    - depth\n    - JSD\n    rows:\n    - - 0\n      - 0.002\n    - - 1\n      - 0.018\n    - - 2\n      - 0.031\n    - - 3\n      - 0.042\n  figures_description:\n  - Retrain vs prompt JSD decay 对比图，两条曲线近乎重叠，附 95% CI shading。\n  - Feature space t-SNE：retrain 和 prompt 在同一 depth 的点高度混合，不同 depth 之间有清晰分离。\n  analysis: 'K* diff=0 完美落入 best 档 [0,1]，直接验证假设 6。prompt-chain 作为 controlled proxy\n    的生态效度得到确认。审稿人关于\"prompt-chain 不代表真实递归污染\"的顾虑被有力回应。 Feature distribution JSD 随 depth\n    缓慢递增的模式也可报告为 supplementary finding。\n\n    '\n- name: Contamination dose-response\n  plan_id: exp-009\n  description: 10%/30%/50% synthetic injection, graduated vs binary filtering, MMLU+HellaSwag\n  expected_results:\n    mmlu_delta_graduated_vs_binary:\n      injection_10pct: 0.82\n      injection_30pct: 2.24\n      injection_50pct: 3.41\n    hellaswag_delta_graduated_vs_binary:\n      injection_10pct: 0.54\n      injection_30pct: 2.07\n      injection_50pct: 2.89\n    graduated_advantage_trend: monotonically increasing with injection rate\n  result_rationale: '低污染率（10%）时，binary filtering 已经足够好——需要移除的合成文本少， 错分 gen-1 为\"全部合成\"的代价也小（因为总量少），所以\n    graduated 的边际收益有限（< 1pp）。 30% 污染率对应论文主实验（exp-006）条件，graduated 优势约 2pp。 50% 污染率时，binary\n    filtering 的困境最大：半数数据是合成的，其中包含大量质量尚可的 gen-1， 全部移除导致训练数据量骤降，保留则引入大量 gen-2+ 噪声。graduated\n    filtering 通过 \"保留 gen-1 降权 + 移除 gen-2+\"的策略在数据量和质量间取得更好平衡， 优势达到 ~3.4pp (MMLU) /\n    ~2.9pp (HellaSwag)。 单调递增趋势证明 graduated filtering 的价值随污染严重程度而增加—— 即\"问题越严重，我们的方法越有价值\"，这是强有力的叙事。\n\n    '\n  tables:\n  - caption: 'Dose-response: graduated vs binary Δ by contamination rate'\n    columns:\n    - injection_rate\n    - Δ_MMLU (pp)\n    - Δ_HellaSwag (pp)\n    rows:\n    - - 10%\n      - 0.82\n      - 0.54\n    - - 30%\n      - 2.24\n      - 2.07\n    - - 50%\n      - 3.41\n      - 2.89\n  figures_description:\n  - Dose-response curve：x 轴为 injection rate，y 轴为 graduated vs binary Δ。两条线（MMLU/HellaSwag）均单调递增，暗示实际\n    web 数据（估计 30-50% 合成）中的应用价值。\n  analysis: '单调递增的 dose-response 关系是 C3 的有力补充证据。在预计的 web-scale 污染率（30-50%）下， graduated\n    filtering 的优势最为显著。这为 practical impact 叙事提供了直接支撑： \"随着合成文本在 web 数据中的比例持续增长，depth-aware\n    curation 的价值只会越来越大。\"\n\n    '\n- name: Ordinal vs multinomial vs regression baseline\n  plan_id: exp-010\n  description: CORAL vs standard multiclass vs ordinal regression on depth classification\n  expected_results:\n    coral_ordinal:\n      accuracy: 0.483\n      mae: 0.87\n      adjacent_accuracy: 0.821\n    multinomial:\n      accuracy: 0.472\n      mae: 1.03\n      adjacent_accuracy: 0.784\n    ordinal_regression:\n      accuracy: 0.461\n      mae: 0.91\n      adjacent_accuracy: 0.808\n  result_rationale: 'Depth 具有天然的 ordinal 结构：gen-1 比 gen-3 更接近 gen-2，这种关系应被建模利用。 CORAL（Consistent\n    Rank Logits）通过共享权重的累积概率建模天然适配 ordinal data， 在 MAE 上显著优于 multinomial（0.87 vs 1.03）——因为\n    multinomial 将 gen-1 和 gen-3 的 混淆视为与 gen-1 和 gen-2 的混淆同等严重，而 CORAL 的损失函数惩罚距离更远的错误。\n    Ordinal regression（proportional odds model）也利用了序数结构但参数化更受限（平行线假设）， 在 depth 数据的非等间距分布下表现略逊于\n    CORAL。 Accuracy 差异较小（因为所有模型都集中犯\"±1 depth 错误\"）， 但 MAE 和 adjacent accuracy 差异清晰地展示了\n    ordinal structure 的价值。\n\n    '\n  tables:\n  - caption: Classifier architecture comparison\n    columns:\n    - method\n    - accuracy\n    - MAE\n    - adjacent_acc\n    rows:\n    - - CORAL (ordinal)\n      - 0.483\n      - 0.87\n      - 0.821\n    - - multinomial\n      - 0.472\n      - 1.03\n      - 0.784\n    - - ordinal regression\n      - 0.461\n      - 0.91\n      - 0.808\n  figures_description:\n  - Confusion matrices (3 panels)：CORAL 的 off-diagonal mass 集中在 ±1 对角线，multinomial\n    更分散。\n  analysis: 'CORAL 在所有指标上最优，验证了 ordinal structure 的必要性。MAE 差异（0.87 vs 1.03） 对应下游 filtering\n    中每个错分导致的质量估计偏差，直接影响 graduated filtering 性能。 这为论文的方法论选择提供了消融实验支撑。\n\n    '\n- name: LLM zero-shot depth estimation\n  plan_id: exp-011\n  description: GPT-4o / Claude 3.5 zero-shot depth判断, depth 0-4, 200 samples per depth\n  expected_results:\n    gpt4o:\n      accuracy: 0.187\n      mae: 1.82\n      kendall_tau_with_true_depth: 0.11\n    claude_3_5:\n      accuracy: 0.203\n      mae: 1.71\n      kendall_tau_with_true_depth: 0.14\n    human_baseline_estimated:\n      accuracy: 0.162\n      mae: 1.94\n  result_rationale: 'LLM 的 zero-shot depth estimation 近乎随机，原因有三： (1) Depth 信号是统计性的（需要对比同一\n    domain 的多样本分布），单文本缺乏参照系； (2) LLM 未被训练理解\"递归生成导致的信息损失\"这一概念，其质量判断偏向 fluency 和 coherence，\n    而这些高层语义特征恰恰是最后才饱和的（与 C2 一致）——即使 gen-3 文本的 vocabulary diversity 已经严重退化，LLM 仍可能判定其\"写得不错\"因为它仍然\n    fluent； (3) Prompt 中无法有效传达\"相对于 seed 域的偏移\"信息。 Claude 略优于 GPT-4o 可能是偶然（差异在 noise\n    range 内），也可能反映其对文本微妙质量差异的 slightly better calibration，但两者都远低于我们的 ordinal classifier（accuracy\n    0.48 vs 0.19）。 这个结果直接回应\"为什么不直接让 LLM 判断\"的审稿人问题。\n\n    '\n  tables:\n  - caption: Zero-shot depth estimation by frontier LLMs\n    columns:\n    - model\n    - accuracy\n    - MAE\n    - Kendall tau\n    rows:\n    - - GPT-4o\n      - 0.187\n      - 1.82\n      - 0.11\n    - - Claude 3.5 Sonnet\n      - 0.203\n      - 1.71\n      - 0.14\n    - - Our ordinal classifier\n      - 0.483\n      - 0.87\n      - 0.52\n  figures_description:\n  - Confusion matrix 对比：LLM 预测近乎 uniform 分布，ordinal classifier 显示清晰的对角线主导结构。\n  analysis: 'LLM zero-shot 性能仅略高于 random chance (0.20 for 5-class)，而 ordinal classifier\n    是其 2.5 倍。这确立了 depth estimation 作为一个需要专门方法的 task—— 不能被 frontier LLM 的 general intelligence\n    \"免费\"解决。强力支持论文的 problem formulation 贡献。\n\n    '\n- name: Binary detector confidence as depth proxy\n  plan_id: exp-012\n  description: DivEye/Binoculars score 与 true depth 的 Spearman correlation\n  expected_results:\n    diveye:\n      spearman_rho: 0.23\n      spearman_p_value: 0.001\n      depth_discrimination_auc_0v1: 0.94\n      depth_discrimination_auc_1v2: 0.53\n    binoculars:\n      spearman_rho: 0.19\n      spearman_p_value: 0.003\n      depth_discrimination_auc_0v1: 0.92\n      depth_discrimination_auc_1v2: 0.51\n  result_rationale: 'Binary detectors 被优化为区分 human vs synthetic，其 confidence score\n    理论上与\"合成程度\"正相关。 但这种相关性极弱（ρ < 0.25），因为： (1) Binary detectors 的训练目标是最大化 real/synthetic\n    的决策边界，不是估计\"多 synthetic\"； (2) 它们的 score 在 gen-1 处已经几乎饱和（AUC_0v1 > 0.92）， 之后 gen-1\n    到 gen-5 的 score 差异被压缩到极窄的高 confidence 区间内—— 即\"所有合成文本都长得差不多 synthetic\"，无法区分代际；\n    (3) Depth signal 是细粒度的分布特征偏移，而 binary detectors 用的 summary statistics （如 min-k%\n    概率）在 gen-1 之后就进入了平坦区。 Spearman ρ 显著但极弱，证明 binary confidence ≠ depth，binary 框架本质上不足以捕捉\n    ordinal structure。\n\n    '\n  tables:\n  - caption: Binary detector scores as depth proxy\n    columns:\n    - detector\n    - Spearman ρ\n    - p-value\n    - AUC 0v1\n    - AUC 1v2\n    rows:\n    - - DivEye\n      - 0.23\n      - 0.001\n      - 0.94\n      - 0.53\n    - - Binoculars\n      - 0.19\n      - 0.003\n      - 0.92\n      - 0.51\n    - - Our features (15D)\n      - '-'\n      - '-'\n      - 0.996\n      - 0.696\n  figures_description:\n  - Binary score vs true depth scatter plot：score 在 depth=0 和 depth=1 之间有大跳跃，depth≥1\n    后几乎平坦，形成明显的 ceiling effect。\n  analysis: 'Binary detectors 在 0v1 分辨上强劲但在 1v2 上近乎 chance level， 直接证明\"binary detection\n    ≠ depth estimation\"的核心论点。 这是论文 related work positioning 的关键数据点：现有方法解决的是不同的问题。\n\n    '\n- name: Cross-model transfer\n  plan_id: exp-013\n  description: Model A 训练的 depth classifier 在 Model B 的 chain 上的 transfer accuracy\n  expected_results:\n    transfer_matrix_accuracy:\n      pythia_to_olmo: 0.364\n      pythia_to_qwen: 0.371\n      olmo_to_pythia: 0.352\n      olmo_to_qwen: 0.358\n      qwen_to_pythia: 0.387\n      qwen_to_olmo: 0.374\n    in_domain_accuracy:\n      pythia: 0.401\n      olmo: 0.388\n      qwen: 0.418\n    transfer_retention_pct:\n      mean: 74.6\n      min: 70.3\n      max: 78.9\n    transfer_ordinal_mae:\n      mean: 1.14\n  result_rationale: 'Cross-model transfer 成功率反映了 depth signal 中\"模型无关成分\"的比例。 在 best\n    档下，transfer retention ≥70% 因为： (1) vocabulary diversity 特征（type-token ratio、hapax\n    ratio）测量的是分布的通用统计性质， 不依赖于具体模型的 token 偏好——任何模型的递归生成都会收窄词汇分布； (2) surprisal dynamics\n    在 cross-model 设置下仍有 partial transfer， 因为虽然绝对 surprisal 值因模型而异，但相对变化模式（递归导致 surprisal\n    下降）是通用的； (3) 15D 特征中的 7-8 维是\"模型无关\"的，占特征预测力的大部分。 Qwen → others 的 transfer 最好（78.9%），因为\n    Qwen 作为最强模型学到的 decision boundary 更准确、更 general；OLMo → others 最差（70.3%），因为 1B 模型的信号更弱，\n    学到的 boundary 更 noisy。\n\n    '\n  tables:\n  - caption: Cross-model transfer accuracy matrix\n    columns:\n    - train\\test\n    - Pythia\n    - OLMo\n    - Qwen\n    - mean_transfer\n    rows:\n    - - Pythia\n      - 0.401*\n      - 0.364\n      - 0.371\n      - 0.368\n    - - OLMo\n      - 0.352\n      - 0.388*\n      - 0.358\n      - 0.355\n    - - Qwen\n      - 0.387\n      - 0.374\n      - 0.418*\n      - 0.381\n  - caption: Transfer retention (%)\n    columns:\n    - train→test\n    - retention %\n    rows:\n    - - Pythia→OLMo\n      - 73.1\n    - - Pythia→Qwen\n      - 74.2\n    - - OLMo→Pythia\n      - 70.3\n    - - OLMo→Qwen\n      - 71.5\n    - - Qwen→Pythia\n      - 77.4\n    - - Qwen→OLMo\n      - 78.9\n  figures_description:\n  - Transfer retention heatmap：对角线（in-domain）标星，off-diagonal 颜色在 70-79% 范围，视觉上接近但非相同。\n  analysis: 'Mean transfer retention 74.6% 落入 best 档 [70, 80]。这证明 depth signal 主要由\n    模型无关的语言统计量驱动，支持 C1 的\"信息论基本量\"叙事—— K* 不是某个特定模型的 artifact，而是递归信道的通用性质。 Qwen → others\n    最优暗示更强模型的 depth boundary 更 transferable。\n\n    '\n- name: Naturalistic validation (Common Crawl)\n  plan_id: exp-014\n  description: 对 Common Crawl 2025/2026 snapshot 做 depth 预测，与 AlignScore 和 vocabulary\n    richness correlation\n  expected_results:\n    spearman_predicted_depth_vs_alignscore: -0.31\n    spearman_predicted_depth_vs_vocab_richness: -0.37\n    pct_samples_predicted_depth_geq_1: 18.4\n    pct_samples_predicted_depth_geq_2: 7.2\n  result_rationale: 'Common Crawl 中的真实合成文本比例和代际深度无法获得 ground truth， 因此只能通过与外部质量指标的\n    correlation 间接验证。 Predicted depth 与 AlignScore（事实一致性指标）呈负相关（ρ≈-0.31）， 因为更深代际的文本事实偏差更大（递归\"电话游戏效应\"）。\n    与 vocabulary richness 的负相关更强（ρ≈-0.37），与 C2 一致：vocabulary diversity 是最先退化的特征。 ~18%\n    样本被预测为 depth≥1 与 2025-2026 时期 web 合成文本比例的外部估计（15-25%）一致。 depth≥2 仅 7.2%，但这正是 graduated\n    filtering 最有价值的区间。 相关性不高是预期中的——wild data 的噪声、domain 多样性、unknown model 族都会稀释信号。\n\n    '\n  tables:\n  - caption: Naturalistic validation on Common Crawl\n    columns:\n    - metric\n    - value\n    rows:\n    - - Spearman(depth, AlignScore)\n      - -0.31\n    - - Spearman(depth, vocab richness)\n      - -0.37\n    - - '% predicted depth≥1'\n      - 18.4%\n    - - '% predicted depth≥2'\n      - 7.2%\n  figures_description:\n  - Predicted depth 分布直方图：depth=0 占约 82%，depth=1 约 11%，depth=2+ 约 7%。与 web 合成文本比例估计一致。\n  - 'Scatter: predicted depth vs AlignScore，带 LOESS smooth line，下降趋势清晰但散点稀疏。'\n  analysis: 'Naturalistic validation 提供了\"proof of concept\"级别的 wild-data 证据。 相关性中等偏弱但方向正确且显著，足以支持\n    appendix 或 discussion section 的 generalizability 论述。 不足以作为 main claim 但有效回应\"只在\n    controlled 设置下验证\"的审稿人顾虑。\n\n    '\n- name: Learned representation baseline\n  plan_id: exp-015\n  description: Frozen Qwen2.5-1.5B embeddings + MLP vs hand-crafted 15D features\n  expected_results:\n    frozen_embeddings_mlp:\n      accuracy: 0.452\n      mae: 0.94\n      training_time_gpu_hours: 2.8\n      feature_dim: 4096\n    handcrafted_15d:\n      accuracy: 0.483\n      mae: 0.87\n      training_time_gpu_hours: 0.1\n      feature_dim: 15\n  result_rationale: 'Frozen embeddings 包含丰富的语义信息但存在两个劣势： (1) 4096 维中大部分编码的是内容语义（topic、entity）而非递归退化信号，\n    MLP 需要从高维空间中\"挖掘\"少数相关维度，在 5K 样本量下容易过拟合； (2) Frozen embeddings 来自同一模型（Qwen2.5-1.5B），引入了自我参照偏差——\n    模型对自己生成的文本的 embedding 可能有系统性偏向， 但这种偏向在 cross-model 设置下不 transfer。 Hand-crafted\n    15D features 虽然维度低，但每个特征都直接编码了与递归退化相关的统计量 （diversity、surprisal、tail weight），特征工程的人类先验弥补了维度不足。\n    更重要的是，15D 特征支持 degradation ordering 分析（C2）和 feature group ablation（exp-005）， 这是\n    frozen embeddings 无法提供的。 Hand-crafted 优于 frozen 的幅度不大（accuracy +3.1pp），但 interpretability\n    和 efficiency 优势明显。\n\n    '\n  tables:\n  - caption: Learned vs hand-crafted features comparison\n    columns:\n    - method\n    - accuracy\n    - MAE\n    - dim\n    - GPU hours\n    rows:\n    - - frozen embeddings + MLP\n      - 0.452\n      - 0.94\n      - 4096\n      - 2.8\n    - - hand-crafted 15D\n      - 0.483\n      - 0.87\n      - 15\n      - 0.1\n  figures_description:\n  - Performance vs interpretability scatter：x 轴 feature dim (log)，y 轴 accuracy。Hand-crafted\n    在低维高性能象限，frozen 在高维低性能象限。\n  analysis: 'Hand-crafted features 在所有指标上优于或持平 frozen embeddings，且维度低 270 倍、训练快 28\n    倍。 这验证了论文\"选择 interpretable features 不是妥协而是优势\"的叙事， 回应审稿人\"为什么不用 learned representations\"的问题。\n\n    '\n- name: Base vs Instruct model comparison\n  plan_id: exp-016\n  description: Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异\n  expected_results:\n    base:\n      k_star: 2\n      pairwise_auc_0v1: 0.993\n      pairwise_auc_1v2: 0.714\n      pairwise_auc_2v3: 0.598\n      pairwise_jsd_0v1: 0.289\n    instruct:\n      k_star: 2\n      pairwise_auc_0v1: 0.996\n      pairwise_auc_1v2: 0.696\n      pairwise_auc_2v3: 0.589\n      pairwise_jsd_0v1: 0.267\n    base_vs_instruct_auc_1v2_diff: 0.018\n    base_vs_instruct_feature_divergence:\n      surprisal_mean_shift: -0.12\n      vocab_diversity_shift: 0.04\n  result_rationale: 'Base model 的 depth signal 略强于 Instruct（AUC_1v2: 0.714 vs 0.696），原因：\n    Instruct 微调（RLHF/DPO）将模型输出拉向\"人类偏好的模式\"——更规范的句式、更安全的措辞、 更集中的 vocabulary 选择。这种 alignment\n    相当于对输出分布施加了额外约束， 使得即使是 gen-0（human text passed through instruct model）也已经部分\"标准化\"了。\n    因此 instruct 模型的递归代际间差异更小——每代输出都被拉向同一个\"preferred mode\"。 但 K* 仍为 2，因为 alignment\n    的影响是 quantitative（减弱信号）而非 qualitative（改变收敛行为）。 Surprisal mean shift 为负（instruct\n    的 surprisal 更低），反映其输出更\"可预测\"； vocab diversity shift 为正（instruct 的词汇稍微更多样），反映 RLHF\n    鼓励的表达多样性。 这些差异小但方向一致，为 discussion 中关于\"检测 instruct model 输出\"的段落提供数据。\n\n    '\n  tables:\n  - caption: Base vs Instruct comparison (Qwen2.5-1.5B)\n    columns:\n    - variant\n    - K*\n    - AUC_0v1\n    - AUC_1v2\n    - AUC_2v3\n    - JSD_0v1\n    rows:\n    - - base\n      - 2\n      - 0.993\n      - 0.714\n      - 0.598\n      - 0.289\n    - - instruct (MVP)\n      - 2\n      - 0.996\n      - 0.696\n      - 0.589\n      - 0.267\n  figures_description:\n  - Base vs Instruct JSD decay 对比图：base 曲线始终略高于 instruct，差距在 depth 1-2 最明显。\n  - Feature distribution violin plots：base vs instruct 在 depth=1 的 surprisal 和 diversity\n    分布差异。\n  analysis: Base model 信号略强但 K* 不变，表明 RLHF alignment 压缩了代际差异但未改变信息论收敛行为。 这个结果对实际应用有意义：野外数据可能来自\n    base 或 instruct model， K*=2 在两种设置下都成立意味着 graduated filtering 框架对两者都适用。\n",
      "numLines": 1009,
      "startLine": 1,
      "totalLines": 1009
    }
  },
  "sourceToolAssistantUUID": "6149ca36-5a42-4b5d-824f-06d369aa9325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17 · 2026-05-13T08:09:37.334Z_

````json
{
  "parentUuid": "ca95460c-2532-4d3a-a3d9-e463dbec9c3c",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**gen-depth-contamination**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"gen-depth-contamination\")` 或 `load_project_config(\"gen-depth-contamination\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/gen-depth-contamination/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "ced1c672-c425-459b-871c-8654d57dc1b0",
  "timestamp": "2026-05-13T08:09:37.334Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1' 全面成立 + C3 downstream 收益显著 — 原始 2+1 claim 结构可直接支撑 EMNLP main 核心假设：['exp-003 解码消融: K*=2 在 ≥3/4 解码配置下成立，至少一个配置 K*=3（证明 K* 可被解码策略调控）', 'exp-004 7B: 1v2 AUC…",
  "leafUuid": "ced1c672-c425-459b-871c-8654d57dc1b0",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "K*=2: Generational discrimination boundary for recursive synthetic text",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266"
}
```

---

### Assistant

_source line 20 · 2026-05-13T08:15:45.005Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the project context. Let me also check the previous dream report for the best tier to understand what was already predicted, and then I need to produce an updated version based on the current state of experiments (some are now DONE with real metrics).

The user wants me to generate detailed predictions for ALL planned experiments in the experiment_plan under the "best" tier scenario. The key difference from the previous dream report is that:

1. Several experiments are now DONE with real metrics (exp-001, exp-002, exp-005, exp-007, exp-010, exp-013, exp-017, mvp-001)


2. exp-003 is currently running
3. The remaining planned experiments are exp-004, exp-006, exp-008, exp-009, exp-011, exp-012, exp-014, exp-015, and exp-016

For the completed experiments, I'll use their actual metrics. For the running and planned ones, I need to generate predictions based on the "best" tier definition, which assumes C1' is fully established with significant C3 downstream benefits and directly supports the EMNLP main claim. The key assumption for exp-003 is that the decoding ablation will show K*=2.

Now I'm laying out the specific metric targets for each remaining experiment: exp-004 with 7B models should hit AUC ≥0.65 with K*≥2, exp-006's graduated filtering needs at least one benchmark showing a 2+ percentage point improvement with statistical significance, exp-015's learned features should show less than 3pp gap between hand-crafted and frozen embedding approaches, and the Qwen continuation experiments should maintain stable AUC above 0.60. I'm also tracking the expected ranges for key metrics like the 1v2 continuation AUC between 0.62-0.7 and 7B AUC between 0.65-0.75.

Looking at the additional metric ranges, K* should appear in at least 3/4 of configs with values around 2-3, the graduated filtering improvement should land in the 2-4 percentage point range, cross-model transfer retention should stay strong at 0.82-0.95, and ordinal accuracy for the best model should reach 0.42-0.48. I need to generate detailed predictions for each planned experiment, incorporating actual results where available and focusing specifically on the experiments still in progress. 现在我需要为每个实验仔细构建预测，基于最佳层级假设和已完成实验的实际数据。对于 exp-003，我有 Qwen2.5-1.5B 的基线数据——续写模式下 1v2 AUC 为 0.6114，改写模式下为 0.6957——现在要在这个模型上测试四种解码配置，预期至少三个配置的 K*=2，可能有一个达到 K*=3。

对于贪心解码，由于输出完全确定性，第一代生成就会快速崩溃，后续生成变化不大，所以我预测 1v2 AUC 会低于基线，大约在 0.59-0.60 之间。

虽然 0v1 信号仍然很强（人类文本到贪心模型输出差异大），但 1v2 应该很弱，因为贪心生成的文本在统计特征上（如惊讶度方差）会保持稳定，使得两代之间难以区分。对于最佳等级，我需要在至少 3/4 的配置中达到 K*=2。

现在预测各种采样策略：贪心应该给出 K*=2，但 1v2 的 AUC 较低（约 0.62-0.63）；nucleus p=0.9 比 p=0.95 更保守，所以应该产生类似或略低的 1v2 AUC；温度 T=0.7 会进一步限制多样性。

而 T=1.2 应该增加多样性，可能保留更多信号，预测 1v2 AUC 约 0.68，K* 可能达到 3。基线是 p=0.95 T=1.0 的 0.6114，所以新配置应该在 0.62-0.70 范围内表现更好。

现在看这四个新配置：贪心、p=0.9、T=0.7 和 T=1.2。贪心和 T=0.7 会降低多样性导致更快收敛，1v2 AUC 会更低；T=1.2 则相反；p=0.9 介于两者之间。最佳层级要求至少 3/4 的配置达到 K*=2（1v2 AUC > 0.60），至少一个达到 K*=3，这应该是 T=1.2。贪心如果过于确定性，1v2 AUC 可能跌破 0.60。

我预测贪心、p=0.9 和 T=0.7 都会达到 K*=2，而 T=1.2 会达到 K*=3，这样就满足了最佳层级的要求。

不过让我再看看具体的指标范围——新配置的 1v2 AUC 应该在 0.62 到 0.7 之间，而且需要在至少 3/4 的配置中看到 K*=2，同时至少一个配置出现 K*=3 来证明 K* 可以被解码策略调控。

关于低温下的 K*=3 这个说法有点奇怪，但从信息论的角度来看，更高的温度应该会导致需要更多生成才能饱和信号，所以 K*=3 在高温配置中更合理。现在让我整理完整的 YAML 输出，为每个预测都加上理由。

对于具体的预测，我需要基于已知信息更精确地估计——exp-003 的基线延续（p=0.95, T=1.0）给出 1v2 AUC = 0.6114，现在看贪心解码的表现。

贪心是完全确定性的，第一代输出是 argmax 序列，第二代会非常相似因为它进入同样的贪心过程，但第一代与第零代（人类文本）差异很大，所以 0v1 应该很高，1v2 应该中等水平，我预测 1v2 AUC ≈ 0.625，K*=2。对于 nucleus p=0.9，这比 p=0.95 更严格，保留的 token 更少，采样多样性更低，收敛更快，1v2 AUC ≈ 0.635。

现在看温度参数。T=0.7 会锐化分布，效果类似于减小 nucleus 大小，1v2 AUC ≈ 0.628，K*=2。T=1.2 则平坦化分布，输出更多样化，每一代都保留更多输入的分布特性，1v2 AUC ≈ 0.685，2v3 AUC ≈ 0.625，K*=3。

为了让最佳层级的数字在指定范围 [0.62, 0.70] 内更整洁，我调整一下：贪心设为 1v2 = 0.6285，K*=2；p=0.9 设为 1v2 = 0.6412，K*=2；T=0.7 继续调整中。

现在看 T=1.2 的情况，1v2 = 0.6831，2v3 = 0.6214，K*=3。

对于 exp-004 的 7B 跨尺度探针，关键假设是 1v2 AUC ≥ 0.65，K*≥2。7B 模型相比 1.5B 多了约 5 倍的参数，更多参数意味着更丰富的输出分布，每一代保留更多信息，因此 1v2 AUC 应该更高。但 K* 会增加到 3 吗？用标准解码参数（p=0.95，T=1.0）在 7B 上，之前的预测显示 K*=3，1v2=0.741。

不过最佳层级的假设只要求 K*≥2，不一定非得是 3。让我更保守一点，但仍在最佳范围内——K*=2 或 3 都可以，但 K*=3 会更强。我倾向预测 K*=3，1v2=0.72，2v3=0.64。

现在考虑到这个实验只有 1K 文档（其他的有 5K），方差会更大，而且深度范围只到 3（不是 5），这意味着能评估的深度对更少。我预测 1v2 AUC 约 0.695，2v3 约 0.618，这样 K*≥3。由于深度范围的限制，我无法精确确定 K* 的确切值，但这足以证明最佳层级的表现。

现在看下游过滤实验，关键假设是渐进式方法相比二元方法至少要在某个基准上高出 2 个百分点，且配对 t 检验 p 值小于 0.05。实验对比六种策略——无过滤、我们的二元方法、Drayson 的二元方法、渐进式、基于惊讶度和 DSIR——在 5 个随机种子下，用 MMLU 和 HellaSwag 测试，还要做渐进式方法的 α 敏感性扫描。我预期无过滤基线会因为在污染数据上训练而表现较差，我们的二元方法会比无过滤好但会丢失一些有用的生成数据，而 Drayson 的二元方法应该会有不同的权衡。

渐进式方法用三分类序数信号应该是最好的策略，基于惊讶度作为单一特征代理会比二元方法好但不如渐进式，DSIR 的分布匹配方法因为没有估计深度所以对深度特定污染的帮助有限。在 MMLU 上，我预期渐进式方法会比我们的二元方法高出约 2.4 个百分点，比 DSIR 高出 2.0 个百分点，而在 HellaSwag 上继续检查各方法的表现。

现在看 exp-008，我在考虑用 Pythia-1.4B LoRA 重新训练与提示链的生态有效性，由于 LoRA 秩数较低模型变化最小，重新训练链应该会给出与提示链相似的结果。

我预测 1v2 AUC 约为 0.638，K* 仍为 2，两者差异不大。

在 exp-009 中，我看到随着注入率增加，graduated 相对于 binary 的优势单调递增——10% 注入时差异仅 0.8pp，30% 时达到 2.4pp，50% 时扩大到 3.6pp。

对于 exp-011，我预期大语言模型在深度估计上表现接近随机水平，5 分类任务的随机准确率是 20%，而 GPT-4o 和 Claude 的准确率分别约为 22% 和 23%。

在 exp-012 中，我注意到二元检测器在 0v1 上表现优异但在 1v2 上接近随机，现在检查 DivEye 与真实值的 Spearman 相关系数。 Looking at the pairwise AUC metric from the earlier experiments, the frozen embeddings with an MLP should perform within about 3 percentage points of the hand-crafted 15D features—I'm predicting around 0.608 versus 0.624, which gives a gap of 1.6pp and validates that assumption. Now I'm considering how the base model might differ from the instruct variant, expecting a slightly stronger depth signal in the base model. I'm identifying which experiments need detailed data — the ones marked as planned or currently running are exp-003 through exp-016, excluding the completed ones. Now I'll compile comprehensive YAML output with tables and analysis for each of these ten experiments.

I need to ground my predictions in the actual experimental data rather than being overly optimistic. For exp-003, which was already running before the continuation mode control was established, I should calibrate the expected AUC values more conservatively based on what the actual baseline showed rather than inflated projections. predictions in best tier, I should predict AUCs that are in the range [0.62, 0.70] for the new configs. But the baseline continuation mode gives 0.6114. So some configs should give higher AUC (high temperature, more randomness) and some lower (greedy, low temperature).

Wait, actually the description says "Qwen2.5-1.5B" without specifying Instruct. But the MVP used Qwen2.5-1.5B-Instruct. For decoding ablation, it might use the Instruct model since that's what they've been working with.

Let me also consider: the 4 configs are greedy, nucleus p=0.9, T=0.7, T=1.2. The existing baseline is nucleus p=0.95 T=1.0 (from both mvp-001 rewrite and exp-017 continuation). The decoding ablation probably uses continuation mode since that's the canonical condition established in the paper.

For continuation mode baseline (exp-017): 1v2 AUC = 0.6114. Now I'm thinking through the 4 configs. Greedy should be the most deterministic, collapsing generations to the mode of the distribution, which means recursive generations converge fastest and the 1v2 AUC should dip below baseline—I'll predict around 0.604. The nucleus and temperature variants should spread out from there, with higher temperature giving more randomness and potentially better AUC. For the best tier constraint where K*=2 in at least 3 out of 4 configs, greedy dipping below 0.60 would give K*=1, leaving the other three configs to satisfy the requirement.

Actually, this creates a stronger narrative: showing that K* genuinely varies with decoding strategy—greedy at K*=1, standard configs at K*=2, high temperature at K*=3—demonstrates that depth estimation is truly modulated by how we generate, rather than just being a fixed property. the assumption requires K*=2 in at least 3 out of the 4 new configs, so if greedy has K*=1, the other three (nucleus p=0.9, T=0.7, T=1.2) would all need K*≥2, which satisfies the constraint and creates a stronger narrative contrast.

For the paper, I should keep exp-003 in continuation mode to maintain a clean comparison across the decoding ablations. Now I'm settling on the greedy predictions: 0v1 accuracy of 0.996 and 1v2 of 0.582.

Looking at the full results across all three configurations, the nucleus sampling and temperature variants both show K*=2, indicating they can discriminate up to depth 2, while greedy stays at K*=1. The nucleus approach yields slightly higher 1v2 accuracy at 0.635 compared to greedy's 0.582, and temperature 0.7 is similar at 0.625. The Jensen-Shannon divergence metrics are all quite small, clustering around 0.27 for the 0v1 comparison and under 0.01 for 1v2. Looking at the K* values across all temperature settings at θ=0.60, I'm seeing that three out of four configurations yield K*≥2, with one reaching K*=3—this is the strongest outcome we could hope for. Now I'm moving to exp-004 with the 7B model, which has a smaller dataset of 1K documents but should produce clearer signals than the 1.5B baseline, so I can compare the pairwise AUC scores across the available depth levels.

The 7B model shows strong performance with 1v2 at 0.695 and 0v1 reaching 0.998, while 2v3 sits at 0.612—this suggests K* is at least 3, though I can't determine if it goes higher given the depth constraints. For ordinal accuracy on the 4-class problem, I'm estimating around 0.475 based on the stronger signal strength compared to previous experiments.

Now I'm looking at exp-006, the downstream filtering experiment that's critical for C3. It involves 5 seeds with continued pretraining on contaminated data—mixing Qwen2.5-1.5B depth chain data with C4—then evaluating across MMLU and HellaSwag using six different filtering strategies: no-filter, binary-ours, binary-Drayson, graduated, surprisal-based, and DSIR. The graduated approach has an alpha sensitivity sweep, and the key metric is whether any strategy achieves at least a 2 percentage point improvement on at least one benchmark.

On MMLU, the graduated strategy hits 29.1% accuracy with optimal alpha around 0.5, which gives 2.5pp over binary-ours and 2.1pp over DSIR—both meeting the required thresholds. The other methods fall between the baseline of 25.4% and graduated's performance, with surprisal-based reaching 27.8% and the binary approaches around 26-27%. For HellaSwag, the baseline without filtering is 42.8% and binary-ours gets to 43%.

Generating markdown table...

Now I'm setting up experiment 008 to compare retraining with LoRA against the prompt-chaining baseline from experiment 001, expecting similar K* values but slightly degraded AUC due to adaptation noise. For experiment 009, I'm planning a dose-response study that varies synthetic data injection at different percentages to measure how the graduated approach scales compared to the binary baseline.

For experiment 011, I'm running zero-shot depth classification with both GPT-4o and Claude 3.5 Sonnet across 1000 samples, where GPT-4o achieves barely above-chance accuracy while Claude performs marginally better.

Now looking at experiment 012, I'm evaluating DivEye and Binoculars as depth proxies on language model chains—DivEye shows weak correlation with true depth but strong binary detection capability, while Binoculars performs similarly with slightly lower correlation metrics.

My 15-dimensional feature set substantially outperforms both baselines, achieving near-perfect binary discrimination and meaningfully better performance on the harder depth-ranking task.

For the naturalistic Common Crawl validation in experiment 014, predicted depth correlates negatively with quality indicators like AlignScore and vocabulary richness, with only a small fraction of samples predicted at higher depth levels.

Finally, comparing hand-crafted features against learned representations in experiment 015 shows the gap is minimal—less than 3 percentage points in AUC—suggesting the engineered features capture most of what a frozen embedding approach would learn. Looking at the 1v2 AUC results more carefully—the hand-crafted 15D features achieve 0.696 on the rewrite variant, while the frozen embeddings with MLP get 0.675, so the gap is actually around 2.1 percentage points, which fits the claim. But I need to verify which experiment variant (rewrite vs. continuous) I'm comparing, since the frozen embedding approach was specifically trained on Qwen2.5-1.5B.

For the canonical continuous mode, the 15D features hit 0.611 AUC while frozen embeddings are closer to 0.600, giving a 1.1pp gap. Either way, both comparisons stay well under the 3pp threshold. The frozen embeddings likely underperform slightly because the 1536-dimensional embeddings create overfitting risk with limited training data, and most of those dimensions probably encode information that's already captured in the simpler hand-crafted features.

Now I'm looking at the actual results from the experiments: the 15D approach achieves 0.611 AUC with 0.388 ordinal accuracy, while the frozen embeddings baseline gets around 0.597 AUC and 0.371 accuracy—a 1.4pp gap that still comfortably meets the requirement. This supports the interpretability argument for sticking with the hand-crafted features.

For the base model comparison, I'm expecting the untuned version to produce more diverse outputs since it hasn't been constrained by RLHF, which should actually strengthen the depth signal and push the 1v2 AUC higher to around 0.638. The information-theoretic regime stays at K*=2, but I need to think through how the base model's raw output distribution affects the 0v1 comparison—it's less clear whether that gets better or worse without the alignment pressure. I'm thinking through how base models might behave differently in continuation tasks—they'd likely produce more diverse outputs since they're not constrained by instruction-following, which could make successive generations easier to distinguish from each other. This suggests the depth signal might be a fundamental property of iterative generation rather than an artifact of the instruction tuning process. Now I need to finalize the metrics and identify which model configuration performed best to complete the analysis. Now I'm structuring the YAML output with all the required fields for each experiment—name, plan_id, description, expected results with detailed metrics, rationale for the predictions, tables, figures, and analysis sections. I need to make sure the predictions stay internally consistent across related experiments, like ensuring the Spearman ρ degradation patterns align between exp-003 and exp-007, the scaling relationships hold between exp-004 and the 7B results, and the dose-response curves in exp-006 match what exp-009 shows. Generating YAML output... narrative_guidance, I should update it based on the now-known actual results from completed experiments.

Actually, let me reconsider the numbers more carefully for exp-003.

The baseline for Qwen2.5-1.5B continuation is from exp-017: 1v2 AUC = 0.6114, with nucleus p=0.95 T=1.0.

For greedy decoding, the output becomes deterministic—each continuation is just the single most likely token sequence. This means gen-1 diverges sharply from human text since greedy lacks natural variability, but when I feed gen-1 through greedy again for gen-2, the model-like text produces similar model-like outputs. The specific content differs though, so there's still some variation. I'd expect 1v2 AUC around 0.582-0.590, which falls below the 0.60 threshold, suggesting K*=1.

For nucleus p=0.9, it's more restrictive than the p=0.95 baseline since it only keeps the top 90% probability mass instead of 95%, but that difference is fairly marginal in practice. The 1v2 AUC should stay very close to the baseline, maybe slightly lower—I'm estimating around 0.632.

But wait, that estimate seems inconsistent. If p=0.9 is more restrictive and produces less diversity, the AUC should actually be lower than the baseline, not higher. Less diversity means fewer distinguishing features between generations, which would reduce the separation signal. So 1v2 AUC should drop below 0.6114, possibly below 0.60, which would make K*=1.

That creates a problem though: if both greedy and p=0.9 yield K*=1, I'd only have two configs with K*=2 (the T=0.7 and T=1.2 variants), which doesn't meet the ≥3/4 requirement.

I need to think through the direction of this effect more carefully.

Looking at the actual results, there's competing dynamics at play. Higher diversity in outputs could mean more varied features for detection, pushing AUC up. But it could also introduce noise that obscures systematic differences, pushing AUC down. The data suggests the instruction-rewrite mode, which is more constrained, actually shows the highest AUC at 0.6957, while the less constrained continuation modes cluster lower around 0.61-0.65. This points toward the noise effect dominating—more constraint leads to clearer generational signals.

Now I'm reconsidering how decoding strategies fit in. Greedy decoding is deterministic, so it applies the same transformation consistently each time, which should make the pattern detectable. But the real question is whether gen-1 and gen-2 develop systematically different feature distributions that a classifier can latch onto.

The pattern emerging is that stochasticity drives change—higher temperature sampling introduces more variation between generations, making them easier to distinguish, while greedy's conservatism keeps consecutive generations more similar and thus harder to separate. So I'd expect greedy to show the lowest AUC, with performance improving as temperature increases.

But there's a complication: p=0.9 and T=0.7 might both fall below the baseline's 0.6114 threshold needed for K*=2, since they're reducing stochasticity compared to the baseline p=0.95 T=1.0 setup. The probability mass difference between p=0.9 and p=0.95 is relatively small though, so the effect might be subtle.

Looking at the experiment description more carefully, it seems to list four distinct conditions: greedy sampling, nucleus p=0.9, temperature T=0.7, and temperature T=1.2, which suggests these are separate configurations rather than combinations.

But thinking about how researchers typically design ablations, they'd vary one parameter at a time while keeping others fixed. So the most sensible interpretation is that the baseline uses nucleus p=0.95 and T=1.0, then they test greedy decoding, nucleus p=0.9 with T=1.0, nucleus p=0.95 with T=0.7, and nucleus p=0.95 with T=1.2. This gives me a clearer picture of what's being tested.

Looking at the expected effects on diversity and performance: reducing the nucleus parameter or lowering temperature should decrease diversity and hurt AUC, while increasing temperature should boost it. The actual results show greedy performs worst around 0.577 AUC, the nucleus p=0.9 variant sits around 0.607, the colder temperature variant lands near 0.603, and I'd expect the warmer temperature to perform best.

Across the four configurations, K* equals 2 in two cases, 3 in one, and 1 in the greedy baseline—so three out of four favor K*≥2. But I'm noticing those borderline cases where the 1v2 AUC barely crosses 0.60, which feels fragile. I'm wondering if I should tighten the threshold to make the best tier predictions more robust. I'm verifying that K*≥2 holds across three-quarters of the configurations and that K*=3 appears in the T=1.2 case, which establishes the narrative. The AUC values for the K*=2 configs cluster nicely in the [0.62, 0.70] range, though I need to bump up a couple of the lower values slightly to stay within bounds—adjusting the p=0.9 T=1.0 and p=0.95 T=0.7 cases to 0.628 and 0.624 respectively keeps everything aligned.

The p=0.95 T=1.2 config hits 0.682, and the 2v3 AUC of 0.622 confirms K*=3 is solid. For the Spearman correlation analysis, I'm expecting the feature degradation ordering to stay consistent with the baseline around ρ=0.87-0.92, which aligns with what I saw in the earlier experiments where continuation-mode comparisons held ρ≥0.85.

Now I need to refine the exp-006 predictions since it's actually running 5 seeds across 6 strategies with an α sensitivity sweep, not the smaller setup I initially sketched. The key distinction is between binary-ours (direct binary classifier on the 15D features) and graduated (ordinal decision on the same features), which isolates whether the ordinal framing helps. There's also binary-Drayson from the literature that uses importance resampling, but that's a separate method entirely. Let me get the YAML structured with these details in mind.

For the continued pretraining baseline, I'm estimating that a 1.5B model would start around 25-30% on MMLU and 45-50% on HellaSwag without filtering, then the contamination and filtering strategies would shift these by a few percentage points depending on how aggressively they remove data.

Now I'm thinking through the learned features experiment—comparing frozen embeddings with an MLP against hand-crafted 15D features, where the success criterion is keeping the gap under 3 percentage points in AUC. I need to figure out which AUC metric to use as the baseline for comparison. I'm verifying the Qwen-cont 1v2 AUC of 0.6112 with its confidence interval [0.6015, 0.6213], which suggests the lower bound should remain above 0.60 across repeated experiments, potentially even higher around 0.605. Now I'm writing out the YAML with all the experimental results, making sure to clearly specify the generation mode for each and cross-reference the data from exp-003 and exp-004 to support the stability claims.

For the 4-class ordinal accuracy on the 7B model with 1K docs, I'd expect it to outperform the 6-class baseline since there are fewer classes to distinguish—25% chance versus 16.7%—so if the 6-class best was around 0.4229, the 4-class version should land somewhere in the 0.52-0.55 range given the stronger signal from the smaller model.

Looking at the 7B experiment results, I'm seeing ordinal accuracy around 0.475 with ordinal MAE near 0.72, which is reasonable for this setup. Now I need to finalize the YAML output with all the required fields for each imagined experiment, making sure to include the narrative guidance that ties the best-tier results back to the paper's core claims.

Generating YAML output... Let me work through the remaining experiments. For exp-006, the downstream task results show consistent improvements across MMLU and HellaSwag with our graduated approach compared to baselines, with strong statistical significance. Exp-008 reveals that the prompt-chain variant achieves slightly better performance than the base K*=2 prediction. Looking at exp-009, there's a clear dose-response relationship where increasing the percentage of graduated examples yields progressively larger gains, peaking around 50%. I still need to compile the GPT-4o zero-shot results from exp-011 to complete the picture. I'm starting to write up the results now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ced1c672-c425-459b-871c-8654d57dc1b0",
  "isSidechain": false,
  "requestId": "req_011CazEAZ4KTksGQGPt5mzYu",
  "type": "assistant",
  "uuid": "07db6b83-5852-49ca-b8f6-e86be05944e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUrVDN9ekH2GVRLhC3bUfw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26580,
      "cache_read_input_tokens": 32873,
      "output_tokens": 32879,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26580,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32879,
          "cache_read_input_tokens": 32873,
          "cache_creation_input_tokens": 26580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26580
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

_source line 21 · 2026-05-13T08:21:00.209Z_

```yaml
tier: best
narrative_guidance: >
  C1' 全面成立 + C3 downstream 收益显著。exp-003 解码消融建立 K* 可调控梯度（greedy K*=1 → standard K*=2 → high-temp K*=3），
  直接消解 "K*=2 太浅" 审稿人顾虑。exp-004 7B 确认 scale → K* 因果链（K*≥3），与 exp-003 形成两条独立路径推高 K*。
  exp-006 graduated filtering 在 MMLU/HellaSwag 上均显著优于 binary（Δ≥2pp, p<0.01），exp-009 dose-response 单调递增。
  exp-015 15D hand-crafted features 与 frozen embeddings 差距 <1.5pp，支撑 interpretable features 叙事。
  Qwen-cont 的 0.0015 margin 脆弱性被 exp-003 新 configs 的一致 K*=2 所补偿——多条件汇聚证据远强于单点 CI。
  所有完成实验的实际数据与 best 档预测高度一致，原始 2+1 claim 结构可直接支撑 EMNLP 2026 Main，reviewer score 预期 3.5-4.0。

imagined_experiments:
  - name: "Qwen2.5-1.5B 解码策略消融"
    plan_id: "exp-003"
    description: >
      Qwen2.5-1.5B-Instruct continuation mode, C4 5K docs, depth 0-5,
      4 解码配置: greedy / nucleus p=0.9 T=1.0 / nucleus p=0.95 T=0.7 / nucleus p=0.95 T=1.2。
      Baseline 为 exp-017 (nucleus p=0.95, T=1.0, continuation): 1v2 AUC=0.6114, K*=2。
    expected_results:
      greedy:
        k_star: 1
        pairwise_auc:
          0v1: 0.9965
          1v2: 0.5862
          2v3: 0.5481
          3v4: 0.5225
          4v5: 0.5108
        pairwise_jsd:
          0v1: 0.2753
          1v2: 0.0038
          2v3: 0.0029
          3v4: 0.0022
          4v5: 0.0019
        ordinal_accuracy: 0.3412
      nucleus_p0.9_T1.0:
        k_star: 2
        pairwise_auc:
          0v1: 0.9968
          1v2: 0.6278
          2v3: 0.5582
          3v4: 0.5312
          4v5: 0.5124
        pairwise_jsd:
          0v1: 0.2814
          1v2: 0.0057
          2v3: 0.0035
          3v4: 0.0028
          4v5: 0.0024
        ordinal_accuracy: 0.3685
      T0.7_p0.95:
        k_star: 2
        pairwise_auc:
          0v1: 0.9963
          1v2: 0.6241
          2v3: 0.5558
          3v4: 0.5286
          4v5: 0.5115
        pairwise_jsd:
          0v1: 0.2685
          1v2: 0.0052
          2v3: 0.0033
          3v4: 0.0026
          4v5: 0.0022
        ordinal_accuracy: 0.3648
      T1.2_p0.95:
        k_star: 3
        pairwise_auc:
          0v1: 0.9981
          1v2: 0.6823
          2v3: 0.6218
          3v4: 0.5614
          4v5: 0.5305
        pairwise_jsd:
          0v1: 0.3082
          1v2: 0.0118
          2v3: 0.0056
          3v4: 0.0035
          4v5: 0.0027
        ordinal_accuracy: 0.3975
      cross_config_spearman_rho_feature_ordering:
        greedy_vs_baseline: 0.886
        p0.9_vs_baseline: 0.921
        T0.7_vs_baseline: 0.914
        T1.2_vs_baseline: 0.878
      k_star_summary: "K*=2 in 3/4 configs (p=0.9, T=0.7, T=1.2≥2); K*=1 for greedy; K*=3 for T=1.2"
    result_rationale: >
      解码策略通过控制 token 采样的有效熵，直接调控递归信道的信息保持率。
      Greedy 解码（argmax）将输出钉死在条件分布的 mode 上：gen-1 已高度确定性，gen-2 对 gen-1 施加相同的 argmax 压缩后几乎无新增信息损失可测——
      因此 1v2 AUC=0.586 低于 θ=0.60 阈值，K*=1。这不是检测失败，而是 greedy 信道本身在首代就完成了绝大部分信息丢弃。
      p=0.9（vs baseline p=0.95）仅移除尾部 5% 概率质量的差异，效应量小——1v2 AUC 从 0.611 降到 0.628，仍稳定在 K*=2。
      T=0.7 压缩 softmax 温度使分布更 peaked，效应与收窄 nucleus 类似，1v2=0.624 保持 K*=2。
      T=1.2 是关键条件：高温度展平分布→每代输出保留更多"非主流" token 选择→这些 tail tokens 携带的分布结构需要更多代际才能被递归"洗掉"。
      信息论机制：T=1.2 抬高了初始互信息 I(X;Y₁)，DPI 保证 I(X;Yₖ) 单调递减，但更高起点意味着 2v3 AUC=0.622 仍高于 0.60→K*=3。
      Feature ordering 一致性（ρ≥0.878）表明解码策略改变信号强度但不改变哪些特征最先饱和——退化顺序是信息论结构性规律。
    tables:
      - caption: "解码策略消融: K* 与关键 pairwise AUC"
        columns: [decoding_config, K*, AUC_0v1, AUC_1v2, AUC_2v3, AUC_3v4, JSD_0v1]
        rows:
          - [greedy, 1, 0.9965, 0.5862, 0.5481, 0.5225, 0.2753]
          - ["nucleus p=0.9 T=1.0", 2, 0.9968, 0.6278, 0.5582, 0.5312, 0.2814]
          - ["p=0.95 T=0.7", 2, 0.9963, 0.6241, 0.5558, 0.5286, 0.2685]
          - ["p=0.95 T=1.2", 3, 0.9981, 0.6823, 0.6218, 0.5614, 0.3082]
          - ["baseline (p=0.95 T=1.0)", 2, 0.9972, 0.6114, 0.5609, 0.5408, 0.2863]
      - caption: "Feature degradation ordering 一致性 (Spearman ρ vs baseline)"
        columns: [config, spearman_rho]
        rows:
          - [greedy, 0.886]
          - [p=0.9, 0.921]
          - [T=0.7, 0.914]
          - [T=1.2, 0.878]
    figures_description:
      - "K* vs 解码有效熵散点图: x轴为各解码配置的实际 token 分布熵估计，y轴为 K*。Greedy 在最左 K*=1，standard configs 居中 K*=2，T=1.2 在最右 K*=3，形成清晰阶跃。"
      - "五配置 JSD decay 曲线族谱图: T=1.2 曲线在 depth=3 才穿过 θ=0.60 对应的 JSD 阈值线，greedy 在 depth=1 就穿过，其余在 depth=2。"
      - "Bootstrap CI 对比图: 各配置的 1v2 AUC 95% CI 与 θ=0.60 阈值线的关系，视觉化 K* 判定。"
    analysis: >
      T=1.2 → K*=3 + greedy → K*=1 建立了完整的 K* 可调控梯度，这是论文最有力的发现之一。
      审稿人无法再说 "K*=2 is a ceiling"——它是 standard 解码下的 operating point，可被解码熵上下调控。
      3/4 configs K*≥2 表明 K*=2 在合理解码空间内高度稳健；greedy 的 K*=1 不是弱点而是优势：
      它证明 K* 捕捉的是信道的真实信息论性质，而非分类器的统计 artifact。
      Feature ordering ρ≥0.878 跨所有配置，扩展了 exp-005 的 degradation ordering 一致性结论到新解码条件。

  - name: "Qwen2.5-7B 跨规模探测"
    plan_id: "exp-004"
    description: >
      Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3。
      测试模型规模是否是 K* 的杠杆。1K docs（vs 5K）引入更大方差但降低 GPU 成本。
    expected_results:
      pairwise_auc:
        0v1: 0.9984
        1v2: 0.6948
        2v3: 0.6175
      pairwise_auc_std:
        0v1: 0.0004
        1v2: 0.0092
        2v3: 0.0108
      pairwise_jsd:
        0v1: 0.3415
        1v2: 0.0285
        2v3: 0.0112
      k_star: 3
      ordinal_accuracy_4class: 0.4752
      ordinal_mae: 0.7240
      bootstrap_ci_1v2: [0.6782, 0.7108]
      bootstrap_ci_2v3: [0.6015, 0.6338]
      top3_features:
        - surp_d1_std
        - surp_std
        - freq_entropy
      comparison_vs_1.5B:
        delta_auc_1v2: "+0.0834"
        delta_auc_2v3: "+0.0566"
        delta_jsd_0v1: "+0.0552"
    result_rationale: >
      7B 模型的参数空间是 1.5B 的 ~4.7 倍，编码了更丰富的语言分布。递归生成时，每代输出保留更多原始分布的细微结构：
      rare n-grams、长距离 discourse patterns、低频词汇的上下文相关用法。这些信息在 1.5B 级模型中首代就大部分丢失，
      但在 7B 中至少保持到第二代——因此 2v3 AUC=0.618 仍高于 θ=0.60，K*≥3。
      具体机制：7B 的 next-token 分布有更长的"有意义尾巴"（tail tokens 仍携带语义区分力），
      递归第二代保留了这些 tail 的部分结构特征，到第三代才显著丢失。
      1v2 AUC=0.695 较 1.5B 的 0.611 提升 8.3pp，JSD_0v1=0.342 较 1.5B 的 0.286 提升 19%——
      更大模型的输出在特征空间中占据更大体积，递归压缩的"距离"更长。
      1K docs 的样本量约束使 CI 较宽（±0.015 vs 5K docs 的 ±0.010），但 2v3 CI lower=0.602 仍 comfortably 高于 0.60。
      Ordinal accuracy 4-class=0.475（chance=0.25），MAE=0.724，均显著优于 1.5B 的 6-class 表现，
      确认更多参数→更多可利用的代际特征梯度。
    tables:
      - caption: "Qwen2.5-7B vs 1.5B pairwise discrimination 对比"
        columns: [depth_pair, 7B_AUC, 7B_JSD, 1.5B_AUC_cont, 1.5B_JSD_cont]
        rows:
          - [0v1, 0.9984, 0.3415, 0.9972, 0.2863]
          - [1v2, 0.6948, 0.0285, 0.6114, 0.0051]
          - [2v3, 0.6175, 0.0112, 0.5609, 0.0036]
      - caption: "7B bootstrap 95% CI"
        columns: [depth_pair, AUC, CI_lower, CI_upper, "CI_lower > 0.60?"]
        rows:
          - [1v2, 0.6948, 0.6782, 0.7108, "✅ +7.8pp"]
          - [2v3, 0.6175, 0.6015, 0.6338, "✅ +0.15pp"]
    figures_description:
      - "Scale-K* 关系图: x轴为模型参数量（log scale: 1B, 1.4B, 1.5B, 7B），y轴为 K*。1B-1.5B 区间 K*=2 稳定，7B 跳到 K*=3。虚线外推暗示更大模型 K*≥4。"
      - "7B vs 1.5B JSD decay 对比: 7B 曲线整体上移且右移，穿过 θ 阈值的 depth 更深，视觉化 scale → K* 效应。"
    analysis: >
      7B K*≥3 确认模型规模是 K* 的因果杠杆，与 exp-003 T=1.2 → K*=3 形成两条独立路径。
      结合两者可写: "K*=2 is not a ceiling but a floor that rises with model scale (7B) and decoding entropy (T=1.2)."
      2v3 CI lower=0.602 虽然 margin 较小（受 1K docs 限制），但方向明确且与 1v2 的强信号一致。
      如需更强统计力度，可考虑增至 2K docs（额外 4 GPU-hours），但当前结果已足以支撑 claim。
      对 ordinal_accuracy_best_model 的贡献: 7B 4-class=0.475 落入 best 档范围 [0.42, 0.48]。

  - name: "Downstream graduated filtering 评估"
    plan_id: "exp-006"
    description: >
      Qwen2.5-1.5B depth chain (continuation mode), 比较 6 种过滤策略:
      no-filter / binary-ours (15D binary) / binary-Drayson (importance resampling) / graduated (3-class ordinal) /
      surprisal-based (单特征) / DSIR (分布匹配)。Continued pretraining + lm-eval-harness (MMLU, HellaSwag)。
      5 seeds, paired t-test。graduated 加 α sensitivity sweep (α ∈ {0.1, 0.3, 0.5, 0.7, 0.9})。
    expected_results:
      mmlu_accuracy_pp:
        no_filter: 25.82
        binary_ours: 26.93
        binary_drayson: 27.21
        graduated_best_alpha: 29.41
        surprisal_based: 28.15
        dsir: 27.32
      hellaswag_accuracy_pp:
        no_filter: 43.24
        binary_ours: 44.38
        binary_drayson: 44.65
        graduated_best_alpha: 47.08
        surprisal_based: 45.92
        dsir: 44.81
      mmlu_std_5seeds:
        no_filter: 0.21
        binary_ours: 0.28
        binary_drayson: 0.32
        graduated: 0.25
        surprisal_based: 0.33
        dsir: 0.30
      hellaswag_std_5seeds:
        no_filter: 0.18
        binary_ours: 0.23
        binary_drayson: 0.27
        graduated: 0.20
        surprisal_based: 0.28
        dsir: 0.25
      key_deltas:
        graduated_minus_binary_ours_mmlu_pp: 2.48
        graduated_minus_binary_ours_hellaswag_pp: 2.70
        graduated_minus_dsir_mmlu_pp: 2.09
        graduated_minus_dsir_hellaswag_pp: 2.27
      paired_ttest_pvalues:
        graduated_vs_binary_ours_mmlu: 0.0043
        graduated_vs_binary_ours_hellaswag: 0.0067
        graduated_vs_dsir_mmlu: 0.0125
        graduated_vs_dsir_hellaswag: 0.0098
      alpha_sensitivity_mmlu:
        alpha_0.1: 27.45
        alpha_0.3: 28.72
        alpha_0.5: 29.41
        alpha_0.7: 29.08
        alpha_0.9: 28.14
      alpha_sensitivity_hellaswag:
        alpha_0.1: 44.85
        alpha_0.3: 46.28
        alpha_0.5: 47.08
        alpha_0.7: 46.72
        alpha_0.9: 45.65
      optimal_alpha: 0.5
    result_rationale: >
      Binary filtering 的核心困境: gen-1 文本保留了原始文本 ~85% 的信息（0v1 AUC>0.99 说明 gen-1 与 human 可区分，
      但 1v2 AUC~0.61 说明 gen-1 仍保留了大部分质量）。Binary 策略要么丢掉这些高质量 gen-1（过严→训练数据量骤降），
      要么连 gen-2+ 一起保留（过松→引入已过 K* 的噪声数据）。
      Graduated filtering 通过 3-class ordinal signal 精确解耦: 对 gen-1 施加 α 衰减权重（降低但不移除），
      对 gen-2+ 完全移除。最优 α=0.5 意味着 gen-1 以半权重参与训练——保留了其信息价值同时抑制了合成偏差。
      MMLU 收益（+2.48pp）高于 HellaSwag，因为 MMLU 对知识密度更敏感：graduated 保留的 gen-1 中知识保真度高，
      binary 移除后的知识缺口比常识推理缺口更难弥补。
      Binary-Drayson 的 importance resampling 略优于 binary-ours（soft vs hard 决策边界），但仍做二值判断→无法利用 ordinal signal。
      DSIR 做分布匹配但不估计 depth→对 depth-specific 污染效果有限。
      Surprisal-based 策略用单一特征（surprisal mean）做 proxy filtering，优于 binary 但不及 graduated 的多维 ordinal signal。
      α sensitivity 呈倒 U 形: α 太小（0.1）几乎等于 binary 移除，α 太大（0.9）几乎等于 no-filter。
      5 seeds paired t-test p<0.01 确认 graduated vs binary-ours 的差异非采样噪声。
    tables:
      - caption: "6 策略 downstream 评估 (5 seeds mean ± std)"
        columns: [strategy, MMLU_pp, MMLU_std, HellaSwag_pp, HS_std]
        rows:
          - [no-filter, 25.82, 0.21, 43.24, 0.18]
          - [binary-ours, 26.93, 0.28, 44.38, 0.23]
          - [binary-Drayson, 27.21, 0.32, 44.65, 0.27]
          - [graduated (α=0.5), 29.41, 0.25, 47.08, 0.20]
          - [surprisal-based, 28.15, 0.33, 45.92, 0.28]
          - [DSIR, 27.32, 0.30, 44.81, 0.25]
      - caption: "关键对比统计显著性 (paired t-test, 5 seeds)"
        columns: [comparison, Δ_MMLU_pp, p_MMLU, Δ_HellaSwag_pp, p_HellaSwag]
        rows:
          - [graduated vs binary-ours, 2.48, 0.0043, 2.70, 0.0067]
          - [graduated vs DSIR, 2.09, 0.0125, 2.27, 0.0098]
          - [graduated vs binary-Drayson, 2.20, 0.0082, 2.43, 0.0054]
          - [graduated vs surprisal-based, 1.26, 0.0318, 1.16, 0.0425]
      - caption: "α sensitivity sweep (graduated, MMLU)"
        columns: [α, MMLU_pp, HellaSwag_pp]
        rows:
          - [0.1, 27.45, 44.85]
          - [0.3, 28.72, 46.28]
          - [0.5, 29.41, 47.08]
          - [0.7, 29.08, 46.72]
          - [0.9, 28.14, 45.65]
    figures_description:
      - "6 策略 benchmark bar chart (error bars = 1 std over 5 seeds): graduated 最高，与 binary-ours 之间有清晰 gap。"
      - "α sensitivity curve (倒 U 形): 最优 α=0.5，α→0 趋向 binary 性能，α→1 趋向 no-filter 性能。"
      - "Filtering precision-recall 在 gen-1 附近: graduated 的 calibrated soft boundary vs binary 的 hard step function，视觉化 ordinal signal 的阈值优势。"
    analysis: >
      graduated vs binary-ours Δ≥2.48pp (MMLU) 和 2.70pp (HellaSwag) 均落入 best 档 [2.0, 4.0] 且 p<0.01。
      C3 成立: 即使 K*=2 的粗粒度 3-class ordinal signal 也能在 downstream 产生显著收益。
      Binary-ours vs graduated 的唯一变量是 binary/ordinal decision→公平验证了 ordinal structure 的价值。
      DSIR 和 binary-Drayson 的存在证明 graduated 的优势不仅来自"更好的 filtering"而是来自 depth-aware 决策。
      α=0.5 的最优性直观: gen-1 质量约为 human 的 ~85%（基于 1v2 AUC），半权重大致反映这个质量折扣。

  - name: "Retrain-chain 生态效度验证"
    plan_id: "exp-008"
    description: >
      Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain vs prompt-chain,
      C4 5K docs, depth 0-4。验证 prompt-chain 是否是 retrain-chain 的合理实验代理。
    expected_results:
      retrain_chain:
        k_star: 2
        pairwise_auc:
          0v1: 0.9895
          1v2: 0.6362
          2v3: 0.5448
          3v4: 0.5128
        pairwise_jsd:
          0v1: 0.2058
          1v2: 0.0118
          2v3: 0.0044
          3v4: 0.0029
      prompt_chain_actual:
        k_star: 2
        pairwise_auc:
          0v1: 0.9932
          1v2: 0.6539
          2v3: 0.5515
          3v4: 0.5153
      kstar_diff: 0
      auc_1v2_diff: -0.0177
      feature_distribution_jsd_retrain_vs_prompt:
        depth_0: 0.0018
        depth_1: 0.0162
        depth_2: 0.0285
        depth_3: 0.0378
      cross_method_transfer_retention: 0.915
    result_rationale: >
      LoRA rank=16 (alpha=32) 只修改了参数空间中一个 16 维的低秩子空间，
      实际参数变化量 < 模型总参数的 0.2%——这意味着 retrain-chain 的每代"模型"与原始 Pythia-1.4B 高度相似。
      因此 retrain-chain 的行为应近似于 prompt-chain：两者都是同一个（或近似相同的）模型对自身输出的迭代。
      K* diff=0：DPI 约束是拓扑性的——只要信道是有损的（LoRA 微调后仍是有损信道），收敛行为保持。
      AUC 差异 -0.018：retrain-chain 略低，因为 LoRA 微调在每代引入微小但累积的分布偏移，
      这些偏移模糊了"纯递归"的代际边界——相当于在递归信道上叠加了一层 adaptation noise。
      Feature distribution JSD 随 depth 递增是预期行为：更深代际累积了更多 retrain 偏移。
      但 JSD < 0.04 在所有 depth，远低于代际间的 JSD（~0.01-0.21），
      确认 prompt-chain 的代际差异主导了 retrain 偏移效应。
      Cross-method transfer retention 91.5%: prompt-chain 上训练的 classifier 在 retrain-chain 上保持高性能。
    tables:
      - caption: "Retrain-chain vs prompt-chain 对比 (Pythia-1.4B)"
        columns: [depth_pair, retrain_AUC, prompt_AUC, Δ_AUC]
        rows:
          - [0v1, 0.9895, 0.9932, -0.0037]
          - [1v2, 0.6362, 0.6539, -0.0177]
          - [2v3, 0.5448, 0.5515, -0.0067]
          - [3v4, 0.5128, 0.5153, -0.0025]
      - caption: "Feature 分布偏移 (retrain vs prompt JSD by depth)"
        columns: [depth, JSD]
        rows:
          - [0, 0.0018]
          - [1, 0.0162]
          - [2, 0.0285]
          - [3, 0.0378]
    figures_description:
      - "Retrain vs prompt JSD decay 对比: 两条曲线近乎重叠，附 bootstrap 95% CI shading。"
      - "Feature space t-SNE: retrain 和 prompt 在同一 depth 的点高度混合，depth 之间有清晰分离。不同颜色区分 method，不同标记区分 depth。"
    analysis: >
      K* diff=0 且 AUC 差异 < 2pp，直接回应 "prompt-chain 不代表真实递归污染" 的审稿人顾虑。
      Prompt-chain 作为 controlled proxy 的生态效度得到确认。
      Feature JSD 随 depth 缓慢递增的模式可作为 supplementary 报告:
      它表明 retrain adaptation 的效应虽然累积但始终被代际退化信号所主导。
      Cross-method transfer 91.5% 与 exp-013 的 Pythia↔OLMo 91-92% 一致——
      换言之，prompt vs retrain 的差异与同族不同模型的差异量级相当。

  - name: "Contamination dose-response"
    plan_id: "exp-009"
    description: >
      10%/30%/50% synthetic injection 比例下 graduated vs binary filtering 的收益差异。
      基于 exp-006 的实验框架，仅变化 injection 比例。5 seeds, MMLU+HellaSwag。
    expected_results:
      graduated_vs_binary_delta_mmlu_pp:
        injection_10pct: 0.72
        injection_30pct: 2.48
        injection_50pct: 3.82
      graduated_vs_binary_delta_hellaswag_pp:
        injection_10pct: 0.51
        injection_30pct: 2.70
        injection_50pct: 3.48
      graduated_vs_binary_pvalue_mmlu:
        injection_10pct: 0.142
        injection_30pct: 0.0043
        injection_50pct: 0.0008
      graduated_vs_binary_pvalue_hellaswag:
        injection_10pct: 0.218
        injection_30pct: 0.0067
        injection_50pct: 0.0012
      trend: "monotonically increasing with injection rate"
      significance_threshold_pct: "~20% injection for p<0.05"
    result_rationale: >
      10% injection 时，训练数据中仅 10% 是合成文本（其中 gen-1 约 5%，gen-2+ 约 5%），
      binary 策略移除全部 10% 的信息损失较小，错分 gen-1 的代价也小（因为总量少）→graduated 的边际收益有限（<1pp, p>0.05）。
      30% 对应 exp-006 主实验条件，graduated 优势 ~2.5pp。
      50% injection 是 graduated 价值最大化的条件: 半数数据是合成的，其中 gen-1 占 ~25% 的全部训练数据。
      Binary 面临极端权衡——移除全部 50% 导致训练数据减半（catastrophic data loss），
      保留则引入 ~25% gen-2+ 噪声。Graduated 精确解耦: gen-1 以 α=0.5 权重保留→等效保留 12.5% 高质量数据，
      gen-2+ 移除→等效移除 25% 噪声。净效果: graduated 比 binary 多保留 12.5% 有用数据同时多移除等量噪声。
      单调递增趋势是 C3 的核心叙事: "The value of depth-aware curation scales with contamination severity."
    tables:
      - caption: "Dose-response: graduated vs binary Δ by contamination rate"
        columns: [injection_rate, Δ_MMLU_pp, p_MMLU, Δ_HellaSwag_pp, p_HellaSwag]
        rows:
          - ["10%", 0.72, 0.142, 0.51, 0.218]
          - ["30%", 2.48, 0.0043, 2.70, 0.0067]
          - ["50%", 3.82, 0.0008, 3.48, 0.0012]
    figures_description:
      - "Dose-response curve: x轴 injection rate, y轴 graduated−binary Δ (pp)。MMLU/HellaSwag 两条线均单调递增。横虚线标注 2pp 和 p=0.05 阈值。"
      - "Stacked bar: 各 injection rate 下 no-filter/binary/graduated 绝对性能对比。随着 injection rate 升高，no-filter 下降最快，graduated 最稳健。"
    analysis: >
      单调递增的 dose-response 关系是 graduated filtering 实际部署价值的最直接证据。
      10% injection 下 p>0.05 是预期中的——低污染率下任何 filtering 策略都足够好，无需精细化。
      50% injection 下 Δ=3.82pp (MMLU) 落入 best 档上限附近 [2.0, 4.0]。
      这为 practical impact 叙事提供核心论据: 当前 web 数据合成文本比例估计 15-30%（且在增长），
      graduated filtering 在这个区间恰好开始产生统计显著收益，随比例增长价值越大。

  - name: "LLM zero-shot depth estimation baseline"
    plan_id: "exp-011"
    description: >
      GPT-4o / Claude 3.5 Sonnet 对 depth 0-4 文本做 zero-shot depth 判断。
      200 samples per depth (共 1000 样本), 5-class classification。
      验证 depth estimation 不能被 frontier LLM 的通用能力"免费"解决。
    expected_results:
      gpt4o:
        accuracy: 0.218
        mae: 1.742
        kendall_tau_with_true_depth: 0.082
        confusion_matrix_diagonal_pct: 0.218
      claude_3_5_sonnet:
        accuracy: 0.234
        mae: 1.668
        kendall_tau_with_true_depth: 0.118
        confusion_matrix_diagonal_pct: 0.234
      our_ordinal_classifier:
        accuracy: 0.423
        mae: 0.984
        kendall_tau_with_true_depth: 0.552
      random_baseline:
        accuracy: 0.200
        mae: 2.000
      llm_common_failure_mode: "LLM 倾向将所有文本判为 depth 0 或 1，几乎不预测 depth≥3"
    result_rationale: >
      LLM zero-shot depth estimation 近乎随机，三个结构性原因:
      (1) Depth signal 是统计性的——需要同一 domain 的多样本分布对比，单文本缺乏参照系。
      LLM 每次只看一篇文本，无法感知"这篇相对于同源文本的 vocabulary diversity 降低了多少"。
      (2) LLM 的"质量判断"偏向 fluency/coherence/factuality，而这些高层语义特征恰恰是最后才饱和的（与 C2 degradation ordering 一致）。
      即使 gen-3 的 vocabulary diversity 已严重退化，LLM 仍判定其"写得不错"因为它仍然 fluent。
      (3) Depth 是一个 training-data 中从未出现过的概念——LLM 没有被训练理解"递归生成导致的信息损失梯度"，
      其世界模型中不存在"第 N 代合成文本"这个 schema。
      Claude 略优于 GPT-4o（差异在 noise range 内）可能反映 Claude 对文本微妙模式的 slightly better sensitivity。
      两者均远低于 15D ordinal classifier（accuracy 0.42 vs 0.22），倍率 ~1.9x。
    tables:
      - caption: "Zero-shot depth estimation: frontier LLM vs ordinal classifier"
        columns: [method, accuracy, MAE, Kendall_τ]
        rows:
          - [GPT-4o (zero-shot), 0.218, 1.742, 0.082]
          - [Claude 3.5 Sonnet (zero-shot), 0.234, 1.668, 0.118]
          - [Random baseline, 0.200, 2.000, 0.000]
          - [Our ordinal classifier (15D), 0.423, 0.984, 0.552]
    figures_description:
      - "Confusion matrix 三面板: LLM 预测分布近乎 uniform（微偏向 depth 0-1），ordinal classifier 对角线主导。"
      - "Per-depth accuracy breakdown: LLM 在 depth=0 的 accuracy 最高（~0.35）但仍低于 classifier（~0.70），depth≥2 完全随机。"
    analysis: >
      LLM zero-shot 仅比 random chance 高 1.8-3.4pp，而 ordinal classifier 高出 22.3pp。
      这确立了 depth estimation 作为需要专门方法的 task——不能被 frontier LLM 的 general intelligence "免费"解决。
      这是论文 problem formulation 的关键支撑: 我们定义的问题是 genuinely novel 且有技术门槛的。
      LLM 偏向预测 depth=0/1 的 failure mode 与 C2 一致——高层语义质量在前几代保持，
      导致 LLM "认为大部分文本都是 human-written 或 first-generation"。

  - name: "Binary detector confidence 作为 depth proxy"
    plan_id: "exp-012"
    description: >
      DivEye / Binoculars score 与 true depth 的 Spearman correlation,
      在 exp-001 (Pythia) 和 exp-002 (OLMo) depth chain 上评估。
    expected_results:
      diveye:
        spearman_rho_with_depth: 0.223
        spearman_p_value: 0.001
        auc_0v1: 0.935
        auc_1v2: 0.528
        auc_2v3: 0.508
      binoculars:
        spearman_rho_with_depth: 0.184
        spearman_p_value: 0.003
        auc_0v1: 0.912
        auc_1v2: 0.521
        auc_2v3: 0.505
      our_15d_features:
        auc_0v1: 0.9950
        auc_1v2: 0.6340
        auc_2v3: 0.5505
      binary_score_depth_correlation_interpretation: >
        Binary scores 在 depth=0→1 处有大跳跃然后 plateau——
        所有 depth≥1 的合成文本在 binary score 空间中挤在一个窄 band 内。
    result_rationale: >
      Binary detectors 的训练目标是最大化 real/synthetic 决策边界，不是估计 "how synthetic"。
      其 confidence score 在 depth=0→1 跳跃后迅速饱和，原因:
      (1) DivEye 和 Binoculars 使用的 summary statistics（如 min-k% perplexity、cross-entropy ratio）
      在 gen-1 就已经偏离 human 文本的分布，之后 gen-2→gen-5 的偏移量极小（增量 < noise）。
      (2) 这些 detectors 被优化为在 human/synthetic 边界处有最大 separability——
      边界远处（depth≥2）的分辨力从未被训练目标所选择。
      Spearman ρ 显著但极弱（0.18-0.22），因为 depth=0 vs depth≥1 的 rank 差异贡献了大部分 correlation，
      depth≥1 内部几乎无 rank 信息。
      DivEye 略优于 Binoculars 因为其 vocabulary diversity 相关特征恰好也编码了少量 depth 信息。
      关键对比: 我们的 15D features 在 1v2 AUC 上高出 binary detectors ~10pp，
      证明 binary confidence ≠ depth，depth estimation 需要专用特征。
    tables:
      - caption: "Binary detector scores 作为 depth proxy"
        columns: [detector, Spearman_ρ, p_value, AUC_0v1, AUC_1v2, AUC_2v3]
        rows:
          - [DivEye, 0.223, 0.001, 0.935, 0.528, 0.508]
          - [Binoculars, 0.184, 0.003, 0.912, 0.521, 0.505]
          - [Our 15D features, "—", "—", 0.995, 0.634, 0.551]
    figures_description:
      - "Binary score vs true depth scatter: score 在 depth=0→1 有大跳跃，depth≥1 几乎平坦 (ceiling effect)。附 LOESS smooth line。"
      - "Pairwise AUC decay 对比: binary detectors 在 1v2 处即降至 chance level，我们的 features 保持到 depth=2。"
    analysis: >
      Binary detectors 在 0v1 处强劲（AUC 0.91-0.94）但 1v2 处近乎 chance level（0.52-0.53），
      直接证明 "binary detection ≠ depth estimation"。
      这是论文 related work positioning 的关键数据: existing methods solve a different (easier) problem。
      Spearman ρ 的统计显著性反映的是 binary 信号本身（depth=0 vs all），而非 ordinal depth estimation 能力。

  - name: "Common Crawl 自然验证"
    plan_id: "exp-014"
    description: >
      对 Common Crawl 2025/2026 snapshot 10K 样本做 depth 预测，
      与 AlignScore (事实一致性) 和 vocabulary richness 指标做 correlation。
      无 ground truth，仅间接验证。
    expected_results:
      spearman_predicted_depth_vs_alignscore: -0.288
      spearman_predicted_depth_vs_vocab_richness: -0.342
      spearman_p_values:
        alignscore: "<0.001"
        vocab_richness: "<0.001"
      pct_samples_predicted_depth_geq_1: 17.5
      pct_samples_predicted_depth_geq_2: 6.8
      pct_samples_predicted_depth_geq_3: 2.1
      predicted_depth_distribution:
        depth_0: 82.5
        depth_1: 10.7
        depth_2: 4.7
        depth_3_plus: 2.1
    result_rationale: >
      Common Crawl 中的真实合成文本比例和代际深度无 ground truth，只能通过与外部质量指标的 correlation 间接验证。
      Predicted depth 与 AlignScore 呈负相关（ρ≈-0.29），因为更深代际的文本在递归"电话游戏"中积累了更多事实偏差。
      与 vocabulary richness 的负相关更强（ρ≈-0.34），与 C2 degradation ordering 一致:
      vocabulary diversity 是最先退化的特征组，predicted depth 高的文本确实词汇更贫乏。
      ~17.5% 样本被预测为 depth≥1 与 2025-2026 时期 web 合成文本比例的外部估计（15-25%）一致。
      Depth≥2 仅 6.8%——大部分合成文本是"首代"（直接由模型生成），多代递归仍是小众现象。
      相关性不高（|ρ|<0.35）是预期中的: wild data 的噪声（domain 多样性、unknown model 族、未知解码策略）
      稀释了在 controlled 实验中观察到的信号。这些结果属于 "proof of concept" 级别。
    tables:
      - caption: "Common Crawl 自然验证"
        columns: [metric, value]
        rows:
          - ["Spearman(pred depth, AlignScore)", -0.288]
          - ["Spearman(pred depth, vocab richness)", -0.342]
          - ["% pred depth ≥ 1", "17.5%"]
          - ["% pred depth ≥ 2", "6.8%"]
          - ["% pred depth ≥ 3", "2.1%"]
    figures_description:
      - "Predicted depth 分布直方图: depth=0 占 82.5%，depth=1 占 10.7%，depth=2+ 占 6.8%。"
      - "Predicted depth vs AlignScore scatter (LOESS smooth): 清晰下降趋势但散点稀疏。"
      - "Predicted depth vs vocabulary richness scatter: 负相关趋势更清晰。"
    analysis: >
      自然验证提供 "proof of concept" 级别的 wild-data 证据。
      相关性方向正确且显著，足以支持 appendix 或 discussion section 的 generalizability 论述。
      不足以作为 main claim 的证据但有效回应 "只在 controlled 设置下验证" 的审稿人顾虑。
      Predicted depth 分布与 web 合成文本比例估计的一致性增加了 classifier 的可信度。

  - name: "Learned representation baseline"
    plan_id: "exp-015"
    description: >
      Frozen Qwen2.5-1.5B embeddings (last hidden state, 1536-dim) + 2-layer MLP
      vs hand-crafted 15D features + LightGBM。在 Qwen continuation depth chain 上评估。
    expected_results:
      frozen_embeddings_mlp:
        auc_1v2: 0.5982
        mean_pw_auc: 0.5865
        ordinal_accuracy: 0.3708
        mae: 1.195
        training_time_gpu_hours: 2.6
        feature_dim: 1536
      handcrafted_15d:
        auc_1v2: 0.6112
        mean_pw_auc: 0.6048
        ordinal_accuracy: 0.3875
        mae: 1.155
        training_time_gpu_hours: 0.08
        feature_dim: 15
      gap_auc_1v2_pp: 1.30
      gap_mean_pw_auc_pp: 1.83
      gap_ordinal_accuracy_pp: 1.67
      cross_model_transfer_frozen:
        frozen_on_qwen_test_pythia_retention: 0.62
        handcrafted_on_qwen_test_pythia_retention: 0.85
    result_rationale: >
      Frozen embeddings 包含丰富的语义信息但存在三个结构性劣势:
      (1) 1536 维中绝大部分编码内容语义（topic, entity, style），而非递归退化信号——
      MLP 需要从高维空间中"挖掘"少数相关维度。在 5K 训练样本下，这个搜索问题容易过拟合。
      (2) Frozen embeddings 来自同一模型（Qwen2.5-1.5B），引入自我参照偏差:
      模型对自己生成的文本有系统性 embedding 偏向，但这种偏向在 cross-model 设置下不 transfer——
      因此 frozen 的 cross-model retention 仅 62%，远低于 15D 的 85%。
      (3) Embedding 空间中的 depth signal 不是线性可分的，2-layer MLP 的容量有限。
      Hand-crafted 15D 的优势: 每个特征都直接编码与递归退化相关的统计量（diversity/surprisal/tail weight），
      人类先验弥补了维度不足。AUC gap 1.30pp < 3pp (best 档要求 < 3pp)。
      更关键的是 interpretability 优势: 15D 支持 degradation ordering 分析（exp-005/C2）和 feature group ablation，
      这是 frozen embeddings 无法提供的。论文叙事需要 interpretable features 来讲述 "which linguistic properties degrade first" 的故事。
    tables:
      - caption: "Learned vs hand-crafted features 对比"
        columns: [method, AUC_1v2, mean_pw_AUC, ordinal_acc, MAE, dim, GPU_hours]
        rows:
          - [frozen embeddings + MLP, 0.5982, 0.5865, 0.3708, 1.195, 1536, 2.6]
          - [hand-crafted 15D, 0.6112, 0.6048, 0.3875, 1.155, 15, 0.08]
      - caption: "Cross-model transfer 对比 (train Qwen → test Pythia)"
        columns: [method, in_domain_acc, cross_model_acc, retention_pct]
        rows:
          - [frozen embeddings, 0.3708, 0.2299, "62%"]
          - [hand-crafted 15D, 0.3875, 0.3294, "85%"]
    figures_description:
      - "Performance vs interpretability 双轴图: 15D 在 Pareto 前沿（低维高性能），frozen 在高维略低性能区。"
      - "Cross-model transfer retention bar chart: frozen 62% vs 15D 85%，视觉化 interpretable features 的 generalization 优势。"
    analysis: >
      AUC gap 1.30pp < 3pp 满足 best 档假设。15D hand-crafted 在所有指标上优于或持平 frozen embeddings，
      且维度低 102 倍、训练快 32.5 倍。
      Cross-model transfer 的巨大差距（85% vs 62%）是 decisive argument:
      frozen embeddings 过拟合 model-specific embedding space，而 15D 统计特征是 model-agnostic 的。
      这验证了论文 "选择 interpretable features 不是方法论妥协而是设计优势" 的叙事，
      同时回应审稿人 "为什么不用 learned representations" 的问题。

  - name: "Base vs Instruct 模型对比"
    plan_id: "exp-016"
    description: >
      Qwen2.5-1.5B base model (非 instruct 微调版) continuation mode, C4 5K docs, depth 0-5。
      与 exp-017 (Qwen2.5-1.5B-Instruct continuation) 对比，分离 RLHF/instruction-tuning 对 K* 的影响。
    expected_results:
      base:
        k_star: 2
        pairwise_auc:
          0v1: 0.9958
          1v2: 0.6382
          2v3: 0.5685
          3v4: 0.5358
          4v5: 0.5148
        pairwise_jsd:
          0v1: 0.2952
          1v2: 0.0068
          2v3: 0.0042
          3v4: 0.0032
          4v5: 0.0028
        ordinal_accuracy: 0.3948
        top3_features:
          - surp_d1_std
          - surp_std
          - freq_entropy
      instruct_actual:
        k_star: 2
        pairwise_auc:
          0v1: 0.9972
          1v2: 0.6114
          2v3: 0.5609
          3v4: 0.5408
          4v5: 0.5139
      base_vs_instruct_diff:
        delta_auc_1v2: "+0.0268"
        delta_auc_2v3: "+0.0076"
        delta_jsd_0v1: "+0.0089"
      feature_shift:
        surprisal_mean_base_vs_instruct: "-0.14 std units"
        vocab_diversity_base_vs_instruct: "+0.06 std units"
    result_rationale: >
      RLHF/instruction-tuning 将模型输出拉向 "人类偏好的模式"——更规范的句式、更安全的措辞、更集中的 vocabulary 选择。
      这种 alignment 相当于对输出分布施加了额外的低熵约束，使得即使 gen-0→gen-1 的转换也已经部分"标准化"了。
      结果: instruct 模型的递归代际间差异更小，因为每代输出都被拉向同一个 "preferred mode"。
      Base model 没有这个约束，输出更接近预训练数据的原始分布→递归代际间保留更多分布结构→1v2 AUC 高 2.7pp。
      但 K* 仍为 2: alignment 的影响是 quantitative（减弱信号 2.7pp）而非 qualitative（改变收敛行为）。
      DPI 的信息论约束在有无 RLHF 的情况下都成立——只要模型是有限容量的 lossy channel。
      Surprisal mean 偏移为负（instruct 更"可预测"，反映 RLHF 倾向于生成预期输出）;
      vocabulary diversity 偏移为正（instruct 词汇稍更多样，反映 RLHF 鼓励的表达丰富性）。
      两种偏移方向一致且量级小（< 0.15 std），为 discussion 段落提供数据。
    tables:
      - caption: "Base vs Instruct 对比 (Qwen2.5-1.5B, continuation mode)"
        columns: [variant, K*, AUC_0v1, AUC_1v2, AUC_2v3, JSD_0v1, ordinal_acc]
        rows:
          - [base, 2, 0.9958, 0.6382, 0.5685, 0.2952, 0.3948]
          - [instruct (exp-017), 2, 0.9972, 0.6114, 0.5609, 0.2863, 0.3819]
          - [Δ (base − instruct), 0, "-0.0014", "+0.0268", "+0.0076", "+0.0089", "+0.0129"]
    figures_description:
      - "Base vs instruct JSD decay 对比: base 曲线在 depth 1-2 段系统性高于 instruct，差距在 depth≥3 后消失。"
      - "Feature distribution violin plots: base vs instruct 在 depth=1 的 surprisal mean 和 vocab diversity 分布差异。"
    analysis: >
      Base 信号更强但 K* 不变——RLHF alignment 压缩了代际差异但未改变信息论收敛行为。
      这对实际应用有关键意义: 野外合成文本可能来自 base 或 instruct 模型，
      K*=2 在两种设置下一致意味着 graduated filtering 框架对两者都适用。
      Base model 1v2 AUC=0.638 的 CI 预期 lower bound ~0.628（远高于 0.60），
      为 Qwen-cont instruct 的 0.0015 margin 脆弱性提供了安全网:
      即使 instruct 模型在重复实验中偶尔 CI lower 落到 0.599，base model 的稳健 K*=2 仍支撑 claim。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07db6b83-5852-49ca-b8f6-e86be05944e5",
  "isSidechain": false,
  "requestId": "req_011CazEAZ4KTksGQGPt5mzYu",
  "type": "assistant",
  "uuid": "6b541fbb-69f9-4c96-b851-72b832339f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUrVDN9ekH2GVRLhC3bUfw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26580,
      "cache_read_input_tokens": 32873,
      "output_tokens": 32879,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26580,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32879,
          "cache_read_input_tokens": 32873,
          "cache_creation_input_tokens": 26580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26580
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1' 全面成立 + C3 downstream 收益显著 — 原始 2+1 claim 结构可直接支撑 EMNLP main 核心假设：['exp-003 解码消融: K*=2 在 ≥3/4 解码配置下成立，至少一个配置 K*=3（证明 K* 可被解码策略调控）', 'exp-004 7B: 1v2 AUC…",
  "leafUuid": "6b541fbb-69f9-4c96-b851-72b832339f26",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "K*=2: Generational discrimination boundary for recursive synthetic text",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1' 全面成立 + C3 downstream 收益显著 — 原始 2+1 claim 结构可直接支撑 EMNLP main 核心假设：['exp-003 解码消融: K*=2 在 ≥3/4 解码配置下成立，至少一个配置 K*=3（证明 K* 可被解码策略调控）', 'exp-004 7B: 1v2 AUC…",
  "leafUuid": "6b541fbb-69f9-4c96-b851-72b832339f26",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "K*=2: Generational discrimination boundary for recursive synthetic text",
  "sessionId": "17a0a56a-c5cc-4d9c-b9dc-64f84dc25266"
}
```

---
