# collect goal r4 std 3seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_goal-r4-std-3seeds_20260522T164911_result.json`
- **Structured JSON:** [`4f81426a419491cad20c.json`](../../sessions/4f/4f81426a419491cad20c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个 seed 结果已收集，均为 n_rollouts=20。

## Per-Seed Results

| Task | Seed42 | Seed43 | Seed44 |
|------|--------|--------|--------|
| open_middle_drawer | 0.95 | 1.00 | 0.90 |
| put_bowl_on_stove | 1.00 | 1.00 | 1.00 |
| put_wine_bottle_on_cabinet | 0.95 | 0.95 | 1.00 |
| open_top_drawer_put_bowl | 1.00 | 0.90 | 0.85 |
| put_bowl_on_cabinet | 1.00 | 1.00 | 1.00 |
| push_plate_to_front_stove | 0.90 | 1.00 | 1.00 |
| put_cream_cheese_in_bowl | 1.00 | 1.00 | 1.00 |
| turn_on_stove | 1.00 | 1.00 | 1.00 |
| put_bowl_on_plate | 1.00 | 0.95 | 1.00 |
| put_wine_bottle_on_rack | 1.00 | 1.00 | 1.00 |
| **Overall SR** | **0.980** | **0.980** | **0.975** |

## 3-Seed Summary (Mean ± Std)

| Task | Mean | Std |
|------|------|-----|
| open_middle_drawer | 0.950 | 0.050 |
| put_bowl_on_stove | 1.000 | 0.000 |
| put_wine_bottle_on_cabinet | 0.967 | 0.029 |
| open_top_drawer_put_bowl | 0.917 | 0.076 |
| put_bowl_on_cabinet | 1.000 | 0.000 |
| push_plate_to_front_stove | 0.967 | 0.058 |
| put_cream_cheese_in_bowl | 1.000 | 0.000 |
| turn_on_stove | 1.000 | 0.000 |
| put_bowl_on_plate | 0.983 | 0.029 |
| put_wine_bottle_on_rack | 1.000 | 0.000 |
| **Overall SR** | **0.978 ± 0.003** | |

最弱任务是 `open_top_drawer_and_put_the_bowl_inside`（0.917 ± 0.076），其余 9 个任务均 ≥ 0.95。

---
