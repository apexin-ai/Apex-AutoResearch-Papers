# diag baseline eval gpu status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_baseline_eval_gpu_status_20260516T005903_result.json`
- **Structured JSON:** [`ae7617b81a772fe60ec8.json`](../../sessions/ae/ae7617b81a772fe60ec8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 进程状态

| PID | 模型 | GPU | 状态 | 运行时间 | 当前任务 |
|-----|------|-----|------|----------|----------|
| 471056 | baseline_plus | cuda:0 | **ALIVE** | 1h45m | libero_goal |
| 508625 | baseline_std | cuda:1 | **ALIVE** | 1h24m | libero_goal |

### GPU 使用

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 2140 MiB / 97887 MiB (2.2%) | 1% |
| cuda:1 | 3068 MiB / 97887 MiB (3.1%) | 0% |

GPU 近乎空闲是正常的——eval 瓶颈在仿真环境 CPU 端，不在 GPU。

### 已完成 suite 结果

| 模型 | Suite | Success Rate |
|------|-------|-------------|
| baseline_plus (v2) | libero_spatial | **408/500 = 81.6%** |
| baseline_plus (v2) | libero_object | **444/500 = 88.8%** |
| baseline_std (v3) | libero_spatial | **330/500 = 66.0%** |
| baseline_std (v3) | libero_object | **339/500 = 67.8%** |

### libero_goal 进度

- **baseline_plus**: 9/10 tasks 已有视频输出 (task 0-8)，正在跑 task 9 或刚完成 task 8
- **baseline_std**: 7/10 tasks 已有视频输出 (task 0-6)，正在跑 task 7 或刚完成 task 6

### 注意
实际输出目录是 `baseline_plus_v2`（不是 v3），进程命令行也确认了 `--output_dir=.../baseline_plus_v2/libero_goal`。

---
