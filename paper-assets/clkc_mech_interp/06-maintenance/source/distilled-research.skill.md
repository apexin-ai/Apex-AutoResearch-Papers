---
name: distilled-research
description: "跨语言知识冲突与机制可解释性领域的实验设计共识、方法论趋势、竞品定位与研究空白"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [li2025taming, zhao2025steering, ifergan2024beneath, wang2025lost, xie2024adaptive, xu2024knowledge, zhao2024analysing, wendler2024llamas, kargaran2024mexa, feng2026finegrained, basu2026interpretability, boer2026probing, kialy2026universal, pham2026where, wong2026langfir, zhao2026when, li2023iti, wu2020emerging, muller2021first, hewitt2019designing, conneau2018xnli, rei2020comet, team2026qwen, xing2024evaluating, grattafiori2024llama]
  last_distilled: "2026-05-24T18:00:00Z"
---

## 实验设计共识

**模型**：Llama-2-7B 是标准测试床（7/8），Llama-3-8B/Gemma-2 为新兴标配。7B 主流。**7/8 高**（li2025taming）

**数据集**：NQSwap 最常用（3/8），PopQA 用于行为分析（2/8）。跨语言方向各组自建数据集（CLIKE/KLAR），无统一标准。**5/8 高**

**指标**：Exact Match 主流（5/8），跨语言一致性 CKC/CKR（3/8），探测用 AUROC（2/8）。**5/8 高**

**Baseline**：CAD 是知识冲突最常见 baseline（3/8）；表征工程需对比 ActAdd/TaskVec/SEA。**3/8 中**（zhao2025steering）

## 方法论趋势

**上升趋势 — SAE 方法**：5 篇论文使用 SAE（zhao2025steering, kialy2026universal, wong2026langfir, team2026qwen, basu2026interpretability），从分析工具演进为实用干预手段。SpARE 超越表征工程+10%、超越对比解码+15%。**支持度 5/25，置信度 高**

**上升趋势 — 推理时干预**：JuICE、SpARE、ITI、fine-grained steering 均无需微调，在测试时编辑激活。这一范式正在取代需要训练的方法。**支持度 4/25，置信度 高**（代表：li2025taming, li2023iti）

**稳定 — 残差流分析**：线性探测 + 层级分析是机制理解的标准工具（3/8 深读），中间层是冲突信号和知识选择的关键位置。**支持度 3/8，置信度 高**（代表：zhao2024analysing 层14峰值）

## 关键发现共识

**跨语言表示共享 ≠ 行为一致性**：编辑一种语言的知识后，传播遵循脚本（script）相似性而非语言家族。CKC 高不代表 CKR 高。**支持度 2/8，置信度 高**（代表：ifergan2024beneath, wang2025lost）

**英语概念空间偏置**：Llama-2 在中间层通过接近英语的概念空间处理非英语输入，最终层才转换到目标语言。转换失败导致跨语言不一致。**支持度 2/8，置信度 高**（代表：wendler2024llamas, wang2025lost）

**CP 叠加现象**：注意力头同时编码上下文和参数知识（非排他性），需双运行干预才能解耦。**支持度 1/8 但 ICML Spotlight，置信度 中**（代表：li2025taming）

## 竞品定位与研究空白

**竞品 claim**：pham2026where 做 intra-memory 冲突机制分析；zhao2026when 做跨语言冲突分析（CLEAR 框架）；basu2026interpretability 警告机制可解释性存在"知识-行动鸿沟"。

**研究空白**：(1) 知识冲突 × 多语言的交叉研究极少——大多数论文只研究其一；(2) SAE 方法在跨语言知识冲突场景未被验证；(3) 7B 以上规模的机制分析缺失；(4) 非英语 pivot 的替代方案无人探索。**置信度 高**（8篇深读论文交叉比对）
