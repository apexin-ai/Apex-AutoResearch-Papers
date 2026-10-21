# analysis fnlt zero death analysis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fnlt-zero-death-analysis_20260518T214427_result.json`
- **Structured JSON:** [`9e56870e08dadae14f81.json`](../../sessions/9e/9e56870e08dadae14f81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**`focus on` 是所有 11 tasks 中唯一的死亡机制**（146 次死亡全部来自 `focus on`，0 次来自其他 action）。find-non-living-thing 使用 `focus on` 105 次（比任何 death-prone task 都多），却 0 次致死。

原因是 **ScienceWorld 的 task-dependent `focus on` 语义**：
- 相同的 `focus on inventory` 在 freeze/chemistry-mix 中 → 死亡（-100 分），在 find-non-living-thing 中 → 中性（0 分）
- find-non-living-thing 的目标类别（非生物）是环境中的**绝对多数类**：房间、家具、工具、食物等几乎都是非生物
- 对比 find-animal：动物是**少数类**，随机 `focus on` 绝大多数命中非动物 → 死亡率 45%

这使得 find-non-living-thing 成为 death dominance 结论的**天然控制组**：大量使用致死 action，但因 task 结构使死亡不可能发生，证明死亡需要 `focus on` + 特定 task context 两个条件同时满足。

报告已保存到 `artifacts/appendix/fnlt_zero_death_analysis.md` 并注册。

---
