# diagnose repo level failed

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_repo-level-failed_20260512T112514_result.json`
- **Structured JSON:** [`a2d098a92094ddc08d75.json`](../../sessions/a2/a2d098a92094ddc08d75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/repo_level_failure_diagnosis.md`。

**结论**：两个实验同一个 bug —— HF Trainer 默认 `remove_unused_columns=True`，把 `sample_weight` 列在进入 DataLoader 前就删了，导致 `compute_loss` 里 `inputs.pop("sample_weight")` 抛 `KeyError`。

**修复**：在两个文件的 `TrainingArguments` 中加 `"remove_unused_columns": False`，一行改动即可。

---
