# ssh kill vllm 155544 5090c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-vllm-155544-5090c_20260520T070147_result.json`
- **Structured JSON:** [`9b665d7912454cb2fe99.json`](../../sessions/9b/9b665d7912454cb2fe99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 155544 已不存在。当前 GPU 2 被 PID **804667** 占用（30516 MiB），4 张卡都在跑 python 进程（PID 804665-804668），看起来是 14B 训练的 4-GPU 分布式任务。

**结论**：vLLM 残留进程已消失，GPU 2 目前被训练进程 804667 使用，不需要 kill。4 卡均正常工作。

---
