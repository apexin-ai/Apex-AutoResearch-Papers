# research metrics table prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_metrics-table-prep_20260516T025449_result.json`
- **Structured JSON:** [`3c93653fb5b09edef6c0.json`](../../sessions/3c/3c93653fb5b09edef6c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已生成并注册：

**59 个已完成实验，9 个分组：**

| 组 | 数量 | 最佳 PPL |
|---|---|---|
| baseline | 4 | 17.686 (uniform_seed123) |
| adaptive (n_min=2) | 3 | 17.643 (adaptive_fix_seed123) |
| adaptive (n_min=3) | 3 | 17.631 (adaptive_seed123) |
| ESS-only | 3 | 17.719 (ess_only_seed456) |
| grid-sweep | 17 | 17.638 (grid_b0_5_seed123) |
| tau-sweep | 11 | 17.679 (tau_07_seed42) |
| contamination_60 | 4 | 17.704 (grid_b0_5) |
| batch_size | 3 | 17.730 (bs8_nmin2_seed42_r2, ⚠️ negative) |
| other | 11 | 17.654 (golden_ratio_seed42) |

已修正 `contamination_60_uniform_seed42` 从 baseline 移至 contamination_60 组。没有匹配 `detect_remove_*` 的已完成实验。

- `art_20260516_dfc240` → `metrics_summary.csv`
- `art_20260516_54e96f` → `metrics_summary.md`

---
