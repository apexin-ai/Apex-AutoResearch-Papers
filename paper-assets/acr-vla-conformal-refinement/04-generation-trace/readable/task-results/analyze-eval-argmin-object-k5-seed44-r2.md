# analyze eval argmin object k5 seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-argmin-object-k5-seed44-r2_20260519T191723_result.json`
- **Structured JSON:** [`1aaaf5830d640d28ff6f.json`](../../sessions/1a/1aaaf5830d640d28ff6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 总结

**eval-argmin-object-k5-seed44-r2: SR = 11%**

Per-task breakdown:
| Task | SR |
|---|---|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 10% |
| bbq_sauce | 20% |
| ketchup | 0% |
| tomato_sauce | 10% |
| butter | 0% |
| milk | 30% |
| chocolate_pudding | 20% |
| orange_juice | 20% |

### 4-seed 对比 (K=5 argmin-only, LIBERO-Object)

| Seed | SR |
|---|---|
| 42 | 15% |
| 43 | 13% |
| 44 | **11%** |
| 45 | 13% |

**4-seed 均值: 13.0%，标准差: 1.63%**

seed44 略低于其他 seed，但在 1σ 范围内，结果一致。Argmin-only selection（K=5，无 CRM correction）在 LIBERO-Object 上提供约 13% 的 SR。

---
