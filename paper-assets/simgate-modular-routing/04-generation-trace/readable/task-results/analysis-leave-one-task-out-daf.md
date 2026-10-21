# analysis leave one task out daf

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_leave-one-task-out-daf_20260518T194504_result.json`
- **Structured JSON:** [`04a4897723958c31fb95.json`](../../sessions/04/04a4897723958c31fb95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Full DAF = 78.9%** (75 death-asymmetry / 95 decisive episodes)，验证通过。

| Leave-one-out 结论 | |
|---|---|
| 10 个 death-prone tasks | 移除任意一个，DAF 变化 ≤ 3.0 pp (range: 75.9%--78.9%) |
| find-non-living-thing | 唯一 death-free task，贡献全部 20 个 score-comparison episodes；移除后 DAF = 100% (by construction) |

关键发现：DAF 对 task 组成高度稳健。find-non-living-thing 的 +21.1 pp 跳变恰好说明为什么 DAF 不是 100%（唯一一个 death-free task 提供了所有非死亡路由信号），这反而强化了 death dominance 的叙事。

产出：
- LaTeX table → `artifacts/appendix/leave_one_task_out_daf_table.tex` (art_20260518_8eda42)
- JSON data → `artifacts/appendix/leave_one_task_out_daf_data.json` (art_20260518_1d2974)

---
