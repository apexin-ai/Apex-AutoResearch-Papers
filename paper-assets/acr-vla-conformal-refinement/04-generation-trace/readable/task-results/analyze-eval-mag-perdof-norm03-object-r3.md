# analyze eval mag perdof norm03 object r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-mag-perdof-norm03-object-r3_20260516T110345_result.json`
- **Structured JSON:** [`a079c1d28cc37e02e9db.json`](../../sessions/a0/a079c1d28cc37e02e9db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron，无需删除。

## 诊断结果

**eval-mag-perdof-norm03-object-r3** 已完整完成：

| 指标 | 值 |
|------|-----|
| Tasks | 10 |
| Rollouts | 100 |
| Success Rate | **4.0% (4/100)** |
| Suite | LIBERO-object |
| Norm | 0.3 |
| Seed | 42 |

比预期的 10-15% 还弱，是 perdof 系列在 object 上最差的结果。趋势：norm 越大性能越差（0.03→14%, 0.05→14%, 0.1→11%, 0.2→11%, 0.3→4%）。

Registry 已更新为 DONE/success。**bjb2-28827:cuda:2 已释放可用。**

---
