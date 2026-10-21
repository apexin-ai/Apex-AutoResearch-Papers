# check adaptive fix progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_adaptive_fix_progress_20260514T171509_result.json`
- **Structured JSON:** [`ff9b743b121df4f8df47.json`](../../sessions/ff/ff9b743b121df4f8df47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前时间约 01:16 UTC。汇总如下：

## GPU 状态

| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 | 99% | 46.5 / 97.9 GiB | grid_b3_0_seed42 (PID 112475) |
| 1 | 78% | 75.0 / 97.9 GiB | adaptive_fix_seed42 (PID 108213) |
| 2 | 100% | 75.0 / 97.9 GiB | adaptive_fix_seed123 (PID 109362) |
| 3 | 99% | 75.0 / 97.9 GiB | adaptive_fix_seed456 (PID 115071) |

## 训练进度

| 实验 | GPU | 当前 step | 总 step | 速度 | 剩余时间 | 预估完成 (UTC) |
|------|-----|-----------|---------|------|----------|---------------|
| adaptive_fix_seed42 | 1 | 7121 | 8477 | 3.27 it/s | ~7 min | ~01:23 |
| adaptive_fix_seed123 | 2 | 5367 | 8477 | 3.23 it/s | ~16 min | ~01:32 |
| adaptive_fix_seed456 | 3 | 7241 | 8477 | 3.18 it/s | ~6.5 min | ~01:23 |
| grid_b_seed42_batch | 0 | 4148 | 6103 | 2.12 s/it | ~69 min | ~02:25 |
| uniform_seed42 | (1) | 6103 | 6103 | — | **已完成** | EXIT_CODE=0 |

注意：adaptive_fix 三组总 step 是 **8477**（非任务中提到的 6103）。seed42 和 seed456 进度接近（84-85%），seed123 落后（63%）。grid_b 批量任务当前跑 b=3.0，还需约 1 小时。

---
