# diagnose epoch matched dr failures

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_epoch_matched_dr_failures_20260518T145546_result.json`
- **Structured JSON:** [`8bf90db72d68b914bcab.json`](../../sessions/8b/8bf90db72d68b914bcab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已清理 stale exit files。

## 诊断结果

**根因**: agent-ml-research wrapper 中 `source /root/miniconda3/bin/activate` 在嵌套 `bash -c` 中未能正确激活 conda，导致 `python: command not found` (EXIT_CODE=127)。同类日志 `detect_remove_q03_seed42.log` 逐字记录了:
```
bash: line 1: python: command not found
EXIT_CODE=127
```

**当前状态**: 三个实验已被手动重启（使用 `/root/miniconda3/bin/python` 绝对路径），**正在正常训练中**:

| 实验 | 进度 | 预计剩余 |
|------|------|---------|
| epoch_matched_dr_seed456 | 293/2532 (12%) | ~1h18m |
| epoch_matched_dr_seed123 | 293/2532 (12%) | ~1h18m |
| detect_remove_q01_seed42 | 292/6103 (5%) | ~3h23m |

**无需重跑**。尚无模型 checkpoint 和 eval metrics（训练未完成）。已清理 stale `.exit` 文件。后续提交任务应在 wrapper 中使用 `/root/miniconda3/bin/python` 绝对路径。

详细报告: `artifacts/diagnosis_exit127_20260518.md`

---
