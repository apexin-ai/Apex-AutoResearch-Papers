# ssh check d021 status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-d021-status_20260515T210547_result.json`
- **Structured JSON:** [`9c8c2c21b1b7a6ff5d0a.json`](../../sessions/9c/9c8c2c21b1b7a6ff5d0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d021_instruction_ablation 状态报告

### 1. 进程状态：RUNNING

| PID | 任务 | GPU | 运行时间 | 当前进度 |
|-----|------|-----|---------|---------|
| **658056** | untrained no_inst 特征提取 | GPU:1 | 37 min | task 3/10 (`push_the_plate`) 62% |
| **661030** (新) | trained no_inst 特征提取 | GPU:0 | ~4 min | task 1/10 (`open_middle_drawer`) 38% |

- PID 659993 已不存在，被 661030 替代（启动命令含 `kill 660873`，说明做了重启）。

### 2. GPU 占用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU:0 | 0% | 16.4 / 97.9 GB |
| GPU:1 | 60% | 16.4 / 97.9 GB |

另有 PID 651902 在跑 `pca_linear_probe_perlayer.py`（当前 layer 23，acc=0.9994）。

### 3. 特征提取输出文件

**untrained_libero_goal_no_inst/** — 3 文件（2 完成 + 1 写入中）:
- `open_the_middle_drawer_of_the_cabinet.h5` — 2.9 GB
- `open_the_top_drawer_and_put_the_bowl_inside.h5` — 4.2 GB
- `push_the_plate_to_the_front_of_the_stove.h5` — 1.9 GB (写入中)

**trained_libero_goal_no_inst/** — 1 文件（写入中）:
- `open_the_middle_drawer_of_the_cabinet.h5` — 1.0 GB (写入中)

文件大小与参考目录一致（参考: trained_libero_goal/ 和 untrained_libero_goal/ 各 10 个 task，各 ~25 GB）。

### 4. RSA 分析：未开始

results 目录下无 `*no_inst*` 或 `*ablation*` 相关文件。

### 5. 预估剩余时间

- **untrained (GPU:1)**: 已完成 ~2.5/10 tasks in 37 min → 预计还需 **~2 小时**
- **trained (GPU:0)**: 已完成 ~0.4/10 tasks in 4 min → 预计还需 **~1.5-2 小时**（GPU:0 速度更快，~40 step/s vs GPU:1 的 ~20 step/s）

两路提取可能在 **~2 小时后** 同时完成，之后还需跑 RSA 分析。

---
