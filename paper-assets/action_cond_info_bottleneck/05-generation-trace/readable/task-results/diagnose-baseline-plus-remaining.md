# diagnose baseline plus remaining

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_baseline-plus-remaining_20260516T103030_result.json`
- **Structured JSON:** [`c34c9746ccd39ada62fe.json`](../../sessions/c3/c34c9746ccd39ada62fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Per-task 数据已拿到。从日志可知 overall pc_success = 67.2%。

## 诊断结果

**进程状态**: PID 675231 已退出，日志显示 `End of eval` + `All suites completed.`，**正常完成**。

**libero_10 per-task success rate** (50 episodes each):

| Task | SR |
|------|----|
| task_0 | 42.0% |
| task_1 | 70.0% |
| task_2 | 86.0% |
| task_3 | 88.0% |
| task_4 | 62.0% |
| task_5 | 90.0% |
| task_6 | 62.0% |
| task_7 | 54.0% |
| task_8 | 42.0% |
| task_9 | 76.0% |
| **Average** | **67.2%** |

## smolvla_libero_plus baseline 4-suite 汇总

| Suite | SR |
|-------|----|
| libero_spatial | 81.6% |
| libero_object | 88.8% |
| libero_goal | 87.8% |
| libero_10 | **67.2%** |

---
