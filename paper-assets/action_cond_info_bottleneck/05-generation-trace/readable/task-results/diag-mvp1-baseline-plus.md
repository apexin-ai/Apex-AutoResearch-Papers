# diag mvp1 baseline plus

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp1_baseline_plus_20260515T212532_result.json`
- **Structured JSON:** [`03853d7b62d03cd2854d.json`](../../sessions/03/03853d7b62d03cd2854d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结果：部分完成（1/4 suites），标记为 failed。**

**libero_spatial（已完成，Avg SR = 81.6%）：**

| Task | SR | Detail |
|------|-----|--------|
| 0 | 98.0% | 49/50 |
| 1 | 82.0% | 41/50 |
| 2 | 92.0% | 46/50 |
| 3 | 94.0% | 47/50 |
| 4 | 74.0% | 37/50 |
| 5 | 32.0% | 16/50 |
| 6 | 94.0% | 47/50 |
| 7 | 86.0% | 43/50 |
| 8 | 80.0% | 40/50 |
| 9 | 84.0% | 42/50 |

**失败原因：** 进程在 libero_object task 1 rollout (~step 76/280) 中途被杀。日志无 Traceback/Error/OOM，dmesg 无 OOM killer 记录，疑似被外部信号终止。

**未完成：** libero_object（仅 task 0 完成）、libero_long、libero_goal 需要重跑。cron 不存在，无需清理。

---
