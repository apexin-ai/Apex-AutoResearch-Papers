# ssh cleanup westb disk for seed456

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup_westb_disk_for_seed456_20260522T142637_result.json`
- **Structured JSON:** [`0f5491f509b5bdfc548e.json`](../../sessions/0f/0f5491f509b5bdfc548e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 使用率 | 94% (233G/250G) | 88% (218G/250G) |
| 可用空间 | 18G | **33G** |
| 释放量 | — | **~15G** |

删除内容：
1. `grpo_qwen_math_cka_only_20/checkpoint-100/optimizer.pt` — 15GB（模型权重不受影响，仅 resume 训练需要）
2. `grpo_random_20/` — 220K（旧 killed 实验残留）

33G 可用，seed456 checkpoint (~12GB) 保存空间充足。

---
