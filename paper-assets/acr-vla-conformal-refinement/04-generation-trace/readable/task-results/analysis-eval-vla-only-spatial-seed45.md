# analysis eval vla only spatial seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-vla-only-spatial-seed45_20260519T151919_result.json`
- **Structured JSON:** [`e0cdf1575191d8f0204d.json`](../../sessions/e0/e0cdf1575191d8f0204d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果如下：

```
success_rate: 0.27
per_task:
  between_plate_and_ramekin: 0.70 (7/10)
  next_to_ramekin:           0.90 (9/10)
  from_table_center:         0.00 (0/10)
  on_cookie_box:             0.20 (2/10)
  in_top_drawer:             0.00 (0/10)
  on_ramekin:                0.00 (0/10)
  next_to_cookie_box:        0.90 (9/10)
  on_stove:                  0.00 (0/10)
  next_to_plate:             0.00 (0/10)
  on_wooden_cabinet:         0.00 (0/10)
successes: 27 / total: 100
```

三个 seed 的 VLA-only baseline 汇总：

| seed | success_rate |
|------|-------------|
| 42 | 0.30 |
| 43 | 0.29 |
| 45 | 0.27 |
| **mean** | **0.287** |

seed 45 与前两个 seed 结果一致，VLA-only baseline 在 LIBERO-Spatial 上的平均成功率约 28.7%。

---
