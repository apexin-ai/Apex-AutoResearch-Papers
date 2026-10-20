# analysis plan 005 routing patterns v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-005-routing-patterns-v2_20260515T173050_result.json`
- **Structured JSON:** [`a2b45731b44a9fbc13ac.json`](../../sessions/a2/a2b45731b44a9fbc13ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果摘要

**数据集**: 11 tasks, 245 episodes（完整 plan_c 数据）

### A. Per-task routing frequency
- **5 death-dominated** (DAF ≥ 0.95): inclined-plane, freeze, melt-pt, life-stages-2, grow-fruit
- **6 genuine-det** (0 < DAF < 0.95): 包括 find-non-living-thing (DAF=0, 零死亡任务)
- Weighted DAF = **0.9614**, Weighted Δ(D-I) = **29.60** — 与 C1 claim 精确匹配
- 死亡率: internal 42.9% vs deterministic 16.3% (2.62×)

### B. Episode phase analysis
- **100% 的死亡发生在 late phase**（终端步骤）— ScienceWorld 的致死 action 直接结束 episode
- 分数在 step 8-9 开始分化（internal 开始落后）
- Internal 死亡时只走了 deterministic 的 **65% 步数**（mean 19.4 vs 30 steps）

### C. 生成 3 张图
- `routing_heatmap.pdf/png` — 三面板主图（death rate / label distribution / DAF）
- `phase_heatmap.pdf/png` — 阶段性死亡差异热力图
- `daf_scatter.pdf/png` — DAF vs 死亡率差散点图

### D. Failure taxonomy
- **100%** 死亡来自 `focus on &lt;location>` 动作（task-independent）
- 主导模式: **exploration loop** (68%) — agent 在非目标区域间反复导航直到触发致死
- Top 致死位置: workshop (21×), inventory (15×), kitchen (11×)

报告已写入 `artifacts/plan005_routing_patterns_v2.md`，JSON 数据在服务器 `artifacts/plan005_v2_summary.json`。

---
