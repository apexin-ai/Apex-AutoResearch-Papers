# monitor training progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training_progress_20260513T235517_result.json`
- **Structured JSON:** [`90b2fc51ed4ca4354666.json`](../../sessions/90/90b2fc51ed4ca4354666.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/training_progress_check.md`。关键结论：

**全部 4 个实验正常运行，无异常。**

| 实验 | 进度 | 预计剩余 |
|------|------|---------|
| uniform_seed42 | 1422/6103 (23%) | ~1h 45m |
| uniform_seed123 | 1419/6103 (23%) | ~1h 45m |
| uniform_seed456 | 1419/6103 (23%) | ~1h 45m |
| grid_b (b=0.5, 第1/6个) | 179/6103 (3%) | ~19h（全部6个b值） |

- 4 卡 GPU 利用率 93-99%，显存约 44-47 GB / 98 GB
- 磁盘 30G/250G（12%），预计全部完成后 ~40G，无风险
- 3 个 uniform 实验约 09:40 UTC 完成；grid-b 全部 6 个值约明天 03:00 UTC 完成

---
