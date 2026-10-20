# code asb write

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_asb_write_20260520T162800_result.json`
- **Structured JSON:** [`c3d1a3cdc5993e019a81.json`](../../sessions/c3/c3d1a3cdc5993e019a81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `artifacts/experiments/asb/run_asb.py`，语法正确。

**产出概要：**
- 5 个 Phase 完整实现：subsampling → instance features → optimal N labels → predictor 训练 (LR/RF/MLP, 5-fold CV) → budget-constrained evaluation
- 支持多数据集（逗号分隔 `--data_paths` / `--dataset_names`）
- 输出 `asb_results.json`（聚合结果）+ `instance_details_{dataset}.jsonl`（逐 instance 细节）
- 包含 oracle adaptive baseline 和 feature importance 分析
- **CPU-only 实验，不需要 GPU**

---
