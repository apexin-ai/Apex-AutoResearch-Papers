# code d028 pipeline integration fdr

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d028_pipeline_integration_fdr_20260515T105558_result.json`
- **Structured JSON:** [`7e6f97d59b32fe701260.json`](../../sessions/7e/7e6f97d59b32fe701260.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项任务完成。总结：

**Task 1 (P0): consensus_framework.py FPR ground truth 切换**
- `main()` 现在先调 `compute_fpr_null_control`（α=0.0 null control）作为 primary FPR → `fpr_fnr_table.json`
- `compute_fpr_fnr_diff`（differenced_xcorr）保留为 legacy → `fpr_fnr_table_legacy.json`
- 顶部注释已更新，`DIFF_INDEX` 保留（legacy 路径仍用）
- 验证通过：null control 下 permG FPR=0%, TY FPR=0%；legacy 下 consensus FPR=0%, FNR=0%
- 3 个文件已同步到本地 `artifacts/analysis/consensus_framework/`

**Task 2 (P1): Phase 2 报告 FDR 化**
- 主表替换为 BH FDR-corrected 数字，raw 值移至引用块对比
- 关键翻转：α=0.25 permG 25%→**0%**, α=0.50 permG 25%→**0%**, α=0.25 TY 62.5%→**37.5%**
- Registry metrics 已更新：所有 sig rate 字段加 `_raw`/`_fdr` 后缀，新增 `fdr_correction: "BH q=0.05"`

---
