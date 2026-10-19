# analyze eval obs only object norm02 seed49

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-object-norm02-seed49_20260520T124604_result.json`
- **Structured JSON:** [`36b6efec87f8cae94b77.json`](../../sessions/36/36b6efec87f8cae94b77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**汇总：**

| 项目 | 值 |
|------|-----|
| seed49 SR | **14.0%** (14/100) |
| 更新后 Object CRM norm02 | **16.4% ± 2.0% (n=7)** |
| 原始值 | 16.8% ± 1.8% (n=6) |
| VLA-only baseline | 10.9% |
| CRM 提升 | **+5.5pp** (+50.5% relative) |
| 异常 | 无 |

seed49 偏低（14% < prior mean 16.8%），略拉低均值并增大方差，但仍在1σ范围内，per-task pattern与其他seed一致。结论 = success，已注册到registry。

---
