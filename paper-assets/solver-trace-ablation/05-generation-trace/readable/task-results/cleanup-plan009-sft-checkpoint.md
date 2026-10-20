# cleanup plan009 sft checkpoint

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_plan009-sft-checkpoint_20260514T142538_result.json`
- **Structured JSON:** [`ece484924218030be4a5.json`](../../sessions/ec/ece484924218030be4a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

- **删除**: `checkpoint-500/` 整个目录（~23GB，含 15GB optimizer.pt + 模型副本）
- **保留**: eval_results.json、模型文件、tokenizer、config 等全部在上级目录
- **磁盘**: `/root/autodl-tmp/` 从 48% 使用率，可用 131GB

---
