---
name: distilled-writing
description: "LLM agent adaptive routing/reasoning领域的论文叙事模式、图表编排共识和可模仿写作策略"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 9
  paper_keys: [mtrouter-2026, retool-2026, tsr-2026, cogrouter-2026, itp-2026, ares-2026, dynathink-2025, llm-agentic-failures-2025, envsimbench-2025]
  last_distilled: "2026-05-22T22:00:00Z"
---

## 叙事结构共识

**主流故事类型**: 突破局限型(4/8: MTRouter, ReTool, CogRouter, Failures) > 跨界迁移型(2/8: TSR, ITP) > 化繁为简型(1/8: ARES)、统一框架型(1/8: Dyna-Think)。支持度: 8/8 | 置信度: 高

**Intro 标准结构(4-6段)**: ①痛点 → ②现有方法局限 → ③核心洞察 → ④方法+结果预告 → ⑤贡献列表。支持度: 7/8 | 来源: CogRouter, TSR | 置信度: 高

**贡献数量**: 3 个最普遍(5/8)，"problem + method + evaluation"三段式。支持度: 5/8 | 置信度: 高

## 叙事策略拆解（可直接模仿）

**CogRouter**: Figure 1 展示 GRPO→L4 坍缩 vs CoPO 均衡分布，把"问题"变成视觉贡献。hook 用"cognitive rigidity"造术语。→ **用一张图量化问题现象，同时暗示方案解决了它。**

**TSR**: Sokoban Corner Trap 让抽象 rollout quality 变棋盘演示；compute-matched baseline 堵住"只是多算了"的质疑。→ **找直觉性 failure case 做 Figure 1；用 compute-matched control。**

**ReTool**: 6-panel 训练动态图讲"学会用工具"的故事(code ratio↑, length↓, invocation 提前)；Figure 4 展示 aha moment 自纠错。→ **训练动态图比最终结果图更有说服力；找 emergent behavior 做定性案例。**

**ARES**: 把方法定位在 performance-cost frontier 散点图上，与 model routing 形成视觉对比。→ **routing/efficiency 论文用 frontier 图定位方法。**

**Dyna-Think**: Figure 1 颜色标注 R1 思维链中有用(绿=WM simulation)与冗余(橙)部分，Table 3 量化"只保留 WM simulation 就够"。→ **对复杂系统做减法分析：高亮 what matters + 证明其余可删。**

## Figure 编排共识

**Figure 1 类型**: method overview(3/8) ≈ motivation/problem(3/8) > teaser result(1/8)。问题可视化冲击力更强但 method overview 同样常见。支持度: 7/8 | 置信度: 高

**叙事流**: Fig1(问题/方法) → Fig2(方法细节) → Fig3-4(训练曲线+结果) → Fig5+(行为分析)。5-7 张图是标准量。支持度: 6/8 | 置信度: 高

**行为分析图是加分项**: CogRouter(cognitive level 分布)、ReTool(6-panel 训练动态)、MTRouter(model specialization heatmap)、ARES(effort 分布)——解释 WHY 而非只展示 WHAT。支持度: 4/8 | 置信度: 高

## 表格编排共识

**主结果表**: row=methods 按类别分组(prompt/offline/online/frontier)；col 按 dataset 分组；bold best；**同时报效率指标已成惯例**(4/8)。Baseline 数 6-13，中位 ~10。支持度: 7/7 | 置信度: 高

**Ablation 表**: full numbers(5/7) > delta(2/7)。w/o X 是标准格式。CogRouter ablation 最值得学：同时展示 accuracy + token + level distribution。支持度: 7/7 | 置信度: 高

**图表分工**: 主结果=表，训练动态=图，行为分析=图，ablation=表或图均可。附录放 hyperparams 和 per-domain 细分。支持度: 6/8 | 置信度: 高
