---
name: distilled-writing
description: "Schema-guided zero-shot IE 领域写作 patterns：故事类型、开篇钩子、张力技法、intro 结构、图表编排共识"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [crossagentie-2025, zeroner-2025, kggen-2025, gliner2-2025, code4uie-2024, iepile-2024, lost-in-middle-2024, self-improve-ner-2024, self-prompting-re-2024, cmas-ner-2025, nuner-2024, familiarity-2025, gliner-2024, guidex-2025, uniner-2024, knowcoder-2024, slot-2025, godey-anisotropy-inherent-2024, llm-pee-2025, parse-2025, dee-2024, dlisc-2025, spt-2025, gollie-2024, llm4ie-survey-2024]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 故事类型

**突破局限型占主导**（6/8，高）：标准结构："现有方法假设 X → X 本身就是问题 → 我们直接改 X"。PARSE 最典型："schema 被视为静态合约 → schema 本身为人类设计非 LLM 优化 → 让 LLM 优化 schema"。化繁为简型 1/8（GLiNER），统一框架型 1/8（GLiNER2）。

## 开篇钩子

1. **LLM 悖论型**（4/8，高）：LLM 在其他任务强但 IE 上差。GoLLIE: "GPT-3.5 zero-shot NER 仅约 20 F1"。CrossAgentIE: "GPT-3.5 CoNLL03 仅 45%"。用反差制造动机。
2. **修辞提问型**（1/8）：ZeroNER "What happens when a NER system encounters entities it has never seen?"
3. **产业框架型**（1/8）：PARSE 用"Software 3.0"包装学术问题。适合 Industry track。
4. **效率冲击型**（1/8）：GLiNER 全文围绕"140 倍更小"的倍数对比。

## 张力构建技法

**定量铺垫**（3/8，高）：用数字量化问题。CMAS-NER: "87.33% demonstration 不含目标类型"配柱状图。ZeroNER: 报告 contamination 率。CrossAgentIE: "仅 45% F1"。

**双管齐下**（2/8，中）：CMAS-NER Figure 1 左 panel 定性示例 + 右 panel 定量柱状图。GoLLIE Figure 3 左右代码对比，视觉长度差异传达信息增益。

**自我批判**（1/8，低但值得注意）：GLiNER2 用自身成功带来的碎片化作为动机。

## Intro 结构

**5 段最常见**（6/8，高）：P1 任务重要性 → P2 LLM 新可能+不足 → P3 具体挑战（加粗） → P4 方案概述 → P5 贡献列表。

**贡献数量**：3-4 条安全区间（7/8）。挑战-贡献一一映射增加可追踪性（CrossAgentIE）。

## Figure 1 设计

- **method_overview**（4/8）：PARSE, CrossAgentIE, ZeroNER, GLiNER2 展示完整 pipeline。最主流。
- **problem_illustration**（2/8）：CMAS-NER 双 panel（定性+定量），GLiNER 左右范式对比。说服力最强。
- **teaser_result**（1/8）：GoLLIE 把结果 bar chart 放 intro，"先给结果再讲方法"建立 credibility。

**Figure 叙事流**：motivation/method → architecture → main results → ablation/analysis。5-8 图（中位 6）。

## 主结果表共识

- **行=methods，列=datasets×metrics**（7/8，高），grouped_by_dataset
- **bold best + underline second**；参数量标注方法名后形成隐式效率对比（GLiNER: "0.3B" vs "13B"）
- **Average 列**放最右（6/8）；baseline 3-13 个，中位 5-6
- **单次运行无 std 是常态**（6/8）；显著性检验仅 GoLLIE（p-value）和 CMAS-NER（*标记）使用
- 行按类别分组（by_category）主流

## 消融表与图表分工

**消融**：full_numbers 主导（6/8），checkmark_grid 不常见。GoLLIE 附 p 值是亮点。

**分工**：图用于方法架构、趋势曲线、定性 case study；表用于主结果、消融、错误分析。附录放超参数、prompt 模板、per-dataset 完整数字、数据集统计。Table 5-13 个（中位 5-6）。
