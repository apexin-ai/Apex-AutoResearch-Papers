# code fix llama grammar only dataset

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_llama_grammar_only_dataset_20260518T040929_result.json`
- **Structured JSON:** [`3a854d7bd721fc588908.json`](../../sessions/3a/3a854d7bd721fc588908.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已修复并确认运行正常。

**总结：**
- **问题**：`test.jsonl` 只有 20 docs，完整的 246 docs test 集在 `all.jsonl`
- **修复**：杀掉旧进程，用 `--data_path data/wikievents/all.jsonl` 重启
- **确认**：日志显示 `Samples: 246`，GPU 1 正在使用（87%, 16GB），Llama grammar_only 正在跑完整 246 docs

---
