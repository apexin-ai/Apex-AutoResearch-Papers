# analysis bjb1 32546 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bjb1-32546-batch_20260520T145705_result.json`
- **Structured JSON:** [`6eb90d9d908521277bc9.json`](../../sessions/6e/6eb90d9d908521277bc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 3 个实验均正常完成（EXIT_CODE=0），JSON 和日志一致。

---

```
exp_id: eval-vla-only-goal-seed51
success_rate: 0.69
conclusion: success
checkpoint_path: N/A (eval only)
log_path: ~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed51.log

exp_id: eval-vla-only-object-seed48-r2
success_rate: 0.11
conclusion: success
checkpoint_path: N/A (eval only)
log_path: ~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed48-r2.log

exp_id: eval-obs-only-object-norm02-seed50
success_rate: 0.18
conclusion: success
checkpoint_path: N/A (eval only)
log_path: ~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed50.log
```

### Per-task breakdown

**eval-vla-only-goal-seed51** (SR=69%):

| Task | SR |
|---|---|
| put_the_bowl_on_the_plate | 100% |
| open_the_middle_drawer_of_the_cabinet | 90% |
| put_the_bowl_on_the_stove | 90% |
| push_the_plate_to_the_front_of_the_stove | 90% |
| turn_on_the_stove | 80% |
| put_the_wine_bottle_on_the_rack | 70% |
| put_the_bowl_on_top_of_the_cabinet | 60% |
| put_the_wine_bottle_on_top_of_the_cabinet | 40% |
| open_the_top_drawer_and_put_the_bowl_inside | 40% |
| put_the_cream_cheese_in_the_bowl | 30% |

**eval-vla-only-object-seed48-r2** (SR=11%):

| Task | SR |
|---|---|
| chocolate_pudding | 40% |
| orange_juice | 20% |
| cream_cheese / salad_dressing / bbq_sauce / tomato_sauce / milk | 10% each |
| alphabet_soup / ketchup / butter | 0% |

**eval-obs-only-object-norm02-seed50** (SR=18%):

| Task | SR |
|---|---|
| bbq_sauce | 50% |
| milk | 30% |
| chocolate_pudding | 30% |
| salad_dressing / orange_juice | 20% each |
| cream_cheese / tomato_sauce / butter | 10% each |
| alphabet_soup / ketchup | 0% |

### 关键对比

- **Goal VLA-only seed51 (69%) vs CRM obs_only Goal seed51 (66%)**: VLA baseline 略高于 CRM，CRM 在 Goal 上未显示优势。
- **Object VLA-only seed48 r2 (11%) vs 前次 (10%)**: 重跑结果一致，确认 sr≈11% 不是 process death 导致的异常，这就是 Object VLA-only 的真实水平。
- **Object CRM obs_only norm02 seed50 (18%) vs VLA-only Object (~11%)**: CRM 在 Object 上提升 +7pp，bbq_sauce 从 10%→50% 提升最显著。

---
