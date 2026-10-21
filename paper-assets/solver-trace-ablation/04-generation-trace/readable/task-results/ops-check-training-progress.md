# ops check training progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-training-progress_20260514T020044_result.json`
- **Structured JSON:** [`e6a44896513faee6f11b.json`](../../sessions/e6/e6a44896513faee6f11b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常运行，无异常：

| 实验 | 进度 | 预计完成 |
|---|---|---|
| **plan013-random-reward-s42-r4** | 165/500 (33%) | ~02:36 UTC (~35 min) |
| **plan001-exec-only-s43-r4** | 123/500 (24.6%) | ~02:47 UTC (~46 min) |

- GPU 0/1 利用率 100%/91%，显存占用 ~82%，正常
- 磁盘 112G 剩余 (56%)，安全
- 两个实验 parse_rate 稳定 1.0，prove_rate 正常波动

报告已写入 `artifacts/training_progress_check.md`。

---
