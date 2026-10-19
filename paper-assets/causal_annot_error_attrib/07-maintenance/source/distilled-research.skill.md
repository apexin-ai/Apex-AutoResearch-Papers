---
name: causal-annot-error-attrib-research
description: 领域蒸馏——LLM标注误差在因果推断中的传播与校正：基线、指标、方法论共识与研究空白（12篇论文归纳）
---

## 基线共识

- **Naive/unadjusted**（分类器输出直接当真值）：5/8篇必设基线。置信度：高。（Wood-Doughty 2018, TeBlunthuis 2024, Baumann 2025）
- **Human-only**：3/8篇。LLM-human比较场景必设。（Gligoric 2025, Baumann 2025）
- **Matrix adjustment / MLA**：3/8篇作为校正方法。数值不稳定是核心挑战。置信度：高。（Wood-Doughty 2018, TeBlunthuis 2024, Lee 2024）
- **PPI / DSL / CDI**：2/8篇。上升趋势，prediction-powered inference家族。（Gligoric 2025, Baumann 2025）
- **MC-SIMEX**：2/8篇。需已知误差矩阵。（Lee & Wood-Doughty 2024）

## 指标共识

- **CI coverage**：4/8篇。校正方法必须证明coverage接近nominal。置信度：高。（Messing 2026, Gligoric 2025, TeBlunthuis 2024）
- **偏差度量**（squared distance / RMSE / OR bias）：4/8篇。置信度：高。（Wood-Doughty 2018, Lee 2024）
- **Type I/II/S/M错误率**：Baumann 2025独创完整分类。校正面临Type I↓ vs Type II↑根本权衡（DSL/CDI降Type I但增Type II达60pp）。置信度：中。
- **分类器F1/accuracy**：4/8篇报告但共识是**高F1不保证下游正确**——F1>0.93仍有>50%错误风险（Baumann 2025），92% accuracy仍导致定性错误（TeBlunthuis 2024）。置信度：高。

## 数据集选择

- **CSS标注任务**（politeness, stance, hate speech）：3/8篇。Baumann 2025覆盖37任务为最大规模。
- **合成+真实双重验证**：3/8篇。置信度：高。（Wood-Doughty 2018, TeBlunthuis 2024, Messing 2026）
- **LLM评估基准**（MMLU, Helm, Arena）：2/8篇。（Kim & Garg 2025, Messing 2026）
- **临床NLP（MIMIC）**：唯一有真实causal estimand的实证。（Lee 2024）

## 方法论趋势

- **上升**：PPI-based校正、G-theory方差分解、LLM误差相关性分析、大规模风险量化（13M+标注）
- **稳定**：Matrix adjustment / MLA（Hernán 2009 → Wood-Doughty 2018 → TeBlunthuis 2024 → Lee 2024）
- **消退**：Missing data formulation（Wood-Doughty 2018提出后未被采纳）

## 竞品claim汇总

**Foundation组**（7篇）：DAG starred-node notation是基石（Hernán 2009）；matrix adjustment理论正确但不稳定（Wood-Doughty 2018）；MLA跨4种DAG场景一致有效（TeBlunthuis 2024）；可推广到categorical confounders（Lee 2024）；confidence-guided sampling+PPI保证统计有效性（Gligoric 2025）；polytomous misclassification可向任意方向偏倚（Brenner 1993, Veierød 2001）

**Complementary组**（5篇）：LLM误差高度相关（60% agreement when both err），违反独立性假设（Kim & Garg 2025）；31-50%假设因LLM标注得出错误结论（Baumann 2025）；item-judge交互贡献44%方差但不含因果识别（Messing 2026）；differential error有closed-form sensitivity公式（VanderWeele & Li 2019）；E-value量化未观测混杂敏感性（VanderWeele & Ding 2017）

## 共同局限（按出现频率）

1. **仅binary分类**（4/12）——categorical扩展不足（Brenner 1993, Veierød 2001部分补充）
2. **假设human无误**（3/8）——annotator disagreement普遍存在
3. **Non-differential error假设**（3/12）——differential更现实但更难处理
4. **小验证集致矩阵逆不稳定**（2/8）——误差矩阵估计方差大
5. **不含因果估计**（2/8明确标注）——Gligoric 2025和Messing 2026均排除causal inference

## 研究空白

- **因果识别+标注误差校正统一框架**：12/12篇均未覆盖。项目核心定位。置信度：高。
- **误差相关性纳入校正**：Kim & Garg 2025证明误差相关，0篇将此纳入校正。置信度：中。
- **多变量同时含噪**：0/12篇处理多个含误差变量。置信度：中。
- **Differential error实证校正**：Hernán 2009框架 + VanderWeele 2019公式，0篇实证。置信度：中。
- **因果场景下标注预算分配**：Gligoric 2025解决统计推断，0篇针对因果估计。置信度：中。
