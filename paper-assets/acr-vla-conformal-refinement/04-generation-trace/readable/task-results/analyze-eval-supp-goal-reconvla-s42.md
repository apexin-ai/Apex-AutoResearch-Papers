# analyze eval supp goal reconvla s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-goal-reconvla-s42_20260523T100553_result.json`
- **Structured JSON:** [`8f190e1445607771db9b.json`](../../sessions/8f/8f190e1445607771db9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Goal Reconvla K=10 argmin, seed=42

**Overall: 81.0% (162/200)**

| Task | Success Rate | Successes/Total |
|------|-------------|-----------------|
| open_the_middle_drawer_of_the_cabinet | 75.0% | 15/20 |
| put_the_bowl_on_the_stove | 95.0% | 19/20 |
| put_the_wine_bottle_on_top_of_the_cabinet | 90.0% | 18/20 |
| open_the_top_drawer_and_put_the_bowl_inside | 50.0% | 10/20 |
| put_the_bowl_on_top_of_the_cabinet | 95.0% | 19/20 |
| push_the_plate_to_the_front_of_the_stove | 85.0% | 17/20 |
| put_the_cream_cheese_in_the_bowl | 45.0% | 9/20 |
| turn_on_the_stove | 100.0% | 20/20 |
| put_the_bowl_on_the_plate | 95.0% | 19/20 |
| put_the_wine_bottle_on_the_rack | 80.0% | 16/20 |

对比：Goal VLA-only=83.5%, Goal CRM=85.5%, **Goal Reconvla=81.0%**。Reconvla 在 Goal suite 上低于 VLA-only 2.5pp，低于 CRM 4.5pp。两个弱任务拖后腿：cream_cheese (45%) 和 top_drawer_bowl (50%)。

---
