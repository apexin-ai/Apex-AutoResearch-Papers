# ssh 7b find nonliving death rate

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-find-nonliving-death-rate_20260517T215819_result.json`
- **Structured JSON:** [`4b019e9ddb6b94e19931.json`](../../sessions/4b/4b019e9ddb6b94e19931.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**find-non-living-thing: 7B death rate = 0%**（65 episodes across 3 experiments, 0 deaths）

这与 72B 一致，确认 find-non-living-thing 是天然 "non-death-prone" task——环境中根本不存在致死动作，与模型能力无关。

7B 其他 task 的 death rate 在 40%-60%（整体均值 55.6%），唯独 find-non-living-thing 为 0%。

结果已写入 `artifacts/7b_per_task_death_rate.md`。

---
