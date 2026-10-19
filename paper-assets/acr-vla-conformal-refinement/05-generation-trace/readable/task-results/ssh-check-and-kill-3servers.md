# ssh check and kill 3servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-and-kill-3servers_20260517T115858_result.json`
- **Structured JSON:** [`5943544d6577cf414845.json`](../../sessions/59/5943544d6577cf414845.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== bjb2-28827 cuda:2 PID 401104 ===
判断：保留
证据：运行 20:55，< 30 分钟。日志显示正在初始化（已加载 CRM 337,438 params，已加载 10 tasks），尚未进入 rollout 阶段，属正常启动耗时。

=== bjb1-18228 cuda:1 PID 617632 ===
判断：保留
证据：运行 19:24，< 30 分钟。日志显示正在初始化（已加载 CRM 327,198 params，已加载 10 tasks），尚未进入 rollout 阶段，属正常启动耗时。

=== bjb2-40593 cuda:0 PID 388460 ===
判断：已 kill（Director 确认）
验证：进程已终止（PROCESS_GONE）。cuda:0 已释放 — 0MiB / 24564MiB，无运行进程。
```

---
