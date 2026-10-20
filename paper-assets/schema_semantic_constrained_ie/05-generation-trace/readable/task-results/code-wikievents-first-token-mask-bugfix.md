# code wikievents first token mask bugfix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_first_token_mask_bugfix_20260517T153956_result.json`
- **Structured JSON:** [`08b406ccb6b2d52d5caf.json`](../../sessions/08/08b406ccb6b2d52d5caf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Import 验证通过。

### 修复总结

**修改文件**: `compiler/type_mask_processor.py`

**修改了 2 个函数**:

1. **`_apply_type_mask`** (line 478-481) — RE 路径使用（`_mask_entity_type`, `_mask_head_type`, `_mask_tail_type`, `_mask_argument_entity_type`）
   - 新增 `allowed_first_tokens` 集合，disallowed 列表增加 `tid not in allowed_first_tokens` 条件

2. **`_apply_first_token_mask`** (line 496-499) — EE 路径使用（`_mask_event_type`, `_mask_argument_role`）
   - 新增 `allowed_tokens` 集合，disallowed 列表增加 `tid not in allowed_tokens` 条件

**RE 路径是否有同样的 bug**: **是**。`_apply_type_mask` 使用完全相同的有 bug 的模式（`if etype not in allowed_types` 不检查 token 是否被其他 allowed type 共享）。虽然当前 RE 数据集（SciERC/DocRED）的 entity type first tokens 恰好唯一没触发，但逻辑上存在相同的 collision 风险，已一并修复。

---
