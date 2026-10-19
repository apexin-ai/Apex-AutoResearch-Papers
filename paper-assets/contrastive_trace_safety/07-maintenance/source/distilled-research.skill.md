---
name: contrastive-trace-safety-research
description: LLM safety mechanistic interpretability 领域实验设计共识、方法论趋势与研究空白——10 篇论文蒸馏
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 10
  paper_keys: [zou2023representation, zou2023universal, zhou2024alignment, kaya2019shallow, hewitt2019control, zhou2020bert, arditi2024refusal, harmthoughts, safethink, chen2025unfaithful]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 方法论主流

### 对比对→方向提取（4/10，高）
构造 harmful/harmless 对比对，difference-in-means 提取方向。Arditi 128 对提取 refusal direction；RepE 对比刺激做表征读取；HarmThoughts 验证 16 行为类别近正交可分。共识：128-500 对即够。

### 简单探针优于复杂分类器（4/10，高）
Zhou (ACL'24) 用 sklearn 默认 SVM/MLP 达 >95%，"弱分类器也能分"是核心论据。Hewitt (EMNLP'19) 证明 MLP selectivity 仅 4.5 vs 线性 26.0。HarmThoughts Linear Probe (~0.49 F1) 优于 RFM/DoM。**经验：线性探针 + 随机标签对照（selectivity）是硬要求。**

### 逐层分析是标配（8/8 全文篇，高）
Zhou 发现伦理分类前几层即 >95%；Arditi 发现 refusal direction 在 40-80% 深度最强；PABEE 跨层一致性做 early exit；SafeThink 验证 1-3 步即可转向。共识：安全信号在不同层有不同功能（早层分类→中层关联→深层生成）。

## 实验设计共识

**指标**：ASR（4/10，安全领域标准度量）、分类准确率/Macro-F1（探针评估）、Selectivity（探针质量金标准，Hewitt）、跨层一致性（confusion/patience → crossing rate）、CoT 忠实度（Chen）

**数据集**：AdvBench（3/10）、JailbreakBench（2/10）、HarmBench（2/10）；推理安全用 HarmThoughts（56,931 句）；Llama 系列最常用模型族（4/10）

**统计**：单次运行为主（5/8 全文篇），领域对统计显著性要求偏低但 Arditi 用标准误差条、PABEE 报中位数（5 runs）

**对比对规模**：128（Arditi）-500（Zhou）对，不需要大规模标注

## 竞品 Claim 格局

- 安全信号预训练已存在，对齐仅建立"桥接关联"（Zhou ACL'24）
- Refusal 由单一方向调控，rank-1 编辑即可绕过（Arditi NeurIPS'24）
- CoT 忠实度仅 ~25%，RL 训练后趋平不再提升（Chen, Anthropic）
- 安全输出可掩盖不安全推理过程（HarmThoughts）
- 推理安全可在推理时 1-3 步恢复（SafeThink）

## 研究空白（高置信度）

1. **隐状态×推理模型**：Zhou 做隐状态不涉及推理模型；HarmThoughts 做推理链仅句子级文本；Chen 做推理模型仅文本忠实度→无人将隐状态探针用于推理安全轨迹的 token 级分析
2. **安全信号时序动态**：所有论文做 layer-wise（空间），无人追踪 token 生成过程中安全信号的时间演变
3. **跨层一致性用于安全选层**：Kaya/PABEE 建立 early exit 理论仅用于推理效率，未用于安全探针最优层选择
4. **控制任务用于安全探针**：Hewitt selectivity 仅应用于语言结构任务，未在安全分类场景验证探针是否真正捕获表征而非记忆
