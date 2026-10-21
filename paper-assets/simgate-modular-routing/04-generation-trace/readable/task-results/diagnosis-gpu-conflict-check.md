# diagnosis gpu conflict check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_gpu-conflict-check_20260520T063233_result.json`
- **Structured JSON:** [`4424bc916e93a119beb7.json`](../../sessions/44/4424bc916e93a119beb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**无 GPU 冲突。** 两块 GPU 各跑一个 vLLM 进程，分配正常：

| GPU | PID | 显存占用 | 对应 session |
|-----|-----|---------|-------------|
| GPU 0 | 532172 | 20,330 MiB / 32,607 MiB | **gemma-gpu0** (Gemma 9B) |
| GPU 1 | 532006 | 20,588 MiB / 32,607 MiB | **gemma-gpu1** (Gemma 9B) |

**alfworld-llama-cross-model 已 crash。** 日志最后一行：
```
ERROR 05-20 14:30:39 Engine core proc EngineCore died unexpectedly, shutting down client.
```

时间线：alfworld-llama 在 14:11 启动，gemma-gpu0 在 14:30 启动抢占 GPU 0，alfworld-llama 的 vLLM EngineCore 在 14:30:39 被挤死。当前 GPU 0 上运行的是 gemma-gpu0 的 vLLM 进程。

---
