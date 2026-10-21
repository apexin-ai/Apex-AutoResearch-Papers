# ssh check direct correction r3 log

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-direct-correction-r3-log_20260517T044728_result.json`
- **Structured JSON:** [`5a6c12238bdc4498b7f3.json`](../../sessions/5a/5a6c12238bdc4498b7f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果: eval-direct-correction-object-seed42-r3

**Overall Success Rate: 14.0% (14/100)**

### Per-task breakdown (10 rollouts each):

| Task | SR | Successes |
|------|-----|-----------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 10% | 1/10 |
| salad_dressing | 10% | 1/10 |
| bbq_sauce | **40%** | 4/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 10% | 1/10 |
| milk | 10% | 1/10 |
| chocolate_pudding | **30%** | 3/10 |
| orange_juice | 20% | 2/10 |

### Conclusion: **success**

实验正常完成，SR = 14%，高于 VLA-only baseline (12%)。提升 2 个百分点，幅度不大但方向为正。bbq_sauce (40%) 和 chocolate_pudding (30%) 表现最好，alphabet_soup 和 ketchup 完全失败 (0%)。

---
