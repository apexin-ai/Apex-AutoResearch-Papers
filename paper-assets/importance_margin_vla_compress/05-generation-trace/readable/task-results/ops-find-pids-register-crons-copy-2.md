# ops find pids register crons

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_find_pids_register_crons_20260526T084257_result.json`
- **Structured JSON:** [`b4460a445e3478ca745d.json`](../../sessions/b4/b4460a445e3478ca745d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

| 实验 | 服务器 | PID | Cron Job | 状态 |
|------|--------|-----|----------|------|
| eval_openvla_attn_k09_goal_seed43_v4 | westd-27271 | 112477 | `574557a3` 每20min | RUNNING |
| eval_openvla_baseline_spatial_seed42_v4 | westd-27271 | 112404 | `44bba8c8` 每20min | RUNNING |
| eval_openvla_attn_k07_object_seed42 | westd-41074 | 415737 | `62db7f1f` 每20min | RUNNING |

Registry 已更新 PID，cron 监控已注册。进程结束后会自动检查日志并更新状态。注意 cron 为 session-only，退出 Claude 后失效。

---
