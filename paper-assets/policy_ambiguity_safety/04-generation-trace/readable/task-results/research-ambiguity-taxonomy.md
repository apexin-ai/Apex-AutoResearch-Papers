# research ambiguity taxonomy

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ambiguity_taxonomy_20260520T071428_result.json`
- **Structured JSON:** [`ece75c35f83e00e3377d.json`](../../sessions/ec/ece75c35f83e00e3377d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已写入 `artifacts/ambiguity_taxonomy.md` 并注册。核心内容概览：

**理论基础** — 综合了三套分类体系：
- Massey et al. (2014) 的 6 类监管文本歧义分类
- DRIP-R (Borkakoty et al., 2025) 的 5 类零售策略歧义分类
- Li et al. (2024) 的 11 类 NLP 歧义分类
- 以 Chantree et al. (2006) 的 nocuous/innocuous 区分框架约束范围

**三类操作定义**：

| 类型 | 核心机制 | 预期违规率 | 预期频率 |
|---|---|---|---|
| Scopal | 量词/修饰语作用域交互，结构性歧义 | 最高 — LLM 默认 surface scope，无法自纠 | 最低 |
| Lexical | 策略术语多义，语义层面 | 最低 — LLM WSD 能力强，上下文可补偿 | 中等 |
| Incompleteness | 缺失条件/异常/定义，语用层面 | 中等 — LLM 填充合理但不一定符合作者意图 | 最高 |

**9 个 matched pairs**（每类 3 个）覆盖电商退货、航空改签、内容审核、金融服务、医疗数据、客服升级等真实策略场景。每个 pair 只在歧义点处不同，标注了具体歧义词/短语、可能解读、预期 agent 行为差异。

**标注指南** — 包含决策流程图（结构检查→词汇检查→完整性检查）和 IAA 协议（Cohen's kappa ≥ 0.7）。

---
