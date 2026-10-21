# restart frontier sc claude

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_restart_frontier_sc_claude_20260521T073016_result.json`
- **Structured JSON:** [`0654af49fc089a20c42f.json`](../../sessions/06/0654af49fc089a20c42f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**重要发现 — 不需要重启，情况与预期不同：**

| 指标 | 值 |
|------|-----|
| 运行中的 Claude SC 进程 | **2 个**（PID 5791 带 `--resume`，PID 6307 由 nohup 启动） |
| checkpoint 总行数 | 251 |
| 唯一实例数 | **146** |
| 重复条目 | **105**（两个进程同时处理相同实例导致） |
| 实例范围 | 0–145（已完成 146 个） |
| 剩余 | **54 个**（146–199） |

**问题：** PID 6302（bash wrapper）并没有死，它和子进程 PID 6307 都还在运行。加上 PID 5791，两个 Python 进程在同时跑同一个任务，导致 105 条重复结果和 API 额度浪费。

**建议操作：**
1. Kill 其中一个进程（建议保留 PID 5791，它有 `--resume` 标志）
2. 让存活进程跑完剩余 54 个实例
3. 不需要重启新进程

是否要 kill PID 6307（以及其 wrapper PID 6302）？

---
