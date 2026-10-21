# diagnose baseline westd35807 double fail

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_baseline_westd35807_double_fail_20260520T144652_result.json`
- **Structured JSON:** [`4851a498044a0e5cbce2.json`](../../sessions/48/4851a498044a0e5cbce2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断数据收集完毕。以下是报告：

---

## 诊断报告

### 时间线

| 事件 | 时间 (CST/UTC) |
|------|---------------|
| v3 训练启动（pudding） | 06:23 CST / 22:23 UTC (前一天) |
| v3 训练启动（bowl） | 06:35 CST / 22:35 UTC (前一天) |
| v3 两个进程同时被杀 | ~22:37 CST / 14:37 UTC |
| v2 两个进程启动（当前） | 22:37 CST / 14:37 UTC |

### 失败原因

**两个 v3 进程被外部信号杀死，不是代码错误。**

证据：
- 两个 v3 日志中 **零 Traceback、零 Error、零 EXIT_CODE** — 日志在训练进度条输出处突然中断
- 两个进程在 **完全相同的时刻** 同时死亡
- v2 进程在 v3 死亡的同一秒启动 → **submit_training_job 系统主动杀掉 v3 并启动 v2 替代**

最可能的解释：v2 任务提交时，系统自动终止了占用同一 GPU 的 v3 进程。这不是"失败"，而是**被替换**。

### 训练进度与丢失

| 实验 | v3 最后 step | 最后 checkpoint | 丢失 steps | v2 resume from |
|------|-------------|----------------|-----------|---------------|
| object_pudding | 16491 | 16000 | 491 (~29 min) | 16000 |
| spatial_bowl | 15822 | 14000 | **1822** (~107 min) | 14000 |

spatial_bowl 丢失较多，因为它到了 15822 但 save_interval=2000，上次 checkpoint 在 14000（还没到 16000）。

### Checkpoint 完整性

两组 checkpoint 完整，每个包含 model.safetensors (~6.5GB) + optimizer.pt (~11.7GB) + metadata.pt + norm_stats.json：

- `baseline_object_pudding/.../16000/` — 完整 ✓
- `baseline_object_pudding/.../14000/` — 完整 ✓
- `baseline_spatial_bowl/.../14000/` — 完整 ✓
- `baseline_spatial_bowl/.../12000/` — 完整 ✓

### 当前状态

**两个 v2 进程正在正常运行：**
- PID 222977 (pudding): step 16000 → 当前 ~16136, 正常训练中
- PID 222898 (bowl): step 14000 → 当前 ~14138, 正常训练中
- GPU 0: 35.7/97.9 GB, 61°C ✓
- GPU 2: 35.7/97.9 GB, 72°C ✓
- 磁盘: 121/350 GB (35%) ✓

### 结论

**不需要修复。** 实验没有"失败"——v3 进程是被 submit_training_job 替换为 v2。当前 v2 已从最后一个 checkpoint 成功 resume，正在正常训练。唯一的代价是 spatial_bowl 丢失了 1822 步（~1.8h）计算量，已无法恢复。

---
