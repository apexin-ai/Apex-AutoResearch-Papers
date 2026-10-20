# code permutation test fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_permutation-test-fix_20260514T055613_result.json`
- **Structured JSON:** [`04fa199560ef90993057.json`](../../sessions/04/04fa199560ef90993057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### 修改的文件
`/root/autodl-tmp/pacs/pacs/analysis/permutation_test.py`

### 变更内容
1. **Test statistic**: `np.mean(diffs)` → `np.median(diffs)` 作为主统计量，mean 保留为辅助
2. **EPS**: `1e-6` → `1e-10`
3. **输出结构**: 主字段用 median（`observed_median_diff`, `p_value`），辅助字段加 `_mean` 后缀（`observed_mean_diff`, `p_value_mean`）
4. **新增**: 95% CI（bootstrap on median of diffs, 2000 iterations）
5. **Bonferroni 校正**: 同时输出 median 和 mean 版本

### Dry-run 结果（v6_importance_s020 vs v6_random_s020）

| Sparsity | n_paired | gradient_ratio | perm_p (median) | perm_p (mean) | wilcoxon_p |
|----------|----------|---------------|-----------------|---------------|------------|
| s015 | 22 | 30.9x | **0.0041** | 0.0007 | 9.87e-05 |
| s020 | 18 | 27.4x | **0.0016** | 0.0002 | 1.91e-04 |
| s025 | 12 | 51.5x | 0.0740 (n.s.) | 1.0000 | 0.0342 |

s025 的 mean p-value = 1.0 印证了 reviewer 的担忧：heavy-tail 下 mean 统计量不可靠，被极端值主导导致 null distribution 方差极大。切换到 median 后 p=0.074，虽然未达 0.05 但比 mean 版本信息量大得多。s015/s020 的 median-based p-value 均显著（Bonferroni 校正后仍 < 0.05）。

---
