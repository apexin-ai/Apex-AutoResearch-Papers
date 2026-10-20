# analysis excluded tasks data fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_excluded-tasks-data-fix_20260515T163652_result.json`
- **Structured JSON:** [`96c9872f2d6cb99e3956.json`](../../sessions/96/96c9872f2d6cb99e3956.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。以下是向 Director 汇报的结构化数据：

---

## 修正后关键统计值

### Included 11 tasks (plan_c 20-ep)

| Task | det_death% | Δnd | source |
|------|-----------|-----|--------|
| chemistry-mix | 25.0 | +1.69 | plan_c n=20 |
| find-animal | 25.0 | +1.67 | plan_c n=20 |
| find-non-living-thing | 0.0 | +9.58 | plan_c n=40 |
| freeze | 25.0 | +0.44 | plan_c n=20 |
| grow-fruit | 20.0 | −0.64 | plan_c n=20 |
| identify-life-stages-1 | 10.0 | +2.78 | plan_c n=20 |
| identify-life-stages-2 | 20.0 | −1.20 | plan_c n=20 |
| inclined-plane-determine-angle | 20.0 | +1.25 | plan_c n=20 |
| lifespan-longest-lived | 16.0 | +2.59 | plan_c n=25 |
| lifespan-longest-lived-then-shortest-lived | 10.0 | +6.44 | plan_c n=20 |
| measure-melting-point-unknown-substance | 25.0 | −0.56 | plan_c n=20 |
| **Mean** | **17.82%** | **+2.19** | |
| **Δnd=0 count** | | **0/11** | |

### Excluded 19 tasks (mvp 20-ep + prescreening 5-9-ep)

| Metric | Value |
|--------|-------|
| mean det_death_rate | 14.89% |
| mean det_mean_score | −13.98 |
| Δnd=0 count | 10/19 |
| tasks det_death≥20% | 10/19 |

### 四个修正的具体问题

| 问题 | 旧值 | 修正值 | 原因 |
|------|------|--------|------|
| **Included det_death_rate mean** | 3.8% | 17.82% | 旧版混用了 prescreening 5-ep 数据；20-ep 数据 death rate 显著更高 |
| **measure-melting-point-unknown delta_nd** | 16.5 | −0.56 | 16.5 无法溯源，任何数据源都不匹配；plan_c 20-ep 值为 −0.56 |
| **Group C "均得分 0.0" 描述** | "两种策略均得分 0.0" | "6/7 得分 0.0；use-thermometer 例外 (det_nd=0.75, int_nd=1.50)" | use-thermometer 有微小非零分 |
| **核心叙事** | "excluded 死亡率更高 (15.5% vs 3.8%)" | "两组死亡率相近；关键区分是 routing signal：included 全部 Δnd≠0, excluded 53% 为 Δnd=0" | 20-ep 数据推翻了死亡率差异叙事 |

### measure-melting-point-unknown-substance delta_nd 各数据源

| 数据源 | n | delta_nd |
|--------|---|---------|
| prescreening (first 5-ep) | 5 | +9.83 |
| prescreening (all 9-ep) | 9 | +7.93 |
| **plan_c (20-ep, 最终采用)** | **20** | **−0.56** |
| 旧分析声称 | ? | 16.5 (无法验证) |

---
