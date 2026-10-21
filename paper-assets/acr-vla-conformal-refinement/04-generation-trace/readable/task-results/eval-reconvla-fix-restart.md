# eval reconvla fix restart

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_reconvla-fix-restart_20260513T201919_result.json`
- **Structured JSON:** [`0d6b32bf2e97e3b7e720.json`](../../sessions/0d/0d6b32bf2e97e3b7e720.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常。

### 产出汇总

**1. eval-reconvla-spatial-v1** — 已修复并重启
- **PID**: 85963
- **GPU 2** (GPU-7d267f8c): 4139 MiB 已占用
- 日志前 10 行无 EGL 错误，模型加载成功，10 个 task 已加载
- **根因**: 系统仅有 1 个 EGL device (index 0)，原命令设 `MUJOCO_EGL_DEVICE_ID=2` 越界
- **修复**: 更新 `run_eval_gpu.py` —— unset `CUDA_VISIBLE_DEVICES` 让 EGL 默认用 device 0，用 `torch.cuda.set_device(2)` 把计算放到 GPU 2

**2. precompute-k5** (cuda:3) — 正常运行
- PID 79517，GPU 3 占用 1532 MiB
- 进度: `2100/12167` (~17%)，~0.25s/sample，预计还需 ~2500s (~42 min)

---
