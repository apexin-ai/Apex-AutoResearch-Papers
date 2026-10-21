# code fix s2 pass2 semantic

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_s2_pass2_semantic_20260513T213645_result.json`
- **Structured JSON:** [`faf21d9e15b9b3f3e9fd.json`](../../sessions/fa/faf21d9e15b9b3f3e9fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**D/R violations: 0/8 (0.0%)**

Bug 修复成功。总结：

### 发现的 Bug（共 2 个）

**Bug 1**: `_mask_head_type()` / `_mask_tail_type()` 从不查 EntityRegistry，只走 D/R 约束路径。同时 `_RE_TAIL_TEXT_VAL` 正则缺失导致 `current_tail_text` 永远为 None。（上一轮已修复）

**Bug 2**（本轮定位）: `PositionDetector.detect()` 用 `rfind('{"head"')` 定位 relation 对象起始位置，但 XGrammar 生成的 JSON 是 pretty-printed 的（`{\n      "head"`），`rfind` 匹配不到。导致 `current_relation_type`/`current_head_type` 始终为 None，D/R 约束永远不会被应用。

**修复**: 将 `rfind` 替换为正则 `_RE_REL_START = re.compile(r'\{\s*"head"')`，用 `finditer` 取最后一个匹配。

### 验证结果
- 3 样本 dry-run: 3/3 成功，8 个 relation 全部通过 D/R 检查
- D/R violation rate: **0.0000**（从 25% 降为 0%）
- 剩余 1 个 cross-field consistency violation 不在本次修复范围内

---
