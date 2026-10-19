# analyze eval obs only object norm02 k5 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-object-norm02-k5-seed44_20260518T205135_result.json`
- **Structured JSON:** [`77fe1a6e92518cd4e7fd.json`](../../sessions/77/77fe1a6e92518cd4e7fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B query is failing due to a tool issue. The log and JSON data are sufficient. Here are the results:

---

## 实验结果: eval-obs-only-object-norm02-k5-seed44

**conclusion: success** (17.0% > 11.6% VLA-only baseline)

**overall_success_rate: 17.0%** (17/100)

**n_tasks: 10**
**n_rollouts: 10 per task (100 total)**

### per_task_results

| Task | Success Rate | Successes/Total |
|------|-------------|----------------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 10% | 1/10 |
| salad_dressing | 10% | 1/10 |
| **bbq_sauce** | **40%** | **4/10** |
| ketchup | 0% | 0/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 10% | 1/10 |
| milk | 30% | 3/10 |
| chocolate_pudding | 30% | 3/10 |
| orange_juice | 30% | 3/10 |

### K=5 三 seed 汇总

| Seed | Success Rate |
|------|-------------|
| 42 | 14% |
| 43 | 19% |
| 44 | 17% |
| **Mean** | **16.7%** |
| **Std** | **2.5%** |

### 注意事项
- 实验正常完成，EXIT_CODE=0，无异常
- K=5 mean 16.7% vs K=10 (n=6) mean 17.5%，两者非常接近，差异在 noise 范围内
- W&B 查询因工具问题失败，数据仅来自日志和 JSON

---
