# analysis plan 012 preliminary

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-012-preliminary_20260514T045209_result.json`
- **Structured JSON:** [`322fb328376ededc53ba.json`](../../sessions/32/322fb328376ededc53ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Death Decomposition 初步分析结果 (PRELIMINARY)

### 全局汇总

| 指标 | 本次 (11 tasks, 235 eps) | Prescreening (30 tasks) | 变化 |
|------|------------------------|------------------------|------|
| Δ_full (det-int) | **+29.85** | +37.9 | ↓ 更低 |
| Δ_nd (no-death) | **+2.95** | +0.2 | ↑ 略高但仍极小 |
| Death fraction | **90.1%** | 99% | ↓ 仍然 dominant |
| Pearson r | **0.967** (p=1.2e-06) | 0.989 | ↓ 仍极强相关 |
| Death rate | int=43.0%, det=16.2% | — | — |
| Labels | det=83, int=8, no-pref=144 | — | — |

### Per-task CSV

| task | n | death_int | death_det | Δ_full | Δ_nd | det_pref | int_pref |
|------|---|-----------|-----------|--------|------|----------|----------|
| **chemistry-mix** ⚠️ | 10 | 0.50 | 0.30 | 20.0 | 0.0 | 3 | 1 |
| find-animal | 20 | 0.50 | 0.25 | 26.65 | 0.0 | 5 | 0 |
| find-non-living-thing | 40 | 0.00 | 0.00 | 9.58 | 9.58 | 16 | 4 |
| freeze | 20 | 0.55 | 0.25 | 30.5 | 0.0 | 6 | 0 |
| grow-fruit | 20 | 0.45 | 0.20 | 25.1 | 0.0 | 6 | 1 |
| identify-life-stages-1 | 20 | 0.55 | 0.10 | 47.5 | 0.0 | 9 | 0 |
| identify-life-stages-2 | 20 | 0.50 | 0.20 | 30.0 | 0.0 | 6 | 0 |
| inclined-plane-determine-angle | 20 | 0.55 | 0.20 | 36.0 | 0.0 | 7 | 0 |
| lifespan-longest-lived | 25 | 0.56 | 0.16 | 44.0 | 0.0 | 11 | 1 |
| lifespan-longest-lived-then-shortest | 20 | 0.45 | 0.10 | 40.8 | 0.0 | 8 | 1 |
| measure-melting-point-unknown | 20 | 0.55 | 0.25 | 30.05 | 0.0 | 6 | 0 |

⚠️ chemistry-mix 仅 10 episodes（incomplete，缺 12 eps），最终版需重跑。

### 关键观察

1. **核心结论不变**：90.1% 的 det-int gap 来自 death avoidance，与 prescreening 的 99% 方向一致
2. **Δ_full 偏低**（29.85 vs 37.9）：plan_c 的 11 个 task 子集 death rate 差距比 30-task 全集小
3. **find-non-living-thing 是唯一零死亡 task**：Δ_nd=9.58 = Δ_full，说明该 task 的 gap 完全来自非死亡因素，拉高了全局 Δ_nd
4. **Pearson r=0.967 仍极强**：death rate 差异几乎完美预测 score gap

---
