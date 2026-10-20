---
name: distilled-research
description: "多轮越狱检测与说服攻击领域的实验设计共识、基线选择、评估标准和研究空白"
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

## 评估指标共识

- **ASR（Attack Success Rate）是通用语言**：攻击论文报 higher_better，防御论文报 lower_better。25 篇中 20+ 篇使用。**支持度**：20/25，**置信度**：高
- **GPT-4/4o Judge 是攻击质量标准评判器**：1-5 或 1-10 Likert 评分。PAP/ActorAttack/Simple Adaptive 均采用。**支持度**：5/25，**置信度**：高
- **Safety-Utility Tradeoff 必须报告**：MT-Bench（3 篇）、AlpacaEval（1 篇）、GSM8K/MMLU/HumanEval（1 篇）。防御论文不报 utility 会被质疑。**支持度**：5/8 深度精读，**置信度**：高
- **检测论文额外指标**：F1/Precision/Recall（DeepContext、G-Guard、WildGuard）、推理延迟 ms（DeepContext）、Mean Turns to Detection（DeepContext）。**支持度**：3/8，**置信度**：中

## 基线选择共识

**攻击基线 Tier-1（必选）**：GCG（5 篇）、PAIR（4 篇）、PAP（3 篇）。**多轮必加**：Crescendo（2 篇）、ActorAttack（2 篇）。**支持度**：5/8，**置信度**：高
**防御/检测基线 Tier-1**：Llama Guard 系列（4 篇）、WildGuard（2 篇）、GPT-4 native（3 篇）。商业 API（Azure/AWS/GCP）在 DeepContext 中首次系统对比。**支持度**：4/8，**置信度**：高

## 数据集共识

- **HarmBench behaviors**（510 条）：最广泛采用的标准行为集，5 篇使用。**置信度**：高
- **AdvBench**（50 条）：轻量快速评估，3 篇使用，但规模偏小。**置信度**：高
- **JailbreakBench**：多轮评估新标准，3 篇使用。**置信度**：中
- **多轮专用数据集碎片化**：MHJ（BIID）、SafeMTData（ActorAttack）、SafeDialBench/CoSafe（BIID）各自为营，无统一标准。**置信度**：高

## 方法论趋势

**上升**：多轮攻击（ActorAttack/Crescendo/Deceptive Delight/Foot-in-Door/LRM，5 篇）；多轮检测（DeepContext/BIID/G-Guard/SafeDream，4 篇）；表征工程分析（RepEng/Linear Probes，2 篇）；说服理论迁移（PAP/Linear Probes，2 篇）。
**稳定**：LLM-based 安全分类器（WildGuard/ShieldGemma/Constitutional，3 篇）。
**消退**：纯梯度单轮攻击（GCG 系）——仍作基线但非前沿。

## 竞品 Claim 汇总

**直接竞争者（多轮检测）**：DeepContext（GRU 状态追踪，F1=0.84，19ms）、BIID（双向意图推理，近零 ASR，无需训练）、G-Guard（GNN 图建模，HarmBench accuracy=1.0）、SafeDream（世界模型，提前 1.06-1.20 轮检测）。
**基础设施**：WildGuard（三任务一体分类器，ASR 79.8%→2.4%）、HarmBench（标准化评估框架）。

## 共同局限（出现频率）

- 对新型攻击的泛化能力不足：4/8 篇提及
- Safety-Utility 权衡：3/8 篇（ActorAttack、HarmBench R2D2、BIID）
- 多轮评估标准碎片化：隐含于所有防御论文
- GPT-4 Judge 可靠性存疑：2 篇（Simple Adaptive、PAP）
- 长对话可扩展性：2 篇（G-Guard、DeepContext）

## 研究空白

- **无论文联合建模说服策略检测 + 越狱检测**：PAP 证明说服有效但仅做攻击；Linear Probes 证明表征可读但未接入防御。**置信度**：高
- **多轮检测缺乏 turn-level 说服特征**：DeepContext/BIID/G-Guard 均未利用说服理论信号。**置信度**：高
- **表征工程 + 实时检测未结合**：RepEng 论文为分析性工作，未产出部署方案。**置信度**：中
