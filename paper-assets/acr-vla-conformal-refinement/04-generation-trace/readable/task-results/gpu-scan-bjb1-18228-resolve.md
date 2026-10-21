# gpu scan bjb1 18228 resolve

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-scan_bjb1-18228-resolve_20260520T110520_result.json`
- **Structured JSON:** [`bf3df78673a7f1b1570f.json`](../../sessions/bf/bf3df78673a7f1b1570f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

冲突已解决。PID 349877 已被 kill，cuda:3 显存从 10357MiB 降到 5202MiB。

## 最终 GPU 状态

| GPU | PID | 实验 | 启动时间 | 状态 |
|-----|-----|------|---------|------|
| cuda:0 | 346801 | `random-selection-spatial-seed42` (mass-deploy) | 18:51:05 | 运行中 |
| cuda:1 | 347075 | `random-selection-spatial-seed43` (mass-deploy) | 18:51:11 | 运行中 |
| cuda:2 | 348897 | `random-selection-spatial-seed44` (mass-deploy) | 18:51:38 | 运行中 |
| cuda:3 | 344862 | `adaptive-k-spatial-p90-seed43` (Director) | 18:45:14 | 运行中 |

- **PID 344852**（Director wrapper bash）存活，其子进程 344862 是实际的 python 评估进程
- **PID 349877**（`obs-only-goal-norm02-seed51`）已被 kill，cuda:3 冲突解除
- `obs-only-goal-norm02-seed51` 需要重新调度到空闲 GPU 上运行

---
