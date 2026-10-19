# urgent kill duplicate pid32153

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_kill-duplicate-pid32153_20260516T140515_result.json`
- **Structured JSON:** [`3d5c1d17bff60c8a0202.json`](../../sessions/3d/3d5c1d17bff60c8a0202.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Kill 结果：**

- PID 32153：已终止，GPU 显存已释放
- PID 21363：正常运行，GPU 0，v7_contrastive seed1，已跑 1h20m
- PID 27427：正常运行，GPU 1（注：命令行写的 `--gpu 0` 但实际在 GPU 1），v7_seed2，已跑 21m
- GPU 0：仅 PID 21363 一个训练进程
- GPU 1：仅 PID 27427 一个训练进程

另外注意到 PID 33047 占用 ~6.5GB 显存，不属于已知训练任务。

---
