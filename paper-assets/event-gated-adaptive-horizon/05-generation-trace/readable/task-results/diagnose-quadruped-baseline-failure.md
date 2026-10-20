# diagnose quadruped baseline failure

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_quadruped_baseline_failure_20260529T043517_result.json`
- **Structured JSON:** [`ac3c7d0f86c676f96e29.json`](../../sessions/ac/ac3c7d0f86c676f96e29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

**1. GPU 状态**
- **NVIDIA RTX PRO 6000 Blackwell (98GB)** — 完全空闲，显存 0 MiB，利用率 0%。可用。

**2. quadruped_baseline_s0 失败原因**
- **EGL 初始化失败**，不是 OOM。
- 错误：`ImportError: Cannot initialize a headless EGL display.`
- dm_control 尝试加载 EGL 渲染器失败，`nouveau_dri.so` 不存在。
- logdir 里只有空的 tfevents 文件（88 bytes），没有 metrics.jsonl，没有 checkpoint —— 在创建环境阶段就崩了，零训练。
- **根因**：缺少 EGL 环境变量。需要在启动前设置 `MUJOCO_GL=egl` 和 `PYOPENGL_PLATFORM=egl`，确保 dm_control 走 NVIDIA EGL 而非 mesa。

**3. humanoid_baseline_s0 状态**
- **已正常完成**（EXIT_CODE=0），跑到 212K steps。
- 进程已退出，无残留 python3 进程。
- 最终 eval_return 曲线：峰值 2.16 (step 165K)，最后一次 eval (step 205K) = **1.24**。
- 最终 train_return (step 212K)：0.76 / 1.87 / 2.69 / 3.43 / 2.15（4 个 env 的分别值）。
- CIVO 检测器在 step 195K 触发了一次警告（ve_ratio=9.88），但训练继续到完成。

**下一步建议**：重跑 quadruped_baseline_s0 时在启动命令前加 `export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl`。

---
