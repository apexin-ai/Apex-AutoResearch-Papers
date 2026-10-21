# analysis compile results table

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile-results-table_20260516T060455_result.json`
- **Structured JSON:** [`4de9ee139f3608fcc84f.json`](../../sessions/4d/4de9ee139f3608fcc84f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个产出已生成并注册：

**63 个 DONE 实验**，其中 41 个 success、3 个 negative、5 个 failed、14 个 killed。

产出文件：
- `experiment_results_summary.csv` — 63 行结构化数据（`art_20260516_45bd10`）
- `experiment_results_summary.md` — 按 claim 分组的 markdown 报告（`art_20260516_f0194b`）

关键发现：
- `eval_loss_clean` 和 `eval_loss_contaminated` 在 registry 中不存在，全部标记为 N/A
- `gpu_hours` 部分实验缺失
- 3 个 negative 实验：`bs8_nmin2_seed42_r2`（bs=8 性能下降）、`tau_095_seed42` 和 `tau_09_seed42`（τ>0.8 导致 PPL 退化）

---
