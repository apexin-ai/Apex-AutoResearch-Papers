# ops cleanup zombie irt processes

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_zombie_irt_processes_20260517T043606_result.json`
- **Structured JSON:** [`ccf8b40c0c3cc53dd10a.json`](../../sessions/cc/ccf8b40c0c3cc53dd10a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。已 kill 11 个 May 16 旧 IRT 进程（含 7 个 zombie `&lt;defunct>`）。

剩余进程均为 May 17 活跃任务（signals 计算、tmux session），无 IRT/cmdstan zombie 残留。PID 929599/929719 未受影响（它们未出现在 IRT grep 结果中，应为其他类型进程）。

---
