# diagnose exp 015b v3

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_015b_v3_20260515T121619_result.json`
- **Structured JSON:** [`a94145ba191eba8692d3.json`](../../sessions/a9/a94145ba191eba8692d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。进程已过了 `Create envs` 阶段，正在 prefill dataset。

## 诊断结果

**错误信息**：`AttributeError: 'NoneType' object has no attribute 'glGetError'` — PyOpenGL 3.1.10 的 OSMesa 平台无法加载 `libOSMesa` GL 库。

**根本原因**：`submit_plan015b.sh` 设置了 `MUJOCO_GL=osmesa`，但 OSMesa 后端在当前环境下已损坏（所有之后启动的进程都会复现）。EGL 后端完好可用。

**修复**：将脚本中 `MUJOCO_GL=osmesa` / `PYOPENGL_PLATFORM=osmesa` 改为 `egl`。实验已重新启动，成功通过环境创建阶段，正在 prefill。

**注意**：其他脚本（`cheetah_run_experiments.sh`、`multi_seed_runs.sh`、`submit_plan017.sh`、`submit_plan020_cheetah_baseline.sh`）也都用了 osmesa，后续启动前需要同样修改。

---
