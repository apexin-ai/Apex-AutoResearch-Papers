# ssh westd cleanup and grpo 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_cleanup_and_grpo_25_20260521T024133_result.json`
- **Structured JSON:** [`f32ce5f81817f2ee352e.json`](../../sessions/f3/f32ce5f81817f2ee352e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 westd-29022 只有 **41GB free**。optimizer/scheduler 文件总共只有 ~304MB，远不够。

主要清理机会：v2 目录的 checkpoint-100 子目录与顶层 model.safetensors 重复（各 ~13G）。

**清理方案**（均为冗余数据）：

| 目标 | 大小 | 原因 |
|------|------|------|
| `grpo_cka_only_15_v2/checkpoint-100/` | ~13G | 顶层已有同一 model.safetensors |
| `grpo_standard_15_v2/checkpoint-100/` | ~13G | 同上 |
| `grpo_standard_15_seed123_v3/checkpoint-100/optimizer.pt` | 304M | 已完成，不需 resume |

预计释放 ~26G → 41+26 = **67GB free**，达标。

执行清理？

---
