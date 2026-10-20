# monitor contamination 60 progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_contamination_60_progress_20260516T011451_result.json`
- **Structured JSON:** [`f30784d1cfe934f3eb6f.json`](../../sessions/f3/f30784d1cfe934f3eb6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 三组实验训练进度

| 实验 | Step | 进度 | 速率 | 预估剩余 | 状态 |
|------|------|------|------|----------|------|
| **contamination_60_seed42_r2** (cuda:0) | 5180/6103 | 84.9% | 2.26 s/it | ~35 min | 正常 |
| **contamination_60_grid_b0_5_seed42** (cuda:3) | 5743/6103 | 94.1% | 2.12 s/it | ~13 min | 正常 |
| **contamination_60_ess_only_seed42** (cuda:2) | 2887/6103 | 47.3% | 2.12 s/it | ~1h54m | 正常 |

**GPU 状态：** 4 卡均 95-99% 利用率，显存 46.5GB/97.9GB，无异常。

**注意：** 三个 PID 均存活。grid_b0_5 预计 ~13 分钟内完成，seed42_r2 约 35 分钟完成。两者完成后因 WANDB_MODE=disabled，cron 可能误判为 failed（同 uniform_seed42 先例）。ess_only 启动较晚，还需约 2 小时。

---
