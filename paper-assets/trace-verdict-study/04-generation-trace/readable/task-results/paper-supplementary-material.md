# paper supplementary material

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_supplementary_material_20260521T164101_result.json`
- **Structured JSON:** [`31e3e1562c18f357e5c6.json`](../../sessions/31/31e3e1562c18f357e5c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

内容已成功追加到 `appendix.tex`。新增内容：

**Section: Confusion Matrix and Error Bias Analysis** (`\label{sec:confusion_bias}`)
- **Table `tab:confusion_summary`**: 8 conditions × TP/FP/TN/FN/Accuracy，Tier 1/Tier 2 分组
- **Table `tab:fp_fn_bias`**: 8 conditions × FP Rate/FN Rate/Dominant FP Type
- **Prose**: 3 句话总结 Tier 1 (conservative FN-only) vs Tier 2 (bidirectional, AssertionError-dominated FP) 的失败模式差异，加 overlap 统计（7/430 overlap, zero universal failures），交叉引用已有的 Error Overlap 节

**关于 Calibration (plan_019)**：现有 appendix 已有两处 calibration 表格（`tab:calibration_cross` 4 models × ECE/Brier/MCE + `tab:calibration_model_level` 4 models × Accuracy/ECE/Brier/Mean Conf），plan_019 数据已完整覆盖，无需重复添加。

---
