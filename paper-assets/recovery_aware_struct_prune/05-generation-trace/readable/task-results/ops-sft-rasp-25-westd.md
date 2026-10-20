# ops sft rasp 25 westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sft-rasp-25-westd_20260516T052045_result.json`
- **Structured JSON:** [`17aa47156598a7e282c9.json`](../../sessions/17/17aa47156598a7e282c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘空间不足，需要清理才能启动。**

当前状态：
- westd `/root/autodl-tmp/` 仅剩 **18GB**，需要 ~23GB（11GB model + 12GB SFT output）
- `grpo_unpruned_v2` 占 **110GB**，其中 3 个 checkpoint 各 32GB

建议：删除 `grpo_unpruned_v2/checkpoint-90` 和 `checkpoint-95`（共 64GB），保留 checkpoint-100 和最终模型。

是否可以删除这两个旧 checkpoint？

---
