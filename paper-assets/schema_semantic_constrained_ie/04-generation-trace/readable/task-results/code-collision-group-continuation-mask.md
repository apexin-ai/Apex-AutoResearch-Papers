# code collision group continuation mask

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_collision_group_continuation_mask_20260518T025425_result.json`
- **Structured JSON:** [`3d9f5df0bc45e7445e72.json`](../../sessions/3d/3d9f5df0bc45e7445e72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。

**结果**：

| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| AC violations | ~16.6% | **0.0%** |
| 行数 | 812 | 913 (+101) |

**修改内容**（`compiler/type_mask_processor.py`）：

1. `GenerationState` 新增 3 个字段：`in_entity_type_value`, `entity_type_value_start_len`, `entity_type_allowed_types`，用于 entity type 值的续写追踪
2. `_build_entity_type_collision_groups()` — 初始化时检测共享首 token 的 entity type 碰撞组（Mistral 检测到 4 组：A→{ABS,AML}, B→{BAL,BOD}, P→{PLA,PTH}, S→{SEN,SID,SIDE}）
3. `_apply_entity_type_continuation_mask()` — 碰撞组首 token 生成后，在第二 token 步基于已生成的 partial text 阻塞不可达 disallowed type 的续写 token
4. `__call__` 修改：ARGUMENT_ENTITY_TYPE 位置检测时设置续写状态；后续 token 步拦截做 continuation mask；正常退出续写追踪
5. 对无碰撞 tokenizer（Qwen/Llama），`_entity_type_collision_groups` 为空，新逻辑完全不触发

---
