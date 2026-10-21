# gpu scan bjb2 28827 resolve

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-scan_bjb2-28827-resolve_20260520T110514_result.json`
- **Structured JSON:** [`ea788f49fb6f72cf360e.json`](../../sessions/ea/ea788f49fb6f72cf360e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

冲突已解决。最终 GPU 状态：

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| cuda:0 | eval-adaptive-k-spatial-p75-seed44 (Director) | 307491 (wrapper 307478) | 运行中 |
| cuda:1 | eval-adaptive-k-spatial-p25-seed44 (Director) | 307767 (wrapper 307754) | 运行中 |
| cuda:2 | eval-adaptive-k-spatial-p90-seed42 (Director) | 308043 (wrapper 308030) | 运行中 |
| cuda:3 | — | — | 空闲 |
| cuda:4 | — | — | 空闲 |
| cuda:5 | — | — | 空闲 |

已 kill 的 mass-deploy 冲突进程：
- PID 313787 `eval-obs-only-spatial-norm02-seed42` (cuda:0)
- PID 314063 `eval-vla-only-goal-seed47` (cuda:1)
- PID 314659 `eval-vla-only-spatial-seed48` (cuda:2)

GPU 3-5 空闲，可用于重新部署被 kill 的 mass-deploy 实验。

---
