# analysis three way comparison d035

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_three_way_comparison_d035_20260516T021431_result.json`
- **Structured JSON:** [`62d56d0655a176d8a742.json`](../../sessions/62/62d56d0655a176d8a742.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总结果

### 任务 A：三方比较

| Metric | 16-rel independent | 80-pool → 16-sub | 80-rel full |
|---|---|---|---|
| N batches | 100 | 100 | 25 |
| BCS range | [0.653, 0.900] | [0.458, 0.684] | [0.646, 0.823] |
| Slope | -0.449 | -0.401 | -0.151 |
| Slope 95% CI | [-0.549, -0.345] | [-0.694, -0.057] | [-0.930, 0.657] |
| Pearson r | -0.637 | -0.221 | -0.082 |
| Δ(Q4-Q1) pp | -7.42 | -3.92 | +0.35 |
| Δ CI 95% | [-9.45, -4.49] | [-8.62, -0.16] | [-9.38, 7.55] |

**Permutation tests** (slope difference): 三组两两对比均无显著差异 (p = 0.44, 0.15, 0.33)。斜率方向一致（均为负），但 80-rel full 只有 25 个 random batch，统计功效不足。

### 任务 B：D035 极端批次重算

| Metric | 16-rel (D033) | 80pool-16sub | 80-rel (reference) |
|---|---|---|---|
| Method | bottom/top 5 of 100 | bottom/top 5 of 100 | 1 greedy low vs 1 greedy high |
| **Δ_extreme (pp)** | **-11.65** | **-9.79** | **-31.25** |
| 95% CI | [-14.76, -5.16] | [-17.71, -1.45] | N/A (single batch) |
| Low BCS range | [0.653, 0.712] | [0.458, 0.478] | 0.472 |
| High BCS range | [0.900, 0.900] | [0.629, 0.684] | 0.971 |
| Low group mean acc | 0.9222 | 0.8562 | 0.8229 |
| High group mean acc | 0.8056 | 0.7583 | 0.5104 |

关键发现：
- 16-rel 极端批次 Δ = -11.65pp，比四分位法的 -7.42pp 更大（符合预期，极端值更极端）
- 80-pool-16sub 极端批次 Δ = -9.79pp，也显著（CI 不跨零），四分位法的 -3.92pp CI 曾跨零
- 80-rel 的 -31.25pp 远大于前两者，因其 BCS span 极宽（0.47 → 0.97），且用贪心构造的单批次

产出文件均保存在服务器 `artifacts/three_way_comparison/` 和 `artifacts/d035_extreme_batch/` 下。

---
