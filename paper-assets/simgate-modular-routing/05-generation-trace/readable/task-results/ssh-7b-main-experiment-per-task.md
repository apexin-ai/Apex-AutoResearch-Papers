# ssh 7b main experiment per task

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-main-experiment-per-task_20260517T222132_result.json`
- **Structured JSON:** [`80713e1fb6c082265938.json`](../../sessions/80/80713e1fb6c082265938.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果写入 `artifacts/7b_main_per_task_death_rate.md`。

**关键发现：**

| 指标 | 值 |
|------|----|
| 7B overall DR | 42.9% (105/245) |
| 7B death-prone aggregate (excl. find-non-living-thing) | **51.2%** (105/205) |
| 7B DR range (death-prone tasks) | 45.0%–56.0% |

**重要发现：** 同一文件中 paired 72B (deterministic) 的 death rate 仅 16.3%（40/245），远低于任务描述中提供的 72B DR 值（25%–50%）。**提供的"72B DR"可能来自 `results/backbone_72b/` 独立实验（不同 N），不是同一批 episodes 的 paired 数据。** 建议确认论文中应引用哪组 72B 数据作为对比基准。

另外注意：每 task 实际 N=20（非预期的 22），find-non-living-thing N=40，lifespan-longest-lived N=25。

---
