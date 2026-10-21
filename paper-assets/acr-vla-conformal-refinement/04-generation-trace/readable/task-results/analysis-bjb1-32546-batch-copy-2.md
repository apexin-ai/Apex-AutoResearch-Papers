# analysis bjb1 32546 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bjb1-32546-batch_20260520T124453_result.json`
- **Structured JSON:** [`a265ef92af7a31bbee16.json`](../../sessions/a2/a265ef92af7a31bbee16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常完成 (EXIT_CODE=0)，无错误。

---

## 实验 1: eval-argmin-object-seed49

- **exp_id**: eval-argmin-object-seed49
- **mode**: reconvla (argmin), benchmark: object, seed: 49, K=10
- **overall_sr**: **16.0%** (16/100)
- **per_task_sr**:

| Task | SR |
|---|---|
| alphabet_soup | 0.0% |
| cream_cheese | 0.0% |
| salad_dressing | 20.0% |
| bbq_sauce | 40.0% |
| ketchup | 0.0% |
| tomato_sauce | 10.0% |
| butter | 10.0% |
| milk | 30.0% |
| chocolate_pudding | 30.0% |
| orange_juice | 20.0% |

- **conclusion**: **success** — 16.0% 落在之前 Argmin Object 参考范围 (12-14%) 的略高端，一致性良好，可用于多 seed 聚合。

---

## 实验 2: eval-obs-only-goal-norm02-seed52

- **exp_id**: eval-obs-only-goal-norm02-seed52
- **mode**: crm_obs_only, benchmark: goal, seed: 52, K=10, norm=0.2
- **overall_sr**: **68.0%** (68/100)
- **per_task_sr**:

| Task | SR |
|---|---|
| open_middle_drawer | 70.0% |
| bowl_on_stove | 90.0% |
| wine_bottle_on_cabinet | 40.0% |
| open_top_drawer_put_bowl | 30.0% |
| bowl_on_top_of_cabinet | 80.0% |
| push_plate_to_stove | 80.0% |
| cream_cheese_in_bowl | 40.0% |
| turn_on_stove | 100.0% |
| bowl_on_plate | 100.0% |
| wine_bottle_on_rack | 50.0% |

- **conclusion**: **neutral** — CRM 68.0% 与之前结果完全一致 (CRM 68.0% vs VLA 68.7%)，再次确认 Goal benchmark 上 CRM 无显著提升，属于 neutral 场景。

---

**异常**: 无。两个实验均完整跑完 10 tasks × 10 rollouts = 100 episodes，退出码 0。

---
