# analysis excluded 19 tasks

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_excluded-19-tasks_20260515T161414_result.json`
- **Structured JSON:** [`115e21ffc5cd296de52d.json`](../../sessions/11/115e21ffc5cd296de52d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是结果摘要：

---

## 30 Task 分类总览

**Included (11)**: chemistry-mix, find-animal, find-non-living-thing, freeze, grow-fruit, identify-life-stages-1/2, inclined-plane-determine-angle, lifespan-longest-lived, lifespan-longest-lived-then-shortest-lived, measure-melting-point-unknown-substance

**Excluded (19)** 分三组：

### Group A: MVP 开发数据 (5 tasks)
boil, melt, change-the-state-of-matter-of, chemistry-mix-paint-secondary-color, grow-plant
→ 管线开发阶段用过，排除防止循环评估

### Group B: 家族冗余变体 (7 tasks)
chemistry-mix-paint-tertiary-color, find-living-thing, find-plant, inclined-plane-friction-named/unnamed-surfaces, lifespan-shortest-lived, measure-melting-point-known-substance
→ 同一 task family 保留 1 个代表，避免 correlated variants 膨胀样本量

### Group C: Agent 能力天花板 (7 tasks)
mendelian-genetics-known/unknown-plant, power-component/renewable, test-conductivity/unknown, use-thermometer
→ 两种策略在非死亡 episode 中均得分 0.0，7B backbone 无法完成这些任务，routing 无信号可学

## 关键统计对比

| 指标 | Included (11) | Excluded (19) |
|------|--------------|---------------|
| det_death_rate mean | **3.8%** | 15.5% |
| det_mean_score | **+3.22** | -14.61 |
| det_death ≥ 20% | 2/11 | 10/19 |
| Δ_nd = 0 | 9/11 | 14/19 |

## 排除标准合理性
排除 **不会偏向** death-avoidance 结论——included 集合保留了 find-non-living-thing（零死亡、internal 更优）和 measure-melting-point-unknown-substance（Δ_nd=16.5）。纳入 Group C 反而会 **强化** death-dominance claim（7 个全部 DAF=100%）。

## 论文文本
Appendix 和 Limitations 两个版本已写入 `artifacts/excluded_tasks_analysis.md`。

---
