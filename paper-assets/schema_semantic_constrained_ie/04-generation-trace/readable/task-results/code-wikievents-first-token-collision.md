# code wikievents first token collision

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_first_token_collision_20260517T150923_result.json`
- **Structured JSON:** [`30da339de10212f1f853.json`](../../sessions/30/30da339de10212f1f853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 产出总结

### 1. `scripts/check_first_token_collision.py` — 独立分析脚本 ✓

### 2. Collision 报告

| 类别 | 总数 | 唯一首 token | 碰撞率 | 碰撞组 |
|------|------|-------------|--------|--------|
| Event types | 51 | 13 | **96.1%** | 11 groups |
| Roles | 80 | 68 | **31.2%** | 12 groups |
| Entity types | 26 | 26 | **0%** | 0 groups |

### 3. `ontology_compiler.py` 修改 ✓

- 添加了 `logging` 模块
- `compile_event_type_constraints()`: 检测碰撞组并 `logger.warning()`
- `compile_role_constraints()`: 检测碰撞组 + 进一步检测 **same-event collision**（同一事件类型内的角色碰撞）

### 4. 影响评估

- **Event type collision [HIGH but mitigated]**: 96.1% 碰撞，但 XGrammar EBNF enum 已约束合法事件类型字符串，first-token mask 仅为 soft filter，grammar 保证后续 token 正确。实际影响：mask 减少候选但无法单独区分同组事件类型。
- **Role collision [MEDIUM — 6 cases problematic]**: 6 个事件类型存在同事件内角色碰撞（`Place`/`PlaceOfEmployment`, `ConsumedThing`/`ConsumingEntity` 等），且 **grammar 没有 role enum**，mask 是唯一约束层。这些情况下 mask 无法区分碰撞角色。
- **Entity type collision [NONE]**: 26 个实体类型首 token 全部唯一，masking 完全有效。

---
