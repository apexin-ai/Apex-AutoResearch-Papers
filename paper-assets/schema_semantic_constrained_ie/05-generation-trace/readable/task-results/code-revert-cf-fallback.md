# code revert cf fallback

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_revert_cf_fallback_20260515T152255_result.json`
- **Structured JSON:** [`2ab9702d1874c20ad11f.json`](../../sessions/2a/2ab9702d1874c20ad11f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

回退完成。

**1. 回退方式**：项目不是 git 仓库，无法用 `git checkout`。使用 `compiler/type_mask_processor.py.bak`（May 14 11:06，CF fallback 引入前的版本）覆盖恢复。

**2. 差异确认**（CF fallback 版本 → 原始版本）：
- 行数：490 → 399（删除 91 行 CF fallback 代码）
- 大小：20195 → 15666 bytes
- CF fallback 标记位置（已删除）：
  - `self._cf_fallback_count = 0` (init, line 228)
  - 两处 `self._cf_fallback_count += 1`（lines 332, 376，对应 `_mask_head_type` 和 `_mask_tail_type` 中放松 DR 的分支）
  - logger 计数报告 (lines 451-454)

**3. 验证结果**：
- `grep cf_fallback` → 无匹配
- `grep registry_type` → 无匹配
- 核心 DR 逻辑完整：`valid_tail_types_for_head` 在 line 319，`_apply_type_mask` 在 line 336
- `from compiler.type_mask_processor import TypeConstraintProcessor` → `Import OK`
- `__pycache__` 已清除避免加载旧字节码

**4. 产物**：
- `compiler/type_mask_processor.py` (15666 bytes, 23:24 写入) — 已回退
- `compiler/type_mask_processor_cf_fallback.py` (20195 bytes) — CF fallback 版本备份
- `compiler/type_mask_processor.py.bak` (15666 bytes) — 原始备份（保留）

未触碰 `scripts/train_lora_scierc.py` 及任何训练相关文件。

---
