# diagnose bjb2 28827 process gone batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb2-28827-process-gone-batch_20260521T030743_result.json`
- **Structured JSON:** [`e9e7f1edf29f28323535.json`](../../sessions/e9/e9e7f1edf29f28323535.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个实验已修复。确认均为 cron false positive——eval 脚本正常完成、JSON 完整，但无 sentinel/W&B 导致 cron 误判。

| exp_id | 实际状态 | SR | 备注 |
|--------|---------|------|------|
| eval-obs-only-object-norm01-seed71 | DONE ✓ | 0.16 | 10 tasks × 10 rollouts，cron false positive |
| eval-obs-only-object-norm005-seed72 | DONE ✓ | 0.11 | 10 tasks × 10 rollouts，cron false positive |
| eval-obs-only-object-norm003-seed73 | DONE ✓ | 0.16 | 10 tasks × 10 rollouts，cron false positive |
| eval-obs-only-object-norm01-seed74 | DONE ✓ | 0.13 | 10 tasks × 10 rollouts，cron false positive |
| eval-obs-only-object-norm005-seed75 | DONE ✓ | 0.15 | 10 tasks × 10 rollouts，cron false positive |

Registry 已全部更新：status=DONE, conclusion=success, metrics 写入, failure_reason 清除。

---
