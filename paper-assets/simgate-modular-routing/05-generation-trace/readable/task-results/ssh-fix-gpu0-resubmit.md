# ssh fix gpu0 resubmit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-gpu0-resubmit_20260513T221439_result.json`
- **Structured JSON:** [`694de81332f5bc773b06.json`](../../sessions/69/694de81332f5bc773b06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动正常。vLLM 已加载模型，正在运行 find-animal 的 episode 收集。

**总结：**
- 已 kill GPU 0 残留进程 741465（prescreening 的 vLLM 子进程，占 28GB）
- GPU 1 的 plan-001b-gpu1 (PID 774317) 未受影响
- plan-001b-gpu0 已重新提交（PID 794184），正在正常收集数据，当前在 find-animal episode 5

---
