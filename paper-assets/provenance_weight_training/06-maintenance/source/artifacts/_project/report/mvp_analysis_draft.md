# MVP Analysis: Adaptive b* vs Grid-Best vs Uniform

**Date**: 2026-05-15
**Status**: Preliminary (seed456 grid-b incomplete)

---

## 1. Complete Data Summary

### 1.1 Uniform Baselines (eval_ppl_holdout)

| Seed | PPL |
|------|------|
| 42 | 17.69 |
| 123 | 17.69 |
| 456 | 17.70 |
| **Mean** | **17.693** |

### 1.2 Grid-b Results (eval_ppl_holdout)

| b | seed42 | seed123 | seed456 | mean (2-seed) |
|-----|--------|---------|---------|---------------|
| 0.5 | 17.651 | 17.638 | ⏳ ANALYZING | 17.6445 |
| 1.0 | 17.692 | 17.674 | 17.68 | 17.683 |
| 1.5 | 17.718 | 17.701 | 17.71 | 17.7095 |
| 2.0 | 17.741 | 17.725 | ⏳ RUNNING | 17.733 |
| 3.0 | 17.774 | 17.760 | ⏳ RUNNING | 17.767 |
| 5.0 | 17.818 | 17.804 | ⏳ RUNNING | 17.811 |

**Grid-best: b=0.5 in both complete seeds. PPL 单调递增 w.r.t. b.**

### 1.3 Adaptive_fix Results (eval_ppl_holdout)

| Seed | PPL |
|------|-------|
| 42 | 17.65 |
| 123 | 17.643 |
| 456 | 17.66 |
| **Mean** | **17.651** |

---

## 2. MVP Ratio Calculation

### 2.1 Formula

```
improvement_X = mean(uniform_ppl) - mean(X_ppl)
ratio = improvement_adaptive / improvement_grid_best
MVP PASS if ratio ≥ 0.90
```

### 2.2 Two-Seed Result (seed42 + seed123, complete data)

| Metric | Value |
|--------|-------|
| mean(uniform) | 17.690 |
| mean(grid_best, b=0.5) | 17.6445 |
| mean(adaptive_fix) | 17.6465 |
| improvement_grid_best | 0.0455 |
| improvement_adaptive | 0.0435 |
| **ratio** | **0.956** |
| **MVP** | **PASS ✓ (≥ 0.90)** |

### 2.3 Per-Seed Breakdown

| Seed | uniform | grid_best | adaptive_fix | gap (adap−grid) | ratio |
|------|---------|-----------|-------------|-----------------|-------|
| 42 | 17.69 | 17.651 | 17.65 | −0.001 | 1.026 |
| 123 | 17.69 | 17.638 | 17.643 | +0.005 | 0.904 |
| 456 | 17.70 | ⏳ | 17.66 | — | — |

- seed42: adaptive 比 grid-best 还好 0.001
- seed123: adaptive 比 grid-best 差 0.005，ratio=0.904 刚过 0.90 线

### 2.4 Three-Seed Projection

Seed456 grid_b0.5 尚未出 eval_ppl。基于已有 seed456 数据估算：

seed456 已知: b=1.0 → 17.68, b=1.5 → 17.71
其他 seed 的 b=1.0 - b=0.5 gap: seed42=0.041, seed123=0.036, 均值=0.039

**估算 seed456 b=0.5 ≈ 17.68 − 0.039 = 17.641**

| Scenario | seed456 b=0.5 | mean(grid_best) | mean(adaptive) | ratio | MVP |
|----------|---------------|-----------------|----------------|-------|-----|
| 乐观 | 17.66 | 17.650 | 17.651 | 0.977 | PASS |
| 中值估算 | 17.641 | 17.643 | 17.651 | 0.840 | **FAIL** |
| 悲观 | 17.63 | 17.640 | 17.651 | 0.792 | **FAIL** |

**⚠️ 关键风险：如果 seed456 b=0.5 延续 seed42/123 的趋势（显著优于 b=1.0），3-seed ratio 可能降到 0.90 以下。**

原因：adaptive_fix seed456 (17.66) 相对偏弱，而 grid-best seed456 可能很强。

---

## 3. b* Distribution Analysis (Adaptive_fix)

### 3.1 Per-Seed b* Statistics

| Statistic | seed42 | seed123 | seed456 | 3-seed avg |
|-----------|--------|---------|---------|------------|
| count | 26458 | 25906 | 26396 | — |
| mean | 1.399 | 1.431 | 1.416 | 1.415 |
| median | 0.871 | 0.880 | 0.880 | 0.877 |
| std | 1.933 | 2.029 | 1.993 | 1.985 |
| min | 0 | 0 | 0 | — |
| max | 20 | 20 | 20 | — |
| p25 | 0.54 | 0.54 | 0.54 | 0.54 |
| p75 | 1.512 | 1.52 | 1.52 | 1.517 |

