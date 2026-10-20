# analysis plan 005 routing pattern

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-005-routing-pattern_20260514T014249_result.json`
- **Structured JSON:** [`20b35c3c0fb6828cb4a3.json`](../../sessions/20/20b35c3c0fb6828cb4a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。输出总结：

**30 tasks / 314 episodes 分析结果：**

| 分类 | Task 数 | 占比 |
|---|---|---|
| death-dominated | 25 | 83.3% |
| genuine-det | 3 | 10.0% |
| internal-preferred | 2 | 6.7% |

**C1 支持数据：** Weighted mean DAF = **98.09%**，其中 17/25 death-dominated tasks DAF = 1.0（非死亡优势完全为零）。Internal 死亡 144 次 vs deterministic 37 次（3.89x），失败模式全部为 focus-action 探索循环。

**输出文件（服务器 `results/plan005/analysis/`）：**
- `task_classification.json` — 30 tasks 分类 + 关键指标
- `heatmap_data.csv` — Figure 1 数据矩阵（DAF 降序）
- `taxonomy_summary.json` — 分类统计 + C1 claim 分析

**注意：** 与预分析（19 death-dominated / 5 genuine-det / 1 internal-preferred on 25 tasks）相比，新增 5 个 task 后 death-dominated 增加到 25，genuine-det 从 5 降到 3，internal-preferred 从 1 增到 2。整体结论更强化了 C1 claim。

---
