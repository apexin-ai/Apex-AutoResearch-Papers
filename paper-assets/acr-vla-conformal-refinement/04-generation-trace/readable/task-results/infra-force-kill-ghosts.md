# infra force kill ghosts

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_force-kill-ghosts_20260513T161822_result.json`
- **Structured JSON:** [`40381c18dbdc9ba40787.json`](../../sessions/40/40381c18dbdc9ba40787.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 tmux sessions（`tmux list-sessions` 无输出）。

### 总结

| 项目 | 结果 |
|------|------|
| PID 43814, 57633, 57711, 57851 | **已不存在**（可能之前已被 kill 或自行退出） |
| tmux sessions | 无活跃 session，清理命令已执行 |
| GPU 0 | **仍有 3503 MiB 被占用** — PID 87385 正在跑 `evaluate.py --mode vla_only --benchmark spatial` |

PID 87385 是一个正在进行的 eval 任务，不在原始 kill 列表中。是否需要也 kill 掉它？

---
