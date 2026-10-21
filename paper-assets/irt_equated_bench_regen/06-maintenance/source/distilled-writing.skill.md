---
name: distilled-writing
description: "LLM benchmark contamination与IRT评估领域的论文写作共识：叙事结构、开篇模式、Figure 1设计、结果表编排、图表分工"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [dekoninck2024constat, tao2026selfcritique, white2025livebench, li2024latesteval, maiapolo2024tinybenchmarks, balloccu2024leak, golchin2024timetravel, li2024contamination, shi2024mink, wang2026fragility, zhou2026psnirt, chiang2024chatbot, wang2024mmlupro, liang2026dvd, zhang2024minkpp, habba2026growingpains, lalor2019irt, vania2021irt, hendrycks2021mmlu, kiela2021dynabench, chang2024survey, hardy2026scalability, zhang2024gsm1k, li2025atlas, chen2025irtnet]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 故事类型与开篇模式

**突破局限型**(4/7): 现有方法有根本缺陷→新范式。ConStat("effect-based vs information-flow"), Self-Critique("RL erases signals")。
**化繁为简型**(3/7): tinyBenchmarks("100 items够了"), LatestEval("用最新文本")。本项目适合此型。

**开篇钩子**: 震撼数字最主流(4/7)——"90% of QuAC contaminated"(LatestEval), "42% leaked"(Leak,Cheat,Repeat)。可模仿: 引用GSM1k 13% drop或45.8% contamination rate。**置信度高**

## Intro结构

4-5段: (1)问题+震撼数字 → (2)现有方法局限 → (3)本文方法(含Figure 1引用) → (4)结果预告+贡献列表(3-5条,首条用"first"/"novel")。**6/7｜置信度高**

## Figure 1设计

- **method_overview**(3/7): Pipeline流程图(ConStat四步, LatestEval五步)。最安全选择。
- **motivation对比**(2/7): 关键现象可视化(entropy差异, guided vs general)。直觉清晰时更抓人。
- **teaser_result**(1/7): 核心结果浓缩(error vs sample size)。

**置信度高**

## 结果展示共识

**主结果**: 表格(method×dataset矩阵), bold best, 4-8 baselines。row=methods, col=datasets×metrics。3/7。
**补充分析**: scatter(相关性 2/7), line plot(趋势 2/7)。
**统计报告**: 百分比为主; bootstrap p-value/CI(3/7); mean±std少见。
**消融**: full_numbers主流(5/7), checkmark grid不出现。3-5维度。

**7/7精读｜置信度高**

## 图表分工

方法pipeline→Figure 1; 方法对比→Table(检测率/AUC); 相关性→Scatter; 趋势→Line; 案例→Qualitative figure; 消融→Table(full numbers); 详细结果→Appendix table。**置信度高**

## 可模仿策略

1. **Intro嵌数字例子**: ConStat用"60%→expected 37%→actual 72%→δ=35%"让读者一看懂方法。降低认知负载。
2. **"≠"式发现**: Li2024"contamination≠boost"避免简单叙事。提升可信度。
3. **Intentional contamination验证**: Time Travel用fine-tuning注入已知数据做ground truth。说服力强。
4. **Toolkit降低门槛**: tinyBenchmarks附HuggingFace+Package+Colab。增加影响力。
