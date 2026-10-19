# ops bjb1 18228 log diagnosis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-18228-log-diagnosis_20260515T050345_result.json`
- **Structured JSON:** [`4ea16cbae6f5bd238b43.json`](../../sessions/4e/4ea16cbae6f5bd238b43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

## 结果

### eval-acr-spatial-v4-small (PID 253085)
- **退出原因**: 被 kill-restart Worker SIGTERM kill（非 hang）
- **完成进度**: 7/10 tasks
- **部分 metrics** (42.9% SR, 30/70):

| Task | SR |
|---|---|
| between_plate_and_ramekin | 60% (6/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 10% (1/10) |
| on_cookie_box | 40% (4/10) |
| in_top_drawer | 0% (0/10) |
| on_ramekin | 0% (0/10) |
| next_to_cookie_box | **90%** (9/10) |

### eval-acr-spatial-v4-obs-only-r2 (PID 270097)
- **退出原因**: 被 kill-restart Worker SIGTERM kill（非 hang）
- **完成进度**: 6/10 tasks + task 7 部分 (rollout 5/10)
- **部分 metrics** (40.0% SR, 24/60):

| Task | SR |
|---|---|
| between_plate_and_ramekin | **90%** (9/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 40% (4/10) |
| in_top_drawer | 10% (1/10) |
| on_ramekin | 0% (0/10) |

### GPU 状态
4 块 GPU 全部空闲（0 MiB / 0% utilization）。

### 已执行
- Registry: 两个实验 status→DONE, conclusion→failed, failure_reason 已修正为 SIGTERM kill（之前误判为 hang）
- Cron: 两个实验均无活跃 cron（已被之前的诊断清除过）

---
