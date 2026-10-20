# code wikievents llama crash fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_llama_crash_fix_20260517T181343_result.json`
- **Structured JSON:** [`1eb528c50d743ef013a6.json`](../../sessions/1e/1eb528c50d743ef013a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- **修复**：在 `run_constrained_extraction.py:968` 添加了 `if isinstance(parsed, list): parsed = {}`，位于 `record` 赋值和 `parsed.get` 调用之前
- **重启**：tmux session `llama_restart` 运行中，使用 `--resume` 从 doc 52 继续
- **输出**：已从 52 行增长到 55 行，推理正常进行
- **GPU 0**：16GB 显存占用，89% 利用率

---
