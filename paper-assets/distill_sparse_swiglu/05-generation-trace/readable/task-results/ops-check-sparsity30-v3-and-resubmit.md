# ops check sparsity30 v3 and resubmit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_sparsity30_v3_and_resubmit_20260515T221247_result.json`
- **Structured JSON:** [`80e8f9d512f1441f0e61.json`](../../sessions/80/80e8f9d512f1441f0e61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正在运行：模型已加载，数据集已找到（wikitext-2-raw-v1 cached）。

**汇总：**
- **训练 kl_sparsity30_s42_v3**：已完成 1000 步，EXIT_CODE=0
  - 最终 sparsity=0.285（目标 0.30，lambda_max=5000 vs v2 的 0.281 改善有限）
  - loss=0.165, constraint=0, tau=0.1
- **Registry**：已更新为 DONE/success，metrics 已写入
- **Eval**：PID 148805 在 cuda:0 上运行中，加载 llama-3.1-8b + wikitext-2 评估

---
