# ssh mf4v2 s42 s123 v4

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mf4v2_s42_s123_v4_20260521T214520_result.json`
- **Structured JSON:** [`4142112d6fe52a3e84ff.json`](../../sessions/41/4142112d6fe52a3e84ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 状态：

| GPU | 状态 | 进程 |
|-----|------|------|
| cuda:0 | **空闲** (0 MiB) | — |
| cuda:1 | 占用 (30601 MiB, 92%) | VLLM::EngineCore PID 357933 |
| cuda:2 | 占用 (30551 MiB, 84%) | VLLM::EngineCore PID 358101 |
| cuda:3 | 占用 (30295 MiB, 83%) | VLLM::EngineCore PID 346917 |

**cuda:1 被 vLLM 进程占用，无法提交 seed=123。** 只有 cuda:0 可用。

两个选择：
1. 先提交 seed=42 到 cuda:0，seed=123 等 GPU 释放后再跑
2. 如果 cuda:1 上的 vLLM 进程可以终止，我先 kill 再提交两个

怎么处理？

---
