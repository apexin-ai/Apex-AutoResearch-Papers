# ops commit full sgs bugfix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_commit-full-sgs-bugfix_20260515T233707_result.json`
- **Structured JSON:** [`0a536e1170a7a33d156e.json`](../../sessions/0a/0a536e1170a7a33d156e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

1. **git diff 确认的改动**：models.py L647-649 添加了 `requires_grad_(True)` 恢复逻辑——在 `ImagBehavior._train()` 的 `RequiresGrad` context manager 退出后，如果 `full_sgs=True` 且 `dt_emb_freeze=False`，将 `dt_embedding.weight` 重新设为可训练
2. **Commit hash**：`06ab285`
3. **包含文件**：`models.py`（1 file changed, 3 insertions）

configs.yaml 无 uncommitted 改动，`full_sgs` flag 已在之前的 commit 5fc8e49 中包含。exp_018 可以启动。

---
