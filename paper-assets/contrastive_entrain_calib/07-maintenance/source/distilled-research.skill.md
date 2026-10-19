---
name: distilled-research
description: "Activation steering × reward alignment 领域的实验设计共识、baseline 惯例、竞品定位与研究空白"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 21
  paper_keys: [ackermann2026gradreg, burns2023ccs, casper2023openproblems, consistency2025bctact, denison2024subterfuge, gao2023scaling, li2023iti, mckinney2023fragility, obrien2025fewbadneurons, rimsky2024caa, shao2024grpo, shapira2026amplifies, sharma2023sycophancy, sinii2025smallvectors, skalse2022hacking, turner2023actadd, wang2025internal, wei2024synthetic, wen2024mislead, zhang2026latentgrpo, zou2023repe]
  last_distilled: "2026-05-24T00:00:00Z"
---

## 方法族谱

两条主线交汇：**activation engineering**（7/21）和 **reward hacking/alignment**（5/21），sycophancy 研究（7/21）横跨两者。

- **Activation steering**: ActAdd(单对) → CAA(多对平均) → ITI(probe引导) → SAE neuron surgery。演进方向：从粗粒度到精准定位。(**支持度 7/21, 高**)
- **Reward robustness**: 理论不可能性(Skalse) → 经验scaling law(Gao) → 训练时正则化(Ackermann/GRPO)。(**支持度 5/21, 高**)
- **Sycophancy**: 分析型(Sharma/Wang/Wen) → 数据干预(Wei) → 一致性训练(BCT/ACT) → 神经元手术(O'Brien)。(**支持度 7/21, 高**)

## Baseline 惯例

| 必选 baseline | 出现频率 | 来源 |
|---|---|---|
| 无干预 base model | 15/21 | 几乎所有 |
| 标准 RLHF/SFT | 8/21 | Li, Rimsky, Wei 等 |
| KL penalty 约束 | 4/21 | Gao, Shapira, Ackermann |
| Zero/few-shot prompting | 4/21 | Burns, Li |
| System prompting | 3/21 | Rimsky, Turner |

**共识**: 至少需要 base model + 一种 training-based method + 一种 inference-time method 三组对照。(**置信度 高**)

## 评估指标共识

- **任务准确率** 是通用必报指标 (15/21)
- **Sycophancy rate** 作为 alignment-specific 指标已标准化 (6/21, 代表: Sharma)
- **KL divergence** 衡量干预代价 (5/21, 代表: Gao, Li)
- **MMLU** 作为 capability preservation 必测 (3/21, 代表: Li, Rimsky)
- **GPT-4 评分** 用于 open-ended generation (2/21, 代表: Rimsky) (**置信度 中**)

## 实验设计模式

- **Layer sweep** 是 activation engineering 标配消融 (5/7 activation 论文)，结论收敛于中间层最优 (代表: Rimsky layer 13/7B)
- **Model scale sweep** 覆盖 2+ 尺寸 (8/21)，但多数仅 1-2 家族 (**局限**)
- **Probe accuracy vs generation accuracy gap** 是证明 "模型内部知道但不说" 的标准论证 (Burns: +4%, Li: 40% gap)
- **Relearning evaluation** (冻结 reward, 从头训新 agent) 是 reward robustness 的金标准但极少采用 (1/21, McKinney) (**研究空白**)

## 竞品定位

**Competitor** (直接竞争): Wang(机制分析无干预), Wei(synthetic data finetuning)——两者分别代表 "只分析不修" 和 "用数据而非表征" 路线。
**Foundation** (我们的基础): Burns/CCS, Li/ITI, Rimsky/CAA, Zou/RepE, Skalse/理论——这条线确立了 "内部表征可提取并操控" 的范式。

## 研究空白

1. **多轮对话** 中的 steering 效果几乎无人测试 (仅 O'Brien 提及局限) (**置信度 高**)
2. **无监督方向发现** 在 scale 上未被验证 (Li 明确标注为 future work) (**置信度 高**)
3. **Reward hacking 理论 × activation engineering** 无交叉研究——Skalse 的不可能性定理对 steering 意味着什么？(**置信度 中**)
4. **跨模型族迁移** 仅 Sinii 初步探索同族迁移，跨架构迁移空白 (**置信度 中**)
