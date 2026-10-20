# code collision group fix v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_collision_group_fix_v2_20260518T033316_result.json`
- **Structured JSON:** [`c67b8f2df38306c59da2.json`](../../sessions/c6/c67b8f2df38306c59da2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-16980 确认 938 行一致。

### 结果汇总

**新增函数/方法（4 个）：**
- `_build_entity_type_collision_groups()` (L412) — 检测共享首 token 的 entity type 碰撞组
- `_build_entity_type_full_tokens()` (L419) — 预计算碰撞组成员的完整 token 序列
- `_needs_entity_type_continuation()` (L433) — 判断 allowed_types 是否部分重叠碰撞组
- `_apply_entity_type_continuation_mask()` (L442) — 在第 2+ token 步阻止通向非法 entity type 的 token

**新增状态字段（3 个）：**
- `GenerationState.in_entity_type_value` / `entity_type_value_start_len` / `entity_type_allowed_types`

**`__call__` 修改点（5 处）：**
- L596: entity type continuation 检查（与 role continuation 并列）
- L630: ARGUMENT_ROLE 位置重置 entity type 状态
- L647: ARGUMENT_ENTITY_TYPE 位置启用 continuation tracking
- L656: else 分支重置
- L660: exception handler 重置

**修改后总行数：** 938（原 816，+122 行）
**import 测试：** 通过
**rsync：** westd-21461 → westd-16980 成功，行数一致
**GPU dry-run：** 未执行（两卡均在使用：GPU0 63% / GPU1 87%）

---
