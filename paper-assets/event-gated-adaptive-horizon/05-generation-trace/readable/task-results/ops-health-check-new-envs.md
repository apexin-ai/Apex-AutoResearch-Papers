# ops health check new envs

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_health-check-new-envs_20260528T223826_result.json`
- **Structured JSON:** [`d04e599d2a3b860b84fd.json`](../../sessions/d0/d04e599d2a3b860b84fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **Humanoid Walk (`exp_humanoid_baseline_s0`)** — 启动成功。已完成 prefill（2500 steps）、首次 evaluation（step 5000, eval_return=1.2），正在训练中。Action space Box(-1.0, 1.0, (21,))，观测包含 com_velocity/extremities/head_height/joint_angles/torso_vertical/velocity。仅有 FutureWarning（`torch.cuda.amp` 弃用警告），无实质错误。

- **Quadruped Walk (`exp_quadruped_baseline_s0`)** — 启动失败。错误：`ImportError: Cannot initialize a headless EGL display.`。dm_control 尝试初始化 EGL 渲染时失败，进程已退出（EXIT_CODE=1）。

Quadruped 的 EGL 问题说明该 tmux session 启动时缺少 EGL 环境变量。Humanoid 能正常跑说明 EGL 本身可用，Quadruped 大概率是启动时环境变量未正确设置（`MUJOCO_GL=egl` 和 `PYOPENGL_PLATFORM=egl`）。

需要我重新启动 Quadruped 实验并确保 EGL 环境变量正确吗？

---
