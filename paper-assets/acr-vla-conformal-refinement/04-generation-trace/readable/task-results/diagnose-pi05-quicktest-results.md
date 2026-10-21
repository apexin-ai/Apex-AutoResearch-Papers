# diagnose pi05 quicktest results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-quicktest-results_20260521T050912_result.json`
- **Structured JSON:** [`3262cb2b129c776e0989.json`](../../sessions/32/3262cb2b129c776e0989.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：eval-pi05-baseline-object-seed42-r2

**状态：已完成** (EXIT_CODE=0)

注意：PID 831620 当前正在运行一个**新的** quicktest（`--n_rollouts 5 --output_file logs/eval_pi05_quicktest.json`），不是 r2 实验。r2 实验已结束并写出 JSON。

### 每 task Success Rate（每 task 20 rollouts）

| Task | SR | Successes/Total |
|------|----|-----------------|
| pick_up_the_alphabet_soup | 0.0% | 0/20 |
| pick_up_the_cream_cheese | 0.0% | 0/20 |
| pick_up_the_salad_dressing | 0.0% | 0/20 |
| pick_up_the_bbq_sauce | 0.0% | 0/20 |
| pick_up_the_ketchup | 0.0% | 0/20 |
| pick_up_the_tomato_sauce | 0.0% | 0/20 |
| pick_up_the_butter | 0.0% | 0/20 |
| pick_up_the_milk | 0.0% | 0/20 |
| pick_up_the_chocolate_pudding | 0.0% | 0/20 |
| pick_up_the_orange_juice | 0.0% | 0/20 |

### Overall SR: **0.0% (0/200)**

### 结论

**全 10 task 均为 0% SR，无任何信号。** 200 次 rollout 中无一成功。日志中还出现了 CUDA OOM 错误（部分 rollout 在 step 0 就因显存不足崩溃），说明即使不 OOM 的 rollout 也全部失败。

按照 Director 的 GO/NO-GO 标准：**NO-GO，应关闭 π0.5 线。**

---
