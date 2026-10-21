---
name: distilled-writing
description: "LLM剪枝与恢复领域的论文叙事模式——故事类型、开篇钩子、张力构建、图表编排、表格设计共识"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [self_healing_2025, grasprune_2026, bonsai_2025, pat_2025, rac_2025, restorelcc_2025, murphy_debiased_cka_2024, rl_squeezes_2026, p2_law_2025, hape_2026, slimllm_2025, wandapp_2025, davari_cka_reliability_2023, llm_pruner_2023, gao_reward_overoptimization_2023, lachance_thesis_2024, paser_2025, kornblith_cka_2019, raghu_svcca_2017, klabunde_similarity_survey_2025, grasp_2020, resp_2025, opsd_2026, doing_more_with_less_2026, gprune_llm_2026]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 故事类型分布

**突破局限型(4/7)**: 最主流。公式: "现有方法做了X但忽略了Y属性" → "我们发现Y是关键" → "针对Y的方法大幅提升"。代表: RestoreLCC("PEFT overlook distinct properties of pruned models")、RAC("reasoning is decode-dominated")。支持度: 4/7精读。置信度: 高。

**化繁为简型(2/7)**: 将复杂问题归结为一个简洁洞察。GRASPrune("not another metric, but the mismatch")、Bonsai(去掉梯度仍能工作)。置信度: 中。

**跨界迁移型(1/7)**: PAT借用QAT-vs-PTQ的类比。少见但效果好。置信度: 低。

## 开篇钩子模式

**反直觉悖论(最有效)**: RAC开篇指出"剪枝让推理模型变慢"——本应加速却减速，读者立刻被抓住。Murphy CKA用"随机矩阵得到高相似分"制造震惊。来源: RAC, Murphy CKA。置信度: 高。

**资源壁垒**: Bonsai用"gradient methods需要80-640GB内存"建立accessibility叙事。GRASPrune用"quality degrades non-linearly"的量化观察开场。置信度: 中。

**机制追问**: RL Squeezes以"SFT then RL is standard, but why?"开题——提问而非陈述。置信度: 中。

## 张力构建共识

核心模板: **"现有方法做X，但忽略了pruned model的独特属性Y"**。RestoreLCC: PEFT为dense设计，忽略pruned模型的activation特征。RAC: calibration基于input，忽略reasoning模型的decode主导性。GRASPrune: score learning与mask selection脱节。支持度: 5/7篇。置信度: 高。

## 贡献声明格式

**3条贡献是标准数量**(5/7篇)。典型模式: (1) 观察/发现, (2) 方法, (3) 实验验证。Bonsai列5条但属例外。贡献陈述通常在intro末段以bullet形式出现。置信度: 高。

## Intro结构

**4-5段是标准长度**。段落功能固定: P1=动机/问题 → P2=现有方法及局限 → P3=核心洞察和本文方法 → P4=贡献列表 → P5(可选)=论文结构。支持度: 7/7篇。置信度: 高。

## Figure 1设计模式

**Motivation型最主流(4/7)**: 用数据或可视化展示问题的严重性。GRASPrune: 非线性退化曲线。RAC: accuracy↓+runtime↑的悖论双轴图。Murphy CKA: 随机矩阵的高CKA分。设计元素共识: 简洁、单一核心信息、对比明显。置信度: 高。

**Method overview型(1/7)**: PAT直接展示架构图。较少见于intro figure。

## 结果表格编排

**行=方法, 列=数据集×指标**: 普遍共识(7/7篇)。行按category分组(baselines一组, 本方法一组)。支持度: 7/7。置信度: 高。

**高亮策略: bold best, 无underline second**: 6/7篇仅加粗最佳。统计报告以单次运行为主。Baseline数量3-6个为标准范围。

**按剪枝类型分表**: RestoreLCC为unstructured/semi-structured/structured各设独立表——用分表强调"universality"。置信度: 中。

## 消融表偏好

**Full numbers主导(5/7)**: 直接报完整数字而非delta。RestoreLCC用delta_from_base是例外且效果好(清晰显示marginal contribution)。Checkmark grid在本领域罕见。置信度: 高。

## 图表分工模式

**表格**: 主结果对比(所有方法×所有指标)、消融(组件开关)。
**图**: motivation(Fig1)、method overview(Fig2)、scaling/sensitivity曲线、layer-wise heatmap。
**附录**: 敏感性分析、额外模型/数据集结果、per-task breakdown。
图6-8个+表4-6个是典型容量。支持度: 6/7篇。置信度: 高。

## 图的叙事节奏

标准流: **Motivation → Method → Main Results → Analysis/Allocation → Ablation**。GRASPrune: 非线性退化 → pipeline → throughput → allocation → ranking比较。RAC: 悖论 → error heatmap → 结果表 → runtime分析。置信度: 高。

## 值得模仿的叙事技巧

1. **悖论开篇**: RAC的"pruning makes reasoning slower"是最强hook——反直觉+量化证据。
2. **QAT类比迁移**: PAT借用quantization领域的成熟概念，一句话建立直觉。
3. **Metaphor命名**: RL Squeezes的squeeze/expand隐喻创造了持久的mental model。
4. **Mechanism可视化**: RestoreLCC用attention head级对比展示"为什么targeted > generic"。
