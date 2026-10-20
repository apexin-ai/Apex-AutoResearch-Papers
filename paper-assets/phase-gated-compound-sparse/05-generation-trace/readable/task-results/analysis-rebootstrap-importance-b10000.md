# analysis rebootstrap importance b10000

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rebootstrap_importance_b10000_20260514T090502_result.json`
- **Structured JSON:** [`69040f482d2daeb6b446.json`](../../sessions/69/69040f482d2daeb6b446.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### Part A: 检查结果
- 8 个 importance 实验目录全部存在（`profiling_output_bf16_ds_imp_s015~s030` + `bf16_qw_imp_s015~s030`）
- 每个 `profiling_results.json` 都有 per-problem raw data（`ii_high`, `ii_low`）
- 原始 `n_bootstrap = 1000`

### Part B: Re-bootstrap B=10000 结果

| 实验 | median_diff | perm_p | Cohen's d | 95% CI | wilcox_p |
|---|---|---|---|---|---|
| ds_imp_s015 | 0.3236 | 0.0000 | 0.607 | [0.199, 0.472] | 0.000 |
| ds_imp_s020 | 1.1520 | 0.0000 | 0.725 | [0.655, 1.256] | 0.000 |
| ds_imp_s025 | 3.9686 | 0.0000 | 0.953 | [2.829, 5.292] | 0.000 |
| ds_imp_s030 | 9.9436 | 0.0000 | 1.126 | [8.392, 16.653] | 0.000 |
| qw_imp_s015 | 0.0476 | 0.0001 | 0.371 | [-0.005, 0.110] | 0.030 |
| qw_imp_s020 | 0.2075 | 0.0000 | 0.722 | [0.067, 0.402] | 0.000 |
| qw_imp_s025 | 1.1087 | 0.0000 | 1.233 | [0.609, 1.469] | 0.000 |
| qw_imp_s030 | 2.6194 | 0.0000 | 1.439 | [1.722, 3.651] | 0.000 |

注意：这些 median_diff 是 **per-problem 配对** 统计量（`np.median(ii_low) - np.median(ii_high)`，仅含 high/low 均非 None 的 problem），与原 registry 中基于 segment-level aggregate 的值略有差异。

`qw_imp_s015` 的 bootstrap CI 边缘包含 0（[-0.005, 0.110]），但 permutation p=0.0001 仍显著。

### Part C: cross_model_analysis.json
- `random_median_diffs.qwen.s030`: 4.24103 → 2.418272 ✓

Registry 已更新，artifact 已注册。脚本存放在 `analysis/rebootstrap_importance_b10000.py`。

---
