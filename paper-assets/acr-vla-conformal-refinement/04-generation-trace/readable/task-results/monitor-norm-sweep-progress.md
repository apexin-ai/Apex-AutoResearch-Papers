# monitor norm sweep progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_norm-sweep-progress_20260521T010500_result.json`
- **Structured JSON:** [`89c050d024dee4695920.json`](../../sessions/89/89c050d024dee4695920.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成，汇总如下：

## Norm Sweep 实验进度汇总（2026-05-21 09:06 UTC）

### bjb1-18228 (4×4090)

| exp_id | PID | 状态 | 已运行 | 进度 | 预估剩余 |
|--------|-----|------|--------|------|---------|
| norm01-seed57 | 594635 | **已完成** | - | 10/10 | ✅ 09:03 完成 |
| norm005-seed58 | 596867 | **已完成** | - | 10/10 | ✅ 09:02 完成 |
| norm003-seed59 | 599925 | 运行中 | 1h41m | 9.5/10 (orange_juice rollout 5/10) | ~10min → **~09:16** |
| norm005-seed65 | 622479 | 运行中 | 31m | 2.5/10 (salad_dressing rollout 5/10) | ~93min → **~10:40** |

### bjb1-32546

| exp_id | PID | 状态 | 已运行 | 进度 | 预估剩余 |
|--------|-----|------|--------|------|---------|
| norm005-seed61 | 712959 | 运行中 | 1h16m | 6.5/10 (butter rollout 5/10) | ~41min → **~09:47** |
| norm003-seed64 | 723784 | 运行中 | 32m | 2/10 | ~1h28m → **~10:34** |
| norm003-seed65 | 725722 | 运行中 | 29m | 2/10 | ~1h26m → **~10:32** |
| norm01-seed64 | 726800 | 运行中 | 29m | 1.5/10 | ~1h40m → **~10:46** |
| norm01-seed65 | 728057 | 运行中 | 28m | 1.5/10 | ~1h40m → **~10:46** |
| norm005-seed64 | 729873 | 运行中 | 28m | 1.5/10 | ~1h40m → **~10:46** |

### bjb2-28827

| exp_id | PID | 状态 | 已运行 | 进度 | 预估剩余 |
|--------|-----|------|--------|------|---------|
| norm01-seed60 | 890012 | 运行中 | 1h39m | 7.5/10 (milk rollout 5/10) | ~33min → **~09:39** |
| norm01-seed71 | 922504 | 运行中 | 19m | 1/10 | ~2h10m → **~11:16** |
| norm005-seed72 | 922712 | 运行中 | 19m | 1/10 | ~2h10m → **~11:16** |
| norm003-seed73 | 922982 | 运行中 | 19m | 1/10 | ~2h10m → **~11:16** |
| norm01-seed74 | 923256 | 运行中 | 19m | 1/10 | ~2h10m → **~11:16** |
| norm005-seed75 | 923398 | 运行中 | 19m | 1/10 | ~2h10m → **~11:16** |

### 整体预估

- **已完成**: 2/16（norm01-seed57, norm005-seed58）
- **最早完成**: norm003-seed59 → ~09:16（约 10 分钟后）
- **最晚完成**: bjb2-28827 上的 5 个新实验 → **~11:15-11:30 UTC**
- **全部完成**: 今天 ~11:30 UTC（约 2.5 小时后）

注意：bjb2-28827 有 6 个进程但可能只有 4 GPU，GPU 共享可能导致较新实验慢于预期（ETA 可能推迟到 ~12:00）。距 CoRL DDL（5/29）还有 8 天，时间充裕。

---
