# ops check v4 cuda1 result

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-v4-cuda1-result_20260512T163117_result.json`
- **Structured JSON:** [`e434b053a6b3e5f35bf7.json`](../../sessions/e4/e434b053a6b3e5f35bf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**datagen_traj_v4_cuda1 结果：失败**

| 指标 | 值 |
|------|-----|
| 计划轨迹数 | 250 |
| 实际完成 | 1 |
| 成功/失败 | 0 / 1 |
| 文件大小 | 19KB (1 行) |
| Boundary 问题 | N/A（仅 1 条，无需检查） |

**失败原因**：进程 (PID 253522) 在完成第 1 条轨迹后静默退出。日志仅 11 行，无任何 error/traceback/OOM 记录。无 stderr 日志文件。可能原因：未捕获的异常且 stderr 未重定向到日志文件，或被系统 OOM killer 杀死。

**建议**：重跑时将 stderr 也重定向到日志 (`2>&1`)，以便定位崩溃原因。

---
