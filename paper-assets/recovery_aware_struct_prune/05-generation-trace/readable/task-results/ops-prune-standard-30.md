# ops prune standard 30

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prune_standard_30_20260516T090533_result.json`
- **Structured JSON:** [`00dd2e1fe04cb9e0a3b6.json`](../../sessions/00/00dd2e1fe04cb9e0a3b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Standard 30% 剪枝完成。

**结果摘要：**
- Checkpoint: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30/`
- model.safetensors: 10.1GB, 339 keys
- 实际稀疏度: **28.54%**（目标 30%）
- MLP groups pruned: 299/784, Attn GQA groups pruned: 0/112
- 剪枝后参数量: 5,442,379,264
- 纯 CPU 执行，耗时约 25 秒（不含模型加载）

注意：模型实际路径是 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/`（不在 `models/` 子目录下）。

---
