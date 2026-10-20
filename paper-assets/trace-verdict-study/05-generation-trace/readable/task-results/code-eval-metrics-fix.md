# code eval metrics fix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-metrics-fix_20260514T171628_result.json`
- **Structured JSON:** [`e1934aa2cac0e9b4dafd.json`](../../sessions/e1/e1934aa2cac0e9b4dafd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法正确，`--help` 正常。

修改摘要：
- **`compute_metrics`** 新增 `majority_baseline`（= test set 中多数类占比）、`majority_class`、`lift`（= accuracy - majority_baseline）
- **`bootstrap_ci`** 自动对 `majority_baseline` 和 `lift` 也计算 95% CI（跳过非数值字段 `majority_class`）
- **输出格式** 按要求显示 accuracy + CI、majority baseline、lift + CI、per-class P/R/F1
- **`eval_results.json`** 中 `metrics` 和 `confidence_intervals` 自动包含所有新字段

---
