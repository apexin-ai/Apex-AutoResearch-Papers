# ops westd disk cleanup grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-disk-cleanup-grpo_20260516T014658_result.json`
- **Structured JSON:** [`dc2d1f84b4949f3ea9e5.json`](../../sessions/dc/dc2d1f84b4949f3ea9e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 操作 | 释放空间 |
|------|---------|
| 删除 alpha_ablation/ (5个alpha实验) | ~58G |
| 删除 sft_ablation/ (4个alpha实验) | ~46G |
| **总计释放** | **~103G** |

**当前状态**: 110G used / 250G total，**141G 可用** (44%)。远超 50G 安全线，GRPO 训练可以放心启动。

---
