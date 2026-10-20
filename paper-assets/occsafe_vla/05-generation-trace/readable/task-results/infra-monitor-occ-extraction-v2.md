# infra monitor occ extraction v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_monitor-occ-extraction-v2_20260520T090551_result.json`
- **Structured JSON:** [`dc007d151dda40d89f90.json`](../../sessions/dc/dc007d151dda40d89f90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度报告

### 进程状态：全部存活

| Task | PID | 状态 | 已完成 demo | 进度 |
|------|-----|------|------------|------|
| task_0 | 50744 | RUNNING | 1/50 (demo_1 进行中, frame 83/84) | 2% |
| task_1 | 51032 | RUNNING | 1/50 | 2% |
| task_2 | 51482 | RUNNING | 0/50 (demo_0 frame 102/103) | ~1% |
| task_3 | 51931 | RUNNING | 1/50 | 2% |
| task_4 | 52381 | RUNNING | 1/50 | 2% |
| task_5 | 52769 | RUNNING | 1/50 | 2% |
| task_6 | 53280 | RUNNING | 0/50 (demo_0 frame 122/123) | ~1% |
| task_7 | 53636 | RUNNING | 0/50 (demo_0 刚开始) | <1% |
| task_8 | 53988 | RUNNING | 1/50 | 2% |
| task_9 | 72341 | RUNNING | 0/50 (demo_0 刚开始) | <1% |

### 数据产出
- **occ_data 目录**: 22M, 10 个 hdf5 文件（每个 task 已创建空/初始文件）

### 时间分析
- **task_0~8** 启动于 15:23-15:24 UTC，已运行 **1h43m**
- **task_9** 重启于 16:14 UTC（晚 ~50min），已运行 **52min**
- 大部分时间消耗在 **MuJoCo 场景初始化 + geom dump（~90-100 min）**，实际 demo 处理刚开始
- 实测 demo 处理速度: **~1.75s/frame, ~100-150 frames/demo → ~3-3.5 min/demo**

### 预估完成时间

| | 初始化 | Demo 处理 | ETA (UTC) |
|--|--------|-----------|-----------|
| task_0~8 | 已完成 | 48 demos × 3.5 min ≈ 168 min | **~19:55 UTC** |
| task_9 (瓶颈) | 还需 ~40 min | 50 demos × 3.5 min ≈ 175 min | **~20:50 UTC** |

### 结论
- **0 个失败 task**，全部 10 路正常运行
- 初始化阶段占了大部分已消耗时间，demo 提取刚进入正轨
- **整体预估完成: 今天 ~20:50 UTC（约 3.5 小时后）**
- task_9 因重启过是瓶颈，其余 task 预计 ~19:55 完成

---
