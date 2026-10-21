# fix m16 seed44 cron pid

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_m16_seed44_cron_pid_20260519T045121_result.json`
- **Structured JSON:** [`567ee2bd4552362a220a.json`](../../sessions/56/567ee2bd4552362a220a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| 项目 | 结果 |
|------|------|
| **主进程 PID** | 462076 |
| **训练进度** | step 12200/100000，loss ~0.08-0.11，lr 9.7e-5，sps 5.0 |
| **Registry** | 已从 DONE(failed) 恢复为 RUNNING，PID/server/log_path 已更新 |
| **旧 cron** | 已不存在（之前已被清理） |
| **新 cron** | 已注册（每 2 分钟检查 PID 462076 存活 + 日志进度），session 级别，7 天自动过期 |

---
