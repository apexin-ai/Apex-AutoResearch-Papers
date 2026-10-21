---
name: contrastive-trace-safety-writing
description: LLM safety interpretability 论文叙事结构、图表设计共识与可模仿策略——8 篇深读蒸馏
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 10
  paper_keys: [zou2023representation, zou2023universal, zhou2024alignment, kaya2019shallow, hewitt2019control, zhou2020bert, arditi2024refusal, harmthoughts, safethink, chen2025unfaithful]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 叙事结构

### 故事类型：突破局限型主导（6/8，高）
现有方法看似有效→揭示隐藏缺陷→新视角。Chen 先承认推理模型"更忠实"再揭示仅 25%，先正面再转折避免危言耸听。Hewitt 逐条推翻假设（MLP 好？不行；dropout 有用？没用）。**策略：先建立对手最强论据再拆解。**

### 开篇钩子三模式
1. **许诺-颠覆**（3/8）：Chen "CoT promises safety... but?" / Hewitt "probing achieves high accuracy... but meaningful?" → 适用于隐状态分析领域："hidden states reveal reasoning... but do they match text?"
2. **对立张力**（3/8）：Zhou alignment vs jailbreak / Arditi helpfulness vs harmlessness / SafeThink reasoning gain vs safety loss
3. **人类类比命名**（2/8）：Kaya "overthinking" / PABEE "patience"——命名即贡献

### Intro 4-5 段是主流（5/8）
P1=hook → P2=现有局限 → P3=方法 → P4=发现 → P5=贡献列表。贡献声明：编号列表（3/8）vs 叙事渐进无显式列表（3/8）并存。

## 图表设计共识

### Figure 1 模式
method_overview（3/8：Zhou/Kaya/PABEE）、teaser_result（2/8：Arditi/Chen）、motivation 实例（2/8：HarmThoughts/Hewitt）。设计共识：对比布局 5/8，颜色编码安全状态 3/8。**Figure 1 必须不看正文即传达核心论点。**

### 结果可视化
- **折线图**（6/8）：layer-wise 分析、参数扫描首选
- **分组柱状图**（4/8）：方法间对比。增益突出：仅标本方法数值（SafeThink）、Pareto 前沿（PABEE）、视觉骤降（Arditi 0.9→0.0）
- **热力图**（2/8）：密集 layer×token 可视化（Zhou 逐层 Logit Lens）
- 消融用双面板解耦指标最有效（Hewitt accuracy+selectivity 上下行；Chen 6-panel 网格按 hint type 分）

### 表格编排（6/8，高）
行=methods，by_category 分块（7/8）；bold_best 与无高亮各 3/8；Baseline 3-14 个（中位 ~7）；单次运行为主（5/8）。**full_numbers 绝对主导**（7/8），delta_from_base 未见。Chen 全量化结果用图不用表，仅 1 个 setup 表——图优先叙事的极端例子。

### 图表分工
趋势→图，多方法×多任务→表，定性例子→图。附录（5/8）放逐模型细分和方法论验证。SafeThink 主结果用 bar chart（视觉冲击）+ 同内容 table（数值精度）双出。

## 可模仿技巧

1. **命名即贡献**（3/8，高）：给核心概念起直觉名字（"overthinking"/"patience"/"Weak-to-Strong Explanation"），一词概括工作
2. **渐进揭示**（3/8，中）：每节独立叙事弧层层推进。Zhou 3.1→3.2→4 三阶段发现；Chen 正面→中性→警报；SafeThink 问题→理论→1-3步即够
3. **简洁即论据**（2/8，中）：Arditi 反复强调"rank-1、<$5、无需训练"——方法简单时简单性本身是最强修辞
4. **平衡裁决**（2/8，中）：安全领域先承认进步再揭示不足，比单纯报警更可信（Chen "reasoning models ARE more faithful... but only 25%"）
5. **视觉-数值双出**（2/8，中）：SafeThink/HarmThoughts 主结果同时给 bar chart + table，图给直觉、表给精度
