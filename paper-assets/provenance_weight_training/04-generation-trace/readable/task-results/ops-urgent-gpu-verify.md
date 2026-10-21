# ops urgent gpu verify

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-gpu-verify_20260514T024858_result.json`
- **Structured JSON:** [`292b22626272f4447d53.json`](../../sessions/29/292b22626272f4447d53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 adaptive 实验全部在运行，无需重新提交。

| GPU | 利用率 | 显存占用 | PID | 实验 | 运行时间 |
|-----|--------|----------|------|------|----------|
| cuda:1 | 90% | 46523 MiB | 58888 | adaptive_seed42 | 2h55m |
| cuda:2 | 99% | 46523 MiB | 58978 | adaptive_seed123 | 2h53m |
| cuda:3 | 99% | 46523 MiB | 59058 | adaptive_seed456 | 2h52m |

GPU 0 也在满载（98%, 46523 MiB），应该是其他任务。

---
