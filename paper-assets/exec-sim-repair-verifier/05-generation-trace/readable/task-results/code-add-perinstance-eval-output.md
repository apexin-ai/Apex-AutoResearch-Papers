# code add perinstance eval output

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add-perinstance-eval-output_20260512T160625_result.json`
- **Structured JSON:** [`07ff98af9eea1c6bf818.json`](../../sessions/07/07ff98af9eea1c6bf818.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 代码修改
两个脚本各添加了 `--save_predictions` 参数，在 eval 循环中收集 per-instance 数据，条件性输出 `_predictions.json` 文件。

### CLS seed42 predictions
- 文件：`eval_cls_seed42_with_preds_predictions.json`（1890 条）
- 正确率：1660/1890 (87.8%)
- mutation_type 分布：off_by_one=671, return_value=402, original=398, operator_swap=298, variable_swap=85, boundary_removal=36
- 字段：idx, problem_id, mutation_type, source, true_label, predicted_label, correct, raw_output

### CWM seed42 predictions
- 文件：`eval_cwm_seed42_with_preds_predictions.json`（1890 条）
- 正确率：1654/1890 (87.5%)
- 额外字段：error_type, exact_match
- exact match rate: 84.0%

### Aggregate metrics 一致性
CLS aggregate metrics 与原 `eval_seed42.json` **完全一致**，向后兼容验证通过。

### 文件路径
```
/home/sonny/exec-sim-repair-verifier/eval_cls_seed42_with_preds.json          # aggregate
/home/sonny/exec-sim-repair-verifier/eval_cls_seed42_with_preds_predictions.json  # per-instance
/home/sonny/exec-sim-repair-verifier/eval_cwm_seed42_with_preds.json          # aggregate
/home/sonny/exec-sim-repair-verifier/eval_cwm_seed42_with_preds_predictions.json  # per-instance
```

---
