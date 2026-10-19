# diagnose eval obs only object norm003 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm003-seed43_20260520T193932_result.json`
- **Structured JSON:** [`7fed15cb2cdfb8f52123.json`](../../sessions/7f/7fed15cb2cdfb8f52123.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已确认完成，数据完整。

## 诊断结果

**状态：已正常完成。** 进程已退出，JSON 输出文件和 log 均完整。

### Metrics

- **overall_success_rate: 14.0% (14/100)**
- n_rollouts: 10 per task, 10 tasks, 100 total
- mode: crm_obs_only, benchmark: object, ε=0.03

### Per-task 分布

| Task | Success Rate | Successes/Total |
|------|-------------|-----------------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 10% | 1/10 |
| salad_dressing | 20% | 2/10 |
| milk | 20% | 2/10 |
| chocolate_pudding | 20% | 2/10 |
| bbq_sauce | 30% | 3/10 |
| orange_juice | 30% | 3/10 |

### Registry 状态

Registry 已有该实验记录，status=DONE, conclusion=success, metrics 已填充 `{success_rate: 0.14, n_rollouts: 100}`。Cron 之前误判 failed 的问题已不存在——registry 当前状态正确。

**不需要重跑。**

---
