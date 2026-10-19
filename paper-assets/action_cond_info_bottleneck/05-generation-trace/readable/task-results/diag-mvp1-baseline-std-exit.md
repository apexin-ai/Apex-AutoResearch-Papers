# diag mvp1 baseline std exit

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp1_baseline_std_exit_20260515T213241_result.json`
- **Structured JSON:** [`5c2acede6c4318b4040a.json`](../../sessions/5c/5c2acede6c4318b4040a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**mvp1_baseline_std** — 进程被外部终止，libero_spatial 完成，其余未完成。

### libero_spatial (COMPLETED, 10/10 tasks, 500 episodes)

| Task | SR |
|------|----|
| T0 | 82% |
| T1 | 74% |
| T2 | 88% |
| T3 | 86% |
| T4 | 52% |
| T5 | 0% |
| T6 | 90% |
| T7 | 66% |
| T8 | 58% |
| T9 | 64% |
| **Avg** | **66.0%** |

### libero_object (KILLED)
- Task 0 只完成 9/50 episodes，无 eval_info.json
- libero_goal、libero_10 未开始

### 死因
- PID 109428 已退出，日志无 error/traceback/OOM
- dmesg 无权限读取
- 与 mvp1_baseline_plus 同时被杀（plus 也在 libero_object 中途终止），推测为外部信号终止

### 已执行
- Registry: status=DONE, conclusion=killed, notes 含完整结果
- Cron 监控已删除

---
