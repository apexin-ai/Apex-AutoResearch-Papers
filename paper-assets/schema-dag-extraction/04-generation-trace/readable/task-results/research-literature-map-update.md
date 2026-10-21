# research literature map update

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-map-update_20260515T030636_result.json`
- **Structured JSON:** [`bb7d2ca4c79236e57f6e.json`](../../sessions/bb/bb7d2ca4c79236e57f6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入。总结：

**收录 25 篇论文**，分为 direct-competitor (8)、method-component (8)、background (5)、evaluation (2)、survey (2)。

**Novelty 威胁评估：**

| 维度 | 状态 | 说明 |
|------|------|------|
| Type count vs type confusability 解耦 | ✅ 安全 | 无先行工作。IEPILE 的 hard negative 最近但是 training-time，Familiarity 是 evaluation-time |
| Schema DAG 分解 | ✅ 安全 | LLM-PEE 做 similarity partitioning，非 confusability-aware DAG |
| Lost in the Middle → IE | ✅ 机会 | 无人将此应用到 IE task |
| Multi-channel degradation model | ✅ 安全 | 无人提出 count + confusability + context 的形式化模型 |

**⚠️ 唯一中等风险：CROSSAGENTIE** (ACL 2025 Findings) 的 cross-type debate 明确处理 entity-label conflict。需在论文中清晰区分：我们是 proactive decomposition（预防混淆），他们是 reactive debate（事后纠错）。

**必须对比的 baselines：** LLM-PEE、PARSE。建议在 related work 中讨论 CROSSAGENTIE、DEE、SPT、DLISC。

---
