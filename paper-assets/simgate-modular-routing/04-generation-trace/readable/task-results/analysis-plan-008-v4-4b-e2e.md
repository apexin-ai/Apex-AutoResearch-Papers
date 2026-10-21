# analysis plan 008 v4 4b e2e

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-008-v4-4b-e2e_20260517T041811_result.json`
- **Structured JSON:** [`3955ffd3c86d0cc50d3c.json`](../../sessions/39/3955ffd3c86d0cc50d3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

| 指标 | 值 |
|------|-----|
| continuous_score_mean | **-10.72** |
| CI | [-15.69, -5.52] |
| delta_vs_always_det | **-1.25** (worse) |
| death_rate | 0.167 |
| success_rate | 0.207 |
| sim_ratio | 0.956 |
| fallback_rate | **68.0%** (187/275 episodes) |
| n_episodes | 275 |
| n_tasks | 11 |

## 结论判断

- 是否超过 always-det (-9.47)? **NO** (-10.72 < -9.47)
- 建议 conclusion: **negative**
- 与 1.7B router (-10.70) 对比: **持平** (-10.72 vs -10.70, 差异 0.02, 无统计意义)

## W&B run ID: 无（日志中未发现 wandb 链接）

---

**关键发现**:

1. **Fallback rate 68%** — 275 个 episode 中有 187 个没有 step data，被迫回退到 deterministic。这意味着 4B router 实际上只在 32% 的 episode 上真正做了 routing 决策，绝大多数 episode 退化为 always-det。
2. 即便如此，结果仍比 always-det 差 1.25 分，说明 router 在它确实介入的那 32% episode 中做出了负面决策。
3. 4B 与 1.7B router 的 e2e 表现几乎完全相同（-10.72 vs -10.70），capacity scaling 在 deployment 中没有产生任何增益。

**结论**: 进一步强化 analytical framework 的论点 — learned routing at all tested scales (1.7B, 4B) 在 end-to-end deployment 中均未超越 trivial always-det baseline，despite episode-level accuracy 提升（59% vs 55%）。Episode-level routing accuracy 无法转化为 deployment gain。

---
