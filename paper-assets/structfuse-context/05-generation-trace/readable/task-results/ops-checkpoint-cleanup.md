# ops checkpoint cleanup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_checkpoint-cleanup_20260513T013416_result.json`
- **Structured JSON:** [`dd8241f5529a8a43d645.json`](../../sessions/dd/dd8241f5529a8a43d645.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

1. **清理前 checkpoints 各子目录大小**：checkpoints 目录已经是空的，无任何子目录（`p2b_*`、`tau_pilot*` 均不存在）
2. **清理后 checkpoints 残留情况**：无残留
3. **磁盘可用空间**：`/root/autodl-tmp/` 总 169G，已用 109G，可用 **61G**（64% 使用率）

MVP checkpoints 已被清理过，无需再次删除。

---
