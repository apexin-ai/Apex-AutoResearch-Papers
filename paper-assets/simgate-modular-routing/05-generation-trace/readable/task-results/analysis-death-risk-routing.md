# analysis death risk routing

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_death-risk-routing_20260517T090340_result.json`
- **Structured JSON:** [`016fa3553c04c93a9ea6.json`](../../sessions/01/016fa3553c04c93a9ea6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整。总结：

---

## 结果

```
=== Death-Risk Threshold Routing ===
Baselines: always-det = -9.47, always-internal = -39.07

245 episodes, 11 task types (skipped 30 deep_internal-only episodes)
```

**关键发现：threshold routing 无法优于 always-det。**

- 唯一 death_rate=0 的 task type 是 `find-non-living-thing`（internal mean=+18.9, det mean=+28.5）
- 其余 10 个 task types 的 internal death rate 均在 45-56%，全部高于任何合理 threshold
- 最优 threshold=0.0（即：只要 death rate > 0 就路由到 det），只有 find-non-living-thing 走 internal
- 最优得分 = **-11.03**，比 always-det (-9.47) 差 1.56 分
- 原因：find-non-living-thing 用 internal (+18.9) 不如用 det (+28.5)，所以混合反而降分

**Bootstrap CI**: difference = -1.57, 95% CI = [-8.87, +5.92]，不显著。

**结论**：基于 task-type death risk 的 threshold routing 不能优于 always-det。唯一零死亡的 task type 在 internal 下的得分也低于 det，因此没有任何 threshold 能带来正向收益。这种简单的 per-task-type routing oracle 在当前数据集上是无效的。

---
