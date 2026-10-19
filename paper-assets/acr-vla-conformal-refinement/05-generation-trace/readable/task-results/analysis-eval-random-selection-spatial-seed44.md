# analysis eval random selection spatial seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-random-selection-spatial-seed44_20260520T123512_result.json`
- **Structured JSON:** [`859816448fc543fd867a.json`](../../sessions/85/859816448fc543fd867a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新成功。结果汇总：

## 实验结果

**overall_success_rate = 28.0% (28/100)**

**per_task_sr:**

| Task | SR |
|------|-----|
| between_plate_and_ramekin | 70% |
| next_to_ramekin | 90% |
| from_table_center | 0% |
| on_cookie_box | 10% |
| in_top_drawer | 0% |
| on_ramekin | 0% |
| next_to_cookie_box | 90% |
| on_stove | 0% |
| next_to_plate | 20% |
| on_wooden_cabinet | 0% |

## 对比结论

- **Random Selection Spatial (seed44): 28.0%**
- VLA-only Spatial mean: ~29.6%
- CRM Spatial K=10 (obs_only norm02): ~34.4%

**Hypothesis 成立。** Random selection (28.0%) ≈ VLA-only (~29.6%)，差异仅 1.6pp，在噪声范围内。这与 Object benchmark 上的结论一致（Random Object ~10.25% ≈ VLA-only Object ~10.9%）。CRM guidance（argmin selection）才是性能提升的来源，而非 sampling diversity。

Registry 已更新：status=DONE, conclusion=success, metrics 已写入。

---
