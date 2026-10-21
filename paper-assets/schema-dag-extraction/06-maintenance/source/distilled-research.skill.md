---
name: distilled-research
description: "Schema-guided zero-shot IE 领域研究 patterns：baseline 格局、指标/数据集共识、方法论趋势、竞品 claim、研究空白"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [crossagentie-2025, zeroner-2025, kggen-2025, gliner2-2025, code4uie-2024, iepile-2024, lost-in-middle-2024, self-improve-ner-2024, self-prompting-re-2024, cmas-ner-2025, nuner-2024, familiarity-2025, gliner-2024, guidex-2025, uniner-2024, knowcoder-2024, slot-2025, godey-anisotropy-inherent-2024, llm-pee-2025, parse-2025, dee-2024, dlisc-2025, spt-2025, gollie-2024, llm4ie-survey-2024]
  last_distilled: "2026-05-22T00:00:00Z"
---

## Baseline 格局

**必比 baseline**（7/25，高）：ChatGPT/GPT-3.5 是 zero-shot 通用参照线；InstructUIE-11B 是 supervised 参照线。来源：UniversalNER, GLiNER, GoLLIE。

**三角互引**（4/8 深读，高）：UniversalNER、GLiNER、GoLLIE 已形成高频互引格局，新论文需同时对比。来源：ZeroNER, GLiNER2, CMAS-NER。

**Encoder vs LLM 分野**：encoder 路线（GLiNER 0.3B, ZeroNER 110M）强调效率；LLM 路线（GoLLIE 7-34B, UniNER 7-13B）强调泛化。OOD NER F1 差距已 <3 点。（3/8，高）

## 指标与数据集共识

**指标**：span-level micro-F1 exact match 是硬通货（25/25）。效率指标（latency）在 industry track 上升（PARSE, GLiNER2, SLOT）。（高）

**核心 benchmark**：CrossNER 5 domains（7/8）、CoNLL03（6/8）、OntoNotes（5/8）、MIT Movie/Restaurant（4/8）。生物医学用 GENIA/BC5CDR。（高）

**评估警告**：soft zero-shot 存在类型泄漏。ZeroNER 和 Familiarity 证明 GLiNER 训练集与 benchmark 的 entity type overlap 导致 F1 虚高。Hard zero-shot 更可靠。（2/25，中）

## 方法论趋势

**上升趋势**（高）：
1. **Schema 即接口**（9/25）：PARSE 优化 JSON schema、GoLLIE 编码 Python class、KnowCoder code pretraining、SPT tool-calling。
2. **LLM→小模型蒸馏**（6/25）：ChatGPT/Llama 标注→训练 encoder。Pile 语料是共识数据源。
3. **多 Agent 协作**（3/25）：辩论/分工做 IE（CrossAgentIE, CMAS-NER, LLM-PEE）。

**关键设计**：
- **负采样**：frequency-based 是性能关键（UniNER +21.9 F1, GLiNER 50% ratio）。（3/8，高）
- **训练正则化**：entity type dropping + order shuffling 防记忆 schema（GoLLIE, GLiNER）。（2/8，中）
- **硬件**：单卡 A100 标准配置；encoder 训练 5-54h，LLM 依赖 API。（5/8，高）

## 竞品 Claim 图谱

| 竞品 | 核心 claim | 空白 |
|------|-----------|------|
| PARSE | JSON schema 可被 LLM 迭代优化 | 无 DAG 结构 |
| GoLLIE | Guidelines 编码为 Python class | 类型间无依赖建模 |
| GLiNER2 | Schema-driven encoder 统一多任务 | 层次抽取无评估 |
| KnowCoder | 30K+ 类型 code pretraining | 成本极高 |
| SPT | Schema as parameterized tools | tool-calling 限制灵活性 |

## 研究空白

1. **层次/DAG schema 建模**（0/25，高）：所有竞品操作扁平 schema，类型间依赖关系未开发。
2. **Schema 演化**（1/25 提及，中）：PARSE 明确列为局限，无论文处理 schema 版本迁移。
3. **跨任务 schema 统一**（1/25，中）：NER→RE→EE 的 schema 依赖链无人建模。

## 共同局限

- LLM 质量/幻觉依赖（6/25）
- Schema/guideline 质量敏感（3/8 深读）
- 多语言几乎空白（仅 GLiNER 尝试，效果差）
- 嵌套实体支持稀缺（仅 GLiNER2 提及）
