---
name: Schema-Semantic Constrained IE Research Patterns
description: 从10篇论文蒸馏的约束解码+结构化IE领域研究共识——实验设计、baseline选择、评估规范、方法论趋势
source_papers: 10 (8 deep + 2 abstract)
---

## 方法论趋势

**代码式 schema 表示取代 NL 描述**（3/10，GoLLIE/KnowCoder/CodeIE，置信度：高）
Python 类（继承、docstring、类型标注）编码 IE schema。GoLLIE 用 docstring 编码标注指南，KnowCoder 用类继承映射 30K+ Wikidata 类型，CodeIE 证明 Code-LLM 天然适配结构化输出。趋势：2023→2024 从 prompt 级到预训练级深化。

**语法约束解码从 SQL 扩展到通用结构化生成**（5/10，PICARD→GCD→IterGen/CRANE/XGrammar，置信度：高）
演进轨迹：PICARD(2021)SQL 增量解析→GCD(2023)CFG 通用框架→IterGen(2025)回溯纠错→CRANE(2025)理论证明约束损害推理+语法增强恢复→XGrammar(2025)系统级近零开销。趋势从纯语法→语义感知→效率工程。

**无微调推理时方法占半壁江山**（4/8深读，GCD/CodeIE/IterGen/CRANE，置信度：高）
few-shot + constrained decoding 与微调路线并列。CRANE 提供理论基础：有限语法将 LLM 表达限制在 TC0 复杂度类，语法增强可恢复。

**约束-推理 tradeoff 成为核心议题**（3/10，CRANE/IterGen/BoostCD，置信度：中）
CRANE 理论证明严格约束损害推理，IterGen 用回溯缓解，BoostCD 用集成融合。这揭示约束解码不是免费午餐——需要机制设计来保护语义质量。

## 实验设计共识

**必选 Baseline**：GenIE（closed IE 标杆，3篇）、UIE/InstructUIE（通用IE，3篇）、Outlines/SGLang（约束解码系统，3篇）、LLaMA/CodeLLaMA（开源LLM，3篇）

**必选数据集**：ACE05 NER+RE+Event（4篇）、CoNLL03 NER（3篇）、REBEL/Wiki-cIE closed IE（3篇）。约束解码系统论文额外需 JSON/SQL/XML 生成基准。

**核心指标**：IE 任务以 micro-F1 为主（8/10），closed IE 加 macro-F1 反映长尾。约束解码论文必报 parse rate/validity rate（CRANE 100%，IterGen 验证）。系统论文报延迟（XGrammar per-token µs）。

**消融必做维度**：①约束 vs 无约束效果对比（4/10）②核心组件逐步叠加/去除（GoLLIE p-value, XGrammar 248.6x cache 贡献）③模型尺寸 scaling（3/10）

## 训练配方共识

**LoRA/QLoRA 是 LLM-based IE 微调标配**（GoLLIE QLoRA 3e-4, KnowCoder LoRA rank=32 3e-4，置信度：高）
lr=3e-4 + cosine scheduler 是共识。A100 80GB 标配硬件。

**XGrammar 的系统设计启示**：99% token 为 context-independent 可预计算，仅<1% 需运行时检查。160MB→0.46MB 内存压缩。GPU-CPU 重叠实现零开销。

## 竞品 Claim 与研究空白

**竞品**：KnowCoder（30K+类型 schema 库+两阶段训练），BoostCD（约束/无约束互补 boosting +17 F1）

**共同局限**（≥2篇）：①闭源 API 不兼容（GCD, CRANE, CodeIE）②约束解码延迟（GCD 0.05-0.5s/token, IterGen 回溯开销, BoostCD 3次调用）③语法/schema 人工设计成本（PICARD, GCD）④训练数据质量（BoostCD 合成数据, KnowCoder 1.5B token 自动构造）

**研究空白**：①代码 schema 表示 + 语法约束解码两条路线未融合——无论文同时使用 ②语义约束（超越语法合规）系统性方案缺失——仅 CRANE/IterGen 初步触及 ③动态 schema 适应（推理时 schema 变化）无方案 ④约束解码对 IE 特定任务（事件抽取、关系抽取）的针对性设计不足
