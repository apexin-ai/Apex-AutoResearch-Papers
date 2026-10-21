---
name: distilled-writing
description: "多轮越狱检测与说服攻击论文的叙事结构、图表编排和写作模式蒸馏"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys:
    - "WildGuard"
    - "HarmBench"
    - "PAP"
    - "ActorAttack"
    - "Simple Adaptive Attacks"
    - "DeepContext"
    - "BIID"
    - "G-Guard"
    - "SafeDream"
    - "Jailbroken"
    - "Llama Guard 3"
    - "Crescendo"
    - "Large Reasoning Models"
    - "Deceptive Delight"
    - "Red Teaming LM"
    - "Constitutional Classifiers"
    - "ShieldGemma"
    - "RepEng Multi-Turn"
    - "LLM Persuade Probes"
    - "Foot In The Door"
    - "Annotation Artifacts"
    - "Probing NN Arguments"
    - "Debiasing Fact Verification"
    - "DeBERTa"
    - "Which Argument"
  last_distilled: "2026-05-24T06:30:00Z"
---

## 故事类型分布

- **突破局限型**（4/8）：WildGuard、Simple Adaptive、DeepContext、BIID。套路：现有方案在 X 场景下崩溃 → 我们解决了 X。**置信度**：高
- **跨界迁移型**（3/8）：PAP（社会科学说服）、ActorAttack（行动者网络理论）、G-Guard（GNN）。套路：领域 A 的理论/方法可直接迁移到 LLM 安全。**置信度**：高
- **统一框架型**（1/8）：HarmBench。适合评估/benchmark 论文。**置信度**：中

## 开篇 Hook 模式

**模式 1：真实攻击案例（最常用）**。ActorAttack 用 Ted Kaczynski 多轮对话，G-Guard 用 Yahoo 泄露案例，PAP 用 grandma exploit。效果：读者 3 秒内理解威胁。**支持度**：4/8，来源：ActorAttack。**置信度**：高

**模式 2：Gap/Crisis 定量化**。WildGuard 展示 adversarial F1 崩溃（81.6% vs 85.5%），HarmBench 列举 9 种不同评估流程。效果：用数字建立紧迫感。**支持度**：3/8，来源：WildGuard。**置信度**：高

**模式 3：跨域类比**。Simple Adaptive 用 CV 对抗鲁棒性评估类比 LLM 安全。效果：借已知领域信誉。**支持度**：1/8，来源：Simple Adaptive。**置信度**：低

## 张力构建共识

核心张力公式：**"现有方案假设 X，但现实是 Y"**。
- 无状态 vs 有状态：DeepContext（"将多轮对话视为断开事件"）、BIID、G-Guard。3/8 篇。
- 单轮 vs 多轮：PAP（"仅关注单轮说服"→自己承认为 limitation）、ActorAttack、BIID。3/8 篇。
- 复杂 vs 简单：Simple Adaptive（"简单组合比复杂方法更有效"）。反直觉结论制造记忆点。

## Intro 结构共识

5-6 段 + 贡献列表是标准格式（6/8 篇）。典型结构：P1 背景/威胁 → P2 现有方法 → P3 现有方法局限 → P4 本文核心思路 → P5 结果亮点 → 编号贡献列表。贡献数量 3-5 条（PAP 7 条偏多）。**支持度**：6/8，**置信度**：高

## Figure 1 设计模式

- **problem_illustration**（3/8）：ActorAttack、BIID、G-Guard。多轮检测论文主流选择——用真实对话案例建立问题动机。**置信度**：高
- **method_overview**（3/8）：WildGuard、HarmBench、DeepContext。框架/系统论文偏好。**置信度**：高
- **teaser_result**（2/8）：PAP、Simple Adaptive。攻击论文偏好——先亮结果再讲方法。**置信度**：中

**设计元素共识**：多轮论文 Figure 1 几乎都用对话气泡/截图格式，左右对比（安全 vs 不安全），颜色标注（红=有害，绿=安全）。

## 主结果可视化

**表格为主，图为辅**（6/8 篇主结果用表格）。**支持度**：6/8，**置信度**：高
- **Heatmap**：适合展示攻防矩阵（HarmBench Figure 5）或多攻击×多模型全景（BIID Figure 3）。2/8 篇。
- **Bar chart**：适合单维度对比或 adversarial/vanilla 拆分（WildGuard Figure 2）。3/8 篇。
- **Scatter plot**：Safety-Utility tradeoff 可视化（BIID Figure 4，左上角最优的空间隐喻）。1/8 篇但效果极佳。
- **Line plot**：适合展示随轮次/预算变化的趋势（PAP Figure 9，ActorAttack Figure 4）。

## 主结果表编排

- **行轴**：methods，按类别分组（single-turn baselines / multi-turn baselines / proposed）。**支持度**：7/8，**置信度**：高
- **列轴**：models 或 datasets × metrics。按模型分组（grouped_by_model）最常见。**支持度**：5/8，**置信度**：高
- **高亮策略**：bold_best 是标准（6/8）；少数用 bold_best + underline_second。**置信度**：高
- **统计报告**：单次运行百分比为主（6/8），无置信区间。攻击论文尤其如此。**置信度**：高
- **基线数量**：3-11 个，中位数约 7。**置信度**：高

## 消融表偏好

- **full_numbers**（完整数字）最常用（5/8）。**置信度**：高
- **delta_from_base** 用于数据组分消融（WildGuard）或防御效果对比（PAP Table 3 用↓标注）。2/8 篇。
- **checkmark_grid** 在本领域不常用（0/8）。
- 消融嵌入主表（G-Guard w/o Aug 作为一列）是节省空间的常见做法。

## 图表分工模式

**图承担定性/趋势/动机，表承担定量对比**。典型编排：Figure 1 motivation → Figure 2 method → Table 1 main results → Figure 3-4 趋势/分析 → Table 2 消融。附录放 per-category 细分、完整案例、训练细节。**支持度**：6/8，**置信度**：高

## 叙事策略可直接模仿

1. **"State outperforms scale" 反直觉结论**（DeepContext）：用 GRU 打败 12B 模型，标题级记忆点。
2. **三级框架 positioning**（PAP）：算法系统→指令执行者→类人沟通者，一句话定位贡献在谱系中的位置。
3. **Motivation 表代替 motivation 段落**（HarmBench Table 1）：用 9 种评估流程对比表直接展示碎片化，比文字有效 10 倍。
4. **部署实验收尾**（WildGuard）：ASR 79.8%→2.4% 作为实际影响力证据。
