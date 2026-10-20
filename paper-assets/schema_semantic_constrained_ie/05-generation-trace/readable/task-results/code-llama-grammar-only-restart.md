# code llama grammar only restart

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_grammar_only_restart_20260518T040332_result.json`
- **Structured JSON:** [`770d2c5ce7ab97781ee2.json`](../../sessions/77/770d2c5ce7ab97781ee2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常，行数在增长（0 → 2 → 3）。

**总结：**

- **根因**：之前的 12 docs 是跑的 `train.jsonl`（默认），不是 `test.jsonl`。train 集正好 12 docs，所以跑完就退出了
- **修复**：已备份 train 结果为 `ee_llama_wikievents_grammar_only_train_backup.jsonl`，重新用 `--data_path data/wikievents/test.jsonl` 启动全量 test 集（20 docs）
- **当前状态**：
  - GPU 1 占用 16470MiB，PID 525842
  - tmux session `llama_grammar_only` 运行中
  - 已处理 3/20 docs，持续增长
  - 按每 doc ~10-30s 估算，约 5-10 分钟完成全部 20 docs

---
