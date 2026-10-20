# code eval pipeline check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_pipeline_check_20260513T235536_result.json`
- **Structured JSON:** [`735f7b40626a73cc31af.json`](../../sessions/73/735f7b40626a73cc31af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/evaluation/eval_code_status.md`。总结：

- **eval_pipeline.py** 和 **compare_results.py** 均已存在，功能完整，无需新建
- **adaptive 方法已实现**：`pretrain_weighted.py` 支持 `--weighting_method adaptive`，通过 `weighting/alpha_eff.py` 的 `find_optimal_b` 计算 batch-adaptive b*
- **训练缺口**：3 个 uniform checkpoint 已有，但 grid-b 只完成了 1/18（b=0.5/seed42），adaptive 0/3。评估前需先补齐训练

---
