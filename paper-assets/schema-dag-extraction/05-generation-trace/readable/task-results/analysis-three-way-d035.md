# analysis three way d035

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_three_way_d035_20260516T021400_result.json`
- **Structured JSON:** [`6784705b1319ed1543f6.json`](../../sessions/67/6784705b1319ed1543f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都完成了。汇总如下：

---

## 任务 1：三方比较结果

| Metric | Independent 16-rel | 80-pool → 16-sub | Full 80-rel |
|--------|-------------------|------------------|-------------|
| N batches | 100 | 100 | 25 |
| BCS mean±std | 0.826±0.067 | 0.557±0.044 | 0.720±0.046 |
| Slope | -0.449 | -0.401 | -0.151 |
| Slope 95% CI | [-0.549, -0.345] | [-0.694, -0.057] | [-0.930, 0.657] |
| Pearson r | -0.637 (p<1e-12) | -0.221 (p=0.027) | -0.082 (p=0.698) |
| Δ(Q4-Q1) pp | -7.42 | -3.92 | +0.35 |
| Δ CI 95% | [-9.45, -4.49] | [-8.62, -0.16] | [-9.38, 7.55] |

**Permutation tests (slope difference)**：三对比较均不显著（p=0.44, 0.15, 0.33），slope 差异未达统计显著。

---

## 任务 2：D035 极端批次分析

Δ = acc(low BCS) - acc(high BCS)，正值表示低 BCS 准确率更高（BCS 越高 → 越难 → 准确率越低）。

### 16-rel Independent (100 batches)

| n_extreme | Δ (pp) | 95% CI | Low BCS mean | High BCS mean |
|-----------|--------|--------|-------------|--------------|
| 1 | +14.11 | [14.11, 14.11] | 0.6532 | 0.9002 |
| 3 | +13.51 | [7.72, 18.35] | 0.6741 | 0.9002 |
| **5** | **+11.45** | **[7.66, 15.48]** | 0.6879 | 0.9002 |
| 10 | +9.38 | [6.57, 12.12] | 0.7026 | 0.9002 |

### 80-pool → 16-sub (100 batches)

| n_extreme | Δ (pp) | 95% CI | Low BCS mean | High BCS mean |
|-----------|--------|--------|-------------|--------------|
| 1 | +20.83 | [20.83, 20.83] | 0.4578 | 0.6836 |
| 3 | +11.81 | [2.43, 21.18] | 0.4639 | 0.6695 |
| **5** | **+9.79** | **[1.87, 17.50]** | 0.4690 | 0.6552 |
| 10 | +7.40 | [1.46, 12.81] | 0.4816 | 0.6401 |

### 与 80-rel Table 3 对比

80-rel controlled comparison (from bootstrap_ci.json): Δ=**31.25pp** CI [22.92, 39.58]，BCS 范围 0.5705 vs 0.9706。

极端批次方法下的 BCS-accuracy 效应在所有设置中均显著（CI 不含 0），且：
- 16-rel 的 BCS 差距小（0.69 vs 0.90）但仍有 11.45pp 效应
- 80-pool-16sub 的 BCS 差距更小（0.47 vs 0.66）仍有 9.79pp 效应
- 80-rel controlled 的 BCS 差距最大（0.57 vs 0.97），效应最强 31.25pp

结果保存在服务器 `artifacts/extreme_batch_analysis.json` 和 `artifacts/three_way_comparison/results.json`。

---
