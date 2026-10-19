# deploy bjb2 28827 p0p1p2 random spatial k5 k20

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-p0p1p2-random-spatial-k5-k20_20260519T150014_result.json`
- **Structured JSON:** [`2d6b9673b300caf45bc3.json`](../../sessions/2d/2d6b9673b300caf45bc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 不空闲，停下汇报。**

目标 GPU 中只有 cuda:3 空闲，其余三个都有活跃进程：

| GPU | Util | 显存占用 | 状态 |
|-----|------|---------|------|
| cuda:0 | 19% | 3790 MiB | **占用** |
| cuda:2 | 99% | 5520 MiB | **占用**（2个进程） |
| cuda:3 | 0% | 1 MiB | 空闲 ✓ |
| cuda:5 | 22% | 3618 MiB | **占用** |

当前服务器上有 4 个 tmux session 在运行：
- `eval-argmin-object-k5-seed44`
- `eval-random-seed46-t16`
- `eval-random-selection-object-k5-seed43`
- `eval-vla-only-spatial-seed44`

需要你确认：等这些实验跑完再部署，还是终止某些实验腾出 GPU？

---
