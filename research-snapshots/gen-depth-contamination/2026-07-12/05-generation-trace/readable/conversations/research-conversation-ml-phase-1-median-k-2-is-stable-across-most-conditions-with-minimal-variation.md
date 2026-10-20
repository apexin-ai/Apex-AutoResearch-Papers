# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：K*=2 is stable across most conditions with minimal variation, degradation 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/d6bebd24-c6ab-4068-aa92-293da9457dd7.jsonl`
- **Structured JSON:** [`5ee41c433b031bc62574.json`](../../sessions/5e/5ee41c433b031bc62574.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T20:10:40.118Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T20:10:40.118Z",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：K*=2 is stable across most conditions with minimal variation, degradation ordering partially holds, graduated filtering shows modest but real gains\n核心假设：['K*=2 across all 1.5B models and most decoding strategies; only extreme settings (T≥1.2) push K* to 3 on one model', '7B model shows K*=2 or K*=3 inconsistently across seeds', 'Vocabulary diversity generally saturates first but ordering is not perfectly consistent across models (tau 0.5-0.8)', 'Graduated filtering improves over binary but effect size is modest (0.5-1.5pp) and seed variance overlaps', 'Cross-model transfer works for binary (gen-0 vs gen-1+) but degrades substantially for ordinal depth', 'Retrain-chain shows qualitatively similar pattern but quantitative K* may differ by 1']\n关键指标范围：{'k_star_range_across_conditions': [2, 2], 'k_star_extreme_decoding': [2, 3], 'pairwise_auc_1v2_cross_model': [0.6, 0.7], 'pairwise_auc_2v3_any_condition': [0.55, 0.63], 'ordinal_accuracy_best_config': [0.38, 0.45], 'ordinal_mae_best_config': [0.9, 1.1], 'downstream_delta_graduated_vs_binary_mmlu_pp': [0.5, 1.5], 'downstream_delta_graduated_vs_binary_hellaswag_pp': [0.3, 1.2], 'cross_model_transfer_retention_pct': [50, 65], 'degradation_ordering_kendall_tau': [0.5, 0.8]}\n叙事方向：需要调整 claims 的强度和重心。K*=2 不再是\"modulable quantity\"而是\"robust empirical constant for current-generation 1-2B models\"—— reframe 为 universality result 而非 variability result。C1 从\"K* varies with conditions\"收缩为\"K*=2 is a stable, measurable boundary that DPI predicts must exist\"。 C2 degradation ordering 降级为\"tendency\"而非\"strict ordering\"，用 partial consistency 论证仍有 structural regularity。 C3 graduated filtering 从\"clear improvement\"调整为\"better calibrated near threshold\"——强调 calibration 优势而非 raw accuracy gap。 补强 characterization/measurement 贡献：首次系统测量 K*、首次做 depth estimation task formulation。 投稿策略：EMNLP Main 仍可尝试但准备 Findings fallback。需要在 rebuttal 中有力回应\"K*=2 + modest filtering gain = incremental\"。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-contamination\nvenue: EMNLP 2026\nfocus: Route B framing: K* as first-measured saturation boundary, DPI theory validation, graduated filtering with coarse 3-class signal. Key risk: K*=2 may be seen as too shallow for practical impact.\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Core Claims (3 条)\n\n1. **C1 (Saturation Boundary)**: 递归合成文本的代际辨别能力存在可测量的饱和边界 K*，这是一个信息论基本量（DPI 的必然推论），而非分类器能力上限。首次在受控实验中系统测量 K* 并表征其随模型、解码策略的变化。\n2. **C2 (Linguistic Degradation Ordering)**: 递归生成导致语言特征按特定顺序逐层坍缩——vocabulary diversity 先于 surprisal dynamics 饱和，揭示递归生成的结构性规律。\n3. **C3 (Graduated Filtering)**: 即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+三级）下，depth-graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al.) 描述宏观现象但不提供检测工具；verification-based methods (Feng et al., Yi et al.) 用外部验证器做 binary quality gate 但不估计递归深度。**无任何方法估计文本经历了多少轮递归生成。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（Data Processing Inequality）推导出辨别饱和边界 K* 的必然存在。K* 本身是首次测量的基本量——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过系统测量 K* 随模型架构和解码策略的变化，揭示控制 K* 的因素，为实际数据治理提供 actionable guidance。\n- **Headline result template**: \"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with JSD decaying monotonically (0.27→0.004) across 5 generations, and demonstrate that even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*=2 太浅，graduated filtering 收益有限\"** → K* 是模型/解码策略依赖的；展示不同解码策略（高温度/low top-p）如何调控 K*；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated\n2. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation（首次将 depth estimation 作为 prediction task）+ empirical characterization（首次测量 K*）+ 理论框架（DPI impossibility boundary），不是分类器本身\n3. **\"Prompt-chain 不代表真实世界递归污染\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法；wild data 的 Common Crawl 验证作为 appendix\n4. **\"单模型/单数据集，泛化性不够\"** → 扩展到 3 个模型族（Pythia/OLMo/Qwen）+ cross-scale probe（7B）+ 2 个种子数据集\n5. **\"同模型做生成和 surprisal 计算有 bias\"** → 显式讨论此 design choice：这衡量的是\"模型对自身递归输出的 self-recognition\"，与 binary detection 的 premise 一致；cross-model transfer 实验验证特征不是模型特异的\n6. **\"为什么不用 learned representations\"** → 作为 baseline 对比（frozen LM embeddings + MLP），但 hand-crafted features 更 interpretable 且支持 degradation ordering 分析\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 本文同时是 method（depth estimation algorithm）和 empirical study（K* characterization），符合 EMNLP 对 \"Resources and Evaluation\" track 的要求\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization 的 novelty\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-003\n  claim: 1,3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth\n    0-3. 测试 K* 是否随模型规模变化。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: null\n  status: planned\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary / graduated / surprisal-based 四种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。3 seeds。'\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-007\n  claim: 1,2\n  description: 'K* sensitivity analysis: 在 0.55/0.60/0.65/0.70 四个阈值下计算 K*，展示 K* 对阈值选择的稳健性。'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: null\n  status: planned\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: null\n  status: planned\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: null\n  status: planned\n- id: exp-010\n  claim: 1,2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: null\n  status: planned\n- id: exp-013\n  claim: 1,2\n  description: 'Cross-model transfer: 在 model A 训练的 depth classifier 在 model B 的 depth\n    chain 上的 transfer accuracy。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: null\n  status: planned\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features，验证 interpretable features 的价值。'\n  priority: P2\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: null\n  status: planned\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: null\n  status: planned\n- id: mvp-001\n  claim: 1,2,3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_sat_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-12T20:10:40.122Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T20:10:40.122Z",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-12T20:10:40.139Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：K*=2 is stable across most conditions with minimal variation, degradation ordering partially holds, graduated filtering shows modest but real gains
核心假设：['K*=2 across all 1.5B models and most decoding strategies; only extreme settings (T≥1.2) push K* to 3 on one model', '7B model shows K*=2 or K*=3 inconsistently across seeds', 'Vocabulary diversity generally saturates first but ordering is not perfectly consistent across models (tau 0.5-0.8)', 'Graduated filtering improves over binary but effect size is modest (0.5-1.5pp) and seed variance overlaps', 'Cross-model transfer works for binary (gen-0 vs gen-1+) but degrades substantially for ordinal depth', 'Retrain-chain shows qualitatively similar pattern but quantitative K* may differ by 1']
关键指标范围：{'k_star_range_across_conditions': [2, 2], 'k_star_extreme_decoding': [2, 3], 'pairwise_auc_1v2_cross_model': [0.6, 0.7], 'pairwise_auc_2v3_any_condition': [0.55, 0.63], 'ordinal_accuracy_best_config': [0.38, 0.45], 'ordinal_mae_best_config': [0.9, 1.1], 'downstream_delta_graduated_vs_binary_mmlu_pp': [0.5, 1.5], 'downstream_delta_graduated_vs_binary_hellaswag_pp': [0.3, 1.2], 'cross_model_transfer_retention_pct': [50, 65], 'degradation_ordering_kendall_tau': [0.5, 0.8]}
叙事方向：需要调整 claims 的强度和重心。K*=2 不再是"modulable quantity"而是"robust empirical constant for current-generation 1-2B models"—— reframe 为 universality result 而非 variability result。C1 从"K* varies with conditions"收缩为"K*=2 is a stable, measurable boundary that DPI predicts must exist"。 C2 degradation ordering 降级为"tendency"而非"strict ordering"，用 partial consistency 论证仍有 structural regularity。 C3 graduated filtering 从"clear improvement"调整为"better calibrated near threshold"——强调 calibration 优势而非 raw accuracy gap。 补强 characterization/measurement 贡献：首次系统测量 K*、首次做 depth estimation task formulation。 投稿策略：EMNLP Main 仍可尝试但准备 Findings fallback。需要在 rebuttal 中有力回应"K*=2 + modest filtering gain = incremental"。


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
  "promptId": "89feafb1-3a32-4233-b707-1728504086ba",
  "type": "user",
  "uuid": "29ebd45a-3ad5-4943-bf48-e7a60dbb190d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T20:10:40.138Z_

```json
{
  "parentUuid": "29ebd45a-3ad5-4943-bf48-e7a60dbb190d",
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
  "uuid": "5b4ed4cc-795a-44f9-92c1-c2c22940608b",
  "timestamp": "2026-05-12T20:10:40.138Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T20:10:40.138Z_

```json
{
  "parentUuid": "5b4ed4cc-795a-44f9-92c1-c2c22940608b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "70511705-dd1e-499c-acb7-39b92e8a8f1a",
  "timestamp": "2026-05-12T20:10:40.138Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7",
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
  "aiTitle": "Characterize K* saturation boundary in recursive generation",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7"
}
```

---

### Assistant

_source line 7 · 2026-05-12T20:11:14.949Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all planned experiments in the experiment plan, based on the "median" tier definition provided. I need to produce a YAML block with predicted results for each experiment, including rationale for why those results would be expected under the median tier.

Let me carefully go through each experiment and predict results consistent with the median tier definition.

Key median tier characteristics:
- K*=2 is stable across most conditions with minimal variation
- Only extreme settings (T≥1.2) push K* to 3 on one model
- 7B model shows K*=2 or K*=3 inconsistently across seeds


- Vocabulary diversity saturates first but ordering varies (tau 0.5-0.8)
- Graduated filtering shows modest improvements over binary (0.5-1.5pp) with overlapping seed variance
- Cross-model transfer works for binary but degrades for ordinal depth
- Retrain-chain follows similar patterns with potential K* shifts of ±1

Now I'm looking at the expected metric ranges to anchor my predictions: K* stays between 2-3 across most conditions, cross-model AUC drops from around 0.6-0.7 for binary to lower values for ordinal, and I need to fill in the remaining metric bounds to complete the picture. Looking at the baseline metrics from Qwen2.5-1.5B, I can see the pairwise comparisons show strong discrimination at the top (0v1 AUC of 0.9956) but weaker separation in the middle tiers, with k_star settling at 2 and ordinal accuracy around 0.42. Now I'm working through predictions for the cross-model experiments, starting with Pythia-1.4B where I'd expect similar k_star behavior given the comparable model size, though the older architecture might introduce some variation in the AUC patterns.

For LMo-1B, the slightly smaller scale should still maintain k_star=2 as the optimal clustering. Moving to the decoding strategy ablations on the same base model, I'm predicting k_star=2 across greedy, nucleus, and standard temperature settings, with the extreme temperature of 1.2 potentially pushing toward k_star=3. The 7B model is where things get more interesting—the increased capacity might preserve information differently, possibly showing inconsistent k_star values across different random seeds. For the feature ablation experiments, I'm tracking how vocabulary diversity saturates early in the degradation ordering, and I need to examine the Kendall tau correlations to understand the feature importance rankings.

Now I'm looking at the downstream task performance metrics across different filtering approaches—graduated filtering shows modest gains of 0.5-1.5 percentage points on MMLU and 0.3-1.2 on HellaSwag compared to binary filtering. The k_star sensitivity analysis suggests the optimal value is fairly robust across different threshold choices. When I retrain the models with the chain approach, the results look qualitatively similar though k_star might shift by one. The contamination dose-response experiments show that the graduated approach's advantage scales with how much contamination is introduced. Comparing different modeling approaches, CORAL slightly outperforms the multinomial baseline. The zero-shot LLM depth estimation performs poorly, barely better than random guessing for depths greater than one, and using the binary detector's confidence as a proxy for depth also yields weak correlations. Cross-model transfer works well for binary classification with AUC above 0.85, but ordinal predictions degrade significantly with only 50-65% retention. Finally, the naturalistic validation shows moderate correlations with quality metrics, and I'm still working through the learned representations analysis.

Generating YAML summary...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70511705-dd1e-499c-acb7-39b92e8a8f1a",
  "isSidechain": false,
  "requestId": "req_011CayHLj9fBJGg4vGX8S3zG",
  "type": "assistant",
  "uuid": "57321d77-20e5-47dd-9ff3-3a02631aafe6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SvnnwhskhofgRB7maT5DwE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10236,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17385,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10236
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

_source line 8 · 2026-05-12T20:16:10.542Z_

```yaml
tier: median
narrative_guidance: >
  K*=2 不再是 "modulable quantity" 而是 "robust empirical constant for current-generation 1-2B models"。
  Reframe 为 universality result：首次系统测量表明 K*=2 在 3 个模型族、4 种解码策略下高度稳定，
  仅极端解码（T≥1.2）将 K* 推至 3。C2 degradation ordering 降级为 "tendency"（tau 0.5-0.8），
  vocabulary diversity 倾向先饱和但非严格一致。C3 graduated filtering 强调 calibration 优势而非
  raw accuracy gap（0.5-1.5pp MMLU，seed variance 可重叠）。补强 characterization 贡献：
  首次系统测量 K*、首次将 depth estimation 形式化为 prediction task。
  投稿策略：EMNLP Main 可尝试，准备 Findings fallback，rebuttal 需有力回应 "K*=2 + modest gain = incremental"。

imagined_experiments:
  - name: "Pythia-1.4B depth chain generation"
    plan_id: "exp-001"
    description: "Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5"
    expected_results:
      pairwise_auc_0v1: 0.993
      pairwise_auc_1v2: 0.672
      pairwise_auc_2v3: 0.576
      pairwise_auc_3v4: 0.538
      pairwise_auc_4v5: 0.527
      pairwise_jsd_0v1: 0.241
      pairwise_jsd_1v2: 0.014
      pairwise_jsd_2v3: 0.005
      pairwise_jsd_3v4: 0.003
      pairwise_jsd_4v5: 0.003
      k_star: 2
      ordinal_mae: 1.05
      ordinal_accuracy: 0.40
    result_rationale: >
      Pythia-1.4B 是较早期的 GPT-NeoX 架构，参数量与 Qwen2.5-1.5B 同量级（1.4B vs 1.5B），
      但训练数据量和质量略低（The Pile 300B tokens vs Qwen 的多语言数据）。这意味着 Pythia 的
      生成质量基线略低于 Qwen，gen-0→gen-1 的信息损失稍大（JSD 0.241 vs MVP 的 0.267——
      实际上 Pythia 初始分离度可能略低因为其 gen-0 本身已比 Qwen 的 gen-0 更 "synthetic-like"）。
      但核心现象不变：gen-1→gen-2 的 AUC 从 ~0.67 骤降到 gen-2→gen-3 的 ~0.58，确认 K*=2。
      这是因为 DPI 约束与模型规模相关而非架构特异——1.4B 模型的 lossy channel capacity 
      在第二代即耗尽可辨别信息。Ordinal accuracy 略低于 MVP（0.40 vs 0.42）因为 Pythia 的
      特征空间结构性稍弱。
    tables:
      - caption: "Table: Pythia-1.4B pairwise discrimination (AUC / JSD) by generation gap"
        rows:
          - ["Pair", "AUC (mean±std)", "JSD"]
          - ["0 vs 1", "0.993 ± 0.001", "0.241"]
          - ["1 vs 2", "0.672 ± 0.009", "0.014"]
          - ["2 vs 3", "0.576 ± 0.013", "0.005"]
          - ["3 vs 4", "0.538 ± 0.008", "0.003"]
          - ["4 vs 5", "0.527 ± 0.010", "0.003"]
    figures_description:
      - "JSD decay curve (depth 0-5): 与 MVP Qwen 曲线形状高度相似，gen-0→1 陡降后 gen-2+ 趋近平坦，K*=2 的 elbow 清晰可见"
    analysis: >
      Pythia-1.4B 的 K*=2 与 MVP Qwen2.5-1.5B 一致，初步支持 K* 的跨架构稳定性。
      JSD 衰减曲线形状几乎相同（exponential-like decay），仅 absolute magnitude 有差异。
      这为 "K*=2 is a property of the 1-2B scale regime, not a model-specific artifact" 提供证据。

  - name: "OLMo-1B depth chain generation"
    plan_id: "exp-002"
    description: "OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5"
    expected_results:
      pairwise_auc_0v1: 0.991
      pairwise_auc_1v2: 0.648
      pairwise_auc_2v3: 0.562
      pairwise_auc_3v4: 0.531
      pairwise_auc_4v5: 0.522
      pairwise_jsd_0v1: 0.218
      pairwise_jsd_1v2: 0.012
      pairwise_jsd_2v3: 0.004
      pairwise_jsd_3v4: 0.003
      pairwise_jsd_4v5: 0.002
      k_star: 2
      ordinal_mae: 1.08
      ordinal_accuracy: 0.39
    result_rationale: >
      OLMo-1B 参数量最小（1B），且是完全开源训练流程（Dolma 数据集）。更小的模型容量意味着
      其 lossy channel 在每一代损失更多信息——gen-0 的 vocabulary richness 基线就低于 1.5B 模型，
      因此 gen-0 vs gen-1 的初始 JSD 为三者最低（0.218）。但 K* 仍然是 2：gen-1→gen-2 的
      AUC 0.648 仍显著高于 chance（满足 0.60 阈值），而 gen-2→gen-3 的 0.562 已进入 noise floor
      （在 0.55-0.60 区间）。这恰好说明 K* 是 scale-dependent 的 robust constant：即使在略小的
      1B 模型上，第二代仍然是信息饱和的 phase transition point。Ordinal accuracy 最低（0.39）
      因为 gen-2+ 的类间距更小。
    tables:
      - caption: "Table: OLMo-1B pairwise discrimination (AUC / JSD) by generation gap"
        rows:
          - ["Pair", "AUC (mean±std)", "JSD"]
          - ["0 vs 1", "0.991 ± 0.001", "0.218"]
          - ["1 vs 2", "0.648 ± 0.011", "0.012"]
          - ["2 vs 3", "0.562 ± 0.014", "0.004"]
          - ["3 vs 4", "0.531 ± 0.009", "0.003"]
          - ["4 vs 5", "0.522 ± 0.011", "0.002"]
    figures_description:
      - "三模型 JSD decay 叠加图：Qwen > Pythia > OLMo 的 absolute JSD，但归一化后曲线形状几乎重合，K* elbow 位置一致"
    analysis: >
      OLMo-1B 确认了最小规模下 K*=2 仍成立。三模型族的 K*=2 一致性构成论文的核心 universality evidence。
      可以论证：在 1-2B scale regime 下，K*=2 是 robust empirical constant，不依赖于具体架构
      （GPT-NeoX / Transformer++ / Qwen-style）或训练数据（Pile / Dolma / multilingual）。

  - name: "Qwen2.5-1.5B decoding strategy ablation"
    plan_id: "exp-003"
    description: "Qwen2.5-1.5B 在 greedy / nucleus p=0.9 / T=0.7 / T=1.2 四种解码策略下的 depth chain"
    expected_results:
      greedy:
        pairwise_auc_1v2: 0.714
        pairwise_auc_2v3: 0.603
        k_star: 2
        pairwise_jsd_0v1: 0.302
        pairwise_jsd_1v2: 0.019
      nucleus_p09:
        pairwise_auc_1v2: 0.688
        pairwise_auc_2v3: 0.582
        k_star: 2
        pairwise_jsd_0v1: 0.258
        pairwise_jsd_1v2: 0.015
      T07:
        pairwise_auc_1v2: 0.708
        pairwise_auc_2v3: 0.597
        k_star: 2
        pairwise_jsd_0v1: 0.289
        pairwise_jsd_1v2: 0.018
      T12:
        pairwise_auc_1v2: 0.651
        pairwise_auc_2v3: 0.583
        pairwise_auc_3v4: 0.558
        k_star_seed1: 2
        k_star_seed2: 3
        k_star_seed3: 2
        k_star_majority: 2
        pairwise_jsd_0v1: 0.195
        pairwise_jsd_1v2: 0.011
    result_rationale: >
      解码策略通过控制 sampling entropy 调节每一代的信息损失率。
      Greedy（T=0, argmax）：最低 entropy sampling → 每代输出最 "mode-collapsed"，gen-0 vs gen-1 
      的初始差异最大（JSD 0.302）因为 greedy 输出与 human text 的分布差距最大。但这个大初始差距
      也使得 gen-1 vs gen-2 的 AUC 最高（0.714），因为 gen-1 仍保留可辨别的 diversity 信号。
      K*=2 因为 gen-2→gen-3 在 0.603 处——接近阈值但仍 above。
      Nucleus p=0.9：比 MVP baseline（p=0.95）稍 tighter，效果与 baseline 相近，K*=2。
      T=0.7（low temperature）：类似 greedy 的效果但稍温和，K*=2。
      T=1.2（high temperature）：高温增加采样随机性，每代注入更多 noise。这使得 gen-0→gen-1 
      的信息损失最小（JSD 0.195）——高温输出本身就更 diverse 更接近 human text。但同时，
      高温使 gen-1→gen-2 的辨别力降低（AUC 0.651），而 gen-2→gen-3 在 0.583——某些 seed 
      下可能越过 0.60 阈值使 K*=3。这是唯一导致 K* 不稳定的条件：3 个 seed 中 1 个显示 K*=3，
      多数仍为 2。机制是高温保留了更多 per-generation variance，使得 DPI 的信息压缩在第三代
      才完全饱和。
    tables:
      - caption: "Table: Decoding strategy ablation — K* and key AUC values"
        rows:
          - ["Strategy", "AUC 0v1", "AUC 1v2", "AUC 2v3", "JSD 0v1", "K*"]
          - ["Greedy", "0.997", "0.714", "0.603", "0.302", "2"]
          - ["Nucleus p=0.9", "0.996", "0.688", "0.582", "0.258", "2"]
          - ["T=0.7", "0.997", "0.708", "0.597", "0.289", "2"]
          - ["T=1.2", "0.992", "0.651", "0.583", "0.195", "2 (1 seed: 3)"]
          - ["MVP baseline (p=0.95)", "0.996", "0.696", "0.589", "0.267", "2"]
    figures_description:
      - "五种解码策略的 JSD decay curve 叠加：greedy 曲线最高、T=1.2 最低，但 K* elbow 位置一致"
      - "T=1.2 条件下 3 seeds 的 AUC 2v3 scatter plot + 0.60 threshold line：展示 seed variance 导致的 K* 不稳定"
    analysis: >
      四种解码策略中 K*=2 完全稳定，仅 T=1.2 在部分 seed 下 K*=3。这支持 median tier 的核心叙事：
      K*=2 是 robust constant，极端解码是目前发现的唯一调控因素。论文中可以用此结果论证
      "K* is remarkably stable across decoding strategies, with only extreme temperature 
      (T≥1.2) occasionally extending it to 3"。

  - name: "Qwen2.5-7B cross-scale probe"
    plan_id: "exp-004"
    description: "Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3"
    expected_results:
      pairwise_auc_0v1: 0.989
      pairwise_auc_1v2: 0.718
      pairwise_auc_2v3: 0.612
      pairwise_jsd_0v1: 0.193
      pairwise_jsd_1v2: 0.020
      pairwise_jsd_2v3: 0.008
      k_star_seed1: 2
      k_star_seed2: 3
      k_star_seed3: 2
      k_star_majority: 2
      ordinal_mae: 0.93
      ordinal_accuracy: 0.44
    result_rationale: >
      7B 模型的 channel capacity 更高——更大的模型在每一代保留更多信息，因此信息衰减更慢。
      这体现在：(1) gen-0 vs gen-1 的 JSD 更低（0.193 vs 1.5B 的 0.267），因为 7B 的生成质量
      更高，gen-1 与 human text 的分布差异更小；(2) gen-1 vs gen-2 的 AUC 更高（0.718 vs 0.696），
      因为 7B 在 gen-1 中保留了更多可辨别特征；(3) gen-2 vs gen-3 的 AUC 在 0.612——处于
      K*=2 和 K*=3 的边界。某些 seed 下 AUC 2v3 越过 0.60 → K*=3，其他 seed 下刚好在边界上。
      这种 seed-level instability 是 median tier 的特征预测。机制解释：7B 的 lossy channel 
      压缩率更低，DPI 导致的饱和在第三代才完成，而非第二代。但由于只有 1K docs（而非 5K），
      统计 power 较低，加剧了 seed variance。如果有 5K docs，K* 可能稳定在 3。
    tables:
      - caption: "Table: Qwen2.5-7B pairwise discrimination (3 seeds)"
        rows:
          - ["Pair", "AUC (seed1/seed2/seed3)", "K* per seed"]
          - ["0 vs 1", "0.990/0.988/0.989", "-"]
          - ["1 vs 2", "0.722/0.710/0.721", "-"]
          - ["2 vs 3", "0.618/0.597/0.620", "3/2/3"]
    figures_description:
      - "1.5B vs 7B 的 AUC decay curve 对比：7B 曲线整体右移（信息保留更久），K* 边界从 sharp 变为 fuzzy"
    analysis: >
      7B 的结果暗示 K* 可能随模型规模增长而增大，但在当前实验规模下无法确定性地声称 K*=3。
      论文中应保守表述："7B models show suggestive evidence that K* may increase with scale, 
      but the effect is within seed variance at our sample size"。这为 future work（更大模型、
      更多数据）留下了自然的延伸方向。

  - name: "Feature group ablation + degradation ordering"
    plan_id: "exp-005"
    description: "对 Pythia-1.4B 和 OLMo-1B 的 depth chain 按 feature group 分析饱和深度和 degradation ordering"
    expected_results:
      pythia_saturation_order: ["vocabulary_diversity", "tail_thinning", "surprisal_dynamics"]
      olmo_saturation_order: ["vocabulary_diversity", "surprisal_dynamics", "tail_thinning"]
      vocabulary_diversity_saturation_depth_range: [1.5, 2.0]
      surprisal_dynamics_saturation_depth_range: [2.0, 2.5]
      tail_thinning_saturation_depth_range: [2.0, 3.0]
      kendall_tau_ordering_consistency_across_models: 0.67
      feature_group_pairwise_auc:
        pythia_vocab_1v2: 0.641
        pythia_surprisal_1v2: 0.608
        pythia_tail_1v2: 0.622
        olmo_vocab_1v2: 0.625
        olmo_surprisal_1v2: 0.612
        olmo_tail_1v2: 0.598
    result_rationale: >
      Vocabulary diversity（TTR, hapax ratio, entropy-based measures）对递归生成最敏感：
      每一代 LM 生成都倾向于 mode collapse 到高频词汇，vocabulary richness 在 gen-1→gen-2 
      即显著下降。这是因为 LM 的 softmax 分布本质上是对 training distribution 的平滑近似，
      递归采样会累积放大这种平滑效应（"rich get richer" for frequent tokens）。
      Surprisal dynamics（perplexity variance, burstiness）和 tail-thinning（rare token frequency）
      饱和较慢，因为这些特征依赖于高阶统计量，需要更多代际压缩才会坍缩。
      但 ordering 不完全一致：Pythia 上 tail-thinning 先于 surprisal 饱和，OLMo 上反过来。
      这导致跨模型 Kendall tau 为 0.67——有趋势但非严格一致。原因是不同架构的 attention pattern 
      和 vocabulary size 差异导致 rare token 的衰减速率不同。Pythia 的 50K vocabulary 中
      rare tokens 衰减更快（tail-thinning 先饱和），而 OLMo 的训练数据特征使 surprisal 
      burstiness 先丧失。
    tables:
      - caption: "Table: Feature group saturation depth and pairwise AUC (1v2) by model"
        rows:
          - ["Feature Group", "Pythia AUC 1v2", "Pythia Sat. Depth", "OLMo AUC 1v2", "OLMo Sat. Depth"]
          - ["Vocabulary Diversity", "0.641", "1.8", "0.625", "1.6"]
          - ["Surprisal Dynamics", "0.608", "2.3", "0.612", "2.1"]
          - ["Tail Thinning", "0.622", "2.0", "0.598", "2.5"]
      - caption: "Table: Degradation ordering consistency (Kendall tau)"
        rows:
          - ["Model Pair", "Kendall tau", "p-value"]
          - ["Pythia vs OLMo", "0.67", "0.08"]
          - ["Pythia vs Qwen (MVP)", "0.67", "0.08"]
          - ["OLMo vs Qwen (MVP)", "1.00", "0.02"]
    figures_description:
      - "Degradation ordering heatmap: 3 models × 3 feature groups，颜色编码饱和深度，vocabulary diversity 行整体最暗（最早饱和）"
      - "Feature-group-specific AUC decay curves：每个 feature group 一条线，展示 vocabulary diversity 最早触及 noise floor"
    analysis: >
      Vocabulary diversity 的优先饱和跨模型大致一致（3/3 模型中最先饱和），支持 C2 的 "tendency" 
      表述。但 surprisal 和 tail-thinning 的顺序不稳定（tau 0.67），应避免声称严格 ordering。
      论文中建议表述："vocabulary diversity consistently degrades earliest, while the relative 
      ordering of surprisal and tail features is model-dependent"。

  - name: "Downstream filtering evaluation"
    plan_id: "exp-006"
    description: "no-filter / binary / graduated / surprisal-based 四种过滤策略，continued pretraining + lm-eval-harness，3 seeds"
    expected_results:
      mmlu_no_filter: 25.8
      mmlu_binary: 26.4
      mmlu_graduated: 27.2
      mmlu_surprisal: 26.9
      mmlu_graduated_vs_binary_delta_pp: 0.8
      mmlu_std_across_seeds: 0.4
      hellaswag_no_filter: 42.1
      hellaswag_binary: 43.0
      hellaswag_graduated: 43.7
      hellaswag_surprisal: 43.4
      hellaswag_graduated_vs_binary_delta_pp: 0.7
      hellaswag_std_across_seeds: 0.5
    result_rationale: >
      四种策略形成清晰的 hierarchy：no-filter < binary < surprisal ≈ graduated。
      Binary filtering 移除所有 gen-1+ 文本，改善约 0.6pp（MMLU）/ 0.9pp（HellaSwag）——
      这证明合成文本确实有害。Graduated filtering 进一步改善 0.8pp / 0.7pp：机制是 graduated 
      在 binary decision boundary 附近提供更 calibrated 的置信度。具体来说，binary classifier 
      对 gen-1 文本（质量尚可）和 gen-3 文本（质量差）给出相同的 "synthetic" 标签，而 graduated 
      classifier 将 gen-1 标记为 "shallow synthetic"（允许部分保留），gen-3 标记为 "deep synthetic"
      （强力过滤）。这种 calibration 在 training mixture 中保留了更多有用的 gen-1 数据。
      但 effect size 仅 0.5-1.5pp 且 seed variance（std ~0.4-0.5pp）使得 confidence interval 
      可能重叠。这是 median tier 的关键特征：gain 是 real but modest，statistical significance 
      可能需要更多 seeds 才能确认。Surprisal-based filtering（直接用 perplexity 做 quality gate）
      性能介于 binary 和 graduated 之间——它隐式捕获了部分 depth 信息但不如显式 depth 估计精确。
    tables:
      - caption: "Table: Downstream evaluation (MMLU / HellaSwag accuracy) by filtering strategy"
        rows:
          - ["Strategy", "MMLU (mean±std)", "HellaSwag (mean±std)", "Δ vs Binary (pp)"]
          - ["No filter", "25.8 ± 0.3", "42.1 ± 0.4", "-0.6 / -0.9"]
          - ["Binary", "26.4 ± 0.4", "43.0 ± 0.5", "—"]
          - ["Surprisal-based", "26.9 ± 0.3", "43.4 ± 0.4", "+0.5 / +0.4"]
          - ["Graduated (3-class)", "27.2 ± 0.4", "43.7 ± 0.5", "+0.8 / +0.7"]
    figures_description:
      - "Bar chart with error bars: 4 strategies × 2 benchmarks，error bars 显示 seed variance，graduated 与 binary 的 CI 部分重叠"
      - "Calibration plot: graduated classifier 在 gen-1 区域的 predicted depth vs true depth，展示 calibration 优势"
    analysis: >
      Graduated filtering 的优势 real but modest（~0.8pp MMLU，~0.7pp HellaSwag），且 seed 
      variance 使得 p-value 可能在 0.05-0.10。论文中应强调 calibration 优势而非 raw gap：
      "graduated filtering provides better-calibrated quality estimates near the decision 
      boundary, where binary filtering makes its most consequential errors"。
      同时，no-filter → binary 的 gap 本身也不大（~0.6-0.9pp），因为 C4 基础数据质量已较高。

  - name: "K* sensitivity to AUC threshold"
    plan_id: "exp-007"
    description: "在 0.55/0.60/0.65/0.70 四个阈值下计算 K*"
    expected_results:
      threshold_055:
        k_star_pythia: 3
        k_star_olmo: 2
        k_star_qwen_baseline: 2
        k_star_qwen_T12: 3
      threshold_060:
        k_star_pythia: 2
        k_star_olmo: 2
        k_star_qwen_baseline: 2
        k_star_qwen_T12: 2
      threshold_065:
        k_star_pythia: 2
        k_star_olmo: 2
        k_star_qwen_baseline: 2
        k_star_qwen_T12: 2
      threshold_070:
        k_star_pythia: 1
        k_star_olmo: 1
        k_star_qwen_baseline: 2
        k_star_qwen_T12: 1
    result_rationale: >
      K* 定义为最大深度 k 使得 pairwise AUC(k vs k+1) > threshold。阈值选择影响 K* 的绝对值，
      但关键发现是 K* 的跨模型相对 pattern 对阈值 robust。
      Threshold 0.55（宽松）：部分模型的 gen-2v3 AUC（如 Pythia 0.576）仍 > 0.55，K* 升到 3。
      但这个阈值过于宽松——0.55 的 AUC 接近 chance，实际辨别意义不大。
      Threshold 0.60（默认）：所有 1.5B 模型 K*=2，这是论文采用的 operating point。
      Threshold 0.65（偏严）：所有模型仍然 K*=2，因为 gen-1v2 AUC（0.65-0.72）刚好 above 0.65。
      Threshold 0.70（过严）：大部分模型 K* 降到 1，因为 gen-1v2 AUC 多在 0.65-0.70 区间，
      低于 0.70 阈值。仅 Qwen baseline（AUC 1v2 = 0.696）勉强接近。
      核心 insight：在 0.55-0.65 的合理阈值范围内，K*=2 对 1.5B 模型高度稳定。
    tables:
      - caption: "Table: K* stability across AUC thresholds"
        rows:
          - ["Threshold", "Pythia", "OLMo", "Qwen (baseline)", "Qwen (T=1.2)"]
          - ["0.55", "3", "2", "2", "3"]
          - ["0.60", "2", "2", "2", "2"]
          - ["0.65", "2", "2", "2", "2"]
          - ["0.70", "1", "1", "2", "1"]
    figures_description:
      - "Heatmap: threshold (y) × model (x)，色块表示 K* 值。0.60-0.65 区间形成稳定的黄色（K*=2）带"
    analysis: >
      K*=2 在 0.60-0.65 的 threshold 范围内完全稳定。低于 0.55 或高于 0.70 时 K* 变化，
      但这些阈值分别对应 "too lenient"（near chance）和 "too strict"（过滤掉有意义的信号）。
      论文应展示此 robustness check 以预防审稿人质疑 threshold 选择的任意性。

  - name: "Retrain-chain ecological validity"
    plan_id: "exp-008"
    description: "Pythia-1.4B LoRA retrain-chain, depth 0-4"
    expected_results:
      pairwise_auc_0v1: 0.988
      pairwise_auc_1v2: 0.635
      pairwise_auc_2v3: 0.572
      pairwise_auc_3v4: 0.541
      k_star: 2
      jsd_0v1: 0.198
      jsd_1v2: 0.011
      feature_distribution_shift_vs_prompt_chain:
        vocabulary_diversity_ks_test_p: 0.03
        surprisal_dynamics_ks_test_p: 0.12
        tail_thinning_ks_test_p: 0.07
    result_rationale: >
      Retrain-chain（LoRA 微调后用微调模型生成下一代）比 prompt-chain 更接近真实世界的 
      "model collapse" 场景。但其信息损失模式有关键差异：每一代不仅改变输出分布，还改变
      模型参数本身。LoRA rank=16 限制了参数更新的自由度，使得每代的变化幅度比 full retrain 小。
      K*=2 与 prompt-chain 一致，但 AUC 值整体低于 prompt-chain 的 Pythia（1v2: 0.635 vs 0.672）。
      这是因为 retrain-chain 中 gen-1 的文本由微调后模型生成——微调模型比原模型更 "collapsed"，
      gen-1 起点就更接近 gen-2+。K* 没有 differ by 1（仍为 2 而非 1 或 3），因为 LoRA 的
      limited capacity 恰好使衰减速率与 prompt-chain 类似。
      特征分布有显著但不巨大的差异（vocabulary diversity 的 KS test p=0.03），反映 retrain 
      导致的 vocabulary 坍缩更系统性（非随机采样造成而是参数更新造成）。
    tables:
      - caption: "Table: Prompt-chain vs Retrain-chain comparison (Pythia-1.4B)"
        rows:
          - ["Pair", "Prompt AUC", "Retrain AUC", "Δ AUC"]
          - ["0 vs 1", "0.993", "0.988", "-0.005"]
          - ["1 vs 2", "0.672", "0.635", "-0.037"]
          - ["2 vs 3", "0.576", "0.572", "-0.004"]
          - ["3 vs 4", "0.538", "0.541", "+0.003"]
    figures_description:
      - "Prompt-chain vs Retrain-chain 的 JSD decay 对比：形状相似但 retrain 曲线整体偏低"
      - "Feature distribution violin plots: prompt vs retrain 的 vocabulary diversity 分布，retrain 的分布更紧（variance 更低）"
    analysis: >
      Retrain-chain 验证了 K*=2 的 qualitative robustness：即使换用更 ecologically valid 的
      递归方式，饱和边界不变。Quantitative 差异（AUC 偏低 0.03-0.04）可讨论但不影响核心 claim。
      论文中此实验作为 ecological validity check 放在 Section 5 或 Appendix。

  - name: "Contamination dose-response"
    plan_id: "exp-009"
    description: "10%/30%/50% synthetic injection 比例下 graduated vs binary filtering"
    expected_results:
      injection_10pct:
        mmlu_no_filter: 26.1
        mmlu_binary: 26.3
        mmlu_graduated: 26.5
        delta_grad_vs_binary: 0.2
      injection_30pct:
        mmlu_no_filter: 25.8
        mmlu_binary: 26.4
        mmlu_graduated: 27.2
        delta_grad_vs_binary: 0.8
      injection_50pct:
        mmlu_no_filter: 25.2
        mmlu_binary: 26.2
        mmlu_graduated: 27.3
        delta_grad_vs_binary: 1.1
      hellaswag_delta_pattern: "similar trend, slightly smaller magnitudes"
    result_rationale: >
      Contamination dose 调控 graduated filtering 的 value proposition。
      10% injection：基础数据集的 90% 仍是 clean human text，contamination 的影响有限。
      Binary filtering 已经足够（移除 10% synthetic），graduated 的额外收益微乎其微（0.2pp），
      因为 gen-1 文本在整体 training mix 中占比太小，其 quality calibration 的价值被稀释。
      30% injection：接近 exp-006 的设定。Graduated vs binary 的 delta（0.8pp）与 exp-006 
      一致。此时 gen-1 文本在 30% synthetic 中占约 40%（~12% of total），足以使 calibration 
      差异产生可测量影响。
      50% injection：污染严重。No-filter 性能显著下降（25.2）。Binary filtering 恢复大部分性能
      但 graduated 的优势进一步增大（1.1pp），因为 50% synthetic 中包含大量 gen-1 文本，
      graduated filter 选择性保留其中质量较好的部分，而 binary filter 将其全部丢弃导致
      training data 量不足。这是 graduated filtering 最有价值的场景：当 contamination 严重到
      不得不在 "丢弃过多" 和 "保留过差" 之间权衡时，depth calibration 提供了更精细的选择。
    tables:
      - caption: "Table: Dose-response — Graduated vs Binary filtering delta (MMLU pp)"
        rows:
          - ["Injection Rate", "No Filter", "Binary", "Graduated", "Δ Grad-Binary"]
          - ["10%", "26.1", "26.3", "26.5", "+0.2"]
          - ["30%", "25.8", "26.4", "27.2", "+0.8"]
          - ["50%", "25.2", "26.2", "27.3", "+1.1"]
    figures_description:
      - "Line plot: injection rate (x) vs graduated-binary delta (y)，单调递增，表明 graduated filtering 在高污染场景更有价值"
    analysis: >
      Dose-response 揭示了 graduated filtering 的 practical sweet spot：当 contamination ≥30% 时，
      graduated vs binary 的差异变得 meaningful（≥0.8pp）。论文中用此结果论证 "as web data 
      contamination increases, the value of depth-aware curation grows super-linearly"。

  - name: "Ordinal vs multinomial vs regression baseline"
    plan_id: "exp-010"
    description: "CORAL ordinal vs standard multiclass vs ordinal regression 对比"
    expected_results:
      coral_ordinal:
        accuracy: 0.42
        mae: 1.02
        adjacent_accuracy: 0.74
      multinomial:
        accuracy: 0.40
        mae: 1.18
        adjacent_accuracy: 0.68
      ordinal_regression:
        accuracy: 0.41
        mae: 1.05
        adjacent_accuracy: 0.72
    result_rationale: >
      Depth estimation 天然是 ordinal task（gen-0 < gen-1 < gen-2 ...），CORAL 通过将 ordinal 
      regression 编码为一系列 binary threshold 任务来利用这种结构。
      CORAL vs multinomial：accuracy 差异不大（0.42 vs 0.40），因为 K*=2 意味着有效类别只有 
      3 个（gen-0/gen-1/gen-2+），multinomial 在 3 类上也能工作。但 MAE 差异显著（1.02 vs 1.18），
      因为 multinomial 对 "off-by-2" 错误没有 penalty 结构——它可能将 gen-0 错分为 gen-3，
      而 CORAL 的 threshold structure 使这种远距离错误更少。Adjacent accuracy（预测值与真实值
      差距 ≤1 的比例）最能体现 ordinal structure 的优势：0.74 vs 0.68。
      Ordinal regression（传统 cumulative logit model）性能介于两者之间：它有 ordinal structure 
      但缺乏 CORAL 的 neural network flexibility。
    tables:
      - caption: "Table: Ordinal structure comparison"
        rows:
          - ["Method", "Accuracy", "MAE", "Adjacent Acc"]
          - ["CORAL (ordinal)", "0.42", "1.02", "0.74"]
          - ["Multinomial", "0.40", "1.18", "0.68"]
          - ["Ordinal Regression", "0.41", "1.05", "0.72"]
    figures_description:
      - "Confusion matrices (3 panels): CORAL/multinomial/regression，CORAL 的 off-diagonal mass 更集中在 adjacent cells"
    analysis: >
      CORAL 的优势主要在 MAE 和 adjacent accuracy 而非 raw accuracy，这与 ordinal task 的 
      evaluation semantics 一致。论文中用此结果证明 "depth estimation benefits from ordinal 
      modeling, not because it improves top-1 accuracy, but because it produces more 
      calibrated errors"。

  - name: "LLM zero-shot depth estimation"
    plan_id: "exp-011"
    description: "GPT-4o / Claude 3.5 zero-shot depth 判断"
    expected_results:
      gpt4o_accuracy_6class: 0.22
      gpt4o_binary_auc: 0.88
      gpt4o_depth_mae: 1.85
      gpt4o_gen0v1_accuracy: 0.81
      gpt4o_gen1v2_accuracy: 0.39
      gpt4o_gen2v3_accuracy: 0.28
      claude35_accuracy_6class: 0.24
      claude35_binary_auc: 0.91
      claude35_depth_mae: 1.72
      claude35_gen0v1_accuracy: 0.84
      claude35_gen1v2_accuracy: 0.42
      claude35_gen2v3_accuracy: 0.30
    result_rationale: >
      大型 LLM 在 binary detection（human vs synthetic）上表现尚可（AUC ~0.88-0.91），因为
      gen-0 vs gen-1 的文本质量差异足够大，表面线索（如过度流畅、缺乏 typos、topic drift 
      模式）即可捕获。但 depth estimation 失败：gen-1 vs gen-2 的细微差异（vocabulary richness 
      略降、surprisal variance 略减）在 zero-shot 设定下不可区分。LLM 倾向于将所有 synthetic 
      文本标记为 gen-1 或 gen-2（anchoring bias），导致 6-class accuracy 仅 22-24%（接近 
      6 分之一的 chance level 16.7%，但高于 chance 因为 gen-0 的高 recall 拉升了平均）。
      MAE 高达 1.7-1.9，说明 LLM 的预测与真实 depth 相关性很弱。
      这个 baseline 的战略价值在于证明 "depth estimation is a non-trivial task requiring 
      specialized methods"——即使是 SOTA LLM 也无法通过 commonsense reasoning 解决。
    tables:
      - caption: "Table: LLM zero-shot depth estimation performance"
        rows:
          - ["Model", "6-class Acc", "Binary AUC", "MAE", "Gen0v1 Acc", "Gen1v2 Acc"]
          - ["GPT-4o", "0.22", "0.88", "1.85", "0.81", "0.39"]
          - ["Claude 3.5 Sonnet", "0.24", "0.91", "1.72", "0.84", "0.42"]
          - ["Our method (CORAL)", "0.42", "0.99+", "1.02", "0.99+", "0.68"]
    figures_description:
      - "LLM prediction distribution vs true depth: histogram 显示 LLM 将大部分 gen-2+ 文本错误标记为 gen-1"
    analysis: >
      LLM zero-shot 在 depth estimation 上失败，验证了 specialized method 的必要性。
      同时 LLM 在 binary detection 上的不错表现说明 gen-0 vs gen-1 的信号是 "obvious"——
      这与 K*=2 的 narrative 一致（gen-0/gen-1 boundary 是清晰的，gen-1+/gen-2+ boundary 
      才需要精细方法）。

  - name: "Binary detector confidence as depth proxy"
    plan_id: "exp-012"
    description: "DivEye/Binoculars score 的 Spearman correlation with true depth"
    expected_results:
      diveye_spearman_with_depth: -0.31
      diveye_spearman_p_value: 0.001
      binoculars_spearman_with_depth: -0.28
      binoculars_spearman_p_value: 0.003
      diveye_binary_auc_0v1plus: 0.93
      binoculars_binary_auc_0v1plus: 0.95
      diveye_auc_1v2: 0.57
      binoculars_auc_1v2: 0.55
    result_rationale: >
      Binary detectors（DivEye, Binoculars）的 confidence score 与 true depth 有弱负相关
      （Spearman ~-0.3）：更深代际的文本确实获得更低的 "human-likeness" score，但相关性很弱。
      这是因为 binary detectors 的 decision function 是为 binary separation 优化的——它们
      在 gen-0 vs gen-1+ 的 boundary 处 calibrated，但对 gen-1 vs gen-2 vs gen-3 的梯度
      几乎不敏感。Binary AUC 很高（0.93-0.95），但 pairwise AUC 1v2 仅 0.55-0.57（near chance），
      说明 binary confidence ≠ depth。
      这个结果的 narrative 价值：现有工具无法做 depth estimation，不是因为技术问题，
      而是因为它们根本不是为此设计的。Depth estimation 是一个 genuinely new task。
    tables:
      - caption: "Table: Binary detector scores as depth proxies"
        rows:
          - ["Detector", "Binary AUC (0v1+)", "Spearman ρ (depth)", "AUC 1v2"]
          - ["DivEye", "0.93", "-0.31", "0.57"]
          - ["Binoculars", "0.95", "-0.28", "0.55"]
          - ["Our features (15D)", "0.99+", "-0.82", "0.70"]
    figures_description:
      - "Scatter plot: DivEye score (x) vs true depth (y)，点云高度重叠，仅 gen-0 区域有清晰分离"
    analysis: >
      Binary confidence 作为 depth proxy 基本失败（ρ ~-0.3），而我们的 15D 手工特征的 ρ=-0.82 
      显著更好。这构成对 "why not just use existing detectors?" 的有力回应。

  - name: "Cross-model transfer"
    plan_id: "exp-013"
    description: "Model A 训练 → Model B 测试的 transfer accuracy"
    expected_results:
      transfer_matrix_binary_auc:
        pythia_to_olmo: 0.91
        pythia_to_qwen: 0.89
        olmo_to_pythia: 0.90
        olmo_to_qwen: 0.88
        qwen_to_pythia: 0.92
        qwen_to_olmo: 0.90
      transfer_matrix_ordinal_accuracy:
        pythia_to_olmo: 0.26
        pythia_to_qwen: 0.24
        olmo_to_pythia: 0.25
        olmo_to_qwen: 0.23
        qwen_to_pythia: 0.28
        qwen_to_olmo: 0.26
      binary_transfer_retention_pct: 92
      ordinal_transfer_retention_pct: 58
    result_rationale: >
      Binary transfer（gen-0 vs gen-1+）效果好（AUC 0.88-0.92，retention ~92%）：gen-0 vs gen-1 
      的信号是 universal 的——所有 LLM 生成的文本都共享某些与 human text 不同的统计特征
      （过度平滑的 surprisal、降低的 vocabulary diversity）。这些特征跨模型 transferable。
      Ordinal transfer 大幅退化（accuracy 0.23-0.28，retention ~58%）：gen-1 vs gen-2 vs gen-3+ 
      的细微差异是 model-specific 的。不同模型的 lossy channel 特征不同——Pythia 的 mode collapse 
      模式（哪些 token 频率增加）与 OLMo 的不同，导致 gen-2 的 feature profile 不可直接迁移。
      这个结果限制了 graduated filtering 的 practical applicability（需要 model-specific 训练），
      但同时证明了 depth signal 的存在性（如果 ordinal signal 不存在，transfer 应该完全是 chance）。
    tables:
      - caption: "Table: Cross-model transfer matrix — Binary AUC"
        rows:
          - ["Train\\Test", "Pythia", "OLMo", "Qwen"]
          - ["Pythia", "0.993 (in-dist)", "0.91", "0.89"]
          - ["OLMo", "0.90", "0.991 (in-dist)", "0.88"]
          - ["Qwen", "0.92", "0.90", "0.996 (in-dist)"]
      - caption: "Table: Cross-model transfer matrix — Ordinal Accuracy"
        rows:
          - ["Train\\Test", "Pythia", "OLMo", "Qwen"]
          - ["Pythia", "0.40 (in-dist)", "0.26", "0.24"]
          - ["OLMo", "0.25", "0.39 (in-dist)", "0.23"]
          - ["Qwen", "0.28", "0.26", "0.42 (in-dist)"]
    figures_description:
      - "Heatmap pair: binary transfer (warm, 0.88-0.92) vs ordinal transfer (cool, 0.23-0.28)，对比鲜明"
    analysis: >
      Binary transferability 高 + ordinal transferability 低 的组合是重要的 nuanced finding。
      论文中此结果既支持 C1（gen-0/gen-1 boundary 是 universal）又限定 C3 的 practical scope
      （graduated filtering 需要 in-distribution training）。Retention ~58% 说明 ordinal signal 
      有跨模型共性但不够强，与 degradation ordering 的 partial consistency（tau 0.5-0.8）一致。

  - name: "Naturalistic validation on Common Crawl"
    plan_id: "exp-014"
    description: "Common Crawl 2025/2026 snapshot 的 depth 预测 + 外部指标 correlation"
    expected_results:
      predicted_depth_distribution:
        depth_0_pct: 72
        depth_1_pct: 18
        depth_2plus_pct: 10
      correlation_with_alignscore: 0.34
      correlation_with_vocab_richness: 0.41
      high_depth_sample_qualitative_agreement: "70% of predicted depth-2+ samples show visible quality degradation upon manual inspection"
    result_rationale: >
      Common Crawl 2025-2026 中合成文本比例正在增长但仍以浅代际为主。我们的 classifier 
      预测 ~28% 为 synthetic（depth ≥1），其中 ~18% 为 gen-1、~10% 为 gen-2+。这与其他
      估计（如 originality.ai 的 ~25-30% synthetic content in recent crawls）大致一致。
      与 AlignScore 的 correlation 较弱（0.34）——这是预期的，因为 AlignScore 衡量 factual 
      consistency 而非 generational depth，两者正交性高。与 vocabulary richness 的 correlation 
      更好（0.41），因为 vocabulary diversity 是我们特征空间的核心成分且在递归生成中持续衰减。
      但 correlation 不高的原因是：wild data 中的 synthetic text 来源多样（不同模型、不同 
      prompt、不同 domain），我们的 classifier 在 controlled experiment 上训练，domain shift 
      导致 calibration 偏移。手工检查显示 70% 的高 depth 预测有明显质量退化（重复、
      topic drift、vocabulary 贫乏），验证 directional correctness。
    tables:
      - caption: "Table: Common Crawl depth prediction summary"
        rows:
          - ["Predicted Depth", "% of Sample", "Avg AlignScore", "Avg Vocab Richness"]
          - ["0 (human)", "72%", "0.78", "0.65"]
          - ["1 (gen-1)", "18%", "0.71", "0.58"]
          - ["2+ (gen-2+)", "10%", "0.64", "0.49"]
    figures_description:
      - "Stacked bar: Common Crawl sample 的 predicted depth 分布"
      - "Scatter with marginal densities: predicted depth vs vocabulary richness，弱但显著的负相关"
    analysis: >
      Naturalistic validation 提供 directional 而非 definitive 的支持。Correlation 不高是
      expected（domain shift + no ground truth depth labels in the wild）。论文中放入 Appendix 
      作为 ecological validity evidence，不作为主要 claim 的支撑。

  - name: "Learned representation baseline"
    plan_id: "exp-015"
    description: "Frozen Qwen2.5-1.5B embeddings + MLP vs 15D hand-crafted features"
    expected_results:
      learned_accuracy: 0.44
      learned_mae: 0.95
      learned_binary_auc: 0.997
      handcrafted_accuracy: 0.42
      handcrafted_mae: 1.02
      handcrafted_binary_auc: 0.996
      learned_feature_dim: 2048
      handcrafted_feature_dim: 15
    result_rationale: >
      Frozen LM embeddings（2048 维）+ 2-layer MLP 的性能略优于 15D 手工特征（accuracy 0.44 
      vs 0.42，MAE 0.95 vs 1.02）。这是预期的：2048 维的 contextual representations 包含
      比 15 个 hand-crafted statistics 更丰富的信息。但差距很小（~2pp accuracy，~0.07 MAE），
      因为 K*=2 限制了 depth estimation 的 ceiling——即使有完美特征，gen-2+ 的类间距也太小
      无法显著提升。Learned representations 的边际优势来自捕获了一些手工特征未覆盖的信号
      （如句法复杂度的微妙下降、discourse coherence 的退化模式），但这些信号贡献有限。
      手工特征的优势在于 interpretability：15D 特征允许 degradation ordering 分析（exp-005），
      而 2048D embeddings 不透明。论文中此对比证明 "hand-crafted features are competitive 
      with learned representations at a fraction of the dimensionality, while enabling 
      interpretable analysis of degradation patterns"。
    tables:
      - caption: "Table: Hand-crafted vs Learned features"
        rows:
          - ["Features", "Dim", "Accuracy", "MAE", "Binary AUC"]
          - ["15D hand-crafted", "15", "0.42", "1.02", "0.996"]
          - ["Frozen embeddings + MLP", "2048", "0.44", "0.95", "0.997"]
    figures_description:
      - "Bar chart: accuracy/MAE 对比，差距极小，hand-crafted 下方标注 interpretability 优势"
    analysis: >
      Learned representations 仅有微弱优势，验证了 hand-crafted features 的合理性。
      论文中此结果回应审稿人 concern #6 ("why not use learned representations")。

  - name: "Base vs Instruct model comparison"
    plan_id: "exp-016"
    description: "Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异"
    expected_results:
      base_k_star: 2
      instruct_k_star: 2
      base_pairwise_auc_1v2: 0.682
      instruct_pairwise_auc_1v2: 0.696
      base_jsd_0v1: 0.243
      instruct_jsd_0v1: 0.267
      base_vocab_diversity_gen1_mean: 0.58
      instruct_vocab_diversity_gen1_mean: 0.54
      feature_distribution_ks_test_p_vocab: 0.01
      feature_distribution_ks_test_p_surprisal: 0.04
    result_rationale: >
      Instruct 模型经过 RLHF/DPO 对齐，其输出比 base 模型更 "polished"——更长、更结构化、
      vocabulary 更受限（避免 toxic/rare tokens）。这导致 Instruct 的 gen-0→gen-1 JSD 更大
      （0.267 vs 0.243）：Instruct 输出与 human text（C4 原始文本）的差异比 base 输出更大，
      因为 RLHF 引入了 "assistant-like" 的文本模式（长句、连接词使用、hedging language）。
      但 K* 不受影响（均为 2），因为 Instruct 和 base 共享相同的 backbone architecture，
      其 lossy channel capacity 由模型规模决定而非对齐方式。
      有趣的是，Instruct 的 vocabulary diversity 在 gen-1 就更低（0.54 vs 0.58），反映 RLHF 
      的 vocabulary constraining 效应——对齐训练本身就是一种 "pre-collapse"。这意味着 Instruct 
      模型的递归链从一个更 collapsed 的起点开始，但饱和速度与 base 相同。
    tables:
      - caption: "Table: Base vs Instruct comparison (Qwen2.5-1.5B)"
        rows:
          - ["Metric", "Base", "Instruct"]
          - ["K*", "2", "2"]
          - ["AUC 0v1", "0.994", "0.996"]
          - ["AUC 1v2", "0.682", "0.696"]
          - ["JSD 0v1", "0.243", "0.267"]
          - ["Vocab Diversity gen-1", "0.58", "0.54"]
    figures_description:
      - "Feature distribution comparison (violin plots): base vs instruct 在 gen-0, gen-1, gen-2 的 vocabulary diversity，Instruct 起点更低但衰减斜率相同"
    analysis: >
      Base vs Instruct 的 K*=2 一致性进一步加强 universality claim。Instruct 的 lower vocabulary 
      diversity baseline 是一个有趣的观察——可以在 discussion 中简短提及 "alignment training 
      itself acts as a mild form of mode collapse"，但不作为主要 claim。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57321d77-20e5-47dd-9ff3-3a02631aafe6",
  "isSidechain": false,
  "requestId": "req_011CayHLj9fBJGg4vGX8S3zG",
  "type": "assistant",
  "uuid": "54957d24-426c-461f-973d-f225e79146d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SvnnwhskhofgRB7maT5DwE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10236,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17385,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10236
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：K*=2 is stable across most conditions with minimal variation, degradation ordering partially holds, graduated filtering shows modest but real gains 核心假设：…",
  "leafUuid": "54957d24-426c-461f-973d-f225e79146d1",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize K* saturation boundary in recursive generation",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：K*=2 is stable across most conditions with minimal variation, degradation ordering partially holds, graduated filtering shows modest but real gains 核心假设：…",
  "leafUuid": "54957d24-426c-461f-973d-f225e79146d1",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize K* saturation boundary in recursive generation",
  "sessionId": "d6bebd24-c6ab-4068-aa92-293da9457dd7"
}
```

---
