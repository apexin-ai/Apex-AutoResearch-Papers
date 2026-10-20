# research m4 smoke test

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_m4-smoke-test_20260513T204229_result.json`
- **Structured JSON:** [`6dc87ef3b5c6b40c024d.json`](../../sessions/6d/6dc87ef3b5c6b40c024d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 7/7 测试通过：**

| 测试 | 状态 |
|------|------|
| test_gqa_grouping | PASSED |
| test_head_selection | PASSED |
| test_kv_eviction | PASSED |
| test_kv_bos_protection | PASSED |
| test_head_mask_kv_group_skip | PASSED |
| test_compound_forward | PASSED |
| test_head_mask_effect | PASSED |

注意：`compound/` 目录原先未同步到服务器，已手动部署。`test_head_mask_effect` 中的动态类创建模式（`type()` + lambda `__init__`）在服务器 Python 版本上不兼容，已改为标准类定义。本地 artifacts 中的同一处也应同步修复。

---
