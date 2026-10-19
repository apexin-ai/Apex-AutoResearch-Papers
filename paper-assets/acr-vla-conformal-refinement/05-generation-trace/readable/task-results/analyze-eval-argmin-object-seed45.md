# analyze eval argmin object seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-argmin-object-seed45_20260517T003321_result.json`
- **Structured JSON:** [`a543a226422e78e82fd1.json`](../../sessions/a5/a543a226422e78e82fd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 保存到了相对路径 `logs/eval_object_argmin_seed45.json`（相对于运行时工作目录），不在 `~/runs/` 下。无论如何，log 已包含完整结果。

## 结果：argmin baseline (reconvla K=10) — LIBERO Object — seed=45

**Overall SR: 12.0% (12/100)**

| Task | SR |
|------|-----|
| pick_up_the_alphabet_soup | 0% (0/10) |
| pick_up_the_cream_cheese | 0% (0/10) |
| pick_up_the_salad_dressing | 10% (1/10) |
| pick_up_the_bbq_sauce | **40%** (4/10) |
| pick_up_the_ketchup | 0% (0/10) |
| pick_up_the_tomato_sauce | 0% (0/10) |
| pick_up_the_butter | 10% (1/10) |
| pick_up_the_milk | 10% (1/10) |
| pick_up_the_chocolate_pudding | 30% (3/10) |
| pick_up_the_orange_juice | 20% (2/10) |

- **总 rollouts**: 100 (10 tasks × 10 rollouts)
- **异常**: 仅有一个 deprecation warning (`swigvarlink has no __module__ attribute`)，无实质性 error
- **退出码**: 0（正常完成）

---
