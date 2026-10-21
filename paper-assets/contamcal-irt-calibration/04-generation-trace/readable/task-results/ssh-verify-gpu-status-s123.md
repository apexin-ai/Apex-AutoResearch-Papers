# ssh verify gpu status s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-gpu-status-s123_20260513T205215_result.json`
- **Structured JSON:** [`35e1077878d36eb20cd1.json`](../../sessions/35/35e1077878d36eb20cd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部正常，无需重提交。**

| GPU | 实验 | PID | 状态 | 进度 | 速度 | 最新 loss |
|-----|------|-----|------|------|------|-----------|
| 0 | (其他任务) | - | 100% util, 23132/24564 MiB | - | - | - |
| 1 | 0.5B_d000_s123 | 216033 | **ALIVE** (Rl, 11min) | 460/3125 (15%) | ~1.08 s/it | 1.51 |
| 2 | 1.5B_d000_s123 | 216111 | **ALIVE** (Rl, 11min) | 260/3125 (8%) | ~2.10 s/it | 1.52 |
| 3 | 3B_d000_s123 | 216935 | **ALIVE** (Sl, 11min) | 171/3125 (5%) | ~3.78 s/it | (日志中无 loss 输出行可见) |
| 4 | (其他任务) | - | 38% util, 21561/24564 MiB | - | - | - |
| 5 | (其他任务) | - | 0% util, 18663/24564 MiB | - | - | - |

三个 s123 tmux session 和 Python 进程全部存活，训练正常推进。预计完成时间：
- 0.5B: ~47 min 剩余
- 1.5B: ~1h40m 剩余
- 3B: ~3h10m 剩余

---
