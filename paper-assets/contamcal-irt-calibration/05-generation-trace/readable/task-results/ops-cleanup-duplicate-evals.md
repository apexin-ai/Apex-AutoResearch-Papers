# ops cleanup duplicate evals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_duplicate_evals_20260514T020708_result.json`
- **Structured JSON:** [`483de57187da55872d4b.json`](../../sessions/48/483de57187da55872d4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**已 Kill：**
- PID 257853 — evaluate.py (d000_s42 重复实例，占 GPU 0)
- PID 257848 — 其父 nohup bash 进程

**已确认无需处理：**
- PID 255078 (d100_s42) — 已自行结束
- PID 256503 (d100_s42) — CUDA:4 上正常运行
- PID 257034 (d000_s42) — CUDA:2 上正常运行，作为唯一实例保留

**GPU 0 清理后状态：**
- 仅剩 SFT 训练 PID 251924 (10044 MiB / 24564 MiB)，释放了 ~3658 MiB
- GPU 利用率从高负载降至 23%

**全部 GPU 当前状态：**

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 10053 / 24564 MiB | 23% |
| 1 | 12620 / 24564 MiB | 100% |
| 2 | 10993 / 24564 MiB | 99% |
| 3 | 8957 / 24564 MiB | 62% |
| 4 | 9492 / 24564 MiB | 99% |
| 5 | 5829 / 24564 MiB | 47% |

---
