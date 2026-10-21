# analysis pi05 goal batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-goal-batch_20260526T134324_result.json`
- **Structured JSON:** [`617e192dbc2eb5d888f3.json`](../../sessions/61/617e192dbc2eb5d888f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## π0.5 Goal Results

| exp_id | mode | seed | server | SR% | n_rollouts | n_tasks |
|--------|------|------|--------|-----|------------|---------|
| pi05-crm-k2-goal-s42-bjb1-r2 | CRM | 42 | bjb1 | 82.5% | 20 | 10 |
| pi05-crm-k2-goal-s43-bjb1-r2 | CRM | 43 | bjb1 | 83.0% | 20 | 10 |
| pi05-crm-k2-goal-s44-bjb1-r2 | CRM | 44 | bjb1 | 85.0% | 20 | 10 |
| pi05-k2mean-goal-s42-r2 | K2-mean | 42 | cqa1 | 98.0% | 20 | 10 |

**CRM mean ± std: 83.5 ± 1.32%**
**K2-mean s42: 98.0%**

### Per-task breakdown

| Task | CRM s42 | CRM s43 | CRM s44 | CRM avg | K2-mean s42 |
|------|---------|---------|---------|---------|-------------|
| open_middle_drawer | 50% | 55% | 60% | 55.0% | 90% |
| bowl_on_stove | 100% | 95% | 100% | 98.3% | 100% |
| wine_bottle_on_cabinet | 65% | 75% | 70% | 70.0% | 95% |
| drawer_put_bowl | 65% | 65% | 70% | 66.7% | 95% |
| bowl_on_cabinet | 100% | 95% | 100% | 98.3% | 100% |
| plate_to_stove | 95% | 100% | 95% | 96.7% | 100% |
| cream_cheese_in_bowl | 95% | 100% | 100% | 98.3% | 100% |
| turn_on_stove | 100% | 100% | 100% | 100% | 100% |
| bowl_on_plate | 100% | 100% | 100% | 100% | 100% |
| wine_bottle_on_rack | 55% | 45% | 55% | 51.7% | 100% |

CRM always-on 在 Goal 上大幅低于 K2-mean baseline（83.5% vs 98.0%），主要掉分在 open_middle_drawer（55% vs 90%）、wine_bottle_on_rack（51.7% vs 100%）、wine_bottle_on_cabinet（70% vs 95%）、drawer_put_bowl（66.7% vs 95%）。

---
