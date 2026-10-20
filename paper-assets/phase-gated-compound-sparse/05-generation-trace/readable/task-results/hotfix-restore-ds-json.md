# hotfix restore ds json

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_hotfix_restore_ds_json_20260515T053528_result.json`
- **Structured JSON:** [`75edb2e40e5ee6fa5289.json`](../../sessions/75/75edb2e40e5ee6fa5289.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**DeepSeek 数据已恢复。** 验证结果：

| 指标 | 修复前 | 修复后 | 状态 |
|------|--------|--------|------|
| JSON 大小 | 16,832 B | 29,019 B | ✓ |
| CSV 大小 | 2,504 B | 3,932 B | ✓ |
| deepseek 匹配 | 0 | 1 | ✓ |
| qwen 匹配 | 1 | 1 | ✓ |
| CSV 条件数 | 8 (Qwen only) | 14 (DS 6 + QW 8) | ✓ |

CSV 包含完整 14 条件：DeepSeek imp/rand × s015/s020/s025 (6条) + Qwen imp/rand × s015/s020/s025/s030 (8条)。LaTeX 表格也已同步输出两个模型的完整数据。

---
