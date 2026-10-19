# ssh jsd 30 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_jsd_30_s42_20260520T155111_result.json`
- **Structured JSON:** [`6a47e85754b2dffd4ae4.json`](../../sessions/6a/6a47e85754b2dffd4ae4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **前置检查**：cuda:0 空闲 (0 MiB / 97887 MiB)，`--loss_type jsd` 和 `--lambda_max` 均支持，checkpoint 命名 `predictor_jsd.pt` 确认正确
- **训练已启动**：PID 226464，tmux session `jsd_30_s42`，日志 `~/runs/distill_sparse_swiglu/jsd_30_s42.log`
- **Registry**：`jsd_30_s42` → RUNNING，hypothesis 已填写

训练完成后会自动链式执行 7 任务 eval (wikitext2, arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa)。

---
