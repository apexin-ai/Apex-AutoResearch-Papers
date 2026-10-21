# ssh n32v2 gpu cleanup resubmit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n32v2_gpu_cleanup_resubmit_20260522T155045_result.json`
- **Structured JSON:** [`49e8ffac7fad41b208b0.json`](../../sessions/49/49e8ffac7fad41b208b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动。

**汇报：**
- **孤儿进程**：无需清理，cuda:3 在诊断时已空闲
- **额外修复**：模型路径从 `/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct`（不存在）改为 `/root/autodl-tmp/models/Qwen2.5-7B-Instruct`；sampling.py line 686 补了 `errors='replace'`
- **新进程**：PID 155692 (VLLM::EngineCore)，占用 cuda:3 15380MiB / 32607MiB
- **状态**：模型加载完成（14.25 GiB，6.4s），正在编译 torch kernels，即将开始推理

---
