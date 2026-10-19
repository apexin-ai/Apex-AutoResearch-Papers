# analyze eval obs only object default seed45 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-object-default-seed45-r2_20260519T042340_result.json`
- **Structured JSON:** [`69f31b3172534b9ffdf8.json`](../../sessions/69/69f31b3172534b9ffdf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B 查询工具有内部错误，跳过。已从 log 和 JSON 获取到完整结果。

## 实验结果: eval-obs-only-object-default-seed45-r2

**Overall success rate: 18.0% (18/100)**

| Task | SR | Successes/Total |
|---|---|---|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| salad_dressing | 30% | 3/10 |
| bbq_sauce | 30% | 3/10 |
| ketchup | 10% | 1/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 10% | 1/10 |
| milk | 20% | 2/10 |
| chocolate_pudding | 40% | 4/10 |
| orange_juice | 30% | 3/10 |

**执行状态:** EXIT_CODE=0，无错误/警告，output JSON 已保存。10 tasks × 10 rollouts = 100 rollouts 全部完成。

**与已有数据对比 (obs_only default norm):**

| Seed | SR | n_rollouts | 备注 |
|---|---|---|---|
| seed42 | 20% | 10 | |
| seed43 | 20% | 10 | |
| seed44 | 10% | 10 | |
| seed45 (原始) | 12% | 20 | 非标准 |
| **seed45-r2** | **18%** | **10** | 本次标准化重跑 |

**结论: success**

- seed45 标准化重跑得到 18%，高于原始的 12%（但原始用 n_rollouts=20，方差不同）
- 加入 seed45-r2 后，obs_only default 4 seeds 均值: (20 + 20 + 10 + 18) / 4 = **17.0%**
- 结果合理，无异常，实验有效。

---
