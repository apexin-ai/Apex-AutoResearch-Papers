# ops check norm005 seed43 r2 bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-norm005-seed43-r2-bjb1-32546_20260518T004142_result.json`
- **Structured JSON:** [`fa435cb8ad50d566ceef.json`](../../sessions/fa/fa435cb8ad50d566ceef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval-obs-only-object-norm005-seed43-r2** 完成。

| 项目 | 值 |
|---|---|
| 状态 | DONE (success) |
| Overall SR | **14%** (14/100) |
| 方法 | obs_only CRM, ε=0.05, seed43 |
| 服务器 | bjb1-32546 |
| 释放 GPU | **cuda:0** on bjb1-32546 |

Cron 已删除。与 seed42 的 13% 基本一致，确认 ε=0.05 低 norm 段的 magnitude curve 数据点稳定在 ~13-14%。

---
