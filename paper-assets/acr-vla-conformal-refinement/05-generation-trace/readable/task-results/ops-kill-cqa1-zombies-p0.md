# ops kill cqa1 zombies p0

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-cqa1-zombies-p0_20260526T102815_result.json`
- **Structured JSON:** [`380f0e2be1b1258db998.json`](../../sessions/38/380f0e2be1b1258db998.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## Kill 结果

| PID | 任务 | 结果 |
|-----|------|------|
| 197917 | GPU 3 旧 Adaptive Object s44 | 已不存在（先前已清理） |
| 198442 | GPU 4 旧 Adaptive Long s43 | KILL_SENT → DEAD |
| 199049 | GPU 5 旧 Adaptive Long s44 | KILL_SENT → DEAD |
| 286851 | GPU 3 新 Adaptive Object s44 | KILL_SENT → DEAD |

## nvidia-smi 对比

| GPU | Kill 前 | Kill 后 |
|-----|---------|---------|
| 3 | 13176MiB (PID 286851) | **1MiB / P8 / 0%** ✅ |
| 4 | 11860MiB (PID 198442) | **1MiB / P8 / 0%** ✅ |
| 5 | 11860MiB (PID 199049) | **1MiB / P8 / 0%** ✅ |

## GPU 0/1/2 存活状态（未受影响）

- GPU 0: PID 216649，12728MiB，P2，22% util — 运行中 ✅
- GPU 1: PID 219043，10770MiB，P2，44% util — 运行中 ✅
- GPU 2: PID 219679，10307MiB，P2，62% util — 运行中 ✅

GPU 3/4/5 已完全释放，可投放新实验。

---
