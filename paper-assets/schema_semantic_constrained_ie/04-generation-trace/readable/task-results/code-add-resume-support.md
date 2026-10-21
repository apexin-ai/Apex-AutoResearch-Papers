# code add resume support

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add_resume_support_20260513T224311_result.json`
- **Structured JSON:** [`8d26e1daf4005ffa4d02.json`](../../sessions/8d/8d26e1daf4005ffa4d02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全符合预期：

- **Resume 检测**: 正确识别 3 个已处理 sample
- **日志输出**: `Resuming from 3 processed samples, 2 remaining`
- **跳过逻辑**: 只跑了 sent3 和 sent4（编号 [4/5] 和 [5/5]）
- **输出文件**: 5 行（3 原有 + 2 新增）
- **完成信息**: `Done: 2 new samples, success=2, fail=0 (skipped 3 already processed)`

修改完成。变更摘要：

| 修改 | 位置 |
|------|------|
| `import os` | 第 16 行 |
| `load_processed_ids()` 函数 | 第 521 行，S2 模式特殊处理（检查 parsed_output 中有 relations） |
| `--resume` 参数 | 第 567 行 |
| 主循环改造 | 第 640-695 行：resume 时读已有 ID → 构建 todo 列表 → append 模式写文件 → 计数器含 skipped 偏移 |

---
