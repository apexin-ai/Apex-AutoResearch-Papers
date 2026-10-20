# paper hyperparameter appendix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_hyperparameter-appendix_20260516T012050_result.json`
- **Structured JSON:** [`079099a605e4b46ce9f3.json`](../../sessions/07/079099a605e4b46ce9f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。在 `appendix.tex` 末尾添加了 `\section{Training Hyperparameters}` (L69-106)，包含完整的 4 列超参数表。所有数值均来自 registry 中的实际训练配置（`repo-level-cls-v5-conda`, `repo-level-cwm-v12`, `repo-level-cls-8b-conda`, `repo-level-cwm-8b-conda-v5`）。

注意事项：
- 4B CWM 的 `batch_size=1, grad_accum=32` 与 4B CLS 的 `batch_size=2, grad_accum=16` 不同（但 effective batch 都是 32）
- 8B CWM seed 只有 42（registry 中无 seed123 完整训练记录），已如实标注
- LoRA dropout 0.05 取自 `train_cwm_baseline.py` 默认值（registry spec 未单独记录此参数，但训练脚本一致）

---
