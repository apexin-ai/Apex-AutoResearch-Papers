# fix eval obs only default seed45 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-obs-only-default-seed45-check_20260517T173111_result.json`
- **Structured JSON:** [`f6d2b849880a2eb265fb.json`](../../sessions/f6/f6d2b849880a2eb265fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被删除或从未创建）。

**实验完成总结：**

| 字段 | 值 |
|------|------|
| exp_id | eval-obs-only-object-default-seed45 |
| success_rate | **12%** (24/200) |
| 对比 seed42 | 17% → seed45 降到 12% |
| 状态 | DONE (success) |

obs_only default norm 在 seed45 下表现为 12%，低于 seed42 的 17%，说明在不裁剪 norm 的情况下 obs_only 方差较大，性能不稳定。

---
