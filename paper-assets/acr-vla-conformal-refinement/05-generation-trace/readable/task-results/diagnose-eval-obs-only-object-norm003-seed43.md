# diagnose eval obs only object norm003 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm003-seed43_20260520T193843_result.json`
- **Structured JSON:** [`d560c8ffc262de2e06b8.json`](../../sessions/d5/d560c8ffc262de2e06b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验已正常完成，不是失败。** Cron 误报——进程正常退出（return_code=0），结果 JSON 已写入。

### 结果

- **Overall SR: 14.0% (14/100)**
- per_task 分布（10 tasks × 10 rollouts）：

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| ketchup | 0% |
| tomato_sauce | 10% |
| butter | 10% |
| salad_dressing | 20% |
| milk | 20% |
| chocolate_pudding | 20% |
| bbq_sauce | 30% |
| orange_juice | 30% |

### 结论

- 实验完整跑完 10 tasks × 10 rollouts = 100 episodes，结果 JSON 已保存
- Registry 的 `conclusion=success` 是正确的，但缺 W&B metrics 导致 Cron 误判为异常
- **无需重新提交**

---
