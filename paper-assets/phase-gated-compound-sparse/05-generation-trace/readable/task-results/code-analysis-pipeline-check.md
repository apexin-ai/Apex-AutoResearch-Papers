# code analysis pipeline check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis-pipeline-check_20260514T225203_result.json`
- **Structured JSON:** [`43dff8d046aab9f32fd9.json`](../../sessions/43/43dff8d046aab9f32fd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All information collected. Here's the report:

---

## n=500 分析 Pipeline 就绪报告

### ✅ 已就绪
- **脚本存在**：`analyze_n500_unified.py` 存在（26KB, 2026-05-15 更新）
- **B=10,000 Bootstrap**：`B_BOOT = 10000`，正确
- **Median pipeline**：使用 `bootstrap_median_ci` + `np.median`，无 mean 计算（符合 D054）
- **d_z 实现**：within-importance d_z 用 `paired_cohens_dz`（含 bootstrap CI）；imp-vs-rand 仅 Wilcoxon + median_diff，无 d_z（符合 D059）
- **输出格式**：JSON 含 median, median_ci_low/high, d_z, d_z_ci, wilcoxon_p, bonferroni_p, n_valid 等字段
- **依赖**：numpy 2.2.6, scipy 1.17.1, json — 全部可用

### ❌ 需修复
无。Pipeline 代码完全就绪。

### 数据目录状态（16 conditions 总计）

| 状态 | DeepSeek | Qwen |
|------|----------|------|
| ✅ 已完成（有 results.json） | imp_s015, rand_s015, rand_s020 | imp_s015, imp_s020, rand_s015, rand_s020 |
| 🔄 目录存在但无结果（进行中） | imp_s020, rand_s025 | imp_s025, rand_s025 |
| ⏳ 目录尚未创建（待开始） | imp_s025, imp_s030, rand_s030 | imp_s030, rand_s030 |

**已完成 7/16 conditions，进行中 4 个，待开始 5 个。** Pipeline 零阻塞，实验完成即可运行。

---
