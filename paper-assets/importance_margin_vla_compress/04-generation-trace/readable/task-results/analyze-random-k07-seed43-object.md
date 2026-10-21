# analyze random k07 seed43 object

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_random_k07_seed43_object_20260525T123223_result.json`
- **Structured JSON:** [`1f1b15911fd593a5db71.json`](../../sessions/1f/1f1b15911fd593a5db71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果如下：

## random_k07_seed43_object 结果

**Overall: 51.2% (256/500)** | 耗时 270 min | 256→179 vision tokens (k=0.7)

| Task | SR | Succ/Ep |
|------|---:|--------:|
| orange juice | 84.0% | 42/50 |
| alphabet soup | 74.0% | 37/50 |
| ketchup | 72.0% | 36/50 |
| tomato sauce | 62.0% | 31/50 |
| salad dressing | 58.0% | 29/50 |
| bbq sauce | 56.0% | 28/50 |
| chocolate pudding | 42.0% | 21/50 |
| milk | 30.0% | 15/50 |
| butter | 20.0% | 10/50 |
| cream cheese | 14.0% | 7/50 |

**结论：success** — seed43 的 51.2% 与 seed7 的 49.0% 高度一致（差异仅 2.2pp），确认 random k=0.7 的退化模式跨 seed 稳定。随机丢弃 30% vision tokens 导致性能从 baseline 水平稳定下降到 ~50%，且 per-task 分布模式一致（cream cheese/butter/milk 始终是最弱的三个 task）。

---
