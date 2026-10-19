# exec nohup collect cuda1 parallel

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_nohup-collect-cuda1-parallel_20260512T170150_result.json`
- **Structured JSON:** [`376432b3805744fc7f64.json`](../../sessions/37/376432b3805744fc7f64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个 GPU 的收集已经在运行中，无需再启动。**

当前状态：

| GPU | PID | 进度 | 输出目录 | SR |
|-----|-----|------|----------|-----|
| GPU 0 | 266200 | 3/250 | `trajectories_v5_cuda0` | 2/3 |
| GPU 1 | 263025 | 14/250 | `trajectories_v5_cuda1` | 5/14 |

注意：GPU 1 的进程（PID 263025）启动时用的是 `--gpu 1` 而非 `CUDA_VISIBLE_DEVICES=1 --gpu 0` 模式。nvidia-smi 确认它确实在 GPU 1 上运行（7752MiB），功能正常。GPU 0 的进程用了 `CUDA_VISIBLE_DEVICES=0 --gpu 0`。

两个进程都在正常产出轨迹，GPU 1 比 GPU 0 早启动约 10 分钟，已领先。每条轨迹约 60-80 秒，预计各需 ~5-6 小时完成 250 条。

---
