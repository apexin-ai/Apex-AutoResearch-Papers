# code plan 005 routing pattern

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-005-routing-pattern_20260513T233251_result.json`
- **Structured JSON:** [`59d2657b99ccecac3d6e.json`](../../sessions/59/59d2657b99ccecac3d6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行成功。结果摘要：

**数据**: 314 episodes, 30 tasks

**分类分布**:
- death-dominated: 25 tasks (DAF ≥ 95%)
- genuine-det: 3 tasks (find-living-thing, find-plant, measure-melting-point-unknown-substance)
- internal-preferred: 2 tasks (find-non-living-thing, grow-plant)

**Failure taxonomy**: 所有 death 均由 `focus on &lt;location>` 动作触发，internal 模式 144 次 vs deterministic 37 次。最常见致死动作：`focus on workshop` (45 int / 5 det)。

**输出文件**:
- `results/plan005/routing_metrics.json` — 30 tasks 的 per-task metrics
- `results/plan005/fig_routing_heatmap.{pdf,png}` — routing heatmap 图
- `results/plan005/failure_taxonomy.json` — failure mode taxonomy

本地文件: `src/routing_pattern_analysis.py` 已创建。

---
