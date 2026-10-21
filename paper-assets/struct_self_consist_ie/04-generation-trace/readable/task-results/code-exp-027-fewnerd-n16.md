# code exp 027 fewnerd n16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_027_fewnerd_n16_20260517T052936_result.json`
- **Structured JSON:** [`fbc6461a101cafdb3754.json`](../../sessions/fb/fbc6461a101cafdb3754.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成全部提交：

- **数据**: 从 Few-NERD test set (37648条) 随机采样 5000 条 (seed=42)，entity type 分布保持一致
- **推理**: 4 个 tmux session (`exp027_shard0` ~ `exp027_shard3`)，每个 1250 instances × 16 samples，分别绑定 GPU 0-3
- **模型**: `qwen3-8b-fewnerd-exp021-merged`
- **Registry**: `exp_027_fewnerd_n16` 已更新为 RUNNING

当前推理速度 ~70 it/s/GPU，预计 5-8 分钟全部完成。tmux session 名: `exp027_shard{0-3}`。

---
