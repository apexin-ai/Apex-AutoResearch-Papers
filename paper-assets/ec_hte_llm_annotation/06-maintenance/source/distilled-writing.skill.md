---
name: LLM Annotation Debiasing — Writing & Visualization Patterns
description: 从8篇精读论文蒸馏的叙事结构、Figure/Table惯例、贡献声明模式——可直接模仿的写作策略
type: writing
domain: ec_hte_llm_annotation
source_papers: 8
distill_date: 2026-05-21
---

## 主流故事类型

**突破局限型**（5/8）：证明 naive approach 有严重后果，再给解法。需 intro 中"震撼证据"。Egami'23、Zrnic'24、Sui'26、Mehrotra'26、Ashwin'25 均采用。**5/8，高。**

## Intro 结构（4-5 段）

共识：(1) 趋势/背景 → (2) 核心问题 → (3) 现有方案缺陷 → (4) 方法 + 预告数字 → (5) 贡献列表。必须在 intro 预告关键数字。**7/8，高。**

## Hook 技巧

**"反直觉数字"**："90% accuracy → 40% CI coverage"（Egami'23）、">80% budget savings"（Zrnic'24）。intro 第2-3段放置。**3/8，高。**

**"否定直觉解再引正解"**：先证最自然方案行不通。Mehrotra'26 证 persona prompting 失败；Egami'23 展示三种 naive 方法各有致命伤。**3/8，高。**

## 核心洞察呈现

**"一个公式讲全部故事"**：V=(1/n)σ²_{Y-f}+(1/N)σ²_f 同时解释原理、最优条件、预算分配（Sui'26、Zrnic'24）。**2/8，中。**

**"渐进升级"**：accuracy gap → systematic bias → wrong conclusions。Ashwin'25 从 F1 升级到 F-test 再到系数反转。将技术问题转为"论文结论会反"。**1/8，低但极有效。**

## Figure 惯例

**Figure 1：**method overview（4/8）或 motivation+teaser（2/8）。展示 inputs→method→output 数据流。**6/8，高。**

**主结果图：**line plot，y=coverage/CI width/bias，x=标注量 n。画 95% 参考线。3+ 数据集用统一布局。**5/8，高。**

**全图无表策略：**推断论文倾向 0 table（Zrnic'24、Sui'26、Bu'23、Ashwin'25=4/8）。结果是 x₀ 或 n 的函数时图优于表。**4/8，高。**

## Table 惯例（当使用时）

**Benchmark 表：**颜色编码区分指标（非仅加粗），按类别分组行（Egami'23：17数据集）。**1/8，中。**

**群体×方法矩阵：**列=群体，行=方法，格=coverage+error，突出失败群体（Mehrotra'26）。**1/8，中。**

## Figure 叙事节奏

共识：**Overview → Motivation → Results (×3 domains) → Sensitivity**。变体：渐进升级 accuracy→bias→consequences（Ashwin'25）；汇总图收尾呼应 intro hook（Zrnic'24）。**6/8，高。**

## 贡献声明

2-4 个编号贡献。用"guarantee"/"without requiring"强调无条件有效性。Benchmark 论文用 RQ 替代 claim。方法 + 实证作为独立贡献项。**7/8，高。**
