# ops check ste baseline

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_ste_baseline_20260515T192010_result.json`
- **Structured JSON:** [`87ed5ba5f9b5988245e8.json`](../../sessions/87/87ed5ba5f9b5988245e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**ste_baseline_s42 状态汇总：**

- **进程**：PID 116142 存活，已运行 ~3 分钟
- **GPU**：cuda:1 满载（100% utilization, 75185/97887 MiB）
- **训练进度**：Step 80/1000，KL loss 从 6.97 → 0.88，sparsity 0.449（lambda 正在上调以拉回 target 0.5）
- **Registry**：已从 PREPARING → RUNNING

训练曲线正常，loss 稳定下降。按之前同类实验 ~25-30 分钟完成 1000 步估算，约还需 ~25 分钟。

---
