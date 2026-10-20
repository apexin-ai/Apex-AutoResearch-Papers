# ssh gpu cleanup and status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-cleanup-and-status_20260513T231151_result.json`
- **Structured JSON:** [`e5bd686daa59f6e25e63.json`](../../sessions/e5/e5bd686daa59f6e25e63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 清理结果

**Kill 的进程：**
- PID 227941 + 227936 (GPU 1): 0.5B d000 s123 eval（旧，与 GPU 2 的 229521 重复）
- PID 227578 + 227572 (GPU 2): 1.5B d000 s123 eval（旧）

**已 DEAD 的进程：** PID 227160, PID 226817（已自行退出）

## 最终 6 GPU 状态

| GPU | 显存占用 | 实验 | PID |
|-----|---------|------|-----|
| 0 | 0 MiB / 24564 MiB | 空闲 | — |
| 1 | 3658 MiB / 24564 MiB | eval 0.5B d000 s42 | 229375 |
| 2 | 3658 MiB / 24564 MiB | eval 0.5B d000 s123 | 229521 |
| 3 | 17318 MiB / 24564 MiB | train_sft 3B d000 s42 (0.5B adapter) | 216254 |
| 4 | 5820 MiB / 24564 MiB | eval 1.5B d000 s42 | 221376 |
| 5 | 18656 MiB / 24564 MiB | train_sft 3B d000 s42 | 210671 |

GPU 1/2 各从 2 个 eval 降到 1 个，显存分别释放 3658 MiB 和 5820 MiB。

---
