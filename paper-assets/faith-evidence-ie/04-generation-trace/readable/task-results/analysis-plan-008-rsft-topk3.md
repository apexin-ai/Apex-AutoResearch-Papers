# analysis plan 008 rsft topk3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_008_rsft_topk3_20260515T210752_result.json`
- **Structured JSON:** [`d53c37a381d8598fe3a9.json`](../../sessions/d5/d53c37a381d8598fe3a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行中，已加载模型并开始推理（985 docs, 62 batches）。

---

**训练 metrics 摘要（plan_008_rsft_topk3）：**

| 指标 | 值 |
|------|-----|
| train_loss | 0.5543 |
| eval_loss | 0.8297 |
| token_accuracy | 82.28% |
| 训练时长 | 3h02m (1509 steps, 3 epochs) |
| RSFT 样本 | 8037 条 (CED mean=0.621) |
| GPU hours | 3.11h |

训练曲线正常：loss 从 ~0.6+ 稳步下降到 0.554，无异常波动。

**Eval 提交状态：**
- 实验 ID: `eval_plan_008_rsft_topk3`
- PID: **255523**
- GPU: cuda:3 @ rtx5090-4x
- 日志: `~/runs/faith-evidence-ie/eval_plan_008_rsft_topk3.log`
- 已在推理中（985 docs, batch_size=16, 62 batches）

---
