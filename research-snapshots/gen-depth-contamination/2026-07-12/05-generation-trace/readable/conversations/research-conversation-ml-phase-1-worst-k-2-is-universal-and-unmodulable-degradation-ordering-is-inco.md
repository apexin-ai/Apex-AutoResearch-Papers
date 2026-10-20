# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：K*=2 is universal and unmodulable, degradation ordering is inconsistent, gr

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/b07282be-9ccf-4dae-909a-2be30d69df05.jsonl`
- **Structured JSON:** [`0e8ef087cf5c4c0a5c72.json`](../../sessions/0e/0e8ef087cf5c4c0a5c72.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T20:16:12.899Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T20:16:12.899Z",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：K*=2 is universal and unmodulable, degradation ordering is inconsistent, graduated filtering does not significantly outperform binary\n核心假设：['K*=2 across all models, scales (including 7B), and decoding strategies without exception', 'Degradation ordering varies across models — no consistent pattern (tau < 0.5)', 'Graduated filtering improvement over binary is <0.5pp and not statistically significant across seeds', 'Ordinal classifier barely outperforms binary + random depth assignment', 'Cross-model transfer for depth is near chance beyond binary distinction', 'Retrain-chain shows different K* or different feature dynamics, weakening prompt-chain validity']\n关键指标范围：{'k_star_range_across_conditions': [2, 2], 'pairwise_auc_1v2_cross_model': [0.55, 0.65], 'pairwise_auc_2v3_any_condition': [0.52, 0.58], 'ordinal_accuracy_best_config': [0.3, 0.4], 'ordinal_mae_best_config': [1.05, 1.3], 'downstream_delta_graduated_vs_binary_mmlu_pp': [-0.3, 0.5], 'downstream_delta_graduated_vs_binary_hellaswag_pp': [-0.3, 0.5], 'cross_model_transfer_retention_pct': [30, 50], 'degradation_ordering_kendall_tau': [0.2, 0.5]}\n叙事方向：需要重构 story：从 method paper 转型为 empirical analysis / negative-result paper。 新 framing：\"递归合成文本的代际信号在 depth 2 后迅速坍缩到不可区分——这是 DPI 的直接后果， 且当前 1-7B 规模模型无法通过解码策略调控。这一负面结果本身具有重要实践意义： 它表明 depth-aware curation 的窗口极窄（仅 human vs gen-1 vs gen-2+），数据治理应聚焦于 first-generation detection 而非精细 depth estimation。\" C1 变为纯 characterization（\"K*=2 is a hard, universal ceiling\"），C2 被 drop 或降级到 appendix， C3 从\"graduated filtering works\"变为\"graduated filtering has fundamental limits explained by rapid signal collapse\"。 论文价值来自 rigorous negative characterization + DPI 理论预测的实验验证 + 对社区的 cautionary message。 投稿策略：EMNLP Findings 或 AAAI 2027；也可考虑 workshop paper (SyntheticData@NeurIPS)。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-contamination\nvenue: EMNLP 2026\nfocus: Route B framing: K* as first-measured saturation boundary, DPI theory validation, graduated filtering with coarse 3-class signal. Key risk: K*=2 may be seen as too shallow for practical impact.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Core Claims (3 条)\n\n1. **C1 (Saturation Boundary)**: 递归合成文本的代际辨别能力存在可测量的饱和边界 K*，这是一个信息论基本量（DPI 的必然推论），而非分类器能力上限。首次在受控实验中系统测量 K* 并表征其随模型、解码策略的变化。\n2. **C2 (Linguistic Degradation Ordering)**: 递归生成导致语言特征按特定顺序逐层坍缩——vocabulary diversity 先于 surprisal dynamics 饱和，揭示递归生成的结构性规律。\n3. **C3 (Graduated Filtering)**: 即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+三级）下，depth-graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al.) 描述宏观现象但不提供检测工具；verification-based methods (Feng et al., Yi et al.) 用外部验证器做 binary quality gate 但不估计递归深度。**无任何方法估计文本经历了多少轮递归生成。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（Data Processing Inequality）推导出辨别饱和边界 K* 的必然存在。K* 本身是首次测量的基本量——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过系统测量 K* 随模型架构和解码策略的变化，揭示控制 K* 的因素，为实际数据治理提供 actionable guidance。\n- **Headline result template**: \"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with JSD decaying monotonically (0.27→0.004) across 5 generations, and demonstrate that even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*=2 太浅，graduated filtering 收益有限\"** → K* 是模型/解码策略依赖的；展示不同解码策略（高温度/low top-p）如何调控 K*；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated\n2. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation（首次将 depth estimation 作为 prediction task）+ empirical characterization（首次测量 K*）+ 理论框架（DPI impossibility boundary），不是分类器本身\n3. **\"Prompt-chain 不代表真实世界递归污染\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法；wild data 的 Common Crawl 验证作为 appendix\n4. **\"单模型/单数据集，泛化性不够\"** → 扩展到 3 个模型族（Pythia/OLMo/Qwen）+ cross-scale probe（7B）+ 2 个种子数据集\n5. **\"同模型做生成和 surprisal 计算有 bias\"** → 显式讨论此 design choice：这衡量的是\"模型对自身递归输出的 self-recognition\"，与 binary detection 的 premise 一致；cross-model transfer 实验验证特征不是模型特异的\n6. **\"为什么不用 learned representations\"** → 作为 baseline 对比（frozen LM embeddings + MLP），但 hand-crafted features 更 interpretable 且支持 degradation ordering 分析\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 本文同时是 method（depth estimation algorithm）和 empirical study（K* characterization），符合 EMNLP 对 \"Resources and Evaluation\" track 的要求\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization 的 novelty\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-003\n  claim: 1,3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth\n    0-3. 测试 K* 是否随模型规模变化。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: null\n  status: planned\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary / graduated / surprisal-based 四种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。3 seeds。'\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-007\n  claim: 1,2\n  description: 'K* sensitivity analysis: 在 0.55/0.60/0.65/0.70 四个阈值下计算 K*，展示 K* 对阈值选择的稳健性。'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: null\n  status: planned\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: null\n  status: planned\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: null\n  status: planned\n- id: exp-010\n  claim: 1,2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: null\n  status: planned\n- id: exp-013\n  claim: 1,2\n  description: 'Cross-model transfer: 在 model A 训练的 depth classifier 在 model B 的 depth\n    chain 上的 transfer accuracy。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: null\n  status: planned\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features，验证 interpretable features 的价值。'\n  priority: P2\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: null\n  status: planned\n- id: mvp-001\n  claim: 1,2,3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_sat_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-12T20:16:12.902Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T20:16:12.902Z",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-12T20:16:12.921Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：K*=2 is universal and unmodulable, degradation ordering is inconsistent, graduated filtering does not significantly outperform binary
核心假设：['K*=2 across all models, scales (including 7B), and decoding strategies without exception', 'Degradation ordering varies across models — no consistent pattern (tau < 0.5)', 'Graduated filtering improvement over binary is <0.5pp and not statistically significant across seeds', 'Ordinal classifier barely outperforms binary + random depth assignment', 'Cross-model transfer for depth is near chance beyond binary distinction', 'Retrain-chain shows different K* or different feature dynamics, weakening prompt-chain validity']
关键指标范围：{'k_star_range_across_conditions': [2, 2], 'pairwise_auc_1v2_cross_model': [0.55, 0.65], 'pairwise_auc_2v3_any_condition': [0.52, 0.58], 'ordinal_accuracy_best_config': [0.3, 0.4], 'ordinal_mae_best_config': [1.05, 1.3], 'downstream_delta_graduated_vs_binary_mmlu_pp': [-0.3, 0.5], 'downstream_delta_graduated_vs_binary_hellaswag_pp': [-0.3, 0.5], 'cross_model_transfer_retention_pct': [30, 50], 'degradation_ordering_kendall_tau': [0.2, 0.5]}
叙事方向：需要重构 story：从 method paper 转型为 empirical analysis / negative-result paper。 新 framing："递归合成文本的代际信号在 depth 2 后迅速坍缩到不可区分——这是 DPI 的直接后果， 且当前 1-7B 规模模型无法通过解码策略调控。这一负面结果本身具有重要实践意义： 它表明 depth-aware curation 的窗口极窄（仅 human vs gen-1 vs gen-2+），数据治理应聚焦于 first-generation detection 而非精细 depth estimation。" C1 变为纯 characterization（"K*=2 is a hard, universal ceiling"），C2 被 drop 或降级到 appendix， C3 从"graduated filtering works"变为"graduated filtering has fundamental limits explained by rapid signal collapse"。 论文价值来自 rigorous negative characterization + DPI 理论预测的实验验证 + 对社区的 cautionary message。 投稿策略：EMNLP Findings 或 AAAI 2027；也可考虑 workshop paper (SyntheticData@NeurIPS)。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-contamination
venue: EMNLP 2026
focus: Route B framing: K* as first-measured saturation boundary, DPI theory validation, graduated filtering with coarse 3-class signal. Key risk: K*=2 may be seen as too shallow for practical impact.

## paper_framing.md

# Paper Framing — gen-depth-contamination

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)
- Fallback: EMNLP 2026 Findings
- Backup: AAAI 2027 (abstract July 25, paper August 1)

## Core Claims (3 条)

1. **C1 (Saturation Boundary)**: 递归合成文本的代际辨别能力存在可测量的饱和边界 K*，这是一个信息论基本量（DPI 的必然推论），而非分类器能力上限。首次在受控实验中系统测量 K* 并表征其随模型、解码策略的变化。
2. **C2 (Linguistic Degradation Ordering)**: 递归生成导致语言特征按特定顺序逐层坍缩——vocabulary diversity 先于 surprisal dynamics 饱和，揭示递归生成的结构性规律。
3. **C3 (Graduated Filtering)**: 即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+三级）下，depth-graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。

## Story Spine

- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。
- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al.) 描述宏观现象但不提供检测工具；verification-based methods (Feng et al., Yi et al.) 用外部验证器做 binary quality gate 但不估计递归深度。**无任何方法估计文本经历了多少轮递归生成。**
- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（Data Processing Inequality）推导出辨别饱和边界 K* 的必然存在。K* 本身是首次测量的基本量——它告诉数据策展者"在什么深度以下，depth-aware curation 比 binary detection 更有价值"。通过系统测量 K* 随模型架构和解码策略的变化，揭示控制 K* 的因素，为实际数据治理提供 actionable guidance。
- **Headline result template**: "We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with JSD decaying monotonically (0.27→0.004) across 5 generations, and demonstrate that even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag."

## Anticipated Reviewer Concerns & Responses

1. **"K*=2 太浅，graduated filtering 收益有限"** → K* 是模型/解码策略依赖的；展示不同解码策略（高温度/low top-p）如何调控 K*；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated
2. **"只是 feature engineering + off-the-shelf classifier，方法贡献弱"** → 贡献在 problem formulation（首次将 depth estimation 作为 prediction task）+ empirical characterization（首次测量 K*）+ 理论框架（DPI impossibility boundary），不是分类器本身
3. **"Prompt-chain 不代表真实世界递归污染"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法；wild data 的 Common Crawl 验证作为 appendix
4. **"单模型/单数据集，泛化性不够"** → 扩展到 3 个模型族（Pythia/OLMo/Qwen）+ cross-scale probe（7B）+ 2 个种子数据集
5. **"同模型做生成和 surprisal 计算有 bias"** → 显式讨论此 design choice：这衡量的是"模型对自身递归输出的 self-recognition"，与 binary detection 的 premise 一致；cross-model transfer 实验验证特征不是模型特异的
6. **"为什么不用 learned representations"** → 作为 baseline 对比（frozen LM embeddings + MLP），但 hand-crafted features 更 interpretable 且支持 degradation ordering 分析

## Venue Fit

- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作
- 本文同时是 method（depth estimation algorithm）和 empirical study（K* characterization），符合 EMNLP 对 "Resources and Evaluation" track 的要求
- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization 的 novelty


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,
    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: null
  status: planned
- id: exp-002
  claim: 1
  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,
    C4 5K docs, depth 0-5.'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: null
  status: planned
- id: exp-003
  claim: 1,3
  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9
    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'
  priority: P0
  gpu_budget_hours: 20
  deps: []
  registry_id: null
  status: planned
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
  registry_id: null
  status: planned
- id: exp-006
  claim: 3
  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter
    / binary / graduated / surprisal-based 四种策略，用 continued pretraining + lm-eval-harness
    (MMLU, HellaSwag) 评估。3 seeds。'
  priority: P0
  gpu_budget_hours: 48
  deps: []
  registry_id: null
  status: planned
- id: exp-007
  claim: 1,2
  description: 'K* sensitivity analysis: 在 0.55/0.60/0.65/0.70 四个阈值下计算 K*，展示 K* 对阈值选择的稳健性。'
  priority: P0
  gpu_budget_hours: 1
  deps:
  - exp-001
  - exp-002
  - exp-003
  registry_id: null
  status: planned
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
  claim: 1,2
  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs
    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-005
  registry_id: null
  status: planned
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
  claim: 1,2
  description: 'Cross-model transfer: 在 model A 训练的 depth classifier 在 model B 的 depth
    chain 上的 transfer accuracy。'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-001
  - exp-002
  registry_id: null
  status: planned
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
    MLP vs hand-crafted 15D features，验证 interpretable features 的价值。'
  priority: P2
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
- id: mvp-001
  claim: 1,2,3
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
  "promptId": "e2a847a8-1c51-4fcd-ae65-92aea86f9d93",
  "type": "user",
  "uuid": "b52b44b7-19da-40d0-bfd7-4dd16bc395e5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T20:16:12.920Z_

```json
{
  "parentUuid": "b52b44b7-19da-40d0-bfd7-4dd16bc395e5",
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
  "uuid": "72bed04a-a2fe-4e31-96b7-3e0ee2037a47",
  "timestamp": "2026-05-12T20:16:12.920Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T20:16:12.920Z_

```json
{
  "parentUuid": "72bed04a-a2fe-4e31-96b7-3e0ee2037a47",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "95f985a4-ee3a-4c4a-8d95-b48a77d68f57",
  "timestamp": "2026-05-12T20:16:12.920Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Worst-case scenario depth estimation empirical characterization",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05"
}
```

---

### Assistant

_source line 7 · 2026-05-12T20:16:33.212Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "worst" tier scenario for every planned experiment in their experiment plan. Let me carefully go through each experiment and predict what the results would look like under the worst-case scenario they've defined.

Let me review the worst tier definition:
- K*=2 is universal and unmodulable across all models, scales, and decoding strategies
- Degradation ordering varies across models — no consistent pattern (tau < 0.5)
- Graduated filtering improvement over binary is <0.5pp and not statistically significant
- Ordinal classifier barely outperforms binary + random depth assignment


- Cross-model transfer for depth shows near-chance performance except for the basic binary distinction, and retraining on different chains reveals either different K* values or fundamentally different feature dynamics

Now I'm looking at the specific metric ranges I'd expect to see across these worst-case conditions: K* stays locked at 2 everywhere, cross-model pairwise AUCs hover in that weak 0.55-0.65 range for the first comparison and drop further to 0.52-0.58 for deeper distinctions, ordinal accuracy barely reaches 0.3-0.4 at best, and mean absolute error sits around 1.05-1.3 even in the best configurations.

The downstream performance deltas when comparing graduated versus binary setups show mixed results across MMLU and HellaSwag, cross-model transfer retention drops to just 30-50 percent, and the degradation patterns have weak correlation with Kendall tau around 0.2-0.5.

Looking at the experiments themselves: the Pythia and OLMo depth chains both converge on K*=2 similar to the baseline, the decoding strategy ablation on Qwen shows K*=2 is consistent regardless of strategy choice, and I'm starting to examine the cross-scale results.

Continuing through the remaining experiments, I'm seeing that K*=2 holds even at 7B scale, the feature group ablation reveals inconsistent degradation ordering across different models, graduated filtering performs nearly identically to binary filtering, and K* sensitivity analysis confirms robustness across different threshold values. The retrain-chain approach shows different dynamics that undermine the prompt-chain findings, dose-response curves show no meaningful distinction between graduated and binary, and ordinal modeling barely outperforms multinomial or regression approaches. Zero-shot LLM performance is poor, using detector confidence as a depth proxy yields low correlation, cross-model transfer drops to near chance levels beyond binary classification, naturalistic validation shows weak correlations, and the learned representation baseline performs comparably or slightly better than the main approach.

Now I'm adding the final two experiments—base versus instruct model variants both converging on K*=2—and I need to generate detailed predictions with specific metric values for each experiment, using the mvp-001 real data as a calibration reference before producing the full YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95f985a4-ee3a-4c4a-8d95-b48a77d68f57",
  "isSidechain": false,
  "requestId": "req_011CayHmGNYLK7e8NUQTKSX6",
  "type": "assistant",
  "uuid": "d77efc0e-911b-4c27-801d-5d4e9d631e7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyvE8Nym3vAh8531TvYbBN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10229,
      "cache_read_input_tokens": 11841,
      "output_tokens": 21880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21880,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10229
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

_source line 8 · 2026-05-12T20:22:41.456Z_

```yaml
tier: worst
narrative_guidance: >
  需要重构 story：从 method paper 转型为 empirical analysis / negative-result paper。
  新 framing："递归合成文本的代际信号在 depth 2 后迅速坍缩到不可区分——这是 DPI 的直接后果，
  且当前 1-7B 规模模型无法通过解码策略调控。这一负面结果本身具有重要实践意义：
  它表明 depth-aware curation 的窗口极窄（仅 human vs gen-1 vs gen-2+），数据治理应聚焦于
  first-generation detection 而非精细 depth estimation。"
  C1 变为纯 characterization（"K*=2 is a hard, universal ceiling"），C2 被 drop 或降级到 appendix，
  C3 从"graduated filtering works"变为"graduated filtering has fundamental limits explained by rapid signal collapse"。
  论文价值来自 rigorous negative characterization + DPI 理论预测的实验验证 + 对社区的 cautionary message。
  投稿策略：EMNLP Findings 或 AAAI 2027；也可考虑 workshop paper (SyntheticData@NeurIPS)。

imagined_experiments:
  # ============================================================
  # exp-001: Pythia-1.4B depth chain
  # ============================================================
  - name: "Pythia-1.4B cross-model depth chain"
    plan_id: "exp-001"
    description: >
      Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5.
      验证 K* 是否跨模型一致。
    expected_results:
      k_star: 2
      pairwise_auc_0v1: 0.991
      pairwise_auc_1v2: 0.63
      pairwise_auc_2v3: 0.55
      pairwise_auc_3v4: 0.52
      pairwise_auc_4v5: 0.51
      pairwise_auc_0v1_std: 0.001
      pairwise_auc_1v2_std: 0.009
      pairwise_auc_2v3_std: 0.015
      pairwise_auc_3v4_std: 0.008
      pairwise_auc_4v5_std: 0.010
      pairwise_jsd_0v1: 0.231
      pairwise_jsd_1v2: 0.012
      pairwise_jsd_2v3: 0.004
      pairwise_jsd_3v4: 0.002
      pairwise_jsd_4v5: 0.002
      ordinal_accuracy: 0.35
      ordinal_mae: 1.18
    result_rationale: >
      Pythia-1.4B 是较早一代架构（GPT-NeoX based），训练数据量和质量低于 Qwen2.5-1.5B。
      在 worst 档下，Pythia 的 pairwise AUC 1v2 低于 MVP（0.63 vs 0.70），因为 Pythia 的
      generation 质量本身更低——第一代输出已经引入更大噪声，使得后续代际之间的差异更快被噪声淹没。
      JSD 从 0v1 的 0.231 迅速衰减到 1v2 的 0.012，与 DPI 预测的指数衰减一致。
      depth 2+ 区域 AUC 在 0.51-0.55 之间，接近 chance level。
      ordinal_accuracy 仅 0.35，因 depth 2-5 几乎不可区分，classifier 在这些类上接近随机猜测。
      这强化了 K*=2 的 universality claim——即使换了不同架构家族，ceiling 不变。
    tables:
      - name: "Table: Pythia-1.4B pairwise discrimination"
        columns: ["depth_pair", "AUC_mean", "AUC_std", "JSD"]
        rows:
          - ["0 vs 1", 0.991, 0.001, 0.231]
          - ["1 vs 2", 0.63, 0.009, 0.012]
          - ["2 vs 3", 0.55, 0.015, 0.004]
          - ["3 vs 4", 0.52, 0.008, 0.002]
          - ["4 vs 5", 0.51, 0.010, 0.002]
    figures_description:
      - "JSD decay curve (depth 0-5): 与 MVP Qwen 曲线形状高度相似，depth 1 后急剧下降并在 depth 2+ 趋于平坦。Pythia 的 0v1 JSD 略低于 Qwen（0.231 vs 0.267），符合较弱模型产生更均匀退化的预期。"
    analysis: >
      Pythia-1.4B 复现了 MVP 的核心发现：K*=2，且 depth 2+ 区域信号坍缩。
      0v1 JSD 较 Qwen 低约 13%，可能因为 Pythia 的 base generation quality 更低，
      human-gen1 boundary 本身就不如 Qwen 清晰。但 K* 不变——这对 worst 叙事是关键证据：
      K*=2 不是 Qwen-specific artifact，而是当前规模模型的 fundamental limitation。
      ordinal MAE 1.18 表明平均预测偏差超过 1 个 depth level，graduated estimation 实用性极低。

  # ============================================================
  # exp-002: OLMo-1B depth chain
  # ============================================================
  - name: "OLMo-1B cross-model depth chain"
    plan_id: "exp-002"
    description: >
      OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5.
    expected_results:
      k_star: 2
      pairwise_auc_0v1: 0.988
      pairwise_auc_1v2: 0.61
      pairwise_auc_2v3: 0.54
      pairwise_auc_3v4: 0.52
      pairwise_auc_4v5: 0.51
      pairwise_auc_0v1_std: 0.001
      pairwise_auc_1v2_std: 0.011
      pairwise_auc_2v3_std: 0.014
      pairwise_auc_3v4_std: 0.009
      pairwise_auc_4v5_std: 0.012
      pairwise_jsd_0v1: 0.218
      pairwise_jsd_1v2: 0.010
      pairwise_jsd_2v3: 0.004
      pairwise_jsd_3v4: 0.002
      pairwise_jsd_4v5: 0.001
      ordinal_accuracy: 0.33
      ordinal_mae: 1.22
    result_rationale: >
      OLMo-1B 参数量最小（1B vs Pythia 1.4B vs Qwen 1.5B），且训练数据虽然开源透明但
      总 token 量较少。在 worst 档下，OLMo 的信号衰减最快：1v2 AUC 仅 0.61，是三个模型中
      最低的。这与 DPI 一致——更小/更弱的模型作为 lossy channel，每次 pass 丢失更多互信息，
      使得代际差异更快趋同。0v1 仍然高（0.988），因为 human vs machine 的 distributional gap
      足够大，即使弱模型也能被检测。但 gen-1 vs gen-2 的 gap 已经极小（JSD 0.010），
      gen-2+ 完全不可区分。ordinal_accuracy 0.33 接近 6-class random baseline（0.167），
      说明 classifier 只在 depth 0 和 depth 1 上有意义区分能力。
    tables:
      - name: "Table: OLMo-1B pairwise discrimination"
        columns: ["depth_pair", "AUC_mean", "AUC_std", "JSD"]
        rows:
          - ["0 vs 1", 0.988, 0.001, 0.218]
          - ["1 vs 2", 0.61, 0.011, 0.010]
          - ["2 vs 3", 0.54, 0.014, 0.004]
          - ["3 vs 4", 0.52, 0.009, 0.002]
          - ["4 vs 5", 0.51, 0.012, 0.001]
    figures_description:
      - "Cross-model JSD comparison figure: 三条 JSD decay curves（Qwen/Pythia/OLMo）叠加在同一图上。三条曲线在 depth 1 后 converge 到同一狭窄带（JSD < 0.02），仅在 0v1 处有明显分离（Qwen > Pythia > OLMo）。视觉上强烈传达 'depth 2+ 是 universal dead zone' 的信息。"
    analysis: >
      OLMo-1B 进一步确认 K*=2 的 universality。三个模型的 K* 完全一致，
      差异仅在 0v1 和 1v2 的绝对值上——这些差异反映了模型 generation quality 的差异，
      但不影响 saturation boundary 的位置。这是 worst 档最有力的论据：
      K* 是 architecture-invariant 的 hard ceiling。

  # ============================================================
  # exp-003: Decoding strategy ablation
  # ============================================================
  - name: "Qwen2.5-1.5B decoding strategy ablation"
    plan_id: "exp-003"
    description: >
      Qwen2.5-1.5B: greedy / nucleus p=0.9 / T=0.7 / T=1.2, C4 5K docs, depth 0-5.
      测试解码策略对 K* 的调控效应。
    expected_results:
      greedy:
        k_star: 2
        pairwise_auc_0v1: 0.997
        pairwise_auc_1v2: 0.62
        pairwise_auc_2v3: 0.55
        pairwise_auc_3v4: 0.53
        pairwise_auc_4v5: 0.52
        pairwise_jsd_0v1: 0.305
        pairwise_jsd_1v2: 0.014
        pairwise_jsd_2v3: 0.005
        pairwise_jsd_3v4: 0.003
        pairwise_jsd_4v5: 0.002
      nucleus_p09:
        k_star: 2
        pairwise_auc_0v1: 0.996
        pairwise_auc_1v2: 0.68
        pairwise_auc_2v3: 0.57
        pairwise_auc_3v4: 0.54
        pairwise_auc_4v5: 0.53
        pairwise_jsd_0v1: 0.280
        pairwise_jsd_1v2: 0.015
        pairwise_jsd_2v3: 0.006
        pairwise_jsd_3v4: 0.004
        pairwise_jsd_4v5: 0.003
      temp_07:
        k_star: 2
        pairwise_auc_0v1: 0.997
        pairwise_auc_1v2: 0.65
        pairwise_auc_2v3: 0.56
        pairwise_auc_3v4: 0.53
        pairwise_auc_4v5: 0.52
        pairwise_jsd_0v1: 0.295
        pairwise_jsd_1v2: 0.014
        pairwise_jsd_2v3: 0.005
        pairwise_jsd_3v4: 0.003
        pairwise_jsd_4v5: 0.002
      temp_12:
        k_star: 2
        pairwise_auc_0v1: 0.993
        pairwise_auc_1v2: 0.64
        pairwise_auc_2v3: 0.54
        pairwise_auc_3v4: 0.52
        pairwise_auc_4v5: 0.51
        pairwise_jsd_0v1: 0.240
        pairwise_jsd_1v2: 0.011
        pairwise_jsd_2v3: 0.004
        pairwise_jsd_3v4: 0.002
        pairwise_jsd_4v5: 0.001
    result_rationale: >
      在 worst 档下，解码策略对 K* 没有任何调控效应——所有四种策略均产生 K*=2。
      这是因为 DPI bound 取决于 channel 的信息损失率，而不同解码策略改变的是 generation 的
      方差/多样性，但不改变 iterated lossy channel 的 fundamental bottleneck。

      Greedy decoding 产生最高的 0v1 JSD（0.305），因为确定性输出与 human text 的
      distributional gap 最大——greedy 输出高度 peaked、缺少 human text 的 variability。
      但这并不帮助 depth 2+ 的区分：greedy 的 gen-1 输出已经是 degenerate distribution，
      再次 greedy decode 只是在 narrow mode 上迭代，信号迅速坍缩。

      T=1.2（高温度）使 0v1 gap 缩小（JSD 0.240），因为高温度输出更接近 uniform 分布，
      与 human text 的差异减小。同时高温度加速后续代际的 entropy 增长和 mode mixing，
      使 depth 2+ 的信号衰减更快。

      Nucleus p=0.9（较 MVP 的 p=0.95 更 conservative）的 1v2 AUC 略高（0.68），
      因为 truncation 保留了更集中的 probability mass，但仍不足以突破 K*=2 的 ceiling。

      关键：没有任何解码策略能将 K* 推到 3。这直接否定了 Route B framing 中
      "decoding strategy modulates K*" 的希望，使 K*=2 成为 unmodulable constant。
    tables:
      - name: "Table: Decoding strategy ablation — K* and pairwise AUC"
        columns: ["strategy", "K*", "AUC_0v1", "AUC_1v2", "AUC_2v3", "JSD_0v1", "JSD_1v2"]
        rows:
          - ["greedy", 2, 0.997, 0.62, 0.55, 0.305, 0.014]
          - ["nucleus p=0.9", 2, 0.996, 0.68, 0.57, 0.280, 0.015]
          - ["T=0.7", 2, 0.997, 0.65, 0.56, 0.295, 0.014]
          - ["T=1.2", 2, 0.993, 0.64, 0.54, 0.240, 0.011]
          - ["nucleus p=0.95 (MVP)", 2, 0.996, 0.70, 0.59, 0.267, 0.016]
    figures_description:
      - "Heatmap: K* values across all (model × decoding strategy) conditions. 整个 heatmap 是单色（全为 2），视觉冲击力强，直接传达 'K*=2 is universal and unmodulable'。"
      - "Bar chart: 1v2 AUC across decoding strategies, 所有 bars 在 0.62-0.70 的窄区间内，error bars 重叠。清楚表明策略差异不改变 discriminability 的 qualitative regime。"
    analysis: >
      解码策略消融是 worst 档的决定性实验。四种策略覆盖了从 deterministic（greedy）到
      high-entropy（T=1.2）的全谱系，但 K* 完全不变。
      策略之间的 1v2 AUC 差异（0.62-0.68）虽存在但幅度小且不改变 K*。
      这使 C1 claim 从 "K* is measurable" 退化为 "K*=2 is a hard, unmodulable constant"——
      实用价值有限，因为无法通过工程手段扩展 depth-aware curation 的窗口。
      对论文而言，这是核心 negative result：current-scale 模型的 recursive generation
      inherently collapses to binary regime。

  # ============================================================
  # exp-004: Cross-scale probe (7B)
  # ============================================================
  - name: "Qwen2.5-7B cross-scale probe"
    plan_id: "exp-004"
    description: >
      Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3.
      测试 K* 是否随模型规模变化。
    expected_results:
      k_star: 2
      pairwise_auc_0v1: 0.994
      pairwise_auc_1v2: 0.65
      pairwise_auc_2v3: 0.56
      pairwise_auc_0v1_std: 0.002
      pairwise_auc_1v2_std: 0.012
      pairwise_auc_2v3_std: 0.018
      pairwise_jsd_0v1: 0.258
      pairwise_jsd_1v2: 0.014
      pairwise_jsd_2v3: 0.005
    result_rationale: >
      在 worst 档下，7B 模型也产生 K*=2，这是最令人沮丧的发现。
      直觉上，更大模型作为更"高保真"的 channel 应该保留更多 inter-generational 信息，
      从而可能推高 K*。但在 worst scenario 下，7B 的 1v2 AUC（0.65）仅比 1.5B MVP（0.70）
      略低——这看似反直觉，但可以解释：

      7B 模型的 generation quality 更高，意味着 gen-1 输出更接近 human distribution，
      因此 1v2 boundary 反而更难区分（higher-fidelity channel 使连续代际更相似）。
      0v1 AUC 略低于 1.5B（0.994 vs 0.996）也符合这一逻辑——更好的模型产生更
      human-like 的输出，使 binary detection 本身就更困难。

      depth 0-3 的 truncated range（因 GPU 预算限制只到 depth 3）已经足以确认 K*=2，
      因为 2v3 AUC 已经接近 chance。1K docs 的较小样本量导致 std 略大，
      但中位数点估计仍清晰地在 [0.55, 0.65] 的 worst 范围内。

      这一结果否定了 "scaling to larger models might yield higher K*" 的希望，
      使 K*=2 not only architecture-invariant but also scale-invariant（至少在 1-7B 范围内）。
    tables:
      - name: "Table: Cross-scale comparison (1.5B vs 7B)"
        columns: ["model", "params", "K*", "AUC_0v1", "AUC_1v2", "AUC_2v3", "JSD_0v1"]
        rows:
          - ["Qwen2.5-1.5B (MVP)", "1.5B", 2, 0.996, 0.70, 0.59, 0.267]
          - ["Qwen2.5-7B", "7B", 2, 0.994, 0.65, 0.56, 0.258]
    figures_description:
      - "Scatter plot: model scale (x, log) vs K* (y). 两个点都在 K*=2，加上 Pythia-1.4B 和 OLMo-1B 共四个点，全部落在 y=2 水平线上。配合 DPI theoretical bound 作为虚线。强调 scale invariance。"
    analysis: >
      7B 结果是对 "bigger models solve the problem" narrative 的直接否定。
      在 DPI 框架下可以理解：更好的 channel（7B）确实每步丢失更少信息，
      但 detection threshold 也随之提高（因为连续代际更相似），两个效应相互抵消。
      样本量（1K）是局限，但 std 可控（<0.02），结论稳健。
      对论文 narrative：K*=2 是 1-7B scale 下的 hard ceiling，
      突破可能需要 order-of-magnitude 的 scale jump（如 70B+），超出本文 scope。

  # ============================================================
  # exp-005: Feature group ablation + degradation ordering
  # ============================================================
  - name: "Feature group ablation and degradation ordering"
    plan_id: "exp-005"
    description: >
      对每个模型的 depth chain，按 feature group（surprisal/diversity/tail-thinning）
      分别计算 pairwise AUC 和饱和深度，绘制 degradation ordering heatmap。
    expected_results:
      qwen_1p5b_degradation_order: ["diversity", "tail-thinning", "surprisal"]
      qwen_1p5b_diversity_saturation_depth: 2
      qwen_1p5b_surprisal_saturation_depth: 2
      qwen_1p5b_tail_saturation_depth: 2
      pythia_degradation_order: ["surprisal", "diversity", "tail-thinning"]
      pythia_diversity_saturation_depth: 2
      pythia_surprisal_saturation_depth: 2
      pythia_tail_saturation_depth: 2
      olmo_degradation_order: ["tail-thinning", "surprisal", "diversity"]
      olmo_diversity_saturation_depth: 2
      olmo_surprisal_saturation_depth: 2
      olmo_tail_saturation_depth: 2
      cross_model_kendall_tau_ordering: 0.33
      per_group_1v2_auc_range: [0.55, 0.68]
    result_rationale: >
      在 worst 档下，degradation ordering 在不同模型间不一致（Kendall tau 0.33）。

      Qwen 上 vocabulary diversity 先饱和（符合 MVP 初步观察），因为 nucleus sampling
      本身就限制了 token diversity 的变化空间，diversity metrics 在 gen-1 就被压到低值。
      但 Pythia 上 surprisal 先饱和——因为 Pythia 的 next-token 分布本身更 peaked，
      递归生成迅速固化 surprisal 模式。OLMo 上 tail-thinning 先饱和，可能因为其
      训练数据分布使得 rare token usage 在第一代就显著下降。

      关键问题：所有三个 feature group 在所有模型上都在 depth 2 饱和——
      即使 ordering 不同，saturation depth 完全相同。这意味着虽然不同 features
      的 degradation speed 有微妙差异（体现在 1v2 AUC 的 feature-specific 值），
      但这些差异在 depth 2 的 floor 上完全消失。degradation ordering 因此不具备
      跨模型的 prescriptive value——你无法基于某个 feature group 预测它在另一个模型上的
      discriminative utility。

      tau=0.33 表明三个模型的 ordering 几乎是 random permutation
      （3 个 items 的 random tau 期望值约 0，范围 [-1, 1]，0.33 表示 weak agreement）。
    tables:
      - name: "Table: Feature group pairwise AUC (1v2) by model"
        columns: ["model", "surprisal_AUC_1v2", "diversity_AUC_1v2", "tail_AUC_1v2", "ordering_rank"]
        rows:
          - ["Qwen2.5-1.5B", 0.63, 0.58, 0.61, "div → tail → surp"]
          - ["Pythia-1.4B", 0.56, 0.60, 0.59, "surp → tail → div"]
          - ["OLMo-1B", 0.58, 0.59, 0.55, "tail → surp → div"]
      - name: "Table: Feature group saturation depth by model"
        columns: ["model", "surprisal_sat", "diversity_sat", "tail_sat"]
        rows:
          - ["Qwen2.5-1.5B", 2, 2, 2]
          - ["Pythia-1.4B", 2, 2, 2]
          - ["OLMo-1B", 2, 2, 2]
    figures_description:
      - "Degradation ordering heatmap: 3 models × 3 feature groups，颜色编码 1v2 AUC。每行的 ordering 不同——没有一致的 'diversity 先饱和' 模式。对角线没有结构性pattern。"
      - "Per-feature JSD decay curves: 3×3 panel（model × feature group），每个 panel 展示 depth 0-5 的 JSD 衰减。所有 9 个 panel 在 depth 2+ 都趋于平坦，但 0-2 区间内的 slope 因 model×feature 组合而异且无规律。"
    analysis: >
      C2（Linguistic Degradation Ordering）在 worst 档下基本失败。
      Kendall tau 0.33 远低于 0.5 的 meaningful agreement 阈值。
      虽然每个模型内部可以描述一个 ordering，但缺乏跨模型泛化性，
      使得 C2 不构成独立 contribution——它退化为模型特定的描述性观察。
      建议：C2 整体降级到 appendix，仅作为 supplementary characterization，
      不作为论文 main claim。framing 变为 "degradation ordering is model-specific,
      further underscoring the difficulty of generalizable depth estimation"。

  # ============================================================
  # exp-006: Downstream filtering evaluation
  # ============================================================
  - name: "Downstream filtering evaluation"
    plan_id: "exp-006"
    description: >
      Qwen2.5-1.5B depth chain 上比较 no-filter / binary / graduated / surprisal-based
      四种策略，continued pretraining + lm-eval-harness (MMLU, HellaSwag)。3 seeds。
    expected_results:
      no_filter_mmlu: 25.1
      no_filter_hellaswag: 42.3
      binary_mmlu: 25.8
      binary_hellaswag: 43.2
      graduated_mmlu: 25.9
      graduated_hellaswag: 43.4
      surprisal_mmlu: 25.7
      surprisal_hellaswag: 43.1
      delta_graduated_vs_binary_mmlu_pp: 0.1
      delta_graduated_vs_binary_hellaswag_pp: 0.2
      delta_graduated_vs_binary_mmlu_std: 0.3
      delta_graduated_vs_binary_hellaswag_std: 0.4
      binary_vs_nofilter_mmlu_pp: 0.7
      binary_vs_nofilter_hellaswag_pp: 0.9
      graduated_vs_nofilter_mmlu_pp: 0.8
      graduated_vs_nofilter_hellaswag_pp: 1.1
      p_value_graduated_vs_binary_mmlu: 0.62
      p_value_graduated_vs_binary_hellaswag: 0.48
    result_rationale: >
      在 worst 档下，graduated filtering 相对 binary 的增益微乎其微（MMLU +0.1pp, HellaSwag +0.2pp），
      且在 3 seeds 上不显著（p > 0.4）。

      根本原因：graduated filtering 的优势来自对 depth 1 vs depth 2+ 的更精细处理——
      例如对 gen-1 赋予中等权重而非完全删除。但在 worst 档下：
      (1) K*=2 意味着 graduated signal 只有三个有效等级（human/gen-1/gen-2+），
          与 binary 相比仅多一个 bucket；
      (2) gen-1 的 ordinal prediction 不够 reliable（accuracy ~0.35），
          所以 graduated filter 经常错误地 upweight 或 downweight gen-1 文本；
      (3) continued pretraining 本身对训练数据质量的敏感度在 1.5B scale 下有限——
          模型的 learning capacity 不足以从 marginal quality differences 中获益。

      Binary filtering 本身有意义（vs no-filter: +0.7 MMLU, +0.9 HellaSwag），
      因为移除明显的 synthetic text 确实有用。但 graduated 在 binary 之上的
      marginal gain 消失在 noise 中。surprisal-based filtering 与 binary 接近，
      说明 surprisal features 的连续值在这个 scale 下不提供额外的 quality signal。

      这使 C3 从 "graduated filtering outperforms binary" 变为
      "graduated filtering offers no statistically significant advantage over binary
      when K*=2 limits the ordinal signal to three coarse classes"。
    tables:
      - name: "Table: Downstream filtering comparison"
        columns: ["strategy", "MMLU_mean", "MMLU_std", "HellaSwag_mean", "HellaSwag_std"]
        rows:
          - ["No filter", 25.1, 0.2, 42.3, 0.3]
          - ["Binary", 25.8, 0.3, 43.2, 0.4]
          - ["Graduated", 25.9, 0.3, 43.4, 0.3]
          - ["Surprisal-based", 25.7, 0.2, 43.1, 0.4]
      - name: "Table: Pairwise significance tests (graduated vs binary)"
        columns: ["benchmark", "delta_pp", "p_value", "significant_at_005"]
        rows:
          - ["MMLU", "+0.1", 0.62, "No"]
          - ["HellaSwag", "+0.2", 0.48, "No"]
    figures_description:
      - "Bar chart with error bars: 四种策略在 MMLU 和 HellaSwag 上的表现。Binary/graduated/surprisal 的 bars 几乎等高，error bars 大幅重叠。No-filter 明显更低，清楚表明 binary filtering 有用，但 graduated 无额外收益。"
      - "Seed-level scatter: 3 seeds × 4 strategies，每个点是一个 (strategy, benchmark_score) 对。Graduated 和 binary 的点完全 interleaved，无 separation。"
    analysis: >
      C3 在 worst 档下被否定为独立 positive claim。graduated filtering 的理论优势
      （更 calibrated 的 quality 估计）在实践中被两个因素消解：
      (1) K*=2 限制了 ordinal signal 只有 3 个有效 class；
      (2) ordinal classifier 的不可靠性使得即使这 3 个 class 的 assignment 也 noisy。
      论文 narrative 转变：C3 变为 "graduated filtering has fundamental limits
      explained by rapid signal collapse"，并从 positive claim 变为 characterization
      of why the approach fails。实践建议简化为：use binary detection + discard，
      不需要 depth estimation。

  # ============================================================
  # exp-007: K* sensitivity analysis
  # ============================================================
  - name: "K* sensitivity to AUC threshold"
    plan_id: "exp-007"
    description: >
      在 0.55/0.60/0.65/0.70 四个阈值下计算 K*，展示 K* 对阈值选择的稳健性。
    expected_results:
      threshold_055:
        k_star_qwen: 3
        k_star_pythia: 2
        k_star_olmo: 2
      threshold_060:
        k_star_qwen: 2
        k_star_pythia: 2
        k_star_olmo: 2
      threshold_065:
        k_star_qwen: 2
        k_star_pythia: 2
        k_star_olmo: 2
      threshold_070:
        k_star_qwen: 2
        k_star_pythia: 2
        k_star_olmo: 2
      robustness_summary: "K*=2 at thresholds ≥0.60; Qwen bumps to K*=3 only at 0.55 due to its 2v3 AUC=0.59 being marginally above threshold"
    result_rationale: >
      K* 的定义是 max depth k such that pairwise AUC(k-1, k) > threshold。
      在 worst 档下，MVP 的 2v3 AUC 是 0.5893——恰好在 0.55 和 0.60 之间。

      当 threshold=0.55 时，Qwen 的 2v3 AUC（0.5893）> 0.55，所以 K*=3。
      但 Pythia（2v3 AUC=0.55）和 OLMo（2v3 AUC=0.54）在 0.55 阈值下仍为 K*=2，
      因为它们的 2v3 AUC 刚好在边界上或以下。

      当 threshold≥0.60 时，所有模型统一 K*=2。

      这表面上看是 "K* is robust"，但在 worst 的叙事下，robustness 是因为
      signal 衰减太快——2v3 AUC 总是在 0.54-0.59 的狭窄区间内，
      远低于 practical utility 所需的水平（≥0.70）。K*=2 的 "稳健性" 其实是
      bad news：它不是因为测量精确，而是因为 cliff 太陡——threshold 选择不影响
      K* 恰恰是因为 depth 2+ 的 signal 已经完全坍缩。

      唯一的 exception（Qwen at 0.55）恰好暴露了 K* 定义的 brittleness：
      0.5893 vs 0.55 threshold 是统计噪声量级的差异，但 K* 从 2 跳到 3。
      这可以在论文中讨论为 "threshold sensitivity at the margin"，
      但不改变核心结论。
    tables:
      - name: "Table: K* across AUC thresholds"
        columns: ["threshold", "Qwen_K*", "Pythia_K*", "OLMo_K*"]
        rows:
          - [0.55, 3, 2, 2]
          - [0.60, 2, 2, 2]
          - [0.65, 2, 2, 2]
          - [0.70, 2, 2, 2]
    figures_description:
      - "Step plot: threshold (x-axis) vs K* (y-axis), 三条线（三个模型）。Pythia 和 OLMo 是平坦直线 K*=2。Qwen 在 threshold 0.55-0.60 之间有一个 step down（3→2），其余平坦。视觉上传达 K*=2 的稳健性，同时暴露 boundary case 的 brittleness。"
    analysis: >
      Sensitivity analysis 确认 K*=2 在 reasonable threshold range 内稳健。
      Qwen 在 0.55 处的 K*=3 是唯一例外，但其 2v3 AUC（0.5893）仅比 threshold 高 0.04，
      属于统计噪声。在论文中建议选取 0.60 作为默认 threshold（与 binary detection 的
      常见 convention 一致），并在 sensitivity analysis section 报告此结果。
      核心信息：K*=2 的稳健性不是 precision 的体现，而是 signal collapse 的体现。

  # ============================================================
  # exp-008: Retrain-chain ecological validity
  # ============================================================
  - name: "Retrain-chain ecological validity"
    plan_id: "exp-008"
    description: >
      Pythia-1.4B LoRA (rank=16, alpha=32), C4 5K docs, depth 0-4.
      对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。
    expected_results:
      retrain_k_star: 2
      retrain_pairwise_auc_0v1: 0.972
      retrain_pairwise_auc_1v2: 0.58
      retrain_pairwise_auc_2v3: 0.53
      retrain_pairwise_auc_3v4: 0.51
      retrain_jsd_0v1: 0.185
      retrain_jsd_1v2: 0.008
      retrain_jsd_2v3: 0.003
      retrain_jsd_3v4: 0.001
      prompt_vs_retrain_jsd_correlation: 0.82
      prompt_vs_retrain_feature_distribution_ks_test_p: 0.03
      feature_dynamics_qualitative_match: false
    result_rationale: >
      在 worst 档下，retrain-chain 产生 K*=2（与 prompt-chain 一致），但特征动态不同。

      Retrain-chain 通过 LoRA fine-tuning 模拟真实世界的"模型在自身输出上训练"场景。
      LoRA rank=16 提供足够的 adaptation capacity，使模型逐代"记住"自己的 generation 模式，
      导致 model collapse 效应更快显现。

      K* 仍为 2，因为即使 retrain 加速了 signal collapse，saturation boundary
      不变——retrain-chain 下 gen-1 与 gen-2 的差异同样在 noise floor。
      但绝对值更低：0v1 AUC 从 prompt-chain 的 0.991 降到 0.972，
      因为 retrained model 的 gen-1 输出已经部分 "adapted to" synthetic distribution，
      使 human vs gen-1 gap 缩小。

      关键差异：feature distribution KS test 显著（p=0.03），表明 prompt-chain 和
      retrain-chain 产生的文本虽然在 depth discrimination 上有相似的 K*，
      但在 feature space 中的轨迹不同。Prompt-chain 的代际漂移主要表现为
      diversity 下降；retrain-chain 的漂移还包括 surprisal distribution 的 mode sharpening
      （因为模型被 fine-tuned 到更 confident 地复制自身模式）。

      这在 worst 档下是 problematic：prompt-chain 上训练的 features 和 classifier
      不能直接 transfer 到 retrain-chain 场景，削弱了实验的 ecological validity。
      prompt-chain 仅是 retrain-chain 的 noisy proxy。
    tables:
      - name: "Table: Prompt-chain vs retrain-chain comparison (Pythia-1.4B)"
        columns: ["metric", "prompt-chain", "retrain-chain"]
        rows:
          - ["K*", 2, 2]
          - ["AUC 0v1", 0.991, 0.972]
          - ["AUC 1v2", 0.63, 0.58]
          - ["AUC 2v3", 0.55, 0.53]
          - ["JSD 0v1", 0.231, 0.185]
          - ["JSD 1v2", 0.012, 0.008]
          - ["Feature KS-test p-value", "—", 0.03]
    figures_description:
      - "Dual JSD decay curve: prompt-chain（实线）vs retrain-chain（虚线），同一坐标轴。Retrain curve 整体更低更平，在 depth 1 后几乎贴着 x 轴。两条曲线的 shape 相似但 offset 不同。"
      - "Feature distribution comparison: 2D PCA of 15D features，prompt-chain 和 retrain-chain 的 depth 0-4 texts 用不同颜色标注。两种 chain 的 depth 0 cluster 重合，但 depth 1+ 的 clusters 在不同方向漂移——prompt-chain 向 diversity collapse 方向，retrain-chain 向 surprisal concentration 方向。"
    analysis: >
      Retrain-chain 结果在 worst 档下对论文有双重影响：
      (1) Positive: K*=2 在 retrain-chain 下仍然成立，支持 universality；
      (2) Negative: feature dynamics 不同（KS p=0.03），意味着 prompt-chain 实验的
          features 和 classifier 不能直接 generalize to real-world retrain scenarios。
      这是 reviewers 会攻击的弱点。论文需要 explicitly acknowledge 这一 limitation，
      将 prompt-chain 定位为 "controlled upper bound"（因 retrain 加速衰减），
      而非 faithful simulation。建议将此实验降级为 appendix 的 validity check，
      避免在 main paper 中给出过强的 ecological validity claim。

  # ============================================================
  # exp-009: Contamination dose-response
  # ============================================================
  - name: "Contamination dose-response"
    plan_id: "exp-009"
    description: >
      在 10%/30%/50% synthetic injection 比例下测试 graduated vs binary filtering 的收益差异。
    expected_results:
      dose_10pct:
        binary_mmlu: 25.6
        graduated_mmlu: 25.6
        binary_hellaswag: 43.0
        graduated_hellaswag: 43.0
        delta_graduated_vs_binary_mmlu: 0.0
        delta_graduated_vs_binary_hellaswag: 0.0
      dose_30pct:
        binary_mmlu: 25.5
        graduated_mmlu: 25.6
        binary_hellaswag: 42.8
        graduated_hellaswag: 42.9
        delta_graduated_vs_binary_mmlu: 0.1
        delta_graduated_vs_binary_hellaswag: 0.1
      dose_50pct:
        binary_mmlu: 25.2
        graduated_mmlu: 25.3
        binary_hellaswag: 42.3
        graduated_hellaswag: 42.5
        delta_graduated_vs_binary_mmlu: 0.1
        delta_graduated_vs_binary_hellaswag: 0.2
      max_delta_across_doses_mmlu: 0.1
      max_delta_across_doses_hellaswag: 0.2
      trend_description: "graduated advantage does not scale with contamination dose; remains ≤0.2pp and non-significant at all doses"
    result_rationale: >
      在 worst 档下，graduated filtering 的 marginal advantage 不随 contamination dose 放大。

      直觉上，更高的 synthetic injection 比例应该放大 graduated 的优势——
      如果有更多 depth-1 文本需要被精细处理（保留 vs 删除），graduated 的 nuance 应该更有价值。
      但在 K*=2 + noisy ordinal classifier 的条件下：

      10% injection: 太少的 synthetic 文本使 any filtering strategy 的影响可忽略。
      Binary 和 graduated 表现完全一致（delta=0.0），因为 impact 被 90% clean data 稀释。

      30% injection: binary filter 已经移除了大部分 harmful synthetic text；
      graduated 的 marginal refinement（对 gen-1 给予中等权重）只影响 30% 中的
      gen-1 subset（约 30%×(1/5)=6% 的总数据），且 refinement 本身因 classifier noise 不可靠。

      50% injection: 这是 graduated 最有机会显示优势的场景——大量 synthetic data
      需要精细处理。但即使这里，delta 仅 0.1-0.2pp，完全不显著。
      原因：当 50% 数据是 synthetic 时，binary filter 激进地删除一半数据，
      graduated filter 保留部分 gen-1 但以 noisy weights——保留 noisy gen-1 text
      不比完全删除好多少。

      总结：dose-response 曲线是平坦的（graduated advantage 不随 dose 增长），
      直接否定了 "graduated becomes more useful at higher contamination" 的假设。
    tables:
      - name: "Table: Dose-response for graduated vs binary filtering"
        columns: ["dose", "binary_MMLU", "graduated_MMLU", "delta_MMLU", "binary_HS", "graduated_HS", "delta_HS"]
        rows:
          - ["10%", 25.6, 25.6, 0.0, 43.0, 43.0, 0.0]
          - ["30%", 25.5, 25.6, "+0.1", 42.8, 42.9, "+0.1"]
          - ["50%", 25.2, 25.3, "+0.1", 42.3, 42.5, "+0.2"]
    figures_description:
      - "Line plot: contamination dose (x) vs delta (graduated - binary) in pp (y), 两条线（MMLU/HellaSwag）。两条线几乎平坦，在 0 附近波动，shaded area 表示 ±1 std，完全包含 0。清楚传达 graduated advantage 不随 dose 增长。"
    analysis: >
      Dose-response 实验彻底关闭了 "graduated filtering at higher doses" 的逃生通道。
      即使在 50% contamination（已经是极端场景），graduated 的优势仅 0.1-0.2pp。
      这强化了 exp-006 的结论，并为论文提供更完整的 negative characterization。
      在 worst 叙事中，此实验可以作为 supplementary evidence 支撑
      "graduated filtering is fundamentally limited by K*=2 signal collapse"。

  # ============================================================
  # exp-010: Ordinal vs multinomial vs regression baseline
  # ============================================================
  - name: "Ordinal vs multinomial vs regression baseline comparison"
    plan_id: "exp-010"
    description: >
      CORAL vs standard multiclass vs ordinal regression，
      证明 ordinal structure 的必要性。
    expected_results:
      coral_ordinal:
        accuracy: 0.37
        mae: 1.08
        macro_f1: 0.22
      standard_multiclass:
        accuracy: 0.35
        mae: 1.22
        macro_f1: 0.19
      ordinal_regression:
        accuracy: 0.36
        mae: 1.10
        macro_f1: 0.21
      binary_plus_random_depth:
        accuracy: 0.32
        mae: 1.25
        macro_f1: 0.18
      coral_vs_binary_random_accuracy_delta: 0.05
      coral_vs_binary_random_mae_delta: -0.17
    result_rationale: >
      在 worst 档下，ordinal classifier（CORAL）仅 marginally 优于 binary + random depth assignment。

      CORAL accuracy 0.37 vs binary+random 0.32: delta 仅 5pp。这个 delta 主要来自
      CORAL 在 depth 0 和 depth 1 上的正确分类——对 depth 2-5 的预测，CORAL 几乎和
      random assignment 一样糟糕，因为 features 在 depth 2+ 不可区分。

      Standard multiclass（不利用 ordinal structure）的 accuracy（0.35）和 CORAL（0.37）
      接近，说明 ordinal structure 的额外 inductive bias 在 K*=2 条件下几乎无用——
      当只有 2 个 meaningfully distinct levels 时，ordinal vs nominal 的区别消失。

      Ordinal regression（连续 depth 预测 + discretization）的 MAE 1.10 略好于 multiclass 的 1.22，
      但差异很小。所有方法的 macro_F1 都很低（0.18-0.22），因为 depth 2-5 的 per-class F1
      接近 0。

      这直接验证了 worst 档的核心假设："ordinal classifier barely outperforms
      binary + random depth assignment"。ordinal 方法的 overhead（更复杂的 loss function，
      更多 hyperparameters）不 justify 其 marginal gain。
    tables:
      - name: "Table: Classifier comparison"
        columns: ["method", "accuracy", "MAE", "macro_F1"]
        rows:
          - ["CORAL (ordinal)", 0.37, 1.08, 0.22]
          - ["Standard multiclass", 0.35, 1.22, 0.19]
          - ["Ordinal regression", 0.36, 1.10, 0.21]
          - ["Binary + random depth", 0.32, 1.25, 0.18]
    figures_description:
      - "Confusion matrix (4 panels): CORAL / multiclass / regression / binary+random 的 6×6 confusion matrices。所有四个矩阵的 structure 相似：depth 0 行准确率高（>80%），depth 1 行中等（~40%），depth 2-5 行近乎 uniform random。四个矩阵视觉上难以区分，强调 classifier choice 不重要。"
      - "Per-class F1 bar chart: 6 个 depth levels，4 种方法。Depth 0 bars 高（0.7-0.8），depth 1 中等（0.3-0.4），depth 2-5 几乎为 0。所有方法的 per-class pattern 完全一致。"
    analysis: >
      Classifier comparison 实验为 worst 叙事提供重要支撑：
      depth estimation 的瓶颈不在 classifier architecture，而在 feature-level signal。
      无论用什么 classifier，depth 2+ 的分类都接近 random。
      这意味着 C1 的 framing 是正确的——K*=2 是 information-theoretic ceiling，
      不是 classifier capacity 的限制。
      对论文：此实验可以简洁地放在 main paper 中，一个 table + 一段分析即可，
      用于排除 "better classifier might help" 的 reviewer objection。

  # ============================================================
  # exp-011: LLM zero-shot depth estimation
  # ============================================================
  - name: "LLM zero-shot depth estimation baseline"
    plan_id: "exp-011"
    description: >
      GPT-4o / Claude 3.5 对 depth 0-4 文本做 zero-shot depth 判断。
    expected_results:
      gpt4o:
        accuracy: 0.24
        mae: 1.65
        binary_accuracy_human_vs_synthetic: 0.78
        depth_estimation_kendall_tau: 0.12
      claude35:
        accuracy: 0.22
        mae: 1.72
        binary_accuracy_human_vs_synthetic: 0.81
        depth_estimation_kendall_tau: 0.10
      random_baseline_accuracy: 0.20
      both_models_depth_2plus_accuracy: 0.08
    result_rationale: >
      在 worst 档下，frontier LLMs 的 zero-shot depth estimation 接近 random baseline。

      GPT-4o 和 Claude 3.5 都有一定的 binary detection 能力（human vs synthetic: 78-81%），
      这与它们的 RLHF training 中对 "machine-generated text" 的 implicit awareness 一致。
      但 depth estimation（0/1/2/3/4 的精确分类）完全失败：accuracy 0.22-0.24
      仅比 5-class random（0.20）高 2-4pp。

      原因分析：
      (1) Zero-shot 没有 calibrated features——LLMs 依赖 surface-level heuristics
          （如 repetitiveness, formality）而非 information-theoretic statistics；
      (2) 即使 LLMs 有 implicit depth awareness，depth 2-4 的文本在 surface features
          上几乎不可区分——这与我们 handcrafted features 的发现一致；
      (3) LLMs 倾向于 overestimate depth（把 gen-1 判为 gen-3），因为它们 associate
          "synthetic" with "low quality" 但不能 quantify degradation degree。

      Kendall tau 0.10-0.12 表明 predicted depth 与 true depth 几乎没有 monotonic 关系。
      两个模型在 depth 2+ 上的 accuracy 仅 8%（5-class random 在 3 个 class 上的
      期望准确率 = 3/5 × 1/5 = 12%，实际低于 random 因为 LLMs 系统性地 misclassify
      depth 2+ 为 depth 1）。

      这验证了 "depth estimation needs specialized methods" 的 premise，
      但在 worst 档下也削弱了 positive framing——即使专门方法也只能做到 K*=2。
    tables:
      - name: "Table: LLM zero-shot depth estimation"
        columns: ["model", "5-class_acc", "MAE", "binary_acc", "kendall_tau"]
        rows:
          - ["GPT-4o", 0.24, 1.65, 0.78, 0.12]
          - ["Claude 3.5", 0.22, 1.72, 0.81, 0.10]
          - ["Random baseline", 0.20, 2.00, 0.50, 0.00]
          - ["Our classifier (CORAL)", 0.37, 1.08, 0.93, 0.35]
    figures_description:
      - "Grouped bar chart: 5-class accuracy for GPT-4o / Claude / Random / CORAL。CORAL 明显高于 LLMs，但所有方法都远低于 practical utility（~0.6+）。LLMs 仅略高于 random。"
    analysis: >
      LLM zero-shot 实验的价值在于建立 lower bound 和验证 problem difficulty。
      即使 frontier models 也无法做 depth estimation，说明这不是 trivial task。
      但在 worst 档下，我们的 specialized method（CORAL, acc 0.37）也只比 LLMs 高 13-15pp，
      且仍远低于实用水平——这更多地证明了 task difficulty 而非 method value。
      论文中可以用此实验支撑 "depth estimation is fundamentally hard" 的叙事。

  # ============================================================
  # exp-012: Binary detector confidence as depth proxy
  # ============================================================
  - name: "Binary detector confidence as depth proxy"
    plan_id: "exp-012"
    description: >
      用 DivEye/Binoculars score 的 Spearman correlation with true depth，
      验证 binary confidence ≠ depth。
    expected_results:
      diveye_spearman_rho: 0.18
      diveye_spearman_p: 0.001
      binoculars_spearman_rho: 0.22
      binoculars_spearman_p: 0.001
      diveye_auc_0v1: 0.91
      diveye_auc_1v2: 0.54
      binoculars_auc_0v1: 0.94
      binoculars_auc_1v2: 0.56
      diveye_depth_2plus_rank_correlation: 0.03
      binoculars_depth_2plus_rank_correlation: 0.05
    result_rationale: >
      在 worst 档下，binary detector 的 confidence score 与 true depth 的 correlation 很低。

      DivEye 和 Binoculars 的 Spearman rho（0.18, 0.22）虽然统计显著（p < 0.001，
      因大样本量），但 effect size 很小。这些 detector 是为 binary detection 设计的，
      它们的 score 反映的是 "how synthetic" 而非 "which generation"。

      Binary detectors 在 0v1 上表现优秀（AUC 0.91-0.94），因为它们正是为此设计的。
      但 1v2 AUC 急剧下降到 0.54-0.56——binary confidence 不能区分 gen-1 和 gen-2，
      因为两者对 detector 来说都是 "synthetic"。

      在 depth 2+ 区域，rank correlation 几乎为 0（0.03-0.05），表明 binary confidence
      完全不 encode depth information beyond binary distinction。
      这支持了论文的 problem formulation："binary detection ≠ depth estimation，
      需要专门方法"。但在 worst 档下，"专门方法"的收益也很有限（K*=2），
      使得这个 motivation story 变得尴尬——
      "we need specialized methods, but they also can't do much better"。
    tables:
      - name: "Table: Binary detector confidence vs true depth"
        columns: ["detector", "spearman_rho", "p_value", "AUC_0v1", "AUC_1v2", "depth_2plus_rho"]
        rows:
          - ["DivEye", 0.18, "<0.001", 0.91, 0.54, 0.03]
          - ["Binoculars", 0.22, "<0.001", 0.94, 0.56, 0.05]
    figures_description:
      - "Scatter plot: binary confidence (x) vs true depth (y), colored by detector。Points form a blob with slight negative trend for depth 0 vs rest, but depth 1-5 are completely interleaved. Regression line nearly flat."
    analysis: >
      此实验确认 binary detection 和 depth estimation 是不同的 tasks。
      但在 worst 档下，depth estimation 本身因 K*=2 而被限制为近 binary problem，
      削弱了 "we need depth estimation" 的 motivation。
      论文需要 nuanced framing：不是 "binary is insufficient so we need depth"，
      而是 "we investigated whether depth estimation is possible beyond binary,
      and found a hard ceiling at K*=2 — this is itself a useful finding for the community"。

  # ============================================================
  # exp-013: Cross-model transfer
  # ============================================================
  - name: "Cross-model transfer"
    plan_id: "exp-013"
    description: >
      在 model A 训练的 depth classifier 在 model B 的 depth chain 上的 transfer accuracy。
    expected_results:
      transfer_matrix_accuracy:
        qwen_to_pythia: 0.28
        qwen_to_olmo: 0.26
        pythia_to_qwen: 0.30
        pythia_to_olmo: 0.25
        olmo_to_qwen: 0.29
        olmo_to_pythia: 0.27
      transfer_matrix_binary_accuracy:
        qwen_to_pythia: 0.82
        qwen_to_olmo: 0.79
        pythia_to_qwen: 0.84
        pythia_to_olmo: 0.77
        olmo_to_qwen: 0.83
        olmo_to_pythia: 0.80
      in_domain_accuracy_avg: 0.35
      cross_model_accuracy_avg: 0.28
      retention_pct: 40
      cross_model_binary_accuracy_avg: 0.81
    result_rationale: >
      在 worst 档下，cross-model transfer 的 6-class accuracy 平均 0.28，
      是 in-domain accuracy（0.35）的 40%——正好在 worst 范围 [30%, 50%] 内。

      Binary transfer（human vs synthetic）表现尚可（平均 0.81），因为 human vs machine 的
      distributional gap 具有跨模型的 generality——不同模型生成的文本与 human text 的
      统计差异是 qualitatively similar 的（如更低的 perplexity variance, 更 peaked surprisal）。

      但 depth-specific transfer 几乎完全失败：cross-model depth estimation 的 accuracy
      仅 0.25-0.30，接近 6-class random（0.167）。原因：不同模型的 depth-specific
      feature signatures 是 model-specific 的——Qwen 的 gen-2 和 Pythia 的 gen-2
      在 feature space 中的位置不同，因为 degradation 的 trajectory 取决于
      model-specific generation dynamics。

      retention_pct = 40% 表明 cross-model transfer 保留了不到一半的
      in-domain performance，且 retention 主要来自 binary distinction。
      对 depth 2+ 的 transfer 接近 chance。

      这直接支持 worst 档假设："cross-model transfer for depth is near chance
      beyond binary distinction"。
    tables:
      - name: "Table: Cross-model transfer matrix (6-class accuracy)"
        columns: ["train\\test", "Qwen", "Pythia", "OLMo"]
        rows:
          - ["Qwen", "0.37*", 0.28, 0.26]
          - ["Pythia", 0.30, "0.35*", 0.25]
          - ["OLMo", 0.29, 0.27, "0.33*"]
      - name: "Table: Cross-model transfer matrix (binary accuracy)"
        columns: ["train\\test", "Qwen", "Pythia", "OLMo"]
        rows:
          - ["Qwen", "0.93*", 0.82, 0.79]
          - ["Pythia", 0.84, "0.91*", 0.77]
          - ["OLMo", 0.83, 0.80, "0.88*"]
    figures_description:
      - "Two heatmaps side-by-side: (a) 6-class transfer accuracy, (b) binary transfer accuracy。(a) 中 off-diagonal cells 明显浅色（低 accuracy），(b) 中 off-diagonal cells 接近 diagonal。视觉对比传达 'binary signal transfers, depth signal does not'。"
    analysis: >
      Cross-model transfer 实验清楚地分离了 two levels of signal：
      (1) Binary (human vs synthetic): transfers well (avg 0.81) — this is the robust, universal signal；
      (2) Depth-specific: transfers poorly (avg 0.28, retention 40%) — this is model-specific。
      在 worst 档下，depth estimation 不仅 K*=2，而且 model-specific，
      进一步限制了其实用价值——你需要为每个 target model 重新训练 classifier。
      论文可以将此 framing 为 additional evidence that depth signal beyond binary is fragile。

  # ============================================================
  # exp-014: Naturalistic validation (Common Crawl)
  # ============================================================
  - name: "Naturalistic validation on Common Crawl"
    plan_id: "exp-014"
    description: >
      对 Common Crawl 2025/2026 snapshot 样本做 depth 预测，
      与 AlignScore 和独立 vocabulary richness 指标做 correlation。
    expected_results:
      predicted_depth_distribution:
        depth_0: 0.62
        depth_1: 0.25
        depth_2plus: 0.13
      correlation_predicted_depth_vs_alignscore: -0.15
      correlation_predicted_depth_vs_vocab_richness: -0.19
      correlation_binary_synthetic_vs_alignscore: -0.28
      fraction_predicted_synthetic: 0.38
      confidence_calibration_note: "predictions heavily concentrated in depth 0-1; depth 2+ predictions are low-confidence and unreliable"
    result_rationale: >
      在 worst 档下，naturalistic validation 结果 weak 且 ambiguous。

      Predicted depth distribution（62% human, 25% gen-1, 13% gen-2+）看似 reasonable，
      但缺乏 ground truth 使得无法验证准确性。38% predicted synthetic rate
      与近期估计（Common Crawl 2025+ 含 15-40% synthetic text）粗略一致，
      但 confidence interval 极宽。

      Predicted depth 与 AlignScore 的 correlation（-0.15）很弱——
      higher predicted depth 仅 weakly 关联 lower quality。原因：
      (1) AlignScore 衡量的 factual consistency 与 generation depth 不直接对应；
      (2) 我们的 depth predictor 在 depth 2+ 上 unreliable，产生 noisy predictions；
      (3) Common Crawl 中的 synthetic text 来自 diverse models/prompts/settings，
          与我们 controlled experiment 的 distribution 不匹配。

      Vocabulary richness correlation（-0.19）略高但仍弱，反映 generation depth 对
      lexical diversity 确有 monotone 影响，但在 wild data 中被其他 confounders 淹没
      （topic, domain, author style, length）。

      Binary detection（synthetic vs human）与 quality metrics 的 correlation（-0.28）
      高于 depth estimation，再次表明 binary signal 是 robust 且 useful 的，
      而 graduated depth 在 wild data 上几乎没有额外信息。
    tables:
      - name: "Table: Common Crawl naturalistic validation"
        columns: ["metric", "value"]
        rows:
          - ["Predicted human fraction", 0.62]
          - ["Predicted gen-1 fraction", 0.25]
          - ["Predicted depth-2+ fraction", 0.13]
          - ["Corr(predicted_depth, AlignScore)", -0.15]
          - ["Corr(predicted_depth, vocab_richness)", -0.19]
          - ["Corr(binary_synthetic, AlignScore)", -0.28]
    figures_description:
      - "Histogram: predicted depth distribution on Common Crawl sample. 高度 right-skewed，depth 0 主导。"
      - "Scatter plot: predicted depth vs AlignScore。Cloud with slight negative trend but massive scatter。R² annotation 显示 <0.03。"
    analysis: >
      Naturalistic validation 在 worst 档下提供 weak signal at best。
      这是意料之中的——将 controlled experiment 的 classifier 直接 deploy 到
      heterogeneous wild data 是 domain shift 问题。
      论文可以将此作为 appendix 的 preliminary exploration，但不应依赖此实验
      支撑任何 claim。在 worst narrative 中，此实验实际上 supports 论文的
      cautionary message："depth estimation 在 controlled 条件下都 limited，
      在 wild 条件下更不可靠"。

  # ============================================================
  # exp-015: Learned representation baseline
  # ============================================================
  - name: "Learned representation baseline"
    plan_id: "exp-015"
    description: >
      Frozen Qwen2.5-1.5B embeddings + MLP vs hand-crafted 15D features。
    expected_results:
      learned_repr_accuracy: 0.39
      learned_repr_mae: 1.05
      handcrafted_accuracy: 0.37
      handcrafted_mae: 1.08
      learned_repr_auc_0v1: 0.997
      learned_repr_auc_1v2: 0.72
      learned_repr_auc_2v3: 0.58
      learned_repr_k_star: 2
      accuracy_delta: 0.02
      mae_delta: -0.03
    result_rationale: >
      在 worst 档下，learned representations 略优于 handcrafted features，但不改变 K*。

      Frozen LM embeddings（4096-dim from last layer）+ 2-layer MLP 有更大的 capacity
      来 capture subtle distributional differences。1v2 AUC 从 handcrafted 的 0.70 提升到
      0.72——这表明 LM embeddings 确实 encode 了一些 handcrafted features 未 capture 的信息。
      但 2v3 AUC 仍然只有 0.58，不足以突破 K*=2 的 boundary。

      accuracy 提升 2pp（0.39 vs 0.37），MAE 改善 0.03（1.05 vs 1.08）——
      这些差异在统计上可能 significant（取决于 test set size），但 practically negligible。

      关键洞察：learned representations 的 marginal improvement 确认了 handcrafted features
      不是 bottleneck——K*=2 是 information-theoretic ceiling，不是 feature engineering 的限制。
      即使用模型自身的 full-dimensional representation，depth 2+ 的信号仍然不足。

      这对 worst narrative 是重要支撑：既排除了 "better features might help" 的 objection，
      又验证了 handcrafted features 的 interpretability 价值不是以 significant accuracy 为代价的。
    tables:
      - name: "Table: Handcrafted vs learned representations"
        columns: ["feature_type", "accuracy", "MAE", "AUC_1v2", "AUC_2v3", "K*"]
        rows:
          - ["Handcrafted (15D)", 0.37, 1.08, 0.70, 0.59, 2]
          - ["Learned (4096D + MLP)", 0.39, 1.05, 0.72, 0.58, 2]
    figures_description:
      - "Side-by-side pairwise AUC curves: handcrafted vs learned. 两条曲线几乎重合，在 depth 2+ 区域 converge 到同一水平。Marginal separation 仅在 1v2 可见。"
    analysis: >
      Learned representation 实验排除了 feature engineering 作为 bottleneck 的可能性。
      在论文中，这是 important control：证明 K*=2 是 data-intrinsic 的 ceiling，
      与 feature choice 无关。同时 justify 了使用 interpretable handcrafted features
      作为 primary analysis tool（loss < 2pp accuracy, gain = full interpretability for C2 analysis）。

  # ============================================================
  # exp-016: Base vs Instruct model comparison
  # ============================================================
  - name: "Base vs Instruct model comparison"
    plan_id: "exp-016"
    description: >
      Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异。
    expected_results:
      base:
        k_star: 2
        pairwise_auc_0v1: 0.982
        pairwise_auc_1v2: 0.64
        pairwise_auc_2v3: 0.55
        pairwise_jsd_0v1: 0.210
        pairwise_jsd_1v2: 0.012
        pairwise_jsd_2v3: 0.004
        ordinal_accuracy: 0.34
        ordinal_mae: 1.15
      instruct_mvp_reference:
        k_star: 2
        pairwise_auc_0v1: 0.996
        pairwise_auc_1v2: 0.70
        pairwise_auc_2v3: 0.59
        pairwise_jsd_0v1: 0.267
        pairwise_jsd_1v2: 0.016
        pairwise_jsd_2v3: 0.007
      base_vs_instruct_0v1_jsd_delta: -0.057
      base_vs_instruct_1v2_auc_delta: -0.06
    result_rationale: >
      在 worst 档下，Base model 也产生 K*=2，但信号绝对值更低。

      Base model（未经 instruction tuning）的 generation 更 "raw"——
      less coherent, higher entropy, less human-like structure。这导致：

      (1) 0v1 gap 更小（JSD 0.210 vs Instruct 0.267）：base model 的输出本身就
          less structured than human text but also less "distinctively machine-like"
          compared to Instruct models（后者有 RLHF-induced patterns 如 hedging language,
          structured responses that are clearly non-human）；

      (2) 1v2 AUC 更低（0.64 vs 0.70）：base model 的递归 generation 更 chaotic，
          gen-1 和 gen-2 在 feature space 中更接近——high entropy generation 在
          first pass 就引入大量噪声，使后续代际差异更小；

      (3) K* 不变：尽管绝对信号更弱，depth 2+ 的 collapse 模式相同。

      这表明 RLHF/instruction tuning 使模型输出更 "detectably machine-like"
      （higher 0v1 signal），但不改变 recursive degradation 的 fundamental dynamics。
      对 worst narrative：base model 结果是对 K*=2 universality 的又一确认，
      且暗示实际世界中 base model 生成的 recursive text 更难检测（更低的 0v1 AUC）。
    tables:
      - name: "Table: Base vs Instruct comparison (Qwen2.5-1.5B)"
        columns: ["variant", "K*", "AUC_0v1", "AUC_1v2", "AUC_2v3", "JSD_0v1", "ordinal_acc"]
        rows:
          - ["Instruct (MVP)", 2, 0.996, 0.70, 0.59, 0.267, 0.42]
          - ["Base", 2, 0.982, 0.64, 0.55, 0.210, 0.34]
    figures_description:
      - "Paired JSD decay curves: base（虚线）vs instruct（实线）。Instruct 曲线始终在 base 之上，但两者在 depth 2+ 都 converge to floor。Gap 在 0v1 最大，1v2 已缩小，2v3 几乎消失。"
    analysis: >
      Base vs Instruct 对比提供了对 RLHF 效应的洞察：instruction tuning 增强了
      human vs machine 的 detectability（因为 RLHF 引入了 specific stylistic patterns），
      但不改变 recursive degradation dynamics。在 worst 档下，两个 variant 的 K*=2
      进一步缩小了 "K* might vary with model variant" 的可能性空间。
      论文可以简短讨论此结果，作为 K* universality 的 additional evidence point。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d77efc0e-911b-4c27-801d-5d4e9d631e7d",
  "isSidechain": false,
  "requestId": "req_011CayHmGNYLK7e8NUQTKSX6",
  "type": "assistant",
  "uuid": "d278d351-3dc2-4ba2-a1c0-f4c0fdb83acc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyvE8Nym3vAh8531TvYbBN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10229,
      "cache_read_input_tokens": 11841,
      "output_tokens": 21880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21880,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10229
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：K*=2 is universal and unmodulable, degradation ordering is inconsistent, graduated filtering does not significantly outperform binary 核心假设：['K*=2 across a…",
  "leafUuid": "d278d351-3dc2-4ba2-a1c0-f4c0fdb83acc",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Worst-case scenario depth estimation empirical characterization",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：K*=2 is universal and unmodulable, degradation ordering is inconsistent, graduated filtering does not significantly outperform binary 核心假设：['K*=2 across a…",
  "leafUuid": "d278d351-3dc2-4ba2-a1c0-f4c0fdb83acc",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Worst-case scenario depth estimation empirical characterization",
  "sessionId": "b07282be-9ccf-4dae-909a-2be30d69df05"
}
```

---
