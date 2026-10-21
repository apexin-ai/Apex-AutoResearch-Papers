# ops kill and resubmit grid seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_and_resubmit_grid_seed456_20260515T073807_result.json`
- **Structured JSON:** [`4b619bce1c09063f885c.json`](../../sessions/4b/4b619bce1c09063f885c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Kill 结果
- grid_b2_0_seed456 (PID 182488→子进程182493): **KILLED**
- grid_b5_0_seed456 (PID 158295→子进程158300): **KILLED**
- grid_b3_0_seed456 (PID 158211→子进程158216): **KILLED**

## GPU 状态
- cuda:0: **0 MiB / 空闲**
- cuda:1: 75007 MiB (grid_b_low_seed42, PID 163662, 正常运行)
- cuda:2: **0 MiB / 空闲**
- cuda:3: **0 MiB / 空闲**

## Checkpoint 状态
- grid_b2_0_seed456: **checkpoint-3500** 可用 (model.safetensors ✓)，另有 checkpoint-3000
- grid_b3_0_seed456: **checkpoint-3000** 可用 (model.safetensors ✓)，另有 checkpoint-2500
- grid_b5_0_seed456: **checkpoint-3000** 可用 (model.safetensors ✓)，另有 checkpoint-2500

## 建议
三个实验都有有效 checkpoint，重跑时可用 `--resume_from_checkpoint` 从最新 checkpoint 恢复（分别是 step 3500、3000、3000），无需从头训练。注意：给定的父进程 PID 与实际 GPU 进程 PID 有偏差（子进程 PID 各大 5），首次 kill 只杀了 shell wrapper，第二轮才杀掉实际 Python 进程释放显存。

---
