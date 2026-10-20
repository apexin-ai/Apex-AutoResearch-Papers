# code bootstrap gradient fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap-gradient-fix_20260514T070351_result.json`
- **Structured JSON:** [`69fc4c4e3133706b7d33.json`](../../sessions/69/69fc4c4e3133706b7d33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，无报错。

## 修改总结

**文件**: `/root/autodl-tmp/pacs/analysis/mid_sparsity_gap_analysis.py`

**4 处修改：**

| 行号 | 修改 |
|------|------|
| 40-42 | `bootstrap_gradient_ci`: 将 `n = min(len(lo), len(hi)); lo, hi = lo[:n], hi[:n]` 改为长度不等时抛 `ValueError`，等长时直接用 `n = len(lo)` |
| 98-103 | `analyze_experiment`: 新增 `paired_lh` 构造——遍历 `per_problem`，只保留 `ii_low` 和 `ii_high` 同时非 None 的 problem，解包为 `paired_l` 和 `paired_h` |
| 125 | full_set 的 `gradient_ci` 调用从 `bootstrap_gradient_ci(ii_l, ii_h)` 改为 `bootstrap_gradient_ci(paired_l, paired_h)` |
| 167 | 报告文本更新为 "uses problem_id-aligned paired arrays" |

**对齐后有效 problem 数量：** full_set gradient 使用 n=49（50 个 problem 中 1 个缺 ii_high），complete_subset 使用 n=40（同时有 high/mid/low 三个 phase 的 problem）。修复前 full_set 会截断到 min(49, 50)=49，恰好本数据集 ii_high 缺失的 problem 和 ii_low 缺失的 problem 没有错位（ii_low 全部非 None），所以数值上变化不大。但修复后逻辑正确：保证每对 `(lo[i], hi[i])` 来自同一个 problem。

---
