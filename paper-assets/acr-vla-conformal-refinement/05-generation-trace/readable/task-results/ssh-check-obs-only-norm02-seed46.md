# ssh check obs only norm02 seed46

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-obs-only-norm02-seed46_20260517T050611_result.json`
- **Structured JSON:** [`5b0b4addd9e408007276.json`](../../sessions/5b/5b0b4addd9e408007276.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果: eval-obs-only-object-norm02-seed46

**Overall Success Rate: 15.0% (15/100)**

### Per-task Breakdown

| Task | SR | Successes |
|------|-----|-----------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| salad_dressing | 20% | 2/10 |
| bbq_sauce | 30% | 3/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 10% | 1/10 |
| milk | 10% | 1/10 |
| chocolate_pudding | 40% | 4/10 |
| orange_juice | 30% | 3/10 |

### Conclusion: **negative**

实验正常完成（exit code 0，JSON 已保存），但 SR=15.0% 略低于 obs_only 预期范围（16-22%）。表现分布不均匀：3 个 task 完全失败（0%），2 个 task 表现较好（30-40%），其余在 10-20%。

---
