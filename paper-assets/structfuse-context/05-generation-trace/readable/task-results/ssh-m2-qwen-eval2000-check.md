# ssh m2 qwen eval2000 check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m2_qwen_eval2000_check_20260514T014332_result.json`
- **Structured JSON:** [`78936440fe26cf4f5f5d.json`](../../sessions/78/78936440fe26cf4f5f5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval@2000 还没出。** 日志最后一行是 `step 2000 loss=0.0429`，训练刚到 step 2000，eval 还没触发。进程存活（PID 73558，已运行 8h4m），eval@2000 应该马上就会出。

最近一次 eval 是 **eval@1500**：val_loss=0.5365, R@1=0.5228（相比 eval@1000 有回退）。

eval@1000 仍是 best：**val_loss=0.4651, R@1=0.5527**

---

**StarCoder 进度**：当前在 step 1350，eval@1000 的 best 为 val_loss=0.6134, R@1=0.4537。落后 Qwen 约 10pp R@1。

---
