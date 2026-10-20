# exp alfworld llama restart v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_alfworld-llama-restart-v2_20260520T083052_result.json`
- **Structured JSON:** [`a06c63ecc9e3769b8e03.json`](../../sessions/a0/a06c63ecc9e3769b8e03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ALFWorld Llama 已在 GPU 0 上成功重启，从第 69/135 episode 继续。

**关键操作**:
- 杀掉残留进程，备份 68 episodes 数据
- 给脚本加了 resume 逻辑（跳过已完成 task_id）
- 降低 `gpu_memory_utilization` 0.85→0.75 + `enforce_eager=True` 解决 vLLM v1 引擎 OOM
- tmux session `alfworld-v2`，剩余 67 episodes 处理中
- GPU 1 未受影响

---
