# monitor adaptive fix progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_adaptive_fix_progress_20260514T203845_result.json`
- **Structured JSON:** [`34bb0e3dbdf82cc45c6f.json`](../../sessions/34/34bb0e3dbdf82cc45c6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四个日志文件均无 error/traceback/exception（grep 返回 0 匹配，exit code 1 是 grep 无匹配的正常行为）。

## 训练进度汇总

| 实验 | 当前 step / 总 step | 进度 | epoch | loss | 速度 | 预估剩余 |
|------|---------------------|------|-------|------|------|----------|
| **adaptive_fix_seed42** | 6097 / 6103 | **99.9%** | 0.26 | 9.72 | ~2.22s/it | **~13s** |
| **adaptive_fix_seed123** | 6077 / 6103 | **99.6%** | 0.26 | 8.98 | ~2.25s/it | **~58s** |
| **adaptive_fix_seed456** | 5589 / 6103 | **91.6%** | 0.24 | — | ~2.21s/it | **~19min** |
| **grid_b_seed42_batch** | 3735 / 6103 | **61.2%** | 0.16 | 11.27 | ~2.12s/it | **~1h24min** |

- 四组实验均正常运行，**无报错**
- seed42 和 seed123 即将完成（几十秒内）
- seed456 约 19 分钟后完成
- grid_b_seed42_batch 进度较慢，还需约 1.5 小时

---
