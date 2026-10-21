# code fisher source tag

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fisher-source-tag_20260515T215254_result.json`
- **Structured JSON:** [`46e7ab791a168fbc664e.json`](../../sessions/46/46e7ab791a168fbc664e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。JSON 输出包含 `"source": "manual_input"`。

修改总结：
- `run_manual`：捕获 `print_comparison` 返回值，添加 `"source": "manual_input"`，输出 JSON
- `run_from_files`：每个结果添加 `"source": "eval_json"`

脚本不写 JSON 文件，只输出到 stdout，source 字段已包含在输出中。

---
