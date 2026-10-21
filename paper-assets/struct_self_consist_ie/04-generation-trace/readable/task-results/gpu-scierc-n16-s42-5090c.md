# gpu scierc n16 s42 5090c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_scierc_n16_s42_5090c_20260521T113131_result.json`
- **Structured JSON:** [`0feb3daf984873bfb006.json`](../../sessions/0f/0feb3daf984873bfb006.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:1 不空闲，停止提交。**

当前状态：
- **GPU 1**: 92% 利用率，30145MiB / 32607MiB 已占用
- **进程**: `VLLM::EngineCore` (PID 311995) 正在 cuda:1 上运行，占用 30136MiB

cuda:1 上有 vLLM 引擎在跑，无法启动 SciERC N=16 实验。请确认：
1. 该 vLLM 进程是否可以终止？
2. 或者改用其他 GPU / 其他服务器？

---
