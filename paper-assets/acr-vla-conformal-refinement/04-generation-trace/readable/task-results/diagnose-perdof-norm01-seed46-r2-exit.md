# diagnose perdof norm01 seed46 r2 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_perdof-norm01-seed46-r2-exit_20260517T205949_result.json`
- **Structured JSON:** [`f1c85ed614b29d7df827.json`](../../sessions/f1/f1c85ed614b29d7df827.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron（可能在之前 session 中已清理）。

**总结：**

| 字段 | 值 |
|------|-----|
| exp_id | eval-perdof-object-norm01-seed46-r2 |
| status | DONE (success) |
| overall SR | **10%** |
| per-task | bbq_sauce=0.3, orange_juice=0.3, chocolate_pudding=0.2, salad_dressing=0.1, milk=0.1, 其余5个=0 |
| GPU cuda:4 | **已释放**（2MiB, 0% util） |

假设验证：perdof CRM ε=0.1 seed46 = 10%，与 seed42 一致，确认 perdof 在低 norm 下表现显著劣于 obs_only（obs_only ε=0.1 ≈ 22%）。

注：bjb1-32546 上 cuda:5 仍被 `eval-perdof-object-default-seed46`（PID 423767）占用。

---
