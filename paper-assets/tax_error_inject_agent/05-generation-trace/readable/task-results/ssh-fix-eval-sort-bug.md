# ssh fix eval sort bug

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-eval-sort-bug_20260514T142830_result.json`
- **Structured JSON:** [`10bff2150a08bc3cb678.json`](../../sessions/10/10bff2150a08bc3cb678.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，`bash -n` 语法检查通过。两处改动：

1. **`latest_run`**: `ls -d ... | sort | tail -1` → `ls -dt ... | head -1`（按修改时间取最新 run 目录）
2. **`final` checkpoint 排序**: `sort -t- -k2 -n` → `sort -V`（version sort，正确处理 checkpoint-10 vs checkpoint-2 等多位数编号）

---
