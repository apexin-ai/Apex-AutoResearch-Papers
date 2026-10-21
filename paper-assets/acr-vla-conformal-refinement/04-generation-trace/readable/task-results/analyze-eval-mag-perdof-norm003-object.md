# analyze eval mag perdof norm003 object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-mag-perdof-norm003-object_20260516T081059_result.json`
- **Structured JSON:** [`91ef56c830d8ac31fe73.json`](../../sessions/91/91ef56c830d8ac31fe73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

**perdof norm=0.03, LIBERO object, overall_sr = 14%**

Per-task breakdown:
| Task | SR |
|------|-----|
| chocolate_pudding | 40% |
| salad_dressing | 20% |
| bbq_sauce | 20% |
| butter | 20% |
| ketchup | 10% |
| tomato_sauce | 10% |
| milk | 10% |
| orange_juice | 10% |
| alphabet_soup | 0% |
| cream_cheese | 0% |

## Magnitude sweep 对比

| Method | norm=0.03 | norm=0.1 | norm=0.2 |
|--------|-----------|----------|----------|
| **perdof** | **14%** | 11% | 11% |
| obs_only | 16% | — | — |
| argmin baseline | 12% | 12% | 12% |

**分析：** perdof norm=0.03 得到 14%，略高于 norm=0.1/0.2 的 11%，说明更小的 correction norm 对 perdof 稍有帮助（减少过度修正）。但仍低于 obs_only norm=0.03 的 16%，差距 2pp。整体趋势一致：obs_only 在小 norm 区间优于 perdof，两者都仅略优于 argmin baseline（12%），表明 norm 限制下 CRM correction 的增益有限。

---