### 3.2 b* Distribution Buckets (三 seed 一致)

| Range | Percentage |
|-------|-----------|
| b* < 0.5 | 20.9% |
| 0.5 ≤ b* < 1.0 | 35.7% |
| 1.0 ≤ b* < 2.0 | 27.3% |
| b* ≥ 2.0 | 16.1% |

### 3.3 Grid-best b=0.5 vs Adaptive b* 均值 ≈1.4 的差异分析

**表面矛盾**：grid search 选出 b=0.5，但 adaptive 选的 b* 均值 ≈1.4。

**实际不矛盾的原因**：

1. **Median vs Mean**：b* 中位数 ≈0.88，远低于均值 1.4。56.6% 的 batch 的 b* < 1.0。均值被右尾（max=20）拉高。

2. **Per-sample vs Global**：adaptive 为每个 batch 选不同的 b*，本质上是异质化的 weighting。高 b* batch 可能对应高噪声 batch（需要更激进的 downweight），低 b* batch 对应低噪声 batch。全局固定 b 是 compromise。

3. **PPL 对 b 的敏感度低**：从 grid 数据看，b=0.5 到 b=1.0 仅差 0.02-0.04 PPL。即使 adaptive 的"等效全局 b"不是 0.5，差异很小。

---

## 4. b=0.5 Grid 边界问题

### 4.1 事实

- 两个完整 seed 都显示 b=0.5 是 grid 中最优
- PPL 随 b 单调递增（0.5 → 5.0）
- b=0.5 位于 grid 搜索下界

### 4.2 风险评估

**是否需要扩展到 b < 0.5？**

如果 b=0.5 不是全局最优而只是网格中最优：
- 真实 grid-best 在 b < 0.5 处更低 → MVP ratio 分母增大 → ratio 进一步恶化
- 极端情况 b→0 等价于 uniform → grid-best PPL 不可能无限下降

**建议**：补跑 b=0.25 和 b=0.1 各一个 seed 做诊断。如果 PPL 继续下降，说明 grid 未覆盖最优点，需要修正 baseline。如果 PPL 回升，确认 b=0.5 附近是最优。

### 4.3 理论解释

b→0 时 weight = q^0 = 1（所有样本等权），退化为 uniform。b=0 本身就是 uniform baseline。

因此存在一个最优 b*_global ∈ (0, ∞)。当前 grid 显示 b=0.5 最优，可能：
- 真实最优在 b ∈ (0, 0.5)（尚未探测）
- 真实最优在 b ≈ 0.5（恰好被捕捉到）

无论哪种，adaptive 的优势在于免去了这个搜索过程。

---

## 5. Seed456 待补数据

### Grid-b seed456 status

| b | Status | eval_ppl_holdout |
|-----|-----------|-----------------|
| 0.5 | ANALYZING | ⏳ 需补跑 eval |
| 1.0 | DONE | 17.68 |
| 1.5 | DONE | 17.71 |
| 2.0 | RUNNING | ⏳ |
| 3.0 | RUNNING | ⏳ |
| 5.0 | RUNNING | ⏳ |

**关键阻塞**：b=0.5 的 eval 是决定 3-seed MVP ratio 的瓶颈。应优先补跑。

---

## 6. Key Findings

1. **2-seed ratio = 0.956 → PASS**（≥ 0.90 阈值）
2. **Per-seed 表现分化**：seed42 adaptive 优于 grid-best (ratio=1.03)，seed123 刚过线 (ratio=0.90)
3. **3-seed ratio 有下行风险**：seed456 adaptive 相对偏弱 (17.66 vs uniform 17.70，improvement 仅 0.04)，若 grid-best 强则 ratio 可能 < 0.90
4. **b=0.5 在 grid 边界**：PPL 单调递增意味着可能有更优 b < 0.5，会使 ratio 更难达标
5. **b* 分布稳定**：三 seed 的 b* 分布高度一致（mean≈1.4, median≈0.88），说明 adaptive 行为可复现
6. **Adaptive 的实际操作点接近 grid-best**：虽然 b* mean=1.4，但 median=0.88，且 56.6% 的 batch b* < 1.0

## 7. 风险与下一步

| 风险 | 严重度 | 缓解措施 |
|------|--------|----------|
| 3-seed ratio < 0.90 | 🔴 高 | 等 seed456 b=0.5 eval 出来；同时准备 fallback 叙事 |
| Grid 边界 b=0.5 | 🟡 中 | 补跑 b=0.25, b=0.1 诊断 |
| PPL 差异量级太小 (~0.04) | 🟡 中 | 考虑增加 eval token 量或换更灵敏指标 |

**最高优先级**：完成 grid_b0_5_seed456 的 eval，获得确定性的 3-seed ratio。
