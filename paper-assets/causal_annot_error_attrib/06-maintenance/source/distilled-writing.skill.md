---
name: causal-annot-error-attrib-writing
description: 领域蒸馏——LLM标注误差×因果推断论文的叙事策略、图表设计、展示共识（8篇深度精读归纳）
---

## 叙事类型分布

- **突破局限型**：5/8篇主流。Pattern: 工具被广泛使用→揭示被忽视的系统性问题→提出校正。置信度：高。（Gligoric 2025, Baumann 2025, Kim & Garg 2025, TeBlunthuis 2024, Lee 2024）
- **统一框架型**：2/8篇，适用于方法论/形式化贡献。（Hernán & Cole 2009, Messing 2026）
- **跨界迁移型**：1/8篇，开创性工作连接NLP与causal inference。（Wood-Doughty 2018）

## 开篇策略（可直接模仿）

**最有效: Adoption-validity gap**（3/8篇，置信度：高）
- 先承认工具被广泛采用→揭示"几乎无人验证下游影响"
- TeBlunthuis 2024: "85% report metrics but only 1 corrects"
- Baumann 2025: 先"transforming research"再"fundamental threat to scientific validity"

**Counterintuitive result hook**（Messing 2026）
- 更多数据让naive CI更差（45%→12%），打破"more data helps"直觉

**Title-as-question**（Gligoric 2025, TeBlunthuis 2024）
- "Can Unconfident Annotations Be Used for Confident Conclusions?" 标题即hook

## 张力来源（按频率）

1. **采用度vs验证度鸿沟**（3/8）："everyone uses it, nobody validates"。置信度：高。
2. **假设违反**（2/8）：证明标准假设（独立性/non-differential）不成立。置信度：中。
3. **理论-实践差距**（2/8）：校正方法理论正确但实践不稳定。置信度：中。

## Figure 1设计模式

- **DAG问题示意**：3/8篇。DAG是这个子领域的视觉语言。黑白minimal，starred-node notation。置信度：高。（Hernán 2009, Wood-Doughty 2018, Lee 2024）
- **方法流程图**：2/8篇。左到右pipeline，圆角矩形+图标。（Gligoric 2025, Baumann 2025）
- **Teaser result**：2/8篇。反直觉结果立刻抓住读者。（Kim & Garg 2025 heatmap, Messing 2026 coverage curve）
- **设计共识**：颜色2-3色最小化、面板并排对比、observed vs unobserved清晰标注

## 结果可视化共识

- **Line plots（convergence/scaling）**：4/8篇主结果图。Log-log尺度标准。适合展示趋势和收敛。置信度：高。
- **Multi-panel grid**：3/8篇。极信息密集。Gligoric 2025用18-panel，Baumann 2025用7×5 small-multiples。置信度：高。
- **Quantile dot plot**：1/8篇。同时展示bias（中心偏移）和variance（散布）。（TeBlunthuis 2024）
- **Gain突出手法**：dashed reference line（coverage=0.95或diagonal）+颜色对比，4/8篇使用。

## 表格设计共识

- **无表论文**：2/8（理论/框架论文可全用图）。Wood-Doughty 2018, Hernán 2009。
- **Checkmark grid（方法×场景）**：TeBlunthuis 2024 Table 1——一目了然展示适用性。极有效。
- **Baseline 3-8个，按family分组**（by_category最常见4/6）
- **统计报告**：Monte Carlo / bootstrap CI为主（4/8）
- **附录标配**：proofs（3/8）、per-task breakdowns（2/8）、prompt细节（2/8）、robustness（4/8）

## 图表分工

- **结果用图、方法细节用表**：3/8篇。Messing 2026全部结果以figure呈现，tables仅在appendix。
- **结果用表、方法概览用图**：2/8篇。Lee 2024所有定量结果在tables。
- **Narrative flow共识**：motivation→method→result→ablation（4/8）或problem→framework→evidence→application（2/8）

## 可直接模仿的叙事技巧

1. **Catastrophic failure前置**：用极端失败（coverage=0%、符号翻转、31-50%错误率）让校正必要性不言自明。3/8篇。置信度：高。（Gligoric 2025, TeBlunthuis 2024, Baumann 2025）
2. **Running example贯穿全文**：DAG通过具体案例（smoking→cancer, statin→liver）可理解。2/8篇。置信度：中。（Wood-Doughty 2018, Hernán 2009）
3. **Negative result诚实呈现**：方法论领域，负面结果本身就是贡献。2/8篇。置信度：中。（Wood-Doughty 2018矩阵不稳定, Baumann 2025校正权衡）
4. **Summary of findings前置**：methods前用bold声明列出结论。1/8但效果显著。（Baumann 2025）
5. **Dense multi-panel替代多图**：单张18-panel图承载全部结果。2/8篇。（Gligoric 2025, Kim & Garg 2025）
