# harvest eval obs only object norm003 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval-obs-only-object-norm003-seed44_20260520T105317_result.json`
- **Structured JSON:** [`f1d031a73ebee9190d66.json`](../../sessions/f1/f1d031a73ebee9190d66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

**eval-obs-only-object-norm003-seed44 结果汇总：**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **15.0% (15/100)** |
| **Conclusion** | **success** (> 12% baseline) |

**Per-task SR：**

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | **30%** |
| bbq_sauce | **20%** |
| ketchup | 0% |
| tomato_sauce | 10% |
| butter | 10% |
| milk | **20%** |
| chocolate_pudding | **30%** |
| orange_juice | **30%** |

**对比同 norm 的其他 seed：** norm003-seed43-r2 得 14%，norm003-seed44 得 15%，一致性好。比 norm005-seed44 的 12% 高 3pp，说明 ε=0.03 在 Object 上略优于 ε=0.05（可能因为更小 correction 减少了过度干预）。

---
