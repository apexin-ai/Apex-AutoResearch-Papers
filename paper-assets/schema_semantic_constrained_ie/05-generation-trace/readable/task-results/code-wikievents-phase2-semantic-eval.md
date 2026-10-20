# code wikievents phase2 semantic eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_phase2_semantic_eval_20260517T145310_result.json`
- **Structured JSON:** [`299d1cccf516aee549ed.json`](../../sessions/29/299d1cccf516aee549ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's the summary:

---

## 改动总结

### 1. `compiler/ontology_compiler.py` — 扩展 ConstraintSpec 支持 EE

- `ConstraintSpec` 新增字段: `event_types`, `all_roles`, `argument_constraints`, `event_type_first_token`, `role_first_token` 等
- 新增属性 `has_event_constraints` 自动检测 RE/EE 模式
- 新增方法 `get_valid_roles(event_type)`, `get_valid_entity_types_for_role(event_type, role)`
- `_build_spec()` 自动加载 `event_types` + `argument_constraints`（如果 ontology JSON 中存在）
- 新增 `compile_event_type_constraints()`, `compile_role_constraints()`, `compile_event_json_schema()`
- RE 功能完全不受影响（24 个现有测试全部通过）

### 2. `compiler/type_mask_processor.py` — Semantic Layer EE 支持

- `FieldPosition` 新增: `EVENT_TYPE`, `ARGUMENT_ROLE`, `ARGUMENT_ENTITY_TYPE`
- `GenerationState` 新增: `current_event_type`, `current_argument_role`, `in_events_section`
- `PositionDetector` 新增 regex: 检测 `"event_type"`, `"role"`, `"entity_type"` 位置
- 新增 mask 函数: `_mask_event_type()`, `_mask_argument_role()`, `_mask_argument_entity_type()`
- 新增通用 `_apply_first_token_mask()` 用于 event type/role 的 first-token masking
- `__call__()` 自动处理 EE 位置类型

### 3. `violation_checker_wikievents.py` — 5 类 violation 检查

| 缩写 | 检测内容 | 分母 |
|------|---------|------|
| ET | entity type 不在 ontology | entities |
| EV | event_type 不在 ontology | events |
| RoV | role 不在 event_type 允许列表 | arguments |
| AC | (event_type, role) 的 entity_type 不在约束 | arguments |
| CF | 同一 entity 跨 event type 不一致 | entities |

### 4. `eval_event_extraction.py` — Event F1 评估

- Trigger Identification F1: `(trigger_text, event_type)` 匹配
- Argument Extraction F1: `(trigger_text, event_type, arg_text, role)` 匹配
- Entity F1: `(entity_text, entity_type)` 匹配
- Micro P/R/F1 聚合

### 验证结果

- 所有 24 个现有 RE 单元测试通过
- 4 个模块 import 验证全部通过
- EE PositionDetector 5 个功能测试通过
- Violation checker 合成数据验证通过（5 类 violation 均正确检出）
- Eval 脚本合成数据验证通过（Entity/Trigger/Argument F1 计算正确）

---
