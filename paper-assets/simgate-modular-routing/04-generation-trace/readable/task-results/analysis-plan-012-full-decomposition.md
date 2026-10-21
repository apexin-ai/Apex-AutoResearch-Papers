# analysis plan 012 full decomposition

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-012-full-decomposition_20260514T053649_result.json`
- **Structured JSON:** [`b06dc877b1d7296ea71c.json`](../../sessions/b0/b06dc877b1d7296ea71c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量分析完成。结果汇总：

## Death Decomposition 全量结果（11 tasks, 245 episodes）

### 核心指标

| 指标 | 值 | 预分析(10 tasks) | 变化 |
|------|-----|------------------|------|
| **Δ_full** (det-int) | **+29.60** | +29.85 | -0.25 |
| **Δ_nd** (no-death) | **+2.84** | +2.95 | -0.11 |
| **Death avoidance fraction** | **90.41%** | 90.1% | +0.31pp |
| **Pearson r** | **0.9698** | 0.967 | +0.003 |
| **p-value** | **8.12e-07** | — | — |

### Death rate
- Internal: 42.9%
- Deterministic: 16.3%

### Label 分布
- det-preferred: 86
- internal-preferred: 9
- no-preference: 150

### Per-task breakdown

| Task | N | DR_int | DR_det | Δ_full | Δ_nd | Δ_pr | det/int/no |
|------|---|--------|--------|--------|------|------|------------|
| chemistry-mix | 20 | 0.45 | 0.25 | 21.8 | 0.0 | 1.8 | 6/2/12 |
| find-animal | 20 | 0.50 | 0.25 | 26.65 | 0.0 | 1.65 | 5/0/15 |
| **find-non-living-thing** | 40 | **0.0** | **0.0** | **9.58** | **9.58** | **9.58** | 16/4/20 |
| freeze | 20 | 0.55 | 0.25 | 30.5 | 0.0 | 0.5 | 6/0/14 |
| grow-fruit | 20 | 0.45 | 0.20 | 25.1 | 0.0 | 0.1 | 6/1/13 |
| identify-life-stages-1 | 20 | 0.55 | 0.10 | 47.5 | 0.0 | 2.5 | 9/0/11 |
| identify-life-stages-2 | 20 | 0.50 | 0.20 | 30.0 | 0.0 | 0.0 | 6/0/14 |
| inclined-plane-determine-angle | 20 | 0.55 | 0.20 | 36.0 | 0.0 | 1.0 | 7/0/13 |
| lifespan-longest-lived | 25 | 0.56 | 0.16 | 44.0 | 0.0 | 4.0 | 11/1/13 |
| lifespan-longest-lived-then-shortest | 20 | 0.45 | 0.10 | 40.8 | 0.0 | 5.8 | 8/1/11 |
| **measure-melting-point-unknown** | 20 | **0.55** | **0.25** | **30.05** | **0.0** | **0.05** | 6/0/14 |

### 关键观察

- **find-non-living-thing**：唯一零死亡 task（两种 routing 都无死亡），Δ_full=9.58 全部来自 non-death 性能差异（Δ_nd=Δ_pr=Δ_full=9.58），确认 det routing 在无死亡场景也有优势
- **measure-melting-point-unknown-substance**：高死亡率（int=0.55, det=0.25），但 Δ_pr≈0（0.05），说明性能差距几乎完全由死亡避免解释
- 11 tasks 结果与 10 tasks 预分析高度一致，新增 task 未改变核心结论
- r=0.9698, p=8.12e-07：死亡率差异与性能差异的相关性极强且高度显著

### 输出文件
- `/root/autodl-tmp/simgate-modular-routing/results/plan_012_decomposition`（CSV 文件）

---
