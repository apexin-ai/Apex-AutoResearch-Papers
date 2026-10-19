# check v5 status urgent

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v5_status_urgent_20260512T211406_result.json`
- **Structured JSON:** [`c3b8194feee510215bf8.json`](../../sessions/c3/c3b8194feee510215bf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v5 收集状态汇总

| 项目 | 结果 |
|------|------|
| **v5 进程** | **已结束**（无 collect_trajectories 进程在运行） |
| **cuda0 轨迹** | 250 条（成功 94，失败 156），3.9MB，最后修改 May 13 05:05 |
| **cuda1 轨迹** | 250 条（成功 93，失败 157），3.9MB，最后修改 May 13 05:03 |
| **合计** | 500 条，成功 187（37.4%），失败 313（62.6%） |
| **GPU 状态** | GPU 0/1/2/4 空闲（0 MiB）；**GPU 3 占用 22GB/15%，GPU 5 占用 9.3GB/99%**（有其他任务在跑） |

v5 收集已完成。GPU 0/1/2/4 空闲可用，但 GPU 3 和 5 被其他进程占用。

---
