# code per test precision recall

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_per-test-precision-recall_20260512T054931_result.json`
- **Structured JSON:** [`4079a3111c3f8279d8af.json`](../../sessions/40/4079a3111c3f8279d8af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载成功，推理已开始。

**已完成：**
- `eval_precision_recall.py` 已写入 `/home/sonny/exec-sim-repair-verifier/`（326行）
- 任务已通过 `submit_training_job` 提交，tmux session: `per-test-precision-recall`
- 模型 (Qwen3-4B + LoRA) 已加载，正在对 1890 个 test 样本推理
- 输出将保存到 `eval_precision_recall_results.json`，包含：总体 confusion matrix + P/R/F1、按 mutation_type 分组、按 problem test count 分桶、FP/FN 错误样本分析

---
