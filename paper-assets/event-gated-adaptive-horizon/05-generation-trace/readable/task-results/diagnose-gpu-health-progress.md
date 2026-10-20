# diagnose gpu health progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-health-progress_20260529T075708_result.json`
- **Structured JSON:** [`3aa8fa439a002eaf3db9.json`](../../sessions/3a/3aa8fa439a002eaf3db9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. GPU 状态
| | cuda:0 | cuda:1 |
|---|---|---|
| 型号 | NVIDIA RTX PRO 6000 Blackwell (98GB) | **不存在** |
| GPU-Util | 22% | — |
| Memory | 4700MiB / 97887MiB (4.8%) | — |

**这台实例只有 1 张 GPU**，`torch.cuda.device_count()=1`，cuda:1 不可用。

### 2. GPU 利用率分析 (22%)
**正常，不是故障。** Dreamer 交替做 env interaction (CPU-bound MuJoCo) 和 model training (GPU)，CPU 占用 1206%，fps=10.1。这是 model-based RL 的典型模式——大量时间在 CPU 端跑仿真，GPU 周期性空闲。

### 3. EGL 设备
- EGL device 0: **OK**
- EGL device 1: **OK** (EGL 设备独立于 CUDA 设备，即使只有 1 张 GPU 也可用)

之前 `MUJOCO_EGL_DEVICE_ID=1` 的问题不会复现，当前实验已锁定 `MUJOCO_EGL_DEVICE_ID=0`。

### 4. exp_quadruped_baseline_s0_r2 进度

| 指标 | 值 |
|---|---|
| 当前 step | **112000 / 200000 (56%)** |
| 运行时长 | ~3h (12:58 → 15:57) |
| FPS | 10.1 |
| 剩余 | 88000 steps ÷ ~626 steps/min ≈ **2h20m** |
| 预计完成 | **~18:20** |
| 最新 eval (step 105K) | eval_return = **217.4** |
| CIVO alert | step 95K 触发 (ve_ratio=17.4)，step 105K 已恢复 (ve_ratio=1.8) |
| train_return 趋势 | 波动大 (6.0 ~ 393.8)，quadruped 早期典型表现 |

---
