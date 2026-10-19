# Distilled Writing — Certifiable Manipulation Resistance for Multi-Judge LLM Eval

> 8 篇深度精读论文的叙事结构、图表设计、论证策略归纳。

## 1. 主流故事类型："化繁为简型" (3/8)
Yang2026, Feng2026, Turkmen2026: 复杂现象→单一信息论量→简洁解释。Turkmen 用 4 递进定理（独立→分解→饱和→算法）。**中置信度**。
→ 找一个统一量 (K_eff) 归纳不同现象。用递进定理链构建理论。

## 2. Intro: 5 段 + 末段贡献列表 (7/8)
**高置信度**。模板: (1) 领域背景, (2) 现有局限, (3) 核心 insight, (4) 结果预览, (5) 编号贡献。贡献 3 个最常见 (5/8)，措辞 "framework + theory + empirical"。

## 3. Hook: 悖论式最强
分布: 悖论/反直觉 3/8, 问题式 2/8, 能力缺口 1/8, 统一 1/8。**中置信度**。
Turkmen "Don't Always Pick the Highest-Performing Model" 挑战直觉; Robertson "Instead of 'which is better?' ask 'do they share information?'" 概念替换。
→ 可用 "Adding more judges doesn't make evaluation safer"。

## 4. 张力: 假设失效 + 数字冲击
**6/8 篇**。**高置信度**。揭示被忽视假设→展示失效证据。Kim2025 "60% agreement when both err (vs 33% baseline)" 一个数字摧毁多样性假设。
→ 找同样冲击力的反直觉数字。

## 5. Figure 1: 无主导模式，按论文类型选
method_overview 2/8, motivation 2/8, teaser_result 2/8, problem_illustration 2/8。**中置信度**。
理论导向偏 motivation（Yang 的 diminishing returns, Kim 的 heatmap）; 方法导向偏 teaser。
→ 本项目建议 motivation 类: homo vs hetero ASR scaling 对比。

## 6. 主结果: Scaling→Line plot, 对比→Table
**7/8**。**高置信度**。
Scaling 行为: line plot (Turkmen error-vs-k, Yang accuracy-vs-N, Kaneko log-log)。
方法对比: table (PEG Table 1, TVD-MI Table 2)。
高亮: bold best 5/8; 理论验证用 regression slopes+p-values (Kaneko)。
统计: 趋势为 mean±std across seeds，但 3/8 仍 single run。

## 7. 消融: Full numbers 主导 (5/8)
**高置信度**。无 checkmark grid。关键消融放 main（PEG K-scaling），其余 appendix。

## 8. 图表叙事流 (6/8 共识)
**高置信度**。Motivation/Problem → Method/Theory → Main Results → Ablation。
数量: 4-6 figures (中位 5), 3-5 tables (中位 4)。
分工: scaling/correlation→图; 方法对比/消融→表; 扩展→appendix。

## 9. 理论验证的视觉模式
**3/8**。**中置信度**。
Kaneko: log-log plot, slope-1 参考线; Turkmen: empirical vs copula scatter; Yang: K* 单调性。
→ K_eff 验证需 "theoretical prediction vs empirical" 对齐图。
