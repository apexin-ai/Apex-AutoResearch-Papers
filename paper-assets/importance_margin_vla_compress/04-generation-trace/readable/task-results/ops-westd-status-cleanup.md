# ops westd status cleanup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_status_cleanup_20260517T074559_result.json`
- **Structured JSON:** [`1e0e23f58009ce785b68.json`](../../sessions/1e/1e0e23f58009ce785b68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| 项目 | 状态 |
|------|------|
| **westd-27271 连通性** | 可达 |

### eval_stage1only_object_v2_fixed (GPU:0)

- **结论**: negative（0% SR）
- **已完成**: Task 0-5，每 task 50 episodes，全部 FAIL（300 episodes, 0% SR）
- **per_task_sr**: Task 0-5 均为 0/50 (0.0%)
- **当前状态**: 进程 PID 140050 仍在运行（Task 6 也全 FAIL），GPU:0 占用 3.5GB
- **Registry**: DONE / negative

⚠️ **注意**: 进程仍在 GPU:0 上跑（结果已无悬念），需要 kill 释放 GPU 吗？

### eval_stage1only_spatial (GPU:1)

- **进程**: 已自行结束（PID 65128 不存在，grep 无结果）
- **Registry**: DONE / killed
- **Notes**: buggy eval code, pruning never executed (dim guard 64≠128)

### GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|----------|--------|------|
| 0 | RTX PRO 6000 Black | 3562/97887 MiB | 45% | 45°C |
| 1 | RTX PRO 6000 Black | 1/97887 MiB | 0% | 34°C |

GPU 1 完全空闲可用。GPU 0 被 object_v2_fixed eval 进程占着（PID 140055）。

---
