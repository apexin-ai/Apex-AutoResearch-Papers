# analyze eval supp k2mean goal s43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-k2mean-goal-s43_20260523T111919_result.json`
- **Structured JSON:** [`79adb153d3c59678418c.json`](../../sessions/79/79adb153d3c59678418c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval-supp-k2mean-goal-s43 结果**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **81.5%** (163/200) |
| Baseline (Goal VLA-only) | 83.5% |
| **差异** | -2.0pp |

**Per-task:**

| Task | SR |
|------|-----|
| put_the_bowl_on_the_stove | 95% |
| push_the_plate_to_the_front_of_the_stove | 95% |
| turn_on_the_stove | 95% |
| put_the_bowl_on_the_plate | 95% |
| put_the_wine_bottle_on_top_of_the_cabinet | 90% |
| put_the_bowl_on_top_of_the_cabinet | 90% |
| put_the_wine_bottle_on_the_rack | 85% |
| open_the_middle_drawer_of_the_cabinet | 70% |
| open_the_top_drawer_and_put_the_bowl_inside | 55% |
| put_the_cream_cheese_in_the_bowl | 45% |

**Conclusion: success** — 81.5% 与 baseline 83.5% 差 2pp，在 seed 方差范围内，K=2 mean 未显著改变 Goal 性能，符合 baseline 确认预期。Registry 已更新为 DONE，cron 已删除。

---
