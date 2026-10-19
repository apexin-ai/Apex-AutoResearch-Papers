# ops diagnose std baseline exit

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-std-baseline-exit_20260516T025134_result.json`
- **Structured JSON:** [`bd7e97916271d7b3f922.json`](../../sessions/bd/bd7e97916271d7b3f922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**退出原因**：进程在 libero_10 task_1 rollout step 161/520 处被外部 kill（无 traceback/OOM/error，日志直接截断）。

**已获数据**（3/4 suites 完成）：
| Suite | Avg SR |
|-------|--------|
| libero_spatial | 66.0% |
| libero_object | 67.8% |
| libero_goal | **76.4%** |
| libero_10 | 未完成 |

**已执行操作**：
- Registry notes 更新为完整的 per-task SR 数据和退出诊断
- Cron 不存在（已被之前清除），无需操作

---
