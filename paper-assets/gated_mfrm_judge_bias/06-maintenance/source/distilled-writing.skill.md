---
name: judge-bias-contamination-writing
description: LLM judge bias与contamination领域的论文叙事策略、图表设计共识——8篇深度精读蒸馏
type: skill
---

## 叙事类型

"突破局限型"最主流（4/8：preference_leakage, ConStat, UDA, CyclicJudge），其次"化繁为简"（2/8）和"统一框架"（2/8）。G-MFRM 适合混合："突破局限"论证 sequential 的 confounding，"统一框架"呈现 joint model。**置信度 高**

## 开篇钩子

**具体案例**（zheng2023 Figure 1，3/8）、**定量冲击**（CyclicJudge ">94% variance"，3/8）、**实践脱节**（DCR，2/8）。G-MFRM 用定量冲击：lead with confounding 的 θ-RMSE degradation。**置信度 高**

## 张力构建

领域标准：论证现有方法有**不可修补的 structural flaw**。ConStat: "perplexity methods fundamentally evadable"。CyclicJudge: "systematic bias cannot average out"。G-MFRM 的张力：sequential pipeline 存在 identifiability problem，d_j 和 c_n·e_i confounded。**支持度 5/8，置信度 高**

## 洞察呈现

**Method 前的概念重构**效果最强（3/8）：ConStat Section 2 重新定义 contamination，preference_leakage Section 3 形式化 relatedness，CyclicJudge Proposition 1。G-MFRM 建议 Section 2 用 toy example 展示 confounding，Section 3 给 G-MFRM 方程。**置信度 中**

## Figure 1

- motivation 型最多（3/8），**problem illustration** 效果最佳（preference_leakage "data leakage vs preference leakage" 一图定义新概念）
- G-MFRM 建议：左 sequential pipeline（两步+confounding 标注），右 joint model（gating mechanism 高亮），颜色区分 d_j 和 c_n·e_i

## 主结果表

- 行=methods, 列=metrics/datasets（4/8）。judge-model 矩阵在 bias 研究常见（CyclicJudge, UDA）
- **Highlight**: bold_best（4/8），颜色编码（preference_leakage 蓝紫背景最创新），bold+underline_second（CyclicJudge）
- **统计**: mean ± CI/std（3/8），bootstrap 显著性在 contamination 论文是标准
- **Baselines**: 5-10 个
- G-MFRM 主表：行=4 methods，列=ρ levels × metrics，mean ± std ≥20 seeds + Wilcoxon p

## 消融表

full numbers 占绝对主流（6/8），checkmark grid 在此领域不常见。建议 G-MFRM：row=components (gating/judge facet/contamination facet on/off)，full numbers。**置信度 高**

## 图的叙事节奏

典型：motivation → method → main result → mechanism。CyclicJudge: 策略对比 → bias heatmap。ConStat: workflow → quantification scatter (r²=0.94)。G-MFRM 建议：概念图 → 方法 → θ-RMSE vs ρ → 参数恢复 scatter/heatmap。

## 图表分工

- **图**: variance/trend→line plot, correlation→scatter, bias 结构→heatmap
- **表**: precision numbers (accuracy/detection rate), ablation
- **附录**: full matrices, robustness checks, prompts。主文保持 2-5 tables + 2-5 figures
- **支持度 6/8，置信度 高**
