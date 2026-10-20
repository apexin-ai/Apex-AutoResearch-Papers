# analysis quick gpu registry check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_quick_gpu_registry_check_20260519T013128_result.json`
- **Structured JSON:** [`e482fb04fc21d09cb22b.json`](../../sessions/e4/e482fb04fc21d09cb22b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
cuda:0: PID=476966 95479MiB/97887MiB 97%
cuda:1: 空闲       0MiB/97887MiB  0%

tmux: codellama13b_full_trace_tail512_seed42 (running)

Registry:
  seed42:  未找到
  seed456: 未找到
```

GPU0 正在跑 seed42 训练（PID 476966，显存几乎满，利用率 97%），GPU1 空闲。两个实验名在 registry 中都不存在——可能未注册或名称不同。需要我查一下 registry 里实际有哪些实验吗？

---
