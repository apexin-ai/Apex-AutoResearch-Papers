# analysis ess upper bound

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ess-upper-bound_20260516T160218_result.json`
- **Structured JSON:** [`479ac1a7c32b4c7d90c5.json`](../../sessions/47/479ac1a7c32b4c7d90c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

## 结果汇总

### α_eff binding batch (N=1,976 / 5,000 样本，占比 ~40%)

| 指标 | Dual b* (实际) | ESS-only b* (上界) |
|------|---------------|-------------------|
| Mean | 1.19 | 5.88 |
| Median | 0.80 | 3.59 |
| p25 | 0.46 | 1.97 |
| p75 | 1.37 | 7.44 |

### 比值（ESS-only / Dual）

| 统计量 | 值 |
|--------|-----|
| Ratio of means | **4.94×** |
| Per-batch median | **3.61×** |
| Per-batch p25 | 1.70× |
| Per-batch p75 | 9.71× |

### Cross-check（step_metrics.jsonl 实际训练）

- Training records (b>0): 25,991
- α_eff binding rate: **40.1%**（alpha_eff ≈ 0.8）
- ESS binding rate: 65.3%（ESS ≈ 2.0）
- b* when α_eff binding: mean=1.15, median=0.80

### 论文 Claim 1 更新

| | 旧值 | 修正后 |
|--|------|--------|
| Dual b* | 1.67 | **1.19** |
| ESS-only b* | 4.15 | **5.88** |
| Ratio | 2.5× | **4.94×** (means) / **3.61×** (medians) |

修正后比值更大，"最小干预"论据更强。建议论文用 median ratio 3.61× 或 ratio of means 4.94×（后者对 outlier 敏感，前者更稳健）。

---
