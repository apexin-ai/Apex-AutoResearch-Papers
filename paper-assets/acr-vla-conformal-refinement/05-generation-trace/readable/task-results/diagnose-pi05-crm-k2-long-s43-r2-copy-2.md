# diagnose pi05 crm k2 long s43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-crm-k2-long-s43-r2_20260526T122610_result.json`
- **Structured JSON:** [`d5b95d1811f8749987b7.json`](../../sessions/d5/d5b95d1811f8749987b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：False positive，实验已完成。**

| 指标 | 值 |
|------|-----|
| overall_success_rate | **76.0%** |
| 总 successes | 152 / 200 |
| 10 tasks × 20 rollouts | 全部完成 |

与 s42 (82.0%) 相同的模式——eval 进程正常完成并写出 JSON 后退出，cron 检测到进程消失误报为失败。

---
