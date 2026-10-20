# code w1 cf registry consistent fallback

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w1_cf_registry_consistent_fallback_20260515T095943_result.json`
- **Structured JSON:** [`26053a6eda02007f141f.json`](../../sessions/26/26053a6eda02007f141f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，**0 CF violations**（10 样本，21 relations）。

---

## 修改总结

**文件**: `/root/schema_semantic_constrained_ie/compiler/type_mask_processor.py`（435 → 462 行，+27 行）

### Diff 概要

| 位置 | 修改 |
|------|------|
| L205 | `__init__` 新增 `self._cf_fallback_count = 0` |
| L291-292 | `_mask_head_type` docstring: "use D/R constraint" → "force registered type (W1: registry consistency > DR compliance)" |
| L307-316 | `_mask_head_type` 新增 `else` 分支：当 `actual_type ∉ allowed_dr` 时，强制 `_apply_type_mask(logits, {actual_type})`，计数并 debug 日志 |
| L327-328 | `_mask_tail_type` docstring: 同上 |
| L349-359 | `_mask_tail_type` 新增 `else` 分支：同理，当 tail entity 注册类型与 `range(r, head_type)` 冲突时强制注册类型 |
| L423-424 | `reset()` 新增 CF fallback 日志输出 |
| L426 | `reset()` 新增 `self._cf_fallback_count = 0` |

### 逻辑变更

**修改前**: entity 注册类型 ∉ dom(r)/range(r) → fall through 到 DR mask → 模型被迫选 dom(r) 中的类型 → 同一 entity 在不同 relation 中被分配不同类型 → CF violation

**修改后**: entity 注册类型 ∉ dom(r)/range(r) → **强制使用注册类型**（`_apply_type_mask(logits, {actual_type})`）→ 类型跨 relation 一致 → CF violation 消除

安全性：`_apply_type_mask` 内部有 grammar-first safety check，若注册类型被 grammar 层 mask 会自动 fallback 到无约束状态。

### Dry-run 结果

- SciERC 10 样本，**0 crash，0 CF violations**，21 relations 正常输出
- CF fallback 未触发（SciERC 约束松散，预期行为）
- DocRED（约束紧密）预期会触发 CF fallback，需全量实验验证

---
