# analysis oov relation replacement cases

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oov_relation_replacement_cases_20260516T181814_result.json`
- **Structured JSON:** [`af291ff565fa028dae72.json`](../../sessions/af/af291ff565fa028dae72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/oov_replacement_cases.md`。

关键发现：
- DocRED unconstrained 输出中有 **5,261 个 OOV 关系名**（2,038 种），其中 4,357 个被 grammar 替换为 in-vocab 关系名
- **36.6% 的替换引入了新的 DR violation**
- 5 个典型案例覆盖三种失败模式：token 前缀碰撞（"opponent"→"operator"）、ontology 缺失（"population"→"has part"）、静默语义错误（"available on"→"operator" 通过 DR 检查但语义反转）

---
