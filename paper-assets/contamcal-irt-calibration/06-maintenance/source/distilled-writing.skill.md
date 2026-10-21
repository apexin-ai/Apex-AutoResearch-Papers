---
name: distilled-writing
description: "LLM benchmark contamination领域论文的叙事模式、Figure/Table编排共识与可模仿的写作策略"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [dong_2024_cdd, deng_2024_tsguessing, xu_2025_dcr, sun_2025_emperors_new_clothes, li_2025_dcr, zhang_2024_minkpp, choi_2025_kds, lalor_2024_irt_nlp, polo_2024_tinybenchmarks, zhou_2025_psnirt, chiang_2024_chatbot_arena, golchin_2024_time_travel, shi_2023_minkprob, schaeffer_2026_generative_contamination, luettgau_2025_hibayes, zheng_2023_chatbot_arena, brown_2024_ppp, sinharay_2025_irt_fit, guo_2017_calibration, dekoninck_2024_constat, zhang_2024_gsm1k, habba_2025_growing_pains, li_2024_atlas, angelopoulos_2023_conformal, white_2024_livebench]
  last_distilled: "2026-05-23T12:00:00Z"
---

## 叙事类型分布

- **突破局限型**最主流（3/6 深读篇：CDD, TS-Guessing, Emperor's）：现有方法有明确缺陷 → 本文解决。置信度：高。
- **统一框架型**（DCR）和**化繁为简型**（Min-K%++）各占一席。置信度：中。
- **跨界迁移型**（KDS 从 kernel methods 引入 contamination）适合方法论跨界的论文。置信度：中。
- **推荐**：ContamCal 适合「跨界迁移型」——从教育测量 IRT 迁移到 LLM contamination calibration。

## 开篇钩子模式

- **「信任危机」钩子**（4/6 篇）：直接点出 benchmark scores 不可信，LLM 评估的根基动摇。来源：dong "inflated performance estimates", sun "evaluation integrity"。置信度：高。
- **「检测不够，需要量化」钩子**（2/6 篇）：承认检测工作已有进展，但强调 detection ≠ actionable correction。来源：xu_dcr "few methods integrated into actual development"。置信度：中。
- **可模仿策略**：第一句用具体数字制造紧迫感（如 "ChatGPT guesses 52% of masked MMLU options"），而非泛泛说 contamination 是问题。

## 张力构建共识

- **核心张力模板**：existing methods do X but fail at Y，其中 Y 是本文贡献。所有 6 篇深读论文都遵循此模式。置信度：高。
- **高效张力来源**：(1) 理论 vs 启发式（Min-K%++）；(2) 检测 vs 校准（DCR, CDD）；(3) 未经验证 vs 严格评估（Emperor's）。
- **可模仿策略**：ContamCal 的张力 = "检测方法只给 binary flag，不给 calibrated score with uncertainty"。

## Intro 结构共识

- **4-5 段制**（6/6 篇）：problem → existing work limitations → key insight/approach → contributions → [paper outline]。置信度：高。
- **贡献声明**：2-3 条为主流（来源：dong 2条, xu 3条, sun 3条）。置信度：高。
- **可模仿策略**：贡献不超过 3 条，每条用动词开头（"We propose/demonstrate/reveal"），最后一条放 empirical finding 而非 framework。

## Figure 1 设计模式

- **method_overview**（2/6 篇：deng, xu_dcr）和 **motivation**（2/6 篇：dong, choi）并列最主流。置信度：中。
- **设计元素共识**：pipeline/flowchart 布局、对比面板（before/after 或 method A vs B）、实际样例而非纯示意图。
- **最有效模式**：Min-K%++ 的 Figure 2（两个概率分布相同 target probability 但不同 relative ranking）—— 一张图让理论贡献可视化。置信度：高。
- **推荐**：ContamCal Figure 1 用 motivation 型——展示同一 benchmark 上 raw score vs calibrated score 的差异，或 Min-K%++ directional reversal 的视觉证据。

## 主结果表编排

- **行=methods, 列=datasets×metrics** 是标准格式（4/6 篇）。置信度：高。
- **Baselines 数量**：5-8 个（中位数 ~5）。置信度：高。
- **高亮策略**：bold best（4/6 篇）；green significance highlighting 仅 Emperor's 使用。置信度：高。
- **统计报告**：本领域多为 point estimate，仅 2/25 篇用 mean±std。置信度：高——这恰好是 ContamCal 的 Bayesian CI 差异化点。
- **推荐**：主表 row=models, col=benchmarks×{raw_acc, adjusted_acc, 95%CI width}，bold best adjusted accuracy。

## 消融表/图偏好

- **Full numbers 格式主导**（4/6 篇），checkmark grid 不常见。置信度：高。
- **Component decomposition** 适合多信号/多模块方法（Min-K%++ 拆分 mean/std 贡献；ContamCal 可拆分 S1/S2/S3/S4 信号贡献）。

## 图表分工模式

- **结果用表、趋势/相关性用图**（5/6 篇）：散点图看 correlation，柱状图看 across-condition comparison，表格看精确数字。置信度：高。
- **Figure 叙事节奏**：motivation/overview → method diagram → result visualization → ablation。4/6 篇遵循此序列。置信度：高。
- **附录放什么**：implementation details、extended ablation、hyperparameter sensitivity（4/6 篇）。主表 ≤3 张，附录可多。置信度：高。
