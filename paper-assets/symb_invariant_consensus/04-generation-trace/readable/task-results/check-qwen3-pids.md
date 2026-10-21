# check qwen3 pids

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen3-pids_20260524T015138_result.json`
- **Structured JSON:** [`5fe34af6b7ddf9a56a5c.json`](../../sessions/5f/5fe34af6b7ddf9a56a5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验进程和对应的 vLLM 服务均在运行：

```
seed123 (port 8020, GPU 0): PID=804112
seed456 (port 8021, GPU 2): PID=804114
seed789 (port 8022, GPU 3): PID=804116
```

vLLM 服务进程：
- port 8020: PID=801558
- port 8021: PID=801559
- port 8022: PID=801560

所有进程从 02:07 开始运行，已运行约 8 小时。

---
