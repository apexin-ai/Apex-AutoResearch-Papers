# code wikievents fix 21461 type mask

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_fix_21461_type_mask_20260517T193816_result.json`
- **Structured JSON:** [`f0fc6ec31bc1e5525e7c.json`](../../sessions/f0/f0fc6ec31bc1e5525e7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。最终状态汇总：

| 文件 | westd-16980 | westd-21461 修复后 |
|---|---|---|
| `compiler/type_mask_processor.py` | 796 行 | 796 行 ✓ |
| `compiler/ontology_compiler.py` | 485 行 | 485 行 ✓ |
| `run_constrained_extraction.py` | 1008 行 | 1008 行 ✓ |
| `violation_checker_wikievents.py` | 396 行 | 396 行 ✓ |

`type_mask_processor.py`（原 0 字节）和 `violation_checker_wikievents.py`（差 2 行）已从 westd-16980 通过 SCP 修复到 westd-21461，其余文件一致。

---
