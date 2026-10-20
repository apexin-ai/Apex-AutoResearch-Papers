# analysis qwen25 folio read harvest

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen25-folio-read-harvest_20260522T105020_result.json`
- **Structured JSON:** [`8d571cc3b6119ff74ea2.json`](../../sessions/8d/8d571cc3b6119ff74ea2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed=789 还未完成——只有 195/204，实验仍在跑。seed 123 和 456 都是 204 个。

汇总当前状态：

| Seed | N | SC (%) | SICA (%) | Delta (pp) | Status |
|------|---|--------|----------|------------|--------|
| 42 | — | 77.50 | 75.49 | -2.01 | Done (given) |
| 123 | 204 | 74.51 | 73.04 | -1.47 | Done |
| 456 | 204 | 74.02 | 74.02 | 0.00 | Done |
| 789 | 195 | 73.85 | 72.31 | -1.54 | **Incomplete (195/204)** |

**seed=789 还差 9 个问题。** 收割脚本 (PID 576920) 仍在轮询等待。实验进程仍在跑。

进程状态：
- PID 510872: **ALIVE**
- PID 555317 (Guard): **ALIVE**
- PID 576920 (Harvest): **ALIVE**
- GPU 1: 97% utilization, 90161 MiB used

实验还在跑，等剩余 9 个问题完成后收割脚本会自动触发计算。

---
