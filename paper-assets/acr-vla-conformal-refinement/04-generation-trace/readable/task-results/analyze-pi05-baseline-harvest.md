# analyze pi05 baseline harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-baseline-harvest_20260521T121905_result.json`
- **Structured JSON:** [`33e1dc1a14098ba328d6.json`](../../sessions/33/33e1dc1a14098ba328d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6/6 实验全部更新为 DONE。汇总：

```
Object seeds:  seed42=82.0%, seed43=81.5%, seed44=81.0% → mean=81.5%±0.5%
Spatial seeds: seed42=84.5%, seed43=83.0%, seed45=85.0% → mean=84.2%±1.0%
```

**Per-task breakdown (Object):**
| Task | s42 | s43 | s44 |
|------|-----|-----|-----|
| alphabet_soup | 85 | 80 | 85 |
| cream_cheese | 100 | 95 | 95 |
| salad_dressing | 60 | 70 | 65 |
| bbq_sauce | 80 | 85 | 80 |
| ketchup | 80 | 80 | 85 |
| tomato_sauce | 55 | 60 | 55 |
| butter | 100 | 95 | 90 |
| milk | 80 | 80 | 85 |
| chocolate_pudding | 100 | 100 | 100 |
| orange_juice | 80 | 70 | 70 |

**Per-task breakdown (Spatial):**
| Task | s42 | s43 | s45 |
|------|-----|-----|-----|
| between_plate_ramekin | 95 | 95 | 95 |
| next_to_ramekin | 90 | 90 | 90 |
| table_center | 100 | 95 | 100 |
| on_cookie_box | 90 | 95 | 100 |
| top_drawer | 75 | 70 | 60 |
| on_ramekin | 25 | 20 | 30 |
| next_to_cookie_box | 100 | 100 | 100 |
| on_stove | 90 | 95 | 100 |
| next_to_plate | 90 | 85 | 90 |
| on_wooden_cabinet | 90 | 85 | 85 |

Spatial 的 `on_ramekin` 任务跨 seed 一致性地低（25±5%），是 π0.5 的弱项。

---
