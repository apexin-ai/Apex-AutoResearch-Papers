# ops westb disk cleanup and prune retry

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-disk-cleanup-and-prune-retry_20260516T045217_result.json`
- **Structured JSON:** [`7e372dc4c3a84f84fea0.json`](../../sessions/7e/7e372dc4c3a84f84fea0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

**清理空间**：删除残缺 pruned_standard_25（9.6G）+ checkpoint-15（27G）+ checkpoint-25（27G），共释放 ~63G

**Standard 25% 剪枝**：成功
- 模型大小：11G（`model.safetensors` 11.6GB），与 RASP 25% 一致
- MLP groups pruned: 251/784，Attn GQA groups pruned: 0/112
- 实际稀疏度：23.96%（目标 25%）
- Forward pass 验证通过

**磁盘状态**：199G/250G（80%），剩余 52G

---
