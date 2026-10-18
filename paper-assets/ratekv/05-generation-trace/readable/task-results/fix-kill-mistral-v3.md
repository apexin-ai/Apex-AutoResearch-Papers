# fix kill mistral v3

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_mistral_v3_20260514T214017_result.json`
- **Structured JSON:** [`c3a6d43db4c0d0925720.json`](../../sessions/c3/c3a6d43db4c0d0925720.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v3 已 kill，v4 正常运行：

- **PID 264489** 存活，tmux session `mistral_hires_bf16_2bitonly_v4` 正常
- GPU 1 上 python 进程 (PID 264494) 占用 ~18GB 显存，正在跑实验
- GPU 0 上另一个进程 (PID 258952, ~23.5GB) 不受影响

---
