# Deep-Internal vs Fast-Internal 对比分析

**日期**: 2026-05-15
**数据来源**: `results/plan_c/`（fast-internal）, `results/plan-006-deep-internal/`（deep-internal）

## 数据概况

6 个重叠 task，fast-internal 取自 plan_c 的 `internal_final`，deep-internal 取自 plan-006-deep-internal 的 `deep_internal_final`。
- identify-life-stages-1：仅取前 14 episodes（避免伪重复）
- Death 判定：score ≤ -100

## Per-Task 对比表

| Task | n_fast | n_deep | death%_fast | death%_deep | mean_fast | mean_deep | p (MW) | Cohen's d |
|------|--------|--------|-------------|-------------|-----------|-----------|--------|-----------|
| chemistry-mix | 20 | 20 | 45.0% | 55.0% | -43.5 | -53.5 | 0.599 | -0.19 |
| find-non-living-thing | 40 | 20 | 0.0% | 0.0% | 18.9 | 26.6 | 0.268 | +0.31 |
| identify-life-stages-1 | 14 | 14 | 50.0% | 50.0% | -50.0 | -50.0 | 1.000 | 0.00 |
| inclined-plane-determine-angle | 20 | 20 | 55.0% | 50.0% | -55.0 | -50.0 | 0.767 | +0.10 |
| lifespan-longest-lived | 25 | 20 | 56.0% | 55.0% | -54.0 | -55.0 | 0.969 | -0.02 |
| lifespan-longest-lived-then-shortest-lived | 20 | 20 | 45.0% | 45.0% | -45.0 | -43.4 | 0.877 | +0.03 |

## Aggregate 统计

| 指标 | Fast-internal | Deep-internal |
|------|--------------|---------------|
| 跨 task 平均分 | -38.11 | -37.55 |
| 平均 death rate | 41.8% | 42.5% |

- **Paired t-test**（task-level means）: t = -0.224, **p = 0.832**
- **Wilcoxon signed-rank**: W = 6.0, **p = 0.813**

## Direction of Difference

| Task | Δ (deep - fast) | Direction | Significant? |
|------|-----------------|-----------|-------------|
| chemistry-mix | -10.0 | fast > deep | No |
| find-non-living-thing | +7.7 | deep > fast | No |
| identify-life-stages-1 | 0.0 | tie | — |
| inclined-plane-determine-angle | +5.0 | deep > fast | No |
| lifespan-longest-lived | -1.0 | fast > deep | No |
| lifespan-longest-lived-then-shortest-lived | +1.6 | deep > fast | No |

**Deep wins 3, Fast wins 2, Ties 1 — 无一达到 p < 0.05。**

## Special Analysis: find-non-living-thing

两种 mode 均 0% death rate（这是唯一没有死亡的 task）。Deep-internal 均值略高（26.6 vs 18.9），但 p = 0.268，不显著。注意 fast-internal 样本量更大（40 vs 20），分布形态相似：大量 0 分 + 部分 50/58 分。

## Score 分布特征

大多数 task 呈现**双峰分布**：
- **死亡峰**：score = -100（除 find-non-living-thing 外所有 task 都有 45-56% 的死亡率）
- **存活峰**：score = 0（存活但未完成）或少量正分

两种 mode 在每个 task 上的分布形态高度一致，无结构性差异。

## 结论

### Deep-internal 是否提供额外 routing signal？

**否。** 证据：

1. **6 个 task 无一显著差异**（最小 p = 0.268），效应量均为 negligible 到 small（|d| ≤ 0.31）
2. **Aggregate 完全等价**：均分差 0.56，paired tests p > 0.8
3. **Death rate 几乎相同**：41.8% vs 42.5%，无 survival advantage
4. **分布形态无结构差异**：同一 task 的 score 分布在两种 mode 下高度相似
5. **唯一的"趋势"**（find-non-living-thing +7.7 分）远未达到统计显著，且该 task 本身就是最容易的（0% death rate），routing 价值有限

### 3-way routing 是否有数据支撑？

**不支撑。** 3-way routing（deterministic vs fast-internal vs deep-internal）要求 deep-internal 和 fast-internal 在至少部分 task 上表现出系统性差异，使得 router 有理由区分选择。当前数据显示两者在所有 task 上统计等价——router 无法基于 episode 特征有效区分应该调用 deep 还是 fast。

### 建议

**维持 2-way routing（deterministic vs internal）**，将 fast-internal 作为 internal mode 的代表。理由：
- deep-internal 成本更高（thinking token 消耗）但未带来可测量的性能提升
- 样本量（每 task 14-40 episodes）足以检测中等以上效应（power analysis: n=20 可检测 d≥0.9 at α=0.05, 80% power），当前效应量远小于此
- 如需扩展 routing 维度，应优先考虑其他信号（如 task complexity features），而非 internal mode 细分
