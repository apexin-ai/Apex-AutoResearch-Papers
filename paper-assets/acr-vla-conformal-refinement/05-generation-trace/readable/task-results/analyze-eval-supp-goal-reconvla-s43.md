# analyze eval supp goal reconvla s43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-goal-reconvla-s43_20260523T113014_result.json`
- **Structured JSON:** [`e59abc52637fadc56010.json`](../../sessions/e5/e59abc52637fadc56010.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval-supp-goal-reconvla-s43 结果：SR = 81.0% (162/200)，conclusion = negative**

| Task | SR |
|------|-----|
| open_the_middle_drawer_of_the_cabinet | 65% |
| put_the_bowl_on_the_stove | 95% |
| put_the_wine_bottle_on_top_of_the_cabinet | 85% |
| open_the_top_drawer_and_put_the_bowl_inside | 50% |
| put_the_bowl_on_top_of_the_cabinet | 95% |
| push_the_plate_to_the_front_of_the_stove | 90% |
| put_the_cream_cheese_in_the_bowl | 55% |
| turn_on_the_stove | 95% |
| put_the_bowl_on_the_plate | 95% |
| put_the_wine_bottle_on_the_rack | 85% |

对比：
- s42 = 81.0%, s43 = 81.0%（完全一致）
- 两 seed 平均 81.0%，低于 VLA-only baseline 83.5% **-2.5pp**
- Reconvla 在 Goal suite 上表现稳定但一致性地低于 baseline，结论为 **negative**

Registry 已更新，cron 已删除。

---
