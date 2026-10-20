# research pair based impl plan

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pair_based_impl_plan_20260515T141200_result.json`
- **Structured JSON:** [`300ba6d299c50861f508.json`](../../sessions/30/300ba6d299c50861f508.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，实现方案已写入 `artifacts/pair_based_enforcement_plan.md`。

核心发现与方案摘要：

**关键发现**：JSON schema 生成顺序是 `head → tail → type → head_type → tail_type`，relation type 在 entity types 之前生成——不需要 schema reorder。

**三处改动点**：

1. **P0 `_mask_head_type` pair-based**（L321, 最高收益）：当前用 `valid_head_types()`（独立 dom 投影），改为当 tail entity type 从 registry 已知时用 `valid_head_types_for_tail(tail_type)`。`RelationConstraint` 已有此方法但从未被调用。

2. **P1 数据结构**：`RelationConstraint` 添加 `_valid_pair_set` (frozenset) + `is_valid_pair()` 方法实现 O(1) pair 查询。`GenerationState` 新增 `current_tail_type`，`PositionDetector` 新增 tail_type 值提取 regex。

3. **P2 `_mask_relation_type`（新增）**：在 `RELATION_TYPE` 位置基于 entity registry 的 head/tail types 过滤 relation types。SciERC 可直接启用；DocRED 因 P-code first token 全部相同需跳过或用 human-readable names。

**CF fallback 交互**：CF 一致性优先级不变（> pair 约束），新增 `pair_cf_conflict_count` 统计。

**改动量**：~98 行，涉及 `ontology_compiler.py` (+10行) 和 `type_mask_processor.py` (+88行)。

---
