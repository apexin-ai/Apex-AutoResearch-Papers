# eval plan016v2 topic perturbation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan016v2-topic-perturbation_20260518T064402_result.json`
- **Structured JSON:** [`0863d6f79a21b0cbde0e.json`](../../sessions/08/0863d6f79a21b0cbde0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果总结：**

| Model | Delta (full) | 排序 |
|---|---|---|
| Persuasion treatment | 0.000 | 最佳（零退化） |
| Jailbreak MLM (017) | -0.026 | 轻度退化 |
| **Topic (016v2)** | **-0.040** | 中度退化 |
| Vanilla baseline | -0.118 | 严重退化 |
| Wikipedia MLM (018) | -0.121 | 严重退化 |

**假设被拒**：Topic model delta=-0.040，远好于预期的 vanilla 水平（-0.118）。Topic classification fine-tuning 确实学到了一定程度的 lexically-invariant features，但 persuasion treatment（0.000）仍然严格优于所有其他方法。

产出：
- 脚本：`src/plan_016v2_perturbed_eval.py`
- 结果：`results/plan_016v2_topic_perturbation.json`
- Registry：`plan_016v2_topic_perturbation` (DONE, negative)

---
