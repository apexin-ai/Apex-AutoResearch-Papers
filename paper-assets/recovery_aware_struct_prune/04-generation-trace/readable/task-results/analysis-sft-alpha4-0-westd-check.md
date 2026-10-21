# analysis sft alpha4 0 westd check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_alpha4_0_westd_check_20260515T124110_result.json`
- **Structured JSON:** [`b4f3c6fa9aa3b6f4f256.json`](../../sessions/b4/b4f3c6fa9aa3b6f4f256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果：训练失败

**`sft_alpha4_0_westd`** 在 step 935/1870（epoch 1 结束）崩溃。

**原因**：checkpoint 保存时 model shards 写入成功，但 optimizer state（~12GB）序列化失败 — `RuntimeError: basic_ios::clear: iostream error`。磁盘空间充足（数据盘 115GB 可用，根分区 24GB 可用），大概率是 PyTorch `torch.save` 处理超大 optimizer state 时的序列化 bug。

**最后指标**（step 930, epoch ≈ 1.0）：loss=0.8029, token_accuracy=0.7979

**无 checkpoint 留存**，alpha_4.0 目录为空。

**已完成**：registry 标记 DONE/failed，cron 已删除。

**重跑建议**：在训练脚本中加 `save_safetensors=True` + `save_optimizer=False`（如果 Trainer 支持），或用 `save_total_limit=1` 减小 checkpoint 体积，绕过 optimizer state 序列化问题。

---
