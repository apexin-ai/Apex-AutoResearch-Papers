# code pertest precision recall prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pertest-precision-recall-prep_20260512T131752_result.json`
- **Structured JSON:** [`b38315579db8b2af0c51.json`](../../sessions/b3/b38315579db8b2af0c51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。结果摘要：

**Overall (cls_seed0, 1890 samples)**
- Accuracy: 87.78%
- Fail Precision: 84.02%, Recall: 92.21%, F1: 87.92%
- Pass Precision: 92.01%, Recall: 83.64%, F1: 87.63%

**Diagnostic Quality**
- 114 problems, 48 (42.1%) perfect prediction
- Median problem fail-F1: 94.12%
- Mean problem accuracy: 88.27%

**By Mutation Type** — `return_value` 最易检测 (F1=98.6%)，`off_by_one` 最难 (F1=80.8%)，`original` 的 fail 指标为 0（因为 original 都是 pass label，无 fail 样本）

**Worst Problems** — MBPP/397 (40%), HumanEval/130 (46%) 等辨别能力最差

脚本写在 `/home/sonny/exec-sim-repair-verifier/eval_pertest_diagnostic.py`，输出保存在 `eval_pertest_diag.json`。支持 `--predictions_file` 加载已有预测或 `--checkpoint_dir` 从头推理。

---
