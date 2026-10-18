# ssh verify qwen3seed running

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_qwen3seed_running_20260515T195045_result.json`
- **Structured JSON:** [`5f75d9bddf6deb18f9b6.json`](../../sessions/5f/5f75d9bddf6deb18f9b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **正常运行中**，无需重新提交。

| 检查项 | 结果 |
|--------|------|
| PID 369205 | 存活，运行 02:23 |
| GPU 占用 | PID 369210 (子进程) 占用 17460 MiB |
| 日志进度 | `Running loglikelihood requests: 35% (18016/51065)` ~189 it/s |

tmux 命令被 read-only 拦截无法查，但进程和 GPU 占用都在，实验不依赖 tmux session 存活。清理 Worker 杀掉的只是 tmux session 壳，实际 python 进程未受影响。

---
