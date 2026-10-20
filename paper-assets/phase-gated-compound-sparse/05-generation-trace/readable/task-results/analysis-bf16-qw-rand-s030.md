# analysis bf16 qw rand s030

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_qw_rand_s030_20260514T084856_result.json`
- **Structured JSON:** [`a737c33fa0fcac6a5c40.json`](../../sessions/a7/a737c33fa0fcac6a5c40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

---

## bf16_qw_rand_s030 分析报告

### 结果

| 指标 | 值 |
|------|-----|
| **Verdict** | **PASS** |
| Median II (high) | 4.2006 |
| Median II (mid) | 6.4770 |
| Median II (low) | 8.0657 |
| Median diff (low−high) | **2.4183** |
| Permutation p-value | **0.012** |
| Wilcoxon p-value | 0.0157 |
| Cohen's d | −0.035 \[−0.225, 0.490\] (negligible) |
| Bootstrap 95% CI (median diff) | \[0.242, 3.315\] — **不含零** |
| 单调递增 high < mid < low | **是** |

### PASS 判定理由
- Permutation p=0.012 < 0.05
- 单调递增梯度 4.20 → 6.48 → 8.07 确认

### 与 s015/s020/s025 的趋势对比

| 实验 | median_diff | perm_p | Cohen's d | verdict |
|------|------------|--------|-----------|---------|
| s015 | −0.029 | 0.766 | −0.051 | FAIL |
| s020 | 0.058 | 0.352 | 0.247 | FAIL |
| s025 | 1.144 | 0.168 | 0.157 | FAIL |
| **s030** | **2.418** | **0.012** | −0.035 | **PASS** |

清晰的剂量-响应关系：随着 sparsity 增加，median_diff 单调上升（−0.03 → 0.06 → 1.14 → 2.42），p-value 单调下降，在 s=0.30 跨过显著性阈值。

### 注意事项
- Cohen's d 为负（−0.035）是因为 mean_diff=−1.13 被少数大负值 outlier 拉低，而 median_diff=2.42 反映了主体分布的真实趋势。Wilcoxon 和 permutation test 一致支持 PASS。
- **叙述影响**：Random masking 不是"无梯度"的完美对照，而是"仅在极端 sparsity (s≥0.30) 才出现梯度"。这意味着 importance-based masking 的优势在于它在更低 sparsity 就能产生显著梯度。

---
