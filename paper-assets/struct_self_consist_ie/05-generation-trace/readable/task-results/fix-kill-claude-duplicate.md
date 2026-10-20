# fix kill claude duplicate

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_claude_duplicate_20260521T083641_result.json`
- **Structured JSON:** [`899c8a4165c4438b9d3e.json`](../../sessions/89/899c8a4165c4438b9d3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **PID 6307 / 6302**：已不存在（kill 时报 No such process），说明这两个重复进程之前已经自行退出或被其他方式终止。
- **PID 5791（--resume 进程）**：也不在了，没有任何 `run_frontier_sc` 进程存活。
- **checkpoint 进度**：`checkpoint.jsonl` 有 **381 行**。
- **日志**：`claude_sc_restart.log` 不存在。

所有进程均已停止，无存活的 `run_frontier_sc` 进程。如需恢复实验，需要重新启动带 `--resume` 的进程。

---
