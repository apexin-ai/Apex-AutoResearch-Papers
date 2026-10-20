# data proofwriter prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_proofwriter-prep_20260513T174438_result.json`
- **Structured JSON:** [`a094cd7663ec46844016.json`](../../sessions/a0/a094cd7663ec46844016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出文件和统计：

**产出文件：**
- `/root/solver-trace-ablation/scripts/prepare_data.py` — 数据处理脚本
- `/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl` — Phase 0 子集（100 条）
- `/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl` — 训练子集（500 条）

**数据来源：** `tasksource/folio`（1204 条全部带人工标注的 FOL），比 ProofWriter 更适合（ProofWriter 原始数据无 FOL 列）。

**Phase 0 (100 条)：**
- 平均前提数: 5.4
- Answer 分布: true=34, false=25, unknown=41
- Depth 分布: {0:5, 1:3, 2:47, 3:40, 5:5}

**Train (500 条)：**
- 平均前提数: 5.3
- Answer 分布: true=198, false=138, unknown=164
- Depth 分布: {0:24, 1:21, 2:243, 3:178, 5:34}

每条数据包含完整的 NL 前提/结论 + 对应 FOL formalization，可直接用于 ISR baseline 评估和 GRPO 训练。

---
