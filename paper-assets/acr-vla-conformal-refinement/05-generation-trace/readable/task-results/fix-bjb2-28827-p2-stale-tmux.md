# fix bjb2 28827 p2 stale tmux

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb2-28827-p2-stale-tmux_20260520T122452_result.json`
- **Structured JSON:** [`2532f2c0567b6a5b7e9b.json`](../../sessions/25/2532f2c0567b6a5b7e9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 78261 已确认死亡。GPU 3/4/5 显存已释放（从 5248/4607/5148 MiB → 1 MiB）。

**bjb2-28827 最终 GPU 状态：**

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 2555 / 24564 MiB | 运行中 (PID 307491) |
| 1 | 3085 / 24564 MiB | 运行中 (PID 307767) |
| 2 | 2025 / 24564 MiB | 运行中 (PID 308043) |
| 3 | 1 / 24564 MiB | **空闲** ✓ |
| 4 | 1 / 24564 MiB | **空闲** ✓ |
| 5 | 1 / 24564 MiB | **空闲** ✓ |

Kill 78261 连带释放了 GPU 3/4/5 上的 3 个 python 子进程（PID 340026, 336621, 336826）。GPU 0-2 上仍有其他任务在跑。

---
