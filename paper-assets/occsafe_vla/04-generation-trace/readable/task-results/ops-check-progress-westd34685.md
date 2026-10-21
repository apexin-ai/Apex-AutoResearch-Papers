# ops check progress westd34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_progress_westd34685_20260523T194356_result.json`
- **Structured JSON:** [`6592f81363940dd4b356.json`](../../sessions/65/6592f81363940dd4b356.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

| 实验 | Step | 进度 | 速度 | 预估剩余 | 最新 loss |
|------|------|------|------|----------|-----------|
| **reverse_cutoff_s0** (cuda:2) | 47839/50005 | 96% | ~1.04 it/s | **~35 min** | occ=0.0108, action=0.0540 |
| **cutoff_25k_s0** (cuda:3) | 47959/50005 | 96% | ~1.03 it/s | **~33 min** | occ=0.0119, action=0.0630 |
| **cutoff_15k_s0** (cuda:1) | 4105/50005 | 8% | ~1.05 it/s | **~12.1 h** | occ=0.0120, action=0.1309 |
| **cutoff_45k_s0** (cuda:0) | 3153/50005 | 6% | ~1.04 it/s | **~12.5 h** | occ=0.0098, action=0.2412 |

4 个进程全部在运行。reverse_cutoff_s0 和 cutoff_25k_s0 预计约 **~14:50 UTC** 完成（比预估的 18:40-20:30 UTC 早很多）。cutoff_15k_s0 和 cutoff_45k_s0 预计明天凌晨 ~02:30-03:00 UTC 完成。

---
