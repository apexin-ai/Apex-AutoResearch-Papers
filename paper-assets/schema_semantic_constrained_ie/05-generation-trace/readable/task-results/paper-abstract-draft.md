# paper abstract draft

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_abstract_draft_20260514T061835_result.json`
- **Structured JSON:** [`9c5e829b4290f5c7a93a.json`](../../sessions/9c/9c5e829b4290f5c7a93a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 不在可用工具列表中。abstract 已写入：

**文件**: `artifacts/_project/paper/abstract.tex`
**字数**: ~231 words（在 250 上限内）

**结构覆盖**：
1. **Problem** — 量化 SciERC 15.4% / DocRED 18.7% 的 DR violation，点出 tight-constraint 关系集中现象
2. **Prompt insufficiency** — SciERC ↓62% vs DocRED ↓31%，Evaluate-for 恶化 +5.8pp
3. **Approach** — 双层约束：grammar layer (XGrammar) + semantic layer (TypeConstraintProcessor)，bitwise AND 组合
4. **Results** — DR 15.37%→0.93% (↓94%)，ET/RV 完全消除，F1 无损；CF violation 0.08%→9.9% 作为 open challenge；DocRED 用 `\placeholder{}` 占位

---
