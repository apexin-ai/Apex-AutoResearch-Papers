# research d028 number consistency audit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d028-number-consistency-audit_20260514T075449_result.json`
- **Structured JSON:** [`72f738126d5e86795883.json`](../../sessions/72/72f738126d5e86795883.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**根因**：项目存在 3 套数据源被混用——A (11 tasks/245 eps)、B (30 tasks/249 eps)、C (11 tasks/194 eps)。

**6 项不一致**：
1. **最严重**：`death_decomposition_report.json` 用的是 30-task prescreening 数据（Δ=38.33, r=0.9864），不是 plan-012-full 的 11-task 数据（Δ=29.60, r=0.9698）。文件名极易混淆。
2. 245 vs 194 episodes 差异：plan-001b 后续追加了 51 episodes（rebalance），plan-003 baseline 在追加前跑的。
3. `plan005/routing_metrics.json` 混合了 prescreening 和 plan-001b 数据。
4. rule_based_accuracy 三版本 episode 数各不相同（204/203/225）。
5. 死亡率指标命名不统一（catastrophic_failure_rate vs death_rate）。
6. trained-router 完全退化（与 always-det 完全相同）。

**论文写作建议**：decomposition 用 plan-012-full (245 eps) 数字，baselines 用 plan-003 (194 eps) 数字，但需注明两组数字基于不同 episode 集合。

报告已保存为 artifact `art_20260514_e311aa`。

---
