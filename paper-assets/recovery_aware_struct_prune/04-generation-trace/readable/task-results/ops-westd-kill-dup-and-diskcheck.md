# ops westd kill dup and diskcheck

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_kill_dup_and_diskcheck_20260517T193643_result.json`
- **Structured JSON:** [`291bbe6eb1753e793ccf.json`](../../sessions/29/291bbe6eb1753e793ccf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **PID kill**：44270 已成功终止（SIGTERM，无需 force kill）。PID 43911 仍在运行，正在执行 `eval_gsm8k.py` 评估 `pruned_rasp_30`。

2. **磁盘空间**：⚠️ **紧急** — `/root/autodl-tmp` 仅剩 **1.6GB**（750G 用了 749G，100%）。低于 2GB 阈值，需要立即清理空间，否则当前运行的评估任务写结果时可能失败。

3. **sft_cka_only_20 模型**：完整，共 12GB。包含 `model.safetensors`（12.3GB）、`config.json`、`tokenizer.json`、`tokenizer_config.json`、`generation_config.json`、`chat_template.jinja`、`training_args.bin`，文件齐全。

---
