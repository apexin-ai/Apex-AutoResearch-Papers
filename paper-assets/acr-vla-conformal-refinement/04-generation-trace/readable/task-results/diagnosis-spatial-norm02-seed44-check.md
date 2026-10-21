# diagnosis spatial norm02 seed44 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_spatial-norm02-seed44-check_20260519T142131_result.json`
- **Structured JSON:** [`4850371ffb81371cf6f8.json`](../../sessions/48/4850371ffb81371cf6f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **eval-obs-only-spatial-norm02-seed44** 已成功完成。Registry 已更新，cron 已不存在（可能已被之前的 auto-resolve 删除）。

**结果：Overall SR = 36% (36/100)**

Per-task breakdown:

| Task | SR | Successes |
|------|-----|-----------|
| between plate and ramekin | 0.9 | 9/10 |
| next to ramekin | 1.0 | 10/10 |
| next to cookie box | 1.0 | 10/10 |
| on cookie box | 0.4 | 4/10 |
| next to plate | 0.2 | 2/10 |
| in top drawer | 0.1 | 1/10 |
| from table center | 0.0 | 0/10 |
| on ramekin | 0.0 | 0/10 |
| on stove | 0.0 | 0/10 |
| on wooden cabinet | 0.0 | 0/10 |

明显的二分模式：近处/相对位置 task（next to, between）接近满分，而远处/非常规位置 task（stove, cabinet, table center, on ramekin）完全失败。

---
