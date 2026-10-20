---
name: distilled-writing
description: "Data weighting/mixing 论文写作范式：叙事结构、figure/table 编排、结果呈现共识 (8篇顶会精读)"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [drayson_2025_detection_collapse, feng_2025_beyond_collapse, subramanyam_2025_scaling_quality, amin_2025_escaping_collapse, sow_2025_dynamic_reweighting, ye_2025_data_mixing_laws, he_2024_softdedup, chen_2025_aioli]
  last_distilled: "2026-05-24T12:00:00Z"
---

## 叙事类型分布 (8/8, 高)

- **化繁为简型** 3/8: SoftDedup, LinUpper, DML — 复杂问题→单一公式
- **突破局限型** 2/8: Drayson, Feng — 现有方法不能→我们能
- **统一框架型** 2/8: Aioli, Subramanyam — 散乱方法→统一视角
- **跨界迁移型** 1/8: Amin — boosting→synthetic training

## 开篇钩子

**数字冲击** (2/8): Feng "60.4% vs 19.2%"; Drayson "perplexity ↑100%"

**简洁问题** (4/8, 最主流): 一句话定义痛点，无铺垫。如 "treats all samples uniformly"

**共识挑战** (2/8): "no method consistently beats stratified sampling" (Aioli)

**建议:** 本项目用数字冲击 — "1% synthetic causes collapse" (Strong Collapse) 开篇。

## Intro 结构 (8/8, 高)

4-5段: Problem → Existing + limitations → Our insight → Contributions (3个, 动词开头)

## Figure 1 模式

- method_overview/pipeline: 2/8 (DML, LinUpper)
- teaser_result: 2/8 (Drayson, Subramanyam)
- motivation/problem_illustration: 2/8 (SoftDedup, Feng)
- motivation triptych: 2/8 (Aioli, Amin)

**共识:** Fig1 必须不读正文即传达核心 message。高频设计元素：对比布局(5/8), 颜色编码(4/8)。

**建议:** 用 motivation 类 — provenance-unaware 失败 vs provenance-aware 成功的对比。

## 结果可视化 (6/8, 高)

- **Line plot** (training/generation curve): 5/8 主结果图
- **增益突出**: proposed vs baseline 的 gap 面积
- **消融**: line plot (连续参数), 表格 (离散组件)
- **分工**: 图=trends/distributions; 表=final numbers/per-task breakdown

## 主结果表 (7/8, 高)

- Row=methods (by category), Col=datasets×metrics
- Baselines: 3-6个 (中位5)
- **高亮**: bold best (6/8); percentage change format 让 improvement 更直观 (Drayson)
- **统计**: mean±std/3seeds 是金标准; 单次运行也可接受 (LLM pretraining 成本)

## 消融表 (5/8, 中)

- Full numbers: 4/8 (最主流)
- Delta from base: 2/8
- 本领域倾向 full numbers + bold best

## Figure 编排节奏 (6/8, 高)

Motivation(Fig1) → Method(Fig2) → Main results(Fig3-4) → Ablation(Fig5+)

总数: 2-10 (中位5)。理论重=少, 实证重=多。

**建议:** 本项目 5-6 figures: motivation → method → collapse curves → scaling → ablation

## 高影响写作技巧

1. **"Exceeds oracle"** (Drayson, Feng): 证明 curated synthetic > pure human 翻转预期
2. **Zero-overhead** (LinUpper): "uses losses already computed" 一句消除 scalability 顾虑
3. **Fidelity decomposition** (Aioli): 定位失败的精确层次 (law ok → params wrong)
4. **Iso-loss contours** (Subramanyam): quality-quantity tradeoff 可直接查表
