---
name: distilled-writing
description: "Activation steering × alignment 领域论文的叙事结构、图表编排与写作惯例"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 21
  paper_keys: [ackermann2026gradreg, burns2023ccs, casper2023openproblems, consistency2025bctact, denison2024subterfuge, gao2023scaling, li2023iti, mckinney2023fragility, obrien2025fewbadneurons, rimsky2024caa, shao2024grpo, shapira2026amplifies, sharma2023sycophancy, sinii2025smallvectors, skalse2022hacking, turner2023actadd, wang2025internal, wei2024synthetic, wen2024mislead, zhang2026latentgrpo, zou2023repe]
  last_distilled: "2026-05-24T00:00:00Z"
---

## 故事类型

**突破局限型**占主流 (5/8 深读: Burns, Gao, Li, McKinney, Zhang): 现有方法有隐藏瓶颈→发现→解决。**化繁为简型** (2/8: Rimsky, O'Brien): 复杂问题有简洁解法。**统一框架型** (1/8: Skalse): 散乱现象背后有统一理论。默认选突破局限型。(**支持度 5/8, 高**)

## Intro 结构

4-5 段标准 (**6/8, 高**, 代表: Li/ITI): P1 问题(safety stakes) → P2 现有方案局限 → P3 本文方案+核心insight → P4 结果数字+贡献列表 → P5(可选)论文结构。

## 钩子与贡献声明

钩子四式: ①安全焦虑 "raises new risks"(Burns/Rimsky, 3/8); ②Gap量化 — Li "40% knowing-telling gap" 把抽象claim变可记忆数字; ③经典原则引用 — Gao 以 Goodhart's law 锚定; ④生动反例 — Skalse "boat spinning in circles" 三例破冰。

贡献声明: 3-4 bullet points 在 intro 末段 (**4/8, 高**); 范式开创工作用 "initial step" hedging (Burns); 方法足够简洁可不列 list (Rimsky, Zhang, **2/8, 中**)。

## Figure 1 设计

- **Method overview** 最主流 (4/8): Burns, Rimsky, O'Brien, Zhang。左到右 pipeline flow + 关键公式内嵌。(**支持度 4/8, 高**)
- **Teaser result** (3/8): Gao(overoptimization曲线), Li(before/after对比), McKinney(anti-correlation三面板)。适合结果本身有视觉冲击力时。
- 设计共识: 对比布局(before/after 或 ours/baseline) + 颜色编码(2-3色) + 具体示例而非纯抽象。

## 表格编排

主结果表: **行=方法, 列=数据集×指标** (**4/8, 高**, 代表: Burns Table 1)。行按 category 分组 (baselines/ours/ceiling)，baseline 2-8 个。高亮无统一标准: bold best (Zhang)、color max/min (Rimsky)、或无高亮 (Burns)。统计: mean±std / N seeds averaged / 单次 — **各占 1/3** (**置信度 中**)。

消融一律用 **full numbers** 而非 checkmark grid (**8/8, 高**)。Layer sweep 用 line plot; 多维消融用 heatmap (Gao)。分析型论文全用图 (Gao/McKinney)，方法型论文图表混用 (Li/Rimsky)。

## Figure 叙事节奏

典型编排: method overview → empirical evidence → main results → ablation → mechanistic analysis。(**支持度 5/8, 高**, 代表: Rimsky/CAA)

特别有效的技巧:
- **Discovery-first**: Zhang 先用 PCA scatter 展示 clustering 现象 (Fig 2)，再提出利用它的方法 — 让方法显得是发现的自然推论
- **Front-load punchline**: Gao 把两个 scaling law 方程直接放 intro — 读者立刻知道核心结果
- **Composability 论证**: Rimsky 展示 CAA 可叠加 system prompt 和 finetuning — 把 "又一个 steering 方法" 重新定位为 "增强任何现有方案的工具"
