# analysis error cases

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-cases_20260522T120815_result.json`
- **Structured JSON:** [`c99dda3fadb4753f943c.json`](../../sessions/c9/c99dda3fadb4753f943c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。写入了 20 个案例到 `artifacts/_project/paper/error_analysis_cases.json`：

| 类别 | 数量 | 子类 |
|------|------|------|
| False Negatives | 7 | 1 constraint-blocked, 1 missing entity, 1 zero-output, 4 relation type confusion |
| False Positives | 7 | 5 wrong relation type, 2 hallucinated |
| CF Violations | 6 | entity type inconsistency across relations |

关键发现：
- **仅 1 个 FN 是约束阻断的**（P08-1105_sent4），其余 513 个是模型本身未生成——约束几乎不损失 recall
- FP 主要来源是 **Part-of ↔ Used-for 混淆**（schema 内自由度，约束无法纠正）和**语义层面的 hallucination**（如忽略否定语义）
- CF violations 多涉及**多义实体**（如 "approach" Generic/Method、"datasets" Material/Task），反映 entity type 在不同关系上下文中的歧义

---
